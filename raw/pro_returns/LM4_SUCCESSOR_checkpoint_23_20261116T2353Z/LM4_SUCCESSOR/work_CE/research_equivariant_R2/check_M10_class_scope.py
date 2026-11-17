"""Exhaust the inverse-compatible conjugacy classes, not arbitrary heads."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
p=Path(__file__).with_name('check_M10_reflection_obstruction.py')
g={'__file__':str(p),'__name__':'_readonly'}
with redirect_stdout(StringIO()):exec(compile(p.read_text().split('out=dict(scope=')[0],str(p),'exec'),g)
LP,pm,pi,hp,order,ONE=[g[x]for x in ('LP','pm','pi','hp','order','ONE')]
left=set(LP);classes=[]
while left:
 x=min(left);cl={pm(pm(v,x),pi(v))for v in LP};left-=cl;classes.append((x,cl))
which={x:i for i,(_,cl)in enumerate(classes)for x in cl}
rows=[]
for i,(x,cl)in enumerate(classes):
 target=which[pm(pm(hp,x),pi(hp))];inverse=which[pi(x)]
 rows.append(dict(class_index=i,order=order(x),size=len(cl),image=target,inverse=inverse,negative_compatible=target==inverse))
for row in rows:print(row)
assert {r['order']for r in rows if r['negative_compatible']}=={1,2,4}
print('Only orders1,2,4 are negative-compatible. A generating pants passport must therefore be(4,4,4): any2 gives a solvable Euclidean/dihedral triangle quotient.')
print('Every possible negative-compatible generating pants head is stopped by the SL2 trace-sign obstruction.')
Path(__file__).with_name('M10_class_scope.json').write_text(json.dumps(rows,indent=2)+'\n')
