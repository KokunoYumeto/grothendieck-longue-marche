"""Record the actual post-freeze research uses and checks, with limited scope.

This script records already-performed human/model work and saved computation
output. It does not turn source reading into a mathematical proof check.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json
from assemble_research import notes

ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
who='GPT-6 Astra Pro; effort not separately exposed; MPL_67_002-052/root'
rows=[]
def event(id,typ,outcome,date=now,actor=who):
    rows.append([id,date,actor,typ,outcome])

for n in notes:
    event(n['id'],'used and rechecked in this run',
          'Post-freeze textual/context comparison and register-status attribution only. '
          'Cote 67 scan '+n['scan']+'; kind: '+n['kind']+'. '
          'The cited context and per-item searches are recorded in the notes and context_search_ledger.tsv. '
          'No mathematical truth or reading certainty is certified by this row; separate mathematical checks have separate rows.')
    event('MPL67:scan '+n['scan']+':'+n['id'],
          'used and rechecked in this run',
          'Source passage used in '+n['id']+' and compared after freeze with the named context. '
          'The quote, questions, deletions or doubtful readings retain their attributed source status. '
          'This is a textual use/check, not proof by transcription.')

register={
 'EXIT_TOWER A.5':'Headline claim in checkpoint 28; component moduli/stratum statement cited as background in the surgery ledger, without its full proof being supplied.',
 'EXIT_TOWER B.27':'Headline claim in checkpoint 28 concerning a finite groupoid colimit; graph colimit in scan006 not identified with it by this run.',
 'EXIT_TOWER E.23':'Proved, return’s claim; full labelled tower statement and source locators carried without a new proof check.',
 'EXIT_TOWER E.35':'Proved, return’s claim; framed sewing and boundary-fixed groupoid recovery carried with source scope; no proof rederived.',
 'EXIT_TOWER E.36':'Proved, return’s claim; capping/stabilization and quotient actions carried with the excerpt’s target-boundary qualification.',
 'EXIT_TOWER E.39':'Proved, return’s claim; completed tower-action statement carried without promoting it to a review verdict.',
 'EXIT_TOWER E.24':'Open, return’s claim; exact arithmetic images remain open in these notes.',
 'EXIT_TOWER E.45':'Open, return’s claim; higher-genus restriction images remain open in these notes.',
 'PUSH_ORDER5_FRAME Itemsfromt 2':'Open push item; scans004/050/051 supply operations and small examples, not a verified five-point rigid-frame calculation.',
 'IMPL P3':'Open candidate prompt item, carried in context_surgery.md as an index-category/finality lead; full source absent.',
 'MPL_152+120 Q1-07':'Register’s checked pointed-disc-shadow-map claim, with unresolved comparison; full note and its source/search ledger absent. No rederivation.',
 'MPL_147_003-047 N075':'First-pass research lead; available note at source scan003 items9–12 and scans035–047 used for boundary-compatibility comparison, not as an established result.',
 'LM4 C.12':'Open, return’s claim; actual level-zero identity-component kernel and infinite-operator-group question retained without status change.',
 'LM4 F.7':'Open, return’s claim; nonsolvable completion-centralizer comparison retained, including its geometric A5 scope.',
 'LM4_SUCCESSOR B.39':'Open, return’s claim; nonsolvable direction retained without an inferred completion theorem.',
 'LM4_SUCCESSOR E.10':'Open, return’s claim; six fixed-kernel/nonabelian-H1 computations not supplied by the concrete metric calculations.',
 'LM6 C.12':'Open, return’s claim; full profinite involution classification/centralizers in genus at least3 remains open, including smallest uncompleted type(3,0).',
 'LM6 A.22':'Open, return’s claim; full CM group, closed procyclic C in R, and arithmetic normalizer image open in G_Q(i) retained explicitly.',
 'LM6 B.27':'Open, return’s claim; stated point-surjectivity and point-or-cusp problems retained; no completion claimed from scan049.',
 'LM6 F.43':'Proved, return’s claim; truncated statement about labelled normal lines of a smooth normal-crossings pair carried as background. Full source proof absent.',
 'FLAGGED_149 ZCF6':'Open, return’s claim; title and listed source scans verified. Enumerated existence predicates omitted in supplied digest, so use limited to existence-issue background.',
 'WG H2':'Unchecked war-game hunch; vanishing-cycle comparison used as a lead, not proved from the Galois-incompatibility assertion on scan048.',
 'WG2 §1.1 #6':'Unchecked planning item; cote149 normal-boundary and cote147 comparison retained with source locators.',
 'WG2 §1.4 #3':'Unchecked planning item; continuation and boundary-inertia questions retained.',
 'LM4 D.32':'Proved, return’s claim, explicitly refereed14Nov2026 as claimed; three-cusp rank/finite pure-loop result carried with its actual scope, not rederived.',
 'LM4 D.34':'Named in the referee-summary list only; no individual statement supplied. No particular theorem from this ID used in the final notes.',
 'LM7_PUSH D.44':'Review scope reported in the arithmetic ledger is limited to the portions used by D.50/E.58; no modular theorem transferred from the abbreviated row.',
 'LM7_PUSH E.58':'Register review qualification carried in context ledger; no new proof check of the source return.',
 'LM7_PUSH E.65':'Register review qualification carried in context ledger; no conclusion of global vanishing inferred from its criterion.',
}
for id,scope in register.items():
    event(id,'carried as background without fault found',
          'Status/scope attribution checked against context/notes/RESULTS_STATE.md. '+scope+
          ' This event does not certify an unavailable return proof.')

event('LM_P052:S01:scans513-516','carried as background without fault found',
      'The supplied LM_140-2_notes.md labels this a second-pass checked claim and gives S,R and the amalgam presentation. '
      'Attributed as a prior check; present work checks only the new source/reflection assignment, not presentation completeness.')
event('LM_P049:B4:scan483','carried as background without fault found',
      'Prior checked-note objection to the unrestricted normalizer-recognition margin used only to compare the explicit procyclic restriction of cote67 scan049; no reproof.')
event('Hua67:I:genus-one-tree-objection','carried as background without fault found',
      'N68 records Hua’s embedded-tree objection as a credited lead; no independent topological proof check of that example or its added general restriction in this run.')

report=json.loads((ROOT/'records/calculation_results.json').read_text())
for c in report['checks']:
    event(c['id'],'computation or formal certificate',
          c['outcome']+': '+c['detail']+' Executed SymPy '+report['sympy_version']+
          '; exact scope and matrices in records/check_calculations.py and calculation_results.json.',
          report['utc'],report['who'])

proofs={
 'C01.reflection_dictionary':'Exact source-to-source dictionary r1=A,r2=B,r3=-ACA and inverse C=-Ar3A verified by multiplication; no group-presentation proof claimed. Supports N55.',
 'C02a.metric_pullback':'The positive-ray map, area-one normalization, curvature4pi, determinant-one representative, holomorphic and antiholomorphic pullbacks checked by substitution. Credits Hua’s Hermitian-ray/H3 model. Supports N31,N32,N37.',
 'C02b.fixed_models':'Diagonal half-turn/rotation forms, real-symmetric conjugation forms, A_p inverse parameters/opposite poles and scalar antipodal forms checked for the stated maps. Supports N25,N33,N34,N43; no universal compact-subgroup classification reviewed.',
 'C02c.action_reversal':'Four coordinate composition identities checked; verifies the correction C’est l’inverse from scan034 through scans035–036. Supports N35,N36.',
 'C02d.normalizations':'Exponential cylinder pullback and length-one circle, degree-two area formula, and the specific z->2z obstruction checked. Supports N29,N30,N31.',
 'C03.orange_containment':'Hua’s credited extremal-length obstruction checked on the particular C(32,0,0), with explicit symmetric cell, actual collar cap, annulus inclusion/core class, area, extremal-length bounds and strict rational gap. Supports N23 and refined scope in C03.',
 'C04.complement_example':'The exact set differences for X=P1 minus{0,1,infinity} contained in Xprime=P1 checked; records a reading question only. Supports N44.',
 'C05.peripheral_example':'Explicit inverse graph map and abelianization obstruction for the pants self-homotopy equivalence checked. Supports N15; no full outer-automorphism classification claimed.',
 'C06.local_tensor':'The stated xy=t polar map and tangent-tensor coordinate invariance checked. Supports N52; no global arithmetic identification of[Y,N] asserted.',
 'C07.Borel_orbit':'Actual stabilizer, primitive-column/Bézout inverse and mod2 projective reduction checked. Supports N58; no free-group rank theorem rederived.',
 'C08.half_plane_map':'Coordinate formula for induced real affine maps and identity fiber{1,conjugation} in the full conformal centralizer checked. Supports N67; no profinite kernel identification asserted.'
}
for id,scope in proofs.items():
    event(id,'targeted proof check',scope+' Argument in records/research_checks.md; limited to the stated explicit objects.')

for note,certificate in {
    'N15':'C05.peripheral_example', 'N23':'C03.orange_containment',
    'N29':'C02d.normalizations', 'N30':'C02d.normalizations',
    'N31':'C02d.normalizations', 'N33':'C02b.fixed_models',
    'N34':'C02b.fixed_models', 'N35':'C02c.action_reversal',
    'N36':'C02c.action_reversal', 'N37':'C02a.metric_pullback',
    'N44':'C04.complement_example', 'N52':'C06.local_tensor',
    'N55':'C01.reflection_dictionary', 'N58':'C07.Borel_orbit',
    'N67':'C08.half_plane_map'
}.items():
    event(note,'targeted proof check',
          'The explicit calculation in this note was checked under '+certificate+'. '+proofs[certificate]+
          ' The verdict has exactly that scope; it is not a proof of every surrounding source claim.')
event('N41','computation or formal certificate',
      'The substitution(g,nu)=(0,1) is the saved exact check C04.heavy_sign_example. It identifies a sign reading question only.',
      report['utc'],report['who'])

for id in proofs:
    if id.startswith(('C03','C04')):
        continue
    event(id,'targeted proof check',
          'Independent coordinate review passed for this stated calculation; records/coordinate_checks_review.md '
          'gives the arguments, reviewed source hash and limited scope. No substantive correction; explicit '
          'nonzero-coordinate domains and cross-pairing explanation noted as clarifications.',
          '2026-11-18 01:23:55 UTC',
          'GPT-6 Astra Pro; effort not separately exposed; MPL_67_002-052/research_arithmetic')
event('COORDINATE_REVIEW:20_explicit_assertions','computation or formal certificate',
      'Twenty independent symbolic/exact checks returned True, enumerated individually in '
      'records/coordinate_checks_review.md under Independent execution summary. '
      'Scope: displayed matrices, metric coefficients, normalizations and the explicit graph-map substitutions; '
      'no registry presentation proof.',
      '2026-11-18 01:22:02 UTC',
      'GPT-6 Astra Pro; effort not separately exposed; MPL_67_002-052/research_arithmetic')

event('MPL67:scans019-020:orange_model_with_degenerate_discs',
      'refuted, with refined statement C03.orange_containment',
      'The equidistant-label/S3-invariant metric interpretation predicts cap D0 contained inQ0 for C(32,0,0). '
      'C03 gives incompatible extremal-length bounds for that prediction. '
      'Method credited to Hua67§III; exact refined target C03.orange_containment. '
      'No refutation of radii injectivity, full parameter-image characterization or the independent collar question is claimed.')
event('Hua67:III:orange_obstruction','targeted proof check',
      'Credited source argument rechecked through explicit witness C03; no novelty claim.')
event('C03.orange_containment','targeted proof check',
      'Independent research-agent review passed for cell, actual admissible cap, core class, area, both bounds and strict inequality; '
      'a McMullen section-number correction and explicit-cap addition were requested and incorporated. '
      'Review in records/orange_obstruction_review.md.',
      '2026-11-18','GPT-6 Astra Pro; effort not separately exposed; MPL_67_002-052/research_surgery')

for id,scope in {
 'PRIMARY:Borcherds261notes18':'Author PDF pp58–59; determinant/action comparison used forC02. Passage located; no full-paper proof review.',
 'PRIMARY:Mirzakhani2007:C3200':'§2 p186 and§3 p190; zero-length cusp convention and specified pants object used. Passage located; existence carried as published background.',
 'PRIMARY:WeberHoffmanWolf2009:EL':'§2.5 pp368–369; extremal-length convention, annulus and embedding comparison located and used; independent elementary derivation of the particular annulus is inC03.',
 'PRIMARY:McMullen2021:cell':'Printed p44,§4 Curvature; symmetric cell formula located and compared. Section-number correction incorporated after review.',
 'PRIMARY:NakayamaOgus2010:node':'pp2189–2190; actualxy=t polar map opened and used. No global log-fibration or arithmetic-realization theorem applied.',
 'PUBLICATION:CSG_L28d':'Visible title and editorial page1–2 checked against supplied SECTIONS_STATE link; cote67, letter date and draftSeptember2024 verified. Six printed letter pages located at PDF4–9; unrelated retrieval-title metadata rejected in favor of visible document.'
}.items():
    event(id,'used and rechecked in this run',scope)

with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who_model_effort_run','type','outcome']);w.writerows(rows)
print(json.dumps({'events':len(rows),'utc':now,'scope':'actual post-freeze uses, computations and limited proof checks'}))
