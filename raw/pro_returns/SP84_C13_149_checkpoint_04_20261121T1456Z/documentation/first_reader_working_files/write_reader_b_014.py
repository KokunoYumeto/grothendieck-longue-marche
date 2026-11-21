import json
from pathlib import Path
base=Path('/workspace/scratch/4644e52611c0')
page='149_scan014'
packet=base/'work/packets'/page
tex=(packet/'C.tex').read_text().replace(r'\margin{à vérifier ?}',r'\margin{? à vérifier}')
(base/'edition/reviews'/f'{page}.tex').write_text(tex)
boxes=json.loads(Path('/tmp/reader_b_014_boxes.json').read_text())
changes=[]
def ch(id,place,C,H,final,evidence,crop,confidence,ac,ah,kind,category,marked=False,math=False):
 changes.append(dict(id=id,place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/{page}_{crop}.png',box=boxes[crop],confidence=confidence,against_C=ac,against_H=ah,kind=kind,error_category=category,marked_in_H=marked,mathematical=math))
ch('c01','Corollary heading',r'\uline{Corollaire}',r'\textbf{Corollaire}',r'\uline{Corollaire}','One continuous horizontal line is drawn below the entire heading. The source emphasis is underlining, which is preserved explicitly.','c01','high',False,True,'other','Other')
ch('c02','Proof opening, between ouvert and invariant',r'\inserted{$\Gamma\prime$}',r'$\Gamma\prime$ on the baseline without insertion marking',r'\inserted{$\Gamma\prime$}','Gamma-prime stands above the line, and its curved leader descends to the gap before invariant. Its raised position and attachment are unambiguous; the prime is a separate high short stroke.','c04','high',False,True,'insertion or placement','Insertions put in the wrong place',math=True)
ch('c03','Proof opening, punctuation after invariant',r'invariant, Il',r'invariant. Il',r'invariant, Il','A detached dark mark descends in a curved tail after invariant. It is a comma, not a point. Capital Il follows and is retained without normalization.','c04','high',False,True,'misread symbol or index','Symbols and indices')
ch('c04','Left marginal verification note beside bien connu (?)',r'\margin{à vérifier ?} placed after the clause about the centre',r'\marginal{? à vérifier} after the whole proof paragraph',r'\margin{? à vérifier} beside the clause about the centre','The large question mark is above the slanted words à vérifier, rather than following their right end. The note is physically beside bien connu (?) / the assertion about the centre. The output places the marginal note at that clause and orders the above-line question mark first. Crop c05 is rotated 30 degrees clockwise; its recorded box remains in original coordinates.','c05','high',True,True,'insertion or placement','Insertions put in the wrong place')
ch('c05','Revenant paragraph, first subgroup symbol',r'\unsure{\mathcal E|\epsilon}',r'E\prime',r'\unsure{\mathcal E|\epsilon}','The glyph consists of two rounded open lobes without the straight main stem and arms of the neighboring ordinary E. It has no detached prime at the upper right. Script E and epsilon remain unresolved alternatives, but H’s ordinary primed E does not reproduce either the rounded shape or the absent prime. The whole inclusion is in the audit.','c13','medium',False,True,'misread symbol or index','Symbols and indices',math=True)
ch('c06','Revenant paragraph: on voit donc',r'voit',r'sait',r'voit','The initial stroke forms a low v-shaped join, followed by the compressed round middle and a tall final crossed t. The word has the visible voi sequence, not the initial s/a construction of sait.','c14','high',False,True,'misread word','Words')
ch('c07','Revenant paragraph: ambient group after centralisateur ... dans',r'E_{\bar K/K}',r'E',r'E_{\bar K/K}','Below and to the right of E are two K forms separated by a nearly upright oblique slash. A short overbar lies above the first K only. The entire written extension index is present, so the bare E in H omits source ink.','c15','high',False,True,'omission','Omissions',math=True)
ch('c08','Closing paragraph, after la trace de',r'\unsure{\mathcal E\prime|\epsilon\prime}',r'E\prime',r'\unsure{\mathcal E\prime|\epsilon\prime}','The symbol is again rounded, with a large open upper lobe and a lower turned foot; it lacks the ordinary E’s upright stem and horizontal arms. A separate raised oblique stroke at the upper right is plainly a live prime. The alphabet choice remains open, while the prime is certain.','c19','medium',False,True,'misread symbol or index','Symbols and indices',math=True)
ch('c09','Extreme lower-left foliation',r'\margin{13}',r'(omitted)',r'\margin{13}','A small thin 1 with a long entry stroke is followed by the two rounded lobes of 3. The number is in the lower-left corner, distinct in size and pen weight from the main writing; it is assigned to another or uncertain hand.','c20','high',False,True,'omission','Omissions')

marks=[
 ('M0987',r'\unsure{Z|\mathcal Z}','c06','The first centralizer glyph has a small upper rounded lobe, a larger lower lobe and a leftward foot. There is no angular-Z comparison on this leaf that would settle plain versus script alphabet.'),
 ('M0988',r'\unsure{Z|\mathcal Z}','c07','The map source repeats the rounded lobes and leftward foot. The rightward map arrow, Gamma index and prime are clear, but the Z/script-Z alphabet distinction is not. The entire map is retained in the audit.'),
 ('M0989',r'\unsure{Z|\mathcal Z}','c08','Before est fini the glyph repeats the same rounded upper/lower construction and long lower leftward sweep. It does not provide a new angular comparator.'),
 ('M0990',r'\unsure{éléments|élémts}','c10','The initial accented e, tall l and second accented e are followed by a highly compressed flat medial run and a raised t-like join into the terminal s. The reduced reading élémts looks plausible, but the middle run does not securely resolve the presence or absence of e/n; no expansion is imposed.'),
 ('M0991',r'\unsure{Z|\mathcal Z}','c12','After tau-not-in the centralizer again has rounded lobes and a leftward foot. The membership-negation sign is distinct and clear; the alphabet remains undecided.'),
 ('M0992',r'\unsure{Z|\mathcal Z}','c12','Before =(1) the same rounded glyph has a short upper hook and broad lower leftward foot. The whole equality is clear except for the plain/script alphabet choice.'),
 ('M0993',r'\unsure{\mathcal E|\epsilon}','c13','Two rounded open lobes distinguish the first symbol from the adjacent ordinary E. No prime is present. Script capital E and epsilon both fit the surviving shape, so the alphabet remains undecided.'),
 ('M0994',r'\unsure{Z|\mathcal Z}','c15','The centralizer glyph before dans E has the same lobes, with a small loop at its leftward foot. That flourish is consistent with script Z but does not establish an alphabet distinct from a freely written plain Z.'),
 ('M0995',r'\unsure{Z|\mathcal Z}','c17','At the start of the inclusion into pi, the upper hook and long lower sweep again match the preceding centralizer glyphs. The whole inclusion is covered in the audit; the alphabet is not resolved by the group-theoretic context.'),
 ('M0996',r'\unsure{\mathcal E\prime|\epsilon\prime}','c19','A detached upper-right prime is clear. The base glyph has the open lobes and lower foot of the earlier rounded symbol, without enough distinction to choose script E over epsilon.')
]
# Use the same literal apostrophe spelling as the proposed TeX for primed glyphs.
def prime_spelling(s):
 return s.replace(r'\mathcal E\prime',r"\mathcal E'").replace(r'\epsilon\prime',r"\epsilon'").replace(r'\Gamma\prime',r"\Gamma'").replace(r'E\prime',"E'")
for c in changes:
 for key in ['C','H','final']:
  c[key]=prime_spelling(c[key])
decisions=[dict(id=i,decision='undecided',reading=prime_spelling(reading),evidence=e,crop=f'crops/{page}_{crop}.png',box=boxes[crop],confidence='low' if i=='M0990' else 'medium') for i,reading,crop,e in marks]

inv=[]
def el(n,kind,pos,first,hand='main manuscript hand'):
 inv.append(dict(scan=14,sheet_kind='text',hand=hand,element=f'e{n:02}',kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
el(1,'text','top continuation line','égale à 1, ce qui équivaut donc au')
el(2,'text','upper body, three lines including the underlined heading','Corollaire Dans Gamma_Q = Gamma_{Qbar_0/Q}')
el(3,'text','middle body, ten baseline lines','OPS le sous-groupe ouvert ... invariant, Il est bien connu (?)')
el(4,'insertion','above the proof’s first line, leader entering before invariant','Gamma-prime')
el(5,'margin note','left margin beside bien connu (?); question mark above the slanted phrase','? / à vérifier')
el(6,'text','lower body, six baseline lines','Revenant à rounded E-like subgroup symbol subset E_{Kbar/K}')
el(7,'text','extreme lower-left corner','13','another or uncertain hand; small thin foliation')

ab=[]
def audit(n,kind,b,reading):
 ab.append(dict(box=f'b{n:02}',kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=prime_spelling(reading)))
audit(1,'prose',boxes['c02'],r'égale à $1$,')
audit(2,'prose',boxes['c01'],r'\uline{Corollaire} Dans $\Gamma_{\mathbb Q}=\Gamma_{\overline{\mathbb Q}_0/\mathbb Q}$,')
audit(3,'prose',boxes['c03'],r'à $(1)$.')
audit(4,'insertion',boxes['c04'],r'ouvert \inserted{$\Gamma\prime$} invariant, Il est')
audit(5,'margin (slanted)',boxes['c05'],r'\margin{? à vérifier}')
audit(6,'prose',boxes['c09'],r'réduit à $1$')
audit(7,'prose',boxes['c06'],r'donc si $\unsure{Z|\mathcal Z}$ est son centralisateur dans $\Gamma_{\mathbb Q}$,')
audit(8,'formula',boxes['c07'],r'\unsure{Z|\mathcal Z}\longrightarrow\Gamma_{\mathbb Q}/\Gamma\prime')
audit(9,'prose',boxes['c08'],r'$\unsure{Z|\mathcal Z}$ est')
audit(10,'prose',boxes['c10'],r'\unsure{éléments|élémts} $\neq1$ de $\Gamma_{\mathbb Q}$')
audit(11,'prose',boxes['c11'],r'$\Gamma_{\overline{\mathbb Q}}$ est réduit à $(1,\tau)$,')
audit(12,'formula',boxes['c12'],r'$\tau\notin\unsure{Z|\mathcal Z}$, donc $\unsure{Z|\mathcal Z}=(1)$.')
audit(13,'formula',[895,1624,1218,1750],r'$\unsure{\mathcal E|\epsilon}\subset E_{\bar K/K}$,')
audit(14,'prose',boxes['c14'],'on voit donc')
audit(15,'prose',[979,1752,1458,1871],r'$\unsure{Z|\mathcal Z}$ dans $E_{\bar K/K}$')
audit(16,'prose',boxes['c16'],r'$\Gamma$ réduite à $\{1\}$,')
audit(17,'formula',boxes['c17'],r'\unsure{Z|\mathcal Z}\subset\pi_{\bar K/K}')
audit(18,'formula',boxes['c18'],r'\pi\prime\subset\pi=\pi_{\bar K/K}')
audit(19,'prose',boxes['c19'],r'$\unsure{\mathcal E\prime|\epsilon\prime}$ sur $\pi$,')
audit(20,'number',boxes['c20'],r'\margin{13}')
# Normalize pi-prime spelling too, matching the source fragment.
for b in ab: b['reading']=b['reading'].replace(r'\pi\prime',r"\pi'")

cov=[]
def cv(row,classification,change,reason):
 cov.append(dict(row=row,classification=classification,change_id=change,reason=reason))
cv(1,'editorial-only',None,'scanpage 14 is metadata, not a source number at the top.')
cv(2,'material','c03','A comma follows invariant; H’s full stop is not the source mark.')
cv(3,'material','c04','The note is beside the assertion about the centre; its above-line question mark is ordered before the phrase.')
for row,mark in [(4,'M0987'),(5,'M0988'),(6,'M0989')]:
 cv(row,'reading-agrees',None,f'H’s plain Z is one of C’s retained alternatives. {mark} remains explicitly undecided; uncertainty alone is not counted as a material correction.')
cv(7,'reading-agrees',None,'H’s éléments remains one candidate, but the reduced élémts alternative cannot be dismissed. M0990 is not resolved or expanded by sense.')
for row,mark in [(8,'M0991'),(9,'M0992')]:
 cv(row,'reading-agrees',None,f'H’s plain Z remains one of the two alternatives; {mark} is undecided, with the whole formula audited.')
cv(10,'material','c04','The marginal-note placement/order is addressed in c04. H’s separate gloss of OPS is editorial and is not inserted into source text.')
cv(11,'material','c05','The first rounded E-like glyph has no prime and differs graphically from H’s ordinary E-prime; its script-E/epsilon choice remains open.')
cv(12,'material','c06','The source reads voit.')
cv(13,'reading-agrees',None,'M0994 retains plain Z versus script Z; no certain alternative to H’s Z is adopted.')
cv(14,'material','c07','The complete extension index Kbar/K is visible after E.')
cv(15,'reading-agrees',None,'M0995 retains the alphabet doubt; H’s plain Z remains a candidate.')
cv(16,'material','c08','The closing subgroup glyph is rounded and has a clear prime; script E-prime versus epsilon-prime remains open rather than silently becoming ordinary E-prime.')
cv(17,'material','c09','The thin small foliation 13 is visible and retained.')

places={
'M0987':'first centralizer symbol after donc si',
'M0988':'source of the map to Gamma_Q/Gamma-prime',
'M0989':'centralizer symbol before est fini',
'M0990':'éléments/élémts before not-equal 1',
'M0991':'centralizer symbol after tau-not-in',
'M0992':'centralizer symbol in =(1)',
'M0993':'first rounded subgroup symbol after Revenant à',
'M0994':'centralizer symbol before dans E_{Kbar/K}',
'M0995':'centralizer symbol in the inclusion into pi_{Kbar/K}',
'M0996':'last rounded subgroup symbol after la trace de'
}
doubts=[]
for d in decisions:
 if 'mathcal Z' in d['reading']: alternatives=['Z',r'\mathcal Z']
 elif d['id']=='M0990': alternatives=['éléments','élémts']
 elif d['id']=='M0993': alternatives=[r'\mathcal E',r'\epsilon']
 else: alternatives=[r"\mathcal E'",r"\epsilon'"]
 doubts.append(dict(place=f"{d['id']}: {places[d['id']]}",reading=d['reading'],alternatives=alternatives,confidence=d['confidence'],reason=d['evidence']))

report=dict(
 scan=14,reader='/root/reader_b',lines_read=24,changes=changes,decisions=decisions,inventory=inv,
 notes=[
  'Run SP84_C13_149; reader GPT-6 Astra Pro, effort not exposed. The full image was inspected once for layout and each supplied half once. Every word and inline formula was read against the ink. Sixteen retained enlarged crops were personally inspected. No OCR, external research, TeX compilation, or mathematical check was performed.',
  'The leaf continues a sentence, states an underlined Corollaire concerning centralizers of open subgroups in Gamma_Q, gives an argument involving finite-order elements and complex conjugation, then returns to the subgroup of E_{Kbar/K} and its trace in pi. These are source assertions, not checked proofs. The source’s own (?) after bien connu and marginal ? à vérifier are both retained.',
  'There is no author page number, title beyond the local Corollaire heading, or date. The lower-left 13 is small and thin, attributed to another or uncertain hand and encoded with margin. The count of 24 manuscript line units comprises 20 main baseline lines, the one-line Gamma-prime insertion, two levels of the marginal note, and the foliation.',
  'The source underline beneath Corollaire, the inserted Gamma-prime above invariant, the comma followed by capital Il, and the upper placement of the marginal question mark are preserved. The question mark precedes à vérifier in the linear transcription, and the note remains adjacent to the assertion about the centre.',
  'All seven centralizer glyphs share rounded 3-like upper/lower lobes and a leftward lower foot. They do not supply an independent angular-versus-script comparison. Consequently all seven Z/script-Z choices are retained; the consistency establishes the recurring shape, not a certain alphabet.',
  'The two subgroup glyphs are rounded E/epsilon-like forms distinct from the adjacent ordinary E. Their alphabet remains unresolved. The first has no prime; the closing occurrence has a clear detached prime. H’s first E-prime therefore supplies a prime not visible in the source.',
  'The initial letters and final t/s-like construction of éléments/élémts are visible, but the medial run is reduced to a nearly flat joining stroke. The abbreviated reading looks plausible; the full word is not supplied from the mathematical sense. M0990 remains open.',
  'The first Gamma in the corollary has a looped return along its left stem, while the following Gamma is locally retraced more narrowly. Ordinary Gamma is retained: the loop does not establish a deliberate separate alphabet. This graphic judgment is explicit, and the entire equality with its zero index is in the audit. Q has a repeated inner/doubled stroke and remains double-struck.',
  'The map from the centralizer to Gamma_Q/Gamma-prime has a right arrowhead and no left mapsto bar. The source writes Gamma with barred Q in the later tau-centralizer line; no missing quotient denominator is supplied. Parentheses in (1) and (1,tau) and braces in {1} remain distinct.',
  'All ten packet marks remain unresolved in the proposed text. The audit set covers their entire inline formula units, every insertion and marginal note, every different word, and all nine numeral locations including the Qbar-zero index. Numeric or already-settled boxes c09/c11/c16/c18 were not retained as first-pass images; they remain audit rectangles. Crop c05 is rotated 30 degrees clockwise, with its unrotated original-image coordinates recorded.',
  'The retained first-pass crop paths are c01 through c08, c10, c12 through c15, c17, c19 and c20. No source deletions or separate drawings/diagrams are visible on this leaf; the heavy retraced strokes in est and the ordinary E forms are not encoded as cancellations.'
 ],
 checks=[],
 hand=[
  dict(habit='Centralizer symbols have small rounded upper lobes, larger lower lobes and a leftward foot.',pages=[14],consistency='Seven occurrences in c06/c07/c08/c12/c15/c17 match this construction; some feet close into a tiny loop.',misread='No distinct angular-Z comparator settles the plain/script distinction; all seven choices remain open rather than regularized to H’s plain Z.'),
  dict(habit='Rounded open subgroup glyphs are graphically distinct from ordinary E, and a prime is a separate high stroke.',pages=[14],consistency='c13 has the rounded glyph without prime beside a straight-stem E; c19 has the rounded glyph with prime.',misread='H writes ordinary E-prime for both, adding a prime at the first occurrence. Script E versus epsilon is still not settled.'),
  dict(habit='Interlinear insertion leaders curve to a gap in the baseline.',pages=[14],consistency='The Gamma-prime over invariant has a clear curved leader and separate prime.',misread='H leaves the symbol inline without its insertion state.'),
  dict(habit='Letter runs may be compressed into nearly flat strokes.',pages=[14],consistency='The middle of éléments/élémts is flat, whereas the initial accented letters and final t/s construction remain distinct.',misread='The flat run cannot justify expansion to the full word from meaning; the abbreviation doubt is retained.'),
  dict(habit='Retracing and looped return strokes can thicken ordinary capitals.',pages=[14],consistency='The first two Gamma forms in the corollary and the ordinary E forms show locally differing retracing.',misread='No doubled alphabet is inferred solely from the looped first Gamma stem; its full formula remains available for independent review.')
 ],
 notation=[
  dict(written='Gamma_Q = Gamma with Qbar-zero/Q index',rendering=r'\Gamma_{\mathbb Q}=\Gamma_{\overline{\mathbb Q}_0/\mathbb Q}',meaning='Ambient group named in the corollary.',evidence='c01; the small zero follows the barred first Q in the index and the second Q is unbarred.'),
  dict(written='Gamma-prime raised above invariant',rendering=r"\inserted{$\Gamma'$}",meaning='The open subgroup that the proof supposes invariant.',evidence='c04; one left stem and roof, separate upper-right prime, and insertion leader.'),
  dict(written='Repeated rounded centralizer glyph',rendering=r'\unsure{Z|\mathcal Z}',meaning='The centralizer named in each paragraph; alphabet not settled.',evidence='c06, c07, c08, c12, c15, c17; rounded lobes and leftward foot recur.'),
  dict(written='Rightward shaft with a visible pointed end',rendering=r'\longrightarrow',meaning='The written map from the centralizer to Gamma_Q/Gamma-prime.',evidence='c07 shows the right arrowhead and the absence of a left mapsto bar.'),
  dict(written='Rounded open E-like symbol, later with prime',rendering=r"\unsure{\mathcal E|\epsilon},\quad\unsure{\mathcal E'|\epsilon'}",meaning='Subgroup referred to in the Revenant paragraph; alphabet unresolved.',evidence='c13 and c19; first occurrence unprimed, last occurrence primed.'),
  dict(written='Ordinary E with bar over first K of an extension index',rendering=r'E_{\bar K/K}',meaning='Ambient group of the closing paragraph.',evidence='c13 and c15; the complete index is visible in both occurrences, including the one omitted by H.'),
  dict(written='pi with bar-K/K index',rendering=r'\pi_{\bar K/K}',meaning='Group into which the centralizer is then included and in which the trace is taken.',evidence='c17 and the following same-baseline pi-prime inclusion; compact two-legged pi with a broad top bar and explicit extension index.'),
  dict(written='tau and Gamma indexed by barred Q',rendering=r'\tau,\quad\Gamma_{\overline{\mathbb Q}}',meaning='Complex conjugation and the group written in its centralizer sentence.',evidence='Middle/lower proof lines read in the supplied halves; the overbar above Q is retained literally.')
 ],
 abbreviations=[
  dict(form='OPS',expansion='on peut supposer',place='proof opening; expansion appears only in H’s editorial gloss, not in source transcription'),
  dict(form='hom',expansion='homomorphisme',place='l’hom preceding the centralizer map'),
  dict(form='élémts (possible reading)',expansion='éléments',place='M0990 before not-equal 1; abbreviation itself remains doubtful')
 ],
 doubts=doubts,audit_boxes=ab,diff_coverage=cov
)
(base/'edition/reviews'/f'{page}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':page,'changes':len(changes),'decisions':len(decisions),'inventory':len(inv),'audit_boxes':len(ab),'diff_rows':len(cov),'retained_doubts':len(doubts),'retained_crops':16}))
