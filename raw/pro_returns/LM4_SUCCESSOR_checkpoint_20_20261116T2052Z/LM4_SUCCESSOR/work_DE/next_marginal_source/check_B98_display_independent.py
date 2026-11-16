#!/usr/bin/env python3
"""Replay the displayed B98 private coefficient through the independent B-step contraction."""
from pathlib import Path
import re,json,hashlib
H=Path(__file__).resolve().parent
source=(H/'check_zero_head_diagnostics_independent.py').read_text()
exec(compile(source.split('\nnodes=')[0],str(H/'check_zero_head_diagnostics_independent.py'),'exec'))
A=mp(D['old_actions'][2]['geometric_push_paired']);r=(5,15,-5,-15);w=sub(r,A);c=normalize(chainB(r));d=normalize(chainB(w))
assert len(c)==1 and c=={((5,5,()),((),(),())):1};assert len(w)==592 and len(d)==553
tex=(ROOT/'sections/b_coefficient_domain_counterexample.tex').read_text()
heads=[]
for name,j in [('u',5),('v',15)]:
 block=re.search(r'\b'+name+r'&=(.*?)\\end\{aligned\}',tex,re.S).group(1)
 word=tuple(int(k) for chunk in re.findall(r'\[([0-9,\-]+)\]_p',block) for k in chunk.split(','))
 p,core=peel(A[j]);assert core==(j,) and word==p and not fill(word);heads.append(len(word))
t=(-1,-5,-4)
u0=rr(((1,(),2),(-1,t,2)))
def r_inv(w):return tuple((-s,h,i) for s,h,i in w[::-1])
def ag(g):return ((1,g,2),(1,g,3),(1,red(g+(2,)),5),(1,red(g+(2,)),6))
def cg(g):a=ag(g);return rr(a+((-1,red(g+(2,)),7),)+r_inv(a))
d0=((1,(1,-3,-2),2),(1,(1,-3,-2),3),(1,(1,-3),5),(1,(1,-3),6),(1,(1,-3),8),(1,(1,),10),(1,(1,),11))
v0=rr(cg((4,))+cg(())+r_inv(d0));key=((2,2,()),(u0,v0,t));assert d[key]==-1
record=json.loads((ROOT/'records/B98_displayed_counterexample19.json').read_text())
z=record['displayed_private_row_witness'];assert z['row']==[2,2,[]] and z['integer']==-1
convert=lambda a:[[sg,list(h),i] for sg,h,i in a]
assert z['G_coefficient']=={'A_word':convert(u0),'B_word':convert(v0),'retained_word':list(t)}
print('PASS literal83/85-letter TeX conjugators,actual592-letter image and553 full collected G terms.')
print('PASS independently reconstructed factorized private coefficient(row2,2,1;u0,v0,t)=-1.')
out={'statement_file_sha256':hashlib.sha256(tex.encode()).hexdigest(),'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'conjugator_lengths':heads,'image_length':len(w),'full_G_terms':len(d),'private_row':[2,2,[]],'private_integer':d[key],'method':'separate B-step contraction from actual F21 image;factorized witness evaluated in semantic R labels'}
(H/'B98_display_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
