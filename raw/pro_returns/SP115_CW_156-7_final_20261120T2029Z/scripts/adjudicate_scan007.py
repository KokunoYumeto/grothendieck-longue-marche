from pathlib import Path
import json,csv,datetime
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'review/scan007_review.json').read_text())
d['scan']=7
t=(R/'review/scan007_proposed.tex').read_text()
t=t.replace(r'\unsure{M|\mathcal M}','M').replace(r'\unsure{\mathscr F|\mathcal F|\mathfrak F}',r'\mathscr F')
t=t.replace(r'\unsure{élément}\unsure{.}',r'\unsure{élément}')
t=t.replace(r'\unsure{\mathrm{déf}}',r'\unsure{\mathrm{defn}|\mathrm{déf}}')
t=t.replace('quand on a simplement',r'quand on \unsure{à|a} simplement')
t=t.replace(r'$\mathrm{At}_{M}\,1$ à $\mathrm{At}_{M}\,3$',r'$\mathrm{At}_{M}\,1$ \unsure{à|:} $\mathrm{At}_{M}\,3$')
cs=d['changes']
consequential={10,11,14,15,17,18,20,21,22,23,24,27,28,29,30,33,34,35,38,39,40,41,45,46,47,48,49,51}
for c in cs:
 c['crop']=c['crop'].removeprefix('out/')
 n=int(c['id'].split('-')[-1]);c['consequential']=n in consequential
 if n==1:c.update(final='M; alphabet uncertainty consolidated at first occurrence on003',consequential=False)
 if n==2:c.update(final=r'\mathscr F; script/calligraphic uncertainty consolidated at defining occurrence on004',consequential=False)
 if n in [1,2]:c['scan_shows']+=' Root applies the shared alphabet convention; no new Gothic alternative is inferred from H alone.'
 if n==3:c.update(final=r'\unsure{élément} without an added stop',against_C=True,against_H=False,confidence='medium',scan_shows='Root sees the long cancellation extending beyond the last word, but no distinct dark point at the end. Remove the supplied stop rather than transcribing a hypothetical punctuation mark. The cancelled word itself remains doubtful.')
 if n==11:c.update(final=r'\overset{\unsure{\mathrm{defn}|\mathrm{déf}}}{\unsure{\Longleftrightarrow|\Longrightarrow}}',against_H=True,confidence='low',scan_shows='The label is directly above the double-shaft arrow. A d-like loop, descending f and small final returning stroke favour an abbreviated defn; the crossed joins and possible accent are not all plain. Neither the full word défini nor a certain three-letter label is warranted. Its placement above the arrow is clear.')
 if n==36:c.update(final=r'quand on \unsure{à|a} simplement',against_C=True,confidence='medium',scan_shows='The q descender begins quand, followed by on and a compact a-shaped letter. Root also sees a detached slant above that last letter, so literal à is primary, with unaccented a retained as an alternative. The next line starts simplement. H’s grâce à laquelle does not match the words.')
cs.append(dict(id='S007-058',place='range between At_M1 and At_M3',C='à',H='à',final=r'\unsure{à|:}',scan_shows='The existing D’autre part crop shows a detached upper point and a very short lower returning stroke. An extremely compressed à is plausible, but a colon-like form is also admitted. This is added uncertainty alone, not a substantive change count.',confidence='low',kind='other',crop='crops/scan007_dautrepart.png',box=[493,569,1684,785],against_C=False,against_H=False,marked_in_H=False,consequential=False))
# New uncertainty alone is not a collation row: retain its evidence in the doubt record.
range_record=cs.pop()
d['doubts']=[q for q in d['doubts'] if q['place'] not in ['cancelled opening axiom, M','family alphabet, first occurrence and thereafter','cancelled opening axiom, final stop']]
for q in d['doubts']:
 if q['place']=='label on cancelled first arrow':q.update(reading='defn',alternatives=['déf'],confidence='low',reason=cs[10]['scan_shows'])
d['doubts'].extend([
 dict(place='At_M1 to At_M3, range marker',reading='à',alternatives=[':'],confidence='low',reason=range_record['scan_shows']+' Crop crops/scan007_dautrepart.png [493,569,1684,785].'),
 dict(place='quand on à/a',reading='à',alternatives=['a'],confidence='medium',reason='A detached slant stands above the compact letter. The normal syntax would require a, but is not used to erase that visible stroke. Crop crops/scan007_general_case.png [523,972,1666,1164].')])
d['root_adjudication']={'reader':'GPT-6 Astra Pro root; effort not exposed','viewed':'whole once, both halves once, all25 saved crops','decisions':['Live posons insertion distinguished from cancelled i.e. formula below it.','Minimal is a clear live replacement; plus petit élément is cancelled and still partly uncertain.','First-occurrence alphabet uncertainty consolidated on003/004.','Cancelled arrow label remains abbreviated and doubtful; spurious final stop removed.','Literal possible accent in quand on à/a recorded separately from grammatical expectation.','Both overwritten numeral states and the two curved interchange strokes retained.']}
lines=t.splitlines()
def line(p):return next(x for x in lines if x.startswith(p))
def seg(a,b):return t[t.index(a):t.index(b)].strip().replace('\n',' ')
top=line(r'$\mathrm{At}_{M}\,4$')
para=line("D'autre part")
reads={
1:r'\mspage{6}',2:line(r'\deleted{$\mathrm{At}_{M}\,4'),
3:top[:top.index(' Si $X')],
4:r'\deleted{\unsure{plus petit élément}} \inserted{élément minimal}',
5:top[top.index(r'\inserted{dans}'):],
6:line(r'\margin{J\'ai') if False else line("\\margin{J'ai"),
7:line(r'\text{b) Alors}'),8:line(r'\mathrm{At}_{M}\,\deleted{\unsure{5}}6'),9:line(r'\mathrm{At}_{M}\,\deleted{\unsure{6}}5'),
10:line(r'\margin{\tikz'),
11:para[:para.index(r'\deleted{$\mathrm{At}_{M}')],
12:para[para.index(r'\deleted{$\mathrm{At}_{M}'):para.index(r'\deleted{\unsure{At}}')],
13:para[para.index(r'\deleted{\unsure{At}}'):],
14:line(r'\margin{i.e.'),15:line('Dans le cas'),
16:seg(r'\widetilde{\mathscr F}_{\mathrm{tf}}',r'\end{aligned}') if False else '\n'.join(lines[lines.index(line(r'\widetilde{\mathscr F}_{\mathrm{tf}}')):lines.index(line(r'\widetilde{\mathscr F}_{\mathrm{tf}}'))+2]),
17:r'\deleted{\unsure{formées} \unsure{t.q.}} \inserted{telles que :}',
18:line('Pour avoir').split('se donner')[0]+'se',
19:r"l'ens ordonné $\widetilde{\mathscr F}_{\mathrm{tf}}$ précédent\ldots",
20:line(r'\mathscr F^{*}'),21:line(r'\deleted{\text{où}}'),22:line(r'\mathrm{Omb}\,X'),
23:line('(cf Scholie').split(' sous-atelier')[0],
24:r'sous-atelier (pas néc. \unsure{spacieux|spécieux}) de $\mathrm{Fig}(M)$.',
25:r'\deleted{$\mathrm{At}_{M}\,4$}',26:r'$\mathrm{At}_{M}\,4$',27:r'$\uline{\mathrm{At}}\,\deleted{\unsure{6}}5$',
28:r'$\mathrm{At}_{M}\,\deleted{\unsure{5}}6$',29:r'$\mathrm{At}_{M}\,\deleted{\unsure{6}}5$',
30:r'$\mathrm{At}_{M}\,1$ \unsure{à|:} $\mathrm{At}_{M}\,3$',31:r'\deleted{$\mathrm{At}_{M}\,\unsure{1|0}\,(\mathrm{tf})$}',
32:r'\unsure{page|p.} 5',33:'(page 5)',34:r'$\mathrm{At}_{M}\,4,5,6$',35:'p. 28',36:'32'}
bs=json.loads((R/'review/scan007_second_boxes.json').read_text())
for i,b in enumerate(bs,1):
 b['source_box_id']=b['box'];b['box']=f'B{i:03d}';b['reading']=reads[i].replace('\n',' ')
 if i==1 or i>=25:b['kind']='central handwritten numerical inscription, with any corrections and underline'
 elif i in [6,14]:b['kind']='whole marginal note, including formulas and graphic marks'
 elif i==10:b['kind']='central graphic marks; reproduce their complete shapes'
 elif i==19:b['kind']='lower complete text line, including punctuation and mathematical notation'
 elif i in [3,4,5,12,17]:b['kind']='central correction group: include deleted and inserted text and formulas'
 else:b['kind']='complete central text block or formula, including corrections and punctuation'
d['second_boxes']=bs;d['changes']=cs
(R/'pages/H156-01_156-7_scan007.tex').write_text(t)
(R/'review/scan007_final.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
base=R/'second/H156-01_156-7_scan007'
for suffix,cols in [('_boxes.tsv',['box','kind','x0','y0','x1','y1']),('_first.tsv',['box','reading'])]:
 with Path(str(base)+suffix).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(bs)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'review/root_visual_log.tsv').open('a') as f:
 for p in sorted((R/'crops').glob('scan007_*.png')):f.write(f'7\tcrops/{p.name}\t{now}\troot direct crop inspection completed before adjudication\n')
 f.write(f'7\twhole + a + b\t{now}\troot continuous layout and line reading completed; initially truncated top-half call was not counted\n')
print(len(cs),'records;',len(bs),'blind boxes;',len(d['doubts']),'remaining doubts')
