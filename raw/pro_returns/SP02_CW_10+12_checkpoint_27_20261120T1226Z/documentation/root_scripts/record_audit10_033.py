from pathlib import Path
import json,sys,copy
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from record_audit import stable_changes,build_revision
key='B10-01_10_scan033'
out=Path('SP02_CW_10+12')
s=json.loads((out/f'documentation/audit_sessions/{key}_audit001.json').read_text())
r=json.loads((out/f'documentation/page_records/{key}.json').read_text())
c=stable_changes(r,key)
p=dict(audit_id=s['audit_id'],baseline_page_sha256=s['baseline_page_sha256'],audit_reading_complete=True,audit_inventory_confirmed=True)
p['edits']=[
 dict(old=r'Les p\textsuperscript{ges} qui suivent',new=r'Les \unsure{p\textsuperscript{ges}|pages} qui suivent'),
 dict(old=r'\unsure{(p\textsuperscript{ges}|p\textsuperscript{ges}}',new=r'\unsure{(p\textsuperscript{ges}|p\textsuperscript{ges}|(pages|pages}'),
 dict(old=r'X_i\handwritten{\longmapsto}X_i',new=r'X_i\handwritten{\rightsquigarrow}X_i'),
 dict(old=r'$j\handwritten{\in}I$ deux $S_j$',new=r'$j\handwritten{\in}I$ deu\deleted{s}\inserted{\handwritten{x}} $S_j$')]
p['upsert_changes']=[]
for n,final,shows,crop in [
 (1,r'\unsure{p\textsuperscript{ges}|pages}','Second reading: a long descending first stroke is followed by a small detached oval, then the g loop/descender and cramped ending. The oval could belong to the p or be a separate a; its height does not securely establish abbreviation versus full pages. The earlier certainty is withdrawn. No separate 11 is visible.','audit-margin-upper;audit-pges-top'),
 (4,r'\unsure{(p\textsuperscript{ges}|p\textsuperscript{ges}|(pages|pages}','Second reading: the second page-word has the same long p-like stroke and compressed upper ending; the available strokes do not securely distinguish p-ges from full pages or a separate opening parenthesis. The closing parenthesis after117 is clear.','audit-margin-upper;audit-pges-lower')]:
 z=copy.deepcopy(c[n]);z.update(final=final,shows=shows,crop=crop,confidence='medium');p['upsert_changes'].append(z)
def change(i,place,C,H,final,shows,crop,kind):
 p['upsert_changes'].append(dict(id=key+i,place=place,C=C,H=H,final=final,shows=shows,crop=crop,kind=kind,confidence='high',against_C=True,against_H=True,marked_in_H=False))
change('-A001','10.0, object-assignment arrow',r'\longmapsto',r'\mapsto',r'\rightsquigarrow','The shaft begins with three small alternating bends and continues to a right-facing arrowhead. There is no vertical source bar. The enlarged isolated sign supports a wavy arrow, replacing the straight barred arrow in both witnesses.','audit-object-arrow;audit-functors','misread symbol or index')
change('-A002','10.1, word immediately after j in I','deux','deux',r'deu\deleted{s}\inserted{\handwritten{x}}','The surviving typed final letter has an upper rounded shoulder and a lower left-facing bowl, unlike the plain typed x in the earlier deux. Two darker diagonal pen strokes overwrite it as x. Both the original s and handwritten replacement are recorded.','audit-two-x;audit-typed-deux','deletion state')
p['remaining_doubts']=copy.deepcopy(r['remaining_doubts'])
p['remaining_doubts'][0].update(reading=r'(p\textsuperscript{ges}',alternatives=r'p\textsuperscript{ges} | (pages | pages')
p['remaining_doubts'].insert(0,dict(line='upper left note, first page-word',reading=r'p\textsuperscript{ges}',alternatives='pages',confidence='medium'))
p['notation_updates_replace']=copy.deepcopy(r['notation_updates'])
for x in p['notation_updates_replace']:
 if x['sign']=='page abbreviation':x.update(status='uncertain',form=r'p\textsuperscript{ges} | pages',attestations='10/033 upper-left note, twice; second reading retains ambiguity over the small oval and compressed letter heights.')
p['notation_updates_replace'].append(dict(sign='wavy object-assignment arrow',status='read',form=r'\rightsquigarrow',attestations='10/033 §10.0: three alternating shaft bends and right arrowhead; no source bar.'))
p['inventory_patches']={'crossed-comma':{'hand':'another unnamed hand'},'replacement-note':{'first_words_or_objects':r'Les \unsure{p\textsuperscript{ges}|pages} qui suivent'}}
p['inventory_extra']=[dict(scan='10:033',sheet_kind='typescript',hand=h,element=e,kind=k,position=pos,first_words_or_objects=t,transcribed='yes') for h,e,k,pos,t in [('another unnamed hand','audit-archive','margin note','bottom left','archive folio32 retained in comment'),('typewriter','audit-deus-source','deletion','10.1 after j in I','typed s in deus overwritten'),('his hand','audit-deux-replacement','insertion','10.1 final letter of deus','handwritten x over typed s')]]
p['crops_upsert']=json.loads(Path('work/audit10_033_crops.json').read_text())
p['observations']='Root second reading, in map order. The whole and both supplied halves were reread before the immutable image-first observations and text-open receipt. All prose, accents, punctuation, mathematical letters/indices, inequalities, underlines and editorial states were compared with the consolidated page. All20 audit crops were viewed, including both slanted notes rotated upright. The page-word abbreviation is made uncertain again; the wavy object-assignment arrow and typed-s/handwritten-x correction are recorded. The six earlier doubtful loci were revisited: the parenthesis/page-word alternatives are broadened; first algebra font, cancelled comma, composition oval, final citation punctuation and cancelled d-prime remain unresolved. Typed Etant stays unaccented, and the visible acute in handwritten Précisons is retained. The top handwritten1 remains manuscript numbering; bottom pencil32 remains an archival comment and is now included in the inventory. No context or mathematical proof check was used.'
Path('work/audit10_033.json').write_text(json.dumps(p,ensure_ascii=False,indent=2))
_,text=build_revision(p,s,r,(out/f'pages/{key}.tex').read_text());Path('work/audited10_033.tex').write_text(text)
