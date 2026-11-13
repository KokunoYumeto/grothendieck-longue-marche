from pathlib import Path
import json
out=[]
for lang in ['fr','en']:
 label='épi' if lang=='fr' else 'epimorphism'
 old=r'\arrow[d,"\text{'+label+r'}"'+"']"
 new=old.replace("'",'')
 out.append(dict(id='140-3-556-L1',language=lang,package='LM_C3-549-567',scan=556,old=old,new=new,reason='Equation (43): put the second vertical epimorphism label on the right of its arrow, so the two unchanged vertical labels occupy separate column gaps.'))
 old=r'\arrow[r,"\text{'+label+r'}"] & '
 new=old.replace(' & ',' &[30pt] ')
 out.append(dict(id='140-3-568-L1',language=lang,package='LM_C3-568-586',scan=568,variants=[dict(old=old,new=new),dict(old=old.replace(' & ',r' \& '),new=new.replace(' &[',r' \&['))],reason='Composite following equation (79): add 30pt only to the epimorphism-arrow column gap, keeping its label clear of the adjacent effective-object superscripts.'))
 label='épi.' if lang=='fr' else 'epimorphism'
 old=r'\arrow[r,"\text{'+label+r'}"]\&'
 new=old+'[30pt]'
 out.append(dict(id='140-3-542-L1',language=lang,package='LM_C3-530-548',scan=542,old=old,new=new,reason='Marginal equation (46bis): add 30pt to the epimorphism-arrow column gap, keeping its unchanged label clear of both effective-object superscripts.'))
for p in json.loads(Path('work/layout_probes/scan417_candidate.json').read_text()):
 p.pop('sourcepath');p['id']='140-2-417-L1';out.append(p)
Path('work/data/layout_label_clearances.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
p=Path('work/data/layout_expected_matches.json');rows=json.loads(p.read_text())
for r in out:
 if not any((x['package'],x['scan'],x['language'])==(r['package'],r['scan'],r['language']) for x in rows):rows.append(dict(language=r['language'],package=r['package'],scan=r['scan'],expected_changes=1))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Added',len(out),'exact paired label-clearance targets')
