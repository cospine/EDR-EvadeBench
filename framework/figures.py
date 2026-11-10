#!/usr/bin/env python3
"""Render data-equivalent result figures as standalone SVG.

Produces:

* ``fig5_bdd_layer2.svg`` -- Bypass Depth Distribution of the six Layer 2 DET
  strategies (paper Figure 5). Requires ``results/metrics/bdd_layer2.csv``.
* ``fig4_psd.svg``        -- Prevention Stage Distribution per product (paper
  Figure 4). Requires case-level outcomes; skipped with a message otherwise,
  because the released per-product data records only L5 counts.
* ``fig6_prevention_by_stage.svg`` -- six radar panels showing prevention rates
  across the three Layer 1 stages (paper Figure 6).

Design notes
------------
The five outcome levels are an **ordinal** scale (early prevention through
operational success), so they use a single-hue sequential ramp rather than
five categorical hues. Both mode ramps below were validated with the
data-viz validator (``--ordinal``) against their own surface:

    light  #86b6ef #5598e7 #2a78d6 #1c5cab #0d366b   (surface #fcfcfb)  PASS
    dark   #9ec5f4 #6da7ec #3987e5 #256abf #184f95   (surface #1a1a19)  PASS

Worst adjacent hue spread is under 5 degrees in both modes, so the ramp reads
as one ordered family. A legend is always present; segments carry a 2px
surface gap; the outer end of each bar is rounded (4px); only L5 -- the
primary endpoint -- is direct-labelled, so there is no number on every segment.
The accompanying CSV written by ``metrics.py`` is the table view.

Usage
-----
    python framework/figures.py
    python framework/figures.py --outdir results/figures/generated
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import LAYER1_ORDER, LEVELS, PRODUCT_ORDER, read_csv  # noqa: E402

METRICS_DIR = Path(__file__).resolve().parent.parent / "results" / "metrics"

LEVEL_SHORT = {
    "L1": "L1 Pre-execution",
    "L2": "L2 Pre-C2",
    "L3": "L3 Pre-command",
    "L4": "L4 Command-stage",
    "L5": "L5 Operational Success",
}

#: Ordinal ramp per mode: light -> dark, one hue (blue).
RAMP_LIGHT = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#0d366b"]
RAMP_DARK = ["#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95"]

#: Figure 6 radar fill plus two reserved categorical slots.
SERIES_LIGHT = ["#2a78d6", "#eb6834", "#1baf7a"]
SERIES_DARK = ["#3987e5", "#d95926", "#199e70"]

STAGE_LABEL = {
    "Collection": "Collection",
    "Transmission": "Transmission",
    "Detection": "Detection",
}

CSS = """
  .surface   { fill: var(--surface); }
  .ink       { fill: var(--ink); }
  .ink-2     { fill: var(--ink-2); }
  .muted     { fill: var(--muted); }
  .grid      { stroke: var(--grid); stroke-width: 1; }
  .axis      { stroke: var(--axis); stroke-width: 1; }
  text       { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }
  .title     { font-size: 17px; font-weight: 600; }
  .subtitle  { font-size: 12.5px; }
  .row-label { font-size: 12.5px; }
  .tick      { font-size: 11px; font-variant-numeric: tabular-nums; }
  .vlabel    { font-size: 12px; font-weight: 600; font-variant-numeric: tabular-nums; }
  .legend    { font-size: 11.5px; }
  .seg       { stroke: var(--surface); stroke-width: 2; }
"""

RADAR_CSS = """
<style>
  .radar-ring { fill: none; stroke: var(--grid); stroke-width: 1; }
  .radar-axis { stroke: var(--axis); stroke-width: 1; }
  .radar-area { fill: var(--s1); fill-opacity: 0.24; stroke: var(--s1); stroke-width: 2; }
  .radar-dot  { fill: var(--s1); stroke: var(--surface); stroke-width: 1.5; }
  .panel-title { font-size: 12.5px; font-weight: 600; }
</style>
"""


def _css_block() -> str:
    return (
        "<style>\n"
        "  .viz {\n"
        "    --surface: #fcfcfb; --ink: #0b0b0b; --ink-2: #52514e;\n"
        "    --muted: #898781; --grid: #e1e0d9; --axis: #c3c2b7;\n"
        f"    --l1: {RAMP_LIGHT[0]}; --l2: {RAMP_LIGHT[1]}; --l3: {RAMP_LIGHT[2]};\n"
        f"    --l4: {RAMP_LIGHT[3]}; --l5: {RAMP_LIGHT[4]};\n"
        f"    --s1: {SERIES_LIGHT[0]}; --s2: {SERIES_LIGHT[1]}; --s3: {SERIES_LIGHT[2]};\n"
        "  }\n"
        "  @media (prefers-color-scheme: dark) {\n"
        "    .viz {\n"
        "      --surface: #1a1a19; --ink: #ffffff; --ink-2: #c3c2b7;\n"
        "      --muted: #898781; --grid: #2c2c2a; --axis: #383835;\n"
        f"      --l1: {RAMP_DARK[0]}; --l2: {RAMP_DARK[1]}; --l3: {RAMP_DARK[2]};\n"
        f"      --l4: {RAMP_DARK[3]}; --l5: {RAMP_DARK[4]};\n"
        f"      --s1: {SERIES_DARK[0]}; --s2: {SERIES_DARK[1]}; --s3: {SERIES_DARK[2]};\n"
        "    }\n"
        "  }\n"
        + CSS
        + "</style>"
    )


def _right_rounded_path(x0: float, y: float, w: float, h: float, r: float = 4.0) -> str:
    r = max(0.0, min(r, h / 2, w))
    x1 = x0 + w
    if r == 0:
        return f"M {x0},{y} H {x1} V {y + h} H {x0} Z"
    return (f"M {x0},{y} H {x1 - r} A {r},{r} 0 0 1 {x1},{y + r} "
            f"V {y + h - r} A {r},{r} 0 0 1 {x1 - r},{y + h} H {x0} Z")


def stacked_bdd_svg(title: str, subtitle: str, rows: list[dict], group_key: str,
                    width: int = 940) -> str:
    """Horizontal stacked bars over the five ordinal levels."""
    gutter_l, gutter_r = 250, 130
    top, bottom = 96, 74
    row_h, row_gap = 30, 12
    plot_w = width - gutter_l - gutter_r
    height = top + len(rows) * (row_h + row_gap) + bottom

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d">',
        f"<title id='t'>{title}</title>",
        f"<desc id='d'>{subtitle} Values are also available as a CSV table.</desc>",
        _css_block(),
        '<rect class="viz surface" x="0" y="0" width="100%" height="100%"/>',
        '<g class="viz">',
        f'<text class="ink title" x="20" y="34">{title}</text>',
        f'<text class="ink-2 subtitle" x="20" y="55">{subtitle}</text>',
    ]

    # gridlines + x ticks
    y0, y1 = top - 10, top + len(rows) * (row_h + row_gap) - row_gap + 10
    for frac in (0, 25, 50, 75, 100):
        x = gutter_l + plot_w * frac / 100
        parts.append(f'<line class="grid" x1="{x:.1f}" y1="{y0}" x2="{x:.1f}" y2="{y1}"/>')
        parts.append(f'<text class="muted tick" x="{x:.1f}" y="{y1 + 20}" '
                     f'text-anchor="middle">{frac}%</text>')

    for i, row in enumerate(rows):
        y = top + i * (row_h + row_gap)
        parts.append(f'<text class="ink row-label" x="{gutter_l - 14}" y="{y + row_h / 2 + 4}" '
                     f'text-anchor="end">{row[group_key]}</text>')

        total_frac = 1.0
        parts.append(f'<clipPath id="clip{i}"><path d="'
                     f'{_right_rounded_path(gutter_l, y, plot_w * total_frac, row_h)}"/></clipPath>')

        cum = 0.0
        for j, lvl in enumerate(LEVELS):
            frac = float(row[lvl])
            w = plot_w * frac
            if w <= 0:
                cum += frac
                continue
            draw_w = w if j == len(LEVELS) - 1 else max(0.0, w - 2)
            parts.append(
                f'<rect class="seg" clip-path="url(#clip{i})" x="{gutter_l + plot_w * cum:.2f}" '
                f'y="{y}" width="{draw_w:.2f}" height="{row_h}" fill="var(--{lvl.lower()})"/>'
            )
            cum += frac

        l5 = float(row["L5"])
        parts.append(
            f'<text class="ink vlabel" x="{gutter_l + plot_w + 12}" y="{y + row_h / 2 + 4}">'
            f'{l5 * 100:.1f}%</text>'
        )

    # legend
    ly = height - 34
    lx = 20
    for lvl in LEVELS:
        parts.append(f'<rect x="{lx}" y="{ly - 9}" width="11" height="11" rx="2.5" '
                     f'fill="var(--{lvl.lower()})"/>')
        parts.append(f'<text class="ink-2 legend" x="{lx + 17}" y="{ly}">{LEVEL_SHORT[lvl]}</text>')
        lx += 19 + len(LEVEL_SHORT[lvl]) * 6.3
    parts.append(f'<text class="muted legend" x="{gutter_l + plot_w + 12}" y="{ly}">L5 rate</text>')
    parts.append("</g></svg>")
    return "\n".join(parts)


def _radar_point(cx: float, cy: float, radius: float, axis: int,
                 value: float = 1.0) -> tuple[float, float]:
    angle = math.radians(-90 + axis * 120)
    return cx + radius * value * math.cos(angle), cy + radius * value * math.sin(angle)


def _points(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in points)


def radar_small_multiples_svg(title: str, subtitle: str, products: list[str],
                              stages: list[str], values: dict[str, dict[str, float]],
                              width: int = 940) -> str:
    """Paper-style 2x3 radar panels, one for each evaluated product."""
    cols, rows = 3, 2
    top, bottom = 92, 42
    panel_w = width / cols
    panel_h = 250
    height = top + rows * panel_h + bottom
    radius = 72
    display_names = {
        "Sophos": "Sophos",
        "Kaspersky": "Kaspersky",
        "Bitdefender": "Bitdefender",
        "Elastic": "Elastic Security",
        "Huorong": "Huorong",
        "DefenderAV": "Microsoft Defender Antivirus",
    }

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d">',
        f"<title id='t'>{title}</title>",
        f"<desc id='d'>{subtitle} Values are also available as a CSV table.</desc>",
        _css_block(),
        RADAR_CSS,
        '<rect class="viz surface" x="0" y="0" width="100%" height="100%"/>',
        '<g class="viz">',
        f'<text class="ink title" x="20" y="34">{title}</text>',
        f'<text class="ink-2 subtitle" x="20" y="55">{subtitle}</text>',
    ]

    for index, product in enumerate(products):
        col, row = index % cols, index // cols
        cx = col * panel_w + panel_w / 2
        cy = top + row * panel_h + 96

        for fraction in (0.2, 0.4, 0.6, 0.8, 1.0):
            ring = [_radar_point(cx, cy, radius, axis, fraction) for axis in range(3)]
            parts.append(f'<polygon class="radar-ring" points="{_points(ring)}"/>')
        for axis in range(3):
            x, y = _radar_point(cx, cy, radius, axis)
            parts.append(f'<line class="radar-axis" x1="{cx:.2f}" y1="{cy:.2f}" '
                         f'x2="{x:.2f}" y2="{y:.2f}"/>')

        data = [_radar_point(cx, cy, radius, axis,
                             max(0.0, min(1.0, float(values[product].get(stage, 0.0)))))
                for axis, stage in enumerate(stages)]
        parts.append(f'<polygon class="radar-area" points="{_points(data)}"/>')
        for x, y in data:
            parts.append(f'<circle class="radar-dot" cx="{x:.2f}" cy="{y:.2f}" r="3.2"/>')

        for axis, stage in enumerate(stages):
            x, y = _radar_point(cx, cy, radius + 20, axis)
            anchor = "middle" if axis == 0 else ("start" if axis == 1 else "end")
            dy = -2 if axis == 0 else 5
            parts.append(f'<text class="ink-2 tick" x="{x:.2f}" y="{y + dy:.2f}" '
                         f'text-anchor="{anchor}">{STAGE_LABEL[stage]}</text>')

        panel_label = chr(ord("a") + index)
        parts.append(f'<text class="ink panel-title" x="{cx:.2f}" y="{cy + radius + 44:.2f}" '
                     f'text-anchor="middle">({panel_label}) {display_names[product]}</text>')

    legend_y = height - 16
    parts.append(f'<text class="muted legend" x="20" y="{legend_y}">'
                 "Rings: 20%, 40%, 60%, 80%, 100% prevention rate</text>")
    parts.append("</g></svg>")
    return "\n".join(parts)


def _check_geometry(rows: list[dict], name: str) -> None:
    for row in rows:
        total = sum(float(row[lvl]) for lvl in LEVELS)
        if abs(total - 1.0) > 0.005:
            print(f"[!] {name}: row '{row.get('group')}' sums to {total:.4f}, not 1.0")
        for lvl in LEVELS:
            if float(row[lvl]) < -1e-9:
                print(f"[!] {name}: negative proportion in '{row.get('group')}' {lvl}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Render data-equivalent result figures as SVG.")
    ap.add_argument("--outdir", type=Path, default=Path(__file__).resolve().parent.parent
                    / "results" / "figures" / "generated")
    ap.add_argument("--metrics", type=Path, default=METRICS_DIR)
    args = ap.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    wrote = 0

    # ---- Figure 5: BDD of the six Layer 2 strategies -------------------
    layer2 = args.metrics / "bdd_layer2.csv"
    if layer2.exists():
        rows = read_csv(layer2)
        _check_geometry(rows, "fig5")
        svg = stacked_bdd_svg(
            "Bypass Depth Distribution of the six Layer 2 DET strategies",
            "Share of outcomes at each prevention stage. Bars sum to 100%; "
            "L5 (Operational Success) is labelled at the right.",
            rows, "group")
        (args.outdir / "fig5_bdd_layer2.svg").write_text(svg, encoding="utf-8")
        print(f"[+] wrote {args.outdir / 'fig5_bdd_layer2.svg'}")
        wrote += 1
    else:
        print(f"[i] skipped Figure 5: {layer2} not found (run metrics.py first)")

    # ---- Figure 4: PSD per product (needs all five levels) -------------
    psd = args.metrics / "psd_by_product.csv"
    if psd.exists():
        rows = read_csv(psd)
        _check_geometry(rows, "fig4")
        svg = stacked_bdd_svg(
            "Prevention Stage Distribution (PSD) per product",
            "Share of each product's outcomes at each prevention stage, "
            "aggregated over 22 techniques, three payload families and two environments.",
            rows, "product")
        (args.outdir / "fig4_psd.svg").write_text(svg, encoding="utf-8")
        print(f"[+] wrote {args.outdir / 'fig4_psd.svg'}")
        wrote += 1
    else:
        print("[i] skipped Figure 4 (PSD): it needs all five per-product levels, which")
        print("    requires a case-level outcome matrix. Supply one with metrics.py --outcomes.")
        print(f"    Without them, metrics.py emits L5-only PSD at "
              f"{args.metrics / 'psd_by_product_l5_only.csv'}.")

    # ---- Figure 6: prevention rate per product per Layer 1 stage -------
    prev = args.metrics / "prevention_by_stage.csv"
    if prev.exists():
        rows = read_csv(prev)
        values: dict[str, dict[str, float]] = {}
        for r in rows:
            values.setdefault(r["product"], {})[r["stage"]] = float(r["prevention_rate"])
        stages = [s for s in LAYER1_ORDER if any(s in v for v in values.values())]
        groups = [p for p in PRODUCT_ORDER if p in values]
        svg = radar_small_multiples_svg(
            "Prevention rate across DET Matrix Layer 1 stages",
            "Proportion of each product's outcomes prevented from reaching L5 "
            "(Operational Success), per detection-lifecycle stage.",
            groups, stages, values)
        (args.outdir / "fig6_prevention_by_stage.svg").write_text(svg, encoding="utf-8")
        print(f"[+] wrote {args.outdir / 'fig6_prevention_by_stage.svg'}")
        wrote += 1
    else:
        print("[i] skipped Figure 6: it needs case-level outcomes (see Figure 4 above)")

    if not wrote:
        print("[!] no figures written")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
