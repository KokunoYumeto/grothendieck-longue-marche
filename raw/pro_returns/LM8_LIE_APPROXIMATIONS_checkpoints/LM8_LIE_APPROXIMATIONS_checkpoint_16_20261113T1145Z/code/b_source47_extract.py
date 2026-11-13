#!/usr/bin/env python3
"""Read selected original manuscript PDF pages using cached HTTP byte ranges.

This is a source-extraction utility, not a reconstruction of the manuscript.
It keeps original PDF page indices explicit in its extraction manifest.
"""
from pathlib import Path
import hashlib,io,json,time,urllib.request
from pypdf import PdfReader,PdfWriter
from pypdf._page import PageObject

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'source_checks'/'140-3'
CACHE=ROOT/'tmp'/'source_pdf_ranges'/'140-3'
URL='https://grothendieck.umontpellier.fr/140-3.pdf'
SIZE=205929342
BLOCK=262144
OUT.mkdir(parents=True,exist_ok=True)
CACHE.mkdir(parents=True,exist_ok=True)

class RemoteFile(io.RawIOBase):
    def __init__(self): self.pos=0; self.requests=0; self.fetched=0
    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.pos
    def seek(self,pos,whence=0):
        self.pos=pos if whence==0 else self.pos+pos if whence==1 else SIZE+pos
        if self.pos<0: raise ValueError('negative seek')
        return self.pos
    def block(self,i):
        file=CACHE/f'{i:05d}.bin'
        lo=i*BLOCK; hi=min(SIZE-1,lo+BLOCK-1)
        if file.exists():
            data=file.read_bytes()
            if len(data)==hi-lo+1:return data
        for trial in range(3):
            try:
                req=urllib.request.Request(URL,headers={'Range':f'bytes={lo}-{hi}','User-Agent':'Mozilla/5.0'})
                with urllib.request.urlopen(req,timeout=25) as r:
                    assert r.status==206,(r.status,dict(r.headers))
                    assert r.headers['Content-Range']==f'bytes {lo}-{hi}/{SIZE}',dict(r.headers)
                    data=r.read(hi-lo+1)
                assert len(data)==hi-lo+1,(len(data),lo,hi)
                file.write_bytes(data)
                self.requests+=1;self.fetched+=len(data)
                print(f'fetched block {i}, total {self.fetched} bytes',flush=True)
                return data
            except Exception as e:
                print('range retry',i,trial,repr(e),flush=True)
                if trial==2:raise
        raise RuntimeError('unreachable')
    def read(self,n=-1):
        if n<0:n=SIZE-self.pos
        end=min(SIZE,self.pos+n)
        chunks=[]
        while self.pos<end:
            i=self.pos//BLOCK; start=self.pos%BLOCK
            data=self.block(i); count=min(len(data)-start,end-self.pos)
            chunks.append(data[start:start+count]);self.pos+=count
        return b''.join(chunks)

def page_at(node,index):
    node=node.get_object()
    if node.get('/Type')=='/Page':
        assert index==0
        return node
    # If every child contributes one page, go directly to that child.
    # Resolving preceding leaf dictionaries would fetch needless images.
    if int(node['/Count'])==len(node['/Kids']):
        return page_at(node['/Kids'][index],0)
    for ref in node['/Kids']:
        child=ref.get_object()
        count=int(child.get('/Count',1))
        if index<count:return page_at(child,index)
        index-=count
    raise IndexError(index)

def main():
    stream=RemoteFile()
    # Non-strict pypdf validates every object offset and would fetch the
    # whole remote file. The publisher's xref is valid, so parse strictly.
    reader=PdfReader(stream,strict=True)
    tree=reader.trailer['/Root']['/Pages']
    print('total pages',tree['/Count'],'root kids',len(tree['/Kids']),flush=True)
    # Candidate original one-based pages include the requested scan range
    # and one page on either side; the first three establish front matter.
    wanted=[1,2,3]+list(range(228,242))
    manifest=[]
    for p in wanted:
        raw=page_at(tree,p-1)
        page=PageObject(reader,raw.indirect_reference)
        page.update(raw)
        writer=PdfWriter();writer.add_page(page)
        dest=OUT/f'pdfpage{p:03d}.pdf'
        with dest.open('wb') as f:writer.write(f)
        b=dest.read_bytes()
        manifest.append({'original_pdf_page_one_based':p,'original_pdf_page_zero_based':p-1,'lm2_scan_number':p if p>1 else None,'archive_printed_footer':p-1 if p>1 else None,'local_file':str(dest.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
        print('saved',p,len(b),flush=True)
    result={'source_url':URL,'source_pdf_bytes':SIZE,'source_pdf_pages':int(tree['/Count']),'source_last_modified':'2017-05-11T14:09:14Z','extraction':'Exact original selected pages; no OCR replacement','pagination':'LM2 scan k = physical one-based PDF page k; zero-based index and archive printed footer both k-1. Established by folio415 on physical229.','pages':manifest,'new_range_requests':stream.requests,'new_bytes_fetched':stream.fetched}
    (OUT/'extraction_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
    print('DONE',json.dumps({'requests':stream.requests,'fetched':stream.fetched}),flush=True)

if __name__=='__main__':main()
