"""Render all newly integrated proof pages and a compact layout sample."""
from pathlib import Path
import subprocess
from pypdf import PdfReader
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
pdf = root/'SECTION_GHOSTS_paper.pdf'
texts = [p.extract_text() or '' for p in PdfReader(pdf).pages]
terms = ['A.32.']+[f'E.{i}.' for i in range(180,188)]
pages = {1,2,3,4,25,60,100,140,180,len(texts)-1,len(texts)}
starts = {}
for term in terms:
    hits = [i+1 for i,t in enumerate(texts) if term in t and '[Proved]' in t]
    starts[term] = hits
    for p in hits:
        pages.update(range(p,min(p+4,len(texts)+1)))
pages = sorted(p for p in pages if 1 <= p <= len(texts))
dest = root/'build/qa06'
dest.mkdir(exist_ok=True)
for p in pages:
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1200','-png','-singlefile',str(pdf),str(dest/f'page_{p:03}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
for k in range(0,len(pages),3):
    ims=[]
    for p in pages[k:k+3]:
        im=Image.open(dest/f'page_{p:03}.png').convert('RGB')
        frame=Image.new('RGB',(im.width,im.height+32),'#dddddd')
        frame.paste(im,(0,32))
        ImageDraw.Draw(frame).text((10,10),f'Page {p}',fill='black')
        ims.append(frame)
    out=Image.new('RGB',(sum(im.width for im in ims),max(im.height for im in ims)),'white')
    x=0
    for im in ims:
        out.paste(im,(x,0)); x+=im.width
    out.save(dest/f'spread_{k//3+1:02}.png')
print('PDF pages:',len(texts))
print('Rendered pages:',pages)
print('Result heading matches:',starts)
print('Montages:',(len(pages)+2)//3)
print('Rendering complete; actual visual inspection is recorded separately.')
