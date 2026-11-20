"""Main-reader decisions after comparison and 39 effective local image views."""
from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1];s='C29-04_29_scan083'
r=json.loads((O/'readers'/s/'r1/report.json').read_text())
t=(O/'readers'/s/'r1/reading.tex').read_text()
t=t.replace(r'\handwritten{\raisebox{-0.35ex}{\scriptsize q}}',r'\handwritten{\textsubscript{q}}')
t=t.replace(r'\uline{\deleted{\unsure{pe}}}',r'\deleted{\uline{p\unsure{e}}}')
t=t.replace(r'\unsure{\mathbb{X}|X|W}',r'\unsure{\mathbb{X}|\mathbb{V}|X}')
raw={d['id']:copy.deepcopy(d) for d in r['differences']}
def main(f):return f'crops/{s}/{f}.png'
def rd(f,who='r1'):return f'readers/{s}/{who}/crops/{f}.png'
sources={'D01':main('m26_diagonal_cancellation'),'D02':main('m01_start'),'D06':rd('c04_hom_symbols','r3'),'D07':rd('c04_hom_symbols','r3'),'D09':main('m10_product_x'),'D10':main('m11_donnee_du'),'D11':main('m12_inserted_P'),'D13':rd('c06_H_hat'),'D14':rd('c06_H_hat'),'D15':main('m14_quote2'),'D16':main('m15_quote3_start'),'D17':main('m16_quote3_end'),'D31':main('m25_live_deleted_schema'),'D32':main('m25_live_deleted_schema'),'D33':main('m18_section'),'D35':main('m23_algébrisable_semicolon'),'D37':rd('c04_hom_symbols','r3')}
diff=[]
def put(key,**kw):
 d=copy.deepcopy(raw[key]);d.update(kw)
 d['source']=sources.get(key,d.get('source','')) if 'source' not in kw else kw['source']
 if d['source'].startswith('crops/c'):d['source']=f'readers/{s}/r1/'+d['source']
 if 'readers' not in d:d['readers']={x:d['reading'] for x in ['r1','r2','r3']}
 d['marked_in_H']='yes' if ('\\ill' in d.get('H','') or '\\uncertain' in d.get('H','') or d.get('H_doubt_note')) else 'no'
 diff.append(d);return d
for key in ['D01','D02','D03','D04','D05']:
 d=put(key)
 if key=='D03':d['readers']['r2']=r'{}_nG^o'
 if key=='D04':
  d['readers'].update(r2=r'\deleted{les}',r3=r'\deleted{les}')
  d['evidence']='The l is clear, but the middle crossbar and final s contours remain confluent with the x overtyping. Readers 2 and 3 resolve les; the main reader retains the narrower honest reservation of C and reader 1.'
ovalplaces=[('L3, first Hom source',rd('c04_hom_symbols','r3'),[1413,317,1445,363]),('L5, extensions source',main('m03_L5_extensions'),[609,463,653,518]),('L6, second Hom source',main('m04_L6_hom_source'),[1135,532,1187,585]),('L11, extensions source',main('m05_L11_extensions'),[532,891,566,936]),('L12, extensions source',main('m06_L12_extensions'),[828,951,874,1012]),('L14, extension source',main('m07_L14_right_formula'),[1358,1095,1395,1143])]
for n,(place,src,box) in enumerate(ovalplaces,1):
 reading=r'\underline{\unsure{\varnothing|\phi|\Phi}}' if n==1 else r'\underline{\varnothing}'
 if n in [2,3,5]:reading+='_n'
 d=put('D06',id=f'D06.{n}',place=place,source=src,bbox=box,C=reading,reading=reading,H=r'\underline{\mathbb{Z}}'+('_n' if n in [2,3,5] else ''),H_doubt_note='H explicitly says in its note after the first Hom that its contextual Z reading is doubtful as a character; the note concerns this recurrent glyph.',evidence='The blue glyph is an oval crossed by an oblique rising stroke, with a separate underline; no Z outline is visible. Its alphabet remains unresolved. The first occurrence carries the alternatives, and later occurrences use the first candidate under the recurring-sign convention.')
 if n==1:d['readers']['r2']=r'\underline{\varnothing}'
naturalplaces=[('L3, first Hom target',rd('c04_hom_symbols','r3'),[1534,305,1571,354]),('L11, target of extensions',main('m05_L11_extensions'),[691,870,727,921]),('L13, G in reference to (7.6.1)',main('m08_L13_natural'),[795,1008,831,1059]),('L14, first G',main('m09_L14_first_G'),[813,1081,849,1132]),('L14, second G',main('m07_L14_right_formula'),[1521,1077,1555,1129])]
for n,(place,src,box) in enumerate(naturalplaces,1):put('D07',id=f'D07.{n}',place=place,source=src,bbox=box)
put('D08',reading=r'\handwritten{\textsubscript{q}}',readers={'r1':r'\handwritten{\raisebox{-0.35ex}{\scriptsize q}}','r2':r'\handwritten{q}','r3':r'\handwritten{\textsubscript{\unsure{q|,}}}'})
for key in ['D09','D10','D11']:put(key)
quotes=[('L8, complétion formelle',main('m13_quote1'),[1221,674,1638,720],"``complétion formelle''",'« complétion formelle »'),('L9, first systêmes cohérents',main('m14_quote2'),[1080,744,1510,800],"``systêmes cohérents''",'« systèmes cohérents »'),('L11–12, systêmes cphérents',main('m15_quote3_start'),[1410,877,1638,927],"``systêmes cphérents''",'« systèmes cohérents »')]
for n,(place,src,box,reading,h) in enumerate(quotes,1):
 put('D12',id=f'D12.{n}',place=place,source=src,bbox=box,C=reading,H=h,reading=reading,evidence='Each opening and closing mark is a pair of short raised straight strokes, without angular guillemets or internal blank cells. This row concerns quote form; spelling differences are separately located.'+(' The closing pair is on the following line, also inspected in '+main('m16_quote3_end')+'.' if n==3 else ''))
put('D12',id='D12.4',place='L9, between des and opening quotes',source=main('m14_quote2'),bbox=[1048,746,1114,792],C='des``',H='des «',reading='des``',evidence='The opening pair immediately follows the s of des at normal typewriter pitch; there is no blank word cell.')
put('D13',readers={'r1':raw['D13']['reading'],'r2':raw['D13']['C'],'r3':raw['D13']['C']})
for key in ['D14','D15','D16','D17']:put(key)
put('D18',place='L14–15, cancelled underlined pair in dé…pend',reading=r'dé\deleted{\uline{p\unsure{e}}}pend',diff_C=True,readers={'r1':r'dé\uline{\deleted{\unsure{pe}}}pend','r2':r'dé\uline{\deleted{\unsure{pe}}}pend','r3':r'dé\deleted{\uline{pe}}pend'},evidence='A secure p descender survives in the first cancelled cell; the second cell has only partial e-like contours under the x at the edge. A separate black horizontal stroke lies below the pair. The main reader narrows doubt to the second cell and records the underline; no invisible continuation is supplied.')
put('D20',readers={'r1':raw['D20']['reading'],'r2':'précédentes','r3':'précédentes'})
put('D21',C=r"\unsure{qutun|qu'un}")
for key in ['D22','D23','D24']:put(key)
put('D25',reading=r'\margin{\handwritten{$\unsure{V|\checkmark}$}}',readers={'r1':r'\margin{\handwritten{$\unsure{V|\checkmark}$}}','r2':'Literal V-shaped figure inside the cancelled paragraph','r3':r'\margin{\handwritten{$\unsure{V|\checkmark}$}}'},evidence='Two dark joined limbs form a V with a longer right arm. Letter versus check remains unresolved. The mark is in the left margin and outside the continuous text-cancellation trace; the final keeps the separate marginal placement.')
ringplaces=[('L20, after adique',main('m19_ring_adique'),[751,1525,787,1573]),('L21, ideal inclusion',main('m20_ring_inclusion'),[439,1592,474,1647]),('L21, G sur',main('m21_ring_Gsur'),[1123,1592,1160,1643]),('L21, tensor base',rd('c12_lower_round'),[1462,1608,1499,1654]),('L21, right tensor factor',rd('c12_lower_round'),[1485,1586,1521,1637]),('L22, left side of quotient equality',rd('c11_original_ring'),[340,1669,375,1720]),('L24, ring in inserted sur',main('m22_inserted_sur_ring'),[1148,1770,1181,1813])]
for n,(place,src,box) in enumerate(ringplaces,1):
 old=r'\unsure{\mathbb{X}|\mathbb{V}|X}' if n==1 else r'\mathbb{X}'
 reading=r'\deleted{'+old+r'}\handwritten{V}'
 d=put('D26',id=f'D26.{n}',place=place,source=src,bbox=box,reading=reading,C=raw['D26']['C'] if n==1 else reading,diff_C=n==1,evidence='A black V has been written over a blue serifed original capital. Both layers are retained. The unreplaced numerator in '+rd('c11_original_ring')+' supports a crossed X-like original, with double-struck V or plain X as remaining alternatives; no A apex or W twin lower vertices is secured. Alternatives are marked at the first occurrence only.')
 if n==1:d['readers']={'r1':r'\deleted{\unsure{\mathbb{X}|X|W}}\handwritten{V}','r2':r'\deleted{\unsure{\mathbb{X}|\mathbb{V}}}\handwritten{V}','r3':r'\deleted{\unsure{\mathbb{X}|\mathbb{V}}}\handwritten{V}'}
put('D27')
put('D28',place='L21, first lower round, on G',readers={'r1':r'G_{\unsure{o|0}}','r2':'G_o','r3':r'G_{\unsure{o|0}}'},evidence='The first lowered round on G has no diagnostic feature distinguishing o from zero. The two later ring subscripts follow the first-candidate convention and do not create additional differences from H.')
for key in ['D29','D30','D31','D32','D33','D34','D35','D37']:put(key)
diff[-1]['readers']={'r1':r'\underline{\varnothing}\ ,\ G','r2':r'\underline{\varnothing}\ ,\ G','r3':r'\underline{\varnothing},\ G'}
raw['D37']['mathematical']=False;diff[-1]['mathematical']=False
for d in diff:
 if d['id']=='D31':d['evidence']+=' The preceding line end was also inspected in '+main('m24_before_abelien')+'.'
gaps=[('L5, G_n before comma',main('m03_L5_extensions'),[743,457,848,518],'G_n ,','G_n,'),('L10, H_n before full stop',main('m17_Hn_period'),[715,823,825,876],'H_n .','H_n.'),('L12, G_n before comma',main('m06_L12_extensions'),[1047,950,1145,1015],'G_n ,','G_n,'),('L14, first G before comma',main('m09_L14_first_G'),[791,1080,904,1145],r'G^{\natural} ,',r'G^{\sharp},'),('L14, second G before comma',main('m07_L14_right_formula'),[1479,1082,1584,1145],r'G^{o\natural} ,',r'G^{o\sharp},')]
for n,(place,src,box,c,h) in enumerate(gaps,1):put('D36',id=f'D36.{n}',place=place,source=src,bbox=box,C=c,H=h,reading=c,evidence='A full blank interval separates the formula from the typed punctuation. This row records the gap; letter decorations are separately located.')
diff.append(dict(id='D38',place='L4, base. Appliquant',C='same paragraph',H='paragraph break before Appliquant',reading='base. Appliquant in the same paragraph',diff_C=False,diff_H=True,kind='insertion or placement',marked_in_H='no',confidence='high',mathematical=False,source=main('m02_same_paragraph'),bbox=[790,382,1220,452],evidence='base. and Appliquant occupy the same continuous typed line; no paragraph boundary intervenes.',readers={x:'same paragraph' for x in ['r1','r2','r3']}))
cd=copy.deepcopy(r['c_doubts']);u=copy.deepcopy(r['unresolved'])
for seq in [cd,u]:
 for d in seq:
  if 'underlined slashed oval' in d['place']:d['source']=rd('c04_hom_symbols','r3')
  if 'cancelled pe' in d['place']:
   d.update(reading=r'\deleted{\uline{p\unsure{e}}}',evidence='D18: p is secure; e remains tentative under overtyping. The separate lower stroke is retained as an underline.')
   if seq is cd:d['status']='changed'
  if 'original ring cell' in d['place']:d.update(reading=r'\unsure{\mathbb{X}|\mathbb{V}|X}',evidence='D26.1–7 and D29: crossed strokes and broad feet favor double-struck X; double-struck V and plain X remain possible. A and W lack the corresponding diagnostic contours.')
  if 'dark mark after à' in d['place']:d['reading']=r'\handwritten{\textsubscript{q}}'
  if d.get('source','').startswith('crops/c'):d['source']=f'readers/{s}/r1/'+d['source']
  for oc in d.get('occurrences',[]):
   if oc.get('source','').startswith('crops/c'):oc['source']=f'readers/{s}/r1/'+oc['source']
inv=copy.deepcopy(r['inventory'])
for d in inv:
 d['first_words_or_objects']=d['first_words_or_objects'].replace('recurring X/X/W doubt','recurring double-struck X / double-struck V / plain X doubt')
 if d['element']=='E21':d['first_words_or_objects']='p and tentative e, x-overstruck; p secure'
obs=json.loads((O/'adjudication_inputs'/f'{s}_interim_observations.json').read_text())
data=dict(stem=s,base='r1',brief='brief_v05.md',agents={rid:'/root/p083_'+rid for rid in ['r1','r2','r3']},reading_text=t,exclude=list(raw),add_differences=diff,c_doubts=cd,unresolved=u,inventory=inv,main_crops=[main(f.stem) for f in sorted((O/'crops'/s).glob('m*.png'))],main_views=obs['effectively_viewed'],checks=[],
 notes='Typescript draft numbered 74, with handwritten corrections, section 7.6.3 and archive number 82. A single diagonal cancels all three paragraphs. The page states finite/local-freeness and Hom base-change claims, an equivalence between torsors and coherent formal systems, a corresponding description of extensions, functoriality in G and compatibility with complete-trait base change. Section 7.6.3 extends the construction to a noetherian adic base and calls algebraizability of the resulting formal abelian scheme the “question essentielle”; it says the method of 7.2 applies when S is normal. These are reported claims; their proofs and the referred sections are not supplied here and no proof check was performed. Mathematical notation prompted inspection of all six underlined slashed ovals, five natural decorations, the raised/lowered rounds, and the corrected ring letters. The ink supports natural rather than H’s sharp, a typed x, and seven black V replacements while the quotient numerator remains an unreplaced original glyph. H explicitly acknowledges that its Z reading is contextual and that the character is doubtful; that reservation is carried in the collation. No theorem is used to force Z, zero, or V into the transcription. The cramped mark over H remains an uncertain circumflex with maker/technique unassigned. Readable cancelled commute and sché are resolved; les and the second cell of the cancelled underlined pair remain uncertain. Two mixed initial cells in précédentes remain explicit. Literal systêmes twice, cphérents, qutun and inserted sbhéma are retained. The small lowered q-shaped mark is resolved as a shape without assigning a linguistic function; the marginal V/check remains unresolved. H places an illegible cancellation before the live schéma abélien, whereas the readable local cancellation is schéma before tore. No title, date or total page count is written. No OCR, external research or LaTeX compilation was used.',
 slips=['systêmes (twice), cphérents, qutun, and raised sbhéma local are retained as typed.','The cancelled underlined p(e) interrupts dé…pend; two mixed cells begin the word otherwise read as précédentes.'],abbreviations=[{'form':'i.e.','expansion':'id est (that is)','evidence':'29/083 L9, introducing coherent systems.'}],
 adjudication='All three finished returns compared before decision. The main reader inspected 13 existing reader crops and 26 new local crops, 39 effective views. The new narrow affine crop follows the continuous diagonal cancellation without displaying a whole page or half. Every far-apart recurrence of an H discrepancy is separately located. C’s twelve doubt places are accounted for, and the crowded H decoration adds a new doubt. Reader 2 resolved rounds and the slashed oval; the main reader retained the shape/alphabet alternatives. Reader 2/3 resolutions of les and the first mixed cells in précédentes were not adopted. The final cancelled pair narrows uncertainty to e and retains its underline. The first display attempt for m26/m01/m02 overflowed and was not inspected; the same files were subsequently redisplayed, without recropping. Reader 2’s start time was not captured; its explicit timing limitation remains in the independent report. The task’s serial page rule was maintained.')
(O/'adjudication_inputs'/f'{s}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Wrote',s,'difference places',len(diff),'C',sum(d['diff_C'] for d in diff),'H',sum(d['diff_H'] for d in diff))
