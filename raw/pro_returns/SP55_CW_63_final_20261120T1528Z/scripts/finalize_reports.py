"""Finalize report metadata after the primary reader's 26 ordered image audits.

This script does not read images or change any page transcription. The explicit
indices below classify mathematical omissions already recorded by the reader.
"""
from editorial import *

mathematical_omissions = {
    21: [6,7,9,10,11,12,13,14,15,16],
    22: [1,2,3,5,6,8,10,11,12,13],
    27: [0,1,2,3,4,5,6,7],
    30: [0,1,2,4,5,6,7,8,9,10,11,12],
    32: [1,2,3,5,6,7,8],
    33: [0,1,2,3,4,5,6,7,8,9],
    34: [1,2],
}
records=[]
for p in sorted((ROOT/'records').glob('scan*.json')):
    r=json.loads(p.read_text())
    assert r.get('audited'), r['scan']
    for index,c in enumerate(r['changes']):
        c['consequential'] = (
            index in mathematical_omissions.get(r['scan'],[])
            or (r['scan']==29 and c['place']=='display after (4.4), R')
            or (r['scan']==34 and c['kind']==r'readable ink left as \ill{}')
        )
    p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    records.append(r)
assert len(records)==26

notation = [
 ['21–34; 42–52','c, C, c_4, c_6 and c(n)',
  'The French invariants and English Fourier coefficient are different named objects. The varying height of a handwritten c is not by itself capitalization. Explicit C forms in the French marginal table remain as read; the first C/c remains doubtful. No case is propagated merely from another folder.'],
 ['21–34','Ordinary, heavy and doubled type impressions',
  'The first primed a on 25 and 28 has a local doubled contour. R on 29 is ordinary. Heavy c on 26 and p on 29 remain qualified. The plain F_3 on 31 contrasts with visibly doubled F_4 on 32. Wrappers used to approximate a physical impression do not introduce new algebraic objects.'],
 ['21–34; 42–45, 52','pi and tau in different texts',
  'Pi denotes the invariant differential in the French typescript and the circular constant in the English exponential. English tau denotes the upper-half-plane argument and the coefficient function; scan 45 explicitly acknowledges these two uses. Its detached cap and descender recur across the English pages.'],
 ['28; 50–52','lambda and mu',
  'The French coefficient ratios and the English eigen-coefficient notation are read in their local definitions. English conjugation bars cover individual a and lambda letters, not their arguments; this is checked on both 51 and 52.'],
 ['21, 22; 49–52','g_2, g_3 versus g_n(x)',
  'The French Weierstrass parameters and English modular-function family are different local notations. Their subscript shapes are compared without identifying the mathematical objects across the two texts.'],
 ['42–52','Equality, congruence and equation separators',
  'A third handwritten stroke added to a typed equals sign is retained as congruence. Ordinary equality remains where written, including the extension-field identities on 51–52. Commas in local equation references on 46–47 are not regularized to full stops.'],
 ['47–50','M and R',
  'Scan 47 explicitly names multiplicative M-results and their ramified R-cases. This definition governs later occurrences across the H63-05/H63-06 folder boundary.'],
 ['50–52','GF, Q and German p',
  'GF is explicitly introduced as Galois field on 50; the overmarked first GF on 51 remains doubtful as to alphabet. Q and its roofless radical on 52 are kept as written. The margin names German p, supporting the fraktur form rather than rho.'],
 ['21–34; 41–52','Loops, strikes, additions and blanks',
  'Enclosing a word is not automatically deletion. Source layers remain separate, and cancellation scope is decided at each occurrence. The empty last digit of RANKIN(196 ) on 45 and 52 stays a blank; covered running headings on 43 and 50 stay qualified.'],
]
(ROOT/'notation_global.json').write_text(json.dumps(notation,ensure_ascii=False,indent=2)+'\n')

p=ROOT/'README.md'
s=p.read_text()
start=s.index('## Provisional completion status')
end=s.index('\n## Contents',start)
s=s[:start]+'''## Completion status

All 26 first readings and all 26 second image readings are complete, in the requested order. The recurring notation was compared across both texts and folder boundaries. The 26 page files and combined fragment have been frozen with SHA-256 entries in `progress.log`; the closing verification entry records whether they remained unchanged through final packaging. `READING_STATUS.md` confirms that there is no next page to read.

The comparison records contain 102 distinct places: 14 against C and 89 against H, with one place counted against both. Their confidence counts are 82 high, 19 medium and 1 low. H's total includes 70 omitted blocks on its seven partially transcribed pages. There are 54 remaining doubt entries, 85 certainty/scope entries, 539 inventory elements and 73 check events. The 84 crop boxes are documented without returning images.

The primary reader performed every image reading and every textual decision in one ordered stream. Mechanical assistance checked structure, record consistency and specified finite computations. No OCR, other text-recognition software, external textual research or TeX compilation was used. An encoding repair in the alpha command on scan 46 is documented separately from reading changes.
''' + s[end:]
s=s.replace('abbreviations and legibility assessment; completion is governed by the status above.',
            'abbreviations and legibility assessment.')
s=s.replace('UTC reading/audit events and, when completed, the transcription freeze and SHA-256 verification.',
            'UTC reading/audit events, transcription freeze and closing SHA-256 verification.')
s=s.replace('Those checks are responsibilities of the primary reader\'s final audit.',
            'The primary reader checked doubt scope and notation during the final image audit; mechanical review also checked the declared custom macros and all 26 footer inventory entries. Static checking is not a typeset-layout validation.')
p.write_text(s)

build()
log('reports finalized '+utc()+': abbreviations, legibility, cross-page notation, error-sheet feedback and consequential mathematical omissions completed; no page text changed')
print('Reports finalized; transcription files not edited.')
