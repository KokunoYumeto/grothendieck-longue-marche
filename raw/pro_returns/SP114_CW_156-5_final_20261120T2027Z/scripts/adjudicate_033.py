from pathlib import Path
import argparse,json
p=argparse.ArgumentParser();p.add_argument('--utc',required=True);a=p.parse_args()
root=Path(__file__).resolve().parents[1]
x=json.loads((root/'review/scan033_findings.json').read_text());x['scan']=33
manifest=json.loads((root/'review/scan033_crop_manifest.json').read_text())
t=(root/'review/scan033_draft.tex').read_text()
t=t.replace(r'F|\in|\exists|E',r'F|\in|E')
t=t.replace(r"I'^{\ast}",r"I'^{\unsure{\ast|k|+}}")
t=t.replace(r'\draw[line width=.4pt] (.65,0) -- (.90,10);',r'\draw[line width=.4pt] (1.0,0) .. controls (.45,2.0) and (.45,8.2) .. (.90,10);')
t=t.replace('% Approximate whole-image band of rule: x200--270, y145--1735.','% Approximate bowed separator geometry; source crop box [65,125,285,1755].')
(root/'pages/J156-5-04_156-5_scan033.tex').write_text(t)
for c in x['changes']:
    c['crop']=c.get('crop','').removeprefix('deliverable/')
    c['main_decision']='Accepted after main-reader inspection of the saved crop; unresolved overwritten ink remains doubtful.'
    i=int(c['id'].split('-')[1])
    if c['kind'].startswith('readable ink left'):c['kind']='readable ink left as `\\ill{}`'
    if i==16:
        c['place']='Je dis, wording and state of et bien'
        c['against_C']=True;c['confidence']='low'
        c['kind']='deletion state (struck given live or live given struck)'
        c['secondary_kind']='misread word'
        c['evidence']+=' The short stroke is mainly below the bodies and favors live underlining; a low cancellation remains an explicit alternative. Word reading and state are counted as one physical locus.'
    if i==17:
        c['against_C']=False;c['against_H']=False;c['certainty_only']=False;c['review_only']=True
        c['main_decision']='Covered with 033-16; not counted a second time.'
    if i==18:
        c['final']=c['final'].replace(r'F|\in|\exists|E',r'F|\in|E')
        c['evidence']='A left upright with two rightward arms favors F. The lower return may belong to the cancellation, leaving a curved membership-like body or E as alternatives. The right-stem orientation required by H’s existential quantifier is not independently visible.'
        c['main_decision']='Retain preferred F and the supported local alternatives; remove ∃ as an unsupported orientation. The heavily crossed original sign is not fully resolved.'
    if i==23:
        c['against_H']=False;c['review_only']=True
        c['main_decision']='H quotes the complete inserted sentence and explicitly identifies its interlinear placement and subsequent cancellation in an editorial note. That same reading/state is acknowledged; different encoding alone is not a substantive H departure.'
    if i==29:
        c['main_decision']='Prefer the sentence as live because all five long cancellation strokes stop above it; preserve a whole-paragraph cancellation as a state alternative. The words/formula themselves are legible.'
    if i==31:
        c['final']=c['final'].replace(r"I'^{\ast}",r"I'^{\unsure{\ast|k|+}}")
    if i==37:
        c['crop']='crops/scan033_separator.png';c['box']=[65,125,285,1755]
        c['final']=c['final'].replace(r'\draw[line width=.4pt] (.65,0) -- (.90,10);',r'\draw[line width=.4pt] (1.0,0) .. controls (.45,2.0) and (.45,8.2) .. (.90,10);')
        c['evidence']='The long separator bows gently toward the left through the middle of the upright sheet, returning rightward at its two ends. The source crop, rotated −90°, shows the complete stroke and the adjacent sideways note. H already describes this rule; C omits it.'
        c['main_decision']='Reproduce the visible bow by a cubic TikZ path adjoining the rotated words; coordinates approximate the source geometry without adding a head or label.'
        c['rotation']=-90
for c in x['unresolved']:
    for k,v in list(c.items()):
        if isinstance(v,str):c[k]=v.replace(r'F|\in|\exists|E',r'F|\in|E').removeprefix('deliverable/')
    if isinstance(c.get('alternatives'),list):c['alternatives']=[v for v in c['alternatives'] if v not in (r'\exists','∃')]
x['unresolved'].append({'place':'bottom, repeated superscript on I and I′','reading':r'I^{\unsure{\ast|k|+}},\ I\prime^{\unsure{\ast|k|+}}','alternatives':['star','k','plus'],'confidence':'low','reason':'Both raised signs have the same upright and short crossing/diagonal strokes. Apply the same unresolved reading to both; the open-subset interpretation does not decide the glyph.','crop':'crops/scan033_bottom_indices.png'})
for z in x['inventory']:
    z['kind']={'number':'text','text block':'text','margin':'margin note'}.get(z['kind'],z['kind']);z['hand']='his hand'
for z in x['second_boxes']:
    z['reading']=z['reading'].replace(r'F|\in|\exists|E',r'F|\in|E').replace(r"I'^{\ast}",r"I'^{\unsure{\ast|k|+}}")
    z['reading']=z['reading'].replace(r'\draw[line width=.4pt] (.65,0) -- (.90,10);',r'\draw[line width=.4pt] (1.0,0) .. controls (.45,2.0) and (.45,8.2) .. (.90,10);')
x['changes'].append({'id':'033-38','place':'bottom, repeated I′ superscript','C':r"I'^{\ast}",'H':r"I'^{*}",'final':r"I'^{\unsure{\ast|k|+}}",'evidence':'The raised glyph repeats the short upright and rightward crossing strokes of the preceding I exponent; both retain the same star/k/plus ambiguity.','crop':'crops/scan033_bottom_indices.png','box':[475,2100,1155,2220],'confidence':'low','kind':'other','against_C':False,'against_H':False,'H_marked':False,'certainty_only':True,'consequential':False,'main_decision':'Certainty-only consistency decision; no preferred symbol changed.'})
x['notes']=[
    'The handwritten page number is 32 followed by a point. The upper portion argues the two inclusions needed for F\\setminus G=F′\\setminus G′. The second inclusion uses a least containing member A of F and an equality of open strata. The side note reads “va se simplifier, cf plus bas”. A largely cancelled attempt at b)⇒c) follows; a new b⇔c paragraph introduces the common open support U and open subsets of ordered index sets. The sheet stops after “On a”. No title or date occurs.',
    'After “prouvons que A′=A”, the parenthesis clearly says “d’où A∈F”, with no prime. A was already chosen in F. The conclusion that would finish the announced goal is A′∈F; it follows by substitution from A′=A and A∈F (033-check-01), but the transcription keeps the unprimed A. H supplies the expected prime and thereby removes the written slip.',
    'The interlinear clause reads “il suffirait F′≪F”, not H’s i.e. sachant. The text invokes “cf lemme plus bas” for the equality of strata. The lemma is not proved within the supplied end of this page, so no full proof check of the second inclusion or the b/c equivalence is claimed. The two “absurde” conclusions and “qed” are the author’s own proof markers, not certifications by this edition.',
    'The two formulas after the least-element choice have a common lower bracket with upturned ends and two worked-over raised marks on A. The first heavily retraced relation remains subset/membership doubtful. After the lemma reference, the words et bien are visible; bien is preferred as live and underlined but a low cancellation remains possible. The cancelled glyph before A,A′ has a left stem and rightward bars favoring F; H’s right-stem existential quantifier is not supported.',
    'All long oblique cancellations in the lower attempt stop above its final “Prouvons A′^{circ(F′)}=A^{circ(F)}” sentence. The edition therefore prefers that last sentence as live, while retaining a whole-paragraph cancellation as an explicit state alternative. The earlier insertion On suppose is itself crossed with the abandoned passage; H records this accurately in an editorial note. A curved insertion leader before Soit is not a textual parenthesis.',
    'At the bottom, the two raised glyphs on I and I′ are alike and both retain star/k/plus doubt. The densely overwritten difference sign is not regularized. The identification written (=F) has a looped upper arm that also admits P; F remains preferred, without using the expected index identification to settle the letter. The comma after U, the abbreviation ens without a point, and the unmatched outer parenthesis before parties are retained.'
]
x['check_events']=[{'statement_id':'033-check-01','type':'targeted proof check','outcome':'The local intended conclusion A′∈F follows immediately by substitution from the stated A′=A and the earlier choice A∈F. The written parenthesis has unprimed A∈F. This checks only the substitution/target mismatch, not existence of the least containing member or the equality of strata.'}]
x['adjudicator']='GPT-6 Astra Pro, main reader, SP114 second pass; effort setting not exposed';x['adjudicated_utc']=a.utc
(root/'review/scan033_adjudicated.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
with (root/'review/main_image_reviews.tsv').open('a') as f:
    f.write('033\twhole source scan\tmain reader\tinspected once for layout before first adjudication\n')
    for z in manifest:f.write('033\t'+z['crop'].removeprefix('deliverable/')+'\tmain reader\tinspected before first adjudication\n')
rows=sum(bool(c.get('certainty_only') or c.get('against_C') or c.get('against_H')) for c in x['changes'])
with (root/'progress.log').open('a') as f:
    f.write('Final first-reading assignment: B received033 when free after031. First-reading page order: A026,B027,C028,A029,C030,B031,A032,B033. No blind pass began before all eight main adjudications.\n')
    f.write(f"scan 033 done {a.utc}: {x['line_count']} lines read, {len(manifest)} places cropped, {rows} rows\n")
print('Saved033',rows,'rows')
