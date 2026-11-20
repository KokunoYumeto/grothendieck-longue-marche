from pathlib import Path
import json,csv,datetime
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'review/scan003_review.json').read_text())
t=(R/'review/scan003_proposed.tex').read_text()
kindmap={
'C doubt resolved':'other','source punctuation form':'other','words and omissions':'misread word',
'marginal text omitted or misread by H':'readable ink left as \\ill{}','different word':'misread word',
'insertion state':'insertion or placement','abbreviation and C doubt resolved':'abbreviation expanded or spelling modernised',
'H added word':'text not on the page','retained alphabet doubt':'misread symbol or index',
'different ending and C doubt resolved':'misread word','insertion attachment':'insertion or placement',
'functor spelling':'misread symbol or index','written accent':'other',
'deleted text omitted by H':'deletion state (struck given live or live given struck)'}
cs=[]
for c in d['changes']:
 if c['id']=='S003-02':continue
 c['reader_kind']=c['kind'];c['kind']=kindmap[c['kind']]
 c['crop']=(c.get('crop') or '').removeprefix('out/')
 c['against_C']=False
 # Subordinate resolutions in the full marginal passage do not count that same H omission again.
 if c['id'] in ['S003-05','S003-06','S003-25']:c['against_H']=False
 c['consequential']=c['id'] in ['S003-04','S003-08','S003-17','S003-19','S003-21']
 if c['id']=='S003-14':
  c['against_H']=False
  c['scan_shows']+=' This is an unresolved alphabet choice rather than an adjudicated error in H; it is retained here as the disposition of C’s doubt.'
 cs.append(c)
quotes=[
('contrée','main line 2','contree_quotes',[238,170,530,238]),
('figure élémentaire','main line 8','figure_elementaire_quotes',[240,655,855,755]),
('multistrate','main line 8','multistrate_quotes',[940,640,1350,730]),
('lieu','main line 9','lieu_point',[248,734,1662,1013]),
('lieu ponctuel','main line 9','lieu_point',[248,734,1662,1013]),
('point','main line 10','lieu_point',[248,734,1662,1013]),
('strates','upper parenthetical insertion','figure_insertions',[265,1300,1545,1570]),
('grande multiombre','main line 21','mulomb_first',[275,1818,1550,1918]),
('grande ombre','main lines 22–23','grande_ombre_quotes',[272,1900,1600,2070]),
('support','main line 26','reconstituer_deletion_support',[270,2150,1635,2317])]
for i,(word,place,crop,box) in enumerate(quotes,1):
 s="``"+word+"''"
 cs.append(dict(id=f'S003-02-{i:02d}',place=place+' quotation marks',C=s,H='« '+word+' »' if word!='support' else '« support seulement »',final=s,scan_shows='The source has two short raised strokes at each quoted boundary, not angle-shaped guillemets.'+(' The closing pair follows support, before seulement.' if word=='support' else ''),confidence='high',kind='other',crop='crops/scan003_'+crop+'.png',box=box,against_C=False,against_H=True,marked_in_H=False,consequential=False))
d['changes']=sorted(cs,key=lambda c:c['id'])
for x in d['inventory']:
 if x['kind'] not in ['insertion','deletion']:x['kind']='margin note' if x['element']=='diagonal marginal note' else 'text'
d['root_adjudication']={'reader':'GPT-6 Astra Pro root; effort not exposed','viewed':'whole original once, both full-resolution halves once, all eleven reader crops and four additional quotation crops','decisions':['Accepted the proposed diplomatic wording; eleven explicit doubts remain, chiefly under crossed marginal ink.','The formula alphabet M/mathcal M remains unresolved; no claim that H’s calligraphic choice is wrong.','Resolved C doubts retain the same primary letters and are not substantive C changes.','Split the grouped quotation-form decision into ten located entries.','Subordinate marginal doubt resolutions are recorded without recounting H’s already-recorded passage omission.']}
bs=[]
margin=next(c['final'] for c in cs if c['id']=='S003-04')
fix={'scan003-b03':"(voire, la notion de ``lieu ponctuel'' ou ``point'', dont il n'a pas encore été question\\ldots)",
'scan003-b04':r'\margin{'+margin+'}',
'scan003-b11':r'\inserted{$F$}',
'scan003-b12':r"\inserted{(par l'ens de ses ``strates'')}",
'scan003-b14':r"l'ens $\unsure{M|\mathcal M}$",
'scan003-b15':r'\inserted{(ordonné par $\leq$)}',
'scan003-b16':r'\inserted{ensembliste}',
'scan003-b17':r'$M$',
'scan003-b19':r'$\mathrm{Mulomb}(F)$',
'scan003-b21':r'$\mathrm{Mulomb}(F)$',
'scan003-b25':"``support''"}
for b in d['second_boxes']:
 old=b['box']
 if old in ['scan003-b06','scan003-b07','scan003-b13']:continue
 b['reading']=fix.get(old,b['reading']);b['source_box_id']=old;b['box']=f'B{len(bs)+1:03d}'
 if old=='scan003-b04':b['kind']='entire diagonal marginal note; rotate upright; read marginal text only'
 elif old in ['scan003-b11','scan003-b12','scan003-b15','scan003-b16']:b['kind']='insertion; read inserted text and its attachment'
 elif old in ['scan003-b05','scan003-b24']:b['kind']='cancelled passage'
 elif old=='scan003-b01':b['kind']='handwritten number'
 elif old in ['scan003-b14','scan003-b17','scan003-b19','scan003-b21']:b['kind']='complete mathematical expression and immediately attached text'
 else:b['kind']='word or phrase'
 bs.append(b)
for coords,reading in [([1140,1370,1455,1438],'comme'),([270,1480,480,1562],'partie')]:
 bs.append(dict(box=f'B{len(bs)+1:03d}',kind='word at line boundary',x0=coords[0],y0=coords[1],x1=coords[2],y1=coords[3],reading=reading))
d['second_boxes']=bs
(R/'review/scan003_final.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(R/'pages/H156-01_156-7_scan003.tex').write_text(t)
base=R/'second/H156-01_156-7_scan003'
for suffix,cols in [('_boxes.tsv',['box','kind','x0','y0','x1','y1']),('_first.tsv',['box','reading'])]:
 with Path(str(base)+suffix).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(bs)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'review/root_visual_log.tsv').open('a') as f:
 for p in sorted((R/'crops').glob('scan003_*.png')):f.write(f'3\tcrops/{p.name}\t{now}\troot direct crop inspection\n')
 f.write(f'3\twhole + a + b\t{now}\troot direct layout and continuous reading\n')
print(len(cs),'records;',len(bs),'blind boxes')
