#!/usr/bin/env python3
"""Materialize the main reader's recorded scan-028 decisions."""
from pathlib import Path
from copy import deepcopy
import json
R=Path(__file__).resolve().parents[1]
raw={w:json.loads((R/f'readers/scan028/{w}/review.json').read_text()) for w in 'ABC'}
rows={w:raw[w]['loci'] for w in 'ABC'}
amap={n:n for n in range(1,17)}
amap.update({17:16,18:17,19:18,20:19,21:20,22:21,23:22,24:23,25:24,26:25,27:26,28:27})
bmap={n:n for n in range(1,7)}
bmap.update({n:n+1 for n in range(7,29)})
crops={1:'main/01_finies.png',2:'A/01_b_edge.png',3:'A/02_map_source.png',4:'C/03_parenthesis_finis.png',5:'C/03_parenthesis_finis.png',6:'C/03_parenthesis_finis.png',7:'B/B06_card.png',8:'A/05_struck_je_dis_que.png',9:'main/02_example.png',10:'main/02_example.png',11:'A/06_relation_edge.png',12:'A/07_alors_overwrite.png',13:'main/03_initial_omega.png',14:'C/07_middle_index.png',15:'A/09_slanted_margin.png',16:'main/04_compatibilites.png',17:'main/04_compatibilites.png',18:'A/10_compatibility_abbreviations.png',19:'A/10_compatibility_abbreviations.png',20:'main/07_single_rule.png',21:'main/05_extensions.png',22:'A/11_filtration_opening.png',23:'A/11_filtration_opening.png',24:'main/09_filtration_marks.png',25:'A/12_struck_before_definir.png',26:'main/06_lower_isom.png',27:'C/12_final_quotient.png',28:'main/08_double_rule.png'}
loci=[]
for n,z in enumerate(rows['C'],1):
 x=deepcopy(z);x['id']=f'S028-{n:02}'
 x['readers']={'A':rows['A'][amap[n]-1]['reading'],'B':rows['B'][bmap[n]-1]['reading'],'C':z['reading']}
 x['crop']='scan028/'+crops[n]
 x['decision']='Main reader inspected the cited crop and compared all three returns.'
 x.pop('box',None);loci.append(x)
q={n:loci[n-1] for n in range(1,29)}
q[1].update(confidence='medium',evidence='The root crop shows the tall looped f, short i marks, low connected n and ending es. The doubt on finies is removed.')
q[4].update(reading=r'\inserted{(surjection \unsure{si on veut})}',diff_C=False,confidence='medium',unresolved=True,evidence='Surjection and the raised insertion with its returning guide are clear. The following short s/i and on/veut groups remain crowded in the main crop; their proposed wording is retained with a local doubt.',decision='All three readers resolve si on veut; the main crop retains the qualification on those crowded words. The insertion state and destination are clear.')
q[8].update(confidence='low',evidence='The initial barred J, middle d ascender and final q descender survive the cancellation. Intervening low joins merge with the strike, so the main reader retains Je dis que as a qualified recovery.',decision='Retain C’s qualification, agreeing with reader C; A and B remove the doubt.')
q[10]['evidence']='The root crop has J followed directly by ens and the separate low a/v/e/c group of avec, then relation. The low initial a of avec is attached to that word; it is not a separate abbreviation point after ens. H’s added un and expanded muni d’une are absent from this visible sequence.'
q[14].update(confidence='low',evidence='The heavy small head connects to a descending segment and a turned lower foot. The main crop supports 2 before i among the remaining alternatives; no detached i dot is isolated. The wedge’s bound i is read independently.')
q[15]['evidence']='One rotated crop shows broken dark and faint flecks at the physical right edge, without a recoverable word. One estimated illegible unit is retained. No physical origin is assigned to the traces.'
q[16].update(reading=r'\unsure{Compatibilités|Compatibilité}',diff_C=True,confidence='low',unresolved=True,evidence='The final t, high accent and returning terminal body are visible. All three readers see a separate final s; the root crop leaves the joining of that final body unresolved. Both plural and singular are retained, with the readers’ plural first.',decision='The main reader adds an explicit ending doubt after comparing the unanimous plural reading with H’s singular.')
q[17].update(reading=r'underline below the first word only',readers={w:'underline below the first word only' for w in 'ABC'},evidence='The single wavy underline stops at the end of the first word, before entre. The terminal spelling is recorded in the preceding separate locus.')
q[18]['evidence']='The first upright, high returning s and low om strokes are visible. The following gap has no detached point. The separately inspected lower isom. has a visible point; each occurrence is preserved as drawn.'
q[19].update(reading=r'\unsure{can.|cas.}',diff_C=False,diff_H=True,confidence='medium',unresolved=True,evidence='Open c and the closed a bowl are followed by a low raised return with a long tail and a detached point. The final return remains ambiguous between n and s in the main crop.',decision='All three readers resolve can.; the main reader retains the existing can.|cas. alternatives.')
q[22].update(confidence='medium',evidence='The two delimiters have inward medial turns. A broad retraced oval surrounds the small central mark. That independently visible oval supports 0; the braced expression is retained and the C interior-dot doubt is resolved.')
q[24]['evidence']='The main crop shows two separate horizontal ink groups in the gap after E_2, followed by white space and the next inclusion. Both witnesses’ three-dot command is replaced by two marks; no comma is added.'
q[27]['decision']='The main crop leaves slash/stem overlap unresolved, agreeing with reader C; A and B resolve a separate slash. The quotient meaning does not settle the strokes.'
q[28]['evidence']='The main crop shows the long rising upper stroke, the shorter lower stroke starting farther right, and a detached short tick below the upper stroke’s left end. The extra tick omitted by C and reader A is added.'
loci.append({'id':'S028-29','location':'definition display, sign after I−','C':'=','H':'=','reading':'=','diff_C':False,'diff_H':False,'kind':'other','H_marked':False,'confidence':'medium','evidence':'Two separate short strokes, with a curved upper segment, follow I−. Their two-rule structure supports the retained equals sign. This earlier query is explicitly reviewed without changing the witnesses.','crop':'scan028/A/04_set_definition.png','readers':{w:'=' for w in 'ABC'},'decision':'Retain after the root crop and all three independent readings.','unresolved':False})
alts={2:('démonstration','démonstrati.'),4:('si on veut','crowded words remain qualified'),6:('C','f'),8:('Je dis que','intervening strokes obscured'),12:('O','underlying loop unresolved'),14:('2','i'),15:('one illegible unit','no lexical reading'),16:('Compatibilités','Compatibilité'),19:('can.','cas.'),23:('0','underlying loop unresolved'),25:('On','crossed word unresolved'),27:('/','no separate slash')}
doubts=[{'location':q[n]['location'],'reading':a,'alternatives':b,'confidence':q[n]['confidence'],'reason':q[n]['evidence']} for n,(a,b) in alts.items()]
notes='''### N028.1 — What the page states and asks

Paragraph b extends the preceding discussion to finite families of quadratic modules, using two literal equals signs in the prose. Paragraph c writes a map p from J to I, with a raised parenthesis about surjectivity, defines I− by odd cardinality of the fibres, and gives the equivalence-relation example. It then writes an orientation expression with ω_J, ω_{I−} and an indexed wedge of fibre terms. The compatibility line names a), b), c). Under the underlined heading “Cas d’extensions”, the page writes a filtration and asks “Définir un isom. canonique”, followed by its orientation expression. These are source statements carried as background; no proof or calculation of them was performed in this page’s review.

### N028.2 — Mathematics-directed reading decisions

The nested index in the middle orientation expression was inspected because of its relation to the wedge index. Its rounded upper lobe and hooked foot lead to 2|i; the separate bound i supplies no authority to replace it. The final slash remains qualified because its oblique overlaps the second E’s left limb. The lower strokes in both final bounds support 1≤i≤d. The small sign after I− has two separate strokes and is retained as equals. The filtration has exactly two continuation marks. These are reading decisions, with all candidate readings and crop references in the changes log; they are not mathematical verification events.

### N028.3 — Authorial qualifications and page metadata

The raised parenthesis reads “(surjection si on veut)”, with the words si on veut still qualified in the transcription. The crossed “Je dis que”, underlying O, cancelled character before finis, underlying 0 and crossed On remain locally uncertain. The final word of paragraph b meets the right scan edge. The compatibility heading’s terminal number is left open; the title “Cas d’extensions” is clear and singly underlined. Two separator drawings and one illegible slanted marginal unit are retained. There is no written date on this supplied page; its lower-corner archive number is 27 (scan 28). No further claim, date or text is supplied from outside the package.
'''
abbr={'ens':'ensemble(s)','Card':'cardinal','p. ex':'par exemple','isom':'isomorphismes','can.':'canoniques (reading remains qualified)','isom.':'isomorphisme','démonstrati.':'démonstration (unresolved edge alternative)'}
rec={'scan':28,'loci':loci,'inventory':raw['C']['inventory'],'doubts':doubts,'notes':notes,'check_events':[{'statement_id':'N028.1','date':'2026-11-20','who':'GPT-6 Astra Pro; effort not exposed; root/scan028','type':'carried as background without fault found','outcome':'The page’s finite-fibre and filtration statements are reported without a proof check. Visual symbol/word decisions are documented separately.'}],'abbreviations':[{'abbr':a,'expansion':e,'scans':[28]} for a,e in abbr.items()],'consequential':['The middle nested index remains 2|i, led by the ink; the wedge index is not used to regularize it.','The filtration begins with braces around 0 and has two continuation marks. The final quotient slash remains qualified.','H’s expanded example is replaced by the visible “J ens avec relation”; source overwrites, insertions, margin traces and separator drawings are retained.']}
(R/'decisions/scan028.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
page=(R/'readers/scan028/C/page.tex').read_text()
page=page.replace('(surjection si on veut)',r'(surjection \unsure{si on veut})')
page=page.replace(r'\uline{Compatibilités}',r'\uline{\unsure{Compatibilités|Compatibilité}}')
page=page.replace('les isom can.',r'les isom \unsure{can.|cas.}')
page=page.replace('% slanted broken traces at the right; their status as writing remains uncertain','% slanted broken traces at the right; one estimated unreadable unit')
(R/'pages/J75-04_75_scan028.tex').write_text(page)
print(json.dumps({'loci':len(loci),'doubts':len(doubts),'inventory':len(rec['inventory'])}))
