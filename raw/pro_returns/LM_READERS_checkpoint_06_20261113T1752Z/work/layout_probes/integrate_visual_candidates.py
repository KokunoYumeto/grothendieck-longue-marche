from pathlib import Path
import json,sys,re
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs
p=Path('work/data/layout_label_clearances.json');out=json.loads(p.read_text());more=[]
reasons={
562:'Equation (65): increase both existing central vertical-edge offsets from 0.7ex to 2.5ex so they clear the intervening uncertain objects and superscripts; retain all endpoints, arrow styles, matrix dimensions and labels.',
573:'Equation (3): add 110pt only before the final column so the unchanged two-line restriction label clears the adjacent automorphism objects and the arrowhead; retain matrix height.',
574:'Equation (8): add 50pt only before the final column to separate the unchanged sign-of-a-permutation label from the curved-arrow barb and the target brace; retain arrow endpoints and matrix height.',
628:'Equation (26): place the unchanged gerbe-of-group label on the left of its vertical arrow, away from the diagonal to the elliptic-curve object; retain diagram dimensions and every map endpoint.',
}
for r in json.loads(Path('work/layout_probes/additional_label_candidates.json').read_text()):
 if r['scan']==638:continue
 r['reason']=reasons[r['scan']]
 # The selected mechanical repair merely adds the declared replacement token
 # for these raw TikZ-CD diagrams; retain both exact input-stage spellings.
 raw=build_readers.raw_package(r['package'],r['language']);variants=[dict(old=r['old'],new=r['new'])]
 old=r['old'].replace('[ampersand replacement=\\&,','[').replace('[ampersand replacement=\\&]','').replace(r'\&','&')
 new=r['new'].replace('[ampersand replacement=\\&,','[').replace('[ampersand replacement=\\&]','').replace(r'\&','&')
 if old!=r['old'] and old in raw:variants.append(dict(old=old,new=new))
 if r['old'] not in raw:assert len(variants)==2,(r['package'],r['scan'],r['language'])
 r.pop('old');r.pop('new');r['variants']=variants;more.append(r)
for r in json.loads(Path('work/layout_probes/scan165_candidate.json').read_text()):
 r['id']='140-2-165-L1';more.append(r)
for lang in ['fr','en']:
 old=r'\mspage{493}'+'\n\n';new=old+r'\Needspace{6\baselineskip}'+'\n'
 more.append(dict(language=lang,package='LM_C3-492-510',scan=494,id='140-3-495-N1',kind='marginal note placement',old=old,new=new,reason='Before scan 495, reserve six baselines for its scan mark, manuscript-page marker, section heading and short marginal note; keep the unchanged two-line note in the margin with its linked uncertainty.'))
for r in more:
 key=(r['id'],r['language']);assert not any((x['id'],x['language'])==key for x in out),key;out.append(r)
p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
p=Path('work/data/layout_expected_matches.json');rows=json.loads(p.read_text())
for r in more:
 key=(r['package'],r['scan'],r['language']);assert not any((x['package'],x['scan'],x['language'])==key for x in rows),key
 rows.append(dict(language=r['language'],package=r['package'],scan=r['scan'],expected_changes=1))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('integrated',len(more),'exact patches')
