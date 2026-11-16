"""Produce the individual §51.15–51.16 concordance from the statement register.

The quoted questions were located in the supplied transcription and then
checked against the official original images in the sixth-interval audit.
One-based PDF positions, printed archive offsets and folios are stated in D.2.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

passages = {
    'F': r'\S51.16, f.~734, scan 173',
    'A': r'\S51.16, f.~736, scan 177',
    'T': r'\S51.16, ff.~735--736, scans 175--177',
    'K': r'\S51.15, f.~731v, scan 168',
    'L': r'\S51.15, f.~732v, scan 170',
}

answers = {
'A.17': 'The torus quotient has the full two-coordinate completed Kummer section set; its S3-equivariant splitting is unique up to unique geometric conjugation.',
'A.20': 'The stipulated proper local Theorem 1.1 implies the affine point-or-cusp alternative by cofinal neighbourhoods; only this named additional input promotes the global Selmer theorem to all sections.',
'A.21': 'Real sections are classified by connected components. Two cusp sides can give the same component; the plus curve of even exponent has no real section.',
'A.22': 'A density-one support assertion cannot replace all-place descent. The displayed density-intersection inference fails; its repair uses strong positive upper density.',
'A.23': 'The completed Kummer fibres of each cusp packet are computed exactly. Whenever a packet is present the set of section classes is infinite.',
'A.24': 'A nonconstant map to a rank-zero target whose Tate–Shafarevich group has no nonzero divisible subgroup gives only rational-point or rational-cusp sections.',
'A.25': 'The three elliptic quotients of every diagonal quartic are written over Q, with their exact coefficients and CM by Z[i].',
'A.26': 'Explicit quotient maps give rank-zero criteria for diagonal sextics; the complete ten-factor decomposition is supplied in A.34.',
'A.27': 'The diagonal cubic Jacobian is y²=x³−432(abc)²; its isomorphism class depends on the cube class of abc.',
'A.28': 'At good primes, a ramified section in the full prime-to-residue-characteristic quotient lies at one cusp; this uses a single simultaneous quotient.',
'A.29': 'Cross-prime agreement concerns one completed Kummer parameter, not one ordinary integer. An explicit parameter with different primary components refutes the latter reading.',
'A.30': 'The exact independent weakest local hypothesis remains open. The residual modularity and all-place descent requirements used by the proof are separately stated.',
'A.31': 'With the stipulated local theorem, the full global section is cuspidal, which supplies common cusp and parameter data at every prime.',
'A.32': 'The rank-zero fibres exclude noncuspidal ghosts; cusp Kummer parameters can have infinite ramification, so residual finite ramification is insufficient.',
'A.33': 'Elementary torsion classifications bound the two CM families by orders six and four and list every nonzero-coordinate torsion case used by the point census.',
'A.34': 'All ten elliptic factors of a diagonal sextic are supplied, with maps and an independent holomorphic-differential basis.',
'A.35': 'Universal lists of three tripod values for cubic and quartic criteria, and fifteen for sextic criteria, give every ordinary point in the settled classes.',
'A.36': 'For every class meeting a CM rank-zero criterion, the section set is the explicit ordinary-point list together with all rational cusp packets.',
'A.44': 'Every profinite multiple of a rational non-torsion elliptic point lifts through every finite-kernel refinement, or finite collection of such refinements. This is not a Selmer assertion.',
'A.45': 'The full intrinsic metabelian and congruence lifting sets remain open. A59--A69 settle the stated abelian exponent classes and every finite alteration of an integer at the actual joint level-three quotient.',
}

def escape(s):
    s=s.replace('–','--').replace('—','---')
    trans={'ℓ':'ell','κ':'kappa','χ':'chi','μ':'mu','ζ':'zeta','η':'eta',
           'Δ':'Delta','Π':'Pi','π':'pi','Γ':'Gamma','Λ':'Lambda',
           '²':'^2','³':'^3','⁴':'^4','⁵':'^5','¹':'^1',
           '⊕':' plus ','⊗':' tensor ','→':' to ','↦':' maps to ','≥':'>=','≤':'<=',
           '≠':'!=','∈':' in ','∼':' isogenous to ','−':'-',
           'Ẑ':'Zhat','∞':'infinity','ℛ':'R','ℋ':'H'}
    for a,b in trans.items(): s=s.replace(a,b)
    out=[]
    specials={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$',
              '#':r'\#','_':r'\_','{':r'\{','}':r'\}',
              '~':r'\textasciitilde{}','^':r'\textasciicircum{}',
              '<':r'\textless{}','>':r'\textgreater{}'}
    for c in s: out.append(specials.get(c,c))
    return ''.join(out)

rows=[]
for row in csv.DictReader((ROOT/'FERMAT_SUCCESSOR_results.csv').open()):
    sid=row['id']
    if sid[0] not in 'AB': continue
    if sid.startswith('B.'):
        keys=['A','F'] if sid in {'B.1','B.2','B.3','B.4','B.5','B.6','B.12','B.18','B.25','B.26'} else ['A']
    else:
        keys=['F']
        if sid in {'A.17','A.23'}: keys=['T','A']
        if sid=='A.29': keys=['K','F']
        if sid=='A.32': keys=['F','K']
        if sid in {'A.28','A.30','A.46','A.47','A.48','A.49'}: keys=['F','L']
    answer=answers.get(sid,row['statement'])
    rows.append(dict(id=sid,questions=', '.join(keys),
                     passage='; '.join(passages[k] for k in keys),
                     status=row['status'],answer=answer))

links=['% Generated by code/make_manuscript_concordance.py.']
for r in rows:
    value=r['passage']+'; question '+r['questions']+' in D.2.'
    links.append(r'\expandafter\def\csname ms:'+r['id']+r'\endcsname{'+value+'}')
(ROOT/'tables/manuscript_links.tex').write_text('\n'.join(links)+'\n')

tex=[r'\subsubsection*{Individual concordance for Parts A and B}',
r'''The short question keys in the statements and the table refer to the
following passages, checked against the original official manuscript images
after being located in the supplied transcription. \textbf{F}
asks for ``l'inexistence de scindages de (371) autres que ceux
`provenant des pts \`a l'infini' '' (Section 51.16, folio 734, scan 173).
\textbf{A} asks to ``d\'eterminer toutes ces classes de
$\widehat M[n]$-conjugaison possibles de tels scindages'' (Section 51.16,
folio 736, scan 177). \textbf{T} refers to that same question for the
explicit extension (373), constructed on folios 735--736, scans 175--177.
\textbf{K} asks ``sont-ils surjectifs, ou du moins l'image est-elle un
sous-groupe ouvert ?'' and asks this jointly for distinct primes
(Section 51.15, folio 731v, scan 168, (358)(a)--(b)). \textbf{L} asks
``si cet homomorphisme est surjectif, ou si du moins son image est
ouverte ?'' for the restriction to $I_\ell^+$ (Section 51.15,
folio 732v, scan 170, (365)).

The table states the answer or the exact technical contribution of
\emph{each} statement. Intermediate lemmas are not represented as new
questions literally written in the manuscript. The qualifications in
each numbered statement, including the distinction between full and
quotient sections, are retained.''',
r'\begingroup\small\setlength{\tabcolsep}{4pt}',
r'\begin{longtable}{@{}p{.09\textwidth}p{.10\textwidth}p{.75\textwidth}@{}}',
r'\toprule ID & Question & Answer and status \\ \midrule',
r'\endfirsthead',r'\toprule ID & Question & Answer and status \\ \midrule',r'\endhead']
for r in rows:
    tex.append(escape(r['id'])+' & '+escape(r['questions'])+' & '+
               r'\textbf{'+escape(r['status'])+'}. '+escape(r['answer'])+r' \\')
tex += [r'\bottomrule',r'\end{longtable}',r'\endgroup']
(ROOT/'tables/manuscript_concordance.tex').write_text('\n'.join(tex)+'\n')
with (ROOT/'records/manuscript_concordance.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,list(rows[0])); w.writeheader();w.writerows(rows)
print(f'Individual provenance and answer entries: {len(rows)}')
