from pathlib import Path
import json
from datetime import datetime, timezone

base=Path('out/readers/007/B')
def difference(id,location,C,reading,evidence,confidence,kind,diff_C,status,crop,bbox):
    return dict(id=id,location=location,C=C,H=None,reading=reading,evidence=evidence,
                confidence=confidence,kind=kind,diff_C=diff_C,diff_H=False,
                C_doubt_status=status,readers_crop=crop,bbox={'image':'full','xyxy':bbox})
differences=[
 difference('B007-D01','First line, immediately before Soit',r'\deleted{\illegible{1}}',r'\deleted{\illegible{1}}',
   'The enlargement shows a dense dark patch with overlaid loops and short projecting top strokes. The internal traces do not yield a defensible character sequence. C’s unreadable cancelled unit is retained.',
   'low','other',False,'retained','crops/01_initial_deletion.png',[24,15,174,88]),
 difference('B007-D02','Pale note at right of the divisibility conditions, first sign',r'\unsure{a|\alpha}',r'\unsure{a|\alpha}',
   'A small closed loop is followed by a single descending rightward tail. Its top is crowded and the faint strokes do not isolate a second alpha shoulder. Both a and alpha remain supported; the candidate order is retained.',
   'medium','other',False,'retained','crops/02_pale_note.png',[1006,981,1053,1013]),
 difference('B007-D03','Pale note, word after the first sign',r"\unsure{n'exist|n'existe}",r"\unsure{n'exist|n'existe}",
   'After the n and detached apostrophe, a low letter run ends in a tall stroke with a rightward curved return. The final return supports n’exist; its weak joined portion also leaves n’existe possible. No distinct terminal e is established. The duplicate C_doubts entry refers to this same locus.',
   'medium','other',False,'retained','crops/02_pale_note.png',[1046,967,1182,1010]),
 difference('B007-D04','Cancellation of ou p=1 in the Soit p sentence',r'\deleted{ou $p=1$}',r'\deleted{ou $p=1$}, with two explicit rising diagonal strokes in TikZ',
   'Half a at x=823–1068, y=817–918 shows a long dark rising diagonal and a thinner nearly parallel lower stroke, extending below ou at the left and above the equality at the right. Both strokes are also visible in half b at x=823–1068, y=37–138 (origin of b is full y=780). The words ou p=1 remain readable. The deletion state already agrees with C; the added detail is the paired stroke geometry.',
   'high','drawing or diagram',True,None,None,[823,817,1068,918]),
]

def inv(n,kind,position,first,hand='another unnamed hand'):
    return dict(sheet_kind='text',hand=hand,element=f'007.B.{n:02d}',kind=kind,position=position,first_words_or_objects=first,transcribed='yes')
inventory=[
 inv(1,'deletion','Top left before Soit','Dense blacked-out unit, unreadable'),
 inv(2,'text','Top line','Soit a∈ℕ*, b∈ℕ*, c∈ℕ*, q∈ℕ*; q nombre premier (q≠1)'),
 inv(3,'text','Second main line','On suppose que; three bowl-with-1 coprimality signs; (premiers entre eux deux à deux)'),
 inv(4,'insertion','Left between the second and third main lines','et a^q+b^q=c^q'),
 inv(5,'text','Third main line','On a c>a et c>b car a∈ℕ* et b∈ℕ*'),
 inv(6,'text','Line above the expansion','On pose c=a+b′=b+a′ avec b′∈ℕ* et a′∈ℕ*'),
 inv(7,'display','Two expansion rows in upper middle','alors a^q+b^q=c^q=(a+b′)^q=Σ; (Newton); second row (car q≥2)'),
 inv(8,'display','Display beginning donc','b^q=Σ from i=1 to q−1 plus b′^q; label (1)'),
 inv(9,'text','Three prose lines above the fold','la puissance de b′ n’étant jamais nulle … b′|b^q (b′ divise b^q)'),
 inv(10,'text','First line under the fold','Soit p un nombre premier … et tel que :'),
 inv(11,'deletion','Inside the Soit p line','ou p=1, cancelled by two rising diagonal strokes; both drawn explicitly'),
 inv(12,'text','Next line','p|b′ donc p|b. Soit α∈ℕ* et α′∈ℕ* tels que'),
 inv(13,'display','Two divisibility-pair rows','p^{α′}|b′ et p^{α′+1}∤b′; et p^α|b et p^{α+1}∤b'),
 inv(14,'margin note','Pale two-line note to the right of the first divisibility pair','a/α n’exist/n’existe pas si on avait p=1','undetermined hand'),
 inv(15,'text','Right of second divisibility pair','On a α′≤qα car b′|b^q'),
 inv(16,'display','First two implication rows in lower third','(1)⇒p^{qα}|Σ+b′^q; ⇒p^{qα}|b′(Σ+b′^{q−1}) (car q≥2)'),
 inv(17,'text','Below these implications','posons b′=p^{α′}b″ donc b″ bowl-with-1 p (propriété de α′)'),
 inv(18,'display','Final three implication rows','p^{qα}|p^{α′}b″(…); p^{qα−α′}|b″(…); p^{qα−α′}|Σ+b′^{q−1}; two car explanations'),
 inv(19,'text','Bottom-left corner','Archive sheet numeral 6, preserved in comment only','undetermined hand'),
]
report=dict(
 scan=7,reader='B',start_utc='2026-11-20 11:08:02 UTC',
 end_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
 differences=differences,
 doubts=[
  dict(location='First line, blacked-out unit before Soit',reading=r'\deleted{\illegible{1}}',alternatives=[],confidence='low',reason='Overlapping black strokes obscure the internal sequence; the single-unit placeholder is retained.',crop='crops/01_initial_deletion.png'),
  dict(location='Pale note, first character',reading='a',alternatives=[r'\alpha'],confidence='medium',reason='Small loop and descending tail remain compatible with the two candidates; hand attribution remains undetermined.',crop='crops/02_pale_note.png'),
  dict(location='Pale note, word after first sign',reading="n'exist",alternatives=["n'existe"],confidence='medium',reason='Terminal tall stroke has a curved rightward continuation; a separate final e cannot be isolated, and the joined reading remains possible.',crop='crops/02_pale_note.png'),
 ],
 inventory=inventory,
 notes={
  'page_content':'The page writes hypotheses using a,b,c,q, a binomial expansion, a numbered equality (1), two p-power divisibility pairs using alpha and alpha prime, and a descending divisibility chain. A faint two-line note stands at the right.',
  'authors_own_uncertainty':'No explicit authorial question, doubt word, or question mark was read. The pale note is transcribed with editorial uncertainty as “a/alpha n’exist/n’existe pas si on avait p=1”.',
  'title_date_page_counts':'No title or date was read. The pencilled bottom-left 6 is retained only in the archive-sheet-number comment. There is one manuscript sheet and the numbered equation (1).',
  'mathematics_led_reading_decisions':'Final crowded exponents and summation bounds were enlarged and read stroke by stroke: upper q−1, lower i=1, q−i−1 in the summand and q−1 in the final term. All these readings agree with C. No algebraic computation, theorem verification, or proof check was performed.',
  'hands':'The dark main writing forms a consistent upright hand, recorded as another unnamed hand in accordance with the supplied packet’s other-hand designation. Attribution of the paler note remains undetermined.',
  'view_attestation':'The current UTC time was recorded before the brief and packet were read. The full image was viewed exactly once; supplied half a exactly once; supplied half b exactly once. The three generated crops were each viewed exactly once. No other readers, other page images, OCR, internet, or text-recognition outputs were used.',
  'half_geometry':'Full image 1405×1720; both halves 1405×940. Half a begins at full y=0; half b begins at full y=780, with 160 pixels of overlap.',
  'H_status':'metadata.json states hua_has=nothing; H.tex is empty. Every report row has H=null and diff_H=false.',
  'boundary_note':'The final-two-sums crop retains both target rows’ full summation bounds and exponents. It includes clipped fragments of the preceding row at its top, and only the beginning of the final car at its right; those are contextual fragments. The complete preceding row and both car explanations were read in half b. No target was recropped.',
  'report_tex_alignment':'All original C doubts remain in reading.tex. The main text, formulas, insertion and cancellation state agree with C. The only added transcription detail is the explicitly drawn pair of cancellation strokes over ou p=1.'
 },
 notation=[
  dict(location='Top line; repeated membership statements',sign='Doubled left/upward strokes of N and small raised asterisk',latex=r'\mathbb N^*'),
  dict(location='Second main line; posons line; final explanation',sign='Shallow bowl with a detached short hooked 1 below',latex=r'\mathrel{\underset{1}{\smile}}'),
  dict(location='All binomial sums',sign='Open C with raised dotted i and lowered q',latex=r'C_q^i'),
  dict(location='First expansion and subsequent sums',sign='First upper q and lower i=0; later upper q−1 and lower i=1',latex=r'\sum_{i=0}^{q},\sum_{i=1}^{q-1}'),
  dict(location='On pose line and later factors',sign='Single or paired detached rising ticks',latex=r"a',b',b''"),
  dict(location='Soit alpha line and later p powers',sign='Main-hand looped alpha with taller returning right stroke, and separate prime',latex=r"\alpha,\alpha',p^{q\alpha-\alpha'}"),
  dict(location='Divisibility conditions and chain',sign='Plain upright relation; crossed upright; broad two-line rightward implication arrows',latex=r'\mid,\nmid,\Longrightarrow'),
  dict(location='car q≥2 twice; On a; penultimate car',sign='Angled inequality strokes with separate lower equality stroke',latex=r'\geqslant,\leqslant'),
  dict(location='Pale note',sign='Small loop with diagonal tail; faint final word termination',latex=r"\unsure{a|\alpha}\ \unsure{n'exist|n'existe}"),
 ],
 check_events=[],
 crops=[
  dict(path='crops/01_initial_deletion.png',bbox=[24,15,174,88],rotation=0,purpose='Original C doubt: unreadable blacked-out unit, with the whole Soit as nearby context.'),
  dict(path='crops/02_pale_note.png',bbox=[998,964,1325,1052],rotation=0,purpose='Both adjoining original C doubts in the complete pale two-line note, including terminal p=1.'),
  dict(path='crops/03_final_two_sums.png',bbox=[232,1496,960,1661],rotation=0,purpose='Small crowded summation bounds, primes, and exponents in the final two rows; their readings were open after the half view.'),
 ],
 brief_feedback=[
  'The record vocabulary gives no dedicated class for a deletion whose wording/state agrees but whose two visible cancellation strokes need explicit geometry. It is recorded as drawing or diagram, with diff_C=true only for the added paired-stroke detail.',
  'C_doubts.txt repeats the pale n’exist/n’existe locus. Both supplied entries are covered by one local decision B007-D03.',
  'For the inline deletion drawing, a local zero-thickness ulem rule keeps the required deleted macro while the two actual diagonal cancellation strokes are rendered in TikZ; this avoids adding a generic horizontal stroke.'
 ]
)
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
