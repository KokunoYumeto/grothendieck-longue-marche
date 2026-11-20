#!/usr/bin/env python3
"""Main-reader decisions after three independent readings and crop inspection."""
from pathlib import Path
from datetime import datetime,timezone
from copy import deepcopy
import json
root=Path(__file__).resolve().parents[1]
R={r:json.loads((root/f'readers/scan026/{r}/review.json').read_text()) for r in 'ABC'}
ar=R['A']['loci'];br=R['B']['loci'];cr=R['C']['loci']
amap=[1,2,3,4,6,7,5,8,9,10,11,12,13,15,16,17,18,19,20,21,22,20,24,23,25,26,27,28,29,30,31,32,33,35,36,36,37,38,34]
cmap=[1,2,3,4,6,7,5,8,9,10,12,13,14,16,16,17,18,19,20,21,22,23,25,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
rows=[]
for i,b in enumerate(br):
    x=deepcopy(b)
    x['readers']={'A':ar[amap[i]-1]['reading'],'B':b['reading'],'C':cr[cmap[i]-1]['reading']}
    x['source_loci']={'A':ar[amap[i]-1]['id'],'B':b['id'],'C':cr[cmap[i]-1]['id']}
    x['crop']='readers/scan026/B/crops.tsv → '+b['crop'] if b.get('crop') else None
    x['decision']='The main reader inspected the cited crop and adopted the stated reading; genuine remaining doubt is preserved.'
    rows.append(x)

def at(n):return rows[n-1]
def crop(n,who,name):at(n)['crop']=f'readers/scan026/{who}/crops.tsv → {name}' if who!='main' else f'decisions/scan026_main_crops.tsv → {name}'
crop(1,'A','a01_heading_insertion.jpg')
crop(7,'main','m02_natural_glyph.png')
crop(9,'main','m03_signature_sentence.png')
crop(10,'main','m03_signature_sentence.png')
crop(11,'C','c06_ens.png')
crop(14,'main','m04_underlined_headings.png')
crop(15,'main','m04_underlined_headings.png')
crop(20,'main','m05_definit_bijection.png')
crop(21,'main','m05_definit_bijection.png')
crop(30,'main','m01_lower_diagram.png')
for n in [33,34,35,36,37,38,39]:crop(n,'C','c14_footer_note.png')

at(1)['kind']='misread word'
for n in [1,2,8,13,19,22,39]:at(n)['H_marked']=False
for n in [36,37]:at(n)['H_marked']=True
at(4).update(reading=r'\unsure{:|=}',diff_C=True,confidence='low',decision='A and C put colon first; B put equals first. The main crop shows two compact bent flecks, not two extended straight rules. Colon is placed first, and equals remains an alternative. No change is justified by the defining role of the expression.')
at(4)['evidence']='Two separate compact marks have horizontal extent and a small curved profile. Their compact bent shapes support colon as the first reading; equals remains an alternative.'
at(2)['decision']='B and C discarded the ent alternative; A retained it. The compact single low angular glyph does not expose a separate e-n-t run. Keep the interval with a doubtful blackboard-Z subscript reading, leaving the whole cancelled expression marked because its first strokes remain obscured.'
at(5)['decision']='C read the overwritten 0 confidently; A and B retained doubt. The loop is visible around the live upright but is partly merged with it. Keep the doubtful deleted 0 and live 1.'
at(12)['decision']='A and B resolved omega; C retained w. The paired rounded bowls and inward-curled outer ends support omega. Remove this doubt at the first occurrence and use the same reading at all its recurrences.'
at(13)['decision']='A and C resolved Isom(; B kept doubt on Isom while resolving the parenthesis. The main crop separates the opening parenthesis, but cancellation still covers the interior letters. Adopt B’s narrower uncertainty.'
at(19)['evidence']+=' H prints k without a local uncertainty macro; its accompanying note acknowledges an X-like form and chooses k from context. That note has been considered, without using the contextual choice to settle the ink.'
at(22)['evidence']+=' The H note acknowledges an X-like form but does not mark the printed k with an uncertainty macro.'
at(23)['decision']='All readers saw two separated marks and no comma before i_n. A retained a conventional three-dot ellipsis; B and C represented the observed two marks. Preserve two centered marks and the single comma actually drawn after i_1.'
at(25)['decision']='A retained an ellipsis/dash doubt; B and C represented two marks. The crop shows a clear gap between two short strokes and no adjacent commas. Represent the two observed marks without adding a third or joining them into a dash.'
at(26)['decision']='A and B resolved the final nested n; C retained doubt. The small arch and its falling right leg can be separated from the taller crossing stroke of the line beneath. Adopt n, medium confidence.'
at(29).update(reading=r'\mathrm O(\unsure{n|N},k)',diff_C=False,diff_H=True,unresolved=True,confidence='low',evidence='The argument is heavily retraced, with a tall first stroke and a raised return into a descending second leg. The neighboring k has a distinct higher loop. The overtracing leaves n and N possible; the existing n-first reading remains provisional.',decision='A retained n|N; B resolved n; C put N first. The crop does not securely settle the letter case. Retain the two candidates, with n first, without replacing the reading from the expected rank.')
at(30)['kind']='drawing or diagram'
at(30)['evidence']='The main crop shows sgn above the lowest central portion of the curved arrow, below O(n/N,k). The straight inclusion and determinant arrows, hook and endpoints are preserved. Remove near start and place the curved-arrow label centrally on its inner side.'
at(36).update(reading=r'\unsure{vect.|variété}',confidence='low',decision='A and C kept variété; B put vect. first. The main crop has a short low run followed by a tall t-like stroke and a separate point. Put vect. first and retain variété because the line edge and the upper writing still obscure the sequence.')
at(37).update(reading=r'\unsure{réel|via|vie}',confidence='low',evidence='The short group has an initial r/v-like pair, a separate high mark and a final tall return touching the cut edge. The main reader gives réel first; the vi- readings via and vie remain possible. A separate internal d for vide is not recoverable.',decision='A chose doubtful via; B offered réel|via|vide; C offered via|vie. The main reader retains réel|via|vie on the surviving strokes. The discarded vide is not supported by a separately visible d.')
at(38).update(reading=r'\unsure{se pense|ses pts}',diff_H=True,confidence='low',evidence='A short crossed group is followed by a gap and a p-like descent with a loop and low n/s/e-like strokes. The main reader puts se pense first and retains the compressed ses pts alternative. The bottom boundary clips the lower strokes. No separate later i-dot and tall t establish the expanded points, and the group division does not support supra.',decision='A offered ses pts|se pense; B se pense; C se pense|ses pts|ses points. Preserve the two surviving compressed readings, with se pense first. No full phrase is reconstructed from expected mathematical meaning.')
at(39)['decision']='All three readers found the tail attached to the closing parenthesis of E(I,R). Use the source-attached small TikZ arrow and retain the supplied margin macro for the two-line foot annotation. The source comment identifies its attachment explicitly.'

terminal=deepcopy(ar[13]);terminal.update(readers={'A':ar[13]['reading'],'B':r'P/\mathfrak A_n . (in page.tex)','C':cr[14]['reading']},crop='readers/scan026/A/crops.tsv → a06_orientation_quotient_stop.jpg',decision='The main reader sees a detached point to the lower right of the quotient. Retain it.',H_marked=False)
kernel=deepcopy(cr[10]);kernel.update(readers={'A':r'\text{noyau }\mathfrak A_n in the same diagram row (page.tex)','B':r'\text{noyau }\mathfrak A_n in the same diagram row (page.tex)','C':cr[10]['reading']},crop='decisions/scan026_main_crops.tsv → m06_signature_row.png',decision='The main crop confirms noyau and A_n to the right of the target at the same row, with open space and no connecting arrow. Keep this placement.',H_marked=False)
rows.insert(13,terminal)
rows.insert(10,kernel)
for i,x in enumerate(rows,1):x['id']=f'026-{i:02}'
assert all(x.get('crop') for x in rows)

inventory=[]
for item in R['C']['inventory']:
    x=deepcopy(item);x['sheet_kind']='text';x['transcribed']='yes'
    x['hand']='another unnamed hand (archive numeral)' if 'Archive sheet' in x['element'] else 'his hand'
    k=x['kind']
    if k=='paragraph and display':
        a=deepcopy(x);a.update(kind='text',element='Introduction of the canonical bijection',first_words_or_objects='Ceci posé, on définit une bijection canonique');inventory.append(a)
        x.update(kind='display',element='Orientation correspondence for the quadratic module',first_words_or_objects=r'\omega_{E(I,x)}\simeq\omega_I')
    elif k=='two-line annotation and arrow':
        a=deepcopy(x);a.update(kind='drawing',element='Curved explanatory arrow attached to E(I,R)',first_words_or_objects='closing parenthesis → considéré');inventory.append(a)
        x.update(kind='margin note',element='Two-line foot annotation at the clipped edge',first_words_or_objects='considéré / comme vect.|variété réel|via|vie se pense|ses pts')
    elif k=='overwriting':x['kind']='deletion'
    elif k not in ['text','display','diagram','drawing','margin note','insertion','deletion']:x['kind']='text'
    if x['element']=='Inclusion–determinant diagram':x['first_words_or_objects']=r'\mathfrak S_n ↪ O(n|N,k) → {±1}; incl., det, curved sgn'
    inventory.append(x)

doubts=[]
for x in rows:
    if x.get('unresolved') and x['id'] not in ['026-24']:
        # The repeated x is governed by its first occurrence on the page.
        doubts.append({'location':x['location'],'reading':x['reading'],'alternatives':{'026-02':r'[1,n]_{\mathbb Z}, uncertain under cancellation','026-04':':; =','026-05':'underlying 0 uncertain','026-08':r'\mathfrak S; S','026-14':'Isom letters uncertain; opening parenthesis visible','026-19':'donne uncertain','026-20':'donne uncertain','026-21':'x; k; X (also governs the later display)','026-29':'ord. uncertain','026-31':'n; N','026-38':'vect.; variété','026-39':'réel; via; vie','026-40':'se pense; ses pts'}.get(x['id'],''),'confidence':x['confidence'],'reason':x['evidence']})

notes=r'''**N026.1 — Page content.** Section c), “Orientation d'un ensemble fini I”, with the inserted “(cardinal n).”, describes the numbering torsor \(P=\operatorname{Isom}(I_n,I)\), the signature map and the orientation expression \(\omega_I=P\times_{\mathfrak S_n}\{\pm1\}\simeq P/\mathfrak A_n\). It then states compatibility with the scalar product on \(k^I\), and traces the maps \(\mathfrak S_n\hookrightarrow\mathrm O(n/N,k)\xrightarrow{\det}\{\pm1\}\) together with the curved signature arrow. The right note relates a numbering of I to an ordered orthonormal basis; the final correspondence uses \(\mathbb R\). These are reported as the page's claims, not as independently proved constructions.

**N026.2 — Reading decisions prompted by mathematics.** The earlier field letter k and the later argument of E differ in visible shape: both later occurrences have crossed oblique strokes, while the k of the orthogonal-group expression has a separate high loop. The consolidated reading remains x first, with k and X retained as alternatives; no field letter was supplied from the intended construction. The rank-like argument of O remains n/N because its overwritten ink does not settle the case. The two continuation marks in the marginal lists and their punctuation were checked as marks actually drawn. They were not replaced by conventional three-dot notation. The curved-arrow label belongs at the middle and above the lower arc. These are visual decisions, not proof checks of the asserted compatibilities.

**N026.3 — Explicit small-set check of the written quotient correspondence.** At the concrete set \(I=I_1=\{1\}\), the written definitions give \(P=\mathfrak S_1=\mathfrak A_1=\{\mathrm{id}\}\). Thus \(P/\mathfrak A_1\) has one element, while \(P\times_{\mathfrak S_1}\{+1,-1\}\) has the two elements \([(\mathrm{id},+1)]\) and \([(\mathrm{id},-1)]\). The canonical map \([\mathrm{id}]\mapsto[(\mathrm{id},+1)]\) has one-point image and misses the second element. This proves the failure of the displayed bijection in that explicit case. Exhaustive enumeration of the two orbit sets at n=0,1,2,3,4 gives cardinalities (1,2), (1,2), (2,2), (2,2), (2,2), respectively; the code and dated output are preserved in scripts/check_orientation_counts.py and decisions/orientation_count_check.json. No n≥2 restriction is written in this page's heading. The displayed correspondence stays unchanged in the transcription; no general replacement theorem is supplied.

**N026.4 — Qualifications and documentary details.** The heading and the compatibility subheading are retained with their actual underlined spans. There is no visible date or authorial page count; the light lower-left 25 is an archive number. No fully legible “à vérifier” or “sauf erreur” occurs. The foot annotation's last words are unresolved; they are not treated as a secure authorial qualification. Its first line reads “considéré”; the second is “comme” followed by the marked alternatives recorded in the doubts table.'''

now=datetime.now(timezone.utc).isoformat(timespec='seconds');who='GPT-6 Astra Pro; effort not exposed; run root/scan026 adjudication'
check=json.loads((root/'decisions/orientation_count_check.json').read_text())
events=[
 {'statement_id':'N026.1 / scan026 torsor, signature and compatibility claims','date':now,'who':who,'type':'carried as background without fault found','outcome':'Page content described; no proof of the torsor construction or compatibility is claimed from transcription. The quotient correspondence has its separately recorded small-set counterexample.'},
 {'statement_id':'N026.2 / scan026 E(I,x), O(n/N,k), marginal lists and arrow labels','date':now,'who':who,'type':'carried as background without fault found','outcome':'Mathematical syntax used to locate the ink for inspection. No mathematical inference was used to replace the observed symbols; visual checks are documented in the locus records.'},
 {'statement_id':'N026.3 / scan026 orientation quotient display','date':check['utc'],'who':who,'type':'computation or formal certificate','outcome':'Executed scripts/check_orientation_counts.py: exhaustive orbit enumeration at n=0,1,2,3,4 gives (|P/A_n|, |P×_{S_n}{±1}|)=(1,2),(1,2),(2,2),(2,2),(2,2). This is a finite computation, not a formal proof certificate.'},
 {'statement_id':'scan026 orientation quotient display, unqualified correspondence','date':now,'who':who,'type':'refuted, refined statement N026.3','outcome':'The explicit n=1 example has a one-element source and a two-element target. The canonical map [id]↦[(id,+1)] misses [(id,-1)]. N026.3 records the exact counterexample, without proposing a general conditional replacement. Transcription unchanged.'},
 {'statement_id':'N026.4 / scan026 headings and documentary marks','date':now,'who':who,'type':'carried as background without fault found','outcome':'Documentary statements read from the page and reader inventories; no date, external attribution or historical fact was independently researched.'}
]
exp={'hom':'homomorphisme','ens':'ensemble','Isom':'isomorphismes','numérot':'numérotations','Aut':'automorphismes','sgn':'signature','ord.':'ordonnée','orthon.':'orthonormale','incl.':'inclusion','det':'déterminant','comp.':'comparer / compatibilité','vect.':'vectoriel (uncertain reading in the clipped footnote)','pts':'points (uncertain alternative in the clipped footnote)'}
rec={'scan':26,'loci':rows,'inventory':inventory,'doubts':doubts,'notes':notes,'check_events':events,'abbreviations':[{'abbr':a,'expansion':e,'scans':[26]} for a,e in exp.items()],'consequential':['The x/k/X argument is retained from its crossed strokes in both occurrences; H’s context-led k is not imposed. The mathematical comparison remains explicitly doubtful.','The cancelled Isom( and the overwritten E and 0 are retained in their deletion states, and the sgn label and the footnote arrow are attached at their visible positions.','The quotient correspondence is preserved as written; N026.3 records the explicit n=1 counterexample with its canonical map.'],'reader_runs':['scan026_a','scan026_b','scan026_c'],'main_inspection_file':'decisions/scan026_inspection.md','excluded_syntax_only_differences':['H page{25} versus the archive comment is the supplied page-number mapping, not a textual disagreement.','Operatorname/text/roman wrapper and ordinary spacing differences with the same reading are excluded.'],'crop_counts':{'A':13,'B':14,'C':14,'main_new':6,'main_reused':17}}
(root/'decisions/scan026.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
print('Wrote scan026 decisions:',len(rows),'loci;',len(inventory),'inventory elements;',len(doubts),'remaining doubt rows.')
