"""Text-only literal witness-field repair for the earlier Coxeter opening page."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
O=Path(__file__).resolve().parents[1];stem='C123-01_123_scan002'
dest=O/'decisions'/f'{stem}.json';rec=json.loads(dest.read_text())
src={x:(O.parent/'packets'/stem/f'{x}.tex').read_text() for x in ('C','H')}
receipt=O/'decisions/witness_field_repair_02.json';assert not receipt.exists()
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (O/'pages').glob('*.tex')}
changes=[]
def part(field,start,end,include=False):
 t=src[field];a=t.index(start);b=t.index(end,a+len(start));return t[a:b+(len(end) if include else 0)]
def put(id,field,new,note=''):
 assert not new or re.sub(r'\s+','',new) in re.sub(r'\s+','',src[field]),(id,field,new)
 d=next(d for d in rec['differences'] if d['id']==id)
 changes.append({'id':id,'field':field,'old':d[field],'new':new});d[field]=new
 if note:d['evidence']+=' '+note

put('R3-D02','C',part('C',r'\margin{\handwritten{\figure', '\n\na)'))
put('R3-D02','H',part('H',r'\emph{irréductible}', ' »',True),'The H excerpt is from its editorial note describing the oval and call line.')
put('R3-D03','C',part('C',r'\margin{\handwritten{The principal','\n%'))
put('R3-D03','H',part('H',r'\marginal{The principal','\n\\note'))
put('R3-D04','C',r'subgroup ....\quad th. 9.2.')
put('R3-D04','H',r'subgroup …\ \ Th.\ 9.2')
put('R3-D07','C',r'\inserted{alors}')
put('R3-D07','H',"« alors » est ajouté à l'encre au-dessus de la ligne",'H explicitly attributes alors to ink in its editorial note.')
put('R3-D08','C',r'dim $1$')
put('R3-D08','H',r'dim.\ 1')
put('R3-D09','C',r'\inserted{\handwritten{(qui est de dim $1$)}}')
put('R3-D09','H',r'\marginal{\uncertain{(qui est de dim.\ 1)}}')
put('R3-D10','C',part('C',r'\margin{\handwritten{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (-0.16','\n\n\\uline'))
put('R3-D10','H','')
put('R3-D12','C',r'\uline{Corollaire}\handwritten{\unsure{1|!}}')
put('R3-D13','C',part('C',r'\margin{\handwritten{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,0)--','\n\\['))
leftnote=part('H','la seconde dans la marge gauche',"l'énoncé du corollaire 1.",True)
put('R3-D13','H',leftnote,'H describes the left vertical rule in this editorial note.')
put('R3-D16','C',r'(\underline{Z}/h\underline{Z})^{\handwritten{*}}')
put('R3-D16','H',r'(\mathbf{Z}/h\mathbf{Z})^{*}')
put('R3-D17','H',r'(\mathbf{Z}/h\mathbf{Z})^{*}')
put('R3-D19','C',r'\margin{\handwritten{Quelle extension de $(\unsure{Z|\mathbb{Z}}/hZ)^*$ par $Z/hZ$ obtient-on ?}}')
put('R3-D19','H',part('H',r'\marginal{Quelle extension', '\n\\marginal'))
put('R3-D21','H',r'\uncertain{échanger avec cor.\ 3\,?}')
put('R3-D22','C',r'\margin{\handwritten{\unsure{échanger|échange} avec cor.\unsure{3|?}}}')
put('R3-D22','H',leftnote,'H’s quoted positional statement is an editorial note; the slant itself is not typeset.')
put('R3-D25','H','','H gives no literal cancelled word at this locus; its editorial note refers only to a word covered by the machine.')
put('R3-D26','C',r'\inserted{le sous-espace}')
put('R3-D26','H',part('H','« le sous-espace »', 'la machine.',True),'This exact H editorial statement attributes the addition to handwriting.')
put('R3-D27','H','prop.~30')
put('R3-D29','C',r'\handwritten{z\to}\operatorname{Aut}(D)')
for id in ['R3-D30','R3-D31']:put(id,'C',r'\underline{C}^{\handwritten{*}}')
put('R3-D35','C',r'\handwritten{z}=\handwritten{\mu}')
put('R3-D37','C',part('C',r'\margin{\handwritten{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0.05', '\n\nLa suffisance'))
put('R3-D37','H',r'\note{un trait vertical, dans la marge gauche, tient cet énoncé.}')
for field in ['C','H']:put('R3-D38',field,'')
put('R3-D41','C',r'\inserted{Soit $D$ une}')
put('R3-D41','H',r'\struck{Soit D une} \struck{Considérons}','H gives two cancelled beginnings and no live middle Soit D une layer.')
put('R3-D42','C',r'\deleted{\unsure{Considérons}} \deleted{Soit $D$ une}\inserted{Soit $D$ une}')
put('R3-D42','H',r'\struck{Soit D une} \struck{Considérons}')
put('ROOT-obtient','H',r'obtient-on\,?')

dest.write_text(json.dumps(rec,ensure_ascii=False,indent=2))
after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (O/'pages').glob('*.tex')};assert before==after
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
receipt.write_text(json.dumps({'time':now,'scope':'literal witness fields only','transcription_hashes_unchanged':True,'changes':changes,'page_hashes':before},ensure_ascii=False,indent=2))
with (O/'progress.log').open('a') as f:f.write(now+' witness-field provenance repair 02: 42 fields on 123/002 now use exact source excerpts or empty omission fields; all 13 page-file hashes unchanged.\n')
with (O/'SP57_CW_97+123+162-1+162-6_workflow.md').open('a') as f:f.write('\n## Apparatus provenance repair 02\n\nThe same text-only exact-excerpt cleanup was completed for 123/002. Descriptive information remains in evidence, and every nonempty C/H field across the first thirteen finalized records now matches its supplied witness after whitespace normalization. No source reading, difference count or page file changed; the second receipt preserves every old and new field.\n')
print(json.dumps({'fields':len(changes),'page':stem,'transcription_unchanged':True}))
