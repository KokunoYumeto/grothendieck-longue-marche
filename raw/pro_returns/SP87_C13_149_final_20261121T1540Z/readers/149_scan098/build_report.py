import json
from pathlib import Path
p=Path('SP87_C13_149_work/readers/149_scan098')
boxes=json.loads((p/'crop_boxes.json').read_text())
def cr(n):return 'crops/149_scan098_'+n+'.png'
changes=[]
def ch(place,c,h,final,evidence,n,kind='misread word',ac=False,ah=True,conf='high',mh=False,con=False):
 changes.append(dict(place=place,c=c,h=h,final=final,evidence=evidence,crop=cr(n),box=boxes[n],confidence=conf,kind=kind,against_c=ac,against_h=ah,marked_in_h=mh,consequential=con))
ch('098-margin-aura','aura','aurait','aura','The marginal word ends with the short a-like return after aur; there is no final t ascender or cross stroke.','margin')
ch('098-margin-model',r'le modèle complet régulier can. de $K$ sur $k\ldots$',r'une courbe régulière sur $k$ \ill{}',r'le mod\unsure{è|e}le complet régulier can. de $K$ sur $k\ldots$','The rotated note has separate le, modèle, complet, régulier and can. with its stop, then de K sur k and three dots. Modèle has the d/l stems; complet has its p descender and final t. The accent zone in modèle is crossed by the preceding prendre descender, so the preferred accented reading is locally doubtful. The masculine régulier ending does not contain the extra final e of H.','margin',conf='medium',mh=True)
ch('098-alors','alors','tous','alors','The first word has the tall looped l after a, then a small o and a detached low r-s run. No t begins it.','alors')
ch('098-ce','ce','[nothing]','ce','Between de and k is an open c-like loop joined to a low e return; it is a distinct word.','ce','omission')
ch('098-first-sous-groupes','de sous-groupes','[nothing]','de sous groupes','The d/e, sous and the long-descending g with groupes continuation are readable. Between sous and groupes is an empty gap, without a separate hyphen; C’s punctuation is not supplied.','sous_groupes','omission',ac=True)
ch('098-dans','dans','des','dans','After the overdrawn subgroup symbol, d is followed by a long compressed a-n run and a turned s ending before E_K.','Delta_dans_E')
ch('098-pour-sa','(pour sa',r'(\ill{} [first part]','(pour sa','A left parenthesis precedes the long p stem; the o/u/r strokes and separate compressed sa are visible before the line break to structure.','pour_sa',r'readable ink left as \ill{}',mh=True)
ch('098-structure-celle',r'structure : \unsure{celle|cette} $=$',r'\ill{} [continuation]',r'structure : \unsure{celle|cette} $=$','The two t stems in structure and its intervening c are visible; a two-dot colon follows. The next word has two uncrossed middle rises, favouring celle over cette; the segmentation remains uncertain. Two short parallel strokes at its right are retained as the written equals short form.','structure_celle',r'readable ink left as \ill{}',conf='medium',mh=True)
ch('098-interieure',r'\inserted{\unsure{intérieure|extérieure}}',r'\add{inertie}',r'\inserted{intérieure}','The raised word starts with a short i stroke/dot and a low n run before the tall t; there is no crossing x after an initial e. The remaining compressed letters favour intérieure. Its curved leader descends to the gap before the following word.','interieure_relation',conf='medium',con=True)
ch('098-relation','relation','relative',r'\unsure{relation|relative}','After rela-t and the dotted i region, the low final run favours an open o followed by n, but can also be read v-e. The word remains live beneath the insertion leader; preserve the lexical alternative.','interieure_relation',conf='medium')
ch('098-et-les-N-qui',r'\inserted{et les $N_{s\prime}$ qui}',r'et les $N_{s\prime}$ \ill{}',r'\inserted{et les $N_{s\prime}$ qui}','The raised line reads et les, a clear N with lower s and separate prime, then qui with its q descender and final i dot. It stands above the cancelled initial qui and supplies the new subject before sont.','et_les_N_qui','insertion or placement',mh=True,con=True)
ch('098-qui-sont-justement',r'\deleted{qui} sont justement',r'\ill{}',r'\deleted{\unsure{qui}} sont justement','The small initial word is crossed, with a q-like head and descending return still visible; its remaining letters are obscured, so qui is retained doubtfully. Sont and the following j-descender, compressed ustemen run and terminal t return are live. The long return belongs to justement, not a cancellation of that word.','qui_sont_justement',r'readable ink left as \ill{}',conf='medium',mh=True)
ch('098-second-sous-groupes','sous-groupes','sous-groupes','sous groupes','The second occurrence has separate sous and groupes, with a blank gap between their terminal/initial strokes. No detached hyphen appears in the gap.','normalisateurs','text not on the page',ac=True)
ch('098-normalisateurs',r'\deleted{normalisateurs}','[nothing]',r'\deleted{\unsure{normalisateurs}}','A horizontal strike crosses the lower word. The initial low n/orm/a sequence and the l and t ascenders support normalisateurs, but the strike merges several middle and final strokes; the complete word is therefore retained with a local doubt. It is below the live sous groupes phrase.','normalisateurs','deletion state',conf='medium')
ch('098-inertie-decomposition',r'\deleted{inertie} \inserted{décomposition}','décomposition',r'\deleted{inertie} \inserted{décomposition}','The lower inertie has a cancellation crossing its letters. Décomposition is written distinctly above it, with the long p descender and the later t/i sequence. H retains the replacement but loses the cancelled word and raised state.','inertie_decomposition','deletion state',con=True)
ch('098-de-tantot','de tantôt','relatifs','de tantôt','A separate looped de precedes the t-a-n-t-ô-t sequence; a detached curved accent is visible over the o position. The following mark is a comma.','de_tantot')
ch('098-live-extension',r'\deleted{l\textquoteright extension}',"l'extension", "l'extension",'The long curved stroke lies above l’extension, passing above the ordinary letter bodies and ending after the word. It is the attachment leader of de N_s′ sur, not a strike through l’extension. The word is live.','extension_N','deletion state',ac=True,ah=False,con=True)
ch('098-de-N-sur',r'\inserted{de $N_{s\prime}$ sur}',r'des $N_{s\prime}$ sur',r'\inserted{de $N_{s\prime}$ sur}','The raised first word is d plus a low e return, without a terminal s. The N, lower s-prime and sur are clear. The curved leader attaches the phrase after live l’extension, before the main-line des on the following line.','extension_N','insertion or placement',con=True)
ch('098-ouvert',r'\underset{\inserted{\text{ouvert}}}{\subset}',r'\subset',r'\underset{\inserted{\text{ouvert}}}{\subset}','Ouvert is written below the inclusion sign; its initial oval o and u/v run, followed by the terminal r/t strokes, are separate from the main-line formula. It labels the inclusion.','inclusion_ouvert','omission',con=True)
ch('098-inclusion-K',r'\mathcal E_{\unsure{K|k}}',r'\mathcal E_k',r'\mathcal E_K','Read with the full E_k(s) subset E_K formula: the target index has a straight stem and two sharp oblique arms. This differs from the rounded shoulder and return of the small k in the left k(s), and from E_k in the preceding parenthesis. The capital is kept literally.','inclusion_ouvert','misread symbol or index',con=True)
ch('098-trailing-sur','sur',r'\ill{}','sur','A live s followed by u and a turned r stands after the inclusion target and before the parenthesis beginning sections. It is not crossed or joined to the lower ouvert label.','inclusion_ouvert',r'readable ink left as \ill{}',mh=True)
ch('098-sections-donc','(sections donc','(sections','(sections donc','Following sections is a separate word with looped d and a low o-n-c run. The word is present before the quoted phrase on the next line.','sections_donc','omission')
ch('098-composer','composer','comparer','composer','After com and the long p descender, the small o is followed by the angular s and e-r return. There is no a-r sequence after p.','composer')
ch('098-f-replacement',r'\deleted{$f$} \inserted{la section rat. $f$ de $U_K$ sur $S$}',r'la section rat. $f$ de $U_K$ sur $S$',r'\deleted{$f$} \inserted{la section rat. $f$ de $U_K$ sur $S$}','The old f remains visible as a long stem, descender and crossbar beneath separate dense cancellation strokes. The replacement is on a raised line; its leader curves down to the old subject position. Rat. has its detached abbreviation stop; the inserted formula reads f de U_K sur S. The underline beneath définie is separately visible and retained.','subject_f','deletion state',con=True)
ch('098-aussitot','aussitôt','[nothing]','aussitôt','The word begins the next main baseline: the a/u run is followed by the two s strokes, dotted i and tall t stems. A separate accent stroke is present over the o position.','aussitot','omission')
ch('098-section-partielle',r'section \inserted{partielle}',r'restriction \uncertain{partielle}',r'section \inserted{partielle}','The main-line word begins with s and has no re-stric prefix before the t/i/on sequence. Partielle is written above it with distinct final l-l rises; a curved leader returns to the gap before obtenue, placing partielle after section.','section_partielle',mh=True)
ch('098-au-dessus',r'$\mathcal E_{U_K}$ au dessus de',r'$\mathcal E_{U_K}$ \ill{} classe de section',r'$\mathcal E_{U_K}$ au dessus de','The complete group term has U with nested angular K. The words after it are compressed au, then the looped d and e-s-s-u-s sequence of dessus, then de. No further section is written before E_k(s) on the next line.','E_UK_dessus',mh=True)
ch('098-hook-arrow',r'\mathcal E_{k(s)}\hookrightarrow\mathcal E_{\unsure{K|k}}',r'\mathcal E_{k(s)}\to\mathcal E_K',r'\mathcal E_{k(s)}\hookrightarrow\mathcal E_K','The left end of the shaft curls upward into an open hook; the right end has two angular arrowhead arms. The target has a live sharp capital K, though it is retraced over a rounded earlier stroke. No separable earlier letter is invented.','arrow_E','misread symbol or index',con=True)
ch('098-no-elle','est aussi',r'est \uncertain{elle aussi}','est aussi','The first word has a retraced e/s body and a separate tall t. It is followed by aussi directly, across a blank word gap; no elle with l ascenders is present there.','est_aussi','text not on the page',mh=True)
ch('098-deleted-elle-est',r'\deleted{elle est}',r'\struck{\ill{}}',r'\deleted{elle est}','The strike passes through both words, but the initial e and two l ascenders in elle, followed by the e/s run and terminal t of est, remain visible.','elle_est',r'readable ink left as \ill{}',mh=True)
ch('098-en-tant-op',r"(en tant qu'op.",r'\add{à} \struck{\ill{}} \uncertain{quasi-p.} \add{près} (action',r"(en tant qu'op.",'After the left parenthesis and en, the two t uprights and compressed a-n run form tant. Its long crossing/return is continuous with the t strokes, without an independent cancellation. The next word has q, u, apostrophe, small o, descending p and a detached stop. There are no separately written à, près or action in this place.','en_tant_op',mh=True,con=True)
ch('098-ext-stop-effective',r'\deleted{ext.} \inserted{effective}','[not transcribed as these words/states]',r'\deleted{ext}. \inserted{effective}','The lower abbreviation has a strike through e-x-t. Its separate round stop lies to the right, beyond the cancellation endpoint, and remains uncrossed. Effective is raised above, with two distinct f stems and the later t/i/v/e sequence; its curved leader attaches before sur. The surviving stop therefore stands outside the deletion macro.','effective','deletion state',ac=True,con=True)
ch('098-deleted-est',r'\deleted{\unsure{est}}','est',r'\deleted{\unsure{est}}','After pi and the right parenthesis is a crossed word with an open e and dense final s/t-region. The strike is real, but the ending is too overlapped to resolve C’s existing est doubt. H treats est as live.','pi_est','deletion state',conf='medium')
ch('098-nest-autre',"n'est autre que",'induite par',"n'est autre que",'The first cluster has n, an apostrophe and the compressed est ending. Autre is a separate low word with its crossed t, followed by que with the long q descender. It is not induite par.','n_est_autre',con=True)
ch('098-folio97',r'\margin{97}','[nothing]',r'\margin{97}','The fine lower-left figures have a closed 9 head and long tail followed by an angular, cross-stroked 7. They are in another unnamed hand. H’s trailing editorial note is not manuscript text.','folio97','omission')
# Keep witness excerpts free of an invented quotation command.
for v in changes:
 for key in ('c','h','final'):
  v[key]=v[key].replace(r'l\textquoteright extension',"l'extension")
marks=[]
def mark(i,d,r,e,n,co):marks.append(dict(id=i,decision=d,reading=r,evidence=e,crop=cr(n),box=boxes[n],confidence=co))
mark('M1287','undecided',r'\unsure{\Delta_{s\prime}|I_{s\prime}}','The full subgroup/dans/E_K crop contains a distinct triangular outline with a base, but also a top crossbar, an inner upright and dense upper-right overdraw. The live triangle is preferred; no separate cancelled predecessor can be read securely enough to transcribe as a deleted I. The s-prime index is visible.','Delta_dans_E','medium')
mark('M1288','undecided',r'\unsure{celle|cette}','The pair of middle rises lacks t crossbars and favours celle. The tall initial curve and compressed low endings make segmentation uncertain; retain C’s two readings instead of substituting a new abbreviation on syntax alone.','structure_celle','medium')
mark('M1289','first','intérieure','The raised word has an initial short i and low n before the tall t, not the e plus crossing x required for extérieure. The remaining letters are compressed, so confidence remains medium. Its leader attaches before the following live word.','interieure_relation','medium')
mark('M1290','first','K','In the complete inclusion formula, the target index has a straight stem and two angular branches. The left k(s) and the preceding E_k supply visible rounded lowercase controls on this same page. The literal capital is retained irrespective of the expected base.','inclusion_ouvert','high')
mark('M1291','first','K','In the complete hooked-arrow formula, the target index is a heavily retraced capital K with sharp upper and lower branches. A rounded under-stroke does not license a separately deleted k. The left index k(s) remains lowercase.','arrow_E','high')
inventory=[]
def inv(el,ki,pos,first,hand='his hand'):inventory.append(dict(element=el,kind=ki,position=pos,first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes'))
inv('main-paragraph','text','main body, nineteen principal baselines','un corps k, alors … Dans')
inv('slanted-margin','margin note','upper-left margin, oblique writing, x20–410 y20–525','On aura intérêt ici …')
inv('overdrawn-subgroup-symbol','text','baseline 5, before dans E_K','Delta/I with s-prime; unresolved overdraw state')
inv('interieure-addition','insertion','above baseline 6, leader before relation','intérieure')
inv('et-les-N-qui-addition','insertion','above beginning of baseline 7','et les N_s′ qui')
inv('cancelled-qui','deletion','beginning of baseline 7 below raised subject','qui [doubtful]')
inv('cancelled-normalisateurs','deletion','lower than live sous groupes, near right of baseline 7','normalisateurs [doubtful]')
inv('cancelled-inertie','deletion','beginning of baseline 8','inertie')
inv('decomposition-replacement','insertion','above cancelled inertie','décomposition')
inv('de-N-sur-addition','insertion','above end of baseline 9; leader lands after live l’extension','de N_s′ sur')
inv('ouvert-label','insertion','below inclusion in baseline 10','ouvert')
inv('cancelled-f','deletion','after où at beginning of baseline 13','f')
inv('section-rat-replacement','insertion','above baseline 13, leader to cancelled f','la section rat. f de U_K sur S')
inv('partielle-addition','insertion','above baseline 15, leader between section and obtenue','partielle')
inv('cancelled-elle-est','deletion','baseline 17, following et','elle est')
inv('cancelled-ext','deletion','baseline 17, after op.; terminal stop outside strike','ext')
inv('effective-replacement','insertion','above ext, leader before sur','effective')
inv('cancelled-est','deletion','baseline 18 after pi and right parenthesis','est [doubt retained]')
inv('folio97','margin note','bottom-left margin','97','another unnamed hand')
second=[]
def sb(k,b,r):second.append(dict(box=f'B098_{len(second)+1:02d}',kind=k,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=r))
def sc(n,k,r):sb(k,boxes[n],r)
sc('margin','margin note',r'On aura intérêt ici de prendre pour $S$ le mod\unsure{è|e}le complet régulier can. de $K$ sur $k\ldots$')
sc('alors','different word','alors les')
sc('ce','different word',r'de ce $k$')
sc('sous_groupes','different words','de sous groupes')
sc('Delta_dans_E','doubtful formula',r'$\unsure{\Delta_{s\prime}|I_{s\prime}}$ dans $\mathcal E_K$')
sc('pour_sa','different words','(pour sa')
sc('structure_celle','doubtful words',r'structure : \unsure{celle|cette} $=$')
sc('interieure_relation','insertion and different word',r'\inserted{intérieure} \unsure{relation|relative}')
sc('sur_Ek','formula and punctuation',r'sur $\mathcal E_k\ldots$),')
sb('complete parenthesis',[305,465,1620,755],r'(pour sa structure : \unsure{celle|cette} $=$ \inserted{intérieure} \unsure{relation|relative} sur $\mathcal E_k\ldots$),')
sc('et_les_N_qui','insertion',r'\inserted{et les $N_{s\prime}$ qui}')
sc('qui_sont_justement','deletion and text',r'\deleted{\unsure{qui}} sont justement')
sc('normalisateurs','deletion and words',r'les sous groupes \deleted{\unsure{normalisateurs}} de')
sc('inertie_decomposition','deletion and insertion',r'\deleted{inertie} \inserted{décomposition} de')
sc('de_tantot','different words','de tantôt,')
sc('extension_N','live text and insertion',r"l'extension \inserted{de $N_{s\prime}$ sur}")
sc('inclusion_ouvert','complete formula and inserted label',r'$\mathcal E_{k(s)}\underset{\inserted{\text{ouvert}}}{\subset}\mathcal E_K$ sur')
sc('sections_donc','different words','(sections donc')
sc('composer','different word','composer')
sc('subject_f','deletion and insertion',r"où \deleted{$f$} \inserted{la section rat. $f$ de $U_K$ sur $S$} est \uline{définie} en")
sc('aussitot','different word','aussitôt')
sc('section_partielle','insertion and different word',r'section \inserted{partielle} obtenue')
sc('E_UK_dessus','formula and different words',r'$\mathcal E_{U_K}$ au dessus de')
sc('arrow_E','complete formula',r'$\mathcal E_{k(s)}\hookrightarrow\mathcal E_K$')
sc('est_aussi','different words','est aussi')
sc('elle_est','deletion',r'et \deleted{elle est}')
sc('en_tant_op','different words',r"(en tant qu'op.")
sc('effective','deletion and insertion',r'\deleted{ext}. \inserted{effective} sur')
sc('pi_est','formula fragment and deletion',r'$\pi$) \deleted{\unsure{est}}')
sb('complete parenthesis and deletion',[290,1930,1560,2255],r"(en tant qu'op. \deleted{ext}. \inserted{effective} sur $\pi$) \deleted{\unsure{est}}")
sc('n_est_autre','different words',"n'est autre que")
sc('folio97','handwritten number','97')
coverage={
'D0486':('editorial scan marker, not source wording',None),
'D0487':('source aura without final t','098-margin-aura'),
'D0488':('complete marginal model phrase recovered; accent of modèle locally doubtful','098-margin-model'),
'D0489':('source alors','098-alors'),
'D0490':('source ce is present','098-ce'),
'D0491':('source de sous groupes; no supplied hyphen','098-first-sous-groupes'),
'D0492':('Delta/I remains unresolved M1287; actual dans/des wording corrected','098-dans'),
'D0493':('parenthetical words and raised intérieure read in their original order','098-pour-sa; 098-structure-celle; 098-interieure; 098-relation'),
'D0494':('both witnesses encode the three written dots; macro-token difference only',None),
'D0495':('raised subject with qui, cancelled lower qui and live sont justement','098-et-les-N-qui; 098-qui-sont-justement'),
'D0496':('cancelled word retained with local doubt','098-normalisateurs'),
'D0497':('cancelled inertie and raised replacement preserved','098-inertie-decomposition'),
'D0498':('de tantôt with visible accent and comma','098-de-tantot'),
'D0499':('de without s in raised phrase; l’extension is live, against C’s state','098-de-N-sur; 098-live-extension'),
'D0500':('lower ouvert label transcribed and attached to inclusion','098-ouvert'),
'D0501':('literal capital K and live trailing sur','098-inclusion-K; 098-trailing-sur'),
'D0502':('donc is present; quotation encoding is editorial','098-sections-donc'),
'D0503':('same words; double-quote/guillemet representation only, established source convention retained',None),
'D0504':('composer, not comparer','098-composer'),
'D0505':('cancelled f and raised replacement state preserved','098-f-replacement'),
'D0506':('aussitôt is present','098-aussitot'),
'D0507':('section, plus the raised partielle insertion','098-section-partielle'),
'D0508':('au dessus de read after full E_UK formula','098-au-dessus'),
'D0509':('H extra section absent in this source phrase','098-au-dessus'),
'D0510':('left hook is present on the arrow, beyond pure macro-token difference','098-hook-arrow'),
'D0511':('M1291 resolves to first K, agreeing with H’s preferred letter; certainty-only resolution',None),
'D0512':('no elle between est and aussi','098-no-elle'),
'D0513':('readable cancelled elle est and the live parenthesis, without H’s added phrases','098-deleted-elle-est; 098-en-tant-op'),
'D0514':('en tant qu’op.; ext cancellation scope and effective replacement','098-en-tant-op; 098-ext-stop-effective'),
'D0515':('est is cancelled; live n’est autre que follows','098-deleted-est; 098-nest-autre'),
'D0516':('folio97 is source; H’s trailing note about writing is editorial and excluded','098-folio97')}
unresolved=[
 dict(place='M1287',reading=r'\Delta_{s\prime}',alternatives=r'I_{s\prime}; overdraw state remains unresolved, with no safely separable cancelled predecessor',confidence='medium'),
 dict(place='M1288',reading='celle',alternatives='cette; a less secure segmentation of the surrounding strokes as la plus a barred-m short form was considered but not substituted',confidence='medium'),
 dict(place='098-relation',reading='relation',alternatives='relative',confidence='medium'),
 dict(place='098-margin-model-accent',reading='modèle',alternatives='modele; preceding prendre descender enters the accent zone',confidence='medium'),
 dict(place='098-qui-sont-justement',reading='cancelled qui',alternatives='the final letters beneath the heavy strike are not separately recoverable',confidence='medium'),
 dict(place='098-normalisateurs',reading='cancelled normalisateurs',alternatives='several middle and final strokes are merged with the strike',confidence='medium'),
 dict(place='098-deleted-est',reading='cancelled est',alternatives='dense crossing obscures the final letter sequence; retained C doubt',confidence='medium')]
notes=("Content summary: This leaf treats the residue fields k(s) of non-generic points as finite extensions of k and associates conjugacy classes of subgroups of E_K with points s of S. It identifies the N_s′ with the decomposition subgroups discussed in the prose, considers sections of their extensions over E_k(s), and composes such sections with a given section. For a rational section f of U_K over S defined at s, the author claims that the resulting partial section is of the first kind and, as an effective operation on pi, is the one defined by f(s) in U_s(k(s)). A slanted marginal note proposes taking S to be the canonical regular complete model of K over k. The page ends with the isolated continuation word Dans. "
"Layout and source work: one main prose paragraph on nineteen principal baselines, an oblique upper-left marginal note and another-hand folio97 below left. No author page number, display, diagram or drawing was found. The whole and both supplied halves were each read once, including agreed words; thirty unique crops were saved and inspected. The margin crop was rotated clockwise 39 degrees; its original rectangle is retained in crop_boxes.json and the rotation in crop_rotations.json. All other crop boxes are in original pixels. "
"State and punctuation decisions: l’extension is live. Its apparent cancellation in C is a curved insertion leader above the letters, attaching de N_s′ sur after the word. The lower ext has crossed letters but a separate uncrossed stop beyond the strike, hence deleted ext followed by a live stop and the raised effective. The long stroke in tant belongs to its t crossing/return, so en tant remains live. The cancelled est after pi remains doubtful. The cancelled initial qui and normalisateurs acquire local reading doubts because the strikes merge letters. The underline on définie is retained. Both sous groupes occurrences have empty gaps, without a written hyphen. Tantôt and aussitôt each have an actual accent stroke; the modèle accent is uncertain because the preceding descender enters that zone. The three dots after E_k and after marginal k are retained, as are the comma after the first parenthesis, the period after donnée and the final point before Dans. "
"Notation cautions: the subgroup symbol has a triangular live-looking outline, top crossbar/upright and dense upper-right overdraw. This is covered by a whole-symbol Delta/I doubt; no earlier deleted letter is invented. Both disputed targets are literal capital K, supported by sharp branches and same-page contrasts with rounded lowercase k in k(s) and E_k. The lower target K is retraced over a rounded stroke, but a separate deleted k is not recoverable. The capital K readings may conflict with an expected common base in the proposed section construction; they are not normalized. Likewise the extra live sur after the inclusion is not omitted for grammar. The low initial letter in obtenue and the e/s body of est are retraced without a securely separable earlier word. A tiny isolated dot near the lower target K has no secure punctuation role and is not promoted to a formula symbol. The equals short form is preserved; the uncertain celle/cette segmentation is not replaced by a barred-m abbreviation on grammatical expectation. "
"Mathematical scope: only source reading, attachment tracing and same-page notation comparisons were performed. No proof of the assertion about specialization, first-kind sections, conjugacy classes or effective actions was attempted or used to force a reading. The check_events list is therefore empty. H’s final comment about rapid writing is editorial, not source text.")
report=dict(scan=98,line_count=19,changes=changes,marks=marks,inventory=inventory,second_boxes=second,notes=notes,check_events=[],hand_observations=[
 dict(habit='A broad insertion leader can resemble a cancellation when it passes above ascenders.',pages=[98],evidence='The de N_s′ sur curve arches above l’extension and lands after it; the word remains live.',witness_errors='C marks l’extension deleted.'),
 dict(habit='The stop of an abbreviation can survive outside the actual strike.',pages=[98],evidence='A distinct round stop stands beyond the cancellation endpoint of ext, before the effective leader.',witness_errors='C includes the stop within deleted ext.'),
 dict(habit='Angular capital K and rounded lowercase k must be compared locally.',pages=[98],evidence='The inclusion and hooked-arrow targets have sharp branches; k(s) and the parenthetical E_k have rounded shoulders.',witness_errors='C leaves both capitals in K/k doubts; H prints lowercase k for the upper target.'),
 dict(habit='Retracing can leave a prior-looking stroke without a recoverable deleted symbol.',pages=[98],evidence='The Delta/I symbol has triangle, bar and upright; the lower K includes a rounded under-stroke.',witness_errors='No invented predecessor is inserted in the transcription.'),
 dict(habit='Long t crossings and low letter runs can resemble deletion or extra words.',pages=[98],evidence='The two t stems of tant are joined by a long return; qu’op. is a compact q-u-apostrophe-o-p-stop sequence.',witness_errors='H gives à, quasi-p., près and action in this region.'),
 dict(habit='Compound words may be separated by a blank gap without a written hyphen.',pages=[98],evidence='Both sous groupes occurrences lack a detached hyphen.',witness_errors='C supplies hyphens at both occurrences; H supplies one in the occurrence it reads.')],notation_additions=[],abbreviations=[
 dict(form='can.',expansion='canonique'),dict(form='pt',expansion='point'),dict(form='gén.',expansion='générique'),dict(form='=',expansion='même'),dict(form='rat.',expansion='rationnelle'),dict(form='op.',expansion='opération'),dict(form='ext.',expansion='extérieure; letters cancelled, terminal stop uncrossed')],unresolved=unresolved,diff_coverage=[dict(diff_id=k,disposition=v[0],change_place=v[1])for k,v in coverage.items()])
(p/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
draft=r'''\scanpage{98}
\margin{On aura intérêt ici de prendre pour $S$ le mod\unsure{è|e}le complet régulier can. de $K$ sur $k\ldots$}
un corps $k$, alors les $k(s)$ (pour $s\ne\eta$, pt gén.) apparaissent comme des extensions finies de ce $k$, et tout $s\in S$ définit une classe de conjugaison de sous groupes $\unsure{\Delta_{s'}|I_{s'}}$ dans $\mathcal E_K$ (pour sa structure : \unsure{celle|cette} $=$ \inserted{intérieure} \unsure{relation|relative} sur $\mathcal E_k\ldots$), \inserted{et les $N_{s'}$ qui} \deleted{\unsure{qui}} sont justement les sous groupes \deleted{\unsure{normalisateurs}} de \deleted{inertie} \inserted{décomposition} de tantôt, et on peut regarder les sections de l'extension \inserted{de $N_{s'}$ sur} des $\mathcal E_{k(s)}\underset{\inserted{\text{ouvert}}}{\subset}\mathcal E_K$ sur (sections donc ``de deuxième espèce'') et les composer avec la section donnée. Dans le cas où \deleted{$f$} \inserted{la section rat. $f$ de $U_K$ sur $S$} est \uline{définie} en $s$, il résulte aussitôt de ce qui précède que la section \inserted{partielle} obtenue de $\mathcal E_{U_K}$ au dessus de $\mathcal E_{k(s)}\hookrightarrow\mathcal E_K$ est aussi de première espèce, et \deleted{elle est} (en tant qu'op. \deleted{ext}. \inserted{effective} sur $\pi$) \deleted{\unsure{est}} n'est autre que celle qui est définie par le pt $f(s)\in U_s(k(s))$. Dans
\margin{97}
'''
(p/'draft.tex').write_text(draft)
print(json.dumps({k:len(report[k])for k in ['changes','marks','inventory','second_boxes','unresolved','diff_coverage']}))
