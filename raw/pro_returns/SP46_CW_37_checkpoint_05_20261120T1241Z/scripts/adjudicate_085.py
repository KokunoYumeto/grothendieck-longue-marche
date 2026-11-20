from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan085/{a}/report.json').read_text()) for a in 'ABC'}
paths=['crops/scan085/pagination.jpg','readers/scan085/B/B01_chapter_round_character.jpg','readers/scan085/B/B02_left_marginal_mark.jpg','readers/scan085/C/C03_cancelled_rows_stroke.jpg','readers/scan085/B/B04_live_2_5_mark.jpg','readers/scan085/B/B05_reciproques_overtype.jpg','readers/scan085/B/B05_reciproques_overtype.jpg']
ds=copy.deepcopy(R['B']['decisions'])
for i,d in enumerate(ds):
    d['id']=f'M085-{i+1:02}';d['crop']=paths[i]
    d['readers']={a:R[a]['decisions'][i]['reading'] for a in 'ABC'}
    d['h_reading']=None;d['diff_h']=False;d['marked_in_H']='no'
    if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
ds[0]['scan_shows']='The 5 has a top bar and lower bowl, the 3 two right lobes and the 8 two closed bowls. Separate short horizontal typed strokes flank the digits at the left and right. Main confirms all three readers: the page field is - 538 -, with both dashes added to C’s 538.'
ds[1]['scan_shows']='The chapter character is one upright closed oval with heavier sides, no slash, internal point or distinguishing appendage. Main retains O/0 with all three readers. The following low point and horizontal dash are separate. The adjacent capital O impressions do not decide which character was intended.'
ds[2]['alternatives']='Question mark; a bracket or grouping hook with a separate low dash; B also considers an elongated 2 with a detached stroke. The graphic is retained without assigning one textual function.'
ds[2]['scan_shows']='The upper stroke runs right into a rounded turn, descends in a long slightly left-slanting stem, then turns right into a low curled foot. A separate short horizontal mark lies below and considerably to the right. Main confirms the graphic approach of all three readers and adopts B’s proportions. The long stem and displaced dash do not uniquely establish C’s literal question mark; the possible functions remain uncertain.'
ds[3]['scan_shows']='Two tall overlapping oblique runs cross the old 2.4 and 2.5 number fields. Connected low returning loops pass through Fonctions, broader rising and falling curves pass through constructibles, and a nearly horizontal continuation crosses the dotted leader to its end. Main confirms all three readers’ omitted graphic and retains B’s continuous path. Both typed entries remain legible and cancelled; no independent machine cancellation or additional lettering is supplied.'
ds[4]['scan_shows']='The sign after 5 has a curved hook with a left terminal, a short descending stem, and a separate rounded low impression matching the nearby typed point. Its pitch and ribbon texture agree with the surrounding typewriting. Main confirms the typed 2.5? with all readers; no further period or deleted punctuation is recoverable. This is an unchanged C-context target, not an explicit C doubt.'
ds[5]['confidence']='medium'
ds[5]['scan_shows']='The first position has the live p’s bowl, descender and lower foot, plus an extra baseline-level foot and merged upper shoulder compatible with r. The second position preserves a lower p stem and foot beneath the live r. C-reader resolves both underprints; main agrees with A/B that the first upper contour is too merged to isolate r securely, so C’s r doubt remains. The second underlying p is retained as readable.'
ds[6]['reading']=r'roque\unsure{s|\deleted{s}s|ss} de préfaisceaux'
ds[6]['alternatives']='One live s with an offset duplicate impression; an underlying s and a live replacement s; two closely overlapping live s impressions.'
ds[6]['scan_shows']='A paler s-shaped upper turn and lower bowl stand immediately to the right of the dark terminal s. Main confirms the additional impression noticed by all readers. Its displacement is appreciably less than normal character pitch, favouring A/B’s single-letter impression reading over C-reader’s two-live-letter preference; nevertheless no strike or other mark settles the typing operation. The final uncertainty retains all three material alternatives, with single s first. The same retained word crop settled this locus and the adjacent underprints without recropping.'
s=(O/'readers/scan085/B/reading.tex').read_text()
old=r'\unsure{s|\deleted{s}s}'
assert s.count(old)==1
s=s.replace(old,r'\unsure{s|\deleted{s}s|ss}').rstrip()+'\n\\clearpage\n'
(O/'pages/B37-04_37_scan085.tex').write_text(s)
inv=copy.deepcopy(R['B']['inventory'])
inv[36].update(element='Overlapping terminal s impressions in 3.5',kind='text',first_words_or_objects='s; duplicate impression, underlying s, or second live s remain alternatives')
notes="""Undated typescript contents page headed ‘TABLE DES MATIERES’, without a grave on E, and numbered ‘- 538 -’; archive 84 is recorded in a comment. No signature, named author or total page count appears. It lists AVANT-PROPOS, INTRODUCTION, CHAPITRE O/0 .- Préliminaires and three sections with 7, 10 and 7 live numbered entries. The leader fields contain no page-number digits. The old ‘2.4. Fonctions constructibles’ and number-only ‘2.5.’ remain cancelled above their live replacements. The replacement 2.4 has no dotted leader.

The live ‘2.5?’ carries a literal typed question mark. Its role as deliberate doubt or a typing anomaly is not established. The separate marginal hook and displaced low dash may have a questioning or grouping function, which remains uncertain. The connected cancellation stroke is reproduced, and its unnamed writer is not identified from H’s descriptive note. In ‘réciproques’, the probable r under the first corrected p remains uncertain, the p under the following r is readable, and an offset terminal s impression has unresolved duplicate/correction/live-letter status. Both explicit C doubts are retained. H has description only and contributes no collation rows. No mathematical proof or computation was performed."""
math=copy.deepcopy(R['A']['math_reading_decisions'])
math.append('Main compared all three material readings of the terminal s from one retained word crop. The spacing, not expected French spelling, makes the single-s duplicate-impression reading preferred; the other physical alternatives remain marked.')
notation=copy.deepcopy(R['B']['notation'])
for n in notation:
    if n['sign']=='Typed authorial question mark':n['sign']='Typed question mark'
    if n['sign']=='Terminal same-letter impression uncertainty':
        n['latex']=r'\unsure{s|\deleted{s}s|ss}'
        n['evidence']='A pale s-shaped impression overlaps the dark terminal s at less than normal character pitch; duplicate, correction and two-live-letter states remain alternatives.'
out=dict(scan=85,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=math,notation=notation,abbreviations=[],slips=R['A']['slips']+['The additional terminal s impression is preserved with unresolved material status.'],check_events=[],main_crops=json.loads((O/'crops/scan085/manifest.json').read_text()),main_views=list(dict.fromkeys(paths)))
(O/'decisions/scan085.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (O/'workflow_assessment.txt').open('a') as f:f.write('\nScan 085: A/B/C each made five crops. Main viewed five retained crops and made one additional pagination crop because all readers had settled its missing dashes from the half. Seven recorded loci include the two explicit C doubts and an unchanged C-context punctuation target. The linked overprints and newly noticed terminal impression were adjudicated from the same retained word crop, with no recrop. Main retained the first underprint doubt against C-reader’s resolution and ordered all three terminal-s alternatives from observed spacing. The graphic differences were reconciled without imposing punctuation. No brief change was required; differences concerned local ink and material interpretation.\n')
print('Wrote scan 085:',len(ds),'decisions;',sum(d['diff_c'] for d in ds),'C differences;',sum(d['unresolved'] for d in ds),'unresolved.')
