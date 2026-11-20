"""Main-reader decisions after independent returns and the documented crop views."""
from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={r:json.loads((O/f'readers/scan010/{r}/result.json').read_text()) for r in ['R1','R2','R3']}
s=(O/'readers/scan010/R2/reading.tex').read_text()
title=r'\handwritten{\unsure{I|1}) \uline{Le théorème de Griffiths par voie algébrique.}}'
newtitle=r'''% Two brown marginal strokes; numeral/letter/bracket interpretation unresolved.
\margin{\handwritten{\figure{\unsure{\begin{tikzpicture}[x=0.012cm,y=0.012cm]
\draw[brown,line width=1.1pt] (20,123) .. controls (17,103) and (7,44) .. (7,24) .. controls (7,17) and (8,14) .. (11,12);
\draw[brown,line width=1.1pt] (65,137) .. controls (73,132) and (66,105) .. (62,85) .. controls (56,49) and (50,16) .. (33,1);
\end{tikzpicture}}}}}
\handwritten{\uline{Le théorème de Griffiths par voie algébrique.}}'''
assert title in s;s=s.replace(title,newtitle)
s=s.replace(r'\handwritten{\ne}\unsure{\chi|\ell}',r'\ne\unsure{\chi|\ell}')
old=r'(Y,\deleted{\unsure{f^*(F)|f(F)}}\handwritten{F_Y})'
new=r'(Y,\deleted{\unsure{f(F))|f^*(F))}}\handwritten{F_Y)}'
assert old in s;s=s.replace(old,new)
s=s.replace(r'\deleted{\unsure{N-1|m-1}}\handwritten{m-1}',r'\deleted{\unsure{N|N-1|m-1}}\handwritten{m-1}',1)
s=s.replace(r'_{\deleted{2}}',r'_{\deleted{\unsure{2|f}}}')
s=s.replace(r'\deleted{\unsure{xx|de}}',r'\deleted{\unsure{de|xx}}')
(O/'pages/A36-01_36_scan010.tex').write_text(s)

# A row map records the actual alternatives returned by each independent reader.
maps={1:(1,1,2),2:(1,2,1),3:(3,3,4),4:(4,4,6),5:(5,5,8),6:(6,6,9),7:(7,7,11),8:(8,8,13),9:(9,9,14),10:(11,10,15),11:(12,11,16),12:(13,12,18),13:(14,13,19),14:(16,14,22),15:(17,15,23),16:(18,16,24),17:(19,17,25),18:(20,18,26),19:(22,19,27),20:(23,20,29),21:(24,21,30),22:(28,22,33),23:(29,23,34),24:(31,24,36),25:(32,25,37)}
rows=[]
for j,x in enumerate(R['R2']['differences'],1):
    r={k:copy.deepcopy(x[k]) for k in ['place','C','H','against_C','against_H','kind','marked_in_H','confidence','ink','evidence']}
    r['final']=x['reading'];r['readers']=[R[rr]['differences'][ix-1]['reading'] for rr,ix in zip(['R1','R2','R3'],maps[j])]
    r['decision']='Compared all three readings; main reader inspected the cited crop.'
    rows.append(r)
def change(i,**kw):rows[i-1].update(kw)
change(1,final='Two brown marginal strokes reproduced in TikZ, with an in-place doubt mark; interpretation I), 1), or a bracket remains open.',against_C=True,against_H=True,kind='drawing or diagram',ink='A long upright with a small bent foot is followed by a taller concave closing stroke. These strokes can be reproduced securely, but their alphabetic/numerical interpretation cannot. Incidental pale edge traces are not promoted to authorial letters.',decision='R1 and R2 retained I|1; R3 drew the mark. The main reader follows the graphical treatment of the two definite brown strokes, without R3’s uncertain pale edge traces.')
change(2,evidence='crops/scan010/R3/title.jpg')
change(4,against_H=False,final=r'\ne\unsure{\chi|\ell} (mechanical appearance)',C=r'\handwritten{\ne\ell}',H=r'\neq\ell; H describes the machine glyph as chi-shaped',ink='Two regular horizontal bars and a slash precede a serifed crossed glyph with an upper hook and lower foot. The glyph has no distinguishable tall closed ell loop. Repeated forms in the adjective and subscript support mechanical type. Literal chi is first; ell is retained as the alternative, not restored solely from its prime-number role.',decision='R1 and R2 put chi first; R3 put ell first. The visible crossed shape supports chi first, while the glyph’s intended alphabet remains uncertain. The not-equal sign is not securely a pen insertion and is left unmarked as type.')
change(6,against_H=False,evidence='crops/scan010/R3/soit_f_ell.jpg')
change(7,against_H=False,confidence='medium',ink='The capital Z has one normal diagonal, with a distinct lower rule. The subscript is the same serifed chi-shaped mechanical glyph. H’s bold styling is not supported by a distinct bold or doubled alphabet here; uncertainty remains in the prime glyph’s alphabet.')
change(8,decision='R1 removed the live-m doubt; R2 and R3 retained it. The overlaid two-shouldered form is probable m, but the crop does not separate its strokes sufficiently to remove the doubt. H’s note acknowledges the underlying N, so this is a C-doubt review rather than a separate H omission.')
change(9,final=r'\deleted{\unsure{f(F))|f^*(F))}}\handwritten{F_Y)}',ink='The new F and descending Y are followed by a live early closing curve. Farther right, hatching covers an F and two closing curves of the old coefficient/tail. No separate raised old star can be established. The cancelled old expression is therefore f(F)) first, with f*(F)) retained; the live replacement includes its new closing parenthesis.',decision='R1 identified the old two closes and the new earlier close; R2 and R3 retained C-like allocation. The main reader follows R1 for the visible bracket layers and retains the star uncertainty.')
change(10,evidence='crops/scan010/MAIN/primitive_underline.jpg',against_H=False,decision='The ink is a single underline. H’s supplied preamble says emph encodes the author’s own emphasis; this is treated as equivalent emphasis markup, not an H reading error. Final uline preserves the required literal form.')
change(12,final=r'\handwritten{(\unsure{f|F}))}',ink='The live letter has an upper hook, a long descending stem and a leftward cross stroke; lowercase f is visually nearer, but retraced capital F remains possible. Two live closing curves precede the cancelled tail.',decision='R1/R3 prefer F, R2 prefers f. The main crop supports f first; the mathematical role as a coefficient sheaf favours F but does not override the pen shape.',consequential='The inline coefficient remains f|F rather than being silently normalized to the named sheaf F.')
change(13,final=r'\deleted{(F))}',decision='R1 retained doubt on the last close; R2/R3 read two closes. The main crop shows two distinct crossed closing curves, so (F)) is retained without a doubt mark.')
change(14,decision='R1/R3 choose plain E; R2 retains E|double-struck E. The main reader puts plain E first but retains the double-impression alternative because the heavy overlapping contour does not fully settle it.')
change(15,final=r'\deleted{\unsure{N|N-1|m-1}}\handwritten{m-1}',against_C=True,ink='The high old serifed strokes most nearly support N. The visible minus and one are pen-like additions, so an earlier -1 cannot be asserted. N-1 and m-1 remain possible older layers.',decision='R1 puts old N first; R2 omits that possibility; R3 adds it third. The main crop supports N first and preserves the other allowed old-layer candidates.')
change(17,final=r'_{\deleted{\unsure{2|f}}}',confidence='low',ink='The lower cancelled glyph has a curled upper part and a dark foot; a 2 is plausible, but an f-like residual form cannot be excluded.',decision='R2 resolved 2; R1/R3 retained 2|f. The main reader retains 2|f because the crossed foot obscures the distinction.')
change(19,decision='R1/R2 retain Z|double-struck Z|z; R3 excludes double strike. The main crop shows an extra interior contour and supports capital Z first without securely ruling out either superposition alternative.')
change(21,evidence='crops/scan010/MAIN/prose_z.jpg')
change(22,final=r'-\handwritten{2}d^{\handwritten{\prime}}\deleted{\unsure{\mathrm{im}(X\prime/S)|\mathrm{im}(Y\prime/S)}}',ink='The live 2 stands before a clean typewriter d; a high handwritten prime follows. Cancellation begins in the remaining im(...), not in the retained d. The crossed capital visually resembles X, but Y under cancellation remains possible. A live replacement is unequivocally present.',decision='R1 kept all dim(...) cancelled and doubted 2d′; R2/R3 retained the typed d and read live 2d′. The crop supports the retained d and additions. X is first in the uncertain old tail because the visible crossing is X-like; context would favour Y.',consequential='The live degree correction is 2d′; H’s statement that the replacement is absent is contradicted by the ink. The typed d is reused rather than cancelled.')
change(23,against_H=False,final=r'\mathbin{\ooalign{\hfil$\mathrm{x}$\hfil\cr\hfil$\handwritten{\bigcirc}$\hfil\cr}}',decision='All three distinguish a typed x core and handwritten oval. The crop confirms this physical construction. H has the same tensor sign, so no H collation row is generated solely for absent provenance markup.')
change(24,final=r'\deleted{\unsure{de|xx}}',against_C=True,ink='Two x-shaped cancellation impressions cover a tall first remnant and a rounded second remnant. These make underlying de the nearer tentative reading; xx is retained as the visible overtype alternative.',decision='R1/R2 put visible xx first; R3 put underlying de first. The main reader gives the recoverable old-letter candidate de first, without treating it as certain.')
change(25,against_H=False,evidence='crops/scan010/MAIN/final_adique.jpg')

# Explicitly confirm the fibre overwrite, a C-doubt/alphabet checkpoint.
rows.insert(13,dict(place='Fibre cohomology exponent and barred subscripts',C=r'H^{\deleted{N}\handwritten{m}}(Y_{\bar s},F_{\bar s})',H=r'H^m(Y_{\bar s},F_{\bar s}); H note acknowledges N',final=r'H^{\deleted{N}\handwritten{m}}(Y_{\bar s},F_{\bar s})',against_C=False,against_H=False,kind='other',marked_in_H=True,confidence='medium',ink='Tall N stems survive beneath the pen replacement. The separate short rules belong above both subscript s letters.',evidence='crops/scan010/R2/fiber_cohomology.jpg',readers=['Same N-to-m and barred s','Same N-to-m and barred s','Same N-to-m and barred s'],decision='Confirmed on the main-reader crop; no emendation.'))

inv=copy.deepcopy(R['R2']['inventory'])
inv[0]['first_words_or_objects']='Le théorème de Griffiths par voie algébrique.; handwritten title with single underline'
inv.insert(0,dict(sheet_kind='typescript',hand='his hand (attribution supplied; not independently identified)',element='010-prefix',kind='drawing',position='upper-left margin beside title',first_words_or_objects='two brown strokes; I), 1), or bracket interpretation unresolved',transcribed='yes'))
for x in inv:
    if x['element']=='010-07':x.update(kind='text',hand='typewriter (probable)',first_words_or_objects='not-equal sign, no secure evidence of a separate pen insertion')
    if x['element']=='010-16':x['first_words_or_objects']='cancelled f(F)) / f*(F)), including both old right closing curves'
    if x['element']=='010-17':x['first_words_or_objects']='new F_Y and early live closing parenthesis'
    if x['element']=='010-27':x['first_words_or_objects']='earlier N / N-1 / m-1 overwritten'
    if x['element']=='010-31':x['first_words_or_objects']='cancelled 2 / f, unresolved'
    if x['element']=='010-48':x['first_words_or_objects']='cancelled de / xx after Tate, unresolved'
    if 'Grothendieck' in x['hand']:x['hand']='his hand (attribution supplied; not independently identified)'
for j,x in enumerate(inv,1):x['element']=f'010-{j:02d}'

def u(place,reading,alternatives,reason,confidence='low'):
    return dict(place=place,reading=reading,alternatives=alternatives,reason=reason,confidence=confidence)
unresolved=[
u('brown marginal mark','two strokes reproduced in TikZ',['I)','1)','bracket'],'Shape is retained, but its alphabetic/numerical interpretation is not determined.'),
u('first prime glyph and its recurrences',r'\chi',[r'\ell'],'Crossed mechanical shape supports chi; mathematical prime usage supports ell but does not settle the glyph alphabet.','medium'),
u('Soi... F, old terminal letter','t',[],'Overwritten typed character is not independently separable.'),
u('first H exponent, live correction','m',[],'Two-shouldered replacement overlaps N.','medium'),
u('first H coefficient, cancelled layer',r'f(F))',[r'f^*(F))'],'Two old closing curves are visible; a separate old star is not secure.'),
u('inline H^0, live coefficient','f',['F'],'Hooked stem favours f; named coefficient sheaf favours F semantically.'),
u('Leray spectral-sequence alphabet','E',[r'\mathbb{E}'],'Heavy impression without a securely separable doubled vertical.','medium'),
u('Leray old second degree','N',['N-1','m-1'],'Visible minus and one may belong solely to the new pen layer.'),
u('Leray old R degree','m',['N'],'Old upper remnant is obscured.'),
u('Leray old lowered glyph','2',['f'],'Cancellation obscures upper curl and foot.'),
u('Leray old f subscript','f',[],'Star overlaps a small hooked prior form.'),
u('first correspondence-class alphabet','Z',[r'\mathbb{Z}','z'],'Extra inner contour permits double impression or Z/z superposition.'),
u('cancelled tail after retained d',r'\mathrm{im}(X\prime/S)',[r'\mathrm{im}(Y\prime/S)'],'Crossed capital resembles X; Y under cancellation remains possible and is favoured by the following explanation.'),
u('after Tate','de',['xx'],'Tall and rounded remnants permit de; visible x-overtypes obscure the underlying word.')]

notation=[
dict(sign='prime-number glyph',appearance='Repeated mechanical crossed glyph with upper hook and lower serif/foot',convention=r'\unsure{\chi|\ell} first occurrence per page; \chi thereafter',evidence='010: residual-characteristic line, coefficient subscript, and both adic adjectives; R2 prime_letter/coefficient_ring, R3 soit_f_ell, MAIN final_adique'),
dict(sign='integer coefficient',appearance='Single typed Z with distinct lower horizontal rule',convention=r'\underline{Z}',evidence='010 first coefficient; crops/scan010/R2/coefficient_ring.jpg'),
dict(sign='cohomology and direct-image capitals',appearance='Ordinary serifed type H and R; overwritten degrees handled independently',convention='H, R',evidence='010 cohomology/Leray crops; inline R^m is clean type'),
dict(sign='spectral-sequence alphabet',appearance='Heavy E, no securely separate doubled vertical',convention=r'\unsure{E|\mathbb{E}}',evidence='010 Leray display, crops/scan010/R2/leray_class.jpg'),
dict(sign='correspondence class',appearance='Overprinted first Z; later prose z and action Z distinct',convention=r'\unsure{Z|\mathbb{Z}|z} at the first displayed class; z in “z définit”; Z elsewhere as seen',evidence='010 correspondence_class and MAIN prose_z crops'),
dict(sign='geometric point',appearance='Short separate rule above the subscript s',convention=r'\bar s',evidence='010 fibre_cohomology crop'),
dict(sign='product',appearance='Serifed typewriter lowercase x at baseline, with lowered S',convention=r'\mathbin{\mathrm{x}}_S',evidence='010 correspondence_class crop'),
dict(sign='mixed tensor sign',appearance='Typed x core circled with a thinner pen oval',convention=r'standard \ooalign overlay of \mathrm{x} and \handwritten{\bigcirc}',evidence='010 tensor_pairing crop'),
dict(sign='coefficient/correction parentheses',appearance='Some old outer closing curves cancelled and replaced earlier in the line',convention='Preserve both old and new closing curves inside their respective deleted/handwritten layers',evidence='010 first_cohomology and primitive_direct_image crops'),
dict(sign='partly reused typed letter',appearance='Typed d retained from dim; handwritten 2 before it and prime above/right; im(...) cancelled',convention=r'\handwritten{2}d^{\handwritten{\prime}}\deleted{...}',evidence='010 degree_correction crop')]

checks=[]
for rr in ['R1','R2','R3']:
    for ev in R[rr]['check_events']:
        e=copy.deepcopy(ev);e['statement_id']=e['statement_id']+'-'+rr
        e['type']='targeted proof check' if ('first-quadrant' in ev['type']) else 'computation or formal certificate'
        e['who']=f'GPT-6 Astra Pro (inherited model); effort not exposed; {rr}, scan010 independent run'
        if e['type']=='computation or formal certificate':e['outcome']='Hand calculation, no formal certificate: '+e['outcome']
        checks.append(e)
checks += [dict(statement_id='N010.2-leray-main',type='targeted proof check',outcome='Conditional formal check only: in a convergent first-quadrant cohomological spectral sequence, the edge-kernel class lies in filtration 1; gr^1 is E_infinity^{1,m-1}. There are no incoming differentials for r>=2 because 1-r<0, so this term embeds in E_2^{1,m-1}. No geometric specialization theorem or adic convergence result was proved.'),dict(statement_id='N010.3-degree-main',type='computation or formal certificate',outcome='Hand degree bookkeeping, no formal certificate: assuming the usual cup-product degree +N and trace degree -2d′, the output is m′+N-2d′. The visible 2d′, retained typed d, and uncertain erased X/Y were decided by the crop, not restored from this computation.')]

d=dict(scan=10,folder='A36-01',filename='A36-01_36_scan010.tex',brief='v01',decided_utc='',overview='All three independent readings covered the entire page. The main reader inspected every crop named below, plus the complete title crop and three new local crops. The old erased layers remain less secure than the live prose. H’s generic notes acknowledging an overwritten N are treated as evidence already present in H, not as a wholly omitted N. Mere absence of a handwriting wrapper around an otherwise identical filled-in arrow or membership sign is not counted as a different glyph reading; those provenance observations remain in the reader reports and inventory.',rows=rows,inventory=inv,unresolved=unresolved,notation=notation,abbreviations=[dict(form='th.',expansion='théorème'),dict(form='NB',expansion='nota bene')],check_events=checks,notes=[
'The handwritten title reads “Le théorème de Griffiths par voie algébrique.” and is singly underlined. The adjacent brown two-stroke mark is reproduced graphically; I), 1), and bracket interpretations remain unresolved. This is a typescript with handwritten corrections. It begins section 1, has no visible text-page number, date, or total page count, and bears archive sheet number 9 (comment only).',
'The page assumes a proper smooth f:Y→S with a handwritten insertion making S regular, and a twisted constant adic sheaf F. It defines a primitive class by vanishing in the indicated H^0 direct-image group and asserts equivalence with vanishing on a geometric fibre. It assigns u(x) to the Leray term of bidegree (1,m−1). The displayed coefficient in the inline group is graphically f-like; f|F is retained even though F is the named sheaf. The formal spectral-sequence part was checked conditionally as recorded in CHECK_EVENTS.tsv; the geometric equivalence was not proved.',
'A cohomological correspondence on Y x_S Y′ is said to induce a degree-changing map and to preserve primitive classes, with u(Z(x′))=Z(u(x′)). The live degree correction is 2d′, constructed by additions around a retained typed d. H’s “sans rien mettre à la place” is contradicted by the crop. The local degree-and-twist bookkeeping is consistent under the stated formal assumptions; the correspondence formalism and functoriality are not proved here. The continuation sentence ends at “par”.',
'Mathematics prompted reinspection of the coefficient f/F, the degree correction, the old Leray indices, and both layers of closing parentheses. In each case the final reading follows visible strokes rather than the expected formula. The prime-number glyph is rendered chi|ell at its first occurrence because of its crossed mechanical shape; this is a diplomatic alphabet uncertainty, not a claim that the author intended a different mathematical parameter.',
'No explicit authorial “à vérifier”, question mark on a step, or verbal reservation occurs. “NB” explains d′ and the Tate twist; “évidemment” accompanies the assertion about primitive classes and is not converted into a proof certificate.'
],legibility='Ordinary typescript is clear. The least secure material is the overwritten first-page coefficient and Leray layers, the brown prefix, and the old characters after Tate. C preserves substantially more revision history than H. H correctly cautions about a chi-shaped machine glyph, but wrongly says the degree replacement is absent and capitalizes a visibly lowercase prose z. The heavy E/Z alphabet choices remain uncertain.',workflow_observation='38 independent crops (12/13/13); main reused 15 distinct reader crops and made 3 new loci. Disagreements exposed alphabet, retained-letter and parenthesis-layer issues. Preamble path and macro-equivalence guidance added for scan011.')
(O/'decisions/scan010.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

views=[f'crops/scan010/R2/{x}.jpg' for x in ['heading_prefix','prime_letter','coefficient_ring','degree_correction','soit_correction','first_cohomology','primitive_direct_image','fiber_cohomology','leray_class','correspondence_class','tensor_pairing','tate_deletion','regulier']]+['crops/scan010/R3/title.jpg','crops/scan010/R3/soit_f_ell.jpg']+[f'crops/scan010/MAIN/{x}.jpg' for x in ['prose_z','primitive_underline','final_adique']]
(O/'decisions/scan010_main_views.json').write_text(json.dumps({'scan':10,'viewed_once':views,'overlap_note':'R2 heading_prefix settled the brown strokes; R3 title was subsequently used for the different locus of the complete title text. R2 soit_correction settled old t; R3 soit_f_ell was used for the adjacent prime glyph. Neither decided locus was re-cropped.'},indent=2))
print('Wrote final scan010 and',len(rows),'decision rows')
