from edition.scripts.root_audit import Audit

a=Audit(124)
a.keep('B01','The author foliation has a closed lower bowl and long rising entry for 6, followed by a single upright 1. Only the foliation wrapper differs.')
a.keep('B03','The canceled capital retains an upright and roof but is crossed diagonally, leaving T versus Z unresolved. Its lower d has no independent prime before the next lower D; the base ends with a clear d-prime. The first uncertainty remains appropriate.')
old=r"T(d^{\unsure{*}},d')_{d'}"
new=r"T(d^{\unsure{*}},\unsure{d'|d})_{d'}"
f=a.comparison['B05']['first'].replace(old,new)
a.change('B05',f,'Both high clusters after the first d in the second row contain extra angular strokes; they remain star-like versus altered-prime uncertain. After the second argument d, the apparent prime meets the upper turn of the closing parenthesis, so d-prime versus bare d cannot be securely separated. The lower d-prime, base indices, brace and descriptive lines remain as first read.')
a.replace(old,new)
a.add_row('B05','Second argument of T in the second row of (193)',r"T(\unsure{d|d^*},d')_{d'}",r"T(d,d')_{d'}",new,'medium','index','prime overlaps parenthesis',True,True,True)
a.doubt('Second argument of T in the second row of (193)',r"\unsure{d'|d}",'The high short trace touches the beginning of the closing parenthesis; it may be a separate prime or only the parenthesis entry.','medium')
a.keep('B08','The right separator is a small low dot without the descending curved tail seen in the left comma. The connector terminates in a short transverse cap rather than a complete two-barbed head. Both primes and (194) are clear.')
a.keep('B09','Both decorated D forms have a separated upright and lower dot. The multiplication cross has D_d below it, and the last factor is literally D_{d-prime}, with no additional d supplied. The difference is script order and wrappers.')
a.keep('B10','After the open c, the oval has a raised exit characteristic of a, followed by one long n shoulder and a point. There is no second m shoulder to favor com.; can. remains the graphical reading.')
a.keep('B11','The diagram has six objects and seven connections: the dashed top, upper-left, right vertical and lower-right have full heads; the two inner edges have single terminal returns; the lower-left edge is headless. The raised (I_d), lower base D_d with bang, broad S labels and unresolved high cluster are visible. No extra prime is independently visible in the base beneath the upper-left expression.')
a.keep('B12','Although retraced, the first letter retains an upper leftward curl and lower returning S-shaped body, followed by a detached apostrophe. The subsequent identifie is clear; no separate canceled word can be isolated from the retracing.')
a.keep('B14','The Z characters have doubled diagonals, with d and d-prime above. The connector ends in the same short transverse cap as (194), with no converging full head. The label is (196).')
a.keep('B15','The abbreviated group has an opening e return, short n shoulder and extended final s turn, matching ens. It has no separate following point. The initial tall l and apostrophe are clear.')
f=r'$\mathbb Z^d\simeq\mathbb Z^{I_d}$\unsure{.|,}'
a.change('B16',f,'The relation has one wave above a straight bar, and I_d is raised above the right Z. The final dark mark is oblong with a short oblique extension; a point is plausible, but the blind comma reading cannot be excluded from its shape.')
a.replace(a.comparison['B16']['first'],f)
a.add_row('B16','Punctuation at the end of the final equivalence',r'$\mathbb Z^d\simeq\mathbb Z^{I_d}$.',r'$\mathbb{Z}^{d} \simeq \mathbb{Z}^{I_d}$.',f,'medium','punctuation','point versus comma',True,True)
a.doubt('Punctuation at the end of the final equivalence',r'\unsure{.|,}','The oblong dark point has a short oblique extension, so point versus comma is unresolved.','medium')
a.keep('B17','The pencil foliation reads 123: a single upright, sloping 2 with a baseline return, and two rightward bowls for 3. The margin macro is the only difference.')
for e in a.report['inventory']:
 e['first_words_or_objects']=e['first_words_or_objects'].replace(old,new)
a.note('Blind audit: all 12 differing boxes were inspected. The second argument in the lower line of (193) retains d-prime|d because the small high stroke meets the parenthesis, and the final punctuation retains point|comma. The altered high clusters, canceled T|Z, transverse connector caps, literal six-object diagram and abbreviated can. and ens were retained from visible strokes.')
a.finish()
