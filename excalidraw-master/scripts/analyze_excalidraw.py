#!/usr/bin/env python3
import argparse,json,collections,sys

def analyze(path):
    d=json.load(open(path,encoding='utf-8')); es=d.get('elements',[]); active=[e for e in es if not e.get('isDeleted')]
    types=collections.Counter(e.get('type') for e in active)
    xs=[e.get('x',0) for e in active]; ys=[e.get('y',0) for e in active]
    x2=[e.get('x',0)+e.get('width',0) for e in active]; y2=[e.get('y',0)+e.get('height',0) for e in active]
    fonts=collections.Counter(e.get('fontSize') for e in active if e.get('type')=='text')
    strokes=collections.Counter(e.get('strokeColor') for e in active)
    longest=sorted([(len(e.get('text','')),e.get('id'),e.get('text','')[:100]) for e in active if e.get('type')=='text'],reverse=True)[:5]
    return {"type":d.get('type'),"version":d.get('version'),"elements":len(es),"active_elements":len(active),"types":dict(types),
            "files":len(d.get('files',{})),"bounds":None if not active else {"min_x":min(xs),"min_y":min(ys),"max_x":max(x2),"max_y":max(y2),"width":max(x2)-min(xs),"height":max(y2)-min(ys)},
            "font_sizes":dict(fonts),"top_stroke_colors":strokes.most_common(10),"longest_texts":longest}

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('file'); p.add_argument('--json',action='store_true'); a=p.parse_args(); r=analyze(a.file)
    if a.json: print(json.dumps(r,ensure_ascii=False,indent=2))
    else:
        print(f"Elements: {r['active_elements']} / {r['elements']}"); print('Types:',r['types']); print('Files:',r['files']); print('Bounds:',r['bounds']); print('Fonts:',r['font_sizes']); print('Colors:',r['top_stroke_colors'])
