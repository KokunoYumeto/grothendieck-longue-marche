from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[1]
D={l:json.loads((R/f'readers/scan013/{l}/report.json').read_text()) for l in 'ABC'}
bp=lambda n:f'readers/scan013/B/c{n:02}.png'
ap=lambda n:f'readers/scan013/A/crops/c{n:02}.png'
m=lambda s:'crops/scan013/'+s+'.png'
cm={0:m('main01_cohomologie_quotes'),1:bp(1),2:bp(2),3:m('main02_inline_R'),4:bp(3),5:m('main03_grand_quotes'),6:bp(4),7:bp(5),8:ap(6),9:m('main04_main_quotes'),10:bp(7),11:m('main05_acyclique_quotes'),12:bp(8),13:bp(8),14:bp(8),15:bp(9),16:m('main06_NB_underline'),17:bp(10),18:bp(10),19:bp(11),20:bp(12),21:bp(13),22:bp(13),23:bp(13),24:bp(13),25:bp(14),26:bp(14),27:ap(14),28:ap(14),29:ap(14),30:ap(14),31:ap(14)}
aix=[1,0,2,3,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35]
ci=lambda i:i if i<=20 else i+1
ov={str(i):{'crops':[cm[i]],'scan_shows':'Main independently inspected '+cm[i]+': '+v['scan_shows'],'readers':{'A':D['A']['changes'][aix[i]]['reading'],'B':v['reading'],'C':D['C']['changes'][ci(i)]['reading']}} for i,v in enumerate(D['B']['changes'])}
def upd(i,**kw):ov[str(i)].update(kw)
upd(0,scan_shows='Main main01: two short raised strokes open the phrase on its first line and two close relative on the next. No angled guillemets are drawn.')
upd(1,final=r'\unsure{g|q}',against_c=True,confidence='medium',scan_shows='Main B/c01, with repeated forms in B/c07 and B/c08: a one-storey bowl and long descender have a weak leftward foot. The clearer repeated feet favour g, but the first glyph does not securely exclude a handwritten q. Retain the first-occurrence g/q doubt; later identical letters use g under this reservation.',consequential='The recurring morphism is recorded as g/q at its first occurrence; no identification is forced from the expected functor notation.')
upd(2,scan_shows='Main B/c02: the single rule starts under the rightward tail of n, before c, and ends beneath m before final ent. The left attachment leaves ctoriellem / nctoriellem uncertain; fo and ent are outside the rule.')
upd(3,scan_shows='Main main02: the R has an outer stem/loop and a separate inner upright. Preserve the doubled alphabet rather than H’s plain R.')
upd(4,scan_shows='Main B/c03: paired raised pen strokes occur on both sides of géométrique, not angled guillemets.')
upd(5,scan_shows='Main main03: two high strokes open grand and two high endpoints close it beside the parenthesis. The closing ink partly joins the parenthesis but retains the paired quotation form.')
upd(6,scan_shows='Main B/c04: the dark terminal trace remains connected to the final r of exister. The strip before the paper edge has no separate full stop. No stop is supplied from syntax.')
upd(7,scan_shows='Main B/c05: the word ends with the n shoulder and its long exit. There is no independent final s after it. Read singular construction.')
upd(8,scan_shows='Main A/c06: after the n, a tall t stroke has a curved rightward exit. No separate final e loop is secure, although a compressed e cannot be excluded. No plural s survives. Retain évident first and évidente as the alternative, rather than resolve the ending from grammar.')
upd(9,scan_shows='Main main04: paired high strokes frame à la main. A further detached dark point just below-right of the opening pair is recorded separately; it is not used as a third quotation stroke.')
upd(10,confidence='medium',scan_shows='Main B/c07: the small bowl and long descending stem end with a leftward foot. Use g under the first-occurrence g/q reservation.')
upd(11,scan_shows='Main main05: two raised strokes precede the opening parenthesis of (-1) and two follow acyclique. These are double quotes, with a separate hyphen before acyclique.')
upd(12,final=r'F\mathord{-}g_*',against_c=True,confidence='high',scan_shows='Main B/c08: the relation is one blunt horizontal stroke. Its swollen right end has no separate upper and lower arrowhead arms, unlike the clear arrow in B/c11. Read a dash; the word injectif does not justify inserting an arrow.',consequential='The inline relation after F is a literal dash, with no visible arrowhead. The limited mathematical check explicitly assumes the intended unit map and does not alter this source mark.')
for i in [13,14]:upd(i,confidence='medium',scan_shows='Main B/c08: the morphism has a small bowl and left-returning descender, read g under the page’s g/q reservation. The first star is distinctly low and the second distinctly raised; their positions are preserved.')
upd(15,confidence='medium',scan_shows='Main B/c09: the faint opening i/n/j traces include a low j return; ectif and the final long f can be followed. Read injectif. The low return is part of the letter, not a separate underline.')
upd(16,scan_shows='Main main06: a single horizontal line runs below both N and B. It does not begin under the opening parenthesis.')
upd(17,scan_shows='Main B/c10 and B/c11: the small bowl with a long lower stem favours p. The other occurrence has a relatively tall rounded bowl, so case is not secure. Mark p/P at the first occurrence and use p subsequently.',consequential='The slice-object letter remains p/P; its case is not fixed from the expected slice notation.')
upd(18,final=r'\unsure{si|où}',against_c=True,confidence='medium',scan_shows='Main B/c10: an open low joined form and a detached high point favour si. The following lower stroke is faint enough that a separate i cannot be completely isolated; retain où as the alternative without choosing from the conditional meaning.')
upd(19,confidence='medium',scan_shows='Main B/c11: the first letter has a low stem and high rounded bowl, read p under the p/P reservation. The following rightward arrow has separate head strokes; e has an internal return and Y is a subscript.')
upd(20,scan_shows='Main B/c12: initial accented e, p and i and the terminal hisme are visible, but the pale intervening traces do not independently settle every letter. Retain the word doubt épimorphisme.')
upd(21,scan_shows='Main B/c13: the first low subscript is an open curve, without a secure interior bar. Place c before e; the terminal-object interpretation does not override the visible outline.')
upd(22,final=r'B_{\unsure{c|G}}',against_c=True,confidence='low',scan_shows='Main B/c13: a low c-like hook is secure. A higher arc partly joins the bottom of B, but its connection to the low hook is faded. The lower hook supports c first; a larger G is possible but not established.',consequential='The second B subscript is c/G, with c first on the surviving low hook; the expected classifying-topos letter does not settle it.')
upd(23,marked_in_H='yes',scan_shows='Main B/c13: p/l/u/s followed by h/a/u/t can be followed despite variable pressure. Resolve plus haut; H had explicitly marked these words uncertain.')
upd(24,scan_shows='Main B/c13: the closing parenthesis reaches toward the right edge. The following visible strip contains no separate full stop.')
upd(25,scan_shows='Main B/c14: the R has distinct outer and inner upright strokes. Preserve the doubled R.')
upd(26,marked_in_H='no',scan_shows='Main B/c14: multiple crossing strokes cancel a low forked index after Gamma. The remaining upper fork favours Y, but the crossings also allow X. It is a cancelled index, not a live thickened Y. H’s descriptive note empâté is not itself a doubt flag.',consequential='The low Gamma index is deleted Y/X, not H’s live Y; the index identity remains uncertain.')
for i in [27,30]:upd(i,confidence='medium',scan_shows='Main A/c14: the morphism’s bowl and left-returning descending stem support g under the first-occurrence g/q reservation. The outer star is low; the inner star is raised.')
upd(28,scan_shows='Main A/c14: the opener after the low star has an almost vertical side and a basal foot, favouring [. Its rounded upper turn resembles nearby round openers enough to retain (. C’s resolved square bracket is not adopted. The subsequent mismatched delimiters are not repaired.',consequential='Keep the doubtful [/( opener and the written closing sequence; do not silently balance the formula.')
upd(29,confidence='medium',scan_shows='Main A/c14: the rounded glyph curls inward at upper-right and carries an interior return/bar. These strokes support e, like the e in B/c11, rather than an open C. Resolve e; A’s C alternative is not retained.',consequential='The resolution glyph is e rather than H’s C, on its visible interior return.')
upd(31,scan_shows='Main A/c14: the brace begins under e and extends through the first thin closing parenthesis after F. Three further heavier closes follow outside that brace before [-1]. The lower label has both abbreviation stops: résol. inj. H’s note credits those words, but its attachment does not reproduce the visible brace span.',consequential='The resolution underbrace extends through the first closing parenthesis after F; its endpoint and the surrounding delimiters are preserved exactly.')
extras=[]
def extra(ai,cp,**kw):
 row=copy.deepcopy(D['A']['changes'][ai]);row['final']=row.pop('reading');row.pop('crop_ids',None);row['crops']=[cp];row['marked_in_H']='no';row.update(kw);extras.append(row);return row
point=extra(12,m('main04_main_quotes'),readers={'A':D['A']['changes'][12]['reading'],'B':'No separate point transcribed','C':'No separate point transcribed'},scan_shows='Main A/c06 and main04: a small dark point lies below-right of the two high opening quote strokes and is detached from the accent on à. Its physical presence is clear, but its textual role is uncertain. Retain a raised point with a no-textual-character alternative; no semantic role is assigned.')
extra(24,m('main07_short_dash'),readers={'A':'-','B':'- (present in complete reading, omitted from differences list)','C':'-'},scan_shows='Main main07: one short thick horizontal stroke has swollen ends, with no second line or arrowhead. Preserve a short separating dash, not H’s em dash.')
for ai,loc in [(36,'left of the display at source (74,1603)'),(37,'lower and to the right at source (202,1634)')]:
 extra(ai,ap(15),readers={'A':D['A']['changes'][ai]['reading'],'B':'No textual point transcribed; treated as a surface/scan speck','C':'No textual point transcribed'},scan_shows='Main A/c15: a detached black mark '+loc+' is darker and more definite than the surrounding gray noise. It has no secure textual function. Preserve point / no textual character uncertainty in its margin position; the phantom alternative does not deny the physical spot.')
font1=r'\unsure{\mathbb{A}b|\mathit{Ab}}(Y)'
font2=r'\mathbb{A}b'
for ai,cp,final in [(4,m('main08_Ab_first'),font1),(5,m('main09_Ab_second'),font2)]:
 extra(ai,cp,final=final,against_c=True,against_h=True,confidence='medium',kind='misread symbol or index',readers={'A':D['A']['changes'][ai]['reading'],'B':r'\mathit{Ab}(Y)' if ai==4 else r'\mathit{Ab}','C':r'\mathit{Ab}(Y)' if ai==4 else r'\mathit{Ab}'},scan_shows='Main main08 and main09: A has an outer left oblique and a separate interior return running alongside it, particularly clear in the second occurrence. The two diagonals favour a doubled A, while an ordinary looped handwritten A remains possible. The b has one tall stem and a low bowl, without a separate doubled stroke. Mark the A-alphabet doubt at the first occurrence and use its first candidate thereafter. This is a doubt about visible strokes, not a change counted solely from mathit versus mathrm.',consequential='The category-name A is recorded as doubled/plain at first occurrence because of two left-diagonal strokes; all three readers had accepted a plain A.')
uns=[]
for i,u in enumerate(D['B']['unresolved']):
 if i==2:continue
 u=copy.deepcopy(u)
 refs={0:bp(2),1:ap(6),3:bp(10),4:bp(12),5:bp(13),6:bp(13),7:bp(14),8:ap(14)}
 u['evidence']='Main inspected '+refs[i]+'. '+u['evidence'].split(': ',1)[-1]
 if i==6:u.update(reading=r'\unsure{c|G}',alternatives=['c','G'],evidence=ov['22']['scan_shows'])
 uns.append(u)
for place,reading,alternatives,evidence,conf in [
('Recurring morphism, first occurrence',r'\unsure{g|q}',['g','q'],ov['1']['scan_shows'],'medium'),
('Category-name A, first occurrence',font1,[r'\mathbb{A}b',r'\mathit{Ab}'],extras[-2]['scan_shows'],'medium'),
('Connective after slice morphism',r'\unsure{si|où}',['si','où'],ov['18']['scan_shows'],'medium'),
('Point after opening quote before à la main',point['final'],['raised point','no textual character'],point['scan_shows'],'low'),
('Detached left margin point',r'\margin{\unsure{.|\phantom{.}}}',['point','no textual character'],extras[2]['scan_shows'],'low'),
('Detached lower margin point',r'\margin{\unsure{.|\phantom{.}}}',['point','no textual character'],extras[3]['scan_shows'],'low')]:uns.append(dict(place=place,reading=reading,alternatives=alternatives,evidence=evidence,confidence=conf))
inv=copy.deepcopy(D['C']['inventory'])
inv[6]['first_words_or_objects']='(de la catégorie dérivée de '+font1+' dans celle de '+font2+') ?'
inv[10]['first_words_or_objects']=r'Mais je ne vois de construction \unsure{évident|évidente} …'
inv[17]['first_words_or_objects']=r'Y_{/\unsure{p|P}}\to Y'
inv[20]['first_words_or_objects']=r'B_{\unsure{c|e}}\to B_{\unsure{c|G}} plus haut'
# Insert distinct points by their actual vertical loci, keeping the original top-to-bottom sequence.
def invpoint(element,position,first,kind='margin note'):
 return dict(sheet_kind='letter',hand='unnamed pen hand; textual status uncertain',element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes')
inv.insert(12,invpoint('Detached point beside opening quotation','source line 14, below-right of opening quote',point['final'],'text'))
inv.insert(25,invpoint('Detached left point','source (74,1603), left of final formula',r'\margin{\unsure{.|\phantom{.}}}'))
inv.insert(27,invpoint('Detached lower point','source (202,1634), above-right of archive number',r'\margin{\unsure{.|\phantom{.}}}'))
notation=copy.deepcopy(D['C']['notation'])
notation[0]['ink']=ov['1']['scan_shows']
notation[5].update(ink=extras[-2]['scan_shows'],latex=font1+'; '+font2)
notation[8].update(ink=ov['12']['scan_shows'])
notation[10].update(ink=ov['17']['scan_shows'],latex=r'Y_{/\unsure{p|P}}\to Y')
notation[11].update(ink=ov['19']['scan_shows'])
notation[12].update(ink=ov['21']['scan_shows']+' '+ov['22']['scan_shows'],latex=r'B_{\unsure{c|e}}\to B_{\unsure{c|G}}')
notation[16].update(ink=ov['28']['scan_shows'],latex=r'\unsure{[|(}')
notation[17].update(ink=ov['29']['scan_shows'])
notation.append(dict(place='Three detached points',sign='points / no textual character',ink=point['scan_shows']+' '+extras[2]['scan_shows']+' '+extras[3]['scan_shows'],latex=r'\unsure{\textsuperscript{.}|\phantom{\textsuperscript{.}}}; \margin{\unsure{.|\phantom{.}}}'))
notation.append(dict(place='NB separating punctuation',sign='short dash',ink=extras[1]['scan_shows'],latex='-'))
subs=[
 dict(old=r'$g:X\to Y$',new=r'$\unsure{g|q}:X\to Y$'),
 dict(old=r'\mathit{Ab}(Y)',new=font1),
 dict(old=r'celle de $\mathit{Ab}$',new='celle de $'+font2+'$'),
 dict(old="``à la main''",new=r"``\unsure{\textsuperscript{.}|\phantom{\textsuperscript{.}}}à la main''"),
 dict(old=r'F\unsure{\mathord{-}|\to}g_{*}',new=r'F\mathord{-}g_{*}'),
 dict(old=r'\to Y$ si $p',new=r'\to Y$ \unsure{si|où} $p'),
 dict(old=r'B_{\unsure{G|c}}',new=r'B_{\unsure{c|G}}'),
 dict(old='On prend\n',new='On prend\n% isolated point at source (74,1603), left of display\n'+r'\margin{\unsure{.|\phantom{.}}}'+'\n'),
 dict(old='% archive sheet number: 12',new='% isolated point at source (202,1634), above-right of archive number\n'+r'\margin{\unsure{.|\phantom{.}}}'+'\n% archive sheet number: 12')]
pending=json.loads((R/'adjudication/scan013_pending_checks.json').read_text())
event=copy.deepcopy(pending['events'][0]);event['outcome']='Interpretation used only for this check: the written injectivity condition is treated as the unit-map assumption, while the transcription preserves the actual dash after F. '+event['outcome'];event['date']=pending['performed_utc']
seen=set(cm.values())|{e['crops'][0] for e in extras}
c=dict(scan=13,folder='H103-02',filename='H103-02_103_scan013.tex',brief='brief_v10.md',base='B',adjudicated=True,inspected_crops=sorted(seen),change_overrides=ov,extra_changes=extras,substitutions=subs,unresolved=uns,inventory=inv,sheet_kind='letter',notation=notation,abbreviations=D['C']['abbreviations'],notes=[
'[S013.N1] This wholly handwritten continuation raises relative cohomology and gives case a), a displayed expression with a cancelled Gamma index, and the lower annotation résol. inj. It has no new title, date, salutation, signature, author page number or total. The separate pencil archive number is 12. The pen hand remains unnamed. H’s explicitly editorial page-order paragraph is not source ink and was not used to reorder the supplied scans.',
'[S013.N2] The question is whether relative cohomology can be defined functorially in an abelian sheaf, or a complex of such sheaves, on Y, from the derived category of the written Ab(Y) to that of Ab. The geometric interpretation in terms of n-champs de Picard, with n “grand”, is said to suggest existence: “suggère que ça doit exister”. The author says he sees a construction “à la main” only in two extreme cases; only a) occurs here. These are a question, a suggestion and a stated limitation, not a theorem proved in this run.',
'[S013.N3] Case a) calls g “(-1)-acyclique” and states an injectivity condition. The actual short relation after F is a dash, without a visible arrowhead. For a limited mathematical check, interpret the injectivity statement as the unit map F→g_*g^*F being monic, and take an abelian sheaf F with a bounded-below injective resolution I of g^*F. Left exactness makes F[0]→g_*I degreewise monic. Its cokernel Q fits 0→F[0]→g_*I→Q→0, hence Q[-1]→F→g_*I→Q. Exactness of g^* implies that its right adjoint g_* preserves injectives, so g_*I represents Rg_*g^*F; applying RΓ_Y gives the corresponding relative-sections triangle. This supports the written shift [-1] in that restricted sheaf case. It does not prove a canonical cone functor on bare triangulated categories, extend the argument to arbitrary unbounded complexes, or replace the source’s dash by an arrow.',
'[S013.N4] The NB gives a slice-to-topos example under an epimorphism condition and a B-object reference “plus haut”. These assertions are carried as background without a separate proof. The object letter remains p/P, the connective si/où, and the two B subscripts c/e and c/G; no expected terminal-object or classifying-topos notation was used to decide them. The recurring morphism is g/q at first occurrence. The adjective remains évident/évidente, preserving the visible ending rather than grammar.',
'[S013.N5] The final formula retains its cancelled Y/X index, the doubtful [/( opener, four written round closes after F before [-1], and the brace through the first close. The resolution glyph resolves to e on an interior return, not H’s C. The abbreviation label has both stops. The formula’s delimiter mismatch is preserved. Small letters and the brace prompted close visual inspection, not a reconstruction from the mathematical expectation.',
'[S013.N6] Main’s crops of the two category names show a narrow interior return parallel to A’s outer left leg. A doubled/plain A doubt is therefore recorded at first occurrence, with a plain b; all three readers had treated the A as ordinary. This is a graphic uncertainty rather than a macro-only mathit/Mathrm preference. A separate high point beside the opening quote and two lower detached black points are preserved with no-textual-character alternatives. These alternatives acknowledge physical marks without assigning a textual function.',
'[S013.N7] All three complete independent readings and their difference lists were compared. Main inspected thirteen retained B crops, three retained A crops, and nine new crops for half-settled differences: twenty-five distinct crops. No source whole or half was viewed by main. Fourteen loci remain unresolved. The brief already covered isolated marks, but ordinary-font comparison rules needed clarification: differences between mathit and mathrm alone are not substantive, while an extra parallel stroke must be examined before calling the alphabet ordinary. The next brief makes that distinction explicit.'
],check_events=[event,dict(statement_id='S013.N4.examples_and_suggestion',type='carried as background without fault found',outcome='The geometric suggestion through n-champs, the slice example and the B-object reference were transcribed as source assertions or suggestions, without proof. The question of a functor on derived categories is broader than the restricted sheaf-level check in S013.N3. No external theory, historical ordering claim, or unbounded generalization was adopted.')])
(R/'adjudication/scan013.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
print('Config',len(ov)+len(extras),'rows;',len(uns),'doubts;',len(inv),'inventory;',len(seen),'main crops')
