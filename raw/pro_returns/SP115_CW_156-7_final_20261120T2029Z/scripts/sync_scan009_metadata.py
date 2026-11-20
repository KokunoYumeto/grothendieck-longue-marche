from pathlib import Path
import copy,csv,datetime,hashlib,json,re
R=Path('/workspace/scratch/ddf8babdc42e/out')
J=R/'review/scan009_final.json';D=R/'second/H156-01_156-7_scan009_decisions.json'
A=R/'second/H156-01_156-7_scan009_adjudication.tsv';O=R/'second/H156-01_156-7_scan009_root_observations.md'
P=R/'pages/H156-01_156-7_scan009.tex';N=R/'SP115_CW_156-7_notes.md';H=R/'SP115_CW_156-7_hand_log.md'
raw=J.read_bytes();d=json.loads(raw);before=copy.deepcopy(d);dec=json.loads(D.read_text())
with A.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
audit={x['box']:x for x in rows}
assert len(rows)==30 and d['blind_audit']['changed_places']==18
for row in rows:
 expected=row['first']
 for p in dec['patches']:expected=expected.replace(p['old'],p['new'])
 expected=dec['boxes'].get(row['box'],{}).get('final',expected)
 assert row['final']==expected,row['box']
 assert r'\LongrightarrowZ' not in row['final']
initial=(R/'second/H156-01_156-7_scan009_initial.tex').read_text();expected=initial
for p in dec['patches']:
 assert expected.count(p['old'])==p.get('count',1)
 expected=expected.replace(p['old'],p['new'])
assert P.read_text()==expected
protected=[P,D,A,O,R/'scripts/decide_blind009.py']+[R/f'second/H156-01_156-7_scan009_{suffix}' for suffix in ('first.tsv','second.tsv','boxes.tsv','initial.tex')]
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
hashes={str(p):digest(p) for p in protected}
pat=re.compile(r'^## Scan\s*009\b.*?(?=^## |\Z)',re.M|re.S)
oldN=N.read_text();oldH=H.read_text();mN=pat.search(oldN);mH=pat.search(oldH);assert mN and mH
paragraphs=mN.group().split('\n\n')
lemma=next(x for x in paragraphs if x.startswith('**N009-compatible-refinement'))
conditional=next(x for x in paragraphs if x.startswith('**N009-margin-conditional'))
old_tail='In particular, the possible primes and raised cross in the actual NB formula are not erased to fit that intended argument (scan009, rotated NB crop).'
assert old_tail in conditional
conditional=conditional.replace(old_tail,r'The completed ink audit now resolves the first X and second Z of the preceding implication as unprimed, retains Y′/Y, and reads the literal raised cross as Z^{+}. The small At beside the later arrow is an unnumbered reference label; no numbered axiom is inferred from it. These source readings do not establish the meaning of the plus or verify the literal marginal proof. The full marginal argument remains unverified beyond the conditional calculation just stated.')
newN=r"""## Scan 009 — manuscript page 8

The author begins `J’explicite, à cause de son importance...`, with the opening sentence left unfinished after **d’autres**. The full opening already contained conséquence. The upper At DC1 draft, its continuation and both corollaries are cancelled. At DC2 is also abandoned, ending after **Alors** without a conclusion. The source has both the larger cancellations and smaller earlier corrections within them. The completed audit retains **X/X′** after avec in the first axiom, retains **Y′/Y** at the end of the old cancelled implication, and removes the supplied closing parenthesis after the inserted i.e. condition: no closing mark is exposed there. The shallow lower editing rule now includes its separate left oblique as well as the right upturn; the small right-pointing head midway under the two At DC2 assumptions remains a distinct graphic.

Cor1 names F,C and writes **F∥C**, then **F≪F** without a prime. The next line uses C′ and G, concluding with F′ and G′. Cor2 similarly has C′ in its refinement and disjointness hypotheses while retaining G′ in its conclusion. Clear open Cs and absent primes remain unchanged even though a uniform F,G formulation would be needed for the intended statements. Before Cor2's old Sup definition, **avec** is now tentatively supplied inside the local cancellation; the whole old formula remains tentative, and the inserted **L=F∩G** is retained.

In the oblique NB, the implication after the two Z hypotheses now has unprimed **X** and unprimed second **Z**, while **Y′/Y** remains uncertain. The later implication bears a small **At** label below/right of its arrow; this is retained without assigning a numbered axiom. The exposed **c'est** precedes the still-doubtful cancelled impossible. The final raised cross is now clearly literal **Z^{+}≤L**. The candidate absurde retains both cancelled and live alternatives. A thin connected upper stroke, right-side near-vertical stroke and lower oblique are reproduced separately as a graphic, without imposing a new cancellation scope on the whole marginal argument (blind B007).

"""+lemma+'\n\n'+conditional+r"""

The live heading is **Propriété1**, not Proposition1. It proposes comparing compatibility of refinements globally and after restriction to the intersection. The reference **cf GF VI, p.73/13 — On a en tous cas tjrs...** is live; the separate lower **Montrons** row is struck. VI is barred above and below. The reference is not pursued beyond this extract. The next sentence calls the property equivalent, in general form, to the former At12.

The replacement axiom's surviving label is now resolved as **DD**, without inventing a readable prior state. It retains inserted **ou bien** and a resolved **ampersand** between the two variable pairs. It defines **K=X∩Y** but concludes using **L** subscripts. That K/L mismatch is retained; a common symbol would be needed if those restrictions are intended to be to the just-defined intersection. Its parenthesis says **l’inverse**, with a single tentative cancelled **est** before **tjrs vrai**; C’s extra live est is absent. The assertion that the converse always holds is reported and remains independently unverified.

The slanted note calls this a **Critère de compatibilité pour les raffinements de sous-figures**, then says **Mais c’est faux dans le cas simplicial, ex :**. Its drawing has four skew sides, a slightly open oval, one diagonal, two thick points and three crosses. These are graphical crosses rather than the letter labels C proposed. The large lower double arrow belongs to the following marginal implication and is not duplicated in the drawing. The conclusion sign consists of two uprights crossed twice and is reproduced directly. The note uses **contre-exple**, a first **At ∥/11** label that remains uncertain, and later explicit **At11**, with a reference to GF VI, p.67,68. The references and the full interpretation of the drawn counterexample have not been externally researched or independently proved.

Both final headings retain **Cor. Main/Corollaire** under the same underline, with their separate numerals 1 and 2 outside it. The first continues with the article **la/le** and the quoted propriété ci dessus. The implication formula remains beside the second label. **Plus gén.** introduces the last equivalence. Both lower refinement hypotheses again have literal **C′≪G** where their conclusions use G′. Those claims remain reported, not newly proved by the ink audit. The page carries the manuscript number 8 and no date.

"""
newH=r"""## Scan009 additions

- Flat, open C/C′ forms contrast locally with returned G/G′ forms. Clear Cs in upper Cor1/2 and both lower hypotheses are retained; the bound variable expected by the surrounding mathematics never supplies a missing internal stroke. Not every open bowl is automatically C.
- A dark dot above the first Cor2 L belongs to the comma on the preceding line. In the NB implication after the two Z hypotheses, the first X and second Z are now resolved as unprimed; nearby marks belong to commas or the row above. The following Y′/Y remains doubtful. After avec in the first AtDC1 row, X/X′ remains uncertain; the old cancelled implication ends with Y′/Y.
- The small At below/right of an NB implication has a triangular A and crossed t. It is an unnumbered reference label. The exposed c'est before the cancelled impossible is retained. The final cross is raised above Z and is transcribed literally as Z^{+}; its mathematical meaning is not supplied from expectation.
- The NB's thin upper, right-side and lower-oblique strokes form a connected configuration. They are represented as a graphic without newly cancelling the entire note. The retraced absurde retains both deletion and live-state alternatives.
- No closing parenthesis is exposed after the inserted i.e. condition's final Y; the separate rising oblique belongs to cancellation. The supplied closing parenthesis has been removed.
- The low cursive remnants before Cor2's old Sup formula support only tentative cancelled avec. Hatching continues to obscure the whole old formula; the inserted L=F∩G remains a separate layer.
- The two surviving retraced heading letters have closed bowls and uprights, resolving DD. The separator between the variable pairs is a loop with crossing return and terminal stroke, resolving an ampersand. Inserted ou bien remains distinct from the baseline.
- Both lower heading forms retain Cor. Main/Corollaire rather than a certain segmentation. Their numerals remain outside the underlines. The following first-heading article remains la/le; agreement with propriété does not decide its ink.
- Two short arms meet in a right-pointing arrowhead near the middle of the shallow curved connector under the AtDC2 assumptions. The separate lower editing rule has a left rising oblique and right upturn without an arrowhead. The drawing contains three crosses, two filled points and small open gaps; neither letter labels nor closed gaps are supplied from geometric expectations.
- The lower crossed relation has two uprights and two transverse bars. It is kept as explicit strokes without importing a standard named relation. The first At label beside it admits parallel/11, while the later At11 remains separate and clear.

"""
fullN=oldN[:mN.start()]+newN+oldN[mN.end():];fullH=oldH[:mH.start()]+newH+oldH[mH.end():]
source='out/second/H156-01_156-7_scan009_decisions.json and H156-01_156-7_scan009_root_observations.md; root blind audit completed 2026-11-20 20:24:42 UTC'
notes={x['id']:x for x in d['notes']}
notes['009-N2']['source']=source+'; B008, B009, B027, B030, B031'
notes['009-N5'].update(claim='The initial reader performed visual checks only; the previously recorded root checks establish two limited conditional statements, not the literal marginal proof or the page’s other assertions.',source='Existing notes and CHECK_EVENTS; '+source,reasoning_if_any='The ink audit makes no new proof check. Literal Z^{+} is now clear, and At beside the arrow is an unnumbered label. The raised plus is not erased or interpreted to force the conditional proof; the meet/refinement premise and full marginal argument remain unverified.')
notes['009-N6'].update(claim='The small source-shaped rules, mid-stroke arrow and connected NB strokes are retained as graphics.',source=source+'; B007, B012, B015, B016',reasoning_if_any='The AtDC2 editing rule includes a separate left oblique and right upturn; the assumption connector has a mid-stroke right-pointing head. The three thin connected NB strokes do not impose a new whole-note cancellation.')
d['notes'] += [
 {'id':'009-N7','claim':r"The NB now has unprimed X and second Z in the implication, remaining Y'/Y doubt, a small At arrow label, c'est, literal Z^{+}≤L, and deletion/live uncertainty on absurde.",'source':source+'; B007','reasoning_if_any':'These are source readings only. The label is not expanded to a numbered axiom and the raised plus is not given an unverified mathematical meaning.'},
 {'id':'009-N8','claim':'The upper AtDC1 retains X/X′ after avec and Y′/Y in the old implication; the inserted condition has no supplied closing parenthesis. Cor2 has tentative cancelled avec before its tentative old supremum formula.','source':source+'; B003, B004, B006, B009, B010','reasoning_if_any':'All local revisions remain within their pre-existing global cancellations; the cancelled old formula is not resolved by mathematical expectation.'},
 {'id':'009-N9','claim':'The surviving live axiom label DD and variable-pair ampersand are resolved; inserted ou bien and the literal K/L mismatch are retained.','source':source+'; B025–B027','reasoning_if_any':'No earlier heading state is invented, and no common restriction symbol is supplied to repair the source.'},
 {'id':'009-N10','claim':'The first lower marginal At label retains parallel/11. Both lower corollary headings retain Cor. Main/Corollaire, and the first following article retains la/le.','source':source+'; B024, B029, B030','reasoning_if_any':'The later explicit At11 and source placement/underlining remain. Widening alternatives does not erase distinct pre-existing witness disagreements.'},
 {'id':'009-N11','claim':'Root blind audit is complete: 30 differing boxes, 18 changed physical places, with overlapping changes deduplicated.','source':source,'reasoning_if_any':'The metadata synchronization makes no new ink judgment. The separately authorized separator and enumerated-kind repairs are non-ink changes and do not change K.'}
]
h=d['hand_log']
h[1]['place']='Cor2 first L and NB implication after the two Z hypotheses'
h[1]['observation']='The apparent prime over Cor2 L belongs to the upper row’s comma. The NB first X and second Z have no independent raised ticks and are now unprimed; the remaining Y′/Y doubt is retained. AtDC1 after avec retains X/X′, and the old cancelled implication retains Y′/Y.'
h[5]['observation']='Local replacement words and formulas remain inside the later global cancellation. The NB’s thin connected upper/right/lower-oblique strokes are a separately reproduced graphic, not a new global cancellation of that note. The local absurde has deletion/live uncertainty.'
h += [
 {'habit':'Raised cross distinct from a baseline continuation','place':'NB final Z-plus expression; B007','observation':'The cross is raised above Z and followed by ≤L, so the literal form is Z^{+}≤L. No mathematical meaning is inferred for the superscript.'},
 {'habit':'Small arrow reference and short prose survive beside crowded corrections','place':'NB At label and c’est; B007','observation':'The triangular A and crossed t sit below/right of the implication arrow; no numeral is present. Exposed c, joined est and its ascender support c’est before the still-doubtful cancelled impossible.'},
 {'habit':'Retouched heading and variable separator retain distinct shapes','place':'live At DD1; B025','observation':'Closed bowls and uprights settle surviving DD, while the loop/crossing return/terminal stroke settle the ampersand. The earlier state of the heading is not invented.'},
 {'habit':'Compact lower headings and article retain alternatives','place':'both lower corollaries; B029 and B030','observation':'The tall linked strokes and low humps admit Cor. Main/Corollaire under the same underline. Separate numerals stay outside; the first small following article retains la/le.'},
 {'habit':'A source rule can have a separate oblique component','place':'AtDC2 lower editing rule; B012 and B016','observation':'The exposed left oblique is retained alongside the shallow lower stroke and right upturn. The existing mid-stroke headed assumption connector remains distinct.'},
 {'habit':'Unheaded paired strokes can leave sign/digit ambiguity','place':'first At label in lower marginal continuation; B024','observation':'The first pair admits parallel/11. The later explicit At11 is retained separately rather than deciding the first pair by reference consistency.'}
]
inv=d['inventory'];assert len(inv)==40
items={x['element']:x for x in inv}
items['First cancelled axiom']['first_words_or_objects']='At DC 1 : Soient X,Y; after avec, X/X′ remains uncertain'
items['Added first-axiom condition']['first_words_or_objects']='avec X′∥X∩Y=L; (i.e. X′∥Z pour Z≤X,Y; no closing parenthesis supplied'
items['Oblique NB proof']['first_words_or_objects']='NB La chose importante est; unprimed first X and second Z, Y′/Y doubt; At arrow label; c’est; literal Z^{+}≤L'
pos=next(i for i,x in enumerate(inv) if x['element']=='Oblique NB proof')+1
inv.insert(pos,{'element':'NB connected thin-stroke graphic','kind':'drawing','position':'crossing/bordering the oblique NB, original region x≈22–456 y≈622–1467','first_words_or_objects':'connected long upper stroke, right near-vertical stroke and lower oblique; no added whole-note cancellation'})
items['Cancelled old supremum definition']['first_words_or_objects']='tentative cancelled avec, followed by wholly tentative L=Sup Z'
items['Second cancelled axiom']['first_words_or_objects']='At DC 2 (Axiome des ateliers spacieux/spécieux)'
items['Lower editing boundary']['first_words_or_objects']='long shallow stroke, separate rising left oblique and rising right end'
items['Live reference and implication remark']['first_words_or_objects']='cf GF VI, p.73/13 — On a en tous cas tjrs'
items['Counterexample continuation']['first_words_or_objects']='Mais on aura X′_L∥Y′_L; first At parallel/11 uncertain; later At11'
items['Live replacement axiom']['first_words_or_objects']='At DD 1 Soient; resolved DD and ampersand; literal K definition and L subscripts'
items['First live corollary']['first_words_or_objects']='Cor. Main/Corollaire 1 la/le “propriété” ci dessus'
items['Second live corollary']['first_words_or_objects']='Cor. Main/Corollaire 2 F∥G, F′≪F, C′≪G ⇒ F′∥G′'
items['Earlier AtDC1 implication']['first_words_or_objects']='Y′≪Y ⇒ X′∥Y′/Y; final old prime uncertain'
items['NB cancelled impossibility word']['first_words_or_objects']='c’est followed by cancelled tentative impossible'
old_name='NB cancelled contradiction word';new_name='NB contradiction word (deletion/live uncertain)'
items[old_name].update(element=new_name,kind='text',position='before final car; local cancellation state uncertain',first_words_or_objects='absurde; both cancelled and live alternatives retained')
assert len(inv)==41
normalized=[old_name if x['element']==new_name else x['element'] for x in inv if x['element']!='NB connected thin-stroke graphic']
assert normalized==[x['element'] for x in before['inventory']]
def annotate(row,fields,reading,note,boxes):
 row['current_annotation']={'status':'initial metadata retained; current adjudication supersedes or clarifies specified fields','superseded_or_clarified_fields':fields,'current_reading':reading,'observation':note,'source':source+'; '+boxes}
annotate(d['notation'][3],['form'],r'\unsure{\phi|\varnothing} at first occurrence; \phi at final occurrence','The initial varphi form is historical. Current root mapping uses phi, retaining the first local phi/varnothing shape doubt. The source-shaped oval is not reinterpreted by this synchronization.','B007; root_adjudication')
di={x['place']:x for x in d['deletion_insertion_audit']}
specs=[
 ('At DC 1 whole first statement',audit['B003']['final'],'Global deletion is retained; X/X′ after avec is now explicit. The C_span is the historical witness quote.','B003'),
 ('At DC 1 continuation whole',audit['B004']['final'],'Retain global and local states, final old Y′/Y doubt, and the condition without a supplied closing parenthesis.','B004, B006'),
 ('At DC 1 old Y′ formula',r"\deleted{$Y'\ll Y\Longrightarrow X'\parallel\unsure{Y'|Y}$}",'The old X′ tick is retained; the final old Y prime is uncertain.','B004, B006'),
 ('NB impossible',r"c'est \deleted{\unsure{impossible}}",'The struck impossible remains tentative; the separately exposed preceding c’est is present in the current note.','B007'),
 ('NB absurde',r'\unsure{\deleted{absurde}|absurde}','The initial categorical deletion claim is superseded by explicit cancelled/live-state alternatives.','B007'),
 ('Cor 1 whole',audit['B008']['final'],'The outer deletion is retained. Current literal F,C and F∥C, and unprimed F≪F, supersede differing letters in the historical C quote.','B008'),
 ('Cor 2 whole',audit['B009']['final'],'Retain global and local cancellation, tentative cancelled avec before the old formula, inserted L=F∩G, and literal C′ hypotheses.','B009, B010, B011'),
 ('Cor 2 old Sup expression',audit['B010']['final'],'The whole old formula remains tentative, with additional tentative cancelled avec before it. The isolated current excerpt includes the global cancellation layer.','B010'),
 ('At DC 2 whole',audit['B012']['final'],'The whole draft remains cancelled. Current metadata retains spacieux/spécieux, resolved tt, old L doubt and the headed connector rather than the C quote’s simple underline. Its separate lower editing rule now also has a left oblique.','B012–B016'),
 ('At DC 1 added avec/i.e. condition',r"\inserted{avec $X'\parallel X\cap Y=L$, (i.e. $X'\parallel Z$ pour $Z\leq X,Y$}",'The initial evidence claim that both parentheses remain is superseded: no closing parenthesis is exposed after the final Y. The insertion and enclosing cancellation remain.','B004, B006')
]
for place,reading,note,boxes in specs:annotate(di[place],['decision','evidence'],reading,note,boxes)
previous=d['status'];d['status']='root adjudication after blind second reading complete; metadata synchronized'
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['metadata_sync']={'completed_utc':now,'basis':source,'inventory_before':40,'inventory_after':41,'inserted_inventory_element':'NB connected thin-stroke graphic','renamed_existing_inventory_element':{'old':old_name,'new':new_name,'reason':'Describe retained deletion/live uncertainty without asserting categorical cancellation.'},'original_inventory_order_preserved':True,'adjudication_final_excerpts_checked':30,'stale_adjudication_final_excerpts':[],'previous_status':previous,'current_page_sha256':hashes[str(P)],'page_equals_frozen_initial_plus_recorded_patches':True,'syntax_schema_repair_record':'review/scan009_syntax_schema_repair.json','protected_fields_unchanged_in_metadata_sync':['changes','doubts','audit_changes','second_boxes','check_events','root_adjudication','blind_audit'],'new_ink_decisions':False,'new_proof_checks':False,'K_changed':False}
allowed={'notes','hand_log','inventory','notation','deletion_insertion_audit','status','metadata_sync'}
assert all(d[k]==before[k] for k in before if k not in allowed)
assert J.read_bytes()==raw and N.read_text()==oldN and H.read_text()==oldH
N.write_text(fullN);H.write_text(fullH);J.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert all(digest(Path(p))==v for p,v in hashes.items())
for path,old in ((N,oldN),(H,oldH)):
 new=path.read_text();om=pat.search(old);nm=pat.search(new)
 assert old[:om.start()]==new[:nm.start()] and old[om.end():]==new[nm.end():]
assert lemma in N.read_text()
check=json.loads(J.read_text());assert all(check[k]==before[k] for k in before if k not in allowed)
report=f"""# Scan009 metadata synchronization

Completed: {now}. Basis: root blind audit applied **2026-11-20 20:24:42 UTC**, **30 differing boxes**, **18 changed physical places**.

## Synchronized metadata

Only scan009 sections of the current notes and hand log were updated. Embedded notes, hand_log and inventory descriptions now reflect the completed decisions. Inventory is **40 → 41**, adding the **NB connected thin-stroke graphic** after the existing marginal NB element. All original elements retain their relative order. The existing absurde element is labelled **NB contradiction word (deletion/live uncertain)** and classed as text with explicit state alternatives.

The descriptions cover X/X′ after avec; old cancelled Y′/Y; removal of the unsupported inserted-condition closing parenthesis; unprimed NB first X and second Z with remaining Y′/Y doubt; the unnumbered At arrow label and c’est; clear literal Z^+; absurde state uncertainty; the three connected NB strokes; tentative cancelled avec before Cor2’s old formula; the lower editing rule’s left oblique; At parallel/11; resolved DD and ampersand; both Cor. Main/Corollaire headings and la/le.

One initial notation entry and ten initial deletion/insertion-audit entries now have explicit current annotations, preserving their historical fields and C_span quotes. Status records completed blind adjudication.

The literal K/L discrepancy is retained. Existing conditional proof reasoning remains limited to its stated premises: the full marginal proof, the meaning of Z^+, the converse claim and the counterexample remain unverified. The small At is an unnumbered reference label. No new mathematical check event was added.

## Final-excerpt consistency

All **30 adjudication final excerpts** match the recorded decisions and explicit overrides after the separately authorized separator repair. **No stale reading excerpt remains.** The current page equals the frozen initial page with the current recorded patch sequence applied.

Page SHA256: **{hashes[str(P)]}**

Final review JSON SHA256 after metadata synchronization: **{digest(J)}**

## Exact non-ink repairs and preservation

The authorized syntax/schema correction is documented in **scan009_syntax_schema_repair.json** and progress.log: the joined Longrightarrow-Z token was separated consistently in the page, B007 final excerpt, decision override and embedded audit final; the replacement patch/script literal now begins with a space. Kinds for 009-87 and 009-88 are omission in the review, decisions and script. No apply rerun occurred and K remains 18.

After those explicitly authorized repairs, this metadata synchronization leaves the page, decisions, adjudication TSV, script, changes, doubts, audit_changes, frozen files and check_events unchanged. Other pages’ notes and hand-log sections remain byte-for-byte unchanged. No image was viewed, no ink judgment made and no TeX compilation performed.
"""
(R/'review/scan009_metadata_sync.md').write_text(report)
with (R/'progress.log').open('a') as f:f.write('scan009 metadata sync '+now+': notes/hand log and embedded metadata current; inventory 40->41; all30 adjudication finals verified, no stale excerpts; no new ink or proof checks, K remains18. Page SHA256 '+hashes[str(P)]+'. Report review/scan009_metadata_sync.md\n')
print(json.dumps({'inventory':len(check['inventory']),'notes':len(check['notes']),'hand_log':len(check['hand_log']),'notation_annotations':sum('current_annotation' in x for x in check['notation']),'deletion_insertion_annotations':sum('current_annotation' in x for x in check['deletion_insertion_audit']),'final_excerpts_verified':30,'stale':[],'page_sha256':hashes[str(P)],'review_sha256':digest(J),'protected_unchanged':True},ensure_ascii=False,indent=2))
