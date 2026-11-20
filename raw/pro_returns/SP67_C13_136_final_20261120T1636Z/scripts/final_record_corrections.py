from workflow import *
for n,place,explanation in [(352,'H final section heading','H’s closing section heading for the following functor-category section is editorial and is excluded from substantive collation.'),(361,'H closing editorial note','H’s closing note about a possible continuation in another lot is editorial and is excluded from substantive collation.')]:
 p=ROOT/f'records/scan{n}.py';r=ast.literal_eval(p.read_text())
 r['changes']=[x for x in r['changes'] if x['place']!=place]
 if explanation not in r['note']:r['note']+=' '+explanation
 if n==352:
  for d in r['unresolved']:
   if d['place']=='last parenthetical phrase and ending':d['reading']=r"\unsure{d'homotopie à|d'homologie à}; \unsure{a|0}"
 p.write_text(pprint.pformat(r,sort_dicts=False,width=120)+'\n')
p=ROOT/'records/scan359.py';r=ast.literal_eval(p.read_text());r['note']=r['note'].replace('tilted versus hatted','tilded versus hatted');p.write_text(pprint.pformat(r,sort_dicts=False,width=120)+'\n')
log('final report metadata corrections: removed editorial-only H rows on352 and361; corrected352 doubt-table apostrophe notation; no page transcription changed')
rebuild()
