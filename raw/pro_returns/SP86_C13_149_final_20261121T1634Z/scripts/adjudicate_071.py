"""Root adjudication of the fixed 071 blind return."""
from pathlib import Path
import json,csv
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan071';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit');p=B/'pages'/f'{page}.tex';t=p.read_text()
pref=r'pr\unsure{é|e}fère';old=r'\deleted{\unsure{nor-|pro-}}';tail=r't. \deleted{\unsure{un|de}}';neg=r'\unsure{ne|un} recouvrent pas';point=r'$\geq 2$\unsure{.}'
for a,b in [('préfère',pref),(r'\deleted{\unsure{nor-}}',old),(r'\deleted{\unsure{tant}}',tail),('ne recouvrent pas',neg),(r'$\geq 2$',point)]:assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t);c={x['id']:x for x in r['changes']}
pe='The initial p descends deeply, then the r/e group is compressed into a low arch before the tall looped f. A detached accent over the later e is clear, and the terminal r/e is readable. No separately recoverable first acute can be isolated from the compressed pre-f strokes. Preserve pr-é/e-fère while retaining the visible f and ending that support a departure from H prend.'
oe='The raised fermé remains live: tall f, small e loop, low r/m and final accented e. Its long f descender reaches the lower cancellation. Beneath it, the first crossed character has a short descending stem and shoulder that can be n or p; the next low bodies merge under the horizontal strike and the terminal dash remains. Preserve nor-/pro- without expansion, and keep the upper word inserted after sous-groupe.'
te='At the left stands a tall t with its own slanting crossbar returning to its foot; a separate compact dark stop follows it. The two long cancellation strokes begin to the right of that stop and cross a low run with one higher loop. Thus the t. remains live. The following canceled run admits un/de, with its intersections still unresolved. Preserve the preceding line-end pour- and this live t. literally; no full word is supplied.'
ne='The first short word has one shallow cup, a central rise and a long low terminal return. Its component boundaries leave ne/un open. The following recouvrent retains the r/e, c, small o/u, v, r/e, n/t sequence, and pas follows with a deep p. All remain live and retain this observed order.'
pte='The relation has two oblique strokes meeting at a right-pointing angle and a separate lower slanted stroke; the numeral 2 has its upper hook, curved descent and long foot. The geq/geqslant encodings map to those same three relation strokes. A detached round dark mark sits below the left part of the 2, inside the box. Its placement leaves an intended point versus incidental pen mark unresolved; preserve a doubtful point without assigning it the status of a settled punctuation correction.'
for i,f,ev in [('P07',pref,pe),('P08',old+r'\inserted{fermé}',oe),('P10',tail,te),('P11',neg,ne)]:c[i].update(final=f,evidence=ev,confidence='medium' if i!='P10' else 'low')
c['P10'].update(against_C=True,kind='deletion state',error_category='Struck text')
stateev='The live terminal letter visibly has an upper and a lower rounded lobe. Longer doubled upright traces and a crossing middle return leave its earlier-F/retracing state open. The final text still places the whole E/possible-canceled-F-plus-E group under uncertainty. Record the mark as undecided at that full extent; its live E component is visible, but the expanded state alternatives are not a settled correction against C or H.'
c['P02'].update(against_C=False,evidence=c['P02']['evidence'].split('Against_C counts')[0]+stateev,accounting_note='Unresolved state broadening at the same E is excluded from material counts against both witnesses.')
r['changes']=[x for x in r['changes'] if x['id']!='P02'];r.setdefault('nonmaterial_observations',[]).append(c['P02'])
q={x['box']:x for x in csv.DictReader((B/'second'/f'{page}_boxes.tsv').open(),delimiter='\t')}['B16'];xy=[int(q[k]) for k in ['x0','y0','x1','y1']]
r['nonmaterial_observations'].append(dict(id='A_B16',place='line 5, point below the numeral 2',C=r'\geq 2',H=r'\geq 2',final=point,evidence=pte,crop=f'crops/{page}_B16_second.png',box=xy,confidence='low',against_C=False,against_H=False,kind='other',error_category='Other',marked_in_H=False,consequential=False,accounting_note='The possible punctuation is left unresolved and is recorded in doubts; it adds no settled material witness correction.'))
for d in r['decisions']:
 if d['id']=='M1195':d.update(decision='undecided',reading=r'\unsure{E|\deleted{F}E}',evidence=stateev,confidence='medium')
for d in r['doubts']:
 if d['place'].startswith('P08'):d.update(reading=old,alternatives='nor-/pro- within the canceled lower fragment',reason=oe)
 if d['place'].startswith('P10'):d.update(reading=tail,alternatives='live t.; following canceled un/de',reason=te)
r['doubts'].extend([dict(place='P07, line 11, first accent',reading=pref,alternatives='é/e before f',confidence='medium',reason=pe),dict(place='P11, line 18, short opening word',reading=neg,alternatives='ne/un before recouvrent pas',confidence='medium',reason=ne),dict(place='A_B16, line 5, mark below 2',reading=point,alternatives='intended point; incidental pen mark',confidence='low',reason=pte)])
r['notes'][2]='Source continuation: the paragraph compares the written kernels and then speaks of a sous-groupe with the raised replacement fermé over canceled nor-/pro-. It continues with the opens S\'_i and the written line-end pour-, followed by live t. and a canceled un/de fragment. The subsequent ne/un remains uncertain, followed by the live recouvrent pas S, seulement S\'. The page ends without punctuation after que la section; no continuation is supplied.'
r['notes'][5]='The live E component at M1195 is visible; the complete group remains undecided between retraced E and possible canceled F beneath E. This state broadening is excluded from material C/H counts. P03 resolves the separate nested canceled pi_1 doubt. The prose shorthand and final signifier/signifie remain uncertain.'
r['notes'].append('The blind audit leaves the first accent of préfère uncertain and preserves the small detached mark below the numeral 2 as a doubtful point. The actual bound remains ≥2. The source spelling pour- followed by live t. is retained with the line-end hyphen; no expanded pourtant is substituted.')
for h in r['hand']:
 if h['form']=='rounded E':h['witness_errors']='The live E component is visible, while the full mark remains undecided as a retracing/possible earlier-F state. This uncertainty broadening adds no material witness correction; H mathcal E maps to the same live two-lobed body.'
 if h['form']=='long f descender and cancellation':h['observation']=oe
r['hand'].append(dict(form='live abbreviation before a cancellation',observation=te,places='B10 / P10, line 18 after pour-',scope='This crop only; no general cancellation rule inferred.',witness_errors='C wraps the whole tentative tant as canceled; the t and stop are live, and only the following run is crossed.'))
for v in r['inventory']:
 if v['element']=='E08':v['first_words_or_objects']=old
 if v['element']=='E10':v['first_words_or_objects']=r'\deleted{\unsure{un|de}}';v['position']='line 18 after live t., P10/B10'
order=['E03','E01','E02','E05','E06','E07','E09','E08','E10','E04'];r['inventory'].sort(key=lambda v:order.index(v['element']))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,ev):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=ev)
def change(b,final,title,ev):D[b]=dict(final=final,changed=True,decision=title,evidence=ev)
keep('B01','Retain the canceled and live alors','The first a, tall looped l, o, r and s are crossed by the long horizontal strike. In the second occurrence a closed lower a bowl and its right stem lead directly to the tall l; the o, r, s and separate comma remain live. The additional short upper retrace does not obscure the a bowl or extend the first cancellation across the second word.')
keep('B02','Retain the complete relation and its unresolved E state',stateev+' Both pi signs retain their top bars, legs and low 1s; the first S carries a prime. The rightward arrow has a separate tilde above it and the equals has two bars. Plain E and mathcal E refer to the same rounded destination body, with the extra traces explicitly retained in the state alternatives.')
keep('B03','Retain the resolved canceled pi_1','The canceled group has a long pi top bar and two downward legs; a separate low 1 stands at its right. A crossing sweep traverses the pi and joins the lower strike under the 1, ending before live E_K. The following map has one shaft and a small joined right head. The rounded E bodies and their low K/S map component by component to the blind mathcal renderings.')
keep('B04','Retain the two alternatives for the shorthand','The upper component is a separate near-horizontal bar. The lower starts in a shallow cup, rises into a small central cusp and continues almost flat to a thick terminal return. Those visible components retain the equals/flattened-barred-m alternatives. The independent barred-m reading is already the second candidate; the compressed lower contour does not settle the choice.')
keep('B05','Retain the unheaded connector','The horizontal connector ends in one thick rounded/upturned tip, with no separate pair of oblique wings. Compare B03, whose tip has a joined angular head. E_K and E_S-prime have their visible low indices, and the comma follows. The blind uncertainty includes the selected headless stroke; no arrowhead is supplied.')
keep('B06','Retain ou, si on','The first closed oval leads down into a valley and then a broad rounded arch/down-return, supporting u after o. The angular short r shoulder seen at the line-end pour- is not separately articulated in this broad arch. The following comma, s with i dot, and compact o/n remain visible. Retain ou at the existing medium confidence.')
change('B07',pref,'Qualify the first accent',pe)
change('B08',old+r'\inserted{fermé}','Qualify the lower canceled fragment',oe)
change('B10',tail,'Separate live t. from the following canceled ink',te)
change('B11',neg,'Qualify the short word before the live verb',ne)
keep('B12','Retain censé and the uncertain final r','Censé shows an open c, low e/n, short s and accented e. The next word shows s/i, g and its long return, n/i, tall f, dotted i and e followed by a flat exit. A distinct terminal r shoulder is still inseparable from that exit. The blind signifier agrees with the first candidate, but the existing signifier/signifie uncertainty remains.')
keep('B15','Retain the numeral 1','One slanting head leads to a single main upright and long horizontal foot. Both returns read the same numeral; the blind math wrapper adds no glyph or attachment.')
change('B16',point,'Preserve the detached mark as doubtful punctuation',pte)
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_a')
