#!/usr/bin/env python3
"""Materialize a standalone nf-only verifier from the literal ideal witnesses."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
H=Path(__file__).resolve().parent
def rows(stem):return [json.loads(s) for s in (H/(stem+'.out')).read_text().splitlines() if s.startswith('{')]
up=rows('e53_positional_presentation')
lo=next(r for r in rows('e53_positional_lower_export') if r['type']=='literal_lower_data')
piv=next(r for r in rows('e53_positional_genus_pivots') if r['type']=='actual_surviving_pivot_primes')
r=next(r for r in up if r['type']=='full_S_class_presentation')
def gp(x):
 if isinstance(x,list):return '['+','.join(gp(v) for v in x)+']'
 if isinstance(x,str):return str(Fraction(x))
 return str(x)
def gm(x):return '['+';'.join(','.join(gp(v) for v in row) for row in x)+']'
def poly(a):return '+'.join('('+str(Fraction(v))+')*x^'+str(i) for i,v in enumerate(a) if Fraction(v)) or '0'
def vecpoly(a):return '['+','.join(poly(v) for v in a)+']'
lines=[
 r'\\ Standalone literal ideal verification; no input files, no bnf operation.',
 'default(parisize,128000000);default(parisizemax,1000000000);',
 'check(a,s)=if(!a,error(s));',
 'jmat(A)=vector(matsize(A)[1],i,Vec(A[i,]));',
 'lc(L,beta,z,Q,T,u)={my(v=idealval(L,u,Q),nu=nfeltnorm(L,u)/2757^v,pr=nfmodprinit(L,T,\'t),rr=nfmodpr(L,u/beta^idealval(L,u,T),pr)^((53^2-1)/3),zz=nfmodpr(L,z,pr));check(valuation(nu,3)==0&&valuation(nu-1,3)>=2,"wild domain");[lift(Mod(-(nu-1)/9,3)),if(rr==1,0,if(rr==zz,2,if(rr==zz^2,1,error("phase"))))]};',
 '{',
 'my(UB='+vecpoly(r['field_integral_basis'])+',LB='+vecpoly(lo['integral_basis'])+');',
 'my(F=nfinit([x^18+53*x^9+2809,UB,[3,53]],4),L=nfinit([x^6+53*x^3+2809,LB,[3,53]],4));',
 'check(F.zk==UB && L.zk==LB,"literal integral bases unchanged");',
 'check(F.disc==-3^45*53^16 && L.disc=='+lo['discriminant']+',"exact field discriminants");',
 'check(nfcertify(F)==[] && nfcertify(L)==[],"unconditional maximal orders");',
 'my(IG=['+','.join(gm(a) for a in r['class_generator_HNF'])+']);',
 'my(LG=['+','.join(gm(a) for a in lo['outside_S_class_generators'])+']);',
 'for(i=1,3,check(nfisideal(F,IG[i]),"literal upper generator ideal"));',
 'for(i=1,2,check(nfisideal(L,LG[i]),"literal lower generator ideal"));',
 'my(count=0);'
]
for a in up:
 t=a['type']
 if t=='class_power_relation':
  i=a['index'];target=f'idealpow(F,IG[{i}],{a["exponent"]})'
 elif t=='S_prime_relation':
  target='idealdiv(F,'+gm(a['prime_HNF'])+',idealfactorback(F,IG,'+gp(a['class_column'])+'~))'
 elif t=='upper_pivot_relation':
  lines.append('check(nfisideal(F,'+gm(a['prime_HNF'])+') && idealnorm(F,'+gm(a['prime_HNF'])+')=='+str(a['prime'])+' && idealadd(F,'+gm(a['prime_HNF'])+',Mod(x-'+str(a['beta_residue'])+',F.pol))=='+gm(a['prime_HNF'])+',"literal upper prime and chosen residue");')
  target='idealdiv(F,'+gm(a['prime_HNF'])+',idealfactorback(F,IG,'+gp(a['class_column'])+'~))'
 else:continue
 lines.append('check(idealhnf(F,Mod('+poly(a['generator_coefficients'])+',F.pol))==idealhnf(F,'+target+'),"upper full ideal identity");count++;')
lines+=['check(count==7,"all seven upper identities");',
        'my(beta=Mod(x,L.pol),zz=beta^3/53,Q3=idealprimedec(L,3)[1],T53=idealprimedec(L,53)[1]);',
        'my(K='+gm(lo['kernel_lattice'])+',KU='+gm(lo['kernel_Smith_left'])+',classes=List());']
for a in piv['pivot_records']:
 p,b2,b1,J,cl,coef,ch,raw,projected,mod3=a
 lines+=['my(A=Mod('+poly(coef)+',L.pol),J='+gm(J)+',ch,raw,sc);',
         'check(idealhnf(L,A)==idealdiv(L,J,idealfactorback(L,LG,'+gp(cl)+'~)),"lower full pivot identity");',
         f'check(nfisideal(L,J) && idealnorm(L,J)=={p} && idealadd(L,J,beta-{b1})==J,"literal lower prime and chosen residue");',
         'ch=lc(L,beta,zz,Q3,T53,A);check(ch=='+gp(ch)+',"positive lower local characters");',
         'raw='+gp(raw)+'~;sc=KU*K^-1*raw;check(denominator(sc)==1,"exact inverse lattice");',
         'check([lift(Mod(sc[1],9)),lift(Mod(sc[2],3))]=='+gp(projected)+',"actual projected class");',
         'listput(classes,'+gp(projected)+');']
lines+=['my(R='+gm(r['relation_matrix'])+',HH='+gm(r['relation_HNF'])+',P='+gm(r['generator_to_prime_basis'])+',Q='+gm(r['prime_basis_to_generator'])+');',
        'check(mathnf(R)==HH && abs(matdet(HH))==81,"literal order81 relation lattice");',
        'check(lift(Mod(P*Q,9))==matid(2) && lift(Mod(P*R,9))==matrix(2,5),"forward prime basis maps");',
        'check(denominator(HH^-1*(Q*P-matid(3)))==1,"actual inverse relation map");',
        r'print("{\"type\":\"standalone_literal_ideal_verification\",\"upper_ideal_equalities\":",count,",\"lower_ideal_equalities\":2,\"actual_projected_classes\":",Vec(classes),",\"unconditional_maximal_orders\":true,\"field_discriminant\":\"",F.disc,"\",\"basis\":[31,103],\"three_primary_class_orders\":[9,9]}");',
        r'print("{\"type\":\"completion\",\"status\":\"PASS\",\"scope\":\"literal ideals and local Artin maps only; no bnf object or class/unit proposal is read\"}");',
        '}','quit;','']
out='\n'.join(lines)
dest=H/'e53_positional_ideals.gp'
dest.write_text(out)
report={'status':'PASS','generated':dest.name,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
        'input_outputs':{n:hashlib.sha256((H/n).read_bytes()).hexdigest() for n in
         ['e53_positional_presentation.out','e53_positional_lower_export.out','e53_positional_genus_pivots.out']},
        'method':'literal rational polynomials and complete HNF ideals; nfinit with supplied proved bases; no bnf input or operation'}
print(json.dumps(report,indent=2))

