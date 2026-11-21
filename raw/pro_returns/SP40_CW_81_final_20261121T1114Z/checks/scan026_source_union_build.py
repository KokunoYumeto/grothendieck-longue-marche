"""Source-only physical-locus correspondence for the three frozen readers.

No image bytes are opened. No ink choice, mathematical claim, crop selection,
correction count, or final reading is made. Every submitted source scope stays
with its own reader. Compact record references are checked by finite replay.
"""
from __future__ import annotations
import copy
import hashlib
import json
import re
from collections import OrderedDict
from pathlib import Path

BASE=Path('/workspace/scratch/94548b74fbe0'); OUT=BASE/'out/checks'
sha=lambda b:hashlib.sha256(b).hexdigest()
sources={}; raw={}; parsed={}


def add_source(key,path,as_json=True):
 p=BASE/path;b=p.read_bytes();raw[key]=b
 sources[key]={'path':path,'sha256':sha(b),'bytes':len(b)}
 parsed[key]=json.loads(b) if as_json else b.decode()


for who in 'ABC':
 for name,suffix,as_json in [('reading.tex','tex',False),('reading.md','md',False),('report.json','report',True),('source_map.json','map',True)]:
  add_source(who+'.'+suffix,f'out/readers/026/{who}/{name}',as_json)
 crop='crop_manifest.json' if who=='A' else 'crop_audit.json'
 add_source(who+'.crops',f'out/readers/026/{who}/{crop}')
add_source('witness.C','packets/026/C.tex',False);add_source('witness.H','packets/026/H.tex',False)
add_source('C.doubts','out/checks/scan026_C_doubt_catalog.json')
add_source('H.markers','out/checks/scan026_H_marker_catalog.json')
add_source('S.scope','out/checks/scan026_S_scope.json')
expected={'A':'c5079dace4d580a4695749bb745d382e3828681f98e8c037785fc6ac985b5513','B':'1c36f765e58e84962435ac4afe055eb55e561b9f6927f8d09cc139d0562e7289','C':'7c05f3fc0f28985e2cd66c3fbe6486eaf7d38ab20a4a2f7fbf29b1742868b951'}
assert all(sources[w+'.tex']['sha256']==expected[w] for w in expected)


def esc(x):return str(x).replace('~','~0').replace('/','~1')
def resolve(key,ptr):
 v=parsed[key]
 for p in ptr.split('/')[1:]:
  p=p.replace('~1','/').replace('~0','~');v=v[int(p)] if isinstance(v,list) else v[p]
 return v
def ref(key,ptr=''):return {'source':key,'json_pointer':ptr}
def span(key,a,b,show=True):
 t=parsed[key];assert isinstance(t,str);value=t[a:b]
 out={'source':key,'start_char':a,'end_char_exclusive':b,'start_utf8_byte':len(t[:a].encode()),'end_utf8_byte_exclusive':len(t[:b].encode()),'start_line':t.count('\n',0,a)+1,'end_line':t.count('\n',0,max(a,b-1))+1,'sha256':sha(value.encode())}
 if show:out['literal']=value
 assert raw[key][out['start_utf8_byte']:out['end_utf8_byte_exclusive']]==value.encode()
 return out
def exact(key,literal,occurrence=0,within=None,show=True):
 t=parsed[key];a,b=(0,len(t)) if within is None else within
 hits=[m.start()+a for m in re.finditer(re.escape(literal),t[a:b])]
 assert len(hits)>occurrence,(key,literal,len(hits),occurrence)
 return span(key,hits[occurrence],hits[occurrence]+len(literal),show)


# Each pool object is a complete raw JSON value or an exact sequence of fields.
# Large witness paragraphs and full literal TeX bodies are dereferenced, while
# complete candidate/role/hand/state arrays are copied without alteration.
pool=[];pool_ids={}
def pool_record(key,ptr):
 sig=(key,ptr)
 if sig in pool_ids:return pool_ids[sig]
 original=resolve(key,ptr);id='R%04d'%(len(pool)+1);pool_ids[sig]=id
 item={'record_id':id,'raw_ref':ref(key,ptr)}
 if isinstance(original,dict):
  fields=[];reconstructed=OrderedDict()
  for k,v in original.items():
   field={'key':k}
   long=(k in {'C','H','C_anchor','H_anchor','source_excerpt','literal_source','source_exact'} and len(json.dumps(v,ensure_ascii=False))>700)
   if long:
    field['exact_value_ref']=ref(key,ptr+'/'+esc(k));reconstructed[k]=copy.deepcopy(resolve(key,ptr+'/'+esc(k)))
   else:
    field['value']=copy.deepcopy(v);reconstructed[k]=copy.deepcopy(v)
   fields.append(field)
  item['ordered_fields']=fields
  assert json.dumps(reconstructed,ensure_ascii=False)==json.dumps(original,ensure_ascii=False)
 else:item['value']=copy.deepcopy(original)
 pool.append(item);return id


labels={
'L001':'opening underlined definition noun and accent',
'L002':'second ens abbreviation and its following space',
'L003':'opening family alphabet after membership',
'L004':'parenthetical les hémisphères quotation marks',
'L005':'topologique, on s’intéresse au cas où les',
'L006':'second hémisphères: complete word and crossing/cancellation scopes',
'L007':'(et inserted de plus, and the curved insertion guide',
'L008':'raised equation and its guide; adjoining connexes and cancelled item',
'L009':'et où before the first E nonempty condition',
'L010':'relation between E and empty set in following si clause',
'L011':'X connexe / deleted les Sigma connexes correction, et, guide and commas',
'L012':'cancelled aussitôt/aussitot and its crossing paths',
'L013':'pale arc to the left of the main barred conclusion',
'L014':'E after the main closure intersection: upper arm/return',
'L015':'complete oblique diagram, diagramme, endpoints and connector',
'L016':'cancelled upper diagram character',
'L017':'diagram E: lower alpha/return, top arm and shared foot',
'L018':'diagram lower superset run and its extra/retraced lower stroke',
'L019':'detached point below the diagram connector',
'L020':'small trace below the first parenthetical closure roof',
'L021':'whole parenthetical ending and H’s differently placed clauses',
'L022':'peut descender context and three small flecks below peut',
'L023':'être/etre before à la fois',
'L024':'à / colon before la fois',
'L025':'last car clause, est un ouvert, and parenthesis placement',
'L026':'low comma after the last car Sigma, distinct from its raised comma',
'L027':'slash and three points below un in the last car clause',
'L028':'lower paragraph décompositions / dispositions',
'L029':'complete binary pairs and connected correction/guide group',
'L030':'second pair left delimiter and its right brace context',
'L031':'cancelled distinctes after the binary pairs',
'L032':'inserted de X, and its bent guide',
'L033':'qu’elles and its long q descender',
'L034':'complete non adjective, underline and p return',
'L035':'two detached points below the adjective underline',
'L036':'baseline si, inserted distinctness clause, guide and following words',
'L037':'on / three traces before peut trouver',
'L038':'first disjointness operator and adjacent detached point',
'L039':'d’où/d’ou and the exact apostrophe character in the first display',
'L040':'first E in the d’où display, with its local upper curve',
'L041':'second E in the d’où display, with its local upper curve',
'L042':'on … alors / H donc before the final rows',
'L043':'reduced a / independent point in on a alors',
'L044':'first lower inclusion, prior cap and complete relation candidates',
'L045':'cancelled nonempty sign pair after the first lower right Sigma',
'L046':'first i.e. label with its two points',
'L047':'second explanatory label, candidate order and both possible points',
'L048':'def/déf label, raised mark and equals',
'L049':'first final intersection and separate low-left slash',
'L050':'last non-equality sign and its detached endpoint candidate',
'L051':'archive 25 and its hand attribution',
}
sigma_labels={1:'opening family',2:'hemispheres before sont fermés',3:'first inserted Sigma',4:'second inserted Sigma',5:'third inserted Sigma',6:'cancelled group after connexes',7:'following si les Sigma',8:'Sigma in deleted les … connexes',9:'main barred conclusion',10:'first parenthetical barred term',11:'right barred term in parenthetical equality',12:'unbarred term after setminus',13:'et Sigma ne peut',14:'last car Sigma',15:'minus Sigma in margin legend',16:'plus Sigma in margin legend',17:'first pair plus',18:'first pair minus',19:'second pair plus',20:'second pair minus',21:'Sigma1+ before dans l’une',22:'Sigma2+ before dans l’autre',23:'first disjointness left Sigma',24:'first disjointness right Sigma',25:'first lower inclusion left Sigma',26:'first lower inclusion right Sigma',27:'first equality left factor',28:'first equality right factor',29:'first equality right-hand Sigma',30:'second inclusion left Sigma',31:'second inclusion right Sigma',32:'second equality left factor',33:'second equality right factor',34:'second equality right-hand Sigma',35:'Sigma12 before definition',36:'first final intersection left Sigma',37:'first final intersection right Sigma',38:'last intersection left Sigma',39:'last intersection right Sigma'}
for n,location in sigma_labels.items():labels['S%02d'%n]='Sigma occurrence %02d: %s'%(n,location)
rows={id:{'locus_id':id,'location':loc,'status':'pending root ink adjudication','reader_sources':{w:{'source_group_records':[],'difference_records':[],'doubt_records':[],'inventory_records':[],'other_state_records':[],'local_source_spans':[],'declared_crop_records':[]} for w in 'ABC'},'original_C_source_rows':[],'H_source_marker_records':[],'witness_source_spans':[],'source_observations':[]} for id,loc in labels.items()}


def ids(value):return value if isinstance(value,list) else [value]
def attach(loci,who,key,value):
 for loc in ids(loci):
  assert loc in rows,loc
  arr=rows[loc]['reader_sources'][who][key]
  if value not in arr:arr.append(value)
def sigma_locus(who,n):return 'S%02d'%(n+2 if who=='B' and n>=15 else n)


extra_group_maps={
'A':{'G01':'L006','G02':'L007','G03':'L008','G04':'L010','G05':'L011','G06':'L012','M01':'L013','G07':'L014','D01':'L015','M02':'L020','G08':'L029','G09':'L030','M03':'L035','G10':'L036','G11':'L038','E02':'L040','E03':'L041','G12':'L043','G13':'L044','G14':'L045','G15':'L048','M04':'L049'},
'B':{'EFAM':'L003','HSTART':'L006','GDE':'L007','GEQ':'L008','REL1':'L010','GCONN':'L011','GAUSS':'L012','GMAIN':'L013','M03':'L013','DIAG':'L015','GROOF10':'L020','M02':'L020','GPEUT':'L022','M04':'L022','ATWO':'L024','GPAIRS':'L029','DELIM2':'L030','GQDESC':'L033','GADJ':'L034','GDIST':'L036','CAP1':'L038','E1':'L040','E2':'L041','ARED':'L043','INCL1':'L044','GNEDEL':'L045','DEF':'L048','CAPFINAL':'L049','M06':'L049','NEFINAL':'L050'},
'C':{'G01':'L006','G02':'L007','G03':'L008','G04':'L010','G05':'L011','E01':'L017','G06':'L015','G07':'L034','G08':'L029','G09a':'L037','G09':'L036','G10':'L044','G11':'L045','G12':'L048','M02':'L027','M04':'L049'}}
group_keys={'A':'local_groups','B':'source_groups','C':'groups'}
group_locus={};group_record={};group_span={}
for who in 'ABC':
 for i,g in enumerate(parsed[who+'.map'][group_keys[who]]):
  id=g['id'];suffix=id.split('-',1)[1]
  loc=sigma_locus(who,int(suffix[1:])) if re.fullmatch(r'S\d+',suffix) else extra_group_maps[who][suffix]
  group_locus[id]=loc;record=pool_record(who+'.map','/'+group_keys[who]+'/'+str(i));group_record[id]=record
  attach(loc,who,'source_group_records',record)
  if who=='A':a,b=g['source_char_start'],g['source_char_end_exclusive'];literal=g['source_excerpt']
  elif who=='B':a,b=g['start_char'],g['end_char'];literal=g['literal_source']
  else:a,b=g['source_span']['start_character'],g['source_span']['end_character_exclusive'];literal=g['source_exact']
  assert parsed[who+'.tex'][a:b]==literal
  group_span[id]=span(who+'.tex',a,b,False)
  attach(loc,who,'local_source_spans',group_span[id])

# A has typeset diagram Sigma labels; B draws both labels with literal paths.
# Neither has individually named source groups for these two physical positions.
for who,gid in [('A','A026-D01')]:
 bounds=(group_span[gid]['start_char'],group_span[gid]['end_char_exclusive'])
 for n,needle in [(15,r'\Sigma^{-}'),(16,r'\Sigma^{+}')]:
  t=parsed[who+'.tex'];matches=[m.start()+bounds[0] for m in re.finditer(re.escape(needle),t[bounds[0]:bounds[1]])]
  assert len(matches)==1,(who,needle,matches)
  attach('S%02d'%n,who,'local_source_spans',span(who+'.tex',matches[0],matches[0]+len(needle)))
  attach('S%02d'%n,who,'other_state_records',group_record[gid])
bgid='B026-DIAG';bbounds=(group_span[bgid]['start_char'],group_span[bgid]['end_char_exclusive'])
for n,literal in [(15,r'''\draw[line width=.4pt](-55,23)--(-28,23);
\draw[line width=.4pt](-53,27)--(-35,30)--(-41,37)--(-63,48)--(-35,46);
\draw[line width=.4pt](-25,26)--(-14,27);'''),(16,r'''\draw[line width=.4pt](148,20)--(177,19);
\draw[line width=.45pt](149,24)--(166,27)--(159,34)--(142,47)--(174,46);
\draw[line width=.5pt](188,20)--(188,33);\draw[line width=.5pt](180,26)--(195,26);''')]:
 attach('S%02d'%n,'B','local_source_spans',exact('B.tex',literal,within=bbounds))
 attach('S%02d'%n,'B','other_state_records',group_record[bgid])


c_row_loci={1:'L003',2:['S04','S05','S07'],3:'S06',4:'L012',5:'L016',6:'L017',7:'S14',8:'L031',9:'L034',10:'L045',11:'L047',12:'L010',13:'L030',14:'L044',15:['S05','S08','S09','S10','S11','S12','S13','S14']}
a_specific={'L01':'L001','L02':'L002','L03':'S01','H01':'L005','L04':'L006','L05':'S03','L06':'L009','H06':'L011','H07':'L021','H08':'L015','L07':'L028','L08':'L036','L09':['L042','L043'],'L10':'L038','L11':'L039','L12':'L048','L13':'L032'}
b_specific={'L01':'L001','L02':'L002','L03':'S01','L04':'L005','L05':'L006','L06':'S03','L07':'L009','L08':'L011','L09':'L021','L10':'L024','L11':'L028','L12':'L032','L13':'L036','L14':'L042','L15':'L043','L16':'L048','HDIA':'L015','OM-M01':'L019','OM-M02':'L020','OM-M03':'L013','OM-M04':'L022','OM-M05':'L035','OM-M06':'L049'}
c_specific={'D01':'L001','D02':'S01','D03':'L003','D04':'L002','D05':'L005','D06':'L006','D07':'L007','D08':['L008','S03','S04','S05'],'D09a':'S04','D09b':'S05','D09c':'S05','D10':'S06','D11':'L009','D12':'S07','D13':'L010','D14':'L011','D15':'L012','D16':'L015','D17':'L016','D18':'L017','D19':'L019','D20':'L021','D21':['L021','L023'],'D22':'L024','D23':'L021','D24':'L021','D25':'L025','D26':'S14','D27':'L026','D28':'L027','D29':'L028','D30':'L030','D31':'L031','D32':'L032','D33':'L034','D34':'L035','D35':'L036','D36':'L037','D37':'L042','D38':'L044','D39':'L045','D40':'L047','D41':'L048','D42':'L049','D43':c_row_loci[15],'D44':'L017'}
diff_loci={};diff_record={}
for who in 'ABC':
 for i,d in enumerate(parsed[who+'.report']['differences']):
  id=d['id']
  if who=='A':
   if id.startswith('C026-R'):loc=c_row_loci[int(id[-2:])]
   else:
    suffix=id.split('-',1)[1]
    if suffix.endswith('-geometry'):loc=group_locus['A026-'+suffix[:-9]]
    elif suffix.endswith('-head'):loc=group_locus['A026-'+suffix[:-5]]
    else:loc=a_specific[suffix]
  elif who=='B':
   suffix=id.split('-',1)[1]
   if re.fullmatch(r'R\d\d',suffix):loc=c_row_loci[int(suffix[1:])]
   elif suffix.endswith('-HEAD'):loc=group_locus['B026-'+suffix[:-5]]
   elif suffix.startswith('G-'):loc=group_locus['B026-'+suffix[2:]]
   else:loc=b_specific[suffix]
  else:loc=group_locus['C026-'+id[2:]] if id.startswith('G-S') else c_specific[id]
  diff_loci[(who,id)]=ids(loc);record=pool_record(who+'.report','/differences/'+str(i));diff_record[(who,id)]=record
  attach(loc,who,'difference_records',record)


# Every remaining reader doubt gets its own raw record and existing local scope.
for who in 'ABC':
 for i,d in enumerate(parsed[who+'.report']['doubts']):
  if who in ('A','C'):loc=diff_loci[(who,d['id'])]
  elif 'graphic_id' in d:loc=group_locus[d['graphic_id']]
  else:
   part=d['local_part']
   if part.startswith('R02'):loc={'R02a':'S04','R02b':'S05','R02c':'S05','R02d':'S07'}[part]
   elif part.startswith('R15'):loc=c_row_loci[15][int(part[-1])-1]
   else:loc=c_row_loci[int(d['source_row'][-2:])]
  attach(loc,who,'doubt_records',pool_record(who+'.report','/doubts/'+str(i)))


# B exposes separate complete-candidate records and four local component records.
for i,c in enumerate(parsed['B.report']['candidate_records']):
 attach(group_locus[c['graphic_id']],'B','other_state_records',pool_record('B.report','/candidate_records/'+str(i)))
special={'B026-M01':'L019','B026-M05':'L035','B026-CAP1-point':'L038','B026-NEFINAL-point':'L050'}
for i,c in enumerate(parsed['B.report']['special_component_candidates']):
 attach(special[c['id']],'B','other_state_records',pool_record('B.report','/special_component_candidates/'+str(i)))


# Original C parents retain exact row order; a/b/c labels are never equated by
# ordinal across readers. The four root-catalogue parts get explicit mappings.
original_rows=[]
row_keys={'A':'C_doubt_source_rows','B':'C_uncertainty_source_rows','C':'C_uncertainty_rows'}
for n,canon in enumerate(parsed['C.doubts']['canonical_doubt_rows'],1):
 record=pool_record('C.doubts','/canonical_doubt_rows/'+str(n-1));locs=ids(c_row_loci[n])
 item={'source_row_id':canon['source_id'],'canonical_record':record,'loci':locs,'reader_parent_records':{}}
 for loc in locs:rows[loc]['original_C_source_rows'].append(canon['source_id'])
 for who in 'ABC':
  ptr='/'+row_keys[who]+'/'+str(n-1);rid=pool_record(who+'.report',ptr);item['reader_parent_records'][who]=rid
  attach(locs,who,'other_state_records',rid)
 original_rows.append(item)
parts=[
 {'canonical_part':'C026-R02-1','locus':'S04','A_part_index':0,'B_part_index':0,'C_part_index':0,'C_difference':'D09a'},
 {'canonical_part':'C026-R02-2','locus':'S05','A_part_index':2,'B_part_index':2,'C_part_index':1,'C_difference':'D09b'},
 {'canonical_part':'C026-R02-3','locus':'S05','A_part_index':1,'B_part_index':1,'C_part_index':2,'C_difference':'D09c'},
 {'canonical_part':'C026-R02-4','locus':'S07','A_part_index':3,'B_part_index':3,'C_part_index':3,'C_difference':'D12'}]
for p in parts:
 p['raw_reader_part_records']={w:pool_record(w+'.report','/'+row_keys[w]+'/1/local_parts/'+str(p[w+'_part_index'])) for w in 'ABC'}
 for w,rid in p['raw_reader_part_records'].items():attach(p['locus'],w,'other_state_records',rid)
original_rows[1]['four_local_part_correspondences']=parts
ring_parts=[]
for i,loc in enumerate(c_row_loci[15]):
 rr={'locus':loc,'reader_local_records':{}}
 for w,ptr in [('A','/C_doubt_source_rows/14/local_recurrences/'),('B','/C_uncertainty_source_rows/14/local_parts/'),('C','/recurring_ring_occurrences/')]:
  rid=pool_record(w+'.report',ptr+str(i));rr['reader_local_records'][w]=rid;attach(loc,w,'other_state_records',rid)
 ring_parts.append(rr)
original_rows[14]['eight_local_recurrences']=ring_parts


# Every inventory record remains available. Broad unchanged text regions are
# explicitly identified as context; local hand scopes never migrate to them.
inventory_context=[]
inventory_special={
'A':{'A026-I01':'L001','A026-I02':'L005','A026-I03':'L007','A026-I04':'L008','A026-I05':'S04','A026-I06':'S05','A026-I07':'S05','A026-I08':'S06','A026-I09':'S07','A026-I10':'L011','A026-I11':'L011','A026-I12':'L011','A026-I13':'L012','A026-I14':'L015','A026-I15':'L015','A026-I16':'L016','A026-I17':'L028','A026-I18':'L031','A026-I19':'L032','A026-I20':'L036','A026-I21':'L038','A026-I22':'L042','A026-I23':'L044','A026-I24':'L044','A026-I25':'L045','A026-I26':'L051'},
'B':{'B026-T01':'L001','B026-U01':'L001','B026-F01':'L004','B026-DEL01':'L005','B026-T02':'L005','B026-T03':'L006','B026-DEL02':'S04','B026-DEL03':'S05','B026-DEL04':'S05','B026-DEL05':'S06','B026-DEL06':'S07','B026-DEL07':'L011','B026-DEL08':'L011','B026-INS01':'L011','B026-T04':'L021','B026-T05':'L028','B026-DEL09':'L031','B026-INS02':'L032','B026-INS03':'L036','B026-U02':'L036','B026-F02':'L038','B026-F03':'L044','B026-T06':'L042','B026-F04':'L047','B026-F05':'L048','B026-ARCHIVE':'L051'},
'C':{'T01':'L001','U01':'L001','F01':'L004','T02':'L005','DEL01':'L005','T03':'L005','DEL02':'S04','DEL03':'S05','DEL04':'S05','T04':'L008','T05':'S07','DEL09':'L012','T06':'L012','F03':'S09','T07':'L021','T08':'L028','T09':'L034','T10':'L036','F05':'L038','T11':'L042','F06':'L044','ARCHIVE':'L051'}}
for who in 'ABC':
 for i,v in enumerate(parsed[who+'.report']['inventory']):
  rid=pool_record(who+'.report','/inventory/'+str(i));g=v.get('source_group');el=v.get('element')
  if g in group_locus:loc=group_locus[g]
  elif el in group_locus:loc=group_locus[el]
  elif el in inventory_special[who]:loc=inventory_special[who][el]
  else:
   inventory_context.append({'reader':who,'record':rid,'element':el});continue
  attach(loc,who,'inventory_records',rid)
  if not g and el not in group_locus:inventory_context.append({'reader':who,'record':rid,'element':el,'attached_locus':loc,'scope':'raw inventory element may span neighbouring loci; its own full position and hand fields retain their original scope'})


# Exact existing crop metadata, with declared source references only. There is
# no geometric assertion about ink coverage and no selected root crop.
crop_records={}
for who in 'ABC':
 for i,c in enumerate(parsed[who+'.crops']):
  rid=pool_record(who+'.crops','/'+str(i));path=c['path'];crop_records[(who,path)]=rid
  stem=Path(path).stem;crop_records[(who,stem)]=rid
  if 'id' in c:crop_records[(who,c['id'])]=rid
def crop_for(who,value):
 if value is None:return None
 return crop_records.get((who,value))
for who in 'ABC':
 for i,g in enumerate(parsed[who+'.map'][group_keys[who]]):
  view=g.get('crop',g.get('evidence_view'));cr=crop_for(who,view)
  if cr:attach(group_locus[g['id']],who,'declared_crop_records',cr)
 for d in parsed[who+'.report']['differences']:
  cr=crop_for(who,d.get('readers_crop'))
  if cr:attach(diff_loci[(who,d['id'])],who,'declared_crop_records',cr)


# H markers remain tied to their literal local scopes; a drawing parent or note
# never transfers an ill/uncertain marker to every child.
h_bind={
'H026-U01':['L005'],'H026-U02':['L005'],'H026-U03':['L005'],'H026-U04':['L008'],'H026-U05':['S06'],'H026-U06':['L009'],'H026-U07':['L011'],'H026-U08':['L021'],'H026-U09':['L025'],'H026-U10':['L025'],'H026-U11':['L025'],'H026-U12':['L016'],
'H026-N01':['L003'],'H026-N02':['L008','S03','S04','S05'],'H026-N03':['L025'],'H026-N04':['L015','S15','S16','L017'],'H026-N05':['L045'],
'H026-D01':['L015','L016','S15','S16','L017'],'H026-D02':['L015','L016','S15','S16','L017']}
hmarker_index=[]
for section in ['uncertainty_macros','editorial_supplies','notes','marginal_drawing_source_descriptions']:
 for i,m in enumerate(parsed['H.markers'][section]):
  rid=pool_record('H.markers','/'+section+'/'+str(i));locs=h_bind[m['source_id']]
  for loc in locs:rows[loc]['H_source_marker_records'].append(rid)
  hmarker_index.append({'source_id':m['source_id'],'raw_record':rid,'loci':locs,'scope':'literal source marker span; final local marked_in_H remains a root source-audit decision'})


# All witness Sigma occurrences, including explicitly repeated H apparatus
# occurrences, are mapped by their literal source positions.
def atom_end(t,i):
 if t[i]=='{':
  depth=1;j=i+1
  while depth:
   if t[j]=='\\':j+=2;continue
   if t[j]=='{':depth+=1
   elif t[j]=='}':depth-=1
   j+=1
  return j
 if t[i]=='\\':return re.match(r'\\(?:[A-Za-z]+|.)',t[i:]).end()+i
 return i+1
def sigma_end(t,a):
 b=a+len(r'\Sigma')
 while b<len(t) and t[b] in '_^':b=atom_end(t,b+1)
 return b
c_map=list(range(1,10))+['L016',15,16]+list(range(10,15))+list(range(17,40))
h_map=[1,2,7,8,9,10,11,12,13,3,4,5,14,15,16,15,16,15,16]+list(range(17,40))+[25,26]
for key,mapping in [('witness.C',c_map),('witness.H',h_map)]:
 t=parsed[key];hits=list(re.finditer(r'\\Sigma(?![A-Za-z])',t));assert len(hits)==len(mapping),(key,len(hits),len(mapping))
 for ordinal,(m,loc) in enumerate(zip(hits,mapping),1):
  loc='S%02d'%loc if isinstance(loc,int) else loc;a=m.start();b=sigma_end(t,a)
  # Include an immediately surrounding outer closure macro in the local span.
  prefix=r'\overline{'
  if t[max(0,a-len(prefix)):a]==prefix and t[b:b+1]=='}':a-=len(prefix);b+=1
  z=span(key,a,b);z['witness_occurrence_ordinal']=ordinal
  rows[loc]['witness_source_spans'].append(z)


# Exact small prose/ordinary-source spans make report-silent selections visible.
snippets={
'L001':{'A':r'\uline{\unsure{décomposition|dècomposition|decomposition|disposition} binaire}','B':r'\uline{décomposition binaire}','C':r'\uline{\unsure{décomposition|dècomposition|decomposition|disposition} binaire}'},
'L002':{w:'est un ens de deux parties' for w in 'ABC'},
'L003':{'A':r'\unsure{\mathcal E|\mathscr E|\varepsilon}','C':r'\unsure{\mathcal E|\mathscr E|\varepsilon}'},
'L004':{'A':"(les ``hémisphères'')",'B':"(\\text{les ``hémisphères''})",'C':"(\\text{les ``hémisphères})"},
'L005':{'A':"on s'intéresse au cas où les",'B':"on s'intéresse au cas où les",'C':r"on \unsure{s'intéresse|s'intèresse|s'interesse} au cas où les"},
'L009':{w:'et où' for w in 'ABC'},
'L012':{'C':r'\deleted{\unsure{aussitôt|aussitot}}'},
'L014':{'B':r'\cap E\ne\varnothing','C':r'\cap E\ne\varnothing'},
'L021':{'A':'ne peut être à la fois ouvert et fermé','B':' la fois ouvert et fermé car ','C':r'ne peut \unsure{être|etre} \unsure{à|:} la fois ouvert et fermé'},
'L022':{'A':'ne peut être à la fois','C':r'ne peut \unsure{être|etre}'},
'L023':{'A':'être à la fois','B':' être ','C':r'\unsure{être|etre}'},
'L024':{'A':'à la fois','C':r'\unsure{à|:}'},
'L025':{'A':r'est un ouvert $\ne\varnothing$ et $\ne X$)','B':r'est un ouvert $\ne\varnothing$ et $\ne X$)','C':r'\text{un}}$ ouvert $\ne\varnothing$ et $\ne X$)'},
'L026':{'B':'$, est un ouvert','C':'$, est $'},
'L027':{'A':'est un ouvert','B':'est un ouvert'},
'L028':{w:'Considérons deux décompositions binaires' for w in 'ABC'},
'L033':{'A':"on dit qu'elles sont",'C':"on dit qu'elles sont"},
'L034':{'A':r'\uline{non \unsure{panachées|penchées|parallèles}}'},
'L039':{'A':r"\unsure{d'où|d'ou}",'B':r"\text{d'où }",'C':r'\text{d’où }'},
'L040':{'C':r'E_1\cap E_2=\varnothing'},
'L041':{'C':r'E_1\cap E_2=\varnothing'},
'L042':{'C':'on a alors'},
'L043':{'C':'on a alors'},
'L046':{w:r'\text{i.e.}' for w in 'ABC'},
'L047':{'A':r'\unsure{i.e.|i.e|ie}','B':r'\unsure{ie|i.e.|i.e}','C':r'\unsure{i.e|i.e.|ie}'},
'L050':{'A':r'\ne\varnothing'+'\n'+r'\end{aligned}','C':r'\ne\varnothing'+'\n'+r'\end{aligned}'},
'L051':{w:'% archive sheet number: 25' for w in 'ABC'}}
for loc,by_reader in snippets.items():
 for who,literal in by_reader.items():attach(loc,who,'local_source_spans',exact(who+'.tex',literal))


# Local source spans inside group wrappers, without repeating the whole group.
def child_snippet(loc,who,gid,literal):
 g=group_span[gid];attach(loc,who,'local_source_spans',exact(who+'.tex',literal,within=(g['start_char'],g['end_char_exclusive'])))
for who,gid in [('A','A026-G10'),('B','B026-GDIST')]:
 child_snippet('L037',who,gid,'on peut trouver')
for who,gid in [('A','A026-D01'),('B','B026-DIAG'),('C','C026-G06')]:
 for loc in ['L016','L017','L018','L019']:attach(loc,who,'other_state_records',group_record[gid])
for who,gid in [('A','A026-G08'),('B','B026-GPAIRS'),('C','C026-G08')]:
 for loc in ['L030','L031','L032']:attach(loc,who,'other_state_records',group_record[gid])
for who,gid in [('B','B026-GADJ'),('C','C026-G07')]:attach('L035',who,'other_state_records',group_record[gid])
for who,gid in [('A','A026-S09'),('B','B026-S09'),('C','C026-S09')]:attach('L013',who,'other_state_records',group_record[gid])
for who,gid in [('A','A026-S10'),('B','B026-S10'),('C','C026-S10')]:attach('L020',who,'other_state_records',group_record[gid])
for who,gid in [('A','A026-S14'),('B','B026-S14'),('C','C026-S14')]:attach('L026',who,'other_state_records',group_record[gid])
for who,left,right in [('A','A026-S23','A026-S24'),('B','B026-S21','B026-S22'),('C','C026-S23','C026-S24')]:
 a=group_span[left]['end_char_exclusive'];b=group_span[right]['start_char'];attach('L038',who,'local_source_spans',span(who+'.tex',a,b,who=='C'))


observations={
'L004':['Final C source has opening paired backticks before hémisphères and no closing paired apostrophes in the cited span. A and B have both pairs. C reading.md describes the quoted naming line; that prose and the actual source remain separately retained.'],
'L006':['A retains live whole word, deleted initial h with live continuation, and deleted whole word. B retains live whole word and deleted whole word. C retains live whole word and deleted initial h with live continuation. Each complete raw candidate set remains its own reader record.'],
'L008':['A/C group ownership leaves following et où outside the complete guide group; B GEQ owns it. All nested Sigma sources, live connexes and the post-connexes cancellation retain exact boundaries.'],
'L011':['A and C leave preceding si outside their correction group; B GCONN owns si. A/B put the following baseline comma outside the group; C draws that comma in a node inside G05. The raised replacement comma and crossed et retain their separate source positions.'],
'L013':['A records a faint curve with its left approach meeting crop09’s boundary. B records a pale arc plus its own later crop17, and GMAIN places the arc beside S09 once. C S09 has head/body/roof paths and no separately named arc group in its complete source. These are source records and declared viewing limits, not adjudicated ink.'],
'L014':['A supplies a literal E with upper-arm/independent-return states. B and C use the cited ordinary E token at this location.'],
'L015':['A raw diagram inventory parent says his hand; every A diagram complete candidate gives the separate point undetermined hand. Both scopes are retained. B/C likewise keep point-local attribution through their own component/candidate records.'],
'L017':['A/B retain low alpha versus lower-right return/flourish. C selects low alpha in the original R06 and separately qualifies its upper arm. C’s independently qualified upper arm never reopens its original low-index status by inheritance.'],
'L018':['A draws a separate lower run and keeps superset/supseteq candidates in its complete diagram states. B/C retain their own connector/lower-label encodings. The exact source paths and relation tokens remain in the diagram records.'],
'L020':['A nests M02 inside S10. B uses GROOF10 with S10 and M02 at declared separate placements; its three attachment candidates remain local. C S10 draws a roof but has no separately named counterpart to that short trace in its complete source.'],
'L021':['A H07 and B L09 provide broad parenthetical comparison scopes; C submits several smaller D20/D21/D23/D24/D25/D27 scopes. These original report boundaries and raw flags are not collapsed into one common reader state.'],
'L022':['B GPEUT owns peut and places M04 below it. A has ordinary peut; C has ordinary peut with the independently qualified following être. C’s prose-crop descender limitation remains its own declared audit fact.'],
'L027':['C M02 is below un in the final car clause. B M04 is below peut on another line. They remain distinct loci despite their similar reported fleck vocabulary.'],
'L033':['B GQDESC owns the complete qu’elles word and literal q descender. A/C use the cited ordinary word text.'],
'L034':['B’s exact prefix/suffix map retains six complete word candidates including three unaccented candidates; A/C retain their own three-word sets. The p/underline and any lower points keep each source’s exact ownership.'],
'L035':['A M03 owns the two points alone, with adjective and underline excluded. B and C place the point components inside their full adjective group, with independent local hand and role scopes.'],
'L036':['A owns inserted clause and on peut trouver but leaves initial si outside; B includes initial si and the following first Sigma in GDIST; C includes initial si, qualified on and peut trouver but leaves the following Sigma outside. No enclosing ownership scope is transferred between readers.'],
'L037':['C G09a gives complete on and three-trace alternatives with distinct hand scopes. A/B firm on occurs within their cited complete guide groups.'],
'L038':['A keeps cap/wedge-plus-point complete states. B keeps cap with terminal-point/independent-point states. C uses the ordinary cap token between its two mapped Sigma groups.'],
'L039':['A qualifies d\'où/d\'ou; B prints d\'où with U+0027 apostrophe; C prints d’où with U+2019. The exact characters and qualifier scopes are retained. No equivalence is presumed by this source catalogue.'],
'L043':['A/B preserve a reduced a/independent-point alternative locally. C prints ordinary on a alors and contributes no separate graphical a group.'],
'L044':['A primary is deleted cap then subset; B primary is subset; C primary is deleted cap then subset and additionally retains membership. Full old/live states remain reader-specific.'],
'L047':['A primary i.e.; B primary ie; C primary i.e. All three retain their own ordered complete alternative arrays, including terminal-point scope.'],
'L048':['A uses an accent/no-accent text label while its own candidate states mention an independent high tick. B draws the label and upper trace; C draws def, a point and equals. Candidate-specific hand/role fields and exact source forms are kept together without adding a missing component to A.'],
'L049':['A owns a faint trace alone before an ordinary cap. B CAPFINAL owns the cap plus M06, with detached-continuation/independent-slant alternatives. C puts M04 under the cap through its own literal underset source.'],
'L050':['B NEFINAL retains both endpoint and independent-point candidates, with point-specific attribution in special_component_candidates. A/C retain the ordinary final non-equality tokens in the cited spans.']}
for loc,notes in observations.items():rows[loc]['source_observations'].extend(notes)
for loc in ['S09','S10','S11']:
 rows[loc]['source_observations'].append('C’s exact source draws the long outer roof as a separate path, while its ownership/candidate strings and phantom annotation name unbarred Sigma. Both source facts remain explicit; the catalogue does not drop the roof or rewrite the candidate wording.')
for loc in ['S25','S33']:
 rows[loc]['source_observations'].append('A and B state shared body-foot/lower-1 ownership in their own sources. C’s exact source contains its body-foot path and a separate printed 1 node; S25 also has an explicit short downward foot segment. All literal components are retained for root inspection; no duplicate-ink conclusion is drawn.')
for loc in ['S15','S16']:
 rows[loc]['source_observations'].append('A/B use the exact ordinary Sigma label token within their complete diagram source; C has a separate literal group with its own detached-head states. Catalogue Sigma ordinals 15/16 do not fabricate A/B local group ids.')


# Preserve exact notes of stated crop-boundary limits and relevant placement
# fields as raw provenance; no image is reopened to confirm or alter them.
view_limits=[]
for who in 'ABC':
 for key,value in parsed[who+'.report'].get('provenance',{}).items():
  if any(s in str(value).lower() for s in ['clip','boundar','origin','placement']):
   view_limits.append({'reader':who,'record':pool_record(who+'.report','/provenance/'+esc(key))})


# Coverage: every submitted difference, doubt and named graphic has a local map.
coverage={'source_only':True,'reader_counts':{},'unmapped_difference_records':[],'unmapped_doubt_records':[],'unmapped_group_records':[]}
for who in 'ABC':
 coverage['reader_counts'][who]={'differences':len(parsed[who+'.report']['differences']),'doubts':len(parsed[who+'.report']['doubts']),'groups':len(parsed[who+'.map'][group_keys[who]]),'inventory':len(parsed[who+'.report']['inventory'])}
 for section,field in [('differences','difference_records'),('doubts','doubt_records')]:
  included={rid for row in rows.values() for rid in row['reader_sources'][who][field]}
  for i,_ in enumerate(parsed[who+'.report'][section]):
   rid=pool_ids[(who+'.report','/'+section+'/'+str(i))]
   if rid not in included:coverage['unmapped_'+('difference' if section=='differences' else 'doubt')+'_records'].append(rid)
 included={rid for row in rows.values() for rid in row['reader_sources'][who]['source_group_records']}
 for g in parsed[who+'.map'][group_keys[who]]:
  if group_record[g['id']] not in included:coverage['unmapped_group_records'].append(group_record[g['id']])
assert not any(coverage[k] for k in ['unmapped_difference_records','unmapped_doubt_records','unmapped_group_records'])
coverage['original_C_parent_rows']=len(original_rows);coverage['R02_parts']=len(parts);coverage['R15_recurrences']=len(ring_parts)
coverage['Sigma_loci']=len([x for x in rows if x.startswith('S')]);coverage['other_loci']=len([x for x in rows if x.startswith('L')])
assert coverage['original_C_parent_rows']==15 and coverage['R02_parts']==4 and coverage['R15_recurrences']==8 and coverage['Sigma_loci']==39


def compact_json(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def write_json(name,value):
 b=(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode();(OUT/name).write_bytes(b);return {'path':'out/checks/'+name,'bytes':len(b),'sha256':sha(b)}


# Page order uses the catalogue's explicit physical-location labels. The margin
# diagram remains a complete parent with independently indexed local labels.
order=['L001','L002','S01','L003','L004','L005','L006','S02','L007','L008','S03','S04','S05','S06','L009','S07','L010','L011','S08','L012','L013','S09','L014','L015','L016','L017','L018','L019','S15','S16','S10','L020','S11','S12','L021','S13','L022','L023','L024','L025','S14','L026','L027','L028','L029','S17','S18','L030','S19','S20','L031','L032','L033','L034','L035','L036','L037','S21','S22','S23','L038','S24','L039','L040','L041','L042','L043','S25','L044','S26','L045','L046','S27','S28','S29','S30','S31','L047','S32','S33','S34','S35','L048','S36','L049','S37','S38','S39','L050','L051']
assert set(order)==set(rows) and len(order)==len(rows)
ordered=[rows[id] for id in order]
artifacts=[]
artifacts.append(write_json('scan026_source_union_sources_v01.json',sources))
artifacts.append(write_json('scan026_source_union_state_pool_v01.json',pool))
artifacts.append(write_json('scan026_source_union_v01.json',ordered))
artifacts.append(write_json('scan026_source_union_C_rows_v01.json',original_rows))
artifacts.append(write_json('scan026_source_union_H_marker_bindings_v01.json',hmarker_index))
artifacts.append(write_json('scan026_source_union_inventory_context_v01.json',inventory_context))
artifacts.append(write_json('scan026_source_union_view_limits_v01.json',view_limits))

# Bounded complete JSONL chunks are exactly invertible: parse each line in order.
chunks=[];current=[];size=0
for row in ordered:
 line=json.dumps(row,ensure_ascii=False)+'\n';length=len(line.encode())
 if current and size+length>12500:chunks.append(current);current=[];size=0
 current.append(line);size+=length
if current:chunks.append(current)
reviews=[];restored=[]
for i,chunk in enumerate(chunks,1):
 name='scan026_pending_union_review_v01_%02d.jsonl'%i;b=''.join(chunk).encode();(OUT/name).write_bytes(b)
 restored.extend(json.loads(line) for line in chunk)
 reviews.append({'path':'out/checks/'+name,'rows':len(chunk),'bytes':len(b),'sha256':sha(b)})
assert compact_json(restored)==compact_json(ordered)

# Rebuild every pooled raw object from its finite exact field mapping.
for item in pool:
 original=resolve(item['raw_ref']['source'],item['raw_ref']['json_pointer'])
 if 'ordered_fields' in item:
  recovered=OrderedDict((f['key'],copy.deepcopy(f['value']) if 'value' in f else copy.deepcopy(resolve(f['exact_value_ref']['source'],f['exact_value_ref']['json_pointer']))) for f in item['ordered_fields'])
 else:recovered=item['value']
 assert compact_json(recovered)==compact_json(original)
coverage.update({'all_pool_records_replayed_in_exact_key_order':True,'state_pool_records':len(pool),'numbered_review_chunks_reconstruct_exact_union_values_and_key_order':True,'reader_and_packet_sources_unchanged':all((BASE/v['path']).read_bytes()==raw[k] for k,v in sources.items()),'images_opened':0,'root_crop_choices':0,'root_ink_choices':0,'root_review_claimed':False,'review_files':reviews,'artifacts':artifacts})
write_json('scan026_source_union_replay_v01.json',coverage)
readme='''# Scan 026: source-only locus union

This catalogue preserves the three frozen readers and the supplied witnesses. Every locus remains pending the root's ink adjudication. It makes no reading choice and selects no root crop.

`scan026_source_union_v01.json` is the complete 90-locus index: 39 individually mapped Sigma positions and 51 other local scopes. The bounded `scan026_pending_union_review_v01_*.jsonl` files contain the same complete values and field order. Their parse-and-concatenate inverse has been checked exactly.

Each R-number points to `scan026_source_union_state_pool_v01.json`. A pooled object preserves all raw fields in order. Long original witness paragraphs and literal TeX bodies use exact frozen JSON pointers; complete candidate, role, attachment, hand and cancellation/insertion states are kept as that reader supplied them. The source registry supplies exact file paths and SHA-256 hashes. Every pooled record was reconstructed in exact original key order. These references require the frozen raw files; no claim is made about reconstructing unrelated file formatting from a displayed excerpt.

The original C table remains 15 parents. `scan026_source_union_C_rows_v01.json` explicitly maps the four R02 parts without confusing A/B upper-before-lower indexing with the original source order, and maps all eight R15 recurrences. H's 12 uncertainty/illegibility markers, five notes and two drawing descriptions keep their literal local scopes in `scan026_source_union_H_marker_bindings_v01.json`. Their final marked_in_H interpretation remains the root's source audit; raw reader flags have not been overwritten.

The index cites existing crop metadata with original boxes and transformations. Cited metadata is source evidence about the readers' work; the catalogue makes no fresh ink-coverage claim. All detached-mark roles and hands remain local, including a parent inventory attribution that differs in scope from a candidate's point attribution.

All 226 reader difference rows, all 189 remaining-doubt records and all 181 named source groups have mappings. The raw A–B, A–C and B–C unified TeX diffs and their complete numbered chunks remain in `scan026_source_AB_*`, `scan026_source_AC_*` and `scan026_source_BC_*`. No source is normalized or filtered in those diffs.
'''
(OUT/'scan026_source_union_readme_v01.md').write_text(readme)
print(json.dumps({k:coverage[k] for k in ['reader_counts','original_C_parent_rows','R02_parts','R15_recurrences','Sigma_loci','other_loci','state_pool_records','review_files']},ensure_ascii=False,indent=2))
