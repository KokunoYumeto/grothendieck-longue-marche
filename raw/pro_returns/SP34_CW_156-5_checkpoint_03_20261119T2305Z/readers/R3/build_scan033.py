import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/workspace/scratch/4770596940a0')
OUT = ROOT / 'out/readers/R3'
SRC = ROOT / 'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan033.jpg'
C = ROOT / 'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan033.tex'
H = ROOT / 'working/H/scan033.tex'
crops = json.loads((OUT / 'scan033_crops.json').read_text())
differences = []

def d(place, C, H, reading, ink, confidence, kind, crop, against_C, against_H, marked_in_H=False):
    differences.append(dict(id=f'D{len(differences)+1:02}', place=place, C=C, H=H,
        reading=reading, ink=ink, confidence=confidence, kind=kind,
        crop=crop if isinstance(crop,list) else [crop], against_C=against_C,
        against_H=against_H, marked_in_H=marked_in_H))

d('manuscript page number', '32.', '32', '32.',
  'A small point follows the handwritten 32 at upper right.', 'high', 'punctuation', 'whole', False, True)
d('before 1°)', r'\deleted{\unsure{R|P}}', r'\struck{Or}', r'\deleted{\unsure{R|P|Or}}',
  'Tall curved/stemmed form, loop and rightward tail are heavily crossed. Neither one capital nor the two-letter reading is secure.', 'low', 'C doubt retained; added alternative', 'top_cancel', True, True)
d('1°), first capital', r'\unsure{F|\mathcal F}', 'F', 'F',
  'A simple upright stem and bent top/middle arms; no separate calligraphic loop visible.', 'medium', 'C doubt resolved', 'top_F', True, False)
d('sideways margin, first word', r'\unsure{voir}', r'\uncertain{va se simplifier}', r'\unsure{va|voir}',
  'After clockwise rotation the first group has a v-like start and low oval/short exit; a distinct i dot and final r are not secure. va is favored, voir retained.', 'low', 'C doubt retained; alternative preference', 'left_margin', True, True, True)
d('sideways margin, second word', r'\unsure{une|sa}', r'\uncertain{va se simplifier}', r'\unsure{se|sa|une}',
  'A short low group looks closer to s/e than to a clearly articulated une. The faded connections prevent a firm decision.', 'low', 'C doubt retained; added alternative', 'left_margin', True, True, True)
d('sideways margin, third word', r'\unsure{simplification}', r'\uncertain{va se simplifier}', r'\unsure{simplifier|simplification}',
  'Long simplifi-like body; the ending lacks a secure tall terminal t. simplifier fits the terminal low strokes better, without excluding the faded longer noun.', 'low', 'C doubt retained; added alternative', 'left_margin', True, True, True)
d('sideways margin, last word', 'cf plus bas', r'cf plus \ill{}', 'cf plus bas',
  'The final three-letter group has b ascender followed by a low a/s sequence. It is readable after rotation.', 'medium', 'H illegibility resolved', 'left_margin', False, True, True)
d('left edge, long separator', 'No drawn rule; sideways-note comment only', 'Rule described in a note', 'Long curved separator reproduced in TikZ',
  'A thin unbroken line runs down the left of the body, bowing left in the middle. It separates the marginal writing and does not cross its letters.', 'high', 'drawing restored', 'left_rule', True, True)
d('left of Je dis, just right of separator', 'Omitted', 'Omitted', 'Two faint stroke clusters reproduced in TikZ; no lexical reading assigned',
  'Upper cluster: a gray diagonal rising right, with a short darker fragment below it. Lower cluster: a separate broken diagonal rising right. No complete letter or definite attachment.', 'medium', 'drawing restored; function uncertain', 'left_faint', True, True)
d('2°), between initial inclusion and Soit', 'No full stop', 'Full stop', 'No full stop',
  'The interval after the right-hand G and before Soit has no distinct punctuation dot.', 'medium', 'punctuation', 'two_setup', False, True)
d('2°), bracket below two inclusions', 'Underline with short end rules', 'Omitted', 'Shallow bottom bracket with upturned ends, drawn in TikZ',
  'A continuous bottom stroke joins two small end ticks beneath both inclusions.', 'high', 'graphic review/restoration', ['two_setup','two_math'], False, True)
d('2°), old superscript after first A in bounded formula', r'A^{\deleted{\unsure{\prime|\ast|?}}}', 'A', r'A^{\deleted{\unsure{\prime|\ast|?}}}',
  'Tiny elevated strokes lie under cancellation/overtrace. Their original prime/star-like structure cannot be distinguished securely.', 'low', 'C doubt retained; H revision restored', 'two_math', False, True)
d('2°), old superscript after second A, before circ(F)', r'A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}', r'A^{\circ(F)}', r'A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}; closing-parenthesis uncertainty separately in D14',
  'A second, separate elevated overwritten cluster occurs before the open-stratum superscript. Its letterform remains obscured.', 'low', 'C doubt retained; H revision restored', 'two_math', False, True)
d('2°), final closing parenthesis at right image edge', 'Closing ) supplied without doubt', 'Closing ) supplied without doubt', r'\circ(F\unsure{)}',
  'The F is visible at the extreme right, but a complete closing curve falls at or beyond the image edge. Retain a doubtful parenthesis rather than claim it is fully seen.', 'low', 'new uncertainty from clipping', 'two_math', True, True)
d('2°), relation after prouvons que A′', r'A′=A', r'A′=A', r'A′\unsure{\in|=}A',
  'The sign has two heavy horizontal strokes, a curved left connector and a short thin internal bar. Membership is the closest complete visible shape; membership overwritten toward equality is possible. The revision chronology/final sign is not certain.', 'low', 'new sign/overwrite uncertainty', 'two_equality', True, True)
d('2°), d’où A∈F', r'A\in F', r'A′\in F', r'A\in F',
  'The capital has no separate prime above/right. A long diagonal meeting the following membership sign is at body height, not a prime.', 'high', 'index', 'two_equality', False, True)
d('2°), cancelled words at right after d’où clause', r'\deleted{On a}', r'\struck{Or}', r'\deleted{\unsure{On a|Or}}',
  'A large O survives at left; the horizontal strike hides the next letter(s), but a lower short stroke and right small loop favor On a. Or cannot be excluded.', 'low', 'new cancellation uncertainty', 'two_On', True, True)
d('Je dis block, after donc A∈F′', r'\deleted{\unsure{et}}', r'\struck{et}', r'\deleted{et}',
  'Left loop followed by a tall crossed stem is compatible with et; the cancellation crosses it diagonally.', 'medium', 'C doubt resolved', 'et_cancel', True, False)
d('interlinear insertion above cf lemme', r'il suffirait F′\ll F', r'i.e. sachant F′\ll F', r'il suffirait F′\ll F',
  'An initial short il is followed by suffirait, with the repeated f strokes and final tall t. No i.e. or sachant sequence is visible.', 'high', 'wording', 'suffirait', False, True)
d('leader under il suffirait insertion', 'Not drawn', 'Not drawn', 'Curved insertion leader retained in TikZ',
  'A low curved stroke passes below the inserted words and curls upward at the right; it is separate from their letter strokes.', 'high', 'drawing restored', ['suffirait','je2'], True, True)
d('after car F′≼F, before cf lemme', r'\deleted{)}', 'Omitted', r'\deleted{)}',
  'An original closing curve is crossed in the revision that extends the parenthesis through cf lemme plus bas.', 'medium', 'deletion restored', 'je2', False, True)
d('after cf lemme plus bas)', r'et \deleted{\unsure{bien}}', r'\uncertain{d’autre part}', r'et \unsure{\uline{bien}|\deleted{bien}}',
  'et is distinct. The following short b-initial form is compatible with bien. An extra stroke runs below its middle letters, so live/underlined versus deleted state remains uncertain. The short form does not support d’autre part.', 'low', 'C doubt retained; wording and revision state', 'bien', True, True, True)
d('before A,A′∈F′', r'\deleted{\unsure{F|\in}}', r'\struck{\exists}', r'\deleted{\unsure{F|\in|\exists}}',
  'A tall left stroke, horizontal bars and lower curvature remain under heavy cancellation; no complete original sign is securely recoverable. H’s existence sign remains an alternative, not a resolved reading.', 'low', 'C doubt retained; added alternative', 'old_F', True, True)
d('Donc, before prouvé', r'\unsure{on a}', 'on a', r'\unsure{on a}',
  'Very faded low fragments remain in the expected word positions. They do not independently yield all the letters of on a.', 'low', 'C doubt retained', 'on_a', False, True)
d('Donc, overwritten letter before live A′', r'\deleted{\unsure{F|A}}A′', 'A′ only', r'\deleted{\unsure{F|A}}A′',
  'The live A′ is dark; additional stem/bar strokes underneath support an earlier capital but do not separate F from A.', 'low', 'C doubt retained; H revision restored', 'donc_overwrite', False, True)
d('Prouvons qu’on a A′∉G, opening before d’où', '(d’où', ', d’où', '(d’où',
  'A curved opening parenthesis appears immediately before d’où.', 'high', 'punctuation', 'donc', False, True)
d('after A′∈F\G before qed', r'\deleted{)}', 'Omitted', r'\deleted{)}',
  'A crossed closing curve precedes the comma and the word qed.', 'medium', 'deletion restored', 'qed', False, True)
d('qed parenthetical punctuation', ', qed)', '(qed)', ', qed)',
  'The apparent large left curve at qed belongs to the descending q. There is no separate opening parenthesis immediately before q; a closing ) follows d.', 'high', 'punctuation', 'qed', False, True)
d('beginning next sentence', 'Sinon on aurait', 'Si on avait', 'Sinon on aurait',
  'A longer initial Sin…on group is followed by a separate on and the tall-starting aurait group. C’s Sinon on is preferred from the visible spacing.', 'medium', 'wording', 'sinon', False, True)
d('pale mark above final live parenthetical line', 'Omitted', 'Omitted', 'Faint left-pointing arrow-like drawing, with several darker points, reproduced in TikZ',
  'A nearly horizontal pale shaft extends right from a left vertex, with upper-right and lower-right head strokes. Several dark flecks occur on/near the upper arm and vertex. No text and no secure endpoint/attachment; fading or erasure is possible.', 'medium', 'drawing restored; function uncertain', 'pale_mark', True, True)
d('cancelled b⇒c draft, interlinear premise', r'\inserted{On suppose b) i.e. φ induit F′\G′→~F\G}', 'Same premise supplied only in explanatory note', r'\deleted{\inserted{On suppose b) i.e. φ induit F′\G′\overset{\sim}{\longrightarrow}F\G}}',
  'The small premise sits over the start of the draft, has a tilde over the map arrow, and is crossed by the same large oblique cancellation strokes.', 'high', 'insertion placement/state', 'cancel_insert', False, True)
d('cancelled draft, immediately before Soit', 'Soit', '(Soit', 'Soit',
  'The curve beside Soit is the left hook of the long interlinear leader; it joins the line passing beneath the premise. It is not an independent parenthesis.', 'medium', 'punctuation/graphic interpretation', 'cancel_block', False, True)
d('leader below cancelled premise', 'Not drawn', 'Not drawn', 'Long curved insertion leader, drawn in TikZ',
  'The thin line rises from the curl beside Soit, extends right below the premise and turns upward at the far right.', 'high', 'drawing restored', ['cancel_block','cancel_insert'], True, True)
d('cancelled draft, adjective after strate', 'ouverte', r'\ill{}', 'ouverte',
  'The spaced o/u/v/e/r/t/e sequence is readable between the large cancellation strokes.', 'medium', 'H illegibility resolved', 'cancel_block', False, True, True)
d('cancelled draft, strate ouverte … de F′', r'\uline{strate ouverte … de F′}', 'No underline', r'\uline{strate ouverte \deleted{dans \unsure{la}} de F′}',
  'A long horizontal underline extends from strate through the ending F′, independent of the oblique cancellation strokes.', 'high', 'underline restored', 'cancel_block', False, True)
d('cancelled draft, local words before de F′', r'\deleted{dans \unsure{la}}', 'Omitted', r'\deleted{dans \unsure{la}}',
  'dans has visible connected strokes; the short following cluster is heavily scribbled and may be la. Preserve the doubtful final word.', 'low', 'C doubt retained; H deletion restored', 'cancel_local', False, True)
d('cancelled draft, after l’unique élément', r'\deleted{de}', 'Omitted', r'\deleted{de}',
  'A small crossed de-like group lies between élément and tel que.', 'medium', 'deletion restored', 'cancel_element', False, True)
d('large cancellation over b⇒c draft', 'Deletion macro; no stroke geometry', 'Deletion macro and prose note; no drawing', 'Five rising-right diagonal cancellation strokes reproduced in TikZ',
  'Five long oblique strokes pass through the heading, insertion and three body lines, ending above the final Prouvons line.', 'high', 'drawing restored', 'cancel_block', True, True)
d('last Prouvons line of old draft', 'Entire line deleted with preceding paragraph', 'Entire line deleted with preceding paragraph', r'\unsure{\deleted{Prouvons A′°(F′)=A°(F).}|Prouvons A′°(F′)=A°(F).}',
  'No oblique cancellation stroke reaches this physical line. It may nevertheless fall under the paragraph’s cancellation by intention; retain both revision-state possibilities and the full wording.', 'low', 'new deletion-extent uncertainty', 'cancel_block', True, True)
d('bottom, after soit U', 'U, Posons', 'U. Posons', 'U, Posons',
  'The mark after U is a short comma-like descending stroke.', 'medium', 'punctuation', 'bottom1', False, True)
d('bottom, first I superscript', r'I^{\unsure{\ast|k|+}}', 'I*', r'I^{\unsure{\ast|k|+}}',
  'A small forked/crossed elevated mark has more than a simple dot; the blurred arms do not decide star versus k/plus with confidence.', 'low', 'C doubt retained', 'star', False, True)
d('bottom, overwritten operator after F′', r'\deleted{\unsure{\times|\setminus}}', 'No old operator represented', r'\deleted{\unsure{\times|\setminus}}',
  'Several oblique strokes cross at the operator position. An older cross/slash is visible under the thicker final diagonal, but its identity remains uncertain.', 'low', 'C doubt retained; H revision restored', 'star', False, True)
d('bottom, final operator before G′', r'\unsure{\setminus}', r'\smallsetminus', r'\unsure{\setminus}',
  'The downward-right slash is the clearest final stroke, with overlapping residual lines. Set difference is favored, not fully certain from the ink alone.', 'low', 'C doubt retained', 'star', False, True)
d('bottom, abbreviation ens', 'ens', 'ens.', 'ens',
  'No independent punctuation point is visible after ens before d’indices.', 'medium', 'punctuation', 'bottom2', False, True)
d('bottom, I after ordonnés', 'I', 'I', 'I; top serif reviewed, no separate arrow',
  'The heavy top bar turns slightly at its right end; the faint nearby marks do not form a detached directional arrow or superscript.', 'medium', 'notation review, no textual change', 'I_top', False, False)
d('bottom, punctuation after I', 'I,', 'I (', 'I,',
  'A small comma separates I from the cancelled triangular capital and the later (=F).', 'medium', 'punctuation', ['I_top','bottom_Delta'], False, True)
d('bottom, cancelled capital after I', r'\deleted{\unsure{A|\Delta}}', 'Omitted', r'\deleted{\unsure{A|\Delta}}',
  'A triangular outline and internal crossing/cancellation strokes remain. The crossbar is not clean enough to settle A versus Δ.', 'low', 'C doubt retained; H deletion restored', 'bottom_Delta', False, True)
d('bottom, closing parenthesis after I′(=F′)', 'One closing parenthesis; large outer opening remains unclosed', 'Two closing parentheses', 'One closing parenthesis; retain unmatched outer opening',
  'The final visible curve closes (=F′). No second closing curve is present before the period and On a.', 'high', 'punctuation', 'bottom2', False, True)

inventory = []
def inv(kind, position, words, diff=None):
    row = dict(id=f'I{len(inventory)+1:02}', scan='033', sheet_kind='text', hand='handwritten',
        kind=kind, position=position, first_words_or_objects=words, transcribed='yes')
    if diff: row['difference_ids'] = diff
    inventory.append(row)

inv('text','upper right','32.',['D01'])
inv('deletion','top left, before 1°)','R|P|Or',['D02'])
inv('text','top, 1°) paragraph','1°) F\G⊂F′\G′ i.e. Tout A∈F\G … A∈G',['D03'])
inv('deletion','top paragraph, before (comme G≤F)','A∈')
inv('margin note','left edge, sideways, beside 1°)/2°)/Je dis','va|voir se|sa|une simplifier|simplification, cf plus bas',['D04','D05','D06','D07'])
inv('drawing','left edge, from upper paragraph down to cancelled draft','Long curved separating rule',['D08'])
inv('drawing','left of Je dis, just right of rule','Two faint oblique stroke clusters',['D09'])
inv('text','upper middle, 2°) opening','2°) F′\G′⊂F\G Soit A′ … et d’abord A′∈F',['D10'])
inv('deletion','2°), before Soit A le plus petit','On a')
inv('text','2°), next setup','Soit A le plus petit él. de F^{A′} donc')
inv('display','2°), bounded two-inclusion group','A′⊂A^{old}, A′°(F′)⊂A^{old °(F)}',['D12','D13','D14'])
inv('drawing','under the two inclusions','Shallow bottom bracket with two upturned ends',['D11'])
inv('deletion','bounded group, superscript of first A','prime|star|?',['D12'])
inv('deletion','bounded group, superscript of second A','prime|star|?',['D13'])
inv('text','2°), last line','prouvons que A′ ∈|= A (d’où A∈F).',['D15','D16'])
inv('deletion','2°), far right after parenthesis','On a|Or',['D17'])
inv('text','middle, Je dis paragraph first part','Je dis que A∈F\G i.e. A∉G … absurde')
inv('deletion','middle, immediately before Donc A∈F\G','Mais')
inv('text','middle, Donc … Il en résulte','Donc A∈F\G, donc A∈F′, Il en résulte que A°(F)=A°(F′)')
inv('deletion','after donc A∈F′','et',['D18'])
inv('text','middle, parenthesis and lemma citation','car F′≼F … cf lemme plus bas')
inv('insertion','above parenthetical clause','il suffirait F′≪F',['D19'])
inv('drawing','below il suffirait insertion','Curved insertion leader',['D20'])
inv('deletion','after car F′≼F','Original closing parenthesis',['D21'])
inv('text','after cf lemme plus bas)','et bien, with underline/deletion-state alternatives',['D22'])
inv('drawing','under/through bien','Short horizontal stroke; underline versus cancellation uncertain',['D22'])
inv('deletion','beginning next physical line before A,A′','F|∈|∃',['D23'])
inv('text','end of Je dis paragraph','A,A′∈F′ tels que A′°(F′)⊂A°(F′), ce qui prouve A=A′')
inv('text','lower middle, Donc paragraph opening','Donc on a prouvé que A′∈F′\G′⇒A′∈F',['D24','D25'])
inv('deletion','Donc line, underneath A′','F|A',['D25'])
inv('text','lower middle, Prouvons qu’on a','Prouvons qu’on a A′∉G (d’où A′∈F\G, qed).',['D26','D27','D28'])
inv('deletion','inside d’où clause, before qed','Original closing parenthesis',['D27'])
inv('text','lower middle, Sinon on aurait','Sinon on aurait A′∈G … d’où (comme A′∈F′ et G′≤F′) A′∈G′, absurde',['D29'])
inv('drawing','above final live parenthetical line, x775–930,y1575–1645','Faint left-pointing arrow-like mark and darker points',['D30'])
inv('deletion','lower third, old b⇒c draft','b)⇒c) Soit A∈F\G … φ(A′)=A',['D32','D34','D35','D36','D37','D38'])
inv('insertion','above old b⇒c draft, itself crossed','On suppose b) i.e. φ induit F′\G′→~F\G',['D31'])
inv('drawing','below inserted premise','Long insertion leader curling beside Soit and at right',['D33'])
inv('drawing','across old b⇒c draft','Five oblique cancellation strokes',['D38'])
inv('deletion','old b⇒c draft, inside underline','dans la?',['D36'])
inv('drawing','old b⇒c draft, under strate … F′','Long underline',['D35'])
inv('deletion','old b⇒c draft, after élément','de',['D37'])
inv('text','final line of old draft below all five stroke ends','Prouvons A′°(F′)=A°(F).; paragraph-deletion scope uncertain',['D39'])
inv('text','bottom, new argument','b⇔c … On a |F|\|G|=|F′|\|G′|, soit U,',['D40'])
inv('deletion','bottom, between b⇔c and On a','Posons')
inv('text','bottom, index definitions','Posons F\G=I*, F′\G′=I′*',['D41','D42','D43'])
inv('deletion','bottom, between F′ and G′','old ×|setminus',['D42'])
inv('text','last two lines','(parties ouvertes des ens d’indices ordonnés I, (=F), I′(=F′). On a',['D44','D45','D46','D48'])
inv('deletion','last lines, after I,','A|Δ',['D47'])

c_doubts = [
 ('top deleted R|P','D02','retained, Or alternative added'),
 ('first F|mathcal F','D03','resolved to F'),
 ('margin voir','D04','retained with va preferred'),
 ('margin une|sa','D05','retained with se preferred'),
 ('margin simplification','D06','retained with simplifier preferred'),
 ('first old superscript prime|star|?','D12','retained'),
 ('second old superscript prime|star|?','D13','retained'),
 ('deleted et','D18','resolved to et'),
 ('deleted bien','D22','retained; deletion versus underline now explicitly uncertain'),
 ('deleted F|membership','D23','retained; existence alternative added'),
 ('Donc on a','D24','retained'),
 ('old F|A beneath A′','D25','retained'),
 ('deleted la after dans','D36','retained'),
 ('I superscript star|k|+','D41','retained'),
 ('old operator ×|setminus','D42','retained'),
 ('live setminus','D43','retained'),
 ('deleted A|Delta','D47','retained'),
]

who = dict(model='inherited', effort='inherited; not separately exposed', run='R3-scan033')
today = datetime.now(timezone.utc).date().isoformat()
events = [
 dict(statement_id='R3-033-background-closed-family', place='1°), comme G≤F', date=today, who=who,
      type='carried as background without fault found',
      outcome='For the conditional check only, assumed that an F-member whose support lies in |G| belongs to the closed subfamily G. This property was not proved here.'),
 dict(statement_id='R3-033-check-exclusion-Gprime', place='1°), contradiction from A∈G′', date=today, who=who,
      type='targeted proof check',
      outcome='Conditionally checked: given A∈F\G, |G′|=|G| and the stated closed-subfamily property, A∈G′ gives |A|⊂|G′|=|G|, hence A∈G, contradiction. This checks exclusion from G′ only; it does not establish the separate A∈F′ premise or the whole proposition.'),
 dict(statement_id='R3-033-background-strata-partition', place='Je dis, ce qui prouve A=A′', date=today, who=who,
      type='carried as background without fault found',
      outcome='Assumed, only for the next conditional check, that strata indexed by different F′ members are disjoint and that the stratum of A′ is nonempty. No independent proof of those background properties on this page.'),
 dict(statement_id='R3-033-check-stratum-inclusion', place='Je dis, A′°(F′)⊂A°(F′)', date=today, who=who,
      type='targeted proof check',
      outcome='Conditionally checked: if A and A′ are F′ labels and their distinct strata are disjoint, a nonempty A′ stratum contained in the A stratum rules out distinct labels, hence A=A′. The earlier equality A°(F)=A°(F′), referred to a later lemma by the author, was not proved or verified in this check.'),
]

order = ['top','top_cancel','top_F','left_margin','two_setup','two_math','je1','je2','suffirait',
         'bien','old_F','je3','donc','donc_overwrite','donc2','cancel_block','cancel_insert',
         'cancel_local','cancel_element','bottom1','bottom2','star','bottom_Delta','left_rule',
         'pale_mark','qed','sinon','I_top','two_equality','two_On','on_a','et_cancel','left_faint']
crop_by_id = {c['id']:c for c in crops}
images = [str(SRC),str(SRC.with_name(SRC.stem+'_a.jpg')),str(SRC.with_name(SRC.stem+'_b.jpg'))]
images += [crop_by_id[x]['path'] for x in order]

report = dict(
 scan='033', manuscript_page='32.', reader='R3', model='inherited', effort='inherited; not separately exposed',
 start_utc=(OUT/'scan033_start.txt').read_text().strip(), end_utc=datetime.now(timezone.utc).isoformat(),
 scope='scan033 only; no later page, other reader report, or parent adjudication consulted',
 sources=dict(C=str(C), H=str(H), C_doubts=str(C.parent.parent/'J156-5-04_doubts.md'),
              C_notes=str(C.parent.parent/'J156-5-04_notes.md'),
              S=str(ROOT/'source/SP34_CW_156-5_sweep3/readings/156-5_CORRECTIONS.tsv')),
 images_viewed=images,
 viewing_notes=[
     'Whole page, then both supplied halves, then enlarged crops; all actual images emitted and read. No OCR.',
     'The final four tight crops were re-emitted individually after an earlier multi-image output was truncated; only successful views are counted.',
     'two_equality and cancel_block were viewed again after the final four tight crops.',
     'All 17 C uncertainty occurrences were reviewed separately. Words agreed by C and H and all visible mathematical operators/indices were also read from the image.',
 ],
 crops=crops, crop_recipe_method='PIL crop in source coordinates, then rotate with white expansion if nonzero, then integer LANCZOS enlargement; no thresholding or OCR',
 differences=differences,
 C_doubt_resolutions=[dict(occurrence=i+1,place=p,difference_id=x,decision=decision) for i,(p,x,decision) in enumerate(c_doubts)],
 S_row_decisions=[dict(scope='Rows whose where field includes 033, including numeric ranges', applicable_rows=[], decision='No applicable S correction row for scan033; no S wording substituted')],
 inventory=inventory,
 remaining_doubts=['D02','D04','D05','D06','D09','D12','D13','D14','D15','D17','D22','D23','D24','D25','D30','D36','D39','D41','D42','D43','D47'],
 notation=[
     dict(form='F,G,F′,G′',reading='Plain handwritten capitals; primes checked per occurrence; no calligraphic F adopted at the top.'),
     dict(form='A′, A',reading='Primes checked per occurrence; d’où A∈F is unprimed despite H’s A′.'),
     dict(form='A^{circ(F)} / A′^{circ(F′)}',reading='Open-stratum circle followed by parenthesized family in the superscript; F′ primes checked. Two cancelled superscripts in the bounded formula remain unclear.'),
     dict(form='|F|, |G|, |F′|, |G′|',reading='Paired support bars, not parentheses, in the support equalities.'),
     dict(form='⊂, ∈, ∉, ≤, ≼, ≪, ⇒, ⇔, → with tilde',reading='Distinct visible relations retained; the A′ relation in prouvons que remains ∈|= from its own ink.'),
     dict(form='I, I′, I*, I′*',reading='Plain index capitals; first star-like superscript and revised set-difference operator remain doubtful. No arrow inferred over I after ordonnés.'),
     dict(form='él.; ens; cf; i.e.; qed',reading='Abbreviations retained, not expanded in the text. Likely élément; ensembles; confer; id est; quod erat demonstrandum, respectively, in this list only.'),
 ],
 notes_while_reading=[
     'Most live prose is readable; the least secure places are faded marginal words, overwritten/cancelled short glyphs and the right image edge.',
     'The pale arrow-like mark and faint left-margin clusters were inspected as graphical ink, not promoted to words. Their function/deletion state is not known.',
     'The five large cancellation strokes stop above the last Prouvons line. Full text is preserved with deletion-state alternatives, without deciding intention from the paragraph’s mathematics.',
     'The extra stroke at bien is under its middle letters. Both underline/live and deleted interpretations remain possible.',
     'The relation after prouvons que has a membership-like curve and middle bar under heavy horizontals. A revision toward equality is plausible but not certain; expected equality was not used to erase the curved ink.',
     'H has useful alternatives for some obscured marks, but loses local corrections and drawing geometry; C preserves more of these, while some of its doubts remain necessary.',
     'No direct page diagram was found; graphical elements are separators, insertion leaders, underlining, cancellation strokes and faint isolated marks. All are represented in the proposed TEX.',
     'The last outer parenthesis is left unmatched as seen; no grammatical or mathematical balancing has been supplied.',
 ],
 math_reading_checks=[
     'Compared the first two set inclusions, all G′/F′ primes, support bars, membership/negated membership, and G≤F / G′≤F′ directly with enlarged ink.',
     'Compared both bounded-formula inclusions, F^{A′}, the open-stratum superscripts and their two old cancelled marks; final right parenthesis remains visually clipped.',
     'Compared A°(F)=A°(F′), F′≼F and inserted F′≪F; these are readings, not verification of the author’s cited lemma.',
     'Compared the implication A′∈F′\G′⇒A′∈F, the later exclusion A′∉G and its support argument, and the map φ(A′)=A in the cancelled draft.',
     'Compared the final double implication, support-difference equality and index definitions; no continuation on scan034 read.'
 ],
 mathematical_notes=[
     'Only the two expressly conditional inference checks in check_events were performed. No independent re-proof, computation, formal certificate, or verification of the entire proposition is claimed.',
     'The author cites a later lemma for the equality of open strata of common members under refinement. That equality is carried in the transcription; its later proof was not opened.',
 ],
 check_events=events,
 proposed_tex=str(OUT/'scan033.tex'), crop_recipe_file=str(OUT/'scan033_crops.json'),
 validation=dict(status='passed structural checks',
                 checked=['balanced TeX braces','matched begin/end environments','math dollar delimiter parity',
                          'unique difference IDs','all 17 C doubt links','boolean flags',
                          'existence of all image and crop paths','permitted inventory kinds',
                          'permitted check-event types'],
                 compilation_performed=False)
)

(OUT/'scan033.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(saved=str(OUT/'scan033.json'), differences=len(differences), C_doubts=len(c_doubts), inventory=len(inventory), crops=len(crops), images=len(images), check_events=len(events)),ensure_ascii=False))
