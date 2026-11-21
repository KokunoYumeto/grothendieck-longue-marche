from pathlib import Path
import json,re,hashlib
D=Path('out/readers/024/C');s=D.joinpath('reading.tex').read_text();meta=json.loads(D.joinpath('group_metadata.json').read_text())
def span(a,b):
 return {'character_start':a,'character_end_exclusive':b,'utf8_byte_start':len(s[:a].encode()),'utf8_byte_end_exclusive':len(s[:b].encode()),'line_start':s.count('\n',0,a)+1,'line_end':s.count('\n',0,b-1)+1,'exact_tex':s[a:b]}
markers=list(re.finditer(r'^% (BEGIN|END) (C024-[A-Z0-9]+)\n?',s,re.M));stack=[];groups=[]
for m in markers:
 if m[1]=='BEGIN':stack.append((m[2],m.start(),m.end(),stack[-1][0] if stack else None))
 else:
  ident,a,payload,parent=stack.pop();assert ident==m[2]
  g={'id':ident,**meta[ident],'parent_group':parent,'source_span':span(a,m.end()),'payload_span':span(payload,m.start())}
  groups.append(g)
assert not stack
groups.sort(key=lambda x:x['source_span']['character_start'])
# Exact environments and parent options establish units/baselines without pixel mappings.
envs=[];st=[]
for m in re.finditer(r'\\(begin|end)\{(tikzpicture)\}(?:\[([^\]]*)\])?',s):
 if m[1]=='begin':st.append((m.start(),m.group(),m[3],len(st)))
 else:
  a,beg,opts,depth=st.pop();envs.append({'id':f'env-{a}','options':opts,'nesting_depth':depth,'source_span':span(a,m.end())})
assert not st
envs.sort(key=lambda x:x['source_span']['character_start'])
def parent_env(a,b):
 es=[e for e in envs if e['source_span']['character_start']<=a and e['source_span']['character_end_exclusive']>=b]
 return min(es,key=lambda x:x['source_span']['character_end_exclusive']-x['source_span']['character_start'])['id'] if es else None
def command_end(a):
 depth=0;i=a
 while i<len(s):
  c=s[i]
  if c=='%' and (not i or s[i-1]!='\\'):
   q=s.find('\n',i);i=len(s) if q<0 else q;continue
  if c in '{}' and (not i or s[i-1]!='\\'):depth+=1 if c=='{' else -1
  if c==';' and depth==0:return i+1
  i+=1
 raise ValueError(('unterminated path/node',a))
commands=[]
for m in re.finditer(r'\\(draw|fill|path|node)\b',s):
 # Comments contain no active path commands in this source; reject any comment occurrence explicitly.
 line_start=s.rfind('\n',0,m.start())+1
 if '%' in s[line_start:m.start()]:continue
 b=command_end(m.start());containers=[g['id'] for g in groups if g['payload_span']['character_start']<=m.start()<g['payload_span']['character_end_exclusive']]
 commands.append({'id':f'{m[1]}-{m.start()}','command':m[1],'parent_environment':parent_env(m.start(),b),'groups':containers,'source_span':span(m.start(),b)})
wrappers=[]
for m in re.finditer(r'\\(unsure|deleted|inserted|uline|phantom|rlap|figure)\{',s):
 ls=s.rfind('\n',0,m.start())+1
 if '%' in s[ls:m.start()]:continue
 a=m.end()-1;depth=1;i=a+1
 while depth and i<len(s):
  if s[i]=='%' and s[i-1]!='\\':
   i=s.find('\n',i);continue
  if s[i] in '{}' and s[i-1]!='\\':depth+=1 if s[i]=='{' else -1
  i+=1
 assert depth==0
 wrappers.append({'id':f'{m[1]}-{m.start()}','macro':m[1],'source_span':span(m.start(),i),'invisible_annotation':m[1] in ['phantom'],'parent_environment':parent_env(m.start(),i)})
for g in groups:
 a=g['payload_span']['character_start'];b=g['payload_span']['character_end_exclusive']
 g['literal_commands']=[x['id'] for x in commands if a<=x['source_span']['character_start']<b]
 g['wrappers']=[x['id'] for x in wrappers if a<=x['source_span']['character_start']<b]
 g['environments']=[x['id'] for x in envs if a<=x['source_span']['character_start']<b]
 g['visible_word_ownership']='Only the stated owned words/marks occur visibly in this selected group; text inside phantom annotations is provenance and state annotation.'
# Exact plain text sections and original-doubt selectors.
plain=[]
anchors=[('opening',s.index(r'\unsure{Considerons|Considérons}'),s.index(r'\[')),('definition',s.index(r'\['),s.index(r'\]')+2),('lemma',s.index(r'\uline{Lemme} Cette relation'),s.index(r'\unsure{le|Le}')),('explanation',s.index(r'\unsure{le|Le}'),s.index(r'\unsure{Soient|Soit}')),('final_paragraph',s.index(r'\unsure{Soient|Soit}'),s.index('% archive sheet number: 23')),('archive_comment',s.index('% archive sheet number: 23'),len(s))]
for ident,a,b in anchors:plain.append({'id':ident,'source_span':span(a,b),'group_ids':[g['id'] for g in groups if a<=g['source_span']['character_start']<b]})
selectors={
'C024-R01':[r'\Pi_I^{\unsure{\circ|0}}'],
'C024-R02':[r"\bigcup_{\alpha'\in I}",r"E_{\alpha'}"],
'C024-R03':[r"l'ens des classes"],
'C024-R04':['C024-G02'], 'C024-R05':['C024-G04'], 'C024-R06':['C024-G05'], 'C024-R07':['C024-G06'],
'C024-R08':[r'\unsure{ens de|ens des}'], 'C024-R09':[r"d'\unsure{aretes|arêtes|arètes}.)"],
'C024-R10':['C024-G11'], 'C024-R11':[r'\unsure{Soient|Soit}'], 'C024-R12':[r'\unsure{exactemt|exactement}'],
'C024-R13':['C024-U01','C024-U02'],'C024-R14':['C024-S03'],'C024-R15':[r'\unsure{de|dé|qui}'],
'C024-R16':['C024-G08'],'C024-R17':[r'\unsure{le|Le}'],'C024-R18':[r'\unsure{connexes|conn}']}
sm=[]
for rid,sel in selectors.items():
 entries=[]
 for x in sel:
  if x in meta:
   g=next(g for g in groups if g['id']==x);entries.append({'selector':x,'group_id':x,'source_span':g['source_span']})
  else:
   a=s.index(x);entries.append({'selector':x,'source_span':span(a,a+len(x))})
 sm.append({'source_row_id':rid,'entries':entries})
out={'scan':24,'reader':'C','file':'reading.tex','sha256':hashlib.sha256(s.encode()).hexdigest(),'span_convention':'Zero-based character and UTF-8 byte offsets, half-open; line numbers one-based and inclusive. exact_tex is the literal file slice.','coordinate_convention':'Local source dimensions are declared pt units. Each fixed picture declares its bounding rectangle and baseline; nodes use base-west and zero inner/outer separation. No source-to-image metric conversion or curve-extrema computation is claimed. Native image boxes stay in report.json.','groups':groups,'plain_units':plain,'paths_and_nodes':commands,'wrappers':wrappers,'environments':envs,'original_doubt_source_spans':sm,'editorial_scope':'Pipes and phantom state annotations are editorial alternatives, never newly supplied manuscript separators. Complete alternatives and adjoining owned words remain with each group.'}
D.joinpath('source_map.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Source map:',len(groups),'groups,',len(commands),'literal paths/nodes,',len(wrappers),'wrappers,',len(envs),'picture environments')
