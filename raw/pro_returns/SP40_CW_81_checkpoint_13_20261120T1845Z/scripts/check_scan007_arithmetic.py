"""Finite arithmetic certificate for the expressions written in scan007's supplied C draft.
This is one explicit positive-integer instance, not a proof of the manuscript's quantified claims.
"""
from pathlib import Path
from datetime import datetime,timezone
from math import comb,gcd
import json
R=Path(__file__).resolve().parents[1]
a,b,c,q,p=3,4,5,2,2
bp,ap=c-a,c-b
alpha,alphap=2,1
bpp=bp//p**alphap
middle=sum(comb(q,i)*a**i*bp**(q-i) for i in range(1,q))
bracket=sum(comb(q,i)*a**i*bp**(q-i-1) for i in range(1,q))+bp**(q-1)
certificate={
 'values':{'a':a,'b':b,'c':c,'q':q,'p':p,"b'":bp,"a'":ap,'alpha':alpha,"alpha'":alphap,"b''":bpp},
 'coprimality':[gcd(a,b),gcd(a,c),gcd(b,c)],
 'power_identity':[a**q+b**q,c**q],
 'positive_differences':[c-a,c-b],
 'full_binomial_sum':sum(comb(q,i)*a**i*bp**(q-i) for i in range(q+1)),
 'equation_1':[b**q,middle+bp**q],
 'factored_equation_1':[b**q,bp*bracket],
 'valuation_residues':{'b_mod_p_alpha':b%p**alpha,'b_mod_next':b%p**(alpha+1),'bp_mod_p_alphap':bp%p**alphap,'bp_mod_next':bp%p**(alphap+1)},
 'valuation_inequality':[alphap,q*alpha],
 'bpp_factorization':[bp,p**alphap*bpp],
 'bpp_coprimality':gcd(bpp,p),
 'final_divisor':p**(q*alpha-alphap),
 'final_bracket':bracket,
 'final_division':[bracket//p**(q*alpha-alphap),bracket%p**(q*alpha-alphap)]
}
assert certificate['coprimality']==[1,1,1]
assert certificate['power_identity']==[25,25]
assert certificate['equation_1']==[16,16] and certificate['factored_equation_1']==[16,16]
assert certificate['valuation_residues']=={'b_mod_p_alpha':0,'b_mod_next':4,'bp_mod_p_alphap':0,'bp_mod_next':2}
assert certificate['final_division']==[1,0]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
text='''# Scan007 — one exact arithmetic instance

The assignment is q=2, p=2, a=3, b=4, c=5, b′=2, a′=1, α=2, α′=1, b″=1. The evaluation morphism Z[A,B,C,U,V] → Z fixes integers and sends the five generators to 3,4,5,2,1 respectively; it extends by addition and multiplication. Thus each finite polynomial expression is evaluated using those generator images. Prime and divisibility assertions in this instance are checked by integer arithmetic below.

The equalities a²+b²=c²=25, c=a+b′=b+a′=5, b²=2ab′+b′²=16 and b²=b′(2a+b′)=16 hold numerically. The bracket in the last line is 2a+b′=8, and p^(qα−α′)=2³=8. Its quotient is1 and its remainder0. The exact valuations are evidenced by divisibility at2² and2¹ respectively and the nonzero next-power remainders. This finite instance rechecks the exponent/substitution pattern only. It does not prove the page's general implications or settle any glyph or hand attribution.

Executed: NOW

```json
DATA
```
'''.replace('NOW',now).replace('DATA',json.dumps(certificate,ensure_ascii=False,indent=2))
(R/'checks/scan007_arithmetic.md').write_text(text)
event={'statement_id':'007-arithmetic-instance','date':now,'who':'GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root','type':'computation or formal certificate','outcome':'One exact q=2 instance a=3,b=4,c=5,p=2,b-prime=2,alpha=2,alpha-prime=1,b-double-prime=1. Binomial and factored values16 agree; final bracket8 is divisible by final divisor8, quotient1 remainder0. Coprimality and exact valuations checked numerically. Scope is this finite instance only; it is not a proof of the general manuscript statements. Evaluation morphism and all values: checks/scan007_arithmetic.md.'}
(R/'checks/scan007_check_events.json').write_text(json.dumps([event],ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'executed':now,'final_divisor':certificate['final_divisor'],'final_bracket':bracket,'division':certificate['final_division']}))
