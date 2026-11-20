from pathlib import Path
import json,copy
OUT=Path(__file__).resolve().parents[1];stem='C123-01_123_scan003'
r={x:json.loads((OUT/'readers'/stem/x/'report.json').read_text()) for x in ('R1','R2','R3')}
s=json.loads((OUT/'decisions'/(stem+'_pending_spec.json')).read_text());s['base_reader']='R1'
s['text_edits']=[{'old':r'\deleted{\unsure{W}}D','new':r'\deleted{W}D'}]
s['exclude_difference_ids']=['R1-01','R1-08']
R1='readers/'+stem+'/R1/';R3='readers/'+stem+'/R3/';M='decisions/'+stem+'_crops/'
s['difference_overrides']={
 'R1-02':{'final':r'\deleted{W}D','kind':'deletion state (struck given live or live given struck)','crop':R1+'crop01_normalisateur_capital.png','readers':r'R1: \deleted{\unsure{W}}D; R2: \deleted{W}D; R3: \deleted{W}D. The main reader resolves the earlier W from the visible interior diagonals.','evidence':'The outer curved right bowl and straight left stem belong to D. Inside it survive the oblique W strokes and a pointed lower remnant, matching the nearby unovertyped W; they are not a parallel second D contour. The earlier W is retained as deleted.'},
 'R1-03':{'crop':R3+'crop_02_primitive.jpg'},
 'R1-04':{'crop':R3+'crop_02_primitive.jpg','readers':r'R1: h. \unsure{eme|ème}, explicit gap after stop; R2: \unsure{h.ème|h.eme}; R3: h. \unsure{ème|eme}. Final favors the visible unaccented first e, retaining ème because the upper line crosses its accent zone.'},
 'R1-05':{'crop':R3+'crop_02_primitive.jpg','readers':'R1: ordinal physically above donnée in a small TikZ layout, attachment left open; R2: after-donnée insertion with attachment doubt; R3: after-donnée insertion. Final preserves the observed interlinear geometry without choosing an unmarked syntactic anchor.'},
 'R1-06':{'crop':M+'quotation_marks.jpg','evidence':'The crop shows two short upright typewriter strokes at both ends of droites cycliques. These are double quotation marks, represented by the required backticks/apostrophes; no angled guillemets are present.'},
 'R1-07':{'crop':R3+'crop_03_unit_group.jpg','evidence':'Both ordinary typewriter Z letters have a detached low horizontal rule separated from the lower serif by white. H’s bold-font representation loses these underlines.'},
 'R1-09':{'crop':M+'NB_insertion.jpg','evidence':'The phrase en commutant à l’action de W occupies a separate half-height typed interline between the normal NB baseline ending opère and the next baseline beginning librement. It is an inserted phrase, not ordinary continuous baseline text.'}
}
s['c_doubts']=copy.deepcopy(r['R1']['c_doubts'])
for d in s['c_doubts']:
 if 'normalisateur' in d.get('place','') or 'capital' in d.get('place',''):
  d.update(decision=r'\deleted{W}D',crop=R1+'crop01_normalisateur_capital.png',evidence=s['difference_overrides']['R1-02']['evidence'])
s['remaining_doubts']=[{'place':'Interlinear ordinal, first e','reading':r'h. \unsure{eme|ème}','alternatives':'The grave accent may be hidden by the preceding line’s lower strokes.','confidence':'medium'},{'place':'Interlinear ordinal, attachment','reading':'Physical position above donnée retained in TikZ; no caret added.','alternatives':'Before donnée, after donnée, or before primitive; the linear attachment is not secured by an ink call.','confidence':'low'}]
s['inventory']=copy.deepcopy(r['R1']['inventory'])
for d in s['inventory']:
 if d['element']=='Old capital under the live D':d['first_words_or_objects']='W under D'
 if isinstance(d.get('position'),dict):d['position']='Whole-image box '+str(d['position']['bbox'])
s['abbreviations']=r['R3']['abbreviations'];s['main_new_crops']=2
s['consequential']=['D overtypes W in normalisateur de: the overtyped earlier W is retained instead of treating the glyph as double-struck D.','H omits the canceled de under primitive and loses the interlinear status of the commuting-action clause; both are retained.']
s['workflow_note']='All three complete readings were compared. The main reader used the existing overtype and ordinal crops, inspected R1’s tighter D/W crop to decide the differing certainty, and made two crops for the quotation marks and NB insertion already settled by the readers’ halves. Handwritten wrappers for the unchanged c and star were audited in the inventory but excluded from change counts as macro-only differences. H’s explicitly adjacent unnumbered heading was removed from the packet and not counted as an error. Brief version 04, first used on 123/016, adds physical layout for unanchored interlinear additions and clarifies the exclusion of handwriting-wrapper differences without an opposing source-origin claim. This follows the h.eme attachment disagreement and repeated wrapper-only rows.'
# Reader checks are recorded according to what was actually done.
for rn in ['R1','R2','R3']:
 for ev in r[rn]['math_checks']:
  if 'reading only' in str(ev.get('type','')):continue
  content='; '.join(str(ev[k]) for k in ['check_performed','work','result','limit','limits'] if k in ev)
  sid='123-003-line-count' if ('count' in str(ev.get('place',ev.get('claim',ev.get('check','')))).lower() or 'orbit–stabilizer' in content or 'orbit-stabilizer' in content) else '123-003-commuting-stabilizers'
  s['check_events'].append({'statement_id':sid,'who':'GPT-6 Astra Pro; effort not exposed; p03_'+rn.lower(),'type':'targeted proof check','outcome':content})
s['notes']+='\n\nThe initial c and the unit-group star are handwritten according to all three image readings; that medium is marked in the consolidated file and inventory. Their unchanged glyphs are not counted as witness reading differences merely because one macro set lacks a handwriting wrapper. The quotation marks are upright typewriter double marks, not H’s guillemets. The only remaining doubts concern the ordinal’s accent and its unmarked syntactic attachment.'
(OUT/'decisions'/(stem+'_spec.json')).write_text(json.dumps(s,ensure_ascii=False,indent=2))
