#!/usr/bin/env python3
import json, random, time, math
from pathlib import Path

class Diagram:
    def __init__(self, source="excalidraw-master-skill"):
        self.elements=[]; self.files={}; self.source=source; self._n=0
    def _id(self,p="e"):
        self._n+=1; return f"{p}_{self._n}"
    def _base(self, typ, x,y,w,h, stroke="#1e1e1e", bg="transparent", sw=2, opacity=100, roundness=None, eid=None):
        now=int(time.time()*1000); eid=eid or self._id(typ[:1])
        return {"id":eid,"type":typ,"x":x,"y":y,"width":w,"height":h,"angle":0,
          "strokeColor":stroke,"backgroundColor":bg,"fillStyle":"solid","strokeWidth":sw,
          "strokeStyle":"solid","roughness":1,"opacity":opacity,"groupIds":[],"frameId":None,
          "roundness":roundness,"seed":random.randint(1,2_000_000_000),"version":1,
          "versionNonce":random.randint(1,2_000_000_000),"isDeleted":False,"boundElements":[],
          "updated":now,"link":None,"locked":False}
    def rect(self,x,y,w,h,stroke="#1e1e1e",bg="transparent",sw=2,opacity=100,rounded=True,eid=None):
        e=self._base("rectangle",x,y,w,h,stroke,bg,sw,opacity,{"type":3} if rounded else None,eid); self.elements.append(e); return e
    def ellipse(self,x,y,w,h,stroke="#1e1e1e",bg="transparent",sw=2,opacity=100,eid=None):
        e=self._base("ellipse",x,y,w,h,stroke,bg,sw,opacity,None,eid); self.elements.append(e); return e
    def diamond(self,x,y,w,h,stroke="#1e1e1e",bg="transparent",sw=2,opacity=100,eid=None):
        e=self._base("diamond",x,y,w,h,stroke,bg,sw,opacity,None,eid); self.elements.append(e); return e
    def text(self,x,y,text,size=16,color="#1e1e1e",align="left",container=None,eid=None,width=None):
        lines=text.splitlines() or [""]; est=max(len(s) for s in lines)*size*0.58
        w=width or max(20,est); h=max(size*1.25, len(lines)*size*1.25)
        e=self._base("text",x,y,w,h,color,"transparent",2,100,None,eid)
        e.update({"text":text,"fontSize":size,"fontFamily":5,"textAlign":align,"verticalAlign":"top" if not container else "middle",
                  "containerId":container["id"] if container else None,"originalText":text,"autoResize":True,"lineHeight":1.25})
        self.elements.append(e)
        if container:
            container.setdefault("boundElements",[]).append({"type":"text","id":e["id"]})
        return e
    def arrow(self,x1,y1,x2,y2,stroke="#1e1e1e",sw=2,dashed=False,start=None,end=None,label=None,eid=None):
        e=self._base("arrow",x1,y1,abs(x2-x1),abs(y2-y1),stroke,"transparent",sw,100,None,eid)
        e["points"]=[[0,0],[x2-x1,y2-y1]]; e["lastCommittedPoint"]=None
        e["startBinding"]={"elementId":start["id"],"mode":"orbit","fixedPoint":[0.5,0.5]} if start else None
        e["endBinding"]={"elementId":end["id"],"mode":"orbit","fixedPoint":[0.5,0.5]} if end else None
        e["startArrowhead"]=None; e["endArrowhead"]="arrow"; e["elbowed"]=False
        if dashed: e["strokeStyle"]="dashed"
        self.elements.append(e)
        for node in (start,end):
            if node: node.setdefault("boundElements",[]).append({"id":e["id"],"type":"arrow"})
        if label:
            mx=(x1+x2)/2; my=(y1+y2)/2-22; self.text(mx,my,label,14,color=stroke,align="center")
        return e
    def card(self,x,y,w,title,body,stroke="#2563eb",fill="#a5d8ff",header_h=54,body_h=150):
        h=self.rect(x,y,w,header_h,stroke,fill,2,100,True)
        self.text(x+16,y+14,title,18,stroke,"center",h,width=w-32)
        b=self.rect(x,y+header_h,w,body_h,stroke,fill,1,30,True)
        self.text(x+16,y+header_h+14,body,16,"#1e1e1e","left",None,width=w-32)
        return h,b
    def to_dict(self):
        return {"type":"excalidraw","version":2,"source":self.source,"elements":self.elements,
                "appState":{"gridSize":None,"viewBackgroundColor":"#ffffff"},"files":self.files}
    def save(self,path):
        Path(path).write_text(json.dumps(self.to_dict(),ensure_ascii=False,indent=2),encoding="utf-8")

if __name__=="__main__":
    d=Diagram(); d.text(40,30,"Example Diagram",28); a=d.rect(40,100,220,80,"#2563eb","#a5d8ff"); d.text(70,125,"Start",18,"#2563eb","center",a)
    b=d.rect(360,100,220,80,"#22c55e","#b2f2bb"); d.text(390,125,"Outcome",18,"#22c55e","center",b); d.arrow(260,140,360,140,start=a,end=b); d.save("example.excalidraw")
