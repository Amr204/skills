#!/usr/bin/env python3
import argparse,json,sys

def validate(path):
    errors=[]; warnings=[]
    try: d=json.load(open(path,encoding='utf-8'))
    except Exception as e: return [f'JSON parse error: {e}'],[]
    if d.get('type')!='excalidraw': errors.append("top-level type must be 'excalidraw'")
    if not isinstance(d.get('elements'),list): errors.append('elements must be a list'); return errors,warnings
    if not isinstance(d.get('files',{}),dict): errors.append('files must be an object')
    ids={};
    for i,e in enumerate(d['elements']):
        eid=e.get('id')
        if not eid: errors.append(f'element[{i}] missing id'); continue
        if eid in ids: errors.append(f'duplicate id: {eid}')
        ids[eid]=e
        for k in ('type','x','y','width','height'):
            if k not in e: errors.append(f'{eid} missing {k}')
    for eid,e in ids.items():
        for b in e.get('boundElements') or []:
            rid=b.get('id')
            if rid and rid not in ids: errors.append(f'{eid} boundElements references missing {rid}')
        cid=e.get('containerId')
        if cid and cid not in ids: errors.append(f'{eid} containerId references missing {cid}')
        for key in ('startBinding','endBinding'):
            b=e.get(key)
            if b and b.get('elementId') not in ids: errors.append(f"{eid} {key} references missing {b.get('elementId')}")
        if e.get('type')=='arrow':
            pts=e.get('points')
            if not isinstance(pts,list) or len(pts)<2: errors.append(f'{eid} arrow has invalid points')
        if e.get('type')=='text' and 'text' not in e: errors.append(f'{eid} text element missing text')
    return errors,warnings

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('file'); a=p.parse_args(); errors,warnings=validate(a.file)
    for w in warnings: print('WARNING:',w)
    for e in errors: print('ERROR:',e)
    if errors: print(f'FAIL: {len(errors)} error(s)'); sys.exit(1)
    print('OK: structural validation passed')
