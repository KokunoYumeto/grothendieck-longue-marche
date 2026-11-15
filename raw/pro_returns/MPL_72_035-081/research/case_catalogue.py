#!/usr/bin/env python3
"""Inventory explicit prose lists and case partitions, separately from polynomial tables.
The row count counts written alternatives/labels, including a separately stated fourth
condition; it makes no assertion that a criterion is valid. Mathematical indexed totals
are computed from n. Sources are the frozen TeX fragments, never images or OCR.
"""
from pathlib import Path
import json,csv
ROOT=Path(__file__).resolve().parent
rows=[
 ('P01','036','three local smoothness equivalences','adjacent triples and pairs','3','all live'),
 ('P02','036','three grouped invertibility hypotheses','beta list; 2(alpha_i-1+alpha_i); two adjacent alpha-2 values','3','all live'),
 ('P03','038','parameter families','mu_0,...,mu_n; beta_0,...,beta_n-1','2*n+1','two families, cardinality shown'),
 ('P04','039','two linear actions','E and E-prime','2','two written tensor formulas'),
 ('P05','041','even-dimensional invariance conditions','a,b,c; additional local d','4','three core labels plus d'),
 ('P06','042','odd-dimensional invariance conditions','a,b,c,d','4','coefficient condition a has two equations'),
 ('P07','042','coefficient-vanishing specializations','2 invertible; 2=0','2','NB case split'),
 ('P08','043','n=1 numbered cases','1: antipodism; 2: invariance','2','case2 has four lettered conditions'),
 ('P09','043','n=1 invariance subconditions','a,b,c,d','4','live'),
 ('P10','043','proposition numbered assertions','1 and2','2','assertion2 has a,b,c,d'),
 ('P11','043','proposition invariance subconditions','a,b,c,d','4','d question-marked'),
 ('P12','045','normalizing characterization of f','a,b,c','3','all live'),
 ('P13','045','isotropic vertices and edge basis','s_0,...,s_n+1; a_0,...,a_n','2*n+3','two indexed families'),
 ('P14','053','discriminants','delta_E,delta_V,delta_E-prime,delta_V-prime','4','two pairs'),
 ('P15','053','smoothness and biregularity conditions','f_E; f_V; pair(E,V,f)','3','each carries its written qualifications'),
 ('P16','054','parity cases for binary restriction','1: n even; 2: n odd','2','odd case continues055'),
 ('P17','055','coefficient-ring cases','A:2 invertible; B:2=0','2','odd-dimensional continuation'),
 ('P18','073','dual-vector boundary/interior rows','a_0-vee; a_i-vee; a_n-vee','3','interior row indexed1..n-1'),
 ('P19','073','pinning equations','tau_i(s0)=s0 for1..n; tau_0(s0)=s0+a0','n+1','repeated pairing equivalents not extra equations'),
 ('P20','073','normalized quadratic coefficient families','diagonal; nonadjacent; adjacent','3','all live'),
 ('P21','074','numbered linear conditions','1,2,3 and struck4','4','3 live numbered conditions and1 cancelled draft'),
 ('P22','074','pinning descriptions','base ofD0; base ofL0-prime; propagateda_i,a_i-prime','3','three consecutive descriptions'),
 ('P23','075','radius cases','n even; n odd','2','sigma-prime means parity-normalized polynomial here'),
 ('P24','075','orthogonal conditions referenced','1,2,3; deleted4','4','three referenced conditions and cancelled fourth'),
 ('P25','076','projective conditions','1,2,3 and deleted4','4','three live and one cancelled'),
 ('P26','076','dimension qualifications','n>=2; n=1 margin caveat','2','n=1 clause partially doubtful'),
 ('P27','077','objects in the asserted equivalence','C; Q_C; phi_G^C','3','three components of one triple'),
 ('P28','080','classification alternatives','a:four universal spaces; b:two spaces per zero beta','4+2*z','candidate total before coincidences'),
 ('P29','081','corollary lettered items','a,b,c,d','4','d has an earlier cancelled version'),
 ('P30','081','coincidence scalar conditions','mu_i; left beta when present; right beta when present','1+int(i>0)+int(i<n)','endpoint-truncated list'),
 ('P31','081','reflection-characteristic branches','char!=2; char=2','2','criterion is checked separately in invariant_subspaces.py'),
]
fields=['id','scan','enumerates','parameters','total_expression','state']
with ROOT.joinpath('case_catalogue.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(fields);w.writerows(rows)
formulas={
 '2*n+1':lambda n:2*n+1,'2*n+3':lambda n:2*n+3,'n+1':lambda n:n+1,
}
result={'catalogue_rows':len(rows),'fixed_total_rows':{},'indexed_examples':{}}
for id,scan,what,params,total,state in rows:
 if total.isdigit():result['fixed_total_rows'][id]=int(total)
 elif total in formulas:result['indexed_examples'][id]=[{'n':n,'total':formulas[total](n)} for n in range(1,7)]
 elif total=='4+2*z':result['indexed_examples'][id]=[{'n':n,'z':z,'candidate_total_before_coincidences':4+2*z} for n in range(1,7) for z in range(n+1)]
 else:result['indexed_examples'][id]=[{'n':n,'i':i,'scalar_conditions':1+int(i>0)+int(i<n)} for n in range(1,7) for i in range(n+1)]
ROOT.joinpath('case_catalogue_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'catalogue_rows':len(rows),'outputs':['case_catalogue.csv','case_catalogue_results.json']}))
