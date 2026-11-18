"""Exact finite no-opposite-pair condition used in the all-exponent proof."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
p=Path(__file__).with_name('check_Q6_forced_frame.py');src=p.read_text()
G={'__file__':str(p),'__name__':'_A62_head'}
with redirect_stdout(StringIO()):exec(compile(src.split('if frank(RES)==8:')[0],str(p),'exec'),G)
chars=G['chars'];ci={v:i for i,v in enumerate(chars)}
opp=[ci[G['sm'](6,v)]for v in chars]
sp=[next(i for i,a in enumerate(col)if a)for col in G['S']]
assert len(chars)==36 and all(sp[sp[i]]==i and opp[opp[i]]==i for i in range(36))
assert all(sp[i]!=opp[i]for i in range(36))
pairs={frozenset((i,opp[i]))for i in range(36)}
seen=set();oriented=[];fixed=0;double=0
for pair in sorted(pairs,key=lambda x:tuple(sorted(x))):
 if pair in seen:continue
 a,b=sorted(pair);image=frozenset((sp[a],sp[b]))
 assert image in pairs
 seen.add(pair);oriented.append((a,b))
 if image==pair:
  assert sp[a]==a and sp[b]==b;fixed+=1
 else:
  assert image not in seen;seen.add(image);oriented.append((sp[a],sp[b]));double+=1
assert len(oriented)==18 and set((sp[a],sp[b])for a,b in oriented)==set(oriented)
conj={G['mul'][G['mul'][G['inv'][q]][G['s']]][q]for q in range(72)}
bad={G['beta'],G['mul'][G['beta']][G['s']]}
assert not conj&bad
assert fixed==2 and double==8
print('Weight count36; unordered opposite pairs18; s exchanges the two weights of NONE: PASS')
print('Pair orbits under s: fixed2, two-element8')
print('An explicit s-invariant orientation:',oriented)
print('The s conjugacy class in S3 x A4 avoids beta and beta*s: PASS')
print('Finite condition for vanishing integral s orientation carry at every2-power exponent: PASS')
