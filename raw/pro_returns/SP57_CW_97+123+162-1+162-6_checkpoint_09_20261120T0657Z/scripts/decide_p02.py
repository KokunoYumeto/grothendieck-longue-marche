from pathlib import Path
import json,copy
OUT=Path(__file__).resolve().parents[1];stem='C123-01_123_scan002'
r={x:json.loads((OUT/'readers'/stem/x/'report.json').read_text()) for x in ('R1','R2','R3')}
s=json.loads((OUT/'decisions'/(stem+'_pending_spec.json')).read_text())
s['text_edits'].append({'old':'(prop.30)','new':r'(prop.\handwritten{30})'})
R1='readers/'+stem+'/R1/';R2='readers/'+stem+'/R2/crops/';R3='readers/'+stem+'/R3/';M='decisions/'+stem+'_crops/'
paths={1:R1+'01_title.jpg',2:R1+'01_title.jpg',3:R3+'02_english_note.png',4:R3+'02_english_note.png',5:R1+'03_est.jpg',6:M+'faut_suffit_alors.jpg',7:M+'faut_suffit_alors.jpg',8:R1+'04_left_dim.jpg',9:R1+'04_left_dim.jpg',10:M+'right_bracket.jpg',11:R1+'05_heading_1.jpg',12:R1+'05_heading_1.jpg',13:M+'left_cor1_line.jpg',14:R1+'06_inline_mu.jpg',15:R1+'08_display.jpg',16:R1+'08_display.jpg',17:R2+'09_extension.jpg',18:R2+'09_extension.jpg',19:R2+'09_extension.jpg',20:R1+'09_un.jpg',21:R1+'10_left_exchange.jpg',22:R1+'10_left_exchange.jpg',23:R3+'11_proof_opening.png',24:R3+'11_proof_opening.png',25:R1+'11_proof_opening.jpg',26:R1+'11_proof_opening.jpg',27:R2+'15_prop30_z.jpg',28:R2+'15_prop30_z.jpg',29:R1+'13_C_aut.jpg',30:R1+'13_C_aut.jpg',31:R1+'14_C_image.jpg',32:R2+'18_z_retract.jpg',33:R1+'15_comme.jpg',34:R1+'16_On_z.jpg',35:R1+'16_On_z.jpg',36:M+'second_heading_and_line.jpg',37:M+'second_heading_and_line.jpg',38:R2+'22_regular_proof_symbols.jpg',39:R1+'17_bottom_words.jpg',40:R1+'17_bottom_words.jpg',41:R1+'17_bottom_words.jpg',42:R1+'17_bottom_words.jpg',43:R1+'17_bottom_words.jpg',44:R1+'18_bottom_tensor.jpg',45:R1+'18_bottom_tensor.jpg'}
ov={d['id']:{'crop':paths[int(d['id'][-2:])]} for d in r['R3']['differences']}
for d in r['R3']['differences']:
 if d['kind']=='deletion state':ov[d['id']]['kind']='deletion state (struck given live or live given struck)'
def setd(n,**kw):ov[f'R3-D{n:02d}'].update(kw)
setd(2,readers='R1: word inside oval; R2: inserted word plus separate empty oval; R3: word inside oval. Final follows the visible containment and leader, as R1/R3.')
setd(3,readers='R1: separate line below title; R2: margin macro; R3: separate line below title. The crop locates the reference directly below the title.')
setd(4,final=r'subgroup \unsure{....|...} th. 9.2.',confidence='low',readers='R1: four dots; R2: four dots; R3: three dots. All read lowercase th. and a final stop. Final keeps four/three uncertain.',evidence='The two outer leader points are dark, while interior points are pale and not securely countable. Lowercase t and h and the final stop are distinct; the uncertain count is not silently resolved.')
setd(6,evidence='The line ends il faut and the next begins et suffit. There is no second il between et and suffit; all three readers independently made this correction.')
setd(7,evidence='Raised alors has typewriter letterforms and spacing; a pen curve leads down after et. H calls the word handwritten, which the crop contradicts.')
setd(9,readers='R1: staggered note inline with a comment locating it left; R2: staggered margin note with circular call; R3: staggered left-margin note with circular call. Final preserves the left position and both circular marks.')
setd(13,readers='R1: explicitly left margin; R2: unqualified margin; R3: explicitly left margin. The crop places the vertical pen rule left of the text.')
setd(15,readers=r'R1: \unsure{\nu|\psi}; R2: \unsure{\psi|\nu}; R3: \unsure{\psi|\nu}. Final favors psi from the descending stem and two arms, while retaining nu.',evidence='Two upper arms meet a long descending stroke. The shape favors psi rather than the normalizer nu elsewhere, but retracing prevents a certain distinction. The expected mathematical symbol does not settle it.')
setd(17,place='Right marginal question: upper quotient alphabet',C=r'(\unsure{Z|\mathbb{Z}}/hZ)^*',H=r'(\mathbf{Z}/h\mathbf{Z})^*',final=r'(\unsure{Z|\mathbb{Z}}/hZ]^* (alphabet only; delimiter separately recorded)',c_changed=False,confidence='medium',readers='R1: upper and lower pairs double-struck, first with plain-Z alternative; R2: upper first Z/plain-double doubt, upper second plain, lower pair double-struck; R3: all double-struck with first plain-Z alternative. Final distinguishes the upper and lower pairs, following their local strokes.',evidence='The upper Z diagonals are broad and partly retraced without a secure second boundary. Retain C’s first upper Z/plain-double doubt and plain first candidate; the separate lower pair has clearer doubled strokes.')
setd(19,readers='R1: three staggered lines, par lowered/right; R2: shortstack with par on the second line; R3: staggered lines, par lowered/right. Final follows the offset par shown by the crop.')
setd(21,marked_in_H='yes')
setd(22,readers='R1: rotated two-line note at left; R2: linear margin text; R3: two staggered slanted lines at left. Final preserves the slant and left placement.')
setd(24,confidence='low',readers=r'R1: ef\inserted{f}et; R2: ef\inserted{f}et; R3: ef\deleted{\unsure{i}}\inserted{f}et. Final retains the possible covered i with doubt.',evidence='A small baseline serifed stem remains below the raised f. It is compatible with a covered i, but the earlier glyph and exact overwrite boundary are not fully secure; both are represented conservatively.')
setd(27,final=r'prop.\handwritten{30}',c_changed=False,h_changed=False,confidence='medium',kind='other',readers='R1: handwritten 30; R2: handwritten 30; R3: typed 30. Final favors the handwritten origin; the characters 30 themselves are agreed.',evidence='The 3 and 0 have thinner, continuously drawn contours than the neighboring heavy serifed type, and the zero is slightly irregular. This favors C/R1/R2’s handwritten origin. H gives the same characters without an explicit origin claim, so no H collation row is counted.')
setd(28,final=r'\handwritten{\unsure{\mathfrak{z}|z}}',readers=r'R1: \unsure{\mathfrak{z}|z}; R2: \unsure{\mathfrak{z}|z}; R3: \unsure{z|\mathfrak{z}}. Final favors Fraktur while retaining plain z.',evidence='A typed z-like upper part continues into a large handwritten lower loop. Fraktur is the closer typographic representation, but the hybrid construction does not uniquely settle the alphabet; the first occurrence carries the recurring doubt.')
for n,tex in [(29,r'\mathfrak{z}\to\operatorname{Aut}(D)'),(32,r'\mathfrak{z}\to\mu'),(35,r'\mathfrak{z}=\mu')]:
 setd(n,final=tex+'; under first-occurrence alphabet doubt',c_changed=True,h_changed=False,readers='R1: Fraktur z under first-occurrence doubt; R2: Fraktur z under first-occurrence doubt; R3: plain z under first-occurrence doubt. Final repeats the first candidate chosen at the definition.',evidence='The same typed z-shaped top and handwritten descending loop recur here. This occurrence follows the page’s first-occurrence Fraktur/plain doubt, without introducing a new independent alphabet judgment.')
setd(33,final=r'q\unsure{ô|ö}mme',readers=r'R1: q\unsure{ô|ö}mme; R2: \unsure{qômme}; R3: \unsure{qômme|qömme|comme}. Final resolves the visible q and keeps only the diacritic doubt.',evidence='The first letter has a closed bowl and a right descending stem, reading q. The high mark above o has paired short traces and a curved connecting trace: circumflex/umlaut remains uncertain. The grammatical comme is not substituted.')
setd(34,readers=r'R1: \unsure{Bn|On}; R2: \unsure{On|Bn}; R3: \unsure{Bn|On}. Final favors the visible two-chamber B structure while retaining the O trace.')
setd(37,readers='R1: explicitly left margin; R2: unqualified margin; R3: explicitly left margin. Final places the short hooked rule left of the second corollary.')
setd(38,confidence='low',readers='R1: no point in the reading; R2: point marked unsure; R3: point marked unsure. Final retains the detached point with doubt.',evidence='A separate dark point lies immediately to the left of the first c, disconnected from its contour. It is visible, but its status as intentional notation rather than an accidental impression is unresolved.')
setd(42,readers='R1: serial transcription of three layers; R2: serial transcription of three layers; R3: layered TikZ transcription. All three identify the live middle Soit D une. Final preserves their physical vertical order.')
setd(44,readers=r'R1: circled x without doubt; R2: \unsure{\otimes|circled x}; R3: \unsure{circled x|\otimes}. Final keeps the physical circled-x form first, with tensor alternative.',evidence='An upright oval has a typewriter x superposed, with visible projecting serifs. Circled x is the closer visible form; a tensor-sign interpretation remains explicitly possible, rather than being imposed by the mathematics.')
s['difference_overrides']=ov
s['additional_differences']=[
 {'id':'ROOT-lower-Z','place':'Right marginal question: lower quotient alphabet','C':'Z/hZ','H':r'\mathbf{Z}/h\mathbf{Z}','final':r'\mathbb{Z}/h\mathbb{Z}','evidence':'The lower two handwritten Zs have separated diagonal strokes with a pale channel between them. These local strokes are clearer than those of the upper pair.','confidence':'high','kind':'misread symbol or index','marked_in_H':'no','c_changed':True,'h_changed':True,'crop':R2+'09_extension.jpg','readers':'R1: double-struck under a page-level doubt; R2: locally double-struck lower pair; R3: double-struck under a page-level doubt. Final resolves the lower pair locally.'},
 {'id':'ROOT-obtient','place':'Right marginal question: obtient-on','C':'obtient-on ?','H':'obtient-on ?','final':'obtient-on ?','evidence':'The low initial o, tall b/t strokes, dotted i, looped e, connected n/t, hyphen and final on support the wording. The crowded line does not require a different verb.','confidence':'medium','kind':'other','marked_in_H':'no','c_changed':False,'h_changed':False,'crop':R2+'09_extension.jpg','readers':'R1: obtient-on; R2: unsure obtient-on; R3: obtient-on. Final resolves the word, while recording R2’s doubt.'}
]
# Normalize and update every C doubt review from the final decisions.
cd=copy.deepcopy(r['R3']['c_doubts'])
for i,d in enumerate(cd):
 d['C']=d.pop('C_reading',d.get('C',''))
 d['crop']=[paths[1],paths[5],paths[11],paths[17],paths[22],paths[21],paths[23],paths[25],paths[33],paths[34],paths[40],paths[44],paths[15],paths[20],R2+'12_conjugacy.jpg',paths[43],R2+'21_conjugue.jpg'][i]
cd[3].update(decision='Retain first upper Z/plain-double doubt; upper second plain; lower pair locally double-struck',evidence='Upper diagonals are ambiguous; lower diagonals enclose pale channels. Occurrences are not normalized merely from context.')
cd[8].update(decision=r'q\unsure{ô|ö}mme: q resolved, diacritic remains open',evidence=ov['R3-D33']['evidence'])
s['c_doubts']=cd
rem=[]
for d in r['R3']['remaining_doubts']:
 rem.append({'place':d['place'],'reading':d['reading'],'alternatives':d['issue'],'confidence':'low' if any(w in d['place'] for w in ['effect','effet','centralise','point','first c']) else 'medium'})
for d in rem:
 if d['place']=='Right note Zs':d.update(reading='Upper first Z | double-struck Z; upper second plain Z',alternatives='Upper diagonals may be doubled; the lower pair is locally resolved as double-struck.')
 if d['place']=='Centralizer glyph, all four occurrences':d.update(reading='Fraktur z | plain z',alternatives='The typed upper z plus handwritten lower loop admits both alphabets.')
 if d['place']=='Proof after centralise D':d.update(reading='qômme | qömme',alternatives='Only the high mark above o remains uncertain; q is visible.')
rem.insert(1,{'place':'English reference dot leaders','reading':'....','alternatives':'...; the interior points are pale','confidence':'low'})
s['remaining_doubts']=rem
# Inventory: use the more finely separated R2 inventory and add omitted elements found by R3/root.
inv=copy.deepcopy(r['R2']['inventory'])
for d in inv:
 d['sheet_kind']='typescript';d['hand']=d['hand'].replace('handwritten','his hand')
 if d['element']=='Proposition number':d['hand']='his hand (favored over typewriter after comparison)'
for d in r['R3']['inventory']:
 if d['element']=='Underlying stem under raised f':
  q=copy.deepcopy(d);q['sheet_kind']='typescript';inv.append(q)
inv += [dict(sheet_kind='typescript',hand='typewriter overprint',element='Overtyped un after display',kind='text',position='After homomorphism display, est un isomorphisme',first_words_or_objects='un; n-like shoulder with residual dot and lower loop',transcribed='yes'),dict(sheet_kind='typescript',hand='his hand',element='Circular mark beside dimension note',kind='drawing',position='Immediately left of the staggered dimension insertion',first_words_or_objects='Small open circle',transcribed='yes')]
s['inventory']=inv
s['abbreviations']=[{'form':a,'expansion':b} for a,b in [('th.','theorem / théorème, according to the English/French context'),('dim','dimension'),('cor.','corollaire'),('prop.','proposition'),('mod','modulo'),('cqfd.','ce qu’il fallait démontrer'),('h.ème','h-ième (ordinal notation, not expanded in the transcription)')]]
s['main_new_crops']=4
s['consequential']=['The source has il faut et suffit in a); C’s extra il is removed.','H omits the live middle Soit D une in the bottom three-layer correction; it is restored.','The extension question’s square closing bracket, the first-occurrence centralizer alphabet doubt, and the physical circled-x/tensor ambiguity are retained; c^h is not emended to the mathematically expected c^n.']
s['workflow_note']='All three complete readings and reports were compared. Four main-reader crops covered the split-line criterion/raised alors, the right bracket, the first left rule and the second heading/rule; other decisions used existing reader crops. The three tasks had been interrupted before report saving and were resumed with their same independent page contexts; all confirmed no lost context and no whole/half reload. Brief version 03, first used on 123/003, asks readers to save reading.tex before the longer report, quote C/H exactly when setting change flags, include covered baseline glyphs beneath raised corrections, and return exact inventory enums and abbreviation expansions. This follows the covered i, the C-star flag mistakenly described by one report, and heterogeneous inventory field formats.'
for rn in ['R1','R2','R3']:
 for j,ch in enumerate(r[rn]['math_checks']):
  if rn=='R2' and j==2:continue
  sid='123-002-wcw-ch' if j==0 else '123-002-regular-necessity'
  typ="refuted, with refined statement's id 123-002-conjugacy-n" if j==0 else 'targeted proof check'
  outcome='; '.join(str(ch[k]) for k in ['performed','check','result','limit'] if k in ch)
  s['check_events'].append({'statement_id':sid,'who':'GPT-6 Astra Pro; effort not exposed; p02_'+rn.lower(),'type':typ,'outcome':outcome})
# Add an explicit observation to the notes for the one origin disagreement.
s['notes']+='\n\nThe numeral 30 is read identically by all readers, but its production differs in their reports. The main reader favors the thin drawn contours and retains C’s handwritten marking, with medium confidence; this is recorded as a reader-only origin disagreement, not counted as a changed word or symbol.'
(OUT/'decisions'/(stem+'_spec.json')).write_text(json.dumps(s,ensure_ascii=False,indent=2))
print('Final specification saved:',len(r['R3']['differences'])+len(s['additional_differences']),'loci;',len(inv),'inventory elements;',len(rem),'remaining doubts.')
