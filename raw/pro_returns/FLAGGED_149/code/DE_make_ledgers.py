#!/usr/bin/env python3
from pathlib import Path
import re,json
base=Path(__file__).resolve().parents[1]
tex=(base/'sections/DE_agent.tex').read_text()+(base/'sections/DE_Z_agent.tex').read_text()
pat=re.compile(r'\\begin\{result\}\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}(.*?)\\end\{result\}',re.S)
deps={
'D1':'Stacks 58.21.4','D2':'valuation-ring axioms; fundamental inequality','D3':'fundamental inequality; explicit norms','D4':'Temkin 3.4.4,3.5.3; Kuhlmann 2.9; HJP 7.3(a)',
'D5':'D4; Kuhlmann 9.44,9.45','D6':'D3,D5','D7':'D3,D4; C2,C3; Hoshi 2.8','D8':'valuation-ring axioms','D9':'attached return B6-B8,C6','D10':'D4,D5; Kuhlmann 9.45',
'E1':'D1,D4; C2,C3; Hoshi 2.4(i); A4 peripheral theorem','E2':'E1; C1; explicit blow-up coordinates','E3':'D3,D4; E1; character duality','E4':'E1; Borne-Emsalem-Stix Proposition8 proof, Proposition16 proof','E5':'E2,E4; explicit blow-up normal bundles','E6':'E3; explicit norm construction',
'ZD1':'finite-etale Galois category','ZD2':'ZD1; E4; Borne-Emsalem-Stix Remark9','ZD3':'D1,D7','ZD4':'D2,D4; common-model construction','ZD5':'D3,D4,D5; point-section injectivity B2','ZD6':'D4,D9','ZD7':'D3,E2,E3,ZD5','ZD8':'explicit boundary graphs; tubular-neighborhood topology','ZD9':'E1,E4; A4 distinct cusp theorem','ZD10':'D4,ZD3; Borne-Emsalem-Stix Theorem27; attached return','ZD11':'D4; Bresciani TheoremsA,B'}
notes={
'D4':'Correct primewise ranks are dim_F_l Gamma/lGamma; rational rank alone is insufficient.',
'D5':'Actual subgroup equality with compatible prolongations; removes largest divisible convex subgroup.',
'D10':'Includes normalizer in arithmetic group and geometric decomposition subgroup normalizer.',
'E1':'The whole-local-group equivalence needs finite residue over K; nonclosed-point counterexample supplied.',
'E2':'Terminality is among smooth proper SNC compactifications of a product of two hyperbolic curves.',
'E3':'Exact dual saturation criterion; includes divisible groups and nondivisorial DVRs.',
'E4':'Finite-cover/nth-root criterion avoids assuming profinite completion preserves arbitrary exact sequences.',
'E5':'Threefold blow-up gives complete open stratum P1 with normal degrees (1,-1).',
'E6':'DVR with residue union Q(sqrt p_i), algebraic infinite; arithmetic openness corrected.',
'ZD4':'Finite-union sentence is refuted; nonscheme and divisorial claims proved without resolution.',
'ZD5':'Counterexample retains nonzero inertia and rational residue; uniqueness false.',
'ZD6':'Unrestricted subgroup reading refuted; cyclotomic-kernel qualification essential.',
'ZD10':'UNRESOLVED. Exact pullback extension and failed normalizer/abelianization attacks recorded; smallest case Q and U03.',
'ZD11':'Proved equivalence locates universal lifting at the full section conjecture; does not prove either conjectural assertion.'}
results=[]
for m in pat.finditer(tex):
    ident,status,title,body=m.groups()
    passage=re.search(r'\\par\\emph\{Passages?:\}(.*)',body,re.S)
    statement=body[:passage.start()] if passage else body
    results.append({'id':ident,'statement':title+' — '+re.sub(r'\s+',' ',statement).strip(),
                    'status':status,'where_proved':'FLAGGED_149_paper.tex, statement '+ident,
                    'depends_on':deps.get(ident,''),
                    'manuscript_passages':re.sub(r'\s+',' ',passage.group(1)).strip() if passage else '',
                    'depends_on_doubtful_reading':'See DE_readings.json; theorems state exact data independently of transcription.',
                    'notes':notes.get(ident,'')})
(base/'DE_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')

file='MPL_149_091-136_transcription.tex'
data=[
(105,'E_A^{tilde A}=E_X^{tilde X|X}','The pointed group is relative to the universal cover tilde X; replacing it by X omits that datum.','Mathematically strong; scan105 not supplied.'),
(106,'E_{alpha|X}^Omega in (4)','The comparison is between two fiber functors on X, so subscript X is required; the canonical bijection uses the chosen algebraic closure inside Omega.','Mathematically strong; scan106 not supplied.'),
(107,'B_{pi(X)} for finite etale covers of Y','The relevant Galois topos is B pi1(Y); Z supplies a fiber functor as proved in ZD1.','Mathematically strong; scan107 not supplied.'),
(109,'T|Z, relative group definition','Either letter works if it denotes the same connected simply connected Y-scheme; no mathematical preference.','No disambiguation.'),
(110,'suite exacte d’homotopie universelle; isomorphism (12)','The claimed identification requires injective fiber pi1, not only exactness pi1(fiber)→pi1(total)→pi1(base)→1. ZD2 gives the exact missing map and O(-1) counterexample.','Mathematically decisive about the hypothesis; not a paleographic resolution.'),
(112,'(19), ordinary geometric fiber versus pro-cover fiber','Formula(18) computes a connected pullback of the universal pro-cover unconditionally; formula(19) for an ordinary fiber needs left injectivity.','Strong mathematical distinction via the actual comparison map; scan112 unavailable.'),
(117,'L_{x_i’}|I_{x_i’} in (23)','The normal closure is generated by inertia images I; a mere notation L for those same inertia groups is harmless. ZD3 proves it.','Mathematical identification; no letter judgment.'),
(118,'N_{x’}/I_{x’} ≃ k(x’) in (26)','The quotient is the absolute Galois group G_{k(x)}, not the residue field itself; D4 constructs reduction.','Mathematically decisive; scan118 unavailable.'),
(118,'T_0|T_infty in (27)','For residue characteristic zero the full inertia is T_infty=hat Z(1); positive residue characteristic requires a tame quotient.','Mathematically strong; scan118 unavailable.'),
(119,'target E_{overline{k(x)}}|E_{k(x)}^{overline{k(x)}} in (30)','Reduction has target Gal(overline{k(x)}/k(x)); the latter reading is mathematically required.','Visual inspection supports the residue Galois group; not declared a settled transcription.'),
(120,'elementary factors not (0,0) nor (0,1)','DVR criterion valid with both exclusions; arbitrary-valuation extension fails even for U03 squared.','Scan120 visually inspected: its margin visibly excludes (0,0) and (0,1). This agrees with the exact curve hypotheses of D7.'),
(122,'ess.|ext. de type fini; only generic/divisorial noetherian points','Essentially finite type is the divisorial condition. The separate noetherian exhaustion is false by D2 and E6.','Scan122 visually inspected; counterexample cannot repair its wording.'),
(123,'pas stables par réunions finies','The model-associated opens are stable under finite unions on a common proper model; ZD4 refutes the written negation.','Scan123 visually inspected: the parenthesis does say pas stables par réunions finies. Its negation is retained and refuted, not silently removed.'),
(124,'codimension alpha; inserted fini algébrique','Inertia ranks are prime-dependent dim Gamma/lGamma. Algebraic residue need not be finite. E6 shows fini is an additional assumption.','Scan124 visually inspected; both claims corrected mathematically, not silently edited.'),
(126,'fraction field of V intersect L1','D8 proves the fraction field is L1 for either ordinary subextension reading; no dependence on the doubtful superscript on scan125.','Scan126 visually inspected: V1 differs from L1 and the decomposition/inertia restriction arrows are visible. D8 proves their actual maps.'),
(127,'L in (32),(33), versus proposed U correction','Both visible subscripts are L. D9 refutes that assertion and proves its quotient-U replacement using the actual quotient homomorphism.','Scan127 visually inspected and supports L; retained as written.'),
(127,'subgroups of N_V^0 versus all subgroups with open residue image','The broad latter version fails by cyclotomic action (ZD6); retaining N_V^0 is necessary even for inertia to centralize the subgroup.','Mathematical evidence; the compressed margin is not silently normalized.'),
(129,'henselian generic|geometric point','The source is the generic point of the henselized valuation trait; geometric points specify the group maps.','Mathematically strong; scan129 unavailable.'),
(130,'I_x=E_{tilde U_x/K}; equivalence with full injectivity','I_x is the kernel over G_k(x). It equals the kernel over G_K only when the residue Galois map is injective, in particular for a closed point. E1 supplies counterexample for generic boundary point.','Scan130 visually inspected; exact groups distinguish the alternatives.'),
(130,'open image; perhaps surjective; inserted finite residue','E3 gives the exact dual saturation criterion; E6 separately requires finite residue degree for arithmetic openness.','Scan130 visually inspected; original algebraic wording insufficient.'),
(131,'Delta_x|bar Delta_x subset pi_{L/K}|pi_{U/K}','The image of local meridians lies in pi_{U/K}; E1/E3 define this target. The assertions about nontriviality for arbitrary valuations fail by D3.','Scan131 visually inspected: the displayed subscript supports L/K. The actual quotient map to pi_{U/K} supplies the corrected mathematical target; the manuscript is not silently changed.'),
(132,'D_J open stratum versus closed intersection; =|supseteq','Exact J labels the open stratum; superset J labels the closed intersection. E4 must use the open stratum to have exactly |J| torus factors.','Mathematically decisive; scan132 unavailable.'),
(133,'T^J|bar T^J and hookrightarrow|rightarrow in (37)','Domain is the Tate module product T^J. General arrow is not injective; E5 gives kernel antidiagonal T.','Scan133 visually inspected; mathematical evidence supports retaining a general arrow.'),
(133,'D_J infinity-connected; incidence complex equals end homotopy type','Even point strata on P1 minus three points leave circle fibers. ZD8 refutes the proposed inference and proves the intrinsic end pro-system comparison.','Scan133 visually inspected; does not settle the infinity symbol.'),
(134,'pi2(bar D_J)|pi2(D_J) boundary','The relevant base is the chosen open stratum over the geometric field; its Chern evaluation is E4. E5 uses a stratum already complete so either notation yields the same counterexample.','Scan134 visually inspected; no silent choice.'),
(135,'pi|E_{U/K} in (39)','The image is in the geometric kernel pi_{U/K}; conjugacy along a geometric connected component is ZD9.','Scan135 visually inspected: the formula supports pi_{U/K}; its opening admission of extension (37) is exactly the assertion refuted in E5.'),
(136,'full arithmetic invariance of each branch homomorphism','Canonical action fixes a branch only over its Galois stabilizer; full G_K permutes geometric components. ZD9 gives Q(sqrt2) counterexample.','Mathematically decisive; scan136 image not attached.'),
]
readings=[{'file':file,'scan':scan,'the_unsure_or_illegible_place':place,'what_the_mathematics_supports':support,'how_strongly':strength} for scan,place,support,strength in data]
(base/'DE_readings.json').write_text(json.dumps(readings,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'statements':len(results),'readings':len(readings),'open':[r['id'] for r in results if r['status']=='Open']},indent=2))

def integers(spec):
    out=[]
    for part in spec.split(','):
        bounds=re.findall(r'\d+',part)
        if len(bounds)==1:
            out.append(int(bounds[0]))
        elif len(bounds)==2:
            out.extend(range(int(bounds[0]),int(bounds[1])+1))
        else:
            raise ValueError(spec)
    return out

coverage=[]
for line in (base/'DE_report.md').read_text().splitlines():
    if not re.match(r'^\| (?:F\d+|ZD\d+) \|',line):
        continue
    row,location,words,verdict,statements,source=[s.strip() for s in line.strip('|').split('|')]
    section,pages,scans=location.split(';')
    coverage.append({'id':row,'row':row,'section':section,
        'scan':'149 '+location,'scans':integers(scans),
        'manuscript_pages':integers(pages),
        'words':words,'verdict':verdict,'statements':statements,
        'source_opened':source})
assert len(coverage)==20
(base/'DE_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'coverage_rows':len(coverage),'coverage_file':str(base/'DE_coverage.json')},indent=2))
