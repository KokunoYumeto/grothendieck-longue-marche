"""One actual based infinity lasso in the eight-strand tangent model."""
from pathlib import Path
import time,json
from tangent_bundle_braid import Segment,Q,I,red,invert
HERE=Path(__file__).resolve().parent
base=Q(1,100);h=Q(10)
path=[base,h+h*I,-h+h*I,-h-h*I,h-h*I,h+h*I]
records=[];forward=[];started=time.monotonic()
for a,b in zip(path,path[1:]):
 r=Segment(a,b,parameter_bound=25).compute();records.append(r);forward+=r['word']
 print('segment',len(records),'crossings',r['crossing_count'],'seconds',round(time.monotonic()-started,3),flush=True)
w=red(forward+invert(records[0]['word']))
assert sum(1 if a>0 else -1 for a in w)==53
out={'description':__doc__,'base':['1/100','0'],'path':[str(a) for a in path],'word':w,'forward_segments':records,'exponent':53,'scope':'Actual based infinity braid; no identification of its root arc with the q0 arc.'}
(HERE/'tangent_infinity_braid.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS actual based infinity braid; length',len(w),'exponent53',flush=True)
