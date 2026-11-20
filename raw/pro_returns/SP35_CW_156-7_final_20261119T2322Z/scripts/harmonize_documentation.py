"""Normalize documentary counting conventions; does not modify page TeX."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1]
files=list((root/'pages').glob('*.tex'))+[root/'SP35_CW_156-7_transcription.tex']
before={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
records={n:json.loads((root/'records'/f'scan{n:03d}.json').read_text()) for n in range(2,9)}
lookup={d['id']:d for r in records.values() for d in r['decisions']}
updates=[]
def update(ident,**kw):
 lookup[ident].update(kw);updates.append({'id':ident,'fields':kw})
for ident in ['005-57','006-64','007-56']:
 d=lookup[ident];base=d['evidence'].split(' Documentary harmonization:')[0]
 update(ident,diff_H=False,review_only=True,evidence=base+' Documentary harmonization: H’s standard AMS between symbol and the inline TikZ contour encode the same undecorated compatibility sign. Font curvature versus angular handwritten contour is a rendering convention, not a changed reading; this review row is excluded from change and H-collation counts.')
update('004-32',kind='omission',evidence='Both intersection and fine have separate ink underlines. H already marks fine as authorial emphasis with emph; the substantive omission is the unmarked intersection, not the macro conversion over fine.')
update('005-07',H=r'first/final strates plain; \emph{déploiement}',evidence='The first and later strates have independent baseline rules, omitted in H’s markup. H already emphasizes déploiement; no emphasis omission is counted on that word. Its separate spelling difference is the visible descending y in déployement.')
update('005-13',kind='omission',evidence='A separate short rule lies beneath the crossed original baseline, below inserted lieux. M renders it beneath the deleted word, following R1/R3; R2 assigned it to the replacement. The letters éléments remain tentative. H’s note already acknowledges an underlined, cancelled old word; the difference is its omission of the recoverable tentative reading and explicit rendering, not a live-versus-deleted state error.')
update('005-15',H=r'\emph{lieux} followed by colon; note places it above an underlined cancelled word and describes the connector; terminal stop',evidence='The live replacement lies above the cancellation, whose lower rule belongs to the old word. No colon follows lieux and no terminal stop is visible. The long connector is drawn in the final fragment. H’s emph marks authorial emphasis rather than explicitly asserting an underline under live lieux; the remaining differences are the insertion/drawing and punctuation recorded here.')
update('005-23',H=r'équivalent à : si … — \emph{Critère d’inclusion des figures par strates}',evidence='The verb ends in vaut, the conditional has capital S, and de has no terminal s. The underline begins after Critère, whereas H emphasizes the full phrase including Critère. No dash is written between the formula and the heading. The shared emphasis conversion is not a separate difference.')
for ident,word in [('005-46','Relation'),('006-33','Notation')]:
 update(ident,H='\\emph{'+word+'}',diff_H=False,review_only=True,kind='other',evidence='No baseline underline is visible beneath '+word+'. H uses emph for the author’s own emphasis, without an explicit convention asserting a physical underline. M does not count that generic typographic heading emphasis alone as an ink-reading error or as invented text. The plain final heading follows the image; this is a documentary review row only.')
update('006-19',H='plain marginal body; editorial note says the marginal notes are underlined, without exact spans',evidence='Two distinct rules mark compatibilité and par strates, leaving Critère de outside. H’s editorial note does acknowledge marginal underlining generally. The retained difference is the final’s explicit separate spans and their placement, not complete omission of all emphasis.')
update('006-23',H='plain marginal body; editorial note says the marginal notes are underlined, without exact spans',evidence='Three separate rules mark raffinement, par strates and Corollaire, with the surrounding brackets retained. H acknowledges marginal underlining generally in an editorial note. The retained difference concerns the exact spans/placement, not total omission of underlining.')
update('004-12',place='figure-set alphabet in the initial data brace',evidence='At this initial occurrence a looping top stroke crosses a curved descender and small middle bar; it is script, without the Gothic construction. The script-font choice remains uncertain here. The later row-d subscript/set occurrence is separately recorded in004-36; this row is not a global count over both loci.')
update('004-51',evidence='The two later marginal Fig operands repeat the same L shape. The opening L|calligraphic-L uncertainty governs the alphabet convention, and these later operators use its first candidate consistently. This row records the later written loci, distinct from the opening occurrence in004-05; it does not claim a newly resolved alphabet or a new mathematical error.')
update('005-26',diff_H=False,evidence='The capital before (M) has an independent middle cross-stroke below the looped top, making F rather than P and resolving C’s letter alternative. H already reads the letter F. Its family/M alphabet conversion is covered by the explicitly recurring alphabet rows005-03 and005-05, so it is not counted again here.')
for n,r in records.items():(root/'records'/f'scan{n:03d}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
after={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
assert before==after
result={'completed_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'basis':['readers/R1/emphasis_audit.json','readers/R2/macro_equivalence_audit.json'],'updates':updates,'page_and_combined_text_unchanged':True,'sha256':after}
(root/'records/documentary_harmonization.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'updated_records':len(updates),'H_rows_excluded':6,'transcription_unchanged':True},indent=2))
