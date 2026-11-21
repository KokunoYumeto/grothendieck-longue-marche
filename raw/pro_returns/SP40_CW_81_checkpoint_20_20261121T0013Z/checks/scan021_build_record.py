#!/usr/bin/env python3
"""Copy scan021 root-journal selections into a pending source-complete record."""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
import re
import sys
sys.dont_write_bytecode=True
from scan021_prepare_sources import span, literal_span

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
U=json.loads((OUT/'scan021_source_union.json').read_text())
JP='out/checks/scan021_main_decisions.md'
J=(BASE/JP).read_text()
TEXT={r:(BASE/f'out/readers/021/{r}/reading.tex').read_text() for r in 'ABC'}
GROUPS={(g['reader'],g['group_id']):g['tex_source'] for g in U['candidate_graphical_groups']}
RAW={r:{x['value']['id']:x for x in U['reader_sources'][r]['raw_rows']['differences']} for r in 'ABC'}


def write(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


def section(number):
    m=re.search(r'^## '+f'{number:02d}'+r'\b[^\n]*',J,re.M)
    assert m,number
    nxt=re.search(r'^## ',J[m.end():],re.M)
    end=m.end()+nxt.start() if nxt else len(J)
    return span(JP,J,m.start(),end,section=number,source_sha256_utf8=sha(BASE/JP))


def scope(r,selector):
    if selector.startswith('g:'):
        return copy.deepcopy(GROUPS[(r,selector[2:])])
    if selector.startswith('s:'):
        return copy.deepcopy(U['reader_sources'][r]['reported_silent_choices_with_complete_TeX'][int(selector[2:])]['tex_source'])
    if selector=='whole':
        return copy.deepcopy(U['reader_sources'][r]['complete_tex'])
    if selector=='corollary':
        text=TEXT[r];start=text.index('\\uline{Corollaire') if '\\uline{Corollaire' in text else text.index('% BEGIN B021-G10')
        return span(f'out/readers/021/{r}/reading.tex',text,start,len(text))
    if selector.startswith('d:'):
        match=list(re.finditer(r'\\\[.*?\\\]',TEXT[r],re.S))[int(selector[2:])-1]
        return span(f'out/readers/021/{r}/reading.tex',TEXT[r],match.start(),match.end())
    if selector.startswith('l:'):
        return literal_span(f'out/readers/021/{r}/reading.tex',TEXT[r],selector[2:])
    return copy.deepcopy(U['reader_sources'][r]['actual_tex_reading_sources'][selector])


def witness_scopes():
    out={}
    for r in 'CH':
        p=f'packets/021/{r}.tex';t=(BASE/p).read_text();ds=list(re.finditer(r'\\\[.*?\\\]',t,re.S))
        cor=t.index('\\uline{Corollaire' if r=='C' else '\\emph{Corollaire')
        other=t.index("d'autre part")
        bounds={'opening':(t.index('Soit '),ds[0].start()),'first':(ds[0].start(),ds[0].end()),
            'parenthesis':(ds[0].end(),ds[1].start()),'upper':(ds[1].start(),ds[1].end()),
            'or':(t.index('Or '),ds[2].start()),'central':(ds[2].start(),ds[2].end()),
            'cela':(ds[2].end(),ds[3].start()),'middle':(ds[3].start(),ds[3].end()),
            'margin':(ds[3].end(),other),'firstverb':(other,ds[4].start()),
            'exclusion':(ds[4].start(),ds[4].end()),'conclusion':(ds[4].end(),cor),
            'corheading':(cor,ds[5].start()),'corformula':(ds[5].start(),ds[5].end()),
            'corprose':(ds[5].end(),ds[6].start()),'bottom':(ds[6].start(),ds[6].end()),
            'whole':(0,len(t))}
        out[r]={key:span(p,t,*value) for key,value in bounds.items()}
        out[r]['rule']=span(p,t,cor,len(t))
    return out


WS=witness_scopes()
SPECS=[]


def add(n,sec,location,C,H,confidence,final,ids,scopes,public=None,*,kind='other',doubt=False,alternatives='',original=None,
        status=None,area='whole',wC='',wH='',marked=False,groups=(),evidence='',Cparent=None,Hparent=None,physical=None,
        source_only=False,extra=None):
    SPECS.append(dict(id=f'L021-{n:02d}',section=sec,location=location,C=C,H=H,confidence=confidence,final=final,
        reader_ids={r:([ids[i]] if isinstance(ids[i],str) else ids[i]) for i,r in enumerate('ABC')},
        reader_scope_selectors=dict(zip('ABC',scopes)),public_readers=public or {},kind=kind,remaining_doubt=doubt,
        alternatives=alternatives,original_C_row=original,C_doubt_status=status,witness_scope=area,witness_C=wC,witness_H=wH,
        marked_in_H=marked,selected_source_groups=list(groups),evidence=evidence,C_count_parent=Cparent,H_count_parent=Hparent,
        physical_count_parent=physical,root_source_audit_choice_applied=source_only,extra=extra or {}))


def canonical(n,sec,row,C,H,confidence,final,*,doubt,status,alternatives='',area,groups=(),evidence='',wC,wH,marked=False,
              Hparent=None,Cparent=None,physical=None,public=None):
    ids=[f'A021-R{row:02d}',f'B021-D{row:02d}',f'C021-R{row:02d}']
    add(n,sec, U['C_doubt_crosswalk'][row-1]['source_parts'][0]['location_label'],C,H,confidence,final,ids,ids,public,
        kind='misread word' if row in [1,3,5,9,10,11] else 'other',doubt=doubt,alternatives=alternatives,
        original=f'C021-R{row:02d}',status=status,area=area,wC=wC,wH=wH,marked=marked,groups=groups,evidence=evidence,
        Cparent=Cparent,Hparent=Hparent,physical=physical)


canonical(1,1,1,0,1,'medium',r"\unsure{l'on a|on a}",doubt=True,status='retained',alternatives='on a',area='opening',
    wC=r"\unsure{l'on a|on a}",wH=r'\uncertain{on a}',marked=True,
    evidence='The broad opening loop and compressed low continuation leave the l/apostrophe attachment unresolved; l’on a remains the qualified primary.')
add(2,1,'opening endpoint',0,1,'high','no terminal colon',['A021-X01','B021-D16','C021-D01'],['A021-X01','B021-D16','C021-D01'],
    kind='text not on the page',area='opening',wC='no colon',wH=':',evidence='The final short a-shaped run has no separate two-point colon after it.')
canonical(3,2,2,1,1,'medium','i.e',doubt=False,status='resolved',area='first',wC=r'\unsure{i.e|i.e.}',wH=r'\text{i.e.}',groups=['C021-G01'],
    evidence='The e ends in a continuous low tail with no detached final point; the nearby tall stroke belongs to the preceding q-descender.')
add(8,3,'first roofed Sigma: absence of raised plus',0,0,'high',r'\widehat{\Sigma}_{\alpha_0} with no raised +',[[],[],[]],['g:A021G01','g:B021-G01','g:C021-G01a'],
    {'A':r'\widehat\Sigma_{\alpha_0}; no +','B':'First complete roofed Sigma in B021-G01 has no raised plus.','C':r'\widehat{\Sigma}_{\alpha_0}; no written +'},
    area='first',wC=r'\widehat{\Sigma}_{\alpha_0}',wH=r'\widehat{\Sigma}_{\alpha_0}',groups=['C021-G01a'],
    evidence='The first roofed Sigma has the lowered alpha and further-lowered zero; no raised plus is present.')
canonical(9,5,3,1,0,'high','(ce',doubt=False,status='resolved',area='parenthesis',wC=r'\unsure{(ce|Ce}',wH='(ce',
    evidence='A tall independent left hook precedes the two small letters; the selected passage has the opening parenthesis and no supplied closing parenthesis.')
add(10,5,'achèvera accent',1,0,'low',r'ach\unsure{è|é|e}vera',['A021-X02','B021-D17','C021-D08'],['A021-X02','B021-D17','C021-D08'],
    doubt=True,alternatives='acute é; unaccented e',area='parenthesis',wC='achèvera',wH='achèvera',
    evidence='The small high mark over the compressed vowel leaves its direction and attachment unresolved; grave, acute and absent-accent states remain.')
add(11,5,'demonstration first accent',1,1,'low',r'd\unsure{è|é|e}monstration',['A021-X03',[],'C021-D09'],['A021-X03','l:démonstration','C021-D09'],
    {'A':r'd\unsure{è|é}monstration','B':'démonstration','C':r'\unsure{demonstration|démonstration}'},kind='misread word',
    doubt=True,alternatives='acute é; unaccented e',area='parenthesis',wC='démonstration',wH='démonstration',
    evidence='The short high near-vertical stroke after the d-loop leaves accent direction and attachment unresolved; the grave primary retains the acute and absent-accent alternatives.')
add(12,6,'upper condition main brace',1,1,'medium','complete two-run brace with pointed middle return',
    ['A021-X05','B021-D19','C021-D06'],['g:A021G18','g:B021-G02','g:C021-G02'],kind='drawing or diagram',
    area='upper',wC=r'\left\{ ... \right.',wH=r'\bigl|',groups=['C021-G02'],
    evidence='The nearly straight upper run turns through the pointed left return into the surviving lower upright; the complete two-run source preserves that bend.')
add(13,6,'second K in K = K₁ ∪ {i}',1,0,'low',r'K with head/retrace | \deleted{I}K',
    [[],[],'C021-D07'],['g:A021G18','g:B021-G02','g:C021-G02a'],
    {'A':r'K=K_1\cup\{i\}, ordinary K in the condition node','B':r'K=K_1\cup\{i\}, ordinary K in the condition node','C':r'K with head retrace | \deleted{I}K; complete literal C021-G02a'},
    kind='drawing or diagram',doubt=True,alternatives='deleted I predecessor plus live K',area='upper',wC=r'K_1',wH=r'K_1',groups=['C021-G02a'],
    evidence='The transverse upper run crosses the tall K stem above its two right arms; the live K remains and the retrace/predecessor state stays qualified.')
add(14,6,'cancelled Sigma: complete glyph and crossing geometry',1,1,'low','qualified cancelled Sigma-alpha and literal zigzag crossings',
    [['A021-R04','A021-X06'],'B021-D04',['C021-R04','C021-D05']],['g:A021G19','g:B021-G02-cancelled-Sigma','g:C021-G02'],
    kind='drawing or diagram',area='upper',wC=r'\deleted{\unsure{\Sigma_\alpha}}',wH=r'\struck{\ill{}}',marked=True,
    groups=['C021-G02','B021-G02-cancelled-Sigma'],evidence='The complete cancelled group retains the angular body, low curl and observed zigzag crossing runs once; the crossings still obscure exact glyph identity.')
canonical(15,6,4,0,0,'low',r'\deleted{\unsure{\Sigma_\alpha}}',doubt=True,status='retained',area='upper',
    alternatives='underlying cancelled reading remains qualified; original alternative blank retained',wC=r'\deleted{\unsure{\Sigma_\alpha}}',wH=r'\struck{\ill{}}',marked=True,
    groups=['B021-G02-cancelled-Sigma'],Cparent='L021-14',Hparent='L021-14',physical='L021-14',
    evidence='The angular body and low curl survive under the crossings, while their exact identity remains qualified within the single complete cancelled cluster.')
add(17,8,'two interrupted pale upper traces',1,1,'low','qualified C021-M01: two interrupted pale runs',
    ['A021-X04',[],'C021-M01'],['g:A021M01','g:B021-G02','g:C021-M01'],
    {'A':'A021M01: two interrupted pale runs, role/hand/surface origin unresolved.','B':'No corresponding two-run component in the inspected complete upper-display source B021-G02.','C':'C021-M01: two interrupted pale runs, role/hand/surface origin undetermined.'},
    kind='omission',doubt=True,alternatives='role, hand, writing status and surface origin undetermined',area='upper',wC='absent',wH='absent',groups=['C021-M01'],
    evidence='Two roughly parallel interrupted pale runs with separated darker spots are retained together; no letter, equality or deletion role is assigned.')
canonical(18,9,5,0,1,'low',r'Or [qualified complete comme | \deleted{co}mme | \deleted{co}comme | \deleted{car}comme group] on a',
    doubt=True,status='retained',alternatives=r'\deleted{co}mme; \deleted{co}comme; \deleted{car}comme',area='or',
    wC=r'Or \unsure{comme} on a',wH=r'Or \struck{\ill{}} \ill{} :',marked=True,groups=['B021-G03'],
    evidence='The dark initial cluster and the two succeeding low runs leave the cancellation/live boundary unresolved; the complete three-part group and following on a occur once.')
add(19,9,'Or passage: readable on a',0,0,'high','on a',['A021-X07','B021-D20','C021-D02'],['A021-X07','B021-D20','C021-D02'],
    {'A':'on a','B':'on a','C':'on a'},kind=r'readable ink left as \ill{}',area='or',wC='on a',wH=r'\ill{}',marked=True,Hparent='L021-18',physical='L021-18',
    evidence='The separately written on and compact final a are retained within the one complete replacement of H’s Or passage.')
add(20,9,'Or passage: endpoint colon',0,0,'high','no colon',['A021-X08','B021-D20','C021-D02'],['A021-X08','B021-D20','C021-D02'],
    {'A':'no colon','B':'no colon','C':'no colon'},kind='text not on the page',area='or',wC='no colon',wH=':',marked=True,Hparent='L021-18',physical='L021-18',
    evidence='No separate colon follows the final short a run; the endpoint belongs to the one complete H-passage replacement.')
add(21,10,'detached left-margin slash',1,1,'low','qualified C021-M02 oblique trace',['A021-X09',[],'C021-M02'],['g:A021M02','s:5','g:C021-M02'],
    {'A':'A021M02: qualified detached oblique trace.','B':'No corresponding left-margin mark in the inspected complete central-inclusion source.','C':'C021-M02: qualified detached oblique trace.'},
    kind='omission',doubt=True,alternatives='role, hand and surface origin undetermined',area='central',wC='absent',wH='absent',groups=['C021-M02'],
    evidence='The short oblique slash is detached from the display’s letters and relation; its shape and position remain without an assigned role or hand.')
canonical(22,11,14,1,1,'high','round union with definite high left transverse run',doubt=False,status='resolved',area='central',
    wC=r'\unsure{\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup|\bigcup}',wH=r'\bigcup',groups=['C021-G03'],
    evidence='The high run crosses the left stalk, extends left of it and ends inside the round cup; the complete source retains both paths without assigning an operation.')
add(24,11,'point and pale continuation below-left of central roof',1,1,'low','qualified point with pale lower continuation',
    ['A021-X10','B021-D24','C021-M03'],['g:A021G07','g:B021-G04-point','g:C021-M03'],
    {'A':'A021G07 contains the detached point and additional pale lower path.','B':'B021-G04-point contains the qualified point alone.','C':'C021-M03 contains the qualified point alone.'},
    kind='omission',doubt=True,alternatives='attachment to roof, role, hand and surface origin undetermined',area='central',wC='absent',wH='absent',groups=['C021-M03','A021G07'],
    evidence='The small detached dark point and paler downward continuation are retained as one qualified cluster, with each physical trace represented once.')
canonical(25,12,15,0,0,'medium',r'\Sigma_{\unsure{\alpha_0|\alpha}}^-',doubt=True,status='retained',alternatives=r'\alpha',area='middle',
    wC=r'\Sigma_{\unsure{\alpha_0|\alpha}}^-',wH=r'\Sigma_{\alpha_0}^-',groups=['B021-G05-index'],
    evidence='The alpha returns into a dark low terminal curl whose separation as a zero remains unresolved; the complete literal index preserves that shared curve once.')
canonical(28,13,6,1,1,'low','j:e. | j.e. | i:e. | i.e., complete literal lead-in',doubt=True,status='retained',
    alternatives='j.e.; i:e.; i.e.',area='margin',wC=r'\unsure{j.e.|i.e.}',wH='i.e.',groups=['A021G20'],
    evidence='The high dot, descending first stem, two distinct middle points, e-shaped run and final point are retained once; punctuation and first-letter attachment remain qualified.')
add(29,13,'lead-in: two middle points',0,0,'medium','two middle points in the complete qualified lead-in',
    ['A021-R06','B021-D22','C021-D03'],['g:A021G20','g:B021-G06-lead-in','g:C021-G05a'],
    kind='drawing or diagram',area='margin',wC='one middle period in the j.e./i.e. source',wH='one middle period in i.e.',groups=['A021G20'],
    Cparent='L021-28',Hparent='L021-28',physical='L021-28',evidence='Two vertically separated middle points remain within the one complete lead-in cluster and add no duplicate count.')
add(30,14,'complete marginal diagram: brace and placement parent',1,1,'medium','complete A021DG with selected third-label source and resolved central sign',
    ['A021-X12','B021-D18','C021-D04'],['g:A021DG','g:B021-G06','g:C021-G05'],kind='drawing or diagram',area='margin',
    wC='five upright rows, two braces, and sideways labels in the complete C margin diagram',
    wH=r'\note{à droite, un schéma vertical : de haut en bas $\Sigma_i^+$ ou $\Sigma_i^-$, $E_i$, $\Sigma_\alpha$, $E_\alpha$, $\Sigma_{\alpha_0}^+$, réunis par une accolade}',marked=True,
    groups=['A021DG'],evidence='The completed diagram preserves five upright rows, four upright Sigma groups, two sideways Sigma labels, both looped braces and their visible endpoints; the separate lead-in stays outside this parent.')
canonical(31,14,8,0,0,'medium',r'\Sigma_{i\alpha} | \Sigma_{i,\alpha} | \Sigma_{\dot\alpha}',doubt=True,status='retained',
    alternatives=r'\Sigma_{i,\alpha}; \Sigma_{\dot\alpha}',area='margin',wC=r'\unsure{\Sigma_{i\alpha}|\Sigma_{i,\alpha}}',wH=r'\Sigma_\alpha in the complete diagram note',marked=True,
    groups=['B021-G06-middle-row'],Hparent='L021-30',evidence='The shared lower-arm hook and its detached point occur once; i-alpha, i-comma-alpha and dotted-alpha attachments remain qualified.')
canonical(32,14,7,1,0,'medium','literal upright shaft-and-point ! shape',doubt=False,status='resolved',area='margin',
    wC=r'\unsure{\rotatebox{-90}{$!$}|\text{ou}|-}',wH='absent from the complete diagram note',marked=True,groups=['A021D05'],Hparent='L021-30',
    evidence='The detached point and one bent short run give the upright shaft-and-point shape; the complete literal source has no remaining ou/dash qualifier and assigns no mathematical function.')
add(37,14,'detached pale run below outer marginal brace',1,0,'low','qualified A021M04 pale run',
    ['A021-X16','B021-D23','C021-M04'],['g:A021M04','g:B021-G06-lower-trace','g:C021-M04'],kind='omission',doubt=True,
    alternatives='brace connection, role, hand and surface origin undetermined',area='margin',wC='absent',wH='absent from the complete diagram note',marked=True,
    groups=['A021M04'],Hparent='L021-30',evidence='The pale run beyond the outer brace remains detached and qualified; its connection, role, hand and origin stay open.')
add(38,14,'outer marginal brace component',0,0,'medium','complete literal outer looped brace',['A021-X13','B021-D18','C021-D04'],['g:A021DG','g:B021-G06','g:C021-G05'],
    kind='drawing or diagram',area='margin',wC='outer brace path',wH='one accolade described, without this separate outer-brace path',marked=True,groups=['A021DG'],
    Cparent='L021-30',Hparent='L021-30',physical='L021-30',evidence='The long outer brace and its closed middle turn remain within the single complete diagram parent.')
add(39,14,'inner marginal brace component',0,0,'medium','complete literal inner looped brace',['A021-X14','B021-D18','C021-D04'],['g:A021DG','g:B021-G06','g:C021-G05'],
    kind='drawing or diagram',area='margin',wC='inner brace path',wH='no separate inner-brace path in the complete note',marked=True,groups=['A021DG'],
    Cparent='L021-30',Hparent='L021-30',physical='L021-30',evidence='The shorter inner brace and its closed turn remain within the single complete diagram parent.')
add(40,14,'two sideways signed Sigma labels',0,0,'medium','two complete literal sideways Sigma labels with shared index hooks/dots',
    ['A021-X15','B021-D18','C021-D04'],['g:A021DG','g:B021-G06','g:C021-G05'],
    {'A':'A021DG draws both complete transverse signed Sigma/index groups literally.','B':r'\node[rotate=90] labels \Sigma_i^+ and \Sigma_i^- use font glyphs.','C':r'\node[rotate=90] labels \Sigma_i^- and \Sigma_i^+ use font glyphs.'},
    kind='drawing or diagram',area='margin',wC=r'rotated \Sigma_i^- and \Sigma_i^+ labels',wH='sideways labels absent from the complete diagram note',marked=True,
    groups=['A021DG'],Cparent='L021-30',Hparent='L021-30',physical='L021-30',evidence='Both sideways labels retain their complete shared terminal hooks, points and raised signs inside the diagram parent.')
canonical(41,15,9,1,0,'medium',r'\unsure{signifie|signifi}',doubt=True,status='retained',alternatives='signifi',area='firstverb',
    wC=r'\unsure{signifi|signifie}',wH='signifie',evidence='The high point and further detached short oblique support signifie as primary, while the final vowel’s separation remains incomplete.')
add(44,16,'crossed-inclusion relation',0,0,'high','literal two-stroke not-subset relation',['A021-X17','B021-D31',[]],['g:A021G11','g:B021-G07','g:C021-G06'],
    {'A':'A021G11: complete curved inclusion and long crossing stroke.','B':'B021-G07: complete literal inclusion curve and crossing stroke.','C':r'\node at (778,1388) {$\not\subset$};'},
    kind='drawing or diagram',area='exclusion',wC=r'\not\subset',wH=r'\not\subset',groups=['A021G11'],
    evidence='The curved inclusion is crossed by one long near-vertical slant; the two-stroke drawing retains the shared not-subset reading.')
add(45,17,'cancelled verb: complete letter-body and crossing cluster',1,1,'low','qualified cancelled impli/impl. with both actual transverse runs',
    [['A021-R10','A021-X18'],'B021-D10',['C021-R10','C021-D11']],['g:A021G21','g:B021-G08','g:C021-G07'],kind='drawing or diagram',
    area='conclusion',wC=r'\deleted{\unsure{impli|impl.}}',wH=r'\struck{implique}',marked=True,groups=['B021-G08'],
    evidence='The complete cancelled cluster preserves the initial point, tall loop, short high stroke and both transverse runs once; the incomplete ending remains unexpanded.')
canonical(46,17,10,0,0,'low',r'\deleted{\unsure{impli|impl.}}',doubt=True,status='retained',alternatives='cancelled impl.',area='conclusion',
    wC=r'\deleted{\unsure{impli|impl.}}',wH=r'\struck{implique}',marked=True,groups=['B021-G08'],Cparent='L021-45',Hparent='L021-45',physical='L021-45',
    evidence='The ending beneath the crossing runs remains incomplete; impli and impl. stay qualified within the one complete cancelled cluster.')
canonical(47,17,11,1,0,'high','signifie',doubt=False,status='resolved',area='conclusion',wC=r'\unsure{signifie}',wH='signifie',
    evidence='The live replacement has its visible dot, short i stroke and separate final narrow e stroke.')
add(50,18,'concluding intersection, comma and cqfd.',0,0,'high',r'\Sigma_i^+\cap\Sigma_\alpha^+=\varnothing, cqfd.',
    [[],[],[]],['s:8','g:B021-G09','g:C021-G08'],
    {'A':r'Complete concluding formula with separate font i and alpha; comma and cqfd.','B':r'B021-G09 with separate font i and alpha; following comma and cqfd.','C':r'C021-G08 integrates the i stem and alpha curl into the respective lower arms; comma and cqfd. follow.'},
    area='conclusion',wC=r'\Sigma_i^+\cap\Sigma_\alpha^+=\varnothing, cqfd.',wH=r'\Sigma_i^+\cap\Sigma_\alpha^+=\emptyset, cqfd.',groups=['C021-G08'],
    evidence='Both pluses, intersection, equality, empty-set sign, following comma and final cqfd. point remain; the integrated index strokes occur once.')
canonical(51,19,12,0,1,'medium',r'\Pi_I^{\unsure{\circ|0}}',doubt=True,status='retained',alternatives='0',area='corheading',
    wC=r'\Pi_I^{\unsure{\circ|0}}',wH=r'\Pi_I^0',groups=['A021G22'],evidence='The small raised closed loop retains circle and zero readings, with circle as the qualified primary.')
add(52,19,'complete Pi head, stems and lower I',0,0,'medium','complete literal A021G22 with independently retained ring qualifier',
    ['A021-X19',[],[]],['g:A021G22','g:B021-G10','g:C021-G09'],
    {'A':r'A021G22: pale broken head, two stems, lower \mathrm I and qualified raised ring.','B':r'\Pi_I^{\unsure{\circ|0}} in the ordinary text node.','C':r'\Pi_I^{\unsure{\circ|0}} in the ordinary text node.'},
    kind='drawing or diagram',area='corheading',wC=r'\Pi_I^{\unsure{\circ|0}}',wH=r'\Pi_I^0',groups=['A021G22'],physical='L021-51',
    evidence='The selected complete Pi group retains the pale broken head and interrupted right stem together with the lower I and raised ring.')
add(53,19,'pale upright above first corollary V',1,1,'low','qualified point-only C021-M05 above V',
    ['A021-X20','B021-D25','C021-M05'],['g:A021M03','g:B021-G10-V-speck','g:C021-M05'],kind='omission',doubt=True,
    alternatives='role, hand, attachment and surface origin undetermined',area='corheading',wC='absent',wH='absent',groups=['C021-M05'],
    evidence='The independent pale upright above V remains a qualified detached trace; V stays outside the point-only group.')
add(54,20,'corollary union pale left retrace',1,1,'medium','C021-G09a: round union and separate pale left return',
    [[],[],'C021-D16'],['d:6','g:B021-G10','g:C021-G09a'],
    {'A':r'\bigcup_{\alpha\in K}, ordinary union macro.','B':r'\displaystyle\bigcup_{\alpha\in K}, ordinary union macro.','C':'C021-G09a: dark bowl and separate pale left-return path.'},
    kind='drawing or diagram',area='corformula',wC=r'\bigcup',wH=r'\bigcup',groups=['C021-G09a'],
    evidence='A separate pale short return lies beside the cup’s upper-left stalk; the completed source preserves both paths and the original union reading.')
add(56,21,'précédent first accent',1,1,'low',r'pr\unsure{ê|é|e}cédent',['A021-X21','B021-D26','C021-D12'],['A021-X21','B021-D26','C021-D12'],
    {'A':r'pr\unsure{é|ê|e}c\unsure{é|e}dent','B':r'pr\unsure{é|ê}c\unsure{é|è}dent','C':r'pr\unsure{é|ê}cédent'},
    doubt=True,alternatives='é; unaccented e',area='corprose',wC='précédent',wH='précédent',groups=['C021-G09'],
    evidence='The first high accent has a rising left stroke and bent return; circumflex is primary while acute and absent-accent states remain supported.')
add(57,21,'précédent second accent',1,0,'low',r'préc\unsure{é|è|e}dent',['A021-X22','B021-D27',[]],['A021-X22','B021-D27',r'l:pr\unsure{é|ê}cédent'],
    {'A':r'pr\unsure{é|ê|e}c\unsure{é|e}dent','B':r'pr\unsure{é|ê}c\unsure{é|è}dent','C':r'pr\unsure{é|ê}cédent, second é firm'},
    doubt=True,alternatives='è; unaccented e',area='corprose',wC='précédent',wH='précédent',groups=['C021-G09'],
    evidence='The second high stroke is a short near-upright tick; acute remains primary with grave and absent-accent alternatives independently retained.')
add(58,21,'unique underline, dash and on a',0,0,'high',r'\uline{unique} -- on a',[[],[],[]],['s:10','g:B021-G10','s:13'],
    {'A':r'\uline{unique} -- on a','B':'unique with one literal underline, separate dash path and on a node.','C':r'\uline{unique} --, followed by the on a node.'},
    area='corprose',wC=r'\uline{unique} -- on a',wH=r'\emph{unique} — on a',groups=['C021-G09'],
    evidence='One underline spans unique and the following dash is a separate horizontal run; the adjoining prose occurs once.')
canonical(59,22,13,1,1,'high',r'\deleted{V}E_\alpha, complete overlap',doubt=False,status='resolved',area='bottom',
    wC=r'\deleted{\unsure{V}}E_\alpha',wH=r'E_\alpha',groups=['C021-G09b'],
    evidence='Two thin V obliques survive under the live E’s upright and bars; the completed source preserves the predecessor and live glyph at one location without an added strike.')
add(60,22,'complete bottom-brace geometry parent',1,1,'medium','outer brace to physical edge with literal opening and closing set braces',
    ['A021-X24','B021-D29','C021-D15'],['g:A021G24','g:B021-G10','g:C021-G09'],kind='drawing or diagram',area='bottom',
    wC=r'\left\{ and generic \{ ... \} set braces',wH=r'\begin{cases} and generic \{ ... \} set braces',groups=['C021-G09','B021-G10'],
    evidence='The completed outer brace retains its closed middle turn and lower run to the physical edge; the opening set loop and complete right closing curve remain separate source components of this one parent.')
for n,label in [(61,'outer bottom brace'),(62,'opening bottom set brace'),(63,'closing bottom set brace')]:
    add(n,22,label+' component',0,0,'medium','complete literal '+label,[[],[],[]],['s:11','g:B021-G10','g:C021-G09'],
        {'A':'Literal outer brace and generic set braces in A’s complete final-condition source.','B':'Complete literal outer, opening-set and closing-set brace paths in B021-G10.','C':'Literal outer brace and generic set-brace glyphs in C021-G09.'},
        kind='drawing or diagram',area='bottom',wC='generic brace source at this component',wH='generic brace source at this component',groups=['C021-G09','B021-G10'],
        Cparent='L021-60',Hparent='L021-60',physical='L021-60',evidence='This literal brace component belongs to the single completed bottom-brace-geometry parent and adds no duplicate count.')
add(65,22,'last complement: Sigma identity',0,1,'high',r'X\setminus\Sigma_\alpha',['A021-X26','B021-D30','C021-D13'],['A021-X26','B021-D30','C021-D13'],
    kind='misread symbol or index',area='bottom',wC=r'X\setminus\Sigma_\alpha',wH=r'X\setminus E_\alpha',groups=['C021-G09'],
    evidence='The final complement’s glyph has the angular bent Sigma body and low alpha; the complete last condition retains Sigma at this occurrence.')
add(67,23,'lead-in before second inclusion',0,1,'high','cela implique que',['A021-X11','B021-D21','C021-D10'],['A021-X11','B021-D21','C021-D10'],
    kind='misread word',area='cela',wC='cela implique que',wH='ce qui implique que',evidence='The opening has the small c, low run and tall l-loop with its continuation; the selected opening word is cela.')
add(68,24,'complete corollary left side rule',1,1,'medium','A021G25 complete bowed rule path',
    ['A021-X23','B021-D28','C021-D14'],['g:A021G25','g:B021-G10','g:C021-G09'],kind='drawing or diagram',area='rule',
    wC='straight tabular left rule',wH=r'\note{le corollaire, encadré d’un trait vertical, ...}',marked=True,groups=['A021G25','C021-G09'],
    evidence='The continuous dark side run has a shallow lower bend and both visible endpoints; the lower endpoint stops shortly before the paper boundary, and the rule owns no adjacent word.')
add(69,24,'isolated point left of corollary rule',1,1,'low','qualified C021-M06 detached point',
    [[],[],'C021-M06'],['corollary','g:B021-G10','g:C021-M06'],
    {'A':'No corresponding point in the inspected complete corollary source.','B':'No corresponding point in the inspected complete lower-body source B021-G10.','C':'C021-M06: qualified point left of the corollary rule.'},
    kind='omission',doubt=True,alternatives='role, hand and surface origin undetermined',area='rule',wC='absent',wH='absent',groups=['C021-M06'],
    evidence='The isolated small point left of the rule is retained at its detached position without an assigned letter, punctuation role, hand or surface origin.')
add(70,25,'S proposal and locally existing roofs/bar',0,0,'high','existing six roofs and bottom V bar retained; no quoted S example matched',
    [[],[],[]],['whole','whole','whole'],
    {'A':'No exact quoted S example matches this page; six roofs and the lower V bar already occur in C/H.','B':'No exact quoted S example matches this sheet; the local V bar and six roofs already occur in C/H.','C':'S’s quoted examples have no matching formula on this sheet; the V bar and six roofs already occur in C/H.'},
    area='whole',wC='six roofed Sigma groups and lower overline V present',wH='six roofed Sigma groups and lower overline V present',source_only=True,
    evidence='The broad scans015–022 proposal records no scan view by its author; the three complete returns report no matching quoted example, and the observed existing marks remain unchanged.',
    extra=dict(S_id='SA01-K81-06',S_status='no quoted example matched; existing marks retained'))
add(71,25,'agreed prose, formula companions, heading and archive comment',0,0,'high','complete agreed source remainder, including archive comment 20',
    [[],[],[]],['whole','whole','whole'],
    {'A':'Complete A reading.tex with its independently recorded ordinary prose, formula companions, title underline and archive comment.','B':'Complete B reading.tex with its independently recorded ordinary prose, formula companions, literal title underline and archive comment.','C':'Complete C reading.tex with its independently recorded ordinary prose, formula companions, title underline and archive comment.'},
    area='whole',wC='complete ordinary source remainder',wH='complete ordinary source remainder, including diagram/frame apparatus as scoped separately',source_only=True,
    evidence='The agreed ordinary words, formula companions, heading and underline spans remain anchored to the complete independent sources; archive 20 stays a comment.')


# Nineteen individually journaled Sigma upper-run qualifications.
HEADS=[(4,3,1,'C021-G01a'),(5,3,2,'C021-G01'),(6,4,3,'C021-G01'),(7,4,4,'C021-G01'),
       (16,7,5,'A021G05'),(23,11,6,'C021-G03'),(26,12,7,'C021-G04'),(27,12,8,'C021-G04'),
       (42,16,9,'A021G10'),(43,16,10,'A021G12'),(48,18,11,'C021-G08'),(49,18,12,'C021-G08'),
       (55,20,13,'A021G15'),(64,22,14,'C021-G09'),(66,22,15,'C021-G09'),
       (33,14,16,'A021D01'),(34,14,17,'A021D02'),(35,14,18,'B021-G06-middle-row'),(36,14,19,'A021D04')]
macros=[r'\widehat{\Sigma}_{\alpha_0}',r'\widehat{\Sigma}_i^+',r'\Sigma_{\alpha_0}',r'\Sigma_i',
        r'\widehat{\Sigma}_\alpha^+',r'\widehat{\Sigma}_\alpha^+',r'\widehat{\Sigma}_{\alpha_0}^+',
        r'\Sigma_{\unsure{\alpha_0|\alpha}}^-',r'\Sigma_{\alpha_0}^+',r'\Sigma_i^+',r'\Sigma_i^+',r'\Sigma_\alpha^+',
        r'\widehat{\Sigma}_\alpha^+',r'\Sigma_\alpha^+',r'\Sigma_\alpha',r'\Sigma_i^+',r'\Sigma_i^-',
        r'\unsure{\Sigma_{i\alpha}|\Sigma_{i,\alpha}}',r'\Sigma_{\alpha_0}^+']
areas=['first']*4+['upper','central','middle','middle','exclusion','exclusion','conclusion','conclusion','corformula','bottom','bottom']+['margin']*4
for n,sec,index,gid in HEADS:
    cross=U['recurring_Sigma_head_source_crosswalk'][index-1]
    hmacro=macros[index-1]
    if index==8:hmacro=r'\Sigma_{\alpha_0}^-'
    if index==15:hmacro=r'E_\alpha'
    if index==18:hmacro=r'\Sigma_\alpha in the complete diagram note'
    add(n,sec,cross['location']+': separate upper-run role',1,0,'low','complete Sigma group; head/retrace | independent upper rule',
        [[],[],[]],['whole']*3,kind='drawing or diagram',doubt=True,alternatives='independent upper-rule role',area=areas[index-1],
        wC=macros[index-1],wH=hmacro,marked=index>=16,groups=[gid],Hparent='L021-30' if index>=16 else ('L021-65' if index==15 else None),
        evidence='The short upper run and bent letter body remain in the complete local glyph group; their head/retrace-versus-independent-rule role stays qualified without an assigned overline operation.',
        extra=dict(head_crosswalk_id=cross['id'],printed_qualifier=index==1,head_source_crosswalk=copy.deepcopy(cross)))


SPECS.sort(key=lambda s:s['id'])
assert [s['id'] for s in SPECS]==[f'L021-{i:02d}' for i in range(1,72)]
spec_by={s['id']:s for s in SPECS}
spec_by['L021-59']['reader_ids']['A'].append('A021-X25')
spec_by['L021-59']['reader_ids']['C'].append('C021-D17')
spec_by['L021-18']['reader_ids']['C'].append('C021-D02')
ht=(BASE/'packets/021/H.tex').read_text()
for n,begin,end in [(30,r'\note{à droite,',"d'autre part"),(68,r'\note{le corollaire,',r'\end{document}')]:
    item=next(s for s in SPECS if s['id']==f'L021-{n:02d}')
    item['witness_H']=ht[ht.index(begin):ht.index(end,ht.index(begin))].strip()
write('scan021_record_specs.json',dict(scan=21,root_journal=dict(path=JP,sha256=sha(BASE/JP)),specifications=SPECS,main_adjudicated=False))


def reader_mapping(spec):
    public={};provenance={};reported={}
    head=spec['extra'].get('head_source_crosswalk')
    for r in 'ABC':
        if head:
            h=head['readers'][r];rows=copy.deepcopy(h['raw_report_sources']);sources=[copy.deepcopy(h['actual_tex_source'])]
            wording='; '.join(x['value']['reading'] for x in rows)
            form=h['actual_source_form']
            if form.startswith('ordinary'):
                wording=sources[0]['excerpt']
            else:
                wording=(wording+'; ' if wording else '')+form
                if r in 'AC' and rows:
                    wording+='; local head/retrace | independent upper-rule role retained'
            public[r]=wording
            silent=h['report_silent_local_choice']
        else:
            rows=[copy.deepcopy(RAW[r][rid]) for rid in spec['reader_ids'][r]]
            sources=[scope(r,spec['reader_scope_selectors'][r])]
            wording='; '.join(row['value']['reading'] for row in rows)
            public[r]=spec['public_readers'].get(r,wording or sources[0]['excerpt'])
            silent=not rows
        reported[r]=[row['value'].get('reading') for row in rows]
        provenance[r]=dict(original_difference_rows=rows,actual_complete_tex_sources=sources,report_silent_choice=silent,
            source_scope='Exact inspected complete local TeX source; original report wording retained separately. Absence assertions apply only within this source span.')
    return public,provenance,reported


decisions=[]
for s in SPECS:
    ref=section(s['section']);refs=[ref]
    if s['id']=='L021-03':refs.append(section(26))
    if s['id'] in ['L021-18','L021-19','L021-20']:refs.append(section(27))
    crop=re.search(r'Viewed `([^`]+)`',ref['excerpt'])
    pub,provenance,reported=reader_mapping(s)
    row=s['original_C_row']
    d=dict(id=s['id'],location=s['location'],C=s['witness_C'],H=s['witness_H'],final=s['final'],readers=pub,
        readers_report_only=reported,reader_provenance=provenance,confidence=s['confidence'],kind=s['kind'],
        evidence=s['evidence'],diff_C=bool(s['C']),diff_H=bool(s['H']),marked_in_H=s['marked_in_H'],
        marked_in_H_basis='Relevant H uncertainty/deletion/illegibility marker or the explicitly shared H diagram/frame apparatus is present in the attached H scope.' if s['marked_in_H'] else 'The relevant H local reading has no uncertainty, deletion, illegibility or apparatus marker.',
        witness_provenance={r:dict(actual_complete_source=copy.deepcopy(WS[r][s['witness_scope']]),public_reading=s['witness_'+r]) for r in 'CH'},
        C_doubt_status=s['C_doubt_status'],source_C_doubt_rows=[row] if row else [],source_C_doubt_parts=[row+'-1'] if row else [],
        remaining_doubt=s['remaining_doubt'],alternatives=s['alternatives'],root_evidence_source=ref,root_authorization_sources=refs,
        root_decision_section=s['section'],crop=crop[1] if crop else None,
        root_ink_choice_applied=not s['root_source_audit_choice_applied'],root_source_audit_choice_applied=s['root_source_audit_choice_applied'],
        root_source_authorization_sha256=sha(BASE/JP),selected_source_groups=s['selected_source_groups'],
        C_count_parent=s['C_count_parent'],H_count_parent=s['H_count_parent'],physical_count_parent=s['physical_count_parent'],
        final_source_attachment=[],main_approved=False,log_decision=True,mathematical_consequence=None,
        count_status='Root-journal physical count copied; final approval pending.')
    for key,value in s['extra'].items():
        if key!='head_source_crosswalk':d[key]=copy.deepcopy(value)
    if d.get('S_id'):
        d['S_source']=copy.deepcopy(U['sources']['packets/021/S_rows.json'])
        d['reader_S_source_assessments']={r:copy.deepcopy(U['reader_sources'][r]['extra_source_fields']['S_coverage' if r=='C' else 'S_assessment']) for r in 'ABC'}
    decisions.append(d)

by={d['id']:d for d in decisions}
original_rows=copy.deepcopy(U['C_doubt_crosswalk'])
for row in original_rows:
    for part in row['source_parts']:
        relevant=[d for d in decisions if part['part_id'] in d['source_C_doubt_parts']]
        assert len(relevant)==1,(part['part_id'],[d['id'] for d in relevant])
        d=relevant[0]
        part.update(original_source_decision_status=part['decision_status'],root_status=d['C_doubt_status'],
            root_decision_ids=[d['id']],root_evidence_sources=copy.deepcopy(d['root_authorization_sources']),main_approved=False,final_source_attachment=[])
    row['root_original_row_status']=row['source_parts'][0]['root_status']
    row['root_decision_ids']=row['source_parts'][0]['root_decision_ids']
    row['final_source_attachment']=[]
doubts=[dict(decision_id=d['id'],location=d['location'],reading=d['final'],alternatives=d['alternatives'],confidence=d['confidence'],
    reason=d['evidence'],readers=copy.deepcopy(d['readers']),reader_provenance=copy.deepcopy(d['reader_provenance']),
    source_C_doubt_rows=d['source_C_doubt_rows'],source_C_doubt_parts=d['source_C_doubt_parts'],crop=d['crop'],
    root_authorization_sources=copy.deepcopy(d['root_authorization_sources']),final_source_attachment=[],main_approved=False)
    for d in decisions if d['remaining_doubt']]
counts=dict(C=sum(d['diff_C'] for d in decisions),H=sum(d['diff_H'] for d in decisions),decision_loci=len(decisions),remaining_doubt_loci=len(doubts),
    by_witness_confidence={w:dict(Counter(d['confidence'] for d in decisions if d['diff_'+w])) for w in 'CH'})
assert counts['C']==45 and counts['H']==24 and len(doubts)==39,counts
assert counts['by_witness_confidence']=={'C':{'medium':8,'low':33,'high':4},'H':{'medium':8,'high':5,'low':11}},counts
outcomes=dict(Counter(row['root_original_row_status'] for row in original_rows))
assert outcomes=={'retained':9,'resolved':6},outcomes
coverage={r:{} for r in 'ABC'}
for r in 'ABC':
    for rid,raw in RAW[r].items():
        dids=[d['id'] for d in decisions if any(item['value']['id']==rid for item in d['reader_provenance'][r]['original_difference_rows'])]
        assert dids,(r,rid,'uncovered original difference')
        coverage[r][rid]=dict(original_source=copy.deepcopy(raw['source']),root_decision_ids=dids)
meta=json.loads((BASE/'packets/021/metadata.json').read_text())
record=dict(scan=21,folder=meta['folder'],their_page=meta['their_page'],hua_has=meta['hua_has'],filename=Path(meta['codex_file']).name,
    source_record_brief_version='v03',main_adjudicated=False,main_approved=False,released_readers=list('ABC'),pending_readers=[],
    decisions=decisions,doubts=doubts,inventory=[],candidate_inventory=copy.deepcopy(U['candidate_inventory']),
    notes=r"The author writes $\alpha_0\in K_1$, then $\widehat{\Sigma}_{\alpha_0}\cap\widehat{\Sigma}_i^+=\varnothing$, followed by i.e and $\Sigma_{\alpha_0}\cap\Sigma_i=\varnothing$. The first roofed Sigma has no raised plus. The page gives $U=X\setminus\bigcup_{\alpha\in K}\widehat{\Sigma}_\alpha^+$ with $K=K_1\cup\{i\}$ and ends the proof with $\Sigma_i^+\cap\Sigma_\alpha^+=\varnothing$, cqfd. The underlined Corollaire du lemme calls the written expression $V=X\setminus\bigcup_{\alpha\in K}\widehat{\Sigma}_\alpha^+$ unique; its K condition uses $\overline V\cap E_\alpha\ne\varnothing$, i.e. $E_\alpha\cap\dot V\ne\varnothing$. Its last complement reads $X\setminus\Sigma_\alpha$. These are attributed manuscript assertions; no proof check was performed. The cancelled Sigma group, cancelled impli/impl., recovered V beneath E and unresolved retracing after Or remain explicit. The separate Sigma upper-run roles remain qualified. No written date or author page number is reported; archive 20 remains a source comment.",
    abbreviations=[dict(form=form,expansion=expansion,main_approved=False,root_authorization=section(25),final_source_attachment=[]) for form,expansion in
        [('i.e','id est (c’est-à-dire)'),('i.e.','id est (c’est-à-dire)'),('cqfd.','ce qu’il fallait démontrer'),('comp.','composante')]],
    check_events=[],C_source_rows=original_rows,C_doubt_resolution_counts=dict(actual_rows=15,actual_parts=15,original_rows=outcomes,
        resolved_primary_parts=6,retained_primary_parts=9,pending_primary_parts=0,
        resolved_source_rows=[row['source_id'] for row in original_rows if row['root_original_row_status']=='resolved'],
        retained_source_rows=[row['source_id'] for row in original_rows if row['root_original_row_status']=='retained']),
    counts=counts,source_union_manifest='out/checks/scan021_source_union.json',source_union_sha256=sha(OUT/'scan021_source_union.json'),
    root_journal=dict(path=JP,sha256=sha(BASE/JP)),root_approval_status='Complete explicit journal choices copied; selected-source attachments and final root approval pending.',
    root_choices_applied_through_section=27,pending_root_decision_ids=[],pending_root_confidence_ids=[],
    source_attachment_status='Awaiting tex021 selected draft/map.',
    reader_raw_rows={r:copy.deepcopy(v['raw_rows']) for r,v in U['reader_sources'].items()},
    reader_extra_source_fields={r:copy.deepcopy(v['extra_source_fields']) for r,v in U['reader_sources'].items()},
    candidate_graphical_groups=copy.deepcopy(U['candidate_graphical_groups']),
    original_reader_difference_coverage=coverage,
    original_source_issues=copy.deepcopy(U['source_issues']),S_source_rows=copy.deepcopy(U['sources']['packets/021/S_rows.json']['value']),
    processing_provenance=dict(clerk_source_only=True,clerk_image_views=0,optional_mathematical_or_coordinate_computations=0,
        source_offsets_hashes_and_record_bookkeeping_only=True,reader_operations_preserved_without_rerun=True,
        source_preparation_history=copy.deepcopy(U['preparation_history'])),
    source_counting_constraints=[dict(parent=d['id'],C_children=[x['id'] for x in decisions if x.get('C_count_parent')==d['id']],
        H_children=[x['id'] for x in decisions if x.get('H_count_parent')==d['id']]) for d in decisions if any(x.get('C_count_parent')==d['id'] or x.get('H_count_parent')==d['id'] for x in decisions)])
write('scan021_record_draft.json',record)
write('scan021_C_doubt_outcomes.json',dict(scan=21,counts=record['C_doubt_resolution_counts'],rows=original_rows,root_journal=record['root_journal'],main_adjudicated=False))
print(json.dumps(dict(record='out/checks/scan021_record_draft.json',sha256=sha(OUT/'scan021_record_draft.json'),counts=counts,C_outcomes=outcomes,approval=False),ensure_ascii=False))
