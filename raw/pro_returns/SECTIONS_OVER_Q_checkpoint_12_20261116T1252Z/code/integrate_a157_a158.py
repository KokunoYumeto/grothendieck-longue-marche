#!/usr/bin/env python3
"""Integrate the whole-class metabelian exclusion and sharp finite-depth test."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
records={
 'A.157':{
  'file':'harmonic_metabelian_class_obstruction.tex',
  'answers':'A5; A10; A15; L7; L10; L14',
  'depends_on':'A.139 literal degree-eight harmonic cover; A.141 boundary meridians; A.150 proper Prym map; A.152 dyadic injection and fibres; A.154 exact rank/Sha and finite-to-continuous comparison; integral Schreier presentation and actual finite-sheet lifts',
  'uses_local_theorem':'no; the quotient sections are assumed to match actual ordinary or cuspidal local sections',
  'manuscript_passages':'cote149; scans56–58; actual metabelian quotient, local lifts and full section comparison',
  'notes':'The arithmetic-normal kernel N is the kernel of the proper abelian pro2 quotient of the actual index8 geometric cover subgroup. Its quotient is exactly R⋊C8, R=Z2[V]/(V6+V4+V2+1), with original generators x=(1,v²),y=(0,v). The fixed combined mod8 class produces an actual fixed sheet and lift to E_D/N; all ordinary and cusp local lifts are proved on actual point/decomposition groups, including the real place. The Prym map then gives the exact A154 Selmer inverse system, excluding any ordinary dyadic localization. This excludes every ordinary completed pair in that combined class from locally matching full and pro2 metabelian sections, without nine prescribed local centres. Proper D(K) and D(Q) are exactly the four rational boundary points. The m=1 finite reduction is literally the order512 A141 quotient.',
  'detail':'A.157 removes the nine-centre restriction: every ordinary completed pair in the fixed combined mod8 class is excluded from locally matching full and pro2 metabelian sections through an explicit proper-homology quotient.'},
 'A.158':{
  'file':'harmonic_prym_finite_depth.tex',
  'answers':'A5; A10; A15; L7; L10; L14',
  'depends_on':'A.152 exact doubling bounds and torsion fibres; A.154 exact full2-primary Sha; A.157 integral geometric quotient; finite multiplication Kummer sequences; explicit cyclotomic fibre-product ring',
  'uses_local_theorem':'no; finite quotient local matching is specified',
  'manuscript_passages':'cote149; scans56–58; finite nilpotent comparisons retaining the actual local point',
  'notes':'For every n>=1 the image Sel(2^(n+1))→Sel(2^n) is exactly the two global torsion Kummer classes. For an ordinary dyadic source point, r=v_sqrt2(x(q_+P))=2v_sqrt2(W)−v_sqrt2(T) must satisfy r<=2−4n or r>=4n. The least excluded depth is n=1+floor(max(r,2−r)/4). Its actual tripod quotient Q_(n+1) has order2^(6n+9) and exact class4n+6. The all-m exact class4m+2 follows from the literal fibre-product embedding Z2[V]/((V²+1)(V4+1)) into Z2[i] and Z2[zeta8] over F2[delta]/delta². Every arithmetic subgroup/proper map is specified. Hensel ordinary points near all four boundary fibres show the nonuniformity of the stated elliptic finite Kummer test. Root and peer full proof audits plus exact certificate reruns passed.',
  'detail':'A.158 gives each ordinary dyadic point an explicit finite detecting level; the actual quotient has order2^(6n+9) and exact nilpotency class4n+6, with n determined by its Prym coordinate valuation.'}
}
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/two_inert_norm2_generator_agent.tex}'
assert anchor in s
entries='\n'.join(r'\input{sections/'+r['file']+'}' for r in records.values())
if all(r['file'] not in s for r in records.values()):s=s.replace(anchor,anchor+'\n'+entries,1)
else:assert all(r['file'] in s for r in records.values())
p.write_text(s)
p=w/'notes/register_metadata.json';m=json.loads(p.read_text())
for ident,rec in records.items():m[ident]={k:v for k,v in rec.items() if k not in {'file','detail'}}
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)!=3:continue
 for ident,rec in records.items():
  if cells[0] in {x.strip() for x in rec['answers'].split(';')}:
   if ident not in cells[1]:cells[1]+=', '+ident
   if rec['detail'] not in cells[2]:cells[2]+=' '+rec['detail']
 lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: the whole Kummer class and sharp finite nilpotent levels'
if heading not in lines:lines.extend(['',heading,'',stamp+': '+records['A.157']['detail']+' '+records['A.158']['detail'],'',
 'The proper homology of the actual eight-sheeted cover is computed integrally. In the Schreier basis u_j and z, the boundary vectors kill z and the even and odd sums. This gives the literal free rank-six module R=Z2[V]/(V6+V4+V2+1), with an order-eight lift of the deck generator. The arithmetic action preserves the boundary kernel. A fixed sheet of the twisted mu8 torsor places the section in the actual cover subgroup, and every ordinary/cuspidal local matching lifts through its point or decomposition group. The exact Prym calculation applies to this smaller pro2 metabelian quotient, excluding ordinary dyadic matching throughout the combined class. No global cuspidality conclusion from a single local cusp is asserted.',
 'The finite refinement uses the exact Selmer transition, whose image consists of the two rational torsion classes at every power of two. Translation by(0,0) replaces x by b/x, giving the two exact valuation ranges. For r=2v_pi(W)−v_pi(T), the first excluded n is1+floor(max(r,2−r)/4). The proper homology quotient modulo2^(n+1) has order2^(6n+9). Its exact nilpotency class4n+6 is proved at every depth: in the fibre product Z2[i]×_(F2[delta]/delta²)Z2[zeta8], delta^(4m+2)/2^m satisfies the gluing condition and delta^(4m+1)/2^m fails it. This proves the exact lower-central termination. Actual Hensel points approaching all four boundary points verify why the displayed elliptic test has no uniform depth over all ordinary local points.',''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+' A157/A158 root audits PASS. Actual integral meridian/Schreier maps, arithmetic normality, twisted fixed-sheet lift and all-place point/cusp comparisons checked. Sharp nilpotency class4m+2 proved by the exact cyclotomic fibre-product ring, with both membership and nonmembership. Finite Selmer transition, local torsion translation, scaling, least valuation threshold, and actual arithmetic quotient maps checked. Independent certificate reruns passed; peer reviews accepted.\n'
for name in ['notes/hour11_root_audits.md','notes/root_progress.md']:
 with(w/name).open('a')as f:f.write('\n'+audit)
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,capture_output=True,text=True)
out='Integrated audited A157 and A158.\n'+r.stdout
Path(__file__).with_name('integrate_a157_a158_output.txt').write_text(out);print(out,end='')
