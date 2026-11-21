"""Root adjudication of the fixed image-only return for scan 070."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1]; page='149_scan070'
rp=B/'reviews'/f'{page}.json'; r=json.loads(rp.read_text()); assert not r.get('audit')
p=B/'pages'/f'{page}.tex'; t=p.read_text()
oldrelation=r'E_K-E_{U_{\unsure{\eta|K}}}'
relation=r'E_{\unsure{\eta|K}}-E_{U_{\unsure{\eta|K}}}'
oldsurj=r'E_K\twoheadrightarrow E_S'; surj=r'E_{\unsure{\eta|K}}\twoheadrightarrow E_S'
oldcancel=r'\deleted{\unsure{rationnelle}}'; cancel=r'\deleted{\unsure{rationnelle|sur}}'
for a,b in [(oldrelation,relation),(oldsurj,surj),(r'\unsure{défini|defini}','defini'),(oldcancel,cancel)]:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t)
c={v['id']:v for v in r['changes']}
ie='The left index has a long upright, a rising diagonal joined to one upper apex, then a right descending leg with a hooked exit. The continuous apex-to-leg contour admits eta and a joined K. The independently visible split K at B12 and on the right of B16 has a separate lower branch; that branch cannot be isolated here. Preserve eta/K at this left index as well as at the smaller right index. This added uncertainty supplies no material witness correction.'
ae='The d has a closed lower bowl and looped upright, followed by a low e and a tall looped f. The two later i dots are dark and separate; the terminal low stroke ends without another e or a comma. Above the first e the sparse pale traces have the faint tone of the surrounding sheet, with no separate writing-dark accent stroke. Read defini without an accent, retaining the literal ending and blank after the word.'
ce='The live section remains readable before the heavy horizontal cancellation: sinuous s, low e/c, tall crossed t, dotted i, o and final n. The canceled cluster begins with a low curve and contains obscured short uprights and terminal returns. The blind sur and first rationnelle both remain tentative within this one canceled cluster; the thick retracing conceals the letter count. The upper descender is traced independently of the cancellation and leaves section live.'
c['P09'].update(final=relation,evidence=c['P09']['evidence'].replace('complete left E_K','complete left indexed E')+' '+ie)
c['P11'].update(final=surj,evidence=c['P11']['evidence']+' '+ie)
c['P13'].update(final='defini',evidence=ae,against_C=True,confidence='medium')
c['P14b'].update(final='section '+cancel,evidence=ce,confidence='low')
for d in r['decisions']:
 if d['id'] in ['M1190','M1191','M1194']:
  d['evidence']='The whole formula was compared. The disputed nested index has a left upright, joined rising diagonal and hooked right descending leg. Split K is visible at B12 and at the right of B16, while the joined left indices at B11/B13 also remain eta/K after the blind audit. The nested outline remains undecided; no mathematical identification supplies its letter.'
r['doubts']=[d for d in r['doubts'] if '(P13)' not in d['place']]
for d in r['doubts']:
 if 'nested index' in d['place']:d['reason']='Joined apex and hooked right leg admit eta/K; the separate lower branch of split K is absent or merged here. The joined left indices at B11/B13 also remain uncertain.'
 if 'canceled word' in d['place']:d.update(reading=cancel,alternatives='rationnelle/sur; obscured intervening letter bodies',reason=ce)
r['doubts'].extend([
 dict(place='first inserted relation, left index (P09/B11)',reading=r'E_{\unsure{\eta|K}}',alternatives='eta/K',confidence='medium',reason=ie),
 dict(place='main line 13, left index (P11/B13)',reading=r'E_{\unsure{\eta|K}}',alternatives='eta/K',confidence='medium',reason=ie)])
for v in r['inventory']:
 if v['element']=='E03':v['first_words_or_objects']=v['first_words_or_objects'].replace(oldrelation,relation)
 if v['element']=='E05':v['first_words_or_objects']=r'\unsure{rationnelle|sur}'
order=['E01','E02','E04','E03','E05','E06'];r['inventory'].sort(key=lambda v:order.index(v['element']))
r['notes'][6]='The three original eta/K marks remain open. The blind audit also leaves two joined left indices uncertain, in the first inserted relation and in the hom surjectif relation. H\'s K remains within these alternatives, so this uncertainty is excluded from material counts. The prose dash encodings -- and --- each represent the one observed horizontal stroke.'
r['notes'][7]='Root reviewed all first-pass crops and all twelve differing blind boxes. Barred m, split K at M1192, live section, and the two arrowhead wedges at P11 remain accepted. The canceled cluster is now rationnelle/sur; the unaccented defini is read from the absence of a writing-dark accent. The source objective is reported without a proof or refutation; check_events remains empty.'
for h in r['hand']:
 if h['form']=='joined or split K':
  h.update(form='joined eta/K and split K',observation=ie,scope='All disputed nested indices and the two blind-disputed left indices were compared. The visibly split K at B12 and B16 is retained.',witness_errors='M1192 resolves to K. M1190/M1191/M1194 and the two additional joined left indices remain undecided; these unresolved alternatives supply no established witness error.')
 if h['form']=='accent over flattened e':h.update(observation=ae,witness_errors='Both witnesses accent the first e; H also supplies a final e/comma. The final reading is defini.')
for n in r['notation']:
 if n['form']==oldsurj:n.update(form=surj,meaning='Relation called hom surjectif by the source; the two visible head wedges are retained and its joined left index remains eta/K.')
for d in r['diff_coverage']:
 if d['row'] in [12,17]:d['reason']='Joined index remains eta/K; independently split K is visible elsewhere, while the joined left indices are also uncertain after the blind audit.'
 if d['row']==15:d['reason']='Literal defini has no writing-dark accent, no final e and no following comma.'
for i,s in enumerate(r['deletion_insertion_review']):
 if 'C deletion rationnelle:' in s:r['deletion_insertion_review'][i]=ce+' The nested canceled doubt has no supplied MARKS ID.'
r['open_issues']=[d['place']+': '+d['reading'] for d in r['doubts']]
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,ev):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=ev)
def change(b,final,title,ev):D[b]=dict(final=final,changed=True,decision=title,evidence=ev)
keep('B01','Retain schém.','The s/c and tall h lead to the accented low e, then a compressed m and its flat exit. The detached terminal mark is compact, with no full-height bowl and right stem such as the a in élémentaire at B02. It supplies the abbreviation stop. Both open U bodies and the low S are retained.')
keep('B02','Retain the paired quotation strokes and single dash','Two raised strokes appear at each end of élémentaire. After sur S is one horizontal line. The -- and --- source encodings each map to that one line with the same attachment; their TeX length difference adds no manuscript character. Retain the existing -- encoding.')
keep('B04','Retain pi with low 1','The long top bar overhangs the two closely spaced downward legs, with the right leg slanting outward. That compact central-leg form is the page\'s pi; the separate short low stroke to the right supplies 1. Retain the supplied pi notation without changing its level or index.')
keep('B06','Retain the inserted f','A tall upper loop descends through a separate middle shoulder/cross stroke and ends in a hooked lower return. Those three components support f. The separate curved attachment leads to the gap before baseline de, which already follows the insertion in the page; the blind inclusion of de enlarges the excerpt only.')
keep('B07','Retain the uncertain nested index',ie+' Here the uncertainty belongs to the subscript below U; the complete two-lobed E and open U remain visible.')
outer=r'\inserted{(composé de \inserted{la section} $'+relation+r'$ avec $E_{U_K}\unsure{-|\longrightarrow}E_{U_S}$)}.'
change('B09',outer,'Qualify the left index within the complete insertion',ie+' The nested la section leader enters after composé de. The outer leader passes beneath both relations and attaches below; the parentheses and separate dark final point remain. The second relation\'s connector stays uncertain where the prose descender overlaps its endpoint.')
change('B11','$'+relation+'$','Qualify the joined left index',ie+' The intervening horizontal has a single downturned terminal cap without paired wings. Its longer lower line belongs to the insertion leader. The formula is already inside the outer inserted span, so the blind insertion wrapper maps to that existing extent.')
keep('B12','Retain split K and the uncertain connector','The low K has an upright, a rising upper diagonal and an independently descending lower branch. The long prose descender merges with the short connector at its right end, leaving its upper wing unsettled; retain dash/arrow. Both open U bodies and low S remain. The blind parenthesis and point are already present at the right of the enclosing insertion; their inclusion changes only the excerpt extent.')
change('B13','$'+surj+'$','Qualify the left index while retaining two heads',ie+' At the shaft end a small pointed wedge has short upper and lower returns; a second larger detached > stands immediately to its right. Those two heads remain transcribed at medium confidence, together with the target E and low S.')
change('B14','defini','Read the unaccented word',ae)
change('B15','section '+cancel,'Retain the live word and broaden the canceled reading',ce)
keep('B16','Retain the joined-index uncertainty','The first E has a lower open U and smaller joined index with a hooked right leg; eta/K remains open. After sur, the right E_K has a rising diagonal and a separate dark lower branch, supporting K there. The independently suggested eta remains the first candidate for the joined index, without removing its alternative.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D))
record(page);assign('reader_c')
