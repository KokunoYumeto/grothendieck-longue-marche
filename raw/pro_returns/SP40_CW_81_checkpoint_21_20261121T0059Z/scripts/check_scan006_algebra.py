"""Exact truncated-jet coefficient checks for the candidate formulas of scan006.
No ink reading is inferred, no manuscript expression is changed.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

p0,p1,p2,q0,q1,q2,x0,x1,x2,y0,y1,y2,t=s.symbols('P0 P1 P2 Q0 Q1 Q2 x0 x1 x2 y0 y1 y2 epsilon')
half=s.Rational(1,2)
P=p0+p1*t+half*p2*t*t
Q=q0+q1*t+half*q2*t*t
Qi=1/q0-q1*t/q0**2+(q1**2/q0**3-half*q2/q0**2)*t*t
X=x0+x1*t+half*x2*t*t
Y=y0+y1*t+half*y2*t*t

def c(expr,n):
    return s.expand(expr).coeff(t,n)

checks=[
 ('006-jet-inverse','The image assigned to Q inverse multiplies the image of Q to 1 modulo epsilon^3.', [s.expand(q0**3*(c(Q*Qi,n)-(1 if n==0 else 0))) for n in range(3)]),
 ('006-first-quotient','The epsilon coefficient of the image of P/Q agrees with (P1*Q0-Q1*P0)/Q0^2.', [s.expand(q0**2*(c(P*Qi,1)-(p1*q0-q1*p0)/q0**2))]),
 ('006-second-quotient','Twice the epsilon^2 coefficient of the image of P/Q agrees with (P2*Q0^2-Q2*P0*Q0-2*P1*Q0*Q1+2*P0*Q1^2)/Q0^3.', [s.expand(q0**3*(2*c(P*Qi,2)-(p2*q0**2-q2*p0*q0-2*p1*q0*q1+2*p0*q1**2)/q0**3))]),
 ('006-second-product','Twice the epsilon^2 coefficient of the image of x*y agrees with x2*y0+2*x1*y1+x0*y2.', [s.expand(2*c(X*Y,2)-(x2*y0+2*x1*y1+x0*y2))]),
]
for label,statement,residual in checks:
    assert all(v==0 for v in residual),(label,residual)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
root=Path(__file__).resolve().parents[1]
intro=r'''# Scan006 — exact coefficient computations

The computation uses the explicit ring morphism from the commutative Laurent polynomial ring Q[P,Q,Q^{-1},x,y] into
Q[P0,P1,P2,Q0,Q0^{-1},Q1,Q2,x0,x1,x2,y0,y1,y2,epsilon]/(epsilon^3), defined on its generators by:

- P maps to P0 + P1 epsilon + P2 epsilon^2/2.
- Q maps to Q0 + Q1 epsilon + Q2 epsilon^2/2.
- Q^{-1} maps to Q0^{-1} - Q1 Q0^{-2} epsilon + (Q1^2 Q0^{-3} - Q2 Q0^{-2}/2) epsilon^2.
- x maps to x0 + x1 epsilon + x2 epsilon^2/2.
- y maps to y0 + y1 epsilon + y2 epsilon^2/2.

The recorded inverse-product coefficients verify the defining relation Q Q^{-1}=1 in the target. These generator images extend by addition and multiplication; the checked relation proves that the displayed assignment is a well-defined ring morphism. The three remaining computations extract its first and second coefficients and compare them with the displayed candidate derivative expressions. All residuals are expanded exact Laurent-polynomial coefficients; denominators are cleared by the displayed Q0 powers. This specifies the algebraic map used in the checks.

These computations do not determine whether any handwritten exponent is 2 or a double prime, whether a cancelled sign is plus or minus, or which factor order the pen writes. Those are separate ink decisions. No formula on the manuscript is rewritten by this calculation.

'''
lines=[intro,'Executed: '+now+'\n']
events=[]
for label,statement,residual in checks:
    outcome=statement+' Exact denominator-cleared residual coefficient list: '+str(residual)+'. Source: checks/scan006_algebra.md; scripts/check_scan006_algebra.py.'
    events.append({'statement_id':label,'date':now,'who':'GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root','type':'computation or formal certificate','outcome':outcome})
    lines.append('## '+label+'\n\n'+statement+'\n\nResidual coefficients: `'+str(residual)+'`.\n')
(root/'checks/scan006_algebra.md').write_text('\n'.join(lines))
(root/'checks/scan006_check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'executed_utc':now,'events':len(events),'residuals':{a:[str(z) for z in c] for a,b,c in checks}}))
