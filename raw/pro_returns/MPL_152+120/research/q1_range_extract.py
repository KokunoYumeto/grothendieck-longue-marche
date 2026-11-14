from pathlib import Path
import io, urllib.request, re, time, sys, json
from pypdf import PdfReader,PdfWriter
from pypdf._page import PageObject
from pypdf.generic import NameObject
def urlopen_retry(req, timeout=35):
 for attempt in range(4):
  try:return urllib.request.urlopen(req,timeout=timeout)
  except Exception as e:
   if attempt==3:raise
   print('Retry',attempt+1,type(e).__name__,flush=True)
   time.sleep(1+attempt)
class RemotePDF(io.RawIOBase):
 def __init__(self,url,cache,block=65536):
  self.url=url;self.cache=Path(cache);self.cache.mkdir(parents=True,exist_ok=True);self.block=block;self.pos=0;self.ranges=[]
  r=urlopen_retry(urllib.request.Request(url,headers={'Range':'bytes=0-0'}),timeout=30)
  self.size=int(r.headers['Content-Range'].split('/')[-1]);r.read();print(url,self.size,flush=True)
 def seekable(self):return True
 def readable(self):return True
 def tell(self):return self.pos
 def seek(self,off,whence=0):
  self.pos=off if whence==0 else self.pos+off if whence==1 else self.size+off
  return self.pos
 def read(self,n=-1):
  if n<0:n=self.size-self.pos
  end=min(self.size,self.pos+n)
  if end<=self.pos:return b''
  first=self.pos//self.block;last=(end-1)//self.block
  i=first
  while i<=last:
   p=self.cache/f'{i:06d}.bin'
   if p.exists():i+=1;continue
   j=i
   while j<last and not (self.cache/f'{j+1:06d}.bin').exists():j+=1
   lo=i*self.block;hi=min(self.size,(j+1)*self.block)-1
   print('range',lo,hi,flush=True)
   req=urllib.request.Request(self.url,headers={'Range':f'bytes={lo}-{hi}'})
   with urlopen_retry(req,timeout=35) as r:
    data=r.read()
    assert r.status==206 and len(data)==hi-lo+1,(r.status,len(data),hi-lo+1)
   self.ranges.append([lo,hi])
   for b in range(i,j+1):(self.cache/f'{b:06d}.bin').write_bytes(data[(b-i)*self.block:(b-i+1)*self.block])
   i=j+1
  data=b''.join((self.cache/f'{b:06d}.bin').read_bytes() for b in range(first,last+1))
  out=data[self.pos-first*self.block:end-first*self.block];self.pos=end;return out
if __name__=='__main__':
 cote=sys.argv[1];pages=[int(v) for v in sys.argv[2:]]
 path=Path('research_sources/q1')
 f=RemotePDF('https://grothendieck.umontpellier.fr/'+cote+'.pdf',path/(cote+'_ranges'))
 r=PdfReader(f,strict=True)
 tree=r.trailer['/Root']['/Pages']
 print('PAGECOUNT',tree['/Count'],'ROOTKIDS',len(tree['/Kids']),flush=True)
 def select(node,index,inherited=None):
  inherited={} if inherited is None else dict(inherited)
  for k in ['/Resources','/MediaBox','/CropBox','/Rotate']:
   if k in node:inherited[k]=node[k]
  kids=node['/Kids']
  if node['/Count']==len(kids):
   ref=kids[index];child=ref.get_object()
   page=PageObject(r,ref);page.update(child)
   for k,v in inherited.items():
    if k not in page:page[NameObject(k)]=v
   return page
  for ref in kids:
   child=ref.get_object();n=int(child.get('/Count',1))
   if index<n:
    if child.get('/Type')=='/Pages':return select(child,index,inherited)
    page=PageObject(r,ref);page.update(child)
    for k,v in inherited.items():
     if k not in page:page[NameObject(k)]=v
    return page
   index-=n
  raise IndexError(index)
 w=PdfWriter()
 for p in pages:
  print('PAGE',p,flush=True);w.add_page(select(tree,p-1))
 out=path/(cote+'_selected_'+','.join(map(str,pages))+'.pdf')
 with out.open('wb') as g:w.write(g)
 (path/(cote+'_ranges/requests.json')).write_text(json.dumps({'url':f.url,'pages':pages,'ranges':f.ranges,'size':f.size}))
 print('SAVED',out,out.stat().st_size,flush=True)
