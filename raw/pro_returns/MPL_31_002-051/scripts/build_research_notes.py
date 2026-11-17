#!/usr/bin/env python3
"""Build the root-authored notes, executing an actual rg context search per item.
Reads but never writes frozen transcription files. Requires the supplied context
archive to have been opened after the freeze, at ../../context from this script.
"""
from pathlib import Path
import datetime, hashlib, json, re, subprocess, sys

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parent
CONTEXT=ROOT/'context'
PREFIX='MPL_31_002-051'
BT=chr(96)
def code(s): return BT+s+BT
def utc(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def esc(s): return str(s).replace('|','&#124;').replace('\n',' ')
def frozen_check():
    manifest=json.loads((BASE/'records/frozen_sha256.json').read_text())
    bad=[p for p,h in manifest['files'].items() if hashlib.sha256((BASE/p).read_bytes()).hexdigest()!=h]
    if bad: raise RuntimeError('Frozen hash mismatch: '+repr(bad))
    return manifest
manifest=frozen_check()
items=[]
def add(id,section,title,locs,kind,quote,query,analysis,context,ids,refs=None,confidence=None,reason=None,flags=None):
    assert id not in [x['id'] for x in items], id
    if kind=='own idea':
        assert confidence and reason and '?' in analysis,id
    items.append(dict(id=id,section=section,title=title,locations=[{'file':'31.pdf','scan':s,'fragment_line':l} for s,l in locs],kind=kind,quote=quote,object_query=query,analysis=analysis,context_comparison=context,context_ids=ids,primary_refs=refs or [],confidence=confidence,reason=reason,flags=flags or []))
for p in sorted((BASE/'scripts/research').glob('0[1-5]_*.py')):
    exec(compile(p.read_text(),str(p),'exec'),{'add':add})

# Local editorial refinements to root-authored notes only.
byid={x['id']:x for x in items}
byid['N006']['flags']=['self','withdrawn']
byid['N091']['flags']=['self']
byid['N075']['context_comparison']=byid['N075']['context_comparison'].replace('a different specified residue complex','a specified residue complex')

# Two independently written questions on the cancelled idèle leaf.
byid['N071']['title']='The first cancelled idèle quotient question'
byid['N071']['locations']=[{'file':'31.pdf','scan':45,'fragment_line':9}]
byid['N071']['quote']='“ou un quotient ???”'
byid['N071']['analysis']=r'''The first explicit quotient question accompanies the cancelled sequence involving \(Z_2^{r_1}\), \(G_k^0\), and \(U_k^0/\operatorname{Im}E\). Which image of global units in the stated finite idèle-unit group is being factored out, and which map from the real-place factor provides the kernel of the resulting Galois-group map?'''
new=dict(byid['N071'])
new.update(id='N071b',title='The cancelled real-place factor question',locations=[{'file':'31.pdf','scan':45,'fragment_line':25}],quote=r'“ceci est-il \unsure{identique} à \(Z_2^{S^\infty}\) ???”',object_query=r'real|réel|id[èe]le|quotient|unramified|ramif',analysis=r'''The second question asks whether the quotient of \(Z_2^{S^\infty}\) by the displayed intersection of global-unit images is identical to the unquotiented factor. The map to determine is the composite from those global units into the real-place sign group, together with the intersection taken in the cancelled formula; the retained text leaves that computation open.''')
idx=items.index(byid['N071']);items.insert(idx+1,new)
byid={x['id']:x for x in items}


# Reviewed wording and explicitly bounded concrete calculations.
byid['N010']['analysis']=byid['N010']['analysis'].replace(
    'SGA 3 IX §5.1 is the close printed comparator [P03];',
    r'SGA 3 IX §5.1 is the close printed comparator [P03], phrasing centrality on \(u_s\) under the base-change map \(u\mapsto u_s\), where the scan writes \(u\) central;')
byid['N036']['analysis']=byid['N036']['analysis'].replace(
    r'\(\operatorname{Frac}(A)\to\operatorname{Frac}(A^h)\), retaining their dimensions and residue fields',
    r'\(\operatorname{Frac}(A)\to Q(A^h)\), with \(Q\) denoting the total ring of fractions, before choosing a component and comparing dimensions and residue fields')
byid['N038']['analysis']+=r' Does stability under finite products here include the fiber products \(U_i\times_SU_j=(U_i\times U_j)\times_{S\times S}S\) used in those Čech complexes?'
for id in ['N027','N028','N029','N032','N034','N035','N037']:
    byid[id]['object_query']+='|orderab'
reasons={
'N022':'Explicit free resolution and cohomology calculation; undefined historical terminology',
'N025':'Triangular relation computation; remaining comparison of the pushout identifications',
'N029':'Square identities preserved by every unital field embedding into the real numbers',
'N030':'A quadratic with no F3 root, its nonzero derivative, and its nontrivial finite étale torsor',
'N033':'Cyclic degree-p constant-field extensions and the verified characteristic-p upper bound',
'N037':'Explicit kernel, fraction field, residue field and quadratic character; cited upper bound',
'N043':'Written edge map; earlier complexes unavailable beyond excerpts',
'N053':'Written completion map for F=G; earlier projectors and their geometric realizations unavailable',
'N057':'Explicit translation action, closed-edge intersection and quotient; unresolved source convention',
'N060':'Explicit bar-construction faces and stabilizers; missing continuous section comparison and arithmetic marking',
'N063':'Direct trace and Tate-quotient calculation; earlier pairing available only as an uncertain excerpt',
'N073':'Explicit field extension and formal power-series roots; undefined local-field convention on the leaf',
'N080':'Polynomial inverse and additivity identities; comparison of coordinate-polynomial degrees',
'N082':'Displayed regular-norm matrix and one-dimensional constant F2 Galois module',
'N083':'Block determinant and injective first coordinate; unfinished continuation in the source',
'N089':'Explicit quadratic quotient, continuous cocycle and two coboundary calculations'
}
for id,reason in reasons.items():byid[id]['reason']=reason


# Registry metadata is derived from exactly the supplied RESULTS_STATE excerpt.
rs_path=CONTEXT/'notes/RESULTS_STATE.md'
rs_lines=rs_path.read_text().splitlines()
registry={}
for lineno,line in enumerate(rs_lines,1):
    if lineno>=61 or not line.startswith('- **'): continue
    rawid=line.split('**')[1]
    id=('Hua, findings register, '+rawid) if rawid=='31-local-ring-cd-lower-bound' else rawid
    sm=re.search(r'\[([^\]]*)\]',line)
    fm=re.search(r'\(([^()]*(?:\.md|\.csv))\)\s*$',line)
    registry[id]={'id':id,'search_key':rawid,'context_file':'notes/RESULTS_STATE.md','line':lineno,'status':sm.group(1) if sm else 'status in supplied prose','source_file':fm.group(1) if fm else 'Hua findings register; no full external register supplied','excerpt':line[:400],'note_ids':[]}
assert len(registry)==26,len(registry)

prior_locs={
'LM7 E.23':'§51.16; folios 733v–736v; scans 172–178; equations (369)–(379)',
'LM7_PUSH C.6':'C.3; no manuscript scan given in the excerpt',
'INTAKE LM7_CONTINUED §?':'Part E/E.37; no additional manuscript scan in the excerpt',
'MPL_33_147-181+34_002-017 D21':'33.pdf, scan166, approximate lines6–18',
'MPL_11_043-058+56 N045':'56.pdf, scan020, middle table and annotation',
'MPL_131 RN001':'131.pdf, scan002, fragment L13; scan017, fragment L25',
'MPL_60_002-035 §2':'60.pdf, scans003–035, described as a range',
'MPL_60_002-035 C07':'60.pdf, scans002–035; CT44 scans002,004,008–009',
'MPL_60_002-035 F48':'60.pdf, scan035, overwritten lower margin',
'MPL_60_036-070 §2':'60.pdf, scans037–047 and049–059; boundary061; later norm locator truncated',
'MPL_91_099-143 §68':'91.pdf, title124; thickness126,128; point/image locator truncated',
'WG H9':'cote44, Th.4/Th.5; scan locator omitted',
'WG2 §2.1 #2':'cotes16,54,37; one title has manuscript pp.1–16, scans3–18; the excerpt does not explicitly assign its cote',
'Hua, findings register, 31-local-ring-cd-lower-bound':'their p.22 = supplied 31.pdf scan023'
}
dispositions={
'LM7 E.23':'The quotient/path map and the explicit abstract bar-construction question are recorded under this open ID; no continuous arithmetic section map or its fibers are computed here.',
'LM7_PUSH C.6':'Its claimed class-two germ classification is not re-derived; the supplied excerpt does not identify its residue complex with any displayed complex on these scans.',
'INTAKE LM7_CONTINUED §?':'The N/γ3N quotient supplies the exact input to N060; the excerpt’s correction/convergence criterion remains attributed to the intake reading, with no referee promotion.',
'MPL_33_002-049 §96':'An earlier accounting entry reporting29 entries; used only as a reporting lead, and its full source is unavailable.',
'MPL_33_147-181+34_002-017 §123':'An earlier accounting entry reporting44 entries; the present table accounts for the26 substantive selected entries actually supplied here.',
'MPL_131 10':'The reused SGA3 passages and the nonproper Hilbert/Picard programme supply concrete descent and representability maps relevant to this planning-placement lead.',
'MPL_33_002-049 §2':'The S19 comparison programme gains the printed locators indexed below and the current package’s identified subject layers.',
'MPL_33_147-181+34_002-017 11':'A bibliography/method lead; this return independently records the primary passages actually retrieved after its own freeze.',
'MPL_106+107 §136':'A register-accounting excerpt naming BISITE and RESIDUE; N043 asks for an actual chain map before any cohomological-descent identification.',
'MPL_33_147-181+34_002-017 8.3':'An earlier pagination-accounting lead; T01–T07 and the numeral table add the independently observed inscriptions in cote31.',
'MPL_33_147-181+34_002-017 D21':'The Cartan edge maps and the real-analytic quotient comparison give precise objects for its analytic/cohomological-descent programme.',
'MPL_60_002-035 §2':'The trace and local-norm maps provide comparisons to pursue with its local-symbol/L-function programme; its determinant and boundary constructions are not supplied here.',
'MPL_11_043-058+56 N045':'The earlier norm-2 target is uncertain in its own excerpt; N063 supplies a concrete trace-two calculation and asks for the missing coefficient/chain map.',
'MPL_11_043-058+56 §117':'A primary-reference-method lead; N048 gives a newly checked EGA erratum for the current package.',
'MPL_131 RN001':'The explicit completion, Hom, rigidity and GL(n) descent maps add concrete comparisons to the construction-techniques lead at131/002 and017.',
'MPL_131 §2':'The Murre/SGA3 comparison lead receives exact current scans and printed SGA3 destinations; the earlier full claims are unavailable.',
'MPL_142_001-093 §316':'A bibliography/verification-limit lead concerning SGA1; it supplies no earlier path formula or manuscript scan for the questions here.',
'MPL_14_002-044 §107':'Its effectivity lead is connected to completion of covers/line bundles and to the endomorphism map in N053; no projector/cycle identification is asserted.',
'MPL_33_002-049 §93':'A title-inventory lead; the current title and pagination witnesses are independently listed in T01–T07.',
'MPL_60_002-035 C07':'The excerpt’s height programme and cote44 correspondence are not supplied in full; the current norm and completion maps require a specified cycle/pairing morphism before they can test that programme.',
'MPL_60_002-035 F48':'The earlier H²/H⁰ duality reading lacks its full coefficient and pairing data; the inclusion U→Ksep* in N088–N089 supplies a possible coefficient comparison to formulate, with no claimed implication for its ρ+1 annotation.',
'MPL_60_036-070 §2':'The explicit orbit-sum, ring trace, relative trace and norm maps add precise comparison questions to its averaging/norm excerpt.',
'MPL_91_099-143 §68':'N070 identifies a completion/cohomology comparison to put beside its Greenberg point/image lead; the excerpt supplies no connecting morphism.',
'WG H9':'Remains an unchecked cycle-pairing/Lefschetz hunch; N053 specifies the additional cycle-to-endomorphism map needed before testing it by the current completion argument.',
'WG2 §2.1 #2':'Remains an unchecked projector/graded-ring plan; N049 identifies the current associated-graded object, and N053 asks for an explicit realization of the planned projectors.',
'Hua, findings register, 31-local-ring-cd-lower-bound':'The source is headed Corollaire, preserves deleted assumptions and a live question, and has a verified printed comparator in SGA4 X2.4 for its stated scope; the truncated candidate’s broader exceptional/regular cases are not certified.'
}
for id,r in registry.items():
    r['prior_locator']=prior_locs.get(id,'No earlier scan locator is supplied in this excerpt')
    r['disposition']=dispositions[id]

def rg(pattern,fixed=False):
    args=['rg','--json','--line-number','--ignore-case']
    if fixed: args+=['--fixed-strings']
    args+=['--regexp',pattern,str(CONTEXT/'README.md'),str(rs_path)]
    p=subprocess.run(args,text=True,capture_output=True)
    if p.returncode not in (0,1):
        raise RuntimeError('rg failed for '+pattern+': '+p.stderr)
    matches=[]
    for row in p.stdout.splitlines():
        obj=json.loads(row)
        if obj['type']!='match':continue
        d=obj['data'];line=d['lines']['text'].rstrip('\n')
        matches.append({'path':str(Path(d['path']['text']).relative_to(CONTEXT)),'line':d['line_number'],'matched_terms':[z['match']['text'] for z in d['submatches']],'excerpt':line[:300]})
    return {'pattern':pattern,'mode':'literal' if fixed else 'regex','utc':utc(),'command_args':args,'return_code':p.returncode,'matches':matches}

searches=[]
for it in items:
    for loc in it['locations']:
        f=BASE/'pages'/f'{PREFIX}_31_scan{loc["scan"]:03d}.tex'
        assert f.exists(),it['id']
        assert 1<=loc['fragment_line']<=len(f.read_text().splitlines()),it['id']
    sr={'id':'Q-'+it['id'],'item':it['id'],'object_search':rg(it['object_query']),'id_searches':[]}
    for id in it['context_ids']:
        assert id in registry,(it['id'],id)
        registry[id]['note_ids'].append(it['id'])
        sr['id_searches'].append(rg(registry[id]['search_key'],True))
    it['context_search_id']=sr['id']
    searches.append(sr)

coverage_searches=[{'id':'Q-R'+str(i).zfill(2),'context_id':id,'search':rg(r['search_key'],True)} for i,(id,r) in enumerate(registry.items(),1)]
for r in registry.values():r['note_ids']=sorted(set(r['note_ids']))
now=utc()
def write_json(name,obj):
    (BASE/'records'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

sources=[
('P01','M. Artin, SGA 4, Exposé X','https://www.normalesup.org/~forgogozo/SGA4/tomes/tome3.pdf','Recomposed Tome III; X §§2.1–2.4,5.1,6.2. Corollary2.4: original p.50, recomposed p.30, PDF reader36.','All listed passages retrieved and inspected.'),
('P02','J.-L. Verdier, SGA 4, Exposé V','https://www.cmls.polytechnique.fr/perso/orgogozo/SGA4/05/05.pdf','Version2015-04-27; §2.4.5.4, Corollary3.4 and §4.3; PDF reader pp.16,18–20; original marginal pp.24,27,30.','Covering-limit spectral sequence and comparison degree ranges inspected.'),
('P03','A. Grothendieck, SGA 3, Exposé IX','https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp9-8nov09.pdf','Editor-hosted2009-11-08 version; §§5.1–5.3 and5.1bis; printed pp.48–51; original marginal pp.58–61.','Centrality, finite-presentation alternatives, unit locus and subgroup formulation inspected; no attached H/G correction at IX5.2 was located in this version.'),
('P04','A. Grothendieck, SGA 3, Exposé X','https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo10-8nov09.pdf','Editor-hosted2009-11-08 version; §§5.6,5.8–5.16; editorial notes36,43–46; printed pp.83–87.','The editorial qualifications and the original5.15/revised5.14–5.16 relationship were inspected.'),
('P05','A. Grothendieck et al., SGA 2, edited by Y. Laszlo','https://www.cmls.polytechnique.fr/perso/laszlo/sga2/sga2-smf.pdf','Recomposed annotated edition; IX2.1, printed85/original108–109; XII2.2–2.4, printed114–115/original144–145; XII5.10–5.11, printed132–133/original170–171.','Text retrieved; the depth signs in XII2.4 were visually checked by the external-source reader because text extraction renders them misleadingly.'),
('P06','A. Grothendieck, with J. Dieudonné, EGA III, second part','https://wstein.org/sga/circle/EGAIII.2.pdf','Publications mathématiques de l’IHÉS17 (1963),5–91; Errata et addenda, liste2, Err_III24, printed89, PDF reader88.','The three deletions and the added finite-generation hypothesis were checked in the original erratum.'),
('P07','The Stacks Project, Cartan criterion','https://stacks.math.columbia.edu/tag/03F9','Tag03F9, Lemma21.10.9.','The full positive-degree formulation was inspected.'),
('P08','The Stacks Project, covering spectral sequence','https://stacks.math.columbia.edu/tag/03AZ','Tag03AZ, Lemma21.10.6.','The E2 page and the augmentation target were inspected.'),
('P09','The Stacks Project, Tsen’s theorem','https://stacks.math.columbia.edu/tag/03RD','Tag03RD, Theorem59.67.10.','Function-field statement and proof retrieved.'),
('P10','The Stacks Project, Brauer group of a C1 field','https://stacks.math.columbia.edu/tag/03RC','Tag03RC, Theorem59.67.8.','Reduced-norm proof retrieved.'),
('P11','The Stacks Project, Brauer and Galois-cohomology criterion','https://stacks.math.columbia.edu/tag/03R8','Tag03R8, Proposition59.67.4.','Finite-extension hypothesis and ordinary cohomological conclusions inspected.'),
('P12','The Stacks Project, Artin–Schreier sequence','https://stacks.math.columbia.edu/tag/0A3J','Tag0A3J, §59.63; affine lemma: [Tag0A3K](https://stacks.math.columbia.edu/tag/0A3K), Lemma59.63.1.','The exact sequence and affine vanishing statement were retrieved.'),
('P13','J. S. Milne, Algebraic Groups','https://www.jmilne.org/math/Books/iAG2017.pdf','Author-hosted2017 text; Proposition14.54, printed297 (PDF309); Theorem16.13, printed328 (PDF340).','Exponent-p vector groups and perfect-field commutative decomposition inspected.'),
('P14','M. A. Armstrong, On the fundamental group of an orbit space','https://wrap.warwick.ac.uk/id/eprint/74313/1/WRAP_Thesis_Armstrong_1966.pdf','Proceedings of the Cambridge Philosophical Society61 (1965),639–646; reproduced in the1966 thesis, PDF reader pp.5–12; Theorem2,642–643, and Theorem3,646.','Projected-edge-path construction, quotient kernel and subdivision discussion inspected.'),
('P15','M. Eisermann, The fundamental theorem of algebra made effective: An elementary real-algebraic proof via Sturm chains','https://pnp.mathematik.uni-stuttgart.de/igt/eiserm/publications/roots.pdf','Author-hosted preprint compiled2012-04-01; Remark2.4 and Theorem2.5, p.6.','Used only for ordered real closure and positivity-as-square properties; the embedding obstruction in N029 is calculated explicitly.')
]
source_dict={p[0]:dict(id=p[0],title=p[1],url=p[2],locator=p[3],verification=p[4]) for p in sources}
for it in items:
    assert all(k in source_dict for k in it['primary_refs']),it['id']

intro=r'''# MPL_31_002-051 — Research notes

## Evidence, scope, and reading conventions

These notes concern the 46 retained scans of 31.pdf. The transcription was frozen on 16 November 2026 at 23:40:30 UTC; the supplied context was opened at 23:40:37 UTC. Every location below gives the archive file and scan, followed by an approximate locator in its frozen individual LaTeX fragment; these are fragment lines, not claimed original ruled-line numbers. Brief quotations preserve the source wording or explicitly display its uncertainty.

“Unproved claim” describes the evidence in the retained passage: some such claims have printed proofs, while others stop at an outline or a citation. “Self-flagged” identifies the author’s own question or verification marker. “Withdrawn in the same text” records the visible deletion or replacement and its location. Own ideas are posed as questions, with confidence and a reason; their explicit calculations establish only the stated examples or maps.

The supplied context contains exactly README.md and notes/RESULTS_STATE.md. The earlier notes, CSV registers, intake documents, planning files and scans named there were not supplied in full, and several selected entries are visibly truncated. The statuses Open and Proved remain claims of their named returns; an intake reading remains an intake reading, and returned-package notes remain first-pass leads. The referee paragraph lists other specified rows as reviewed; it supplies no such verdict for the selected C.6 or E.23 entries.

Each item has its own executed case-insensitive ripgrep search for objects/notation/words in both supplied context files, plus literal searches for the cited register IDs. Search locators and bounded conclusions appear with the item; the complete patterns, timestamps, exit codes and matched excerpts are in records/context_searches.json and its readable companion. A no-hit statement is limited to those two files. The register-disposition table accounts for all 26 substantive selected entries and explicitly preserves the available earlier scan locators.

The main concrete checks are the real-closure and finite-field tests (N029–N033), the local-ring comparator and explicit real quadric (N034–N037), the revised Cartan degree bounds (N038–N043), the EGA correction and completion maps (N048–N053), the quotient-path and trace constructions (N054–N073), and the norm and coefficient-inclusion tests (N077–N090). Their hypotheses, maps and limits are recorded in the individual items rather than imported into the frozen source.

'''
out=[intro]
search_by_id={s['item']:s for s in searches}
lastsection=None
for it in items:
    if it['section']!=lastsection:
        out.append('## '+it['section']+'\n')
        lastsection=it['section']
    out.append('### '+it['id']+' — '+it['title']+'\n')
    locs='; '.join(f'{l["file"]}, scan {l["scan"]:03d}, fragment ≈L{l["fragment_line"]}' for l in it['locations'])
    out.append('**Source:** '+locs+'  \n**Kind:** '+it['kind']+'  \n**Source words:** '+code(it['quote'])+'\n')
    out.append(it['analysis']+'\n')
    out.append('**Context comparison:** '+it['context_comparison']+'\n')
    s=search_by_id[it['id']]
    refs=sorted(set(f'{m["path"]}:L{m["line"]}' for m in s['object_search']['matches']))
    hitstr=', '.join(refs) if refs else 'No object-query hit in either supplied file.'
    out.append('**Context search '+it['context_search_id']+':** '+code(it['object_query'])+'  \n**Object-query matches:** '+hitstr+'\n')
    if it['context_ids']:
        out.append('**Register evidence:**\n')
        for id in it['context_ids']:
            r=registry[id]
            out.append('- **'+id+'** — '+r['status']+'; '+code('notes/RESULTS_STATE.md')+f', L{r["line"]}; named source '+code(r['source_file'])+'; prior locator: '+r['prior_locator'].rstrip('.')+'.')
        out.append('')
    else:
        out.append('**Register evidence:** No specific selected register result identified for this item; the search record includes the supplied contextual matches.\n')
    if it['primary_refs']:
        out.append('**Checked primary comparison:** '+', '.join('['+k+'](#'+k+')' for k in it['primary_refs'])+'.\n')
    if it['confidence']:
        out.append('**Own-idea confidence:** '+it['confidence']+'  \n**Reason:** '+it['reason']+'\n')

# Standalone, short index of source verification flags.
self_rows=[
('007','N006','reste à vérifier H^{n+1}(G)=0','Taken up on009 through the mu-p reduction; the cancelled route remains recorded.'),
('020','N028–N029','suffit-il de degré de transcendance fini ??','Live margin question; explicit real-closure test recorded.'),
('023','N036','avec égalité dans le cas A hensélien ?','Deleted question; no general equality inferred.'),
('023','N035','cette restriction est-elle [unsure: inutile] ???','Live question; attachment and word remain uncertain.'),
('026','N045','on doit pouvoir obtenir des énoncés','Expected cover/line-bundle equivalences; precise local hypotheses left to supply.'),
('026','N046','il est probable que l’on doit pouvoir','Nonproper Picard expectation.'),
('031','N042','Tout sera fait … si nous prouvons que (iii)⇒(i)','The scan goes on to a proof ending cqfd; recorded as a task addressed on the same leaf.'),
('042','N064','[unsure: Voir] … [unsure: dans le livre de] [illegible1]','Weak marginal checking/reference instruction; author/book unidentified.'),
('043','N066','[unsure: Reste] à prouver','Relative endomorphism-trace lemma explicitly deferred.'),
('044','N068','est bijectif (?)','Units H1 map expressly questioned.'),
('044','N069','Qu’en est-il dans le cas … des Gl(n,O)','Matrix-group extension expressly asked.'),
('044','N070','il y a des hyp. [unsure: noethériennes] à faire ??','Completion/Tate comparison hypotheses expressly unsettled.'),
('045','N071','ou un quotient ???','Inside the cancelled block.'),
('045','N071b','ceci est-il [unsure: identique] à Z_2^{S^infty} ???','Inside the cancelled block; a second distinct quotient question.'),
('048','N076','à vérifier','Decomposition over the perfect ground field.'),
('048','N078','dire qqp; dégager un lemme; limite inductive est essentiel','Requests extraction of the lemma and stresses its limit step.'),
('051','N088–N089','est-ce [unsure: ≃|=] un vrai isomorphisme?','Coefficient-comparison question, with degree and mod-p qualification.'),
('051','N091','Reste à prouver H^i(K,Z/p)=0 si i>1','The sequence is supplied; the retained leaf ends before a prose conclusion.')
]
out.append('## Standing question: steps the manuscript itself marks for checking\n')
out.append('This index records source markers, including deleted questions and a proof task subsequently addressed on its own leaf. A bare “facile”, “trivial” or “bien connue” is handled in the numbered notes as a proof claim, not automatically counted as an authorial doubt. The reservation “pas nécessairement localement libre, hélas” is recorded at N044 as a stated limitation.\n')
out.append('| Scan in31.pdf | Item | His words (uncertainty retained) | State on the retained leaves |\n|---|---|---|---|')
for row in self_rows:out.append('| '+' | '.join(esc(v) for v in row)+' |')
out.append('\nOther unfinished retained passages are indexed at N009, N047, N059, N081, N084 and N093; their incompleteness is visible even where no verification phrase occurs.\n')

def macro_args(s,macro):
    pat=re.compile(r'\\'+re.escape(macro)+r'\{')
    for m in pat.finditer(s):
        pos=m.end();i=pos;depth=1
        while i<len(s) and depth:
            if s[i] in '{}':
                back=0;j=i-1
                while j>=0 and s[j]=='\\':back+=1;j-=1
                if back%2==0:depth+=1 if s[i]=='{' else -1
            i+=1
        yield s[pos:i-1],s[:m.start()].count('\n')+1
out.append('### Complete manuscript-numeral index\n')
out.append('The entries below are the actual mspage occurrences in the frozen fragments, in their within-page order. Cover margins and count-like annotations are recorded separately in T01–T05; no arithmetic total is inferred from independent numbering systems.\n')
out.append('| Scan in31.pdf | mspage occurrence(s) | Fragment line(s) |\n|---|---|---|')
for f in sorted((BASE/'pages').glob('*.tex')):
    n=int(re.search(r'scan(\d+)',f.name).group(1))
    vals=list(macro_args(f.read_text(),'mspage'))
    out.append('| '+f'{n:03d}'+' | '+esc('; '.join(code(v) for v,l in vals) or 'None recorded')+' | '+', '.join(str(l) for v,l in vals)+' |')
out.append('')

out.append('## Disposition of every supplied RESULTS_STATE entry\n')
out.append('There are26 substantive selected entries: one open return, one claimed proved return, one intake excerpt,20 returned-package leads, two unchecked planning items, and one external candidate. The two later run-state rows identify LM7/LM7_PUSH as returned; they are provenance rows rather than additional mathematical claims. Each row below also has its own literal-ID search in the search record.\n')
out.append('| ID and supplied status | Named earlier source and available locator | Contribution or limit of this package | Items |\n|---|---|---|---|')
for id,r in registry.items():
    out.append('| '+esc(id+' — '+r['status'])+' | '+esc(r['source_file']+'; '+r['prior_locator']+f'; supplied RS L{r["line"]}')+' | '+esc(r['disposition'])+' | '+esc(', '.join(r['note_ids']) or 'Register accounting / scope comparison only')+' |')
out.append('')

out.append('## Checked primary sources and exact comparison locators\n')
out.append('All external reading took place in the research phase after the transcription freeze, on16–17 November2026. External-source workers inspected published material only; they did not read the manuscript images or the supplied context. The root reader retrieved the cited primary pages and authored the manuscript/context comparisons. Sources are cited for the indicated passages, with no claim that the manuscript’s broader wording inherits all their conclusions.\n')
for key,title,url,loc,ver in sources:
    out.append('<a id="'+key+'"></a>\n')
    out.append('### '+key+' — '+title+'\n')
    out.append('['+title+']('+url+')  \n**Locator/version:** '+loc+'  \n**Check:** '+ver+'\n')
out.append('### Retrieval limits\n')
out.append('The complete earlier package files listed by RESULTS_STATE were absent from the supplied archive. EGA III1 was too large for one browser retrieval; this dossier cites its numbers only where the manuscript or the checked SGA2 passage cites them, and relies on the separately retrieved EGA III2 erratum for N048. An additional ramified-transfer article was inspected by an external-source reader, but root retrieval failed, so it is not used as a cited proof here. The manuscript’s hatted-cohomology conventions, the full regular-ring extension on scan023, and several incomplete proof tails remain questions in the numbered notes.\n')
out.append('## Research-phase integrity\n')
out.append('The builder verified all47 frozen hashes before and after generating this dossier. Its context-search records are derived work records; the supplied scans, archives and context files themselves are excluded from the deliverable ZIP. The final package integrity check is recorded separately in progress.log and records/final_validation.json.\n')
notes='\n'.join(out)
prose_replacements={
'There are26':'There are 26', 'excerpt,20':'excerpt, 20',
'all47':'all 47','on16–17 November2026':'on 16–17 November 2026',
'reporting29':'reporting 29','reporting44':'reporting 44',
'the26':'the 26','cote31':'cote 31','cote44':'cote 44',
'input to N060':'input to N060','Version2015':'Version 2015',
'version2015':'version 2015','Editor-hosted2009':'Editor-hosted 2009',
'Author-hosted2017':'Author-hosted 2017','compiled2012':'compiled 2012',
'Society61':'Society 61','IHÉS17':'IHÉS 17','the1966':'the 1966',
'Corollary2.4':'Corollary 2.4','Theorem2':'Theorem 2',
'Theorem3':'Theorem 3','Theorem16.13':'Theorem 16.13',
'Theorem2.5':'Theorem 2.5','Proposition14.54':'Proposition 14.54',
'Remark2.4':'Remark 2.4','original5.15':'original 5.15',
'notes36':'notes 36','liste2':'liste 2','Err_III24':'Err_III 24',
'printed297':'printed 297','printed328':'printed 328',
'PDF309':'PDF 309','PDF340':'PDF 340',
'Tag03':'Tag 03','Tag0A':'Tag 0A','Lemma21':'Lemma 21',
'Theorem59':'Theorem 59','Lemma59':'Lemma 59','reader36':'reader 36','Proposition59':'Proposition 59',
'scans002':'scans 002','at131':'at 131',
'degree-p':'degree-p'
}
for old,new in prose_replacements.items():notes=notes.replace(old,new)
notes=re.sub(r'\b(scans?|boundary|printed|original)(?=\d)',r'\1 ',notes)
notes=re.sub(r'\bSGA([234])(?=[\s,.;0-9]|$)',r'SGA \1',notes)
notes=re.sub(r'\b(IX|XII|X)(?=\d)',r'\1 ',notes)
notes=re.sub(r'\b(pp?\.)(?=\d)',r'\1 ',notes)
notes=notes.replace(r"\unsure{!|'} in the frozen file",code(r"\unsure{!|'}")+' in the frozen file')

(BASE/(PREFIX+'_notes.md')).write_text(notes)

write_json('research_items.json',{'generated_utc':now,'items':items})
write_json('context_searches.json',{'generated_utc':now,'searched_files':['README.md','notes/RESULTS_STATE.md'],'note_searches':searches,'register_coverage_searches':coverage_searches})
write_json('results_state_coverage.json',{'generated_utc':now,'entries':list(registry.values())})
write_json('primary_sources.json',{'retrieval_phase':'after 2026-11-16 23:40:30 UTC','sources':list(source_dict.values())})
md=['# Executed context searches\n','Every item below was searched against both supplied context files using rg; the earlier full files named by the register were unavailable.\n']
for s in searches:
    q=s['object_search']
    md+=['## '+s['id']+'\n','UTC: '+q['utc']+'  \nObject query: '+code(q['pattern'])+'  \nExit code: '+str(q['return_code'])+'\n']
    if q['matches']:
        md+=['| Supplied file | Line | Matched terms | Excerpt |\n|---|---:|---|---|']
        for m in q['matches']:md.append('| '+esc(m['path'])+' | '+str(m['line'])+' | '+esc(', '.join(m['matched_terms']))+' | '+esc(m['excerpt'])+' |')
    else:md.append('No object-query match in the two supplied files.')
    md+=['','Literal-ID lookups: '+('; '.join(code(x['pattern'])+' → '+', '.join(m['path']+':L'+str(m['line']) for m in x['matches']) for x in s['id_searches']) or 'none')+'.\n']
md+=['## Register-coverage searches\n']
for c in coverage_searches:
    q=c['search'];md.append('- '+c['id']+': '+code(q['pattern'])+'; '+q['utc']+'; '+', '.join(m['path']+':L'+str(m['line']) for m in q['matches']))
(BASE/'records/context_searches.md').write_text('\n'.join(md)+'\n')
frozen_check()
with (BASE/'progress.log').open('a') as f:
    f.write(f'research notes built {utc()} items={len(items)} substantive={sum(x["id"].startswith("N") for x in items)} title_items={sum(x["id"].startswith("T") for x in items)} context_searches={len(searches)} register_entries={len(registry)} frozen_hashes_unchanged=47\n')
print(json.dumps({'items':len(items),'substantive_items':sum(x['id'].startswith('N') for x in items),'title_items':sum(x['id'].startswith('T') for x in items),'words':len(notes.split()),'notes_bytes':len(notes.encode()),'context_note_searches':len(searches),'registry_entries':len(registry),'frozen_files_unchanged':47}))
