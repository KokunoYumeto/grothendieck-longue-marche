#!/usr/bin/env python3
"""Record checks/uses actually made during integration; idempotent by statement ID."""
import csv
from pathlib import Path
from datetime import datetime,timezone
rec=Path(__file__).resolve().parent
path=rec/'check_events_root.tsv'
cols=['statement_id','date','who','type','outcome']
with path.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
seen={r['statement_id'] for r in rows}
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
who='GPT-6 Astra Pro / effort not exposed / MPL_64_078-115 root integration'
added=[]
def add(sid,typ,outcome):
    if sid in seen:return
    row=dict(zip(cols,[sid,stamp,who,typ,outcome]))
    rows.append(row);added.append(sid);seen.add(sid)

add('R03','targeted proof check','For a mu4-torsor, a fixed section of its mu2 quotient has a mu2-torsor fibre, checked after etale trivialization. This validates the fixed-alpha/all-alpha distinction conditional on the manuscript pinning torsor, not its full construction.')
add('R04','targeted proof check','Preservation of the orientation forces an even permutation, and preservation of t forces its fixed-point equation. Used the finite S3 action; no profinite torsion classification checked.')
add('R13','targeted proof check','Evaluation of alpha:mu4star->omega_J at a chosen i identifies alpha with an orientation; inverse is the unique equivariant bijection. The choice of i is retained.')
add('R14','targeted proof check','A root i is available after the same base change for every parameter, whereas j=1728 imposes a special equation; hence the base change alone is not a CM condition. No LM6 or LM7 image theorem checked.')
add('R16','used and rechecked in this run','Compared frozen096 uncertain V_J label, frozen100 explicit k^J basis and Hua coordinate convention. Three standard ambient vectors cannot be a basis of the two-dimensional V_J; ink remains unresolved.')
add('R17a','targeted proof check','Verified the three values -1/t,1/(1-t),0 are distinct for t!=0,1; Vandermonde and odd-function vanishing prove the scan105-106 restriction kernel as stated for nonzero delta.')
add('R17b','targeted proof check','Compared107 proof using -wp^3 with Vieta and114(59); roots1,2,3 give x^3-6x^2+11x-6. Only algebraic compatibility of frozen degree/sign alternatives tested, no paleographic decision.')
add('R18','targeted proof check','Trace_J(1)=3 proves the direct-sum complement when3 is invertible; in characteristic3 constants are in the kernel and translation leaves a1 unchanged. Confirms the manuscript qualification.')
add('RC10a','used and rechecked in this run','Compared the inserted left-action wording at089 with Hua right-action wording; an inversion convention is needed to compare actions. Documentary/convention comparison, not a new group theorem.')
add('RC10b','used and rechecked in this run','Compared085 Torelli deletion/Jacobi insertion with086 retained Legendre-Torelli and Hua unread-name note. A local terminological comparison only; no frozen reading changed.')
add('RC10c','used and rechecked in this run','Compared the frozen uncertain sharp-like glyph with Hua explicit acknowledgement of an unidentified zigzag and his natural convention. No new decipherment claimed.')
for letter,prior in [('a','P09'),('b','E14'),('c','E16'),('d','C29'),('e','C35')]:
    add('RC02'+letter,'used and rechecked in this run',f'Checked supplied context file inventory and the truncated MPL_93 {prior} register entry. Used only the available heading/status to define the comparison limit; the missing mathematical statement is neither verified nor refuted.')
for letter,topic in [('a','earlier combinatorics'),('b','octahedral characteristic5 exception and reported Lean check'),('c','four-pointed-line and doubling constructions'),('d','earlier level4 and Kummer claims'),('e','later unfinished pinning attempt'),('f','two transcendental drafts'),('g','normality appendix and inferred exceptional parameter')]:
    add('RC12'+letter,'carried as background without fault found',f'Used Hua interpretation of {topic} solely as an out-of-range reading lead. Current scan overlap and modernized page-to-scan offset checked; original out-of-range images and referenced certificates were not checked, and no mathematical authority upgraded.')
add('P01','used and rechecked in this run','Counted38 scan files and697 inventory rows, checked author markers3..11 then1..6 and101 cover. Compared Hua sectionIV boundary using his page100=scan101; no written total inferred. Documentary count verification only.')
add('LM_140-2 LM_P053 S06','carried as background without fault found','Used the supplied qualified four-Legendre-twists lead for B5-03b; retained medium-confidence and outer-homomorphism caveats. No family or monodromy identification re-proved.')
add('Conrad/Level-structures/2.1','carried as background without fault found','Opened primary handout and used its precise N=2 automorphism statement; the pinning consequence is separately checked under R05.')
add('Milne/EC/IV.7.13','carried as background without fault found','Opened primary author book and used the automorphism statement only in characteristic different from2,3; characteristic3 refinement is an independent computation in R10.')
add('Stacks/031W','carried as background without fault found','Opened the exact perfect-field differential-kernel lemma used by ALG02-R; filtration refinement is independently proved in the algebra record, not attributed to a finite sample.')
add('Stacks/0BYA/53.9.3','carried as background without fault found','Opened plane-curve genus formula and used d=3 in ALG05; smoothness, integrality and completion checked separately.')
add('Sutherland2021/Lecture2/2.1-2.2','carried as background without fault found','Opened primary author lecture notes and compared chord/tangent sign and cases. Did not replace the manuscript characteristic restriction with the source convenient characteristic-not2,3 presentation.')
add('Lynn/Explicit-Addition-Formulae','carried as background without fault found','Opened primary author formulas and compared the general secant/tangent shape, retaining the different coefficient-index convention. Exact identities verified separately in ALG07-R.')
add('RC13a/char0-scope','targeted proof check','Accepted algebra-review distinction: meromorphic exactness implies the stated algebraic deRham Picard-Fuchs relation in characteristic0, with lambda!=0,1, and local periods overC. Global char-p deRham conclusion is not inferred; main note and supporting record qualified.')
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
print(f'{len(added)} actual integration checks/uses recorded at {stamp}; no proof status assigned to missing sources')
