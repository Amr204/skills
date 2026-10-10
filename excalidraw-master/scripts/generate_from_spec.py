#!/usr/bin/env python3
import argparse,json,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from excalidraw_builder import Diagram

PALETTE=[('#2563eb','#a5d8ff'),('#f59e0b','#ffd8a8'),('#8b5cf6','#d0bfff'),('#06b6d4','#99e9f2'),('#22c55e','#b2f2bb'),('#ec4899','#eebefa')]

def main():
    p=argparse.ArgumentParser(); p.add_argument('spec'); p.add_argument('output'); a=p.parse_args(); s=json.load(open(a.spec,encoding='utf-8'))
    d=Diagram(); d.text(40,30,s.get('title','Diagram'),28); y=100; nodes={}
    sections=s.get('sections',[])
    for si,sec in enumerate(sections):
        stroke,fill=PALETTE[si%len(PALETTE)]; d.text(40,y,sec.get('title',f'Section {si+1}'),22,stroke); y+=55; x=40
        for ni,n in enumerate(sec.get('nodes',[])):
            w=n.get('width',280); h=n.get('height',110); box=d.rect(x,y,w,h,stroke,fill,2,100,True,eid=n.get('id'))
            d.text(x+16,y+16,n.get('label',''),18,stroke,'center',box,width=w-32); nodes[box['id']]=box; x+=w+50
        y+=190
    for edge in s.get('edges',[]):
        A=nodes.get(edge.get('from')); B=nodes.get(edge.get('to'))
        if A and B:
            x1=A['x']+A['width']; y1=A['y']+A['height']/2; x2=B['x']; y2=B['y']+B['height']/2
            d.arrow(x1,y1,x2,y2,start=A,end=B,label=edge.get('label'))
    d.save(a.output)
if __name__=='__main__': main()
