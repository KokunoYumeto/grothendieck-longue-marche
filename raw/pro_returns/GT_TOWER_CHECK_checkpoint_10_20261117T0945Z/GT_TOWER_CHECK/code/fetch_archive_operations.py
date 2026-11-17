#!/usr/bin/env python3
"""Read selected official archive pages with HTTP byte ranges.

The source scans are reading material and are not part of the deliverable.
This script records the exact URL, page indices and source length.
"""
from pathlib import Path
import io,json,urllib.request,time
from pypdf import PdfReader,PdfWriter

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'work/root_sources'
OUT.mkdir(parents=True,exist_ok=True)
CACHE=OUT/'cote148_ranges'
CACHE.mkdir(exist_ok=True)
URL='https://grothendieck.umontpellier.fr/148.pdf'
LENGTH=35287128

class RangeReader(io.RawIOBase):
    def __init__(self):
        self.pos=0
        self.cache={}
        self.block=131072
        self.total=0
    def readable(self):return True
    def seekable(self):return True
    def tell(self):return self.pos
    def seek(self,offset,whence=0):
        self.pos=offset if whence==0 else self.pos+offset if whence==1 else LENGTH+offset
        return self.pos
    def read(self,size=-1):
        end=LENGTH if size<0 else min(LENGTH,self.pos+size)
        parts=[]
        while self.pos<end:
            k=self.pos//self.block
            if k not in self.cache:
                a=k*self.block;b=min(LENGTH,a+self.block)-1
                req=urllib.request.Request(URL,headers={'Range':f'bytes={a}-{b}'})
                cp=CACHE/f'{a}-{b}.bin'
                if cp.exists():data=cp.read_bytes()
                else:
                    for attempt in range(4):
                        try:
                            with urllib.request.urlopen(req,timeout=30) as r:
                                assert r.status==206,(r.status,r.headers)
                                data=r.read()
                            cp.write_bytes(data)
                            break
                        except Exception as e:
                            print('Range retry',a,attempt+1,type(e).__name__,flush=True)
                            if attempt==3:raise
                            time.sleep(1)
                assert len(data)==b-a+1
                self.cache[k]=data;self.total+=len(data)
                print('Fetched range',a,b,flush=True)
            data=self.cache[k];start=self.pos-k*self.block
            n=min(end-self.pos,len(data)-start)
            parts.append(data[start:start+n]);self.pos+=n
        return b''.join(parts)

r=RangeReader();doc=PdfReader(r)
print('Source PDF pages',len(doc.pages),flush=True)
pages=[51,52,53,54,55,56]
w=PdfWriter()
for i in pages:w.add_page(doc.pages[i])
target=OUT/'cote148_selected_52_57.pdf'
with target.open('wb') as f:w.write(f)
record={'url':URL,'source_bytes':LENGTH,'source_pages':len(doc.pages),
        'zero_based_page_indices':pages,'bytes_read':r.total,
        'selected_pdf_bytes':target.stat().st_size}
print(json.dumps(record,indent=2),flush=True)
(ROOT/'GT_TOWER_CHECK/notes/archive_page_fetch_52_57.json').write_text(json.dumps(record,indent=2)+'\n')
