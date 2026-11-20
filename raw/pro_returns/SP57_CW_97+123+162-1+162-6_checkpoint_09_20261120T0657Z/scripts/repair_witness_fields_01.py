"""Replace apparatus shorthand by exact supplied-witness excerpts.

Text-only provenance repair. No source reading or transcription file changes.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

O=Path(__file__).resolve().parents[1];ROOT=O.parent
receipt=O/'decisions/witness_field_repair_01.json'
assert not receipt.exists(), 'Already applied'
records={};sources={};changes=[]
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (O/'pages').glob('*.tex')}
def data(stem):
 if stem not in records:
  records[stem]=json.loads((O/'decisions'/f'{stem}.json').read_text())
  sources[stem]={f:(ROOT/'packets'/stem/f'{f}.tex').read_text() for f in ('C','H')}
 return records[stem]
def piece(stem,field,start,end,include_end=False):
 data(stem);s=sources[stem][field];a=s.index(start);b=s.index(end,a+len(start))
 return s[a:b+(len(end) if include_end else 0)]
def put(stem,id,field,value,context=''):
 rec=data(stem);d=next(d for d in rec['differences'] if d['id']==id)
 assert not value or re.sub(r'\s+','',value) in re.sub(r'\s+','',sources[stem][field]),(stem,id,field,value)
 old=d[field];d[field]=value
 if context:d['evidence']+=' '+context
 changes.append({'page':stem,'id':id,'field':field,'old':old,'new':value})

s='H97-01_97_scan019'
put(s,'R3-D01','H','numéroté « IV-1102 » à la main.','H records the number inside an editorial note, not as the running head.')
put(s,'R3-D03','C',piece(s,'C',r'$X$\inserted',', de sorte'))
put(s,'R3-D03','H',r'\add{(X étant supposé \emph{noethérien})}')
put(s,'R3-D05','C',piece(s,'C',"l'Idéal ",r' \uline{inversible}'))
put(s,'R3-D05','H',piece(s,'H',"l'Idéal ",r' \emph{inversible}'))
put(s,'R1-D07','C',r'\uline{Idéal de} $\underline O_{X}$')
put(s,'R1-D07','H',piece(s,'H',r'\emph{Idéal de',r'$}',True))
put(s,'R3-D07','H','','H has no separate cancelled qu at this location between Pour and tout.')
put(s,'R3-D09','C',piece(s,'C',r'$t\handwritten',r' (21.2.7)'))
put(s,'R3-D09','H',piece(s,'H',r'$t \in \Gamma',r' (21.2.7)'))
put(s,'R3-D10','C',piece(s,'C',r'\uline{régulière et',". On notera"))
put(s,'R3-D10','H',piece(s,'H',r'\emph{régulière} \add',". On notera"))
put(s,'R3-D13','H','','H has no cancelled cela signifie between car and added pour.')
put(s,'R3-D15','C',r'\underline{\unsure{\mathbb O|O}}_{U}')
put(s,'R3-D15','H',r'\mathcal{O}_{U}')
put(s,'R3-D16','C',r'\underline O_{U}\mathbin{.}t')
put(s,'R3-D16','H',r'\mathcal{O}_{U}.t')
put(s,'R3-D18','C',r'\handwritten{\Gamma}(U,\underline O_{X})')
put(s,'R3-D18','H',r'\Gamma(U,\mathcal{O}_{X})')
put(s,'M3','C',r'\handwritten{(\unsure{sans} \unsure{hyp.}}','C places sans and hyp. on one row of its marginal TikZ node.')
put(s,'R3-D20','C',piece(s,'C',r'\margin{\figure', '\nest un sous-préschéma'))
put(s,'R3-D20','H',piece(s,'H',r'\note{la note marginale',' »}',True))
put(s,'R3-D21','C',r'\operatorname{codim}(\handwritten{\{}x\handwritten{\}},X)')
put(s,'R3-D22','C',r'\operatorname{codim}(\handwritten{\{}x\handwritten{\}},X)={}\allowbreak{}=\operatorname{dim}(\underline O_{X,x})')
put(s,'R3-D22','H',piece(s,'H',r'\mathrm{codim}', ' = 1'))
put(s,'R3-D23','H',r'\mathcal{O}_{X,x}')
put(s,'R3-D25','C',r'\margin{\handwritten{\uline{réf} !}}','C places its marginal command after the X^(1) semicolon.')
put(s,'R3-D25','H',r'\marginal{réf !}','H places its marginal command after Posons.')
put(s,'R3-D26','H',r'\mathcal{O}_{Y(D),x}')
put(s,'R3-D28','H',r'\mathcal{O}_{Y(D),x} = 0')
put(s,'R3-D29','C',r'\handwritten{\sum}^{\handwritten{\unsure{\prime}}}')
put(s,'R3-D30','H',r'\mathcal{O}_{Y(D),x}')
put(s,'R3-D31','C',r'Z^{1}\llap{\raisebox{-.12ex}[0pt][0pt]{\tiny\unsure{.}}}(X)')
put(s,'R3-D31','H',r'Z^{1}(X)')
put(s,'R3-D33','C',r'\deleted{\uline{Si} $X$ \uline{est noethérien},}')
put(s,'R3-D33','H',r'\struck{Si $X$ est noethérien,}')
put(s,'R3-D34','C',r"\deleted{l}\handwritten{L}'application")
put(s,'R3-D34','H',"l'application")
put(s,'R3-D36','H','','H has no separate overwritten punctuation at this point.')
put(s,'R3-D37','C',piece(s,'C',r"\uline{\deleted{l}", '\n\nTout revient'))
put(s,'R3-D37','H',piece(s,'H',r"\emph{l'application", '\n\nTout revient'))
put(s,'R3-D38','C',r"\underline I_{X}(D+D')=\underline I_{X}(D)\underline I_{X}(D')")
put(s,'R3-D38','H',r"I_{X}(D+D') = I_{X}(D) I_{X}(D')")
put(s,'R3-D39','H',r'A = \mathcal{O}_{X,x}')
put(s,'R3-D40','C',r"\operatorname{long}(A/tA)+{}\allowbreak{}+\operatorname{long}(A/t'A)")
put(s,'R3-D40','H',r"\mathrm{long}(A/tA) + \mathrm{long}(A/t'A)")
put(s,'R3-D41','C',r'\deleted{\unsure{$x$}}')
put(s,'R1-D32','C',r'Z^{1}(X)')
put(s,'R1-D32','H',r'Z^{1}(X)')

s='C123-01_123_scan016'
for id in ['R1-D13','R1-D28','R1-D31']:put(s,id,'H','')
put(s,'M-09','C',piece(s,'C',r'\inserted{\handwritten{et $x$', '\n\n\\['))
put(s,'M-09','H',piece(s,'H',r'\note{la ligne b', 'un trait.',True),'This quoted H editorial note describes the connecting trait; it does not draw it.')
s='C123-01_123_scan017'
put(s,'R3-22','H',piece(s,'H',r'\note{la frappe porte', '\n\n'),'The quoted H editorial note explicitly attributes the corrected lower bound to handwriting.')
s='C123-01_123_scan019'
put(s,'R3-D05','C',piece(s,'C',r'i_{\unsure{o|0}}',r'$ de $\operatorname{Dyn}'))
put(s,'R3-D05','H',piece(s,'H','i_0',r'$ de $\mathrm{Dyn}'))
put(s,'R3-D09','H',piece(s,'H',r'$Z_0$ récrit','lettre.',True),'The H excerpt is its editorial note about the overwritten letter, not an independent full glyph drawing.')
for field in ['C','H']:put(s,'ROOT-05',field,'')
s='C123-01_123_scan020'
put(s,'R2-01','H','sont\n\\add{ceux} de')
put(s,'R2-07','H','')
put(s,'R2-14','H','aux\nunipotents')
s='C123-02_123_scan022'
for field in ['C','H']:put(s,'ROOT-03',field,'')
put(s,'ROOT-04','H','Massy 22.10.1969','H supplies this place/date without a placement command.')
s='C123-02_123_scan028'
put(s,'D05','H',piece(s,'H',r'$u_*$', 'exact',True),'The exact quoted H passage is an editorial synopsis, not the full typescript wording.')
put(s,'D22','H',piece(s,'H','pour toute espèce','quelconques',True),'The exact quoted H passage is its editorial synopsis of the structure definition.')
put(s,'D32','H','','H’s editorial synopsis elsewhere uses image inverse, but does not quote this locally cancelled source word.')
put(s,'D33','H',piece(s,'H','nous conseillons au lecteur','validité',True),'The quoted advice appears inside H’s final editorial note; the preceding refusal of formal justification is not transcribed.')
put(s,'D41','H',piece(s,'H','à la note de bas de page','est barrée',True),'H mentions selected corrections here, without the full footnote prose.')
put(s,'ROOT-02','H','')

for stem,rec in records.items():
 (O/'decisions'/f'{stem}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2))
after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (O/'pages').glob('*.tex')}
assert before==after
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
receipt.write_text(json.dumps({'time':now,'scope':'apparatus witness fields only; exact supplied excerpts; no image views or source-reading changes','transcription_hashes_unchanged':True,'changes':changes,'page_hashes':before},ensure_ascii=False,indent=2))
with (O/'progress.log').open('a') as f:f.write(now+' witness-field provenance repair 01: '+str(len(changes))+' fields in '+str(len(records))+' decided-page apparatus records replaced with exact source excerpts or empty omission fields; all 13 page-file hashes unchanged.\n')
with (O/'SP57_CW_97+123+162-1+162-6_workflow.md').open('a') as f:f.write('\n## Apparatus provenance repair 01\n\nA text-only audit found descriptive shorthand and normalized nonliteral formula excerpts in early C/H columns. They were replaced by exact supplied witness snippets, with placement/synopsis explanations retained in evidence. Omitted loci use empty witness fields. This repairs attribution and serialization; it changes no decided source reading, difference count, confidence, or page-file byte. The detailed before/after receipt and unchanged page hashes are in decisions/witness_field_repair_01.json. The remaining early page-002 fields are audited separately.\n')
print(json.dumps({'fields':len(changes),'records':len(records),'transcription_unchanged':True}))
