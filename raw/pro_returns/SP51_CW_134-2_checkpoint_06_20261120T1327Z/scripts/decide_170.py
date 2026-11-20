from pathlib import Path
from datetime import datetime, timezone
import json
root=Path(__file__).resolve().parents[1]
reports={r:json.loads((root/f'records/scan170/{r}/report.json').read_text()) for r in 'ABC'}
A=reports['A']; C=reports['C']
diffs=A['differences']
for x in diffs:
    if 'opening verb' in x['place']:x['kind']='misread word'
    elif 'quotation marks' in x['place']:
        x['crop']='crops/scan170/main/01_quotes.jpg';x['kind']='other'
    elif 'after convenable' in x['place']:
        x['crop']='crops/scan170/C/02_ou_ce_punctuation.png';x['kind']='other'
    elif 'abbreviation after au' in x['place']:
        x['crop']='crops/scan170/C/03_equals_abbreviation.png';x['marked_in_H']=False;x['kind']='abbreviation expanded or spelling modernised'
        x['evidence']='Two near-horizontal strokes are visible; the lower has a distinct small entry hump. The equals-like transcription is preferred, but the compressed overlined-m alternative cannot be excluded. The word même is not written in full.'
    elif 'live capital after cancellation' in x['place']:
        x.update(final='G_n',differs_C=True,differs_H=False,crop='crops/scan170/C/06_deleted_live_capitals.png',confidence='medium',kind='other',evidence='The detached roof occupies the absent upper-left/upper arc of the G bowl. The lower part is not itself a complete G beneath an extra hat. Plain G is selected; the earlier hatted alternative is removed.')
    elif 'paragraph division' in x['place']:
        x['crop']='crops/scan170/main/02_paragraph.jpg';x['kind']='insertion or placement'
        x['evidence']='The previous sentence fills most of its line, and En analogie follows at the ordinary left margin with ordinary interline spacing. There is no independent paragraph cue. A new sentence alone does not establish a new paragraph.'
    elif 'after closing parenthesis' in x['place']:
        x.update(final='familier\\ldots) Il',differs_C=False,differs_H=True,crop='crops/scan170/C/12_final_punctuation.png',confidence='medium',kind='other',evidence='After the closing parenthesis only tiny pale specks survive, unlike the weighted strokes of the ellipsis and parenthesis. No deliberate full stop is established; preserve the open continuation of C and readers B/C.')
    elif 'word after inquiétant' in x['place']:x['kind']='misread word'
    elif 'inserted category symbol' in x['place']:x['kind']='misread symbol or index'
    elif 'cancelled capital' in x['place']:x['kind']='misread symbol or index'
    elif 'first limit sign' in x['place']:x['kind']='other'
    else:x['kind']='other'
stroke=next(x.copy() for x in C['differences'] if x.get('id')=='D15')
stroke.update(kind='drawing or diagram',final='\\figure{...}: short pale down-right curve with hooked end, anchored below nous',evidence='A continuous pale curved stroke below nous has a tapered beginning and returning hooked end. It is distinct from the surrounding copy grain. Its shape is reproduced in TikZ at that text anchor without assigning a linguistic meaning or certain hand.')
diffs.insert(-1,stroke)
for x in diffs:x['marked_in_H']='yes' if x.get('marked_in_H') else 'no'
text=(root/'records/scan170/A/reading.tex').read_text()
text=text.replace('% C page filename: H134-05_134-2_scan170.tex\n','').replace('\\unsure{G|\\widehat G}_n','G_n').replace('familier\\ldots). Il','familier\\ldots) Il')
mark=r'''% Faint interlinear curved mark below nous, whole-image x290–318, y1991–2018; hand/function uncertain.
\raisebox{-1.8ex}[0pt][0pt]{\makebox[0pt][r]{\parbox{3mm}{\figure{\begin{tikzpicture}[x=1mm,y=1mm]
\draw[line width=0.25pt,gray] (0,0) .. controls (0.35,-1.15) and (1.55,-2.45) .. (2.2,-2.55) .. controls (2.65,-2.7) and (2.7,-2.2) .. (2.38,-1.85);
\end{tikzpicture}}}}}'''
text=text.replace('mais cela nous attire','mais cela nous\n'+mark+'\n attire')
(root/'pages/H134-05_134-2_scan170.tex').write_text(text)
unresolved=[x for x in A['unresolved'] if 'live G' not in x['place'] and 'live symbol' not in x['place']]
comparisons=[
 {'place':'L5 abbreviation','A':'\\unsure{=|\\overline m}','B':'=','C':'=','decision':'Retain = with overlined-m alternative: main inspection of C/03 shows a real low entry hump; a plain equals-like form is strongest but not unique.'},
 {'place':'L7 after n-groupoïde','A':', Si','B':'. Si','C':', Si','decision':'Comma selected: C/04 has a thick head and clear descending tail, not a point.'},
 {'place':'L8 live G','A':'\\unsure{G|\\widehat G}_n','B':'\\unsure{G|\\widehat G}_n','C':'G_n','decision':'Plain G selected from C/06: detached upper curve completes the broken G bowl; it is not an added accent over a complete G.'},
 {'place':'L12 preposition','A':'\\unsure{de|du}','B':'\\unsure{de|du}','C':'de','decision':'Retain de|du: C/07 favours the flat e continuation, but the dark retracing does not fully distinguish the final cursive form.'},
 {'place':'L12–13 paragraph boundary','A':'continuous paragraph','B':'paragraph break','C':'continuous paragraph','decision':'Continuous paragraph selected on main/02: no blank line, indent or separator; the preceding line is nearly filled.'},
 {'place':'Below nous, L20','A':'no separate mark identified','B':'no separate mark identified','C':'pale curved mark; TikZ','decision':'Include the observed continuous curved stroke from C/11; place it below nous using a zero-width box so the prose paragraph is not interrupted. Hand and function remain unspecified.'},
 {'place':'L23 final punctuation','A':'\\ldots). Il','B':'\\ldots) Il','C':'\\ldots) Il','decision':'No full stop selected: C/12 shows only pale copy specks after the parenthesis. The actual dot-like pen marks elsewhere are darker and distinct.'}
]
review=[]
for x in A['c_doubts'][:8]:
    resolved=x['place'] in ['line 8 correspondent','line 8 live symbol','line 18 commutent']
    earlier=x['final'];final='G_n' if x['place']=='line 8 live symbol' else x['final']
    review.append({'place':x['place'],'earlier':earlier,'decision':('resolved: ' if resolved else 'retained: ')+final,'evidence':'Main inspected the saved crop '+x['crop']+'. '+('See three-reader decision.' if x['place'] in ['line 5 abbreviation','line 8 live symbol','line 12 preposition'] else 'Strokes documented in the change table or reader return.')})
inv=C['inventory']
for x in inv:
    x['sheet_kind']='letter'
    if x['hand'].startswith('author'):x['hand']='his hand'
    if x['kind']=='drawing':x['placement_note']='Reproduced below nous in a zero-width inline box containing the prescribed figure macro; no new prose paragraph is introduced.'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
events=[]
for x in A['check_events']:
    events.append({'statement_id':x['statement_id'],'date':now,'who':'GPT-6 Astra Pro; inherited effort not separately exposed; /root/scan170_a','type':x['type'],'outcome':x['outcome']+' Method: '+x['method']})
events.append({'statement_id':'S170-notes','date':now,'who':'GPT-6 Astra Pro; inherited effort not separately exposed; /root','type':'carried as background without fault found','outcome':'The definitions, proposed equivalence and recovery by exactness reported in the scan-170 note are source assertions/proposals. No proof is claimed. Visual checks of words and marks are recorded in the changes log, not relabelled as mathematical proofs.'})
d={'scan':170,'folder':'H134-05','filename':'H134-05_134-2_scan170.tex','brief':'briefs/brief_v01_scan170.md','differences':diffs,'reader_comparisons':comparisons,'doubt_review':review,'unresolved':unresolved,'inventory':inv,'abbreviations':[{'written':x['written'],'expansion':x['possible_expansion']} for x in A['abbreviations']],'notes':'''**S170-notes.** The page proposes a definition of a special or n-galoisienne n-category by locally constant (n−1)-champs, and a second formulation using n-functors from a groupoid. It names the fundamental n-groupoid, local n-systems and geometric realization, then proposes recovering the groupoid inside an underlined Hom category using exactness. These proposals are not proved here. The writer’s own qualifications are “ce qui doit revenir au” followed by the equals-like abbreviation, “doit s’interpréter,” “on a envie de dire,” and the unfinished “Il est prudent dans tout.”

The source and target in Hom and the immediately following functor expression agree; reader A performed only that local consistency check (scan170-S3-Hom-description). The ink says **n-systèmes**, while the earlier definition says **(n−1)-champs**; neither the transcription nor the notes silently alters the rank. Mathematical expectation suggests inverse limits in the first limit expression, but its arrowhead remains visually uncertain. The live G after the cancelled symbol is read as an interrupted G bowl, with no separate hat.

This is a handwritten letter continuation, author page **25**, archival pencil number **170**. There is no date, title, salutation, signature or stated total page count on this sheet. The pale hooked interlinear stroke below “nous” is reproduced without assigning it meaning or certain authorship.''','check_events':events,'crop_counts':{r:len(reports[r]['crops']) for r in 'ABC'},'workflow_note':'All three independently read 23 lines. Disagreements concerned paragraph inference, a pale nontext stroke, punctuation and the threshold for resolving doubtful cursive marks. Main reused 13 reader crops and made 2 new crops. H emph convention clarified equally to all readers.'}
d['crop_counts']['main']=2
# Normalize evidence citations to the crops actually inspected by the main reader.
_reference_map={'A/02_inserted_alphabet.png': 'C/01_inserted_capital.png', 'A/03_au_equals.png': 'C/03_equals_abbreviation.png', 'A/11_groupoide_punctuation.png': 'C/04_groupoide_punctuation.png', 'A/05_cancelled_and_live_G.png': 'C/06_deleted_live_capitals.png', 'A/06_de_G.png': 'C/07_geometrique_de.png', 'A/08_inverse_limit.png': 'C/09_inverse_limit.png'}
for _x in d['differences']:
    for _a,_b in _reference_map.items():
        if _x.get('crop')=='crops/scan170/'+_a:_x['crop']='crops/scan170/'+_b
for _x in d['doubt_review']:
    for _a,_b in _reference_map.items():_x['evidence']=_x['evidence'].replace('crops/scan170/'+_a,'crops/scan170/'+_b)

(root/'records/scan170/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(root/'records/scan170/main_viewed_crops.txt').write_text('\n'.join(['crops/scan170/A/01_on_dira.png','crops/scan170/C/01_inserted_capital.png','crops/scan170/C/02_ou_ce_punctuation.png','crops/scan170/C/03_equals_abbreviation.png','crops/scan170/C/04_groupoide_punctuation.png','crops/scan170/A/04_correspondent.png','crops/scan170/C/06_deleted_live_capitals.png','crops/scan170/C/07_geometrique_de.png','crops/scan170/A/07_commutent.png','crops/scan170/C/09_inverse_limit.png','crops/scan170/A/09_engrenage.png','crops/scan170/C/12_final_punctuation.png','crops/scan170/C/11_isolated_stroke.png','crops/scan170/main/01_quotes.jpg','crops/scan170/main/02_paragraph.jpg'])+'\n')
(root/'notation.md').write_text('''# Working notation table

Entries are visual readings, not rules imposed on subsequent pages. Recheck each on the new page. Line numbers count the main handwritten baselines; above-line additions are tied to their destination.

| Sign or form | Representation | Evidence / scope |
| --- | --- | --- |
| Open two-lobed category capital with low n | `\\unsure{\\mathcal E|E}_n` at first occurrence on each page; then `\\mathcal E_n` | Scan 170 L1 insertion and later repeats; rounded capital, typographic alphabet still uncertain. |
| Groupoid capital with long descending return | `G_n` | Scan 170 L6–12; interrupted upper loop on L8 is read as part of G, not a separate hat. Cancelled L8 glyph remains `G_n|\\mathcal E_n`. |
| Equals-like shorthand for même | `\\unsure{=|\\overline m}` when this form remains ambiguous | Scan 170 L5: near-horizontal top and lower line with a low entry hump. Do not spell out même in the transcription. |
| Category targets | `(n\\text{-}\\mathrm{Cat})`, later `(n\\text{-}\\mathrm{cat})` | Scan 170 L6 capital C; L15–16 lower c. Preserve observed case per occurrence. |
| Hom notation | `\\underline{\\mathrm{Hom}}_n` | Scan 170 L15: single rule beneath Hom, low n. |
| Limits | `\\unsure{\\varprojlim|\\underline{\\lim}}`, then `\\varinjlim` | Scan 170 L18–19: first left barb incomplete; second right arrow clear to all readers. Do not resolve the first from mathematics alone. |
| Double quotation marks | two backticks / two apostrophes | Scan 170 L1 paired upper ticks, not guillemets. |
| Underlines | `\\uline`, mathematical `\\underline` | Scan 170 spéciale, galoisienne, Hom and NB single-ruled. H emph is equivalent author emphasis where scope agrees. |
| Abbreviations | `cat.`, `loc.`, `top.`, `NB` | Scan 170. Preserve observed stops and letter case. |
| Local-system rank | `n` in n-systèmes | Scan 170 L10; distinguish earlier `(n-1)` in champs. |
''')
print('Scan 170 decision and page written; assemble before registering done.')
