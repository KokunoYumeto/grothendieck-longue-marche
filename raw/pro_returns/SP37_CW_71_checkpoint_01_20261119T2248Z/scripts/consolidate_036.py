from pathlib import Path
from datetime import datetime,timezone
import json,copy
root=Path(__file__).resolve().parents[1];base=root/'readers/scan036'
reports={w:json.loads((base/w/'report.json').read_text()) for w in ['R1','R2','R3']}
r2=reports['R2'];byid={x['id']:x for x in r2['issues']}
text=(base/'R2/reading.tex').read_text()
text=text.replace(r'\unsure{côtés|cotés}',r'\unsure{cotés|côtés}').replace(r'\unsure{la|le}',r'\unsure{le|la}')
old=r'\draw (m.center) ellipse[x radius=.87cm,y radius=.47cm];'
new=r'\draw (m.center) ellipse[x radius=1.40cm,y radius=.50cm];\draw (-1.02,.72)--(-1.52,-.08);\draw (-1.40,.10)--(-1.34,-.25);'
assert old in text;text=text.replace(old,new)
text=text.replace('% The initial mark in the circled annotation has a long shaft and a compact upturned right end.','% The initial mark has a long shaft and upturned right end; the separate forked oblique stroke beside the oval is also drawn.')
(root/'pages/J71-05_71_scan036.tex').write_text(text)
selected=[f'R2-CD{i:02d}' for i in range(10,25)]+['R2-30','R2-31','R2-33']+[f'R2-H{i:02d}' for i in range(1,8)]
issues=[copy.deepcopy(byid[x]) for x in selected]
lookup={x['id']:x for x in issues}
change_C={10,12,13,14,15,16,18,19,21,22,23,24}
change_H={11,12,13,16,18,21,22,23,24}
for i in range(10,25):
    x=lookup[f'R2-CD{i:02d}'];x['against_C']=i in change_C;x['against_H']=i in change_H
    x['id']=f'036-D{i:02d}'
    x['image']=x.get('image','').replace(str(root)+'/','')
    x['evidence']+=' The main reader inspected the cited crop (or the corresponding crop listed in main_crop_audit) and accepts this decision.'
    x['readers']={w:x['reading'] for w in reports}
lookup['R2-CD10']['image']='readers/scan036/R1/tout.png'
lookup['R2-CD12'].update(reading=r'\unsure{cotés|côtés}',evidence='The final acute is separate. Above o there is no separately recoverable circumflex: the long stroke merges into the t crossbar. The main reader prefers the unaccented-o candidate while retaining the circumflex alternative.',readers={'R1':r'\unsure{côtés|cotés}','R2':r'\unsure{côtés|cotés}','R3':r'\unsure{cotés|côtés}'})
lookup['R2-CD15'].update(readers={'R1':r'\inserted{\unsure{adjacents}}','R2':r'\inserted{adjacents}','R3':r'\inserted{adjacents}'},evidence='Above struck consecutifs the a/d/j group, connected a/c/e/n run and final t/s are recoverable as adjacents. The main reader accepts the unmarked reading, retaining the cancellation and insertion. H omits this correction within omission block H06; it is not counted twice.')
lookup['R2-CD17']['H']='Not transcribed; included in H06 main-text omission.'
lookup['R2-CD20']['readers']={w:r'\deleted{\illegible{2}}!' for w in reports}
lookup['R2-CD21'].update(readers={'R1':'intact subset plus a separate leader with arrowhead','R2':'intact subset plus a separate diagonal with hooked lower end','R3':'intact subset plus a separate slash with lower fork'},evidence='The diagonal is separated from the open inclusion by a white gap, crosses the underline to its left, and has a small bent branch below it. The main reader chooses a direct drawing of this geometry without assigning the mark a mathematical negation or a definite editorial function.',consequential='The second-case inclusion is not transcribed as a negated inclusion. A detached slanted annotation is drawn beside it.')
lookup['R2-CD22'].update(readers={'R1':r'est|\rightarrow|mais','R2':r'\longrightarrow|est','R3':'est|mais'},evidence='The first mark consists of a long nearly horizontal shaft with a small left upstroke and a compact raised right end. The main reader prefers an arrow, retaining compressed est; there are no distinct m/a/i/s bodies to justify mais. The following non vide? is clear.')
lookup['R2-CD23'].update(image='readers/scan036/R1/final_note.png',readers={'R1':r'et tu \unsure{as au|auras|as un} lemme VIII','R2':r'et \unsure{tu as au lemme|tu as un lemme|tu auras lemme} VIII','R3':r'et \unsure{tu as au lemme|tu as un lemme|tu auras lemme} VIII'},evidence='Et, the crossed t-like group, and lemme VIII are visible. The two low groups between tu and lemme are not separable with confidence. The main reader accepts as au first and retains as un and auras. No grammatical reconstruction is substituted.')
lookup['R2-CD24'].update(reading=r'\unsure{le|la}',readers={'R1':r'\unsure{la|le}','R2':r'\unsure{la|le}','R3':r'\unsure{le|la}'},evidence='The article has a high l loop and a short open ending; that ending resembles e more closely than a closed a, but does not settle it. The main reader follows le first, retaining la.')
lookup['R2-CD11']['S']='SA01-K71-01: confirms that the unqualified claim fails for n=3; S’s n≥4 is a mathematical refinement, not literal replacement text. The overwritten sign remains >|≥ in the diplomatic transcription.'
lookup['R2-CD11']['consequential']='The overwritten n >|≥ 3 condition remains uncertain; the triangle objection is confirmed mathematically in the notes, without replacing the ink by n≥4.'
for oldid,path in [('R2-30','main_ambigu.jpg'),('R2-31','main_lemme_X.jpg'),('R2-33','main_faux_leader.jpg')]:
    x=lookup[oldid];x['id']='036-'+oldid[3:];x['image']='crops/scan036/'+path
    x['readers']={w:x['reading'] for w in reports}
lookup['R2-33']['readers']={'R1':'leader drawn in TikZ','R2':'leader drawn in TikZ','R3':'leader described in comment, not drawn'}
lookup['R2-33']['evidence']='A pale curved stroke turns down from beneath the underlined faux and runs right toward the pencil explanation. The main reader chooses to draw it, since a LaTeX comment does not reproduce the visible connecting mark. H also omits the graphic and the underline state.'
for i in range(1,8):
    x=lookup[f'R2-H{i:02d}'];x['id']=f'036-H{i:02d}';x['image']=f'crops/scan036/main_H{i:02d}.jpg'
    x['readers']={w:'complete main-text block, agreeing except for separately logged local decisions' for w in reports}
    x['C']='Complete corresponding paragraph in C; local differences are logged separately.'
    x['reading']=x['reading'].replace('reading.tex','pages/J71-05_71_scan036.tex')
    x['evidence']='The main reader personally inspected this paragraph crop. The coherent main-ink block is present, including the formulas and cancellations recorded in the consolidated page. H supplies a summary and isolated quotation anchors rather than the complete block. The three independent readers agree on the rest of its text.'
issues.append({'id':'036-H08','place':'Literal quotation anchor in H: propriété énoncée','C':'ennoncée','H':'énoncée','reading':'ennoncée','evidence':'The proof crop has an unaccented initial e followed by a doubled n run before o; the later é is accented. This agrees with all three readers and C. The H anchor normalizes the spelling.','image':'crops/scan036/main_H06.jpg','confidence':'high','against_C':False,'against_H':True,'kind':'abbreviation expanded or spelling modernised','H_marked':'no','readers':{w:'ennoncée' for w in reports}})
issues.append({'id':'036-D25','place':'Oblique forked stroke outside the circled non vide? note','C':'Oval only; the external stroke is not drawn','H':'Circle mentioned, external stroke absent','reading':'Oval with a long oblique stroke and short bent branch on its left, drawn in TikZ','evidence':'The crop shows a separate dark diagonal beside the left edge of the lighter oval, extending from above it down-left, with a short bent branch near its lower end. The main reader adds this visible graphic without interpreting its function.','image':'readers/scan036/R2/09_circled_note.jpg','confidence':'high','against_C':True,'against_H':True,'kind':'drawing or diagram','H_marked':'no','readers':{'R1':'external slanted stroke included','R2':'oval only','R3':'oval only'}})
inventory=copy.deepcopy(r2['inventory'])
for x in inventory:
    x['sheet_kind']='text'
    x['hand']=x['hand'].replace('unnamed fair-copy hand','another unnamed hand')
    x['first_words_or_objects']=x['first_words_or_objects'].replace('côtés|cotés','cotés|côtés').replace('la|le','le|la')
inventory.append({'sheet_kind':'text','hand':'another unnamed hand (dark annotation)','element':'Forked oblique stroke beside lower-left oval','kind':'drawing','position':'left of circled non vide?','first_words_or_objects':'detached slanted stroke with bent branch','transcribed':'yes'})
doubts=copy.deepcopy(r2['doubts'])
for d in doubts:
    if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
    if d['place']=='side-count noun':d['reading']='cotés';d['alternatives']='côtés'
    if d['place']=='article before dém in pencil note':d['reading']='le';d['alternatives']='la'
notes='''**N036.1 — What the page does.** Manuscript IX finishes an angular argument for the preceding lemma: the exterior sector exceeds π and the interior sector is below π; the convex hull supplies at least three vertices. It states Lemme XI (two vertices visible through the interior) and begins a proof with the triangle on a vertex and its two neighbors. These are reports of the page’s claims, not an independent verification of the entire proof.

**N036.2 — Mathematics and reading decisions.** The crossed-loop sign in the intersection equations is phi-shaped in the ink. Its use indicates the empty-set role, but the transcription keeps `\\phi|\\varnothing` at the first occurrence and the visible first candidate subsequently. The second-case inclusion is intact; a detached diagonal with a lower hook is drawn beside it. A bare containment does not imply nonemptiness (the empty set is a counterexample), consistent with the circled `non vide?`; this is a check of that local logical implication only. The original Lemma XI wording fails for a triangle: every pair of distinct vertices is joined by a boundary edge, so its open segment is not in the interior. This confirms the diagnosis in S, SA01-K71-01. S’s condition n≥4 is not substituted for the overwritten `n >|≥ 3` in the scan; sufficiency for all larger polygons is not independently proved here.

**N036.3 — The page’s objections and slips.** The annotations read `faux pour n=3!`; `OPS Γ non convexe (sinon c’est clair grâce à --)`; underlined `lemme X`; `ambigu` beside `triangle`; underlined `faux`; `il faut prendre s comme dans le|la dém du lemme VIII (pas son énoncé!)`; a cancelled two-word note that remains unreadable; `→|est non vide?`; and `dire avant! (et tu as au lemme|tu as un lemme|tu auras lemme VIII)`. The first proof reference really has VIII despite the marginal correction to X. The main text’s `et et`, `mésure`, `ennoncée`, and missing accents are kept. No inference is made from what the referred lemmas should contain.

**N036.4 — Pagination and material.** Manuscript number IX, ruled above and below, appears at upper right; archive sheet number 35 is a comment only. Lemme XI is the heading. There is no date or total page count. Main fair-copy ink, darker corrections and pale pencil-like annotations are distinguished, but no named author is assigned from these strokes alone.'''
now=datetime.now(timezone.utc).isoformat();who='GPT-6 Astra Pro; inherited effort not exposed; root SP37_CW_71'
events=[e for e in r2['check_events'] if e['type']=='targeted proof check']+[e for e in reports['R3'].get('check_events',[]) if e['type']=='targeted proof check']
events += [
{'statement_id':'N036.1; manuscript upper argument and Lemma XI','date':now,'who':who,'type':'carried as background without fault found','outcome':'Reported as manuscript content after visual collation; no full proof verification is asserted.'},
{'statement_id':'N036.2; Lemma XI at n=3; S SA01-K71-01','date':now,'who':who,'type':'targeted proof check','outcome':'A triangle has only adjacent vertex pairs; their open connecting segments lie on boundary edges, not in the interior. The n=3 objection is valid. The literal overwritten inequality remains uncertain; no proof of the n≥4 statement is claimed.'},
{'statement_id':'N036.2; second-case inference from containment to existence','date':now,'who':who,'type':'targeted proof check','outcome':'Checked the bare implication: A⊂B allows A=∅. Nonemptiness must be supplied separately. This does not refute the full geometric setting.'},
{'statement_id':'N036.3 and N036.4; annotations, spellings and pagination','date':now,'who':who,'type':'carried as background without fault found','outcome':'Documentary statements grounded in the scan and independent inventories; author objections are reported, not assumed to establish the truth or falsity of the whole argument.'}]
record={'scan':36,'folder':'J71-05','page_file':'J71-05_71_scan036.tex','overview':'Three independent readings compared. The main reader personally inspected the disputed and H-omitted places on crops. Certainty changes are counted; retained doubts are separately visible.','issues':issues,'inventory':inventory,'doubts':doubts,'abbreviations':[{'form':'def.','meaning':'définition'},{'form':'OPS','meaning':'on peut supposer (probable)'},{'form':'dém','meaning':'démonstration'},{'form':'ext','meaning':'extérieur'},{'form':'int','meaning':'intérieur'}],'notes':notes,'check_events':events,'brief':'brief_v01.md','main_crop_audit':['readers/scan036/R1/tout.png','readers/scan036/R2/01_side_count.jpg','readers/scan036/R2/02_grace.jpg','readers/scan036/R2/03_numeral.jpg','readers/scan036/R2/04_adjacents.jpg','readers/scan036/R2/05_phi.jpg','readers/scan036/R2/06_overwritten_int.jpg','readers/scan036/R2/07_faux_note.jpg','readers/scan036/R2/08_deleted_note.jpg','readers/scan036/R2/09_circled_note.jpg','readers/scan036/R2/10_relation.jpg','readers/scan036/R1/final_note.png']+[f'crops/scan036/main_H{i:02d}.jpg' for i in range(1,8)]+['crops/scan036/main_ambigu.jpg','crops/scan036/main_lemme_X.jpg','crops/scan036/main_faux_leader.jpg'],'audit_recorded_utc':now}
(root/'decisions/scan036.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print('Consolidated scan036:',len(issues),'decision rows;',len(inventory),'inventory elements')
