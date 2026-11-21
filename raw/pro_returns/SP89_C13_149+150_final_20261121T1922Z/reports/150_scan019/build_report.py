from pathlib import Path
import json
import re

ROOT=Path('/workspace/scratch/8759b8008681')
PAGE='150_scan019'
OUT=ROOT/'work/reports'/PAGE
C=(ROOT/'packets'/PAGE/'C.tex').read_text()
H=(ROOT/'packets'/PAGE/'H.tex').read_text()
D=(OUT/'draft.tex').read_text()
DC='\n'.join(line for line in D.splitlines() if not line.lstrip().startswith('%'))
BOX=json.loads((OUT/'crop_boxes.json').read_text())

def span(text,start,end):
    first=text.index(start)
    return text[first:text.index(end,first)+len(end)]

changes=[]
def change(id,place,c,h,final,crop,evidence,against_c=False,against_h=True,
           confidence='high',kind='misread word',category='2',marked_in_h=False,consequential=False):
    assert c in C,(id,'C',c)
    assert h in H,(id,'H',h)
    assert final in DC,(id,'final source text',final)
    changes.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,
                        crop=f'crops/{PAGE}_{crop}.png',box=BOX[crop],confidence=confidence,
                        kind=kind,against_c=against_c,against_h=against_h,
                        marked_in_h=marked_in_h,consequential=consequential,error_category=category))

change('P01a','Opening line: au dessus','au dessus','au-dessus','au dessus','P01',
       'The short au ends in a low horizontal return. Blank paper separates that return from the looped d of dessus; no independent hyphen is written between the two words. The adjacent dotted T_i and dotted T each have a separate upper point; the first body is retraced, without a recoverable earlier glyph.',
       kind='abbreviation expanded or spelling modernised',category='8')
change('P02a','Second line: globalement cancellation',r'\deleted{globalement}',r'\emph{globalement}',r'\deleted{globalement}','P02',
       'One long stroke crosses the low letter bodies of globalement, from the g loop through the terminal return. Tall l/b/l traces and the g descender remain above/below it. This is a cancellation through the word, unlike the separate underline below famille on the preceding line.',
       kind='deletion state (struck given live or live given struck)',category='7')
change('P03a','Raised replacement for tubulaire',r'\inserted{conique}',r'\add{conique}',r'\inserted{cônique}','P03',
       'A separate short roof-shaped stroke stands over the o of the raised replacement; the i has its own smaller separate dot. The entire replacement is above cancelled tubulaire and attaches before the following plain T. The written spelling is cônique.',True,True,
       kind='abbreviation expanded or spelling modernised',category='8')
change('P04a','Main definition: on dit / il est','on dit\nil est',r"on dit \add{qu'il est}",'on dit\nil est','P04',
       'The next normal baseline starts with the dotted i and tall l of il, then est. No qu apostrophe sequence is written on that main baseline and no insertion leader adds it. The qu and long descender farther left belong to the diagonal marginal definition.',
       kind='text not on the page',category='9')
change('P04b','Main definition: written p.r. à',r'équisingulier p.r. à $(X_i)$',r'équisingulier pour les $(X_i)$',
       r'équisingulier p.r. à $(X_i)$','P04',
       'The descending p is followed by a separate stop, a short low r and its stop; a small accented à follows before the parenthesized X_i. The letters pour les are not written. The abbreviation is retained as p.r. à.',
       kind='abbreviation expanded or spelling modernised',category='8')
change('P04c','Following line: par rapport à',r"l'est par rapport à $(X_i\cap T\subset T)_i$",
       r"l'est pour les $(X_i\cap T\subset T)_i$",r"l'est par rapport à $(X_i\cap T\subset T)_i$",'P04',
       'Par has its descending p and low a/r continuation; rapport has the long paired p descenders, short low joins and terminal crossed t. A separate accented à follows. The complete parenthesis contains X_i, intersection, plain T, subset, plain T and an outer lowered i. The tiny detached point after the first T is much smaller than the written index i and has no established semantic attachment; it is documented as a pen remnant, without adding an operator or index.')
change('P05a','Cela implique: live main-line wording',r'Cela'+'\n'+r'implique que si',
       r'Cela \uncertain{implique} \struck{\ill{}} que si','Cela\nimplique que si','P05',
       'The main word has a dotted initial i, low m, descending p, tall l, another dotted i and the q/e ending of implique. There is no separable cancelled main-line token after it. The darker group below belongs to the diagonal second note’s p.r. à (X_i), whose attachment is completed in P16; the main q descender crosses that neighboring writing.',
       kind='deletion state (struck given live or live given struck)',category='7',marked_in_h=True)
change('P05b','Conditional premise: à la fois ouverte',r'une'+'\n'+r'partie à la fois ouverte et fermée de $Y$',
       r'une partie \uncertain{ouverte} et fermée de $Y$,',r'une'+'\n'+r'partie à la fois ouverte et fermée de $Y$','P05',
       'After partie there are an accented short à, a tall l with its a, and the long looped f, low oi and terminal s of fois. Ouverte follows with separate low rounded/angled bodies and a final t/e return. The final Y is not followed by a comma on this baseline. H omits à la fois and supplies that comma.',
       kind='omission',category='3',marked_in_h=True)
change('P06a','Beginning of the connectedness clause',r'\unsure{alors|et},',r'\add{et,}','alors,','P16',
       'P06 shows the long l/o/r/s body and following comma; P16 completes the initial connected a that was clipped at P06’s left edge. The whole word is alors, on the normal baseline, not the short et and not a raised insertion. This resolves C’s first alternative.',True,True)
change('P07a','Complete displayed alternative (14)',
       r'(14)\qquad X_i\cap\unsure{\bar T|T}=\varnothing\quad\underline{\text{ou}}\quad X_i\supset Y\ .',
       r'(14)\qquad X_i\cap T=\emptyset\quad\text{ou}\quad X_i\supset Y .',
       r'(14)\qquad X_i\cap T=\phi\quad\underline{\text{ou}}\quad X_i\supset Y\ .','P07',
       'The label is parenthesized 14. The left T has a retraced roof with an upper returning loop, but no independent horizontal overbar. The empty-set glyph is a small oval crossed by a long oblique descending stem, hence source phi. Ou has a separate lower underline. Both X subscripts are dotted i forms; the final point is detached far to the right. The whole formula was read before resolving C’s T alternative.',True,True,
       kind='misread symbol or index',category='1',consequential=True)
change('P08a','First diagonal marginal definition',
       span(C,"on dit qu'il est",r'les $X_i$.'),
       r'on dit \emph{strictement} \ill{} \ldots\ \emph{strict} \ldots\ ',
       span(DC,"on dit qu'il est",r'les $X_i$.'),'P08',
       'The note reads on dit qu’il est, with the q descender and apostrophe independent of the main il est. Strictement équisingulier and the later strictement each have a separate underline. Si de plus il est is live between them. The initial body of compatible is heavily retraced and remains doubtful. P16 completes the last clause: avec has a low a, angled v and e/c continuation; tous has its tall t and low o/u/s ending. Les X_i and its stop are visible below. H leaves most of this live note unread and shortens the second strictement to strict. C’s doubt is narrowed to compatible; avec tous is resolved, not silently supplied.',True,True,'medium',
       kind='readable ink left as \\ill{}',category='5',marked_in_h=True,consequential=True)
change('P09a','Second diagonal marginal statement',
       span(C,'Si $T$ équisingulier',r'$\lambda\in]0,1[$.'),
       r'si $T$ \uncertain{équisingulier} \ldots\ les $\lambda T$ \ldots\ $\lambda\in\,]0,1[$',
       span(DC,'Si $T$ équisingulier',r'$\lambda\in]0,1[$.'),'P09',
       'The first line begins Si T, then the accented initial, q/g descenders and long body of équisingulier. P16 completes the next p.r. à (X_i), including its comma; the overworked à is live and is not a cancelled word in the main text. The following line has lambda T, l apostrophe est, then strictement. Pour is separate on the lower continuation before lambda in the open interval ]0,1[. Both interval digits, both open brackets and the terminal point are visible. No les precedes lambda T.',
       confidence='medium',kind='omission',category='3',marked_in_h=True,consequential=True)
change('P10a','Cancelled circled item number',r'\deleted{\textcircled{\unsure{5}}}',
       r'(5)\note{numéro cerclé, surchargé.}',r'\deleted{\textcircled{\unsure{5}}}','P10',
       'A surrounding oval encloses the overwritten digit and is crossed by a broad zigzag extending upward into a dense loop. A 5-like upper turn and lower rounded body remain possible, but the crossing hides too much to resolve the digit. The entire circled item is cancelled. The upper black cluster is continuous with the cancellation and does not establish another separate number.',
       confidence='low',kind='deletion state (struck given live or live given struck)',category='7')
change('P11a','Lower paragraph: emphasis versus insertion leader',r'équisingulier'+'\n'+r'le long de $Y$',
       r'\emph{équisingulier le long de $Y$}',r'équisingulier'+'\n'+r'le long de $Y$','P11',
       'The long stroke above équisingulier bends down before its initial é and back up below the inserted parenthesis; P17 contains the whole stroke and all of (globalement). It is the insertion’s attachment leader, not an underline of équisingulier. The next baseline le long de Y likewise has no underline. H’s emphasis is not reproduced as a source underline; the literal wording itself agrees.',
       kind='other',category='10')
change('P12a','Lower premise: source cônique spelling',r"s'il existe un voisinage conique",
       r"s'il existe un voisinage conique",r"s'il existe un voisinage cônique",'P12',
       'A distinct short arch is above the o of cônique, separate from the neighboring i dot and q descender. The lower occurrence therefore shares the accented spelling of the raised replacement at P03.',True,True,
       kind='abbreviation expanded or spelling modernised',category='8')
change('P12b','Cancelled word before the dotted T',r'\deleted{\unsure{de}}',r'conique \struck{\ill{}}',
       r'\deleted{\unsure{de}}','P12',
       'The short group before the T has a looped initial and low returning body compatible with de. A horizontal crossing runs through that body, and parts of the letters remain inseparable from it. The inherited de candidate is retained under doubt within the cancellation.',
       confidence='medium',kind='readable ink left as \\ill{}',category='5',marked_in_h=True)
change('P12c','Literal dotted T in the neighborhood premise',r'$\unsure{\dot T|\bar T|T}$ de $Y$ dans $X$',
       r'$T$ de $Y$ dans $X$',r'$\dot T$ de $Y$ dans $X$','P12',
       'A strong separate filled point stands above the retraced T, with blank space between it and the letter’s single roof. The forked strokes below the roof are body overwork, not an additional bar. No strike cancels the upper point. This resolves C’s first alternative, dotted T. H acknowledges a point in its editorial note but omits it from the main formula; this row collates that omission, without treating the note as source text. The literal dotted form is retained despite its mathematical difficulty.',True,True,
       kind='misread symbol or index',category='1',consequential=True)
change('P13a','Cancelled preposition after p.r.',r'p.r. \deleted{à} $(X_i)$',
       r'p.r. \struck{\ill{}} \add{aux} $(X_i)$',r'p.r. \deleted{à} $(X_i)$','P13',
       'There is one short accented à body under a long crossing stroke between p.r. and the parenthesized X_i. The accent survives above the strike; no separately raised aux or independent x ending follows. H’s live aux insertion has no source counterpart.',
       confidence='medium',kind='deletion state (struck given live or live given struck)',category='7',marked_in_h=True)
change('P13b','Conclusion connector: auquel cas',r'--- auquel cas les $\lambda T$',
       r'-- ce qui équivaut à ce que les $\lambda T$',r'--- auquel cas les $\lambda T$','P13',
       'After the dash, the low a/u group, long q descender, e loop and tall l form auquel; cas follows as a short separate word before les lambda T. The longer ce qui équivaut à ce que sequence is absent. The source gives an ensuing consequence, not H’s expanded equivalence wording.',
       consequential=True)
change('P14a','Last line: sont = strictement',r'$(\lambda\in]0,1[)$ sont $=$ strictement équisinguliers.',
       r'($\lambda\in\,]0,1[$) soient \emph{strictement} équisinguliers.',
       r'$(\lambda\in]0,1[)$ sont $=$ strictement équisinguliers.','P14',
       'The verb has a short initial s, joined o/n body and terminal t return, without an added dotted i/e sequence. Two separate parallel bars follow it, the written equals-sign shorthand. Strictement has no independent underline. The open interval has 0, comma and 1 between ] and [, and a full stop follows équisinguliers. The ascenders also lie in the previously read native lower half.',
       consequential=True)
change('P15a','Thin lower-left foliation',r'\margin{18}',r'Le bas du feuillet est blanc.',r'\margin{18}','P15',
       'A thin slanted lead-in and upright make 1; two connected loops make 8. This small lower-left folio is in a lighter instrument than the main text. H’s editorial blank-bottom statement does not represent the written 18.',
       kind='omission',category='3')

decisions=[]
def decide(id,decision,reading,crop,evidence,confidence='high'):
    assert reading in DC,(id,reading)
    decisions.append(dict(id=id,cote='150',scan='19',decision=decision,reading=reading,
                          evidence=evidence,crop=f'crops/{PAGE}_{crop}.png',box=BOX[crop],confidence=confidence))
decide('M0348','first','alors','P16',
       'The completing frame contains the connected initial a and tall looped l, followed by the low o/r/s body and comma already visible in P06. The five-letter word is on the main baseline; it is not et or an insertion.')
decide('M0349','alternative',r'X_i\cap T=\phi','P07',
       'The complete formula has an overtraced T roof and upper return, but no separate overbar. The lower relation and crossed-loop empty-set phi are independently visible; the plain T alternative is accepted.')
decide('M0350','undecided',r'\unsure{compatible} avec tous','P16',
       'The compatible body is retraced across its beginning and several joins, so that word remains doubtful. Avec has its low a, angled v and e/c continuation; tous has a separate tall t and low o/u/s ending. Those last two words are resolved, narrowing the original three-word doubt.','medium')
decide('M0351','first',r'$\dot T$ de $Y$ dans $X$','P12',
       'The filled point above T is independently present and live, separated by blank paper from the single roof. The forked/retraced stem does not supply an overbar or a cancellation of the point. The source’s dotted form is retained.')

inventory=[]
def inventory_item(kind,position,content,hand='his hand'):
    inventory.append(dict(scan=PAGE,sheet_kind='text',hand=hand,element=f'E{len(inventory)+1:02d}',
                          kind=kind,position=position,first_words_or_objects=content,transcribed='yes'))
inventory_item('text','upper continuation, first three lines','mieux, si la famille … locally trivial family and extension to X_i in X')
inventory_item('text','first dotted T_i, P01','retraced forked T body with separate upper point and lowered i; no earlier token recovered')
inventory_item('deletion','second main line, P02','globalement, crossed through the word')
inventory_item('deletion','fourth main line, P03','tubulaire')
inventory_item('insertion','above tubulaire, P03','cônique, attached before T')
inventory_item('text','main definition, P04','on dit / il est équisingulier p.r. à (X_i); l’est par rapport à the intersection family')
inventory_item('text','tiny detached point after the first T inside the P04 parenthesis','unattached pen remnant documented in the adjacent comment; no operator or index supplied')
inventory_item('text','connectedness premise, P05–P06','Cela implique … à la fois ouverte et fermée … alors … l’on ait l’alternative')
inventory_item('deletion','after que in the connectedness clause, P06','whole X_i intersection Y')
inventory_item('display','display (14), P07','X_i intersection T equals phi, underlined ou, X_i superset Y; terminal far-right point')
inventory_item('margin note','first diagonal left-margin paragraph, P08/P16','on dit qu’il est strictement équisingulier … strictement compatible avec tous les X_i')
inventory_item('margin note','second diagonal left-margin paragraph, P09/P16','Si T équisingulier p.r. à (X_i), lambda T l’est strictement pour lambda in ]0,1[')
inventory_item('deletion','before the lower paragraph, P10','cancelled circled doubtful 5; crossing continues into an upper loop')
inventory_item('text','lower paragraph, P11–P14','On dit aussi que X,(X_i)_{i in I} est … équisingulier le long de Y … auquel cas …')
inventory_item('insertion','above lower équisingulier, P11/P17','(globalement), with a curved leader attaching before équisingulier')
inventory_item('deletion','before lower dotted T, P12','doubtful de under the crossing stroke')
inventory_item('text','lower neighborhood premise, P12','independent live point above retraced T, retained as dotted T')
inventory_item('deletion','after lower p.r., P13','à; no aux replacement')
inventory_item('margin note','bottom left, P15','18','thin pencil/other or undetermined hand')

audits=[]
def audit(kind,box,reading):
    assert reading in DC,('audit source scope',reading)
    audits.append(dict(box=f'B{len(audits)+1:02d}',kind=kind,xyxy=box,reading=reading))
audit('C/H different words',BOX['P01'],r'$\dot T_i\subset\dot T$ au dessus')
audit('struck passage',BOX['P02'],r'de $Y$ est \deleted{globalement} loc. triviale.')
audit('struck passage; insertion; C/H different words',BOX['P03'],
      r'voisinage \deleted{tubulaire}\inserted{cônique} $T$ de $Y$ dans $X$ : on dit')
audit('C/H different words',[353,470,1588,567],r'il est équisingulier p.r. à $(X_i)$, si $T$')
audit('C/H different words',[422,568,1295,679],r'par rapport à $(X_i\cap T\subset T)_i$')
audit('C/H different words; struck passage',[230,686,1537,838],r'implique que si $\forall i$, $X_i\cap Y$ est une')
audit('C/H different words',[230,821,1540,940],r'partie à la fois ouverte et fermée de $Y$')
audit('C/H different words',[190,940,414,1032],'alors,')
audit('struck passage',[1047,927,1655,1065],r"que \deleted{$X_i\cap Y$} l'on ait")
audit('handwritten number; doubtful formula',BOX['P07'],span(DC,'\\[\n','\n\\]'))
audit('margin note; C/H different words; less than high confidence departure',[18,435,565,1162],
      span(DC,r'\margin{on dit',r'les $X_i$.}'))
audit('margin note; handwritten number; C/H different words',[18,740,565,1510],
      span(DC,r'\margin{Si $T$',r'$\lambda\in]0,1[$.}'))
audit('struck passage; handwritten number',BOX['P10'],r'\deleted{\textcircled{\unsure{5}}}')
audit('insertion',BOX['P17'],r'\inserted{(globalement)}')
audit('C/H different words',[265,1508,1668,1614],r"le long de $Y$, s'il existe un voisinage cônique")
audit('struck passage; doubtful formula; C/H different words',[265,1605,1668,1710],
      r'\deleted{\unsure{de}} $\dot T$ de $Y$ dans $X$, qui est équisingulier')
audit('struck passage; C/H different words',[264,1708,1525,1830],
      r'p.r. \deleted{à} $(X_i)$ --- auquel cas les $\lambda T$')
audit('handwritten number; C/H different words',[274,1815,1674,1931],
      r'$(\lambda\in]0,1[)$ sont $=$ strictement équisinguliers.')
audit('margin note; handwritten number',BOX['P15'],r'\margin{18}')

doubts=[
    dict(place='P08/P16 first marginal definition',reading=r'\unsure{compatible}',alternatives='compatible; initial body and joins retraced',confidence='medium',
         reason='The letter sequence supports compatible, but its beginning is overwritten and several joins cannot be separated. There is no secure independent strike establishing deletion. Avec tous is readable and has been removed from the doubt scope.'),
    dict(place='P10 cancelled circled item',reading=r'\deleted{\textcircled{\unsure{5}}}',alternatives='5; digit not fully separable under the crossing',confidence='low',
         reason='Broad zigzags cross the central body and circle. A 5 remains possible, but the upper turn and lower loop are partly conflated with cancellation strokes; no additional numeral is inferred from the upper black loop.'),
    dict(place='P12 cancelled short word',reading=r'\deleted{\unsure{de}}',alternatives='de; letters partly obscured',confidence='medium',
         reason='A looped initial and low return support de, but the long strike merges with the letter bodies. The inherited uncertainty is preserved inside the deletion.'),
]
for item in doubts:
    assert item['reading'] in DC

notes=[
    {'id':'N01','text':'This is a continuation leaf without an author page number at its head. It has sixteen main text/display rows, two diagonal left-margin paragraphs, a cancelled circled item number before the lower paragraph, two raised replacements/insertions, and thin foliation 18 at the bottom left. The lower remainder is blank. The whole original and both supplied native halves were inspected once each. Seventeen saved crops were inspected once each: P16 completes unresolved right endpoints clipped in P08/P09, and root-requested P17 completes the ascenders and attachment leader of the mandatory insertion clipped by P11. These completion views do not repeat decided targets. All boxes use original 1682×2359 coordinates; P08/P09/P16 are rotated clockwise45 for reading. H’s page-order note, marginal-reading commentary and final editorial note are not source text.'},
    {'id':'N02','text':'The opening continuation speaks of local triviality of the family of dotted T_i within dotted T over Y, after cancelling globalement. It extends equisingularity to an ambient pair X,(X_i) by using a cone neighborhood T of Y and the family X_i intersect T. The connectedness sentence has an explicit premise that each X_i intersect Y is open and closed in Y, followed by alternative (14). The first marginal note defines strict equisingularity by additional strict compatibility with every X_i; compatible itself remains paleographically doubtful. The second margin and the end of the lower paragraph assert strictness for each scaled lambda T with 0<lambda<1. The lower paragraph adds (globalement) before equisingulier le long de Y. This note describes source claims; the proof and counterexample scopes are given separately.'},
    {'id':'N03','text':'Independent proof of (14) under the written clopen premise and the cone-action stability required by compatibility. Fix i and put A_i=X_i intersect Y. If Y is connected and A_i is both open and closed in Y, then A_i is empty or Y. If A_i=Y, the second alternative X_i superset Y holds. If A_i is empty and x belonged to X_i intersect T, stability under the zero scalar would put 0·x in X_i intersect T; the cone action sends 0·x into Y, contradicting A_i empty. Hence X_i intersect T is empty, giving the first alternative. The argument is pointwise in i and needs no finiteness of the family. Local triviality is unnecessary for this implication once the clopen premise and zero-action stability are supplied. It does not by itself prove that local triviality implies that premise.'},
    {'id':'N04','text':'Counterexample proposed by the root and independently verified here against the intrinsic-cone plus ambient-neighborhood interpretation supplied for this run. Let q=3/8, H=[0,1]×{0}, V={q}×[0,1], and X=H union V with its Euclidean subspace topology. Set Y={(0,0)} and T=[0,1/2]×{0}. T is a closed cone and an ambient neighborhood of Y, since it contains an open initial horizontal segment; the scalar action is mu·(t,0)=(mu t,0). Its specified outer boundary is dotted T={(1/2,0)}, so the map dotted T→Y is globally trivial. Take the family with its sole member X_1=X; the boundary family and compatibility requirement are then trivial. For lambda=3/4, the scaled cone is S=lambda T=[0,q]×{0}, its boundary is p=(q,0), and its intrinsic interior is [0,q)×{0}. The exterior X minus that intrinsic interior consists of the right horizontal branch [q,1]×{0} and the vertical branch {q}×[0,1], meeting only at p. Removing p separates this exterior into two nonempty open-and-closed components. Every neighborhood of p meets both components. If a cylindrical neighborhood of the singleton boundary existed, it would be homeomorphic as a pair to ({p}×[0,1],{p}×{0}); after deleting p its image would be connected, yet would meet both separated components. This is impossible. Thus S has no point collar in its exterior and fails strictness in the exterior-collar sense required by strict compatibility. This refutes the universal assertion N04.L that every lambda T, 0<lambda<1, is strict under those literal assumptions. A stronger standing requirement that the intrinsic interior be open in X, or an ambient collar condition at every radial level, would exclude this branched example; such a strengthened assertion is not what this counterexample refutes.'},
    {'id':'N05','text':'Scope check on the preceding counterexample. The same example does not refute existence of a sufficiently small strict equisingular cone neighborhood. For any radial endpoint r=lambda/2 different from q, choose delta>0 small enough that the horizontal interval [r,r+delta] avoids the branch point q and lies in [0,1]. It is a neighborhood of r in the corresponding exterior, and s↦(r+delta s,0) identifies it with a point collar. In particular every 0<lambda<3/4 has such a collar, and the original endpoint r=1/2 does as well. With X_1=X the collar-compatibility condition is automatic. The specific failure is the universal quantifier over all rescalings of a given T, including the critical lambda=3/4. H’s phrase “ce qui équivaut à ce que” is not written: the manuscript says “auquel cas”, so no extra equivalence is introduced into the transcription.'},
    {'id':'N06','text':'Literal notation diagnostic, separate from the collar counterexample. The final neighborhood premise reads “un voisinage cônique” followed by cancelled doubtful de and live dotted T “de Y dans X”. The upper point is physically separate and uncancelled. For the standard mapping-cylinder cone C(f) with outer boundary represented by B×{1} and base Y obtained from B×{0}, that outer boundary is disjoint from Y. If Y is nonempty, dotted T alone therefore cannot contain Y and cannot be a neighborhood of Y. Undotted T is the mathematically plausible intended object, but the transcript preserves the dotted form. N04 evaluates the intended cone-neighborhood assertion with T as the ambient cone, rather than treating this visible source slip as a new definition.'},
    {'id':'N07','text':'Reading diagnostics. Ordinary T roofs are not added bars; the first dotted T_i, the T in (14), and the lower dotted T have substantial body or roof overwork without a recoverable prior glyph. The tiny point after the first T in the P04 parenthesis has no secure notational attachment and is documented as a pen remnant, not converted into multiplication or a subscript. The darker group below main implique is the live à in the diagonal note, not a separate cancelled main word. The insertion leader of (globalement) is not an underline of équisingulier le long de Y. Both written cônique occurrences have a separate arch over o. The main grammar “on dit / il est” is left as written, without supplying qu’. The open intervals, source phi, underlined ou and written equals-sign shorthand are retained exactly.'},
]
check_events=[
    dict(statement_id=PAGE+'.N03',type='independent re-proof',outcome='Proved (14) from the explicit clopen premise, connectedness and stability under the zero scalar; no local-triviality or finiteness premise was used.'),
    dict(statement_id=PAGE+'.N04',type='refuted, with refined id',outcome='Independently checked the root-proposed branched-space example and its disconnected punctured exterior. It refutes the literal universal-all-rescalings version N04.L in the exterior-collar sense, with the stronger ambient-openness/collar qualification stated explicitly.'),
    dict(statement_id=PAGE+'.N05',type='targeted proof check',outcome='Constructed explicit horizontal collars at every noncritical endpoint in the same example, separating failure at lambda=3/4 from existence of small strict neighborhoods.'),
    dict(statement_id=PAGE+'.N06',type='targeted proof check',outcome='Checked that the specified outer boundary B×{1} is disjoint from the base Y in the mapping-cylinder cone; the literal dotted neighborhood premise cannot hold for nonempty Y under that notation.'),
]
notation=[
    dict(form=r'T,\dot T_i,\dot T',meaning='Cone object and its specified dotted boundary family; retain only separately written points and indices.',evidence='P01 has two independent upper points; P03/P04 have ordinary single-roof T forms; P07 has a retraced roof without an independent bar; P12 has a separate live point above its retraced T.'),
    dict(form=r'\phi',meaning="Empty set; ϕ : l’ensemble vide.",evidence='P07: small oval crossed by a long oblique descending stem in (14), rather than a slashed circular empty-set glyph.'),
    dict(form=r'\lambda T,\quad\lambda\in]0,1[',meaning='Scaled cone neighborhood and its open parameter range in both strictness assertions.',evidence='P09/P16 and P14: lambda, plain T, membership, zero/comma/one and the two open interval brackets are separately visible.'),
    dict(form=r'$=$ in prose',meaning='Written shorthand for même in sont = strictement équisinguliers.',evidence='P14: two distinct parallel horizontal strokes stand after sont.'),
]
abbreviations=[
    dict(form='loc.',expansion='localement'),
    dict(form='p.r.',expansion='par rapport'),
    dict(form='= in prose',expansion='même'),
]
hand=[
    dict(habit='A retraced T can have a forked body or an upper returning loop while retaining only one roof.',places='150_scan019 P01, P07, P12',consistency='The added body strokes do not establish an earlier letter or an extra bar; independently placed dots and the lowered i remain legible.',witness_errors='C offers a bar in P07/P12; H omits the live point from its lower main reading while mentioning it editorially.'),
    dict(habit='Diagonal marginal clauses can run through spaces beneath main text and resemble cancellations there.',places='150_scan019 P05, P08, P09, P16',consistency='The note’s p.r. à (X_i) supplies the dark group below main implique; the attachment is determined from the whole slanted clause.',witness_errors='H inserts a cancelled unreadable token after main implique and leaves much of the marginal wording unread.'),
    dict(habit='A curved insertion leader may resemble an emphasis stroke if its downward attachment is ignored.',places='150_scan019 P11/P17',consistency='The full leader runs from the parenthesized globalement to the gap before équisingulier, not below the two-line phrase.',witness_errors='H gives emphasis across équisingulier le long de Y where no source underline appears.'),
    dict(habit='Cônique is locally written with a separate arch over o.',places='150_scan019 P03/P12',consistency='Both occurrences on this leaf have the accent, independently of their i dots.',witness_errors='Both witnesses normalize these two occurrences to conique.'),
    dict(habit='Short written forms and compressed connected returns remain abbreviations or ordinary word endings.',places='150_scan019 P02, P04, P09/P16, P14',consistency='Loc. and p.r. retain their stops; the final sont has no extra i/e; equals consists of two bars.',witness_errors='H expands p.r. à to pour les, replaces par rapport à, changes sont to soient and omits the equals shorthand.'),
]

coverage={
    1:'Macro/editorial only: scanpage19 is a locator; H’s page-order note is not source text.',
    2:'P01a: au dessus is written with a blank, without H’s hyphen.',
    3:'P04a: live il est on the next main baseline; no qu’ insertion.',
    4:'P04b: p.r. à retained as written, not pour les.',
    5:'P04c: par rapport à retained, not pour les.',
    6:'P05b: à la fois is visibly present before ouverte.',
    7:'P05b/P06a: no comma after Y on the prior baseline; normal-baseline alors, resolves C’s first alternative and rejects H’s added et,.',
    8:'P07a/M0349: complete (14) inspected; T has no independent bar. Phi and the source ou underline also retained.',
    9:'P08a: qu’il est is present in the diagonal margin, distinguished from the main il est.',
    10:'P08a/M0350: full marginal definition recovered; compatible alone remains doubtful, avec tous resolved; second word is strictement, not strict.',
    11:'P09a: p.r. à (X_i), belongs to the second diagonal clause; no les before lambda T.',
    12:'P09a: l’est strictement pour is written in the second margin statement.',
    13:'Macro-only: H’s thin-space command before ]0,1[ is not a written comma. Source interval and stop are covered by P09a.',
    14:'H’s marginal-reading commentary is editorial; both actual notes are transcribed from P08/P09/P16.',
    15:'P10a: source circled item is cancelled; H’s literal parentheses are its circle representation, not added source punctuation.',
    16:'P10a: retain doubtful cancelled circled5; H’s description surchargé is editorial, not a separate source token.',
    17:'P12b/P12c/M0351: cancelled de remains doubtful; the separate live point resolves the main symbol as dotted T.',
    18:'P13a: crossed à is present; H’s live aux insertion is absent.',
    19:'P13b: literal auquel cas, not ce qui équivaut à ce que; hyphen-count macro difference is not separately collated.',
    20:'Macro-only: H’s thin-space command inside the interval is not source punctuation. Digits and brackets read in P14.',
    21:'P14a: sont =, with two written bars and no underline of strictement; not soient.',
    22:'P15a: thin18 retained. H’s final note is editorial; its observation about the point is addressed in P12c without copying the note into source text.',
}
rows=(ROOT/'packets'/PAGE/'differences.tsv').read_text().splitlines()[1:]
assert len(rows)==len(coverage)==22
diff_coverage=[dict(row=index,disposition=coverage[index]) for index in range(1,23)]

revision_review=[
    dict(text=r'\deleted{globalement}',scope_attachment='The whole word on the second main baseline is cancelled, between est and loc. triviale.',evidence='P02: a long stroke traverses the low letter bodies; tall stems and g descender remain outside it.'),
    dict(text=r'\deleted{tubulaire}\inserted{cônique}',scope_attachment='Tubulaire is crossed out; the raised cônique replaces it before the following T.',evidence='P03: the old word is under a long strike and the replacement is wholly above it, with its own circumflex.'),
    dict(text=r'\deleted{$X_i\cap Y$}',scope_attachment='Only the intervening formula after que is cancelled; l’on ait remains live to its right.',evidence='P06: the horizontal strike crosses the X, lowered i, intersection and Y; it does not reach the following l/on/ait bodies.'),
    dict(text=r'\unsure{compatible}',scope_attachment='Live preferred in the first marginal definition, with local body uncertainty; no independent cancellation stroke is established.',evidence='P08/P16: the initial body is retraced, while the following avec tous and the line’s attachment remain visible.'),
    dict(text=r'\deleted{\textcircled{\unsure{5}}}',scope_attachment='The whole circled item is cancelled; the upper overtraced loop is continuous with that crossing-out.',evidence='P10: broad zigzag crosses the digit and oval and extends upward; no separate extra numeral is recoverable.'),
    dict(text=r'\inserted{(globalement)}',scope_attachment='The whole parenthesized adverb is raised above the lower paragraph and attaches immediately before équisingulier.',evidence='P17 completes both parentheses and all ascenders; the curved leader descends to the left of the initial é and is not an underline of the following phrase.'),
    dict(text=r'\deleted{\unsure{de}}',scope_attachment='Short old word before the lower dotted T; its reading remains uncertain inside the cancellation.',evidence='P12: the horizontal strike runs through a looped initial and low return.'),
    dict(text=r'$\dot T$ de $Y$ dans $X$',scope_attachment='The upper point is live over a retraced T; no cancellation or removed-dot stage is asserted.',evidence='P12: the strong filled point is separate from the single roof, while body overwork lies below it.'),
    dict(text=r'p.r. \deleted{à} $(X_i)$',scope_attachment='Only the short à is crossed after p.r.; there is no aux replacement.',evidence='P13: one accented low body lies under the strike, with no separately raised word or x-ending before the parenthesis.'),
    dict(text='implique que si',scope_attachment='Main text is live; no separate cancelled token is supplied after implique.',evidence='P05/P16: the darker neighboring group belongs to the diagonal note’s p.r. à (X_i), and the main q descender crosses near it.'),
]
for item in revision_review:
    assert item['text'] in DC

report=dict(page=PAGE,reader='reader_c',line_count=16,changes=changes,decisions=decisions,
            inventory=inventory,audit_boxes=audits,doubts=doubts,notes=notes,check_events=check_events,
            notation=notation,abbreviations=abbreviations,hand=hand,diff_coverage=diff_coverage,
            deletion_insertion_review=revision_review)
mark_ids=[row.split('\t')[0] for row in (ROOT/'packets'/PAGE/'marks.tsv').read_text().splitlines()[1:]]
assert [row['id'] for row in decisions]==mark_ids
assert len({row['id'] for row in changes})==len(changes)
assert len(BOX)==17
for row in changes+decisions:
    assert (ROOT/'work'/row['crop']).is_file()
for row in audits:
    x0,y0,x1,y1=row['xyxy']
    assert 0<=x0<x1<=1682 and 0<=y0<y1<=2359
depth=0
for token in re.findall(r'(?<!\\)[{}]',DC):
    depth += 1 if token=='{' else -1
    assert depth>=0
assert depth==0
assert DC.count('$')%2==0
assert DC.count(r'\[')==DC.count(r'\]')==1
assert r'\illegible' not in DC
assert r'\bar T' not in DC
assert '+l\'est' not in D
assert r"l'est par rapport à $(X_i\cap T\subset T)_i$. Cela" in DC
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=PAGE,changes=len(changes),marks=len(decisions),crops=len(BOX),
                     audit_boxes=len(audits),inventory=len(inventory),doubts=len(doubts),
                     diff_rows=len(diff_coverage),check_events=len(check_events))))
