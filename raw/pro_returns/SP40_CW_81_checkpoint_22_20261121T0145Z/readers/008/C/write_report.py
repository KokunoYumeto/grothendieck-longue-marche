from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/008/C'
crops=json.loads((out/'crop_manifest.json').read_text())
D=[]
def difference(i,location,C,reading,evidence,confidence,kind,diff_C,status=None,crop=None,bbox=None):
 D.append(dict(id=f'008-C-{i:02d}',location=location,C=C,H=None,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=diff_C,diff_H=False,C_doubt_status=status,readers_crop=crop,bbox=bbox))
difference(1,'Upper isolated cancelled line',r'\deleted{donc si $\unsure{p\ne1|p\ne q}$}',r'\deleted{donc si $\unsure{p\ne1|p\ne q}$}','The initial d, the dotted i, a descending p and crossed relation survive. The rightmost narrow upright with an upper turn supports 1; several oblique cancellation strokes prevent a secure exclusion of the q candidate.','low','other',False,'retained','02_struck_donc_si.png',[94,375,483,455])
difference(2,'Second existential line, after the second existential sign',r'\unsure{\zeta|\delta}',r'\unsure{\zeta|\delta}','An upper slant turns left into a waist, followed by a rounded lower return. The raised recurrence in the same crop has the same form. Zeta remains the leading candidate; the strokes do not settle the letter identity against delta.','medium','other',False,'retained','03_zeta_forms.png',[548,879,1167,981])
difference(3,'Coprimality chain, small lower-right patch under a prime',r'a_{\deleted{\unsure{0}}}\prime',r'a_{\deleted{\unsure{0}}}\prime','A compact, substantially black patch sits below and right of a, beneath the independent prime. Its rounded outer edge supports a cancelled 0, but the internal strokes are obscured. No alternative mathematical symbol is established.','low','other',False,'retained','04_cancelled_subscript.png',[449,1044,723,1139])
difference(4,'Below ruled hypothesis, cancellation before on a',r'\deleted{\unsure{alors}}',r'\deleted{\unsure{alors}}','A tall l-like upright and adjoining rounded strokes survive beneath several oblique crossings. The whole word remains compatible with alors, but the initial and final letters cannot be isolated securely.','low','other',False,'retained','05_lower_alors_and_pale.png',[545,1378,1005,1467])
difference(5,'First lower implication, cancelled item before q squared',r'\deleted{\unsure{p^{2}|p}}',r'\deleted{\unsure{p^{2}|p}}','The lower cluster has a descending stem and right-hand bowl; a second compact cluster stands above it. A separate 2 cannot be read securely through the cancellation. Both supplied readings remain supported.','low','other',False,'retained','06_cancelled_p_power.png',[98,1446,551,1540])
difference(6,'Final equality, cancelled q and raised q alpha minus one',r'{\deleted{q}}^{q\alpha-1}',r'{\deleted{q}}^{q\alpha-1} (glyph and raised placement retained; explicit cancellation drawing in reading.tex)','The lower glyph retains a rounded q body and long descending stem. Above and to its right, q, alpha, minus and 1 remain separately visible and uncrossed. This resolves the actual C doubt-table locus even though C.tex did not carry an unsure macro there. No algebraic interpretation or writing chronology is inferred.','high','other',True,'resolved','08_final_cancelled_q.png',[518,1576,733,1699])
difference(7,'Pale addition after on a, letter carrying the prime',r'{\unsure{a|\alpha}}\prime=\gamma',r'{\unsure{a|\alpha}}\prime=\gamma','The pale letter has a small oval body and an upper-right turn, with a separate raised prime. The local small shape supports a as first candidate; the upper-right turn also admits alpha. The mathematical context has not been used to choose between them.','medium','other',False,'retained','05_lower_alors_and_pale.png',[545,1378,1005,1467])
difference(8,'Pale addition, immediately after p=q',r'p=q,',r'p=q\,\underset{\hspace{.2em}\unsure{,}}{,}','Two separate curved strokes are visible after q, the second lower and slightly to the right. C records one comma. The proposed reading preserves the additional comma-shaped mark without assigning it a mathematical role; the pair may be punctuation treated jointly, but its intended role and hand remain unresolved.','low','omission',True,None,'05_lower_alors_and_pale.png',[859,1408,891,1466])
difference(9,'Cancelled parenthesis below alpha prime equals q alpha',r'\deleted{(on l\prime impose sans risque si p=1)}','Same deleted wording, in two visible lines, crossed by two distinct ascending-right strokes in TikZ','Half a shows one oblique stroke through the left portion and another through the right portion of the two-line parenthesis. The words and cancellation state are retained; the two separate physical strokes are now drawn.','high','drawing or diagram',True,None,None,{'image':'a','origin':'top-left of supplied half a','xyxy':[887,588,1348,705]})
difference(10,'First lower implication, cancelled ou p=1',r'\deleted{\text{ou }p=1}','Same deleted text with a long crossing stroke and lower returning stroke','Crop 07 shows a long stroke through ou p=1 and a distinct lower return under the latter part. The proposed drawing preserves both rather than adding a second generic strike over the words. Cancellation state and text are unchanged.','high','drawing or diagram',True,None,'07_lower_cancellations.png',[561,1468,709,1523])
difference(11,'Second lower implication, pale absurde car q nondivides a',r'\deleted{\text{ou }p=1\Longrightarrow p=1}\ \inserted{\text{absurde car }q\nmid a}',r'\overset{\inserted{\text{absurde car }q\nmid a}}{\text{cancelled }\mathrm{ou}\ p=1\Longrightarrow p=1}','The words absurde car are above the cancelled continuation; q nondivides a stands above its right end. reading.tex puts the insertion above the cancelled span. All words and symbols agree with C.','high','insertion or placement',True,None,'07_lower_cancellations.png',[470,1498,830,1588])
difference(12,'Second lower implication, cancellation across ou p=1 implies p=1',r'\deleted{\text{ou }p=1\Longrightarrow p=1}','Same deleted span, crossed by a single long ascending-right path in TikZ','The dark cancellation begins through ou at the left and rises through the remainder of the expression, passing the upper part of the right p=1. The explicit drawing retains that direction and span; it does not assert a chronology for the pale addition.','high','drawing or diagram',True,None,'07_lower_cancellations.png',[461,1518,811,1583])
difference(13,'Final cancelled q',r'\deleted{q}','Same cancelled q with repeated oblique returns and the long lower hook drawn explicitly','Crop 08 shows repeated diagonal sweeps returning across the q, with a final trace extending below its descender and turning at the bottom. Those visible paths are retained around the readable q and below the unchanged raised entry.','high','drawing or diagram',True,None,'08_final_cancelled_q.png',[604,1613,669,1690])
difference(14,'Faint interline area to right of the first lower cancelled ending',None,'Small gray drawing of residual curved strokes and detached points, without a supplied character','Crop 07 contains a pale curved residual line, short strokes, and several darker points in the gap above q nondivides a. Their source, hand, and former textual identity are unresolved. The drawing is an approximation of the visible traces; no word, symbol, or cancellation target has been reconstructed.','low','omission',True,None,'07_lower_cancellations.png',[748,1458,832,1503])
difference(15,'Return arrow from final parenthesis to lower-right note',r'\draw[->] (n.south east) -- ++(.16,0) |- (n.north east);','Same returning arrow, with a small detached point at its lower start','The lower start near the closing parenthesis has a small detached dark point, then a short line leading to the right-hand return. Crop 10 catches the point; the complete arrow and its upper left-pointing end were read on half b.','medium','drawing or diagram',True,None,'10_final_hypothese.png',{'image':'b','origin':'top-left of supplied half b','xyxy':[1327,685,1372,865]})

I=[]
def inv(n,kind,position,first,hand='another unnamed hand',transcribed='yes'):
 I.append(dict(sheet_kind='text',hand=hand,element=f'008.C.{n:02d}',kind=kind,position=position,first_words_or_objects=first,transcribed=transcribed))
inv(1,'text','Top line','Supposons que q alpha - alpha prime nonzero alors')
inv(2,'display','First two implication rows','(1) implies p divides the sum; then p divides q a to the q-1')
inv(3,'deletion','Right end of second implication row','cancelled nonzero before >0')
inv(4,'text','Below first implications','or p divides b prime et b prime divides b to the q')
inv(5,'deletion','Isolated upper-left cancelled line','donc si p non-equal 1 / q')
inv(6,'display','Next implication line','(1) implies p divides q donc p=q (si q alpha - alpha prime nonzero)')
inv(7,'deletion','Before p=q in that display','p=1 ou')
inv(8,'text','Upper middle, next prose line','Donc si p non-equal q p premier et p divides b prime')
inv(9,'insertion','Below p premier','ou p=1')
inv(10,'deletion','Two-line parenthesis at right','(on l\'impose sans risque si p=1)')
inv(11,'drawing','Across the two-line deleted parenthesis','Two distinct oblique cancellation strokes')
inv(12,'text','Before fold, first existential line','Donc exists b0 in N star et exists gamma in N')
inv(13,'margin note','Right beside first existential line','q nondivides b0','undetermined hand')
inv(14,'text','Immediately above fold','de plus b0 divides b et si b=b0 b double prime alors ... ?')
inv(15,'text','First two lines below fold','De même exists a0 in N star et exists zeta/delta in N; avec a0 divides a ... ?')
inv(16,'text','Coprimality implication chain below','or a bowl-1 b implies a prime bowl-1 b prime implies zeta times gamma =0')
inv(17,'deletion','Under a prime in that chain','Small blackened candidate subscript 0')
inv(18,'text','Middle-lower assumption line','Je suppose désormais que zeta=0 donc a prime = a0 to the q')
inv(19,'display','Left above the long rule','Donc c=b+a0 to the q =a+q to the gamma b0 to the q')
inv(20,'margin note','Three-sided numerical example at right','pour q=2 on a, a0=b0=1, gamma=1, b=4, a=3, c=5')
inv(21,'drawing','Around the numerical example','Top, left, and bottom sides; right side open')
inv(22,'drawing','Around ruled hypothesis','Two long horizontal rules')
inv(23,'text','Between the long horizontal rules',"Je fais l'hypothése suivante si q premier et 1 less-or-equal i <q alors q divides C")
inv(24,'text','Under ruled hypothesis','alors Si q greater-or-equal 3 et q alpha - alpha prime greater-or-equal 2 on a')
inv(25,'deletion','Before on a','Cancelled candidate alors')
inv(26,'insertion','Pale line after on a','p=q, a/alpha prime = gamma','undetermined hand')
inv(27,'drawing','After pale p=q','Two curved detached marks, lower comma-shaped mark of unresolved role','undetermined hand')
inv(28,'display','Two bottom implication rows','(1) implies q squared divides q a to the q-1; implies q divides a to the q-1')
inv(29,'deletion','Before q squared','Cancelled p squared / p')
inv(30,'deletion','End of first bottom implication','ou p=1')
inv(31,'drawing','Across first bottom ou p=1','Long crossing stroke with lower return')
inv(32,'deletion','End of second bottom implication','ou p=1 implies p=1')
inv(33,'drawing','Across second bottom cancelled continuation','One rising long cancellation stroke')
inv(34,'insertion','Above second cancelled continuation','absurde car q nondivides a','undetermined hand')
inv(35,'drawing','Faint gap above right end of lower implications','Residual curved strokes and detached points; no character supplied','undetermined hand')
inv(36,'text','Final line','Donc gamma=0 ou gamma= ... (sous réserve que l\'hypothése est vraie)')
inv(37,'deletion','Final equality, lower glyph','q')
inv(38,'text','Raised above final cancelled q','q alpha -1')
inv(39,'drawing','Around and below final cancelled q','Repeated oblique cancellation returns and lower hook')
inv(40,'margin note','Lower-right note','C\'est peut-être interessant car ici 2 est mis à part dans l\'ensemble des nombres premiers')
inv(41,'drawing','Right of final parenthesis and right-hand note','Return arrow, left-pointing upper end, detached lower start point')
inv(42,'text','Lower-left corner; transcription comment only','archive sheet number: 7','undetermined hand')

report=dict(
 scan=8,reader='C-reader',start_utc='2026-11-20 11:21:15 UTC',end_utc=None,
 full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
 image_view_attestation={
  'whole':{'file':'source/SP40_CW_81_scans/J81-01_81_scan008.jpg','views':1,'dimensions':[1404,1721]},
  'half_a':{'file':'source/SP40_CW_81_scans/J81-01_81_scan008_a.jpg','views':1,'dimensions':[1404,940]},
  'half_b':{'file':'source/SP40_CW_81_scans/J81-01_81_scan008_b.jpg','views':1,'dimensions':[1404,941]},
  'crop_count':10,'crop_views':{c['path']:1 for c in crops},
  'order':'UTC start; brief; all assigned text packet files and PREAMBLE; dimensions and H-empty check; whole once; half a once; half b once; crop helper read; ten crops made once and each viewed once.',
  'coordinate_note':'Crop boxes use the original full scan. Half-only evidence identifies the supplied half and uses its own top-left origin. The nominal lower-half offset is 1721-941=780; an exact pixel equality check failed because the supplied JPGs differ in pixel values, so no half-only box is silently converted to a full-scan box.',
  'independence':'No OCR, internet, other page, other reader output, or delegation. The root supplied only the source-section classification of C_doubts.txt, without ink readings.'},
 differences=D,
 doubts=[
  {'location':d['location'],'reading':d['reading'],'alternatives':a,'confidence':d['confidence'],'reason':d['evidence'],'crop':d['readers_crop']}
  for d,a in [(D[0],[r'p\ne q']),(D[1],[r'\delta']),(D[2],[]),(D[3],[]),(D[4],['p']),(D[6],[r'\alpha']),(D[7],['The pair may have one punctuation function; no such function is assigned.']),(D[13],[])]
 ],
 inventory=I,
 notes={
  'page_content':'Handwritten divisibility calculations, two existential decompositions, coprimality expressions, the stated assumption zeta=0, a q=2 numerical example, a ruled hypothesis, lower implications, and a lower-right note. These statements were transcribed, not checked as mathematical claims.',
  'authors_own_uncertainty':["? after b0 bowl-1 b double prime", "? after a0 bowl-1 a double prime", "Je fais l'hypothése suivante", "(sous réserve que l'hypothése est vraie)", "C'est peut-être interessant car ici 2 est mis à part dans l'ensemble des nombres premiers"],
  'title_date_page_counts':'No separate title or date is written. The lower-left pencilled archive numeral is 7, recorded only as an archive comment. No manuscript page-number macro is supplied.',
  'mathematics_led_reading_decisions':[],
  'physical_features':'Horizontal paper fold, upper-right damage/puncture, and image border were observed as substrate features. Written rules, three-sided example frame, all recorded cancellations, pale additions, return arrow and detached point are represented. The faint interline residue is drawn without an assigned character or mathematical role.',
  'slips_checked':[{'reading':'interessant','location':'Lower-right note, first line','evidence':'Half b shows the dotted i and no detached acute above the first e. C spelling retained.','C_doubt_status':None}, {'reading':'hypothése','location':'Ruled hypothesis','evidence':'Crop 09 shows a rising acute over e. C spelling retained.','C_doubt_status':None}, {'reading':'hypothése','location':'Final parenthesis','evidence':'Crop 10 independently shows a rising acute over e. C spelling retained.','C_doubt_status':None}],
  'additional_loci_resolved_without_witness_change':[{'location':'Upper q-i-1 followed by cancelled nonzero and >0','crop':'01_top_cancelled_neq0.png','result':'The two bars/crossing of the cancelled nonzero sign and its rounded zero remain sufficiently visible; retained C reading.'}, {'location':'Lower pair of cancelled endings and pale absurde car q nondivides a','crop':'07_lower_cancellations.png','result':'All supplied words and symbols retained; geometry and placement recorded separately.'}],
  'H_status':'metadata hua_has=nothing; H.tex is empty (0 bytes). Every H field is null and every diff_H is false.'},
 notation=[
  {'location':'Upper and middle coprimality relations','sign':'Shallow bowl with separate small upright 1 beneath','latex':r'\mathrel{\underset{1}{\smile}}'},
  {'location':'All divisibility lines; two pale nondivisibility additions','sign':'Upright bar, or upright crossed by short oblique stroke','latex':r'\mid,\nmid'},
  {'location':'First expansion and ruled hypothesis','sign':'Capital C, lowered q, raised dotted i','latex':r'C_q^i'},
  {'location':'First sum','sign':'Lower i=1 and upper q-1; dotted i in a exponent and b exponent','latex':r'\sum_{i=1}^{q-1}C_q^i a^i b\prime^{q-i-1}'},
  {'location':'First existential line and repeated gamma signs','sign':'Forked upper strokes with a lower loop','latex':r'\gamma'},
  {'location':'Second existential line and its later recurrences','sign':'Upper slant, left waist and rounded lower hook; identity remains qualified','latex':r'\unsure{\zeta|\delta}'},
  {'location':'Both existential lines','sign':'Double-stroked N with separate raised star where present','latex':r'\mathbb N,\mathbb N^*'},
  {'location':'Coprimality questions','sign':'Two separate upper ticks on double-prime letters; small lower ovals as zeros','latex':r'a_0,b_0,a\prime\prime,b\prime\prime'},
  {'location':'Ruled hypothesis and lower condition','sign':'Comparison with separate lower stroke','latex':r'\leqslant,\geqslant'},
  {'location':'Final equality','sign':'Cancelled lower q with uncrossed q alpha minus one raised to its right','latex':r'{\deleted{q}}^{q\alpha-1}'},
  {'location':'Pale p=q addition','sign':'Two comma-shaped strokes, lower stroke slightly right; role unresolved','latex':r'\underset{\hspace{.2em}\unsure{,}}{,}'}
 ],
 check_events=[],crops=[{k:c[k] for k in ('path','bbox','rotation','purpose')} for c in crops],
 actual_C_doubt_map=[{'source_entry':entry,'difference_id':f'008-C-{i:02d}','status':D[i-1]['C_doubt_status']} for i,entry in [(1,'First isolated struck line'),(2,'Second existential line'),(3,'Before second bowl in or a…'),(4,'Above last two implications'),(5,'After (1)⇒ in lower left'),(6,'End of final line'),(7,'Lower line, light addition after on a')]],
 C_doubt_classification='Seven actual Doubtful readings rows. Six earlier source rows are notation entries. The final interessant and hypothése rows are Slips retained, not C doubts.',
 brief_feedback=['The additional lower curved stroke after pale p=q may belong to a compound punctuation sign or be an independent mark. I preserved the visible comma-shaped candidate with unresolved role and hand.', 'Faint residual strokes in the lower interline gap support a small drawing but no character. Their source and cancellation target are unestablished.', 'The final cancelled-q locus is an actual doubt-table row although C.tex has no unsure macro; its resolution is therefore explicitly counted.'],
 counts={'difference_rows':len(D),'diff_C_true':sum(d['diff_C'] for d in D),'diff_H_true':sum(d['diff_H'] for d in D),'actual_C_doubts':7,'C_doubts_resolved':sum(d['C_doubt_status']=='resolved' for d in D),'C_doubts_retained':sum(d['C_doubt_status']=='retained' for d in D),'crops':len(crops),'inventory_elements':len(I),'mathematical_check_events':0}
)
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
