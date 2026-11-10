#!/usr/bin/env python3
"""Generate readable release materials from results/outcomes_scored.csv.

The case-level CSV is the single input for released labels. This tool does not
execute samples, reconstruct event traces, or change any outcome. --check checks
the generated files without writing them.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (ENVIRONMENTS, ENVIRONMENT_ORDER, LAYER1_ORDER,
                    LAYER2_ORDER, LEVELS, LEVEL_NAMES, PAYLOADS, PAYLOAD_ORDER,
                    PRODUCTS, PRODUCT_ORDER, RESULTS_DIR, TECHNIQUES,
                    TECHNIQUE_ORDER, case_id, enumerate_cases, read_csv, write_csv)

SOURCE = RESULTS_DIR / 'outcomes_scored.csv'
OUTCOMES = {
    'L1': 'The product blocked the sample before process creation.',
    'L2': 'The process ran, but the product terminated it before C2 establishment within the 60-second timeout.',
    'L3': 'C2 was established, but the product terminated the session before any command was sent.',
    'L4': 'Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window.',
    'L5': 'The prescribed commands completed successfully and the session remained alive throughout the post-command observation window.',
}

def load_cases():
    rows = read_csv(SOURCE)
    matrix = enumerate_cases() + enumerate_cases(baseline=True)
    expected = {r['case_id']: r for r in matrix}
    if len(rows) != 828 or len({r['case_id'] for r in rows}) != 828 or set(expected) != {r['case_id'] for r in rows}:
        raise ValueError('Expected every one of the 828 cases exactly once')
    for r in rows:
        e = expected[r['case_id']]
        for field in ['technique_id', 'technique_name', 'payload_family', 'product', 'environment', 'layer1', 'layer2']:
            if r[field] != str(e[field]):
                raise ValueError(f'{r["case_id"]}: inconsistent {field}')
        if r['level'] not in LEVELS or r['level_name'] != LEVEL_NAMES[r['level']]:
            raise ValueError(f'{r["case_id"]}: invalid level')
        r['is_baseline'] = r['is_baseline'].lower() == 'true'
        if r['is_baseline'] != e['is_baseline'] or (r['is_baseline'] and r['level'] != 'L1'):
            raise ValueError(f'{r["case_id"]}: invalid baseline')
    return sorted(rows, key=lambda r: (int(r['technique_id'][1:]), PRODUCT_ORDER.index(r['product']), ENVIRONMENT_ORDER.index(r['environment']), PAYLOAD_ORDER.index(r['payload_family'])))

def table(headers, rows):
    def cell(x):return str(x).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join(['| '+' | '.join(headers)+' |', '| '+' | '.join(['---']*len(headers))+' |'] + ['| '+' | '.join(map(cell,r))+' |' for r in rows])

def counts(rows):
    c=Counter(r['level'] for r in rows)
    return [c[l] for l in LEVELS]

def pct(n,d):return f'{100*n/d:.1f}%'

def summary(rows):
    v=counts(rows)
    return [len(rows),*v,*[pct(n,len(rows)) for n in v]]

def render(rows):
    non=[r for r in rows if not r['is_baseline']]
    headers=['Group','Cases',*LEVELS,*[f'{l} %' for l in LEVELS]]
    sections=['# Complete Final Results','',
      'All 828 final case labels follow the manuscript result table: 792 non-baseline cases and 36 T0 cases. The canonical machine-readable dataset is [outcomes_scored.csv](outcomes_scored.csv). This file and [CASE_SUMMARIES.md](CASE_SUMMARIES.md) are generated from that dataset; both use the repository case identifiers.','',
      '## Outcome definitions','',table(['Level','Meaning','Criterion'],[[l,LEVEL_NAMES[l],OUTCOMES[l]] for l in LEVELS]),'',
      'T0 uses the same AES-based encryption and runtime decryption, with no additional evasion mechanism. Every case contributes one final label after the repetition procedure. T0 is excluded from PSD and BDD. See [the test protocol](../framework/TEST_PROTOCOL.md) and [data dictionary](DATA_DICTIONARY.md).','',
      '## Totals','',table(['Item','Count'],[['All cases',len(rows)],['Non-baseline cases',len(non)],['T0 cases',36],['Non-baseline L5 cases',counts(non)[4]],['Overall L5 proportion',pct(counts(non)[4],len(non))]]),'',
      '## Product summary (PSD)','',table(headers,[[p,*summary([r for r in non if r['product']==p])] for p in PRODUCT_ORDER]),'',
      '## Implementation summary (BDD)','',table(headers,[[t,*summary([r for r in non if r['technique_id']==t])] for t in TECHNIQUE_ORDER]),'',
      '## DET membership','',table(['Strategy','Stage','Implementations'],[[s,next(TECHNIQUES[t]['layer1'] for t in TECHNIQUE_ORDER if TECHNIQUES[t]['layer2']==s),', '.join(t for t in TECHNIQUE_ORDER if TECHNIQUES[t]['layer2']==s)] for s in LAYER2_ORDER]),'',
      '## Layer 2 BDD','',table(headers,[[s,*summary([r for r in non if r['layer2']==s])] for s in LAYER2_ORDER]),'',
      '## Layer 1 BDD','',table(headers,[[s,*summary([r for r in non if r['layer1']==s])] for s in LAYER1_ORDER]),'',
      '## Payload summary','',table(headers,[[p,*summary([r for r in non if r['payload_family']==p])] for p in PAYLOAD_ORDER]),'',
      '## Environment summary','',table(headers,[[e,*summary([r for r in non if r['environment']==e])] for e in ENVIRONMENT_ORDER]),'',
      '## Complete case register','',table(['Case ID','Implementation','Name','Payload','Product','Environment','Baseline','Level'],[[r['case_id'],r['technique_id'],r['technique_name'],r['payload_family'],r['product'],r['environment'],'Yes' if r['is_baseline'] else 'No',r['level']] for r in rows]),'',
      '## Calculation and provenance','',
      'PSD normalizes level counts by the number of non-baseline cases for a product (132). BDD normalizes by the cases for an implementation (36) or a DET group (36 times its number of implementations). Percentages are rounded to one decimal place. Run `python framework/tools/export_results.py` and `python framework/metrics.py` from the repository root. The manuscript is the authority for the labels; original screenshots and full logs are retained internally. [PROVENANCE.json](PROVENANCE.json) records the source-table and dataset fingerprints.','']
    cases=['# Test Case Summaries','',
      'These descriptions state the final outcomes of the completed experiments using the manuscript L1-L5 criteria. All 828 labels match [outcomes_scored.csv](outcomes_scored.csv) and [FINAL_RESULTS.md](FINAL_RESULTS.md). Original screenshots, full logs and infrastructure identifiers are not included. See [the test protocol](../framework/TEST_PROTOCOL.md).','']
    for t in ['T0',*TECHNIQUE_ORDER]:
        name=next(r['technique_name'] for r in rows if r['technique_id']==t)
        cases += [f'## {t}. {name}','']
        for p in PRODUCT_ORDER:
            for e in ENVIRONMENT_ORDER:
                group=[r for r in rows if r['technique_id']==t and r['product']==p and r['environment']==e]
                cases += [f'### {t}: {p} / {e}','',table(['Case ID','Payload','Final level','Reported final outcome'],[[r['case_id'],r['payload_family'],r['level'],OUTCOMES[r['level']]] for r in group]),'']
    aggregates={}
    aggregates['technique_level.csv']=(['technique_id','technique_name','layer1','layer2','n',*LEVELS,'l5_rate'],[])
    for t in TECHNIQUE_ORDER:
        sub=[r for r in non if r['technique_id']==t];v=counts(sub);spec=TECHNIQUES[t]
        aggregates['technique_level.csv'][1].append(dict(technique_id=t,technique_name=spec['name'],layer1=spec['layer1'],layer2=spec['layer2'],n=len(sub),**dict(zip(LEVELS,v)),l5_rate=round(v[4]/len(sub),4)))
    for name,key,order in [('by_product.csv','product',PRODUCT_ORDER),('by_payload.csv','payload_family',PAYLOAD_ORDER)]:
        data=[]
        for t in TECHNIQUE_ORDER:
            for g in order:
                sub=[r for r in non if r['technique_id']==t and r[key]==g]
                data.append({'technique_id':t,key:g,'n':len(sub),'n_l5':counts(sub)[4]})
        aggregates[name]=(['technique_id',key,'n','n_l5'],data)
    return {'FINAL_RESULTS.md':'\n'.join(sections),'CASE_SUMMARIES.md':'\n'.join(cases)},aggregates

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',action='store_true',help='check exports without writing')
    args=ap.parse_args();rows=load_cases();documents,aggregates=render(rows)
    failures=[]
    for name,content in documents.items():
        path=RESULTS_DIR/name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=content:failures.append(name)
        else:path.write_text(content,encoding='utf-8')
    for name,(fields,data) in aggregates.items():
        path=RESULTS_DIR/name
        if args.check:
            expected=[{k:str(v) for k,v in r.items()} for r in data]
            if not path.exists() or read_csv(path)!=expected:failures.append(name)
        else:write_csv(path,fields,data)
    provenance=RESULTS_DIR/'PROVENANCE.json'
    if provenance.exists():
        meta=json.loads(provenance.read_text(encoding='utf-8'))
        actual=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        if meta.get('dataset_sha256')!=actual:failures.append('PROVENANCE.json dataset fingerprint')
    if failures:
        print('Out-of-date exports: '+', '.join(failures));return 1
    print(f'{"Checked" if args.check else "Exported"} 828 case labels, 276 case records, and case-derived summaries.');return 0

if __name__=='__main__':raise SystemExit(main())
