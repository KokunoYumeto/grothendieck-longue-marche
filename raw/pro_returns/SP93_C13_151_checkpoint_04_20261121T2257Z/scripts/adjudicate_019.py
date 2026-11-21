from pathlib import Path
import json,csv
R=Path('/workspace/scratch/d12e26a9cd50/SP93_C13_151_work');p=R/'reports/151_scan019.json';d=json.loads(p.read_text());tp=R/'reports/151_scan019.tex';t=tp.read_text()
rows=list(csv.DictReader((R/'second/151_scan019_comparison.tsv').open(),delimiter='\t'));f={r['box']:r['first'] for r in rows};b={r['box']:[int(r[k]) for k in ('x0','y0','x1','y1')] for r in csv.DictReader((R/'second/151_scan019_boxes.tsv').open(),delimiter='\t')}
rev={}
rev['B001']=f['B001'].replace(r'\&K\&{}',r'\&K.\&{}').replace(r'I,J,K\leq3',r'I,J;K\leq3')
assert r'\&K\&{}' in t;t=t.replace(r'\&K\&{}',r'\&K.\&{}',1).replace(r'I,J,K\leq3',r'I,J;K\leq3')
old=r"X'_1\arrow[l]\arrow[u,no head]"
new=r"X'_1\arrow[l]\arrow[u,no head,to path={(\tikztostart.north)--([yshift=-6pt]\tikztotarget.south)..controls([yshift=-2pt]\tikztotarget.south)and([xshift=-5pt,yshift=-2pt]\tikztotarget.south)..([xshift=-5pt,yshift=-5pt]\tikztotarget.south)\tikztonodes}]"
assert old in t;t=t.replace(old,new);rev['B003']=f['B003'].replace(old,new)
old3=r'\mathbb E_{n-1}\arrow[r]\&\mathbb E_n'
new3=r'\mathbb E_{n-1}\arrow[r,to path={(\tikztostart.east)--++(4pt,-2pt)--(\tikztostart.east)--(\tikztotarget.west)\tikztonodes}]\&\mathbb E_n'
assert old3 in t;t=t.replace(old3,new3);rev['B010']=f['B010'].replace(old3,new3)
old4=r'\arrow[r,no head,"{\deleted{\unsure{\alpha}}}"]'
new4=r'\arrow[r,no head,"{\deleted{\unsure{\alpha}}}",to path={(\tikztostart.east)--([xshift=-2pt]\tikztotarget.west)--++(0,3pt)\tikztonodes}]'
assert old4 in t;t=t.replace(old4,new4);rev['B011']=f['B011'].replace(old4,new4)
oldx=r'\deleted{X^2}\&\deleted{X_1}\arrow[l]'
newx=r'\deleted{X^2}\&\deleted{X_{\unsure{1}}}\arrow[l]'
assert oldx in t;t=t.replace(oldx,newx);rev['B021']=f['B021'].replace(oldx,newx)
for c in d['changes']:
 c['final']=c['final'].replace(old,new).replace(old3,new3).replace(old4,new4).replace(oldx,newx)
c=next(c for c in d['changes'] if c['id']=='019-C04');c.update(C='3',H='3.',final='3')
c=next(c for c in d['changes'] if c['id']=='019-C09');c.update(final=new,differs_C=True,evidence='The middle vertical rises to a small curved cap returning left; no two-branch arrowhead is visible. The curved headless terminal replaces the straight headless shaft. Both outer shafts retain full upward chevrons.',crop='crops/151_scan019_second_B003.png',box=b['B003'])
c=next(c for c in d['changes'] if c['id']=='019-C21');c.update(final=rev['B010'],differs_C=True,evidence=c['evidence']+' The bottom rightward arrow also has a short downward-right return at its left endpoint, without a second complete arrowhead; that return is now preserved.',crop='crops/151_scan019_second_B010.png',box=b['B010'])
c=next(c for c in d['changes'] if c['id']=='019-C22');c.update(final=rev['B011'],differs_C=True,evidence=c['evidence']+' The lower horizontal stroke ends in a short upward tick at the right, not a flat blunt end or a completed chevron.',crop='crops/151_scan019_second_B011.png',box=b['B011'])
c=next(c for c in d['changes'] if c['id']=='019-C49');c.update(final=rev['B021'],evidence='The top leftward arrow, upper X squared, lower equality and left upward chevron are visible. A short dark trace at the lower right of the upper-right X overlaps the long cancellation; its reading as subscript 1 is now left uncertain. The smaller lower-right X/x doubt remains. No complete upward head is visible on the curled right shaft.',crop='crops/151_scan019_second_B021.png',box=b['B021'])
for ident,place,C,H,final,evidence in [
 ('019-A01','Bound under the first diagram, separator after J',',',',',';','There is a separate dark point above a curved descending comma immediately after J. The two components form a semicolon; both witnesses supply a comma.'),
 ('019-A02','First fork, punctuation after K','K','K','K.','A separate dark full stop sits immediately to the lower right of K at its baseline. It is distinct from the curved headless branch above and from pale paper specks.')]:
 d['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=evidence,confidence='high',kind='other',crop='crops/151_scan019_second_B001.png',box=b['B001'],differs_C=True,differs_H=True,consequential='',marked_in_H='no'))
d['doubts'].append(dict(place='Cancelled X square, upper-right node',reading=r'\deleted{X_{\unsure{1}}}',alternatives=['X with subscript 1','X with the apparent subscript belonging to the cancellation'],confidence='low',reason='The putative short subscript meets the long almost vertical cancellation. Its complete outline cannot be isolated; the blind reader omitted it, while the first reading supplied 1.'))
d['notes'].append('Independent audit: the bound has a semicolon after J and the first fork has a full stop after K. The middle X-grid shaft has a curled headless top; case III has a short left-end return on its bottom arrow; case IV has an upward terminal tick on its bottom stroke. The cancelled upper-right X subscript is newly uncertain. The case-II lower-left n-1 and the isolated fork lower n are retained as written; no expected index is substituted. Large enclosing and cancellation courses were already represented in the complete page, even where absent from an isolated first-reading box snippet.')
e={
 'B001':'The separate dot after K and the two-component semicolon after J are visible and are added. The circled authorial 2 and printed header agree. The two epi arrows have heavily retraced single terminal shapes, not a securely separated second tip; the existing head-count doubt remains. J has two headless branches.',
 'B002':'The lower central crossed trace has a K-like upright and branches, but its prime remains obscured. The first unsure K-prime is retained rather than deleting the possible prime. The lower-right point is filled and its incoming stroke has no head; all other nodes and directions agree.',
 'B003':'The middle vertical ends in a small cap curving back to the left, without a chevron. That curl replaces the straight headless terminal. The lower-right crossing letter remains locally uncertain X/x; the outer up-arrows and the six indexed nodes otherwise agree.',
 'B004':'The I and I-prime square has the two amalgam labels, complete top inclusion head, headless bottom hook and headless right vertical. The dark retracing of J-prime does not establish a distinct cancelled old letter. The first reading is retained.',
 'B005':'The lower-right X has crossing diagonals despite retracing, and K-prime has a detached prime. The old product is crossed out and replaced below by X of the amalgam. The right vertical has a curled headless top already encoded. The second doubt around X does not require a new competing letter.',
 'B006':'The serifed I and the complete rightward arrow to a blank endpoint agree; inline and diagram wrappers differ only in syntax.',
 'B007':'The left vertical belongs to the upper-left E and ends at E-sub-n, with no minus-one at the lower object. The K upright and branches match the capital form elsewhere. The curved top label does not remove the established delta/partial homography doubt. Both full arrowheads are visible.',
 'B008':'A u-like trough and uprights remain beneath dense crossing strokes, but the whole underlying form is not securely separable. The first deleted unsure u remains an explicit uncertain candidate; the second illegible marker supplies no contrary legible reading.',
 'B009':'The lower-left index is n followed by a horizontal minus and a separate 1; no vertical crosses the minus. It is retained as n-1. The full-page figure already contains the large enclosing course, whose local section appears in the second snippet. The curved labels remain delta/partial doubts.',
 'B010':'The four doubled-E objects, n>=2 and circled III agree. The bottom arrow has a short downward-right return at its left endpoint, so that stroke is added. K retains the full-height form. The long outside enclosure is already present in the full page.',
 'B011':'The bottom headless connector has a short upright tick at its right end; it is added without completing a chevron. The left K has a raised prime, and the two crossed edge labels retain alpha as uncertain candidates. The extra crossed subscript remains unsure. The wave and outside enclosing course are already present.',
 'B012':'K with two detached primes is visible on the left; the top K, four E objects, range 4 and circled V agree. The lower connector has only its upper terminal wing, already encoded. The continuous outside curve belongs to the full four-case figure.',
 'B013':'The lower p and q are crowded and a short intervening trace cannot be confidently assigned to their pen joins or to plus. The existing unsure plus remains. Both complete arrows, p,q>=1, circled I and the upper-left gap in the enclosure agree.',
 'B014':'After p= the closed small left lobe has a crossing upright extending above and below, supporting the previously read closed form of 4 rather than a plain 0. The two struck numerals remain uncertain. All live counts agree. The first frame preserves its upper-left gap and open right side.',
 'B015':'The crossing diagonal traverses a short upright and right loop, supporting the p-like candidate. It does not expose the whole original form, so the first p/asterisk doubt remains.',
 'B016':'The two bars of the retraced equality in n=2 remain separately visible. All six entries and I-prime agree; the left table boundary is already encoded in the full-page figure.',
 'B017':'The five live counts are 2,1,1,1,1. The black strip at the right is the scanned sheet edge, not a drawn table rule, and no right border is added.',
 'B018':'The two E-like old nodes and raised traces remain uncertain under the cancellation. Both rightward shafts and the capped segment are present. Short apparent reverse-head branches coincide with the long cancellation paths and do not establish additional map directions. The complete page already includes those cancellation courses.',
 'B019':'The upper curve, descending diagonal and foot of 2 are clear. Both readers mark the numeral deleted; the placement of math delimiters alone differs.',
 'B020':'The upper-right E has two uprights and three arms; the upper hooked continuation meets the cancellation and does not establish a separate exponent 2. The lower raised strokes remain prime/1 doubts. Apparent arrowhead branches on top and left run into long cancellation courses, so the first headless shafts remain. The separate right-hand 1 and lower equality are visible.',
 'B021':'The top-right X is clear but its short supposed subscript intersects the long cancellation; 1 is now marked uncertain. The lower-left 1 is clear, while the smaller lower-right X/x remains doubtful. The right shaft ends in curls without a complete chevron, as already encoded; the upper segment is present elsewhere in the complete figure.',
 'B022':'The left capped short course lies above the boundary, a separate middle tick descends below it, and the two right ticks cross it. Those strokes are already in the page. The other courses are portions of the full cancellation paths rather than additional table rules.'}
m={k:dict(changed=k in rev,evidence=v) for k,v in e.items()}
for k,v in rev.items():m[k]['final']=v
(R/'reviews/151_scan019_manual.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');tp.write_text(t)
