"""Bind the complete new symbolic proofs without changing frozen37 mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
def bind(rel):
    raw=(ROOT/rel).read_bytes()
    return {'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

sources=[
 'work_A/actual_explicit_elliptic_pentagon_transporter37.md',
 'work_A/A131_explicit_elliptic_pentagon_transporter_proposed.tex',
 'work_DE/actual_negative_hexagon_base_transporter37.md',
 'work_A/actual_elliptic_full_involution_transporter37.md']
reviews=[
 'work_DE/review_A131_explicit_transporter37.md',
 'work_DE/review_A131_explicit_transporter37.json',
 'work_CE/review_explicit_elliptic_pentagon_transporter37.txt',
 'work_CE/review_A131_final_tag_repair37.json',
 'work_A/review_negative_hexagon_base_transporter37.md',
 'work_A/review_negative_hexagon_base_transporter37.json',
 'work_CE/review_negative_hexagon_base_transporter37.txt',
 'work_CE/review_negative_hexagon_base_transporter37.json',
 'work_DE/review_full_elliptic_involution_transporter37.md',
 'work_DE/review_full_elliptic_involution_transporter37.json']
record={'recorded_at':datetime.now(timezone.utc).isoformat(),
 'result':'PASS_COMPLETE_ROOT_AND_INDEPENDENT_SYMBOLIC_SOURCE_REVIEWS',
 'root_complete_source_reads':{'explicit_transporter_and_final_A131':'ceb043',
                             'negative_hexagon_base_transporter':'115372',
                             'entire_full_involution_transporter_and_companion':'56b71e'},
 'root_complete_review_reads':['b36c1a','e29ad3'],
 'sources':[bind(rel) for rel in sources],
 'independent_reviews':[bind(rel) for rel in reviews],
 'formal37_pdf_changed':False,'formal37_statement_count':389,
 'new_mathematical_computation_run':False,
 'proved_scope':['p_w=w(X3^-1,K2)w(X,a)=w(a,b)^-1 w(X,K)w(X2,b)',
                 'a_w=1 for each original profinite commutator pentagon word',
                 'h1=Phi phi(X2,b), b0=1 for the actual original negative full-GT action',
                 'h_u=phi(a,b) as a literal full-group equality',
                 'h_u^-1=B_u^-1 Theta(B_u) in the entire Brunnian kernel',
                 'B_u Pi_u B_u^-1 is fixed by the original Theta and has exact order three'],
 'remaining_scope':['h_u=1 is not asserted','specified two-strand boundary remains Open',
                    'full generation remains Open','original CM frame comparison remains Open',
                    'no bare-GT0 canonical-u pentagon or three-strand action is asserted'],
 'notation_note':'The supplemental proof locally names a C2 cocycle z_u; in formal integration it must receive a different symbol from A.127\'s C3 cyclic-defect z_u.'}
with (ROOT/'records/checkpoint37_late_transporter_root_review.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
addition=r'''

## Late exact transporter results, after the formal37 PDF was frozen

These are complete new symbolic proofs, separately saved and reviewed in
`records/checkpoint37_late_transporter_root_review.json`. They are supplemental
research for the next formal cycle; the present PDF remains the reviewed
719-page,389-statement edition. No numerical or finite-target computation is
claimed for these results. The following conclusions supersede the earlier
unevaluated labels for the particular elliptic parameters and transporter.

For every original full profinite commutator word w satisfying the marked
four-strand pentagon, write U=w(X,K), Z=w(X2,b), A=w(X,a),
E=w(X3^-1,K2), B=w(a,b), with a=sigma^2 and b=tau^2.
The literal based pair identity Pi0(X2,b)Pi0^-1=(X,a), combined with the
ordered pentagon B E A=U Z, gives the ACTUAL unique pure-derived transporter

    p_w=E A=B^-1 U Z,
    Pi_w=p_w Pi0 p_w^-1,
    q(p_w)=(U,U,U), so a_w=1.

This uses the original pentagon without a hexagon for w or a putative
GT pair (d,w). It also supplies a direct proof of the cubic independently
of the repaired longer A.121 cancellation. The canonical full-GT u has
that pentagon by A.37.

The ORIGINAL negative hexagon for phi, with both braid conjugates and
the central decoration retained in their exact order, gives
Ad(tau)(F)=F Ad(tau sigma)(F), where F=phi(a,b). Consequently

    Theta(Pi0)=F Pi_phi F^-1,
    h1=F p_phi=Phi Z_phi,
    q(h1)=(Phi,Phi,Phi), so b0=1.

Thus the particular C3 connecting parameter is exactly one. A further
full-group calculation evaluates even the remaining Br-valued involution
transporter. Both the negative and zero cycles hold for the same ORIGINAL
phi: the latter comes from the actual normalized composite alpha c=(1,phi).
Together with the original phi pentagon they give

    Theta(X2)=Phi Z_phi X2^-1 Z_phi^-1 Phi^-1,
    Theta(Z_u)=Phi Z_u Z_phi^-1 Phi^-1,
    Theta(U Z_u)=(U Z_u)h1^-1,
    h_u=Theta(p_u)h1 p_u^-1=F.

All equations are in the entire original profinite elliptic group. Since
F and B_u=u(a,b) both lie in the ENTIRE Brunnian kernel and
Theta(B_u)=B_u F^-1, the inverse involution cocycle is the explicit
Br-coboundary B_u^-1 Theta(B_u)=F^-1. In particular

    Pi_u^*=B_u Pi_u B_u^-1=(U Z_u)Pi0(U Z_u)^-1

is fixed by the ORIGINAL Theta and has exact order three. It and the
external involution form an actual C6 subgroup. This result follows from
the additional complete norm calculation; it was not inferred merely
from neutral C3 cohomology.

No claim F=1, h_u=1 or Theta(Pi_u)=Pi_u is made. The specified two-strand
boundary, the prescribed marked generator equality, full generation and
the comparison with the ORIGINAL signed CM frames remain Open. Historical
capture/readiness references to an unresolved coherent class refer to
that original frame comparison; the particular elliptic Br-valued class
has now been evaluated and neutralized as explicitly stated above.
No canonical-u hexagon or general three-strand GT0 action is inferred.
All earlier sources and their former unresolved statuses remain retained.
'''
report=ROOT/'records/thirty_seventh_hour_research_report.md'
old=report.read_text()
assert '## Late exact transporter results, after the formal37 PDF was frozen' not in old
report.write_text(old+addition)
print(json.dumps({'result':'LATE_EXACT_TRANSPORTER_PROOFS_RECORDED','sources':len(sources),'peer_files':len(reviews),'formal_pdf_changed':False}))
