from pathlib import Path
import csv, copy, datetime, hashlib, json, re

R=Path('/workspace/scratch/ddf8babdc42e/out')
J=R/'review/scan008_final.json'
D=R/'second/H156-01_156-7_scan008_decisions.json'
A=R/'second/H156-01_156-7_scan008_adjudication.tsv'
O=R/'second/H156-01_156-7_scan008_root_observations.md'
N=R/'SP115_CW_156-7_notes.md'
H=R/'SP115_CW_156-7_hand_log.md'
raw=J.read_bytes(); d=json.loads(raw); before=copy.deepcopy(d)
dec=json.loads(D.read_text())
with A.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
audit={x['box']:x for x in rows}
assert len(rows)==32 and d['blind_audit']['changed_places']==7
assert d['blind_audit']['completed_utc']=='2026-11-20 20:16:08 UTC'
for row in rows:
    expected=row['first']
    for p in dec['patches']: expected=expected.replace(p['old'],p['new'])
    expected=dec['boxes'].get(row['box'],{}).get('final',expected)
    assert row['final']==expected,row['box']
protected=[R/'pages/H156-01_156-7_scan008.tex',D,A,O]
protected += [R/f'second/H156-01_156-7_scan008_{suffix}' for suffix in ('first.tsv','second.tsv','boxes.tsv','initial.tex')]
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
hashes={str(p):digest(p) for p in protected}
pat=re.compile(r'^## Scan\s*008\b.*?(?=^## |\Z)',re.M|re.S)
oldN=N.read_text(); oldH=H.read_text()
mN=pat.search(oldN);mH=pat.search(oldH);assert mN and mH
proof=next(x for x in mN.group().split('\n\n') if x.startswith('**N008-strata'))
newN=r"""## Scan 008 — manuscript page 7

The opening proposes putting the disjointness/compatibility axioms before the axioms on lieux, so as not to seem to derive them from the latter. The insertion is **avoir l’air de**; H's extra moins élégants is absent. The quoted adjective is now `facultatif\unsure{s}`: the terminal loop does not securely separate a final s. The following **des'** is resolved and retained literally despite its grammar. The definitions introduce disjointness of figures and its expression in terms of pairs of strata; the next display interprets disjointness in M as compatibility together with absence of a common lower bound. The raised definition label remains abbreviated and doubtful, **dfn/defn/def** (completed blind audit B003, B004 and B006; changes 008-A01–008-A03).

"""+proof+r"""

The first definition has a clear barred G after compatibility but an open **C** in `F∩C`. In the cancelled Cor, the K-definition has uncertain **C/G**, while the following compatibility assertion and `Y≪C` have open C-shaped operands. The surrounding quantification and parallel formulas would require G at those places for the intended two-variable statement. The transcription retains the visible distinctions and marks intermediate G/C forms in place. A categorical inference that every open form is simply this writer's G was considered and rejected after comparison of the local strokes. These choices were retained in the completed blind audit (B005, B006, B031, B034 and B038).

The NB verb is a partial ending revision: `résul\deleted{\unsure{tera}}\inserted{te}`. The initial résul remains live; only the tentative longer ending tera is cancelled, with te inserted above it. The raised précédents remains attached to axiomes. In the separate cancelled explanation, i.e. and c'est un are tentative, and the final symbol retains the alternatives ∃ and ]. The cancelled article la remains tentative, with no separate live replacement added; d'axiome/d'axiomes at the edge also remains uncertain. The NB asserts one implication between the absence of common inclusion bounds and the absence of common refinement bounds, and promises the converse from later axioms. That claim has not been independently established here (blind B011, B012 and B014–B016; changes 008-A04 and 008-A05).

The lower **At DC 1** and its Cor are cancelled together by three long oblique strokes. The smaller earlier deletions and insertions inside that block remain separately encoded. Inserted **soit** is now resolved, while the cancelled Soient and other retained local doubts remain marked. In the Cor's first Sup-limit operand, the surviving letter is plain **F**: the upper curve belongs to the p of Sup, with no independent tilde. The old X/tilde-X layer remains uncertain; the second old Y/tilde-Y and surviving tilde-G/tilde-C alternatives also remain. The note **et alors seulement** and its inserted **cf Cor** are part of this cancelled draft. The three-letter inscription in the Cor is literally **ses**, inside an oval with a visible upper-right gap; its logical role does not replace it with ssi (blind B020, B021, B031–B033 and B035; changes 008-A06 and 008-A07).

The slanted margin calls an atelier **spacieux** if it satisfies the condition and gives ateliers simpliciaux as a counterexample. One long block strike crosses the note; the intended extent of cancellation remains uncertain. Both the live and cancelled alternatives are marked at the note itself, with every word retained. Neither the extra axiom nor the simplicial counterexample was independently proved. The only written numbers on this sheet are manuscript page 7 and the axiom numeral 1; there is no date. The completed blind audit retained the slanted-note text and state alternatives, spacieux, the C/G distinctions and literal ses.

"""
newH=r"""## Scan008 additions

- Open C-shaped operands coexist with a clearly barred G. The initial claim that all such open forms are shortened Gs is withdrawn; first intersection and final Cor operands support C, while intermediate forms retain C/G doubt. This local contrast is consistent with the clear Cs preserved on 004/005, but is not a universal substitution rule. The blind audit retained these distinctions.
- The quoted facultatif(s) has a compressed terminal loop after f; a separate final s is not secure, so the current reading is `facultatif\unsure{s}`. Its high quotation ticks remain clear. In contrast, the short **des'** group separates into d, e, angular s and a detached apostrophe; the literal ungrammatical form is resolved (B003–B004).
- The small raised definition abbreviation has a looped d, tall narrow stroke and short terminal run. Its alternatives remain **dfn/defn/def**, without expansion to a full word (B006).
- The NB correction is confined to the verb ending: live **résul**, cancelled tentative **tera**, and raised inserted **te**. The t staff and e loop support the replacement; the longer underlying ending remains uncertain. The separate cancelled phrase keeps tentative **i.e.**, tentative **c'est un**, and **∃/]** alternatives (B011–B014).
- The local cancelled et, Il, quantifier and rewritten Cor operands remain distinguishable from three thin continuous block strikes. Both correction layers are preserved. Inserted **soit** is resolved from its s, open o, dotted i and crossed t, while remaining inside the cancelled draft (B020–B021).
- The surviving first Cor Sup-limit operand is plain **F**, with an upright and two arms. The apparent upper curve continues from Sup's p and is not an independent tilde. The earlier X/tilde-X uncertainty remains; the second operand retains its separate wave and G/C uncertainty (B031–B033).
- The circled word has a looped e and reads **ses**; the enclosing oval has an upper-right gap. The blind audit retained both features.
- At DC is underlined while the numeral 1 is outside that underline. The slanted margin underline belongs only to spacieux. Its uncertain overall cancellation state remains separately recorded.

"""
fullN=oldN[:mN.start()]+newN+oldN[mN.end():]
fullH=oldH[:mH.start()]+newH+oldH[mH.end():]
source='out/second/H156-01_156-7_scan008_decisions.json and H156-01_156-7_scan008_root_observations.md; completed root blind audit 2026-11-20 20:16:08 UTC'
notes={x['id']:x for x in d['notes']}
notes['008-N1'].update(claim='The initial first-reader doubt-disposition counts are historical. Current readings follow the completed root blind audit: 32 differing boxes and seven changed places.',source=source,reasoning_if_any="The audit resolves literal des', inserted soit and the surviving plain F; narrows the NB revision to the ending; and retains or extends final-s, definition-label and cancelled-phrase doubts. Cancelled tera and old X/tilde-X remain tentative. No current claim is made that all initial doubts stayed unresolved.")
notes['008-N3'].update(claim='The exact deletion scope of the slanted note remains uncertain; the current transcription explicitly records both live and cancelled alternatives.',source=source+'; B017',reasoning_if_any='The completed audit retained the complete atelier/spacieux/simpliciaux wording and both source-state alternatives. The crossing block stroke does not settle the intended scope.')
notes['008-N5']['source']=source+'; B034 and B035'
notes['008-N7']['claim']='During the initial first-reader stage, three crop windows were extended before their pending decisions because upper strokes touched the original edge.'
notes['008-N8'].update(claim='Root adjudication after blind second reading is complete; the first-reader proposed TeX remains a historical provisional artifact.',source=source+'; current out/pages/H156-01_156-7_scan008.tex',reasoning_if_any='The page was updated by root before this metadata synchronization. This synchronization makes no new ink decision and does not change the page, collation changes, doubts, or frozen TSVs.')
d['notes'] += [
 {'id':'008-N9','claim':r"The opening has quoted facultatif\unsure{s} and literal des'; the definition label retains dfn/defn/def.",'source':source+'; B003, B004, B006; 008-A01–008-A03','reasoning_if_any':'The completed audit distinguishes the uncertain terminal s from the resolved d-e-s-apostrophe group; the small definition label remains abbreviated and uncertain.'},
 {'id':'008-N10','claim':r"The NB verb is résul\deleted{\unsure{tera}}\inserted{te}; the cancelled explanation retains tentative i.e., tentative c'est un, and final alternatives \exists/].",'source':source+'; B011, B012, B014; 008-A04–008-A05','reasoning_if_any':'The live prefix is not cancelled or repeated. The raised te is a separate insertion, now represented by its own inventory element. Neither the underlying ending nor the cancelled explanatory phrase is promoted to certainty.'},
 {'id':'008-N11','claim':r"Inserted soit is resolved. The surviving first Cor Sup-limit operand is plain F, after \deleted{\unsure{\widetilde X|X}}.",'source':source+'; B020, B021, B031, B032; 008-A06–008-A07','reasoning_if_any':'The upper curve belongs to the p of Sup; the earlier X/tilde-X layer remains doubtful. The second operand, C/G choices, global cancellation, slanted-note state and literal ses are retained.'}
]
h=d['hand_log']
h[0]['place']='facultatif(s) and F et G/C disjoints'
h[0]['observation']='Both quotation pairs consist of high pen ticks, consistently unlike guillemets. The ticks remain clear, but the compressed terminal loop after facultatif does not securely establish a separate final s (blind B003).'
h[1]['observation']="The tall l strokes settle d’ailleurs. The ending of termes/terme remains uncertain; the blind audit resolves des' as d, e, angular s and detached apostrophe. The literal grammar is retained. No general final-s rule is inferred."
h[3]['observation']='The current page uses M in prose, relation undersets and membership. Initial alphabet doubts were consolidated at first occurrences on the earlier pages by root; they are not asserted as unresolved at each occurrence on this page.'
h[4]['observation']='The local correction strokes are denser and shorter than the three thin long diagonal strokes. In the NB, live résul precedes cancelled tentative tera and inserted te; the correction does not cancel the whole word. Local states inside the later cancelled At/Cor block remain distinct.'
h += [
 {'habit':'Small raised definition abbreviation remains unresolved','place':'first definition label; blind B006','observation':'The completed audit retains dfn/defn/def from the looped d, tall narrow stroke and short terminal run, without expanding the abbreviation.'},
 {'habit':'Independent tilde distinguished from an operator descender','place':'first and second Cor Sup-limit operands; blind B031–B033','observation':'The curve over the surviving first F continues from Sup’s p, so that F is plain. The earlier X/tilde-X remains uncertain. A separate wave is present over the second replacement, whose G/C interior remains doubtful.'},
 {'habit':'Small separately placed insertion retains a clear letter sequence','place':'At lower-left soit; blind B020–B021','observation':'The completed audit resolves s, open o, dotted i and crossed t as soit. Its insertion state and the enclosing block cancellation are preserved.'}
]
inv=d['inventory'];assert len(inv)==30
items={x['element']:x for x in inv}
items['Opening paragraph']['first_words_or_objects']="Je voudrais maintenant faire passer les axiomes; quoted facultatif(s), terminal s uncertain; literal des'"
items['Definition of disjoint F,G']['first_words_or_objects']=r'F\parallel G/C; equivalence label dfn/defn/def uncertain; compatibility; F∩C=empty figure'
items['Parenthetical NB']['first_words_or_objects']='(NB Il résul [cancelled tentative tera] [inserted te] des axiomes ...'
items['NB verb overwrite'].update(position='verb ending after live résul following Il, y≈1435',first_words_or_objects='partial ending revision: live résul; cancelled tentative tera; raised replacement te')
pos=next(i for i,x in enumerate(inv) if x['element']=='NB verb overwrite')+1
inv.insert(pos,{'element':'NB replacement ending te','kind':'insertion','position':'raised above the cancelled verb ending after live résul, y≈1435','first_words_or_objects':'te; replacement ending, not a repeated whole verb'})
items['NB cancelled explanation']['first_words_or_objects']="tentative i.e.; tentative c'est un; final ∃/]; all locally cancelled"
items['At local lower-left addition']['first_words_or_objects']='soit, resolved; insertion within globally cancelled block'
items['Cor prior first index operand']['first_words_or_objects']='old X/tilde-X uncertain; overwritten by plain F; upper curve belongs to Sup p'
items['Cor prior second index operand']['first_words_or_objects']='old Y/tilde-Y uncertain; surviving tilde-G/tilde-C uncertain'
assert len(inv)==31
assert [x['element'] for x in inv if x['element']!='NB replacement ending te']==[x['element'] for x in before['inventory']]

def annotate(row,fields,reading,note,boxes):
 row['current_annotation']={'status':'initial metadata retained; current adjudication supersedes the specified claim','superseded_or_clarified_fields':fields,'current_reading':reading,'observation':note,'source':source+'; '+boxes}
nt=d['notation']
annotate(nt[2],['place'],r'F\cap C=\varnothing_{\mathscr F}','The initial place label F∩G is superseded by the current literal C-shaped intersection operand. The empty-figure sign itself is unchanged.','B006')
annotate(nt[3],['form','reading','observation'],r'\mathscr F','The current page uses script F. The first-reader alphabet doubt was consolidated at its earlier first occurrence by root; this entry is historical, not a renewed per-occurrence doubt.','root_adjudication.decisions')
annotate(nt[4],['form','reading','observation'],'M','The current page uses M. The initial alphabet question was consolidated at its earlier first occurrence by root; no new doubt is introduced here.','root_adjudication.decisions')
annotate(nt[5],['observation'],r'\deleted{\unsure{\widetilde X|X}}F','The first surviving Cor-limit operand is plain F: the upper curve belongs to Sup’s p. The old X/tilde-X remains doubtful. Clear tildes in the quantified and At displays, and the second Cor operand’s tilde-G/tilde-C uncertainty, are retained.','B031, B032, B033')
di={x['place']:x for x in d['deletion_insertion_audit']}
specs=[
 ('NB overwritten verb',['decision','evidence.observation'],audit['B012']['final'],'The whole-word deletion and repeated surviving-word encoding are superseded. Keep live résul, locally cancelled tentative tera, and separately inserted te.','B011, B012'),
 ('NB cancelled explanatory line',['decision','evidence.observation'],audit['B014']['final'],"The local deletion is retained, but c'est un is now tentative and the final alternatives are ∃/]. The original C_span remains a historical witness quotation.",'B011, B014'),
 ('At opening through lower hypothesis addition',['decision'],audit['B020']['final'],'The outer cancellation and local earlier states are retained. The only revised reading here is inserted soit, now resolved.','B020, B021'),
 ('Cor heading and Sup formula',['decision','evidence.observation'],audit['B031']['final'],'The current excerpt keeps the C/G intersection doubt and second replacement tilde-G/tilde-C doubt, and resolves the first surviving operand to plain F. The original C_span is not a current final excerpt.','B031, B032, B033'),
 ('Cor first prior limit operand',['evidence.observation'],r'\deleted{\unsure{\widetilde X|X}}F','The old X/tilde-X uncertainty is retained; the current surviving F has no independent tilde. This distinguishes the old-layer doubt from the resolved new layer.','B032'),
 ('Cor second prior limit operand',['evidence.observation'],r'\deleted{\unsure{\widetilde Y|Y}}\unsure{\widetilde G|\widetilde C}','The description final G region is historical shorthand. Both old Y/tilde-Y and surviving tilde-G/tilde-C remain uncertain.','B033'),
 ('Cor first assertion row',['decision','evidence.observation'],audit['B034']['final'],'Global and local deletion states are retained. The current literal operand is C, and the ses enclosure is an oval with an upper-right gap; the C_span’s G and full ellipse are historical witness content.','B034, B035, B036'),
 ('Cor final implication row',['decision'],audit['B038']['final'],'The row remains globally cancelled. The current second refinement operand is literal C in Y≪C; the C_span’s G is historical witness content.','B038'),
 ('At soit',['decision','evidence.observation'],r'\inserted{soit}','The earlier still-doubtful claim is superseded: soit is resolved, while insertion state and enclosing global cancellation remain.','B020, B021')
]
for place,fields,reading,note,boxes in specs:annotate(di[place],fields,reading,note,boxes)
previous_status=d['status']
d['status']='root adjudication after blind second reading complete; metadata synchronized'
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['metadata_sync']={'completed_utc':now,'basis':source,'scope':'Current scan008 notes and hand-log sections; embedded notes, hand_log and inventory descriptions; annotations preserving superseded initial notation and C-state audit metadata; current status.','inventory_before':30,'inventory_after':31,'inserted_inventory_element':'NB replacement ending te','historical_claims_preserved_in_annotations':True,'historical_metadata_fields':{'doubt_summary':'Initial first-reader count record, retained unchanged; current doubts array and completed blind_audit are authoritative for the present state.','validation':'Initial validation record, retained unchanged; this metadata synchronization performs no new proof or TeX compilation.'},'previous_status':previous_status,'adjudication_final_excerpts_checked':32,'stale_adjudication_final_excerpts':[],'adjudication_tsv_modified':False,'protected_fields_unchanged':['changes','doubts','audit_changes','second_boxes','check_events','visual_inspections','root_adjudication','blind_audit'],'page_and_frozen_files_unchanged':True,'new_ink_decisions':False}
allowed={'notes','hand_log','inventory','notation','deletion_insertion_audit','status','metadata_sync'}
assert all(d[k]==before[k] for k in before if k not in allowed)
assert J.read_bytes()==raw and N.read_text()==oldN and H.read_text()==oldH
N.write_text(fullN);H.write_text(fullH);J.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert all(digest(Path(p))==v for p,v in hashes.items())
for path,old in ((N,oldN),(H,oldH)):
 new=path.read_text();om=pat.search(old);nm=pat.search(new)
 assert old[:om.start()]==new[:nm.start()] and old[om.end():]==new[nm.end():]
assert proof in N.read_text()
check=json.loads(J.read_text())
assert all(check[k]==before[k] for k in before if k not in allowed)
assert len(check['inventory'])==31
report=f"""# Scan008 metadata synchronization

Completed: {now}.

Basis: root blind audit applied **2026-11-20 20:16:08 UTC**, with **32 differing boxes and seven changed places**, as recorded in the scan008 decisions and root observations.

## Updated

- Only scan008 sections of **SP115_CW_156-7_notes.md** and **SP115_CW_156-7_hand_log.md**.
- Embedded current notes, hand_log, and inventory descriptions in **scan008_final.json**.
- Inventory **30 → 31**, adding **NB replacement ending te** immediately after the existing NB verb-overwrite element. Every prior element remains in its prior relative order.
- Current status now records completed root adjudication.
- Four initial notation entries and nine initial deletion/insertion-audit entries received explicit current annotations. Original entries and literal C_span quotations are preserved.
- Initial doubt_summary and validation records remain unchanged and are explicitly identified as historical in metadata_sync.

The synchronized descriptions cover final-s uncertainty in facultatif(s), resolved literal des', dfn/defn/def, the partial NB ending correction with live résul/cancelled tentative tera/inserted te, tentative cancelled c'est un and ∃/], resolved inserted soit, and plain surviving F in the first Cor Sup-limit operand. The old X/tilde-X uncertainty remains. C/G choices, the slanted-note wording and state alternatives, spacieux and literal ses are retained.

## Adjudication excerpt check

All **32 adjudication final excerpts** equal the frozen-first excerpt with the completed decisions applied, including explicit box-specific final overrides. **No stale final excerpt was found.** The adjudication TSV was not modified.

## Preserved

The current page, frozen first/second/box TSVs, initial page copy, decisions, root observations and adjudication TSV retain their pre-sync hashes. JSON changes, doubts, audit_changes, second_boxes, proof-check events and all other non-metadata fields are unchanged. Other pages' notes and hand-log sections are byte-for-byte unchanged. The conditional N008-strata proof paragraph is unchanged. No image was reread, no new ink decision was made, and no TeX compilation or proof check was performed.
"""
(R/'review/scan008_metadata_sync.md').write_text(report)
print(json.dumps({'inventory_before':30,'inventory_after':31,'notes':len(check['notes']),'hand_log':len(check['hand_log']),'notation_annotations':sum('current_annotation' in x for x in check['notation']),'deletion_insertion_annotations':sum('current_annotation' in x for x in check['deletion_insertion_audit']),'adjudication_final_excerpts_checked':32,'stale_excerpts':[],'protected_hashes_unchanged':True,'report':'out/review/scan008_metadata_sync.md'},ensure_ascii=False,indent=2))
