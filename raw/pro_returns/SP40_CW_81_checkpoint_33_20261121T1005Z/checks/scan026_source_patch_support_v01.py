"""Source-only exact donor spans, reversible edits, and delimiter checks."""
from pathlib import Path
import copy,json,re,runpy,sys
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
API=runpy.run_path(str(OUT/'scan026_source_authority_tools.py'))
class SourceWork:
 def __init__(self,label,sections,previous):
  self.captures,self.root,self.auth,self.helper=API['capture'](label,sections)
  self.exact=self.helper['exact'];self.save=API['save'];self.sha=API['sha']
  self.T={w:(BASE/f'out/readers/026/{w}/reading.tex').read_text() for w in 'ABC'}
  self.M={w:json.loads((BASE/f'out/readers/026/{w}/source_map.json').read_bytes()) for w in 'ABC'}
  self.group_keys={'A':'local_groups','B':'source_groups','C':'groups'}
  self.G={w:{g['id']:g for g in self.M[w][self.group_keys[w]]} for w in 'ABC'}
  self.previous=previous;self.oldplan=json.loads((OUT/previous).read_bytes());self.edits=copy.deepcopy(self.oldplan['edits'])
 def gtext(self,w,gid):
  g=self.G[w][gid]
  if w=='A':a,b=g['source_char_start'],g['source_char_end_exclusive'];literal=g['source_excerpt']
  elif w=='B':a,b=g['start_char'],g['end_char'];literal=g['literal_source']
  else:a,b=g['source_span']['start_character'],g['source_span']['end_character_exclusive'];literal=g['source_exact']
  assert self.T[w][a:b]==literal
  return literal,self.exact(f'out/readers/026/{w}/reading.tex',self.T[w],a,b)
 def candidates(self,w,gid):
  if w=='B':
   rows=self.M[w]['complete_candidate_records'];i=next(i for i,x in enumerate(rows) if x['graphic_id']==gid)
   return copy.deepcopy(rows[i]['complete_candidate_states']),f'/complete_candidate_records/{i}/complete_candidate_states'
  rows=self.M[w][self.group_keys[w]];i=next(i for i,x in enumerate(rows) if x['id']==gid)
  key='complete_candidates' if w=='A' else 'candidate_states'
  return copy.deepcopy(rows[i][key]),f'/{self.group_keys[w]}/{i}/{key}'
 def add(self,eid,a,b,new,sections,purpose,donors=(),changes=()):
  refs=[ref for section in sections for ref in self.auth[section]]
  self.edits.append({'edit_id':eid,'base_char_start':a,'base_char_end':b,'before':self.T['A'][a:b],
   'root_sections':sections,'root_authority_refs':refs,
   'replacement_pieces':[{'literal':new,'purpose':purpose,'root_authority_refs':refs}],
   'exact_donor_sources':list(donors),'bounded_donor_changes':list(changes),'main_approved':False})
 def add_group(self,gid,new,sections,purpose,donors=(),changes=()):
  g=self.G['A'][gid]
  self.add('E026-'+sections[-1]+'-'+gid,g['source_char_start'],g['source_char_end_exclusive'],new,sections,purpose,donors,changes)
 def literal(self,old,new,section,eid,purpose,within=None,donors=(),changes=()):
  a,b=(0,len(self.T['A'])) if within is None else within
  hits=[a+m.start() for m in re.finditer(re.escape(old),self.T['A'][a:b])];assert len(hits)==1,(eid,hits)
  self.add(eid,hits[0],hits[0]+len(old),new,[section],purpose,donors,changes)
 def stage(self,last):
  plan={'scope':f'Cumulative source proposal through root section{last}. Original readers unchanged.',
   'base':copy.deepcopy(self.oldplan['base']),'edits':self.edits,
   'previous_plan':{'path':'out/checks/'+self.previous,'sha256':self.sha((OUT/self.previous).read_bytes())},
   'state_codecs':copy.deepcopy(self.oldplan.get('state_codecs',{})),
   'root_count_and_marker_booleans':'Pending root authority; none chosen by source helper.'}
  artifact=self.save(f'scan026_source_sections01_{last}_plan_v01.json',plan)
  result=self.helper['stage'](plan,f'scan026_source_sections01_{last}_proposal_v01')
  source=Path(result['proposal_path']).read_text();validate(source)
  return result,artifact,source
def replace_once(text,old,new,changes,purpose):
 assert text.count(old)==1,(purpose,old,text.count(old));at=text.index(old)
 changes.append({'start':at,'old':old,'new':new,'purpose':purpose});return text[:at]+new+text[at+len(old):]
def insert_at(text,at,new,changes,purpose):
 changes.append({'start':at,'old':'','new':new,'purpose':purpose});return text[:at]+new+text[at:]
def inverse(text,changes):
 for change in reversed(changes):
  at=change['start'];assert text[at:at+len(change['new'])]==change['new']
  text=text[:at]+change['old']+text[at+len(change['new']):]
 return text
def comment(text,values,changes,purpose,prefix='% complete candidates: '):
 at=text.index(prefix);end=text.index('\n',at)
 return replace_once(text,text[at:end],prefix+json.dumps(values,ensure_ascii=False),changes,purpose)
def validate(text):
 lines=[]
 for line in text.splitlines(keepends=True):
  for i,ch in enumerate(line):
   if ch!='%':continue
   j=i-1
   while j>=0 and line[j]=='\\':j-=1
   if (i-j-1)%2==0:line=line[:i]+('\n' if line.endswith('\n') else '');break
  lines.append(line)
 clean=''.join(lines);braces=[]
 for i,ch in enumerate(clean):
  j=i-1
  while j>=0 and clean[j]=='\\':j-=1
  if (i-j-1)%2:continue
  if ch=='{':braces.append(i)
  elif ch=='}':assert braces,('unexpected close',i);braces.pop()
 assert not braces,braces
 env=[]
 for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
  if m.group(1)=='begin':env.append(m.group(2))
  else:assert env.pop()==m.group(2)
 assert not env
 assert len(re.findall(r'(?<!\\)\$',clean))%2==0
 assert clean.count(r'\[')==clean.count(r'\]')
 for m in re.finditer(r'\\\[([\s\S]*?)\\\]',text):assert not re.search(r'\n[ \t]*\n',m.group(1))
 return {'source_delimiters_balanced':True,'physical_blank_paragraphs_outside_displays':True}
