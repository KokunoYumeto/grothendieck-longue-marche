from pathlib import Path
import json,sys,copy
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from record_audit import build_revision,stable_changes
key='B10-02_10_scan049';out=Path('SP02_CW_10+12');s=json.loads((out/f'documentation/audit_sessions/{key}_audit001.json').read_text());r=json.loads((out/f'documentation/page_records/{key}.json').read_text());c=stable_changes(r,key);t=(out/f'pages/{key}.tex').read_text()
p=dict(audit_id=s['audit_id'],baseline_page_sha256=s['baseline_page_sha256'],audit_reading_complete=True,audit_inventory_confirmed=True,edits=[],upsert_changes=[])
def edit(old,new,count=1):p['edits'].append(dict(old=old,new=new,count=count))
def update(i,**kw):
 z=copy.deepcopy(c[i]);z.update(kw);p['upsert_changes'].append(z)
edit(r'Soi\deleted{\unsure{ent}}',r'Soi\deleted{ent}')
edit('sur un vectoriel sur',r'sur un vec\deleted{o}\handwritten{t}oriel sur')
edit('nécessairement de dimension finie',r'nécessairement de \deleted{\unsure{t|d}}\inserted{d}imension finie')
edit("alors il opère fidèlement sur l'enveloppe", "alors il opère fidèle-\\linebreak ment sur l'enveloppe")
edit(r'que $G$ opère fidèlement sur le vectoriel $V$',r'que $G$ opère fidèle-\linebreak ment sur le vectoriel $V$')
edit('noethé%','noethé-%')
edit(r'\draw (0,0)--(.03,-5);',r'\draw (0,0) .. controls (-.20,-1.5) and (-.03,-3) .. (.12,-5);')
update(2,final=r'Soi\deleted{ent}\handwritten{t}',shows='The e bowl survives beneath the tall pen t; n has its left stem and shoulder; the final typed t has an upright and crossbar emerging above the hatching. These letter parts resolve ent, while the new pen t remains live.',crop='audit-ent',confidence='medium',against_C=True)
update(7,final=r'fidèlement sur X quasi-affine sur k, alors il opère fidèle-\linebreak ment sur ...',shows='The crossed typed line retains the letters of alors il opère, followed by fidèle- at the physical line end; ment begins the following cancelled line. The i and l after alors are distinct; the short terminal hyphen is visible between the overstrikes.',crop='audit-middle;audit-cancel-hyphen',against_C=True)
update(11,crop='audit-formula-one');update(12,crop='audit-formula-two');update(13,crop='audit-Spec-formula');update(14,crop='audit-V-Gamma')
update(19,final='TikZ long grouping stroke with shallow leftward bow',shows='The long pen stroke bows slightly left through its upper and middle length, then returns rightward toward the lower endpoint. The revised curve retains that visible shape.',crop='audit-margin',against_C=True)
rows=[
('overlapping letter in condition iv vectoriel','vectoriel','vectoriel',r'vec\deleted{o}\handwritten{t}oriel','A closed oval o remains beneath a taller straight pen stem and crossbar forming t. Both layers are retained; the separate next o is unaffected.','audit-vectoriel-detail','medium','deletion state (struck given live or live given struck)',True),
('overlapping initial letter of condition iv dimension','dimension','dimension',r'\deleted{\unsure{t|d}}\inserted{d}imension','The live d has its left bowl and right ascender. A second upright and long crossbar overlap it, suggesting an underlying t; a displaced d remains possible. The underletter is kept doubtful rather than silently discarded.','audit-dimension-detail','low','deletion state (struck given live or live given struck)',True),
('line division in final proof paragraph','fidèlement','fidèlement',r'fidèle-\linebreak ment','The first physical line ends with fidèle- and the next begins ment. The visible hyphen and division are retained.','audit-lower','high','other',True),
('page terminal hyphen','noethé without printed hyphen','noethé-','noethé-','A separate short horizontal hyphen follows the accented final é at the page edge. It is restored without supplying any continuation.','audit-ending','high','other',False)]
for no,row in enumerate(rows,23):
 place,C,H,final,shows,crop,confidence,kind,againstH=row;p['upsert_changes'].append(dict(id=key+f'-L{no:03}',place=place,C=C,H=H,final=final,shows=shows,crop=crop,confidence=confidence,against_C=True,against_H=againstH,marked_in_H=False,kind=kind,consequential=False))
p['remaining_doubts']=[copy.deepcopy(d) for d in r['remaining_doubts'] if d['line']!='amended Soient']
p['remaining_doubts'].append(dict(line='condition iv dimension underletter',reading='t',alternatives='d',confidence='low',comment='Overlapping upright and crossbar partly merge with the live d.'))
p['inventory_patches']={x['element']:{'hand':'another unnamed hand'} for x in r['inventory_resolved'] if x['hand'] in ['unknown','unnamed hand']}
p['inventory_patches'].setdefault('049-28',{}).update(kind='drawing')
p['inventory_patches'].setdefault('049-07',{}).update(first_words_or_objects='vertical grouping stroke with shallow leftward bow')
p['inventory_extra']=[]
for el,hand,kind,pos,words in [('archive','another unnamed hand','margin note','bottom left','archive folio48 retained in comment'),('vectoriel-old','typewriter','deletion','condition iv vectoriel','o under corrected t'),('vectoriel-new','his hand','insertion','condition iv vectoriel','t over o'),('dimension-old','typewriter','deletion','condition iv dimension','uncertain t or displaced d under d'),('dimension-new','typewriter','insertion','condition iv dimension','d over overlapping glyph')]:p['inventory_extra'].append(dict(scan='10:049',sheet_kind='typescript',hand=hand,element='audit-'+el,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
p['crops_upsert']=json.loads(Path('work/audit10_049_crops.json').read_text())
p['observations']='Root ordered second reading: whole and both supplied halves viewed before image-first receipt and text opening, followed by29 personally viewed fresh audit crops. The previously truncated upright addition, number marks and long margin were individually reopened. All words, accents, punctuation, conditions, arrows, indices and four plain underlined O symbols were compared with both witnesses and the ink. All four proof implications have two shafts; the morphism arrows have one. The amended ent is resolved from surviving letters. Two overlooked overlapping letter corrections in condition iv are represented, with the underlying dimension letter left doubtful. Cancelled and live fidèle-/ment divisions and page-terminal noethé- are retained. The margin grouping stroke is bowed as drawn. The deleted Aut argument and final K index remain uncertain; pas, enveloppe and grou remain resolved. The number marks and k-insertion stroke remain nonlexical drawings. Manuscript17 and archive48 remain distinct. Three doubts remain. No context or mathematical proof check was used.'
Path('work/audit10_049.json').write_text(json.dumps(p,ensure_ascii=False,indent=2));_,new=build_revision(p,s,r,t);Path('work/audited10_049.tex').write_text(new)
print('edits',len(p['edits']),'upserts',len(p['upsert_changes']),'crops',len(p['crops_upsert']))
