"""Exact structural refutation of the intermediate Q-to-PB5 injection.

This is a new post-recovery result. It does not refute injectivity of the
full theta5: the same source word is explicitly nonidentity in PB6.
"""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import inverse as inv,multiply as mul,substitute as sub,artin
j=json.loads((HERE/'Q_birman_reconstructed_certificate.json').read_text())
acts={name:{int(i):tuple(v) for i,v in A.items()} for name,A in j['actions'].items()}
a,f,e=(acts[n] for n in ['a','f','e'])
C=(1,);T=(2,);R=(3,);S=(4,);V=(-2,3,2);ST=(4,2)
assert sub(C,f)==C and sub(V,f)==V and sub(ST,f)==ST
beta_C=sub(sub(C,e),a) # alpha_(a e)=alpha_a composed with alpha_e.
p=mul(inv(V),inv(ST))
assert beta_C==mul(p,C,inv(p))
assert sub(beta_C,f)==beta_C
print('f fixes C, V=T^-1RT, and ST: PASS')
print('(ae)(C)=p C p^-1 with p=V^-1(ST)^-1, hence f fixes (ae)(C): PASS')
print('Action composition is alpha_(ae)=alpha_a composed with alpha_e.')
print('The push map is antihomomorphic; inversion makes it homomorphic and does not change this fixed-word calculation.')

# Actual old source indices shifted by one: a=f0, e=f4, f=f5, c=f2.
g=(-5,-1,6,1,5);c=(3,)
w=mul(g,c,inv(g),inv(c))
assert w==(-5,-1,6,1,5,3,-5,-1,-6,1,5,-3)
# In Q=A*B*E with A=<a,t>, B=<c,f>, E=<e>, all12 syllables remain.
factors={1:'A',3:'B',5:'E',6:'B'}
syllables=[factors[abs(x)] for x in w]
assert all(x!=y for x,y in zip(syllables,syllables[1:]))
print('Source word:',w)
print('Q free-product syllable sequence:',syllables)
print('All12 nonidentity syllables alternate: the word is nontrivial in Q.')

# A small independent finite quotient of Q: a=c=f=(12), e=(23), t=1.
I=(0,1,2);x=(1,0,2);y=(0,2,1)
def compose(a,b):return tuple(a[b[i]] for i in range(3))
perms={1:x,3:x,5:y,6:x}
P=I
for z in w:P=compose(P,perms[abs(z)]) # all selected images are involutions.
assert P!=I
print('Independent S3 quotient image:',P,'nonidentity: PASS')

five={int(i):tuple(v) for i,v in j['five_strand_source_images'].items()}
b5=sub(w,five);A5=artin(b5,5)
assert A5==tuple((i,) for i in range(1,6))
six=json.loads((HERE/'cyclic_rigid_braid_words.json').read_text())
images6={r['index']+1:tuple(r['braid']) for r in six['basis']}
b6=sub(w,images6);A6=artin(b6,6)
assert A6[0]!=(1,)
assert sum(1 if z>0 else -1 for z in b6)==0
print('Actual PB5 word length',len(b5),'Artin image lengths',[len(v) for v in A5],': identity PASS')
print('Actual PB6 word length',len(b6),'Artin image lengths',[len(v) for v in A6],': nonidentity PASS')
print('PB6 exponent sum0; fixed-pair linking excludes a nonzero central full twist.')
cert={'status':'Proved noninjectivity of intermediate Q map only',
      'source_word_shifted':w,'g_shifted':g,'c_shifted':c,
      'Q_syllable_factors':syllables,'S3_image_zero_based':P,
      'action_checks':{'V':V,'ST':ST,'p':p,'ae_C':beta_C},
      'PB5_word':b5,'PB5_Artin_images':A5,
      'PB6_word':b6,'PB6_Artin_image_lengths':[len(v) for v in A6],
      'PB6_first_Artin_image':A6[0],
      'convention':'Artin multiplicative action; alpha_(ae)=alpha_a composed with alpha_e. Extracted push is anti, corrected by inversion.',
      'remaining_open':'Full theta5 injection and induced full profinite topology'}
(HERE/'Q_noninjection_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS structural extra stabilizer; exact PB5 kernel word; Q nontriviality; PB6 nonidentity')
