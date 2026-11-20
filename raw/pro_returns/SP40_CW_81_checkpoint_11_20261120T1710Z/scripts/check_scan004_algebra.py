"""Exact local calculations for scan 004; no inference of handwritten glyphs."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s

root=Path(__file__).resolve().parents[1]
fi,ei,f1,e1,en,fn=s.symbols('f_i e_i f_1 e_1 e_next f_next',commutative=False)
lam,alpha,beta=s.symbols('lambda alpha beta')
checks={
 '004-lambda-expansion':s.expand((fi+lam*ei)*(f1+lam*e1)-(fi*f1+lam**2*ei*e1+lam*(fi*e1+ei*f1))),
 '004-even-coefficient':s.expand((-alpha*en-beta*fn)+en-((1-alpha)*en-beta*fn)),
}
when=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
lines=['# Scan 004 — exact local algebra calculations','',
       'UTC: '+when,'',
       'Run: /root; GPT-6 Astra Pro; effort inherited and not separately exposed.','',
       'The calculation uses the free associative algebra over Z[lambda,alpha,beta], with the displayed parameters central. The noncommuting generators retain the written factor order. These are explicit symbolic calculations, without adjudication of manuscript symbols.','']
for name,residual in checks.items():
    assert residual==0
    lines.append(f'- {name}: expanded residual `{residual}`.')
lines += ['',
 '004-lambda-expansion expands (f_i+lambda e_i)(f_1+lambda e_1) and subtracts f_i f_1+lambda² e_i e_1+lambda(f_i e_1+e_i f_1).',
 '004-even-coefficient expands (-alpha e_next-beta f_next)+e_next and subtracts (1-alpha)e_next-beta f_next. This records the coefficient arithmetic only.','']
(root/'checks/scan004_algebra.md').write_text('\n'.join(lines))
print('\n'.join(lines))
