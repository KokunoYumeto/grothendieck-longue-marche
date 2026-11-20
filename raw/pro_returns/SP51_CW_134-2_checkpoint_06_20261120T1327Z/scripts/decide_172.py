from decision_helpers import *
import copy
r=load_reports(172)
diffs=[]
# Each quoted expression is a separate place; equivalent dash and doubt syntax is excluded.
for i in [0,1]:diffs.append(row(r,'A',i))
diffs[1]['crop']='crops/scan172/main/01_fleur_phrase.jpg'
diffs.append(row(r,'C',2,crop='crops/scan172/main/02_type_quotes.jpg'))
diffs.append(row(r,'A',3,crop='crops/scan172/main/03_developpement.jpg'))
diffs.append(row(r,'A',4,crop='crops/scan172/B/l07_added_ens_modules.png'))
diffs.append(row(r,'A',5,crop='crops/scan172/B/l07_added_ens_modules.png',consequential='Restores the specified sheaf coefficients, sets or modules, left unread in H; the qualification attaches to faisceaux.'))
for i in [7,8]:diffs.append(row(r,'A',i))
diffs.append(row(r,'B',11,evidence='The first glyph has a closed horizontal oval directly joined to one descender and its returning shoulder; no separate p body follows it. A distinct c precedes the tall t. Read qct, with a point after qu and no intervening hyphen. The qct/cpct/cpt doubt is resolved.'))
diffs.append(row(r,'B',12))
point=row(r,'C',12,final='isolated point drawn below/right of the union index; no assigned mathematical role',kind='drawing or diagram',confidence='low',evidence='A compact dark point stands to the right of the index I, separate from its lower bar and the dotted subscript i of X_i. Its presence is clear, but its origin is not. Reproduce its location as a nontext mark without introducing a factor or an index.')
diffs.append(point)
for word,where in [('cellules','L16 main line'),('strates','L16 addition')]:
 diffs.append(row(r,'A',2,place=where+', quotation glyphs',C='``'+word+"''",H='« '+word+' »',final='``'+word+"''",crop='crops/scan172/main/04_cellules_strates_quotes.jpg',evidence='Paired short high strokes open and close '+word+'; they do not form angular guillemets.'))
for i in [10,11,12,13]:
 d=row(r,'A',i)
 if i in [11,12,13]:d['crop']='crops/scan172/B/l18_loc_constant_cancelled.png'
 diffs.append(d)
diffs.append(row(r,'A',14,crop='crops/scan172/main/05_after_finitude.jpg'))
diffs.append(row(r,'A',15,final='X . (qui',differs_C=True,confidence='high',evidence='The compact dark point between X and the parenthesis is clearly detached and comparable in weight to deliberate points. Transcribe the physical point without a reading doubt; this does not infer a grammatical sentence boundary or repair the unusual punctuation.'))
diffs.append(row(r,'A',16))
diffs.append(row(r,'B',21,crop='crops/scan172/B/l22_apparait.png',confidence='medium',evidence='The long paired descending initial group and following a-r-a-i-t strokes support apparait, not peut. The short curved raised stroke resembles the ordinary handwritten i mark more than a two-sided roof, so apparait is first; a reduced circumflex cannot be excluded.'))
diffs.append(row(r,'B',22,crop='crops/scan172/B/l23_elle_glyph.png',evidence='The lower stroke turns up at the left and has a second small hump before its long exit; a separate bar lies above it. This is a barred m, not two plain parallel strokes. The full word même is not written.'))
diffs.append(row(r,'A',19,crop='crops/scan172/B/l23_elle_glyph.png'))
comparisons=[
 {'place':'L7 addition, after ens','A':"d’ens,",'B':"d’ens,",'C':"d’ens.,",'decision':'Select A/B: a descending comma follows ens, with no separate abbreviation stop before it (B/l07_added_ens_modules.png). etc likewise has no final point.'},
 {'place':'L9–10 modulo separators','A':'--','B':'-','C':'-','decision':'The same horizontal manuscript punctuation is meant in all returns. Keep C’s short-hyphen encoding; exclude the difference from collation and counts as typesetting only.'},
 {'place':'L13 first abbreviated condition','A':r'\unsure{qct|cpct}','B':'qct','C':'qct','decision':'Select B/C: the closed oval is directly joined to the descender; no separate p body is present, and c then t remain distinct (B/l13_abbreviations.png).'},
 {'place':'L15 point by union index','A':'not separately inventoried','B':'lowered point, origin uncertain','C':'lowered point, origin uncertain','decision':'Include the compact point seen in C/13_union_indices.png, below/right of the index. Draw it in a zero-width inline box at that physical anchor; do not assign an arithmetic or grammatical function.'},
 {'place':'L20 point after X','A':r'\unsure{.}','B':r'\unsure{.}','C':r'\unsure{.}','decision':'The main crop inspection resolves the physical reading as a distinct dark point (A/l20_isolated_point.png). Type it literally as a point; no claim about the intended sentence structure follows from that decision.'},
 {'place':'L22 verb accent','A':r'\unsure{apparaît|apparait}','B':r'\unsure{apparait|apparaît}','C':r'\unsure{apparaît|apparait}','decision':'Retain both, with B’s unaccented candidate first: the raised mark is a short hooked stroke, without a clear two-sided circumflex (B/l22_apparait.png). The letters of the verb itself exclude H’s peut.'},
 {'place':'L23 abbreviated même','A':r'\unsure{\overline m|=}','B':r'\overline m','C':r'\overline m','decision':'Select B/C: the lower glyph has two small rises, distinctly unlike a plain second rule (B/l23_elle_glyph.png). This page’s better-formed barred m does not retrospectively erase the flatter-form doubt on scan 170.'},
 {'place':'L8 plaçons-nous doubt notation','A':r'\unsure{plaçons-nous|plaçons nous}','B':r'\unsure{plaçons-nous|plaçons nous}','C':r'\unsure{plaçons-nous|plaçons nous}','decision':'Retain the hyphen/space doubt (A/l08_addition_placons_les.png). H already marks the same preferred reading uncertain. No H collation row is counted for merely spelling out the alternative in our macro.'}
]
unresolved=[]
for x in r['B']['unresolved']:
 if 'X' in x.get('place','') and ('20' in x.get('place','') or 'parenthesis' in x.get('place','')):continue
 # Rebuild below to ensure origin and textual doubts have explicit places.
unresolved=[
 {'place':'L1 after bout','reading':'comma-like knotted mark','alternatives':['incidental or retraced mark'],'confidence':'low','reason':'Two loop-like returns obscure the comma-like lower hook; no new word can be read.'},
 {'place':'L8 addition','reading':'plaçons-nous','alternatives':['plaçons nous'],'confidence':'medium','reason':'The short joining interval is crowded by the insertion guide; a hyphen is likely but not uniquely separable.'},
 {'place':'L15 below/right of union index','reading':'isolated point, drawn','alternatives':['pen point','reproduction debris'],'confidence':'low','reason':'The physical compact point is distinct; its origin and role are uncertain.'},
 {'place':'L17 cancelled word','reading':'chaque','alternatives':['chaq.'],'confidence':'low','reason':'chaq is recoverable under crossing strokes; the cancelled ending does not settle full ue versus abbreviation.'},
 {'place':'L22 verb accent','reading':'apparait','alternatives':['apparaît'],'confidence':'medium','reason':'The raised hooked stroke does not determine ordinary i mark versus reduced circumflex.'}
]
review=[]
items=[('L1 after bout',r'\unsure{,}','retained: comma-like mark','A/l01_bout_mark.png'),('L7 added etc',r'\unsure{etc|etc.}','resolved: etc','B/l07_added_ens_modules.png'),('L8 added join',r'\unsure{plaçons-nous|plaçons nous}','retained','A/l08_addition_placons_les.png'),('L8 main initial',r'\unsure{Les|les}','resolved: Les','A/l08_addition_placons_les.png'),('L12 accent',r'\unsure{modèle|modéle|modele}','resolved: modèle','A/l12_modele.png'),('L13 abbreviation',r'\unsure{qct|cpct|cpt}','resolved: qct','B/l13_abbreviations.png'),('L17 cancelled word',r'\unsure{chaque|chaq.}','retained','A/l17_deleted_chaque.png'),('L18 loc',r'\unsure{loc|loc.}','resolved: loc','B/l18_loc_constant_cancelled.png'),('L18 cancelled conjunction',r'\unsure{et}','resolved: et','B/l18_loc_constant_cancelled.png'),('L20 physical point',r'\unsure{.}','resolved physical point: .','A/l20_isolated_point.png'),('L22 preposition',r'\unsure{de|des}','resolved: de','A/l22_de_ind.png'),('L22 verb accent',r'\unsure{apparaît|apparait}','retained, preference reordered: apparait|apparaît','B/l22_apparait.png'),('L23 shorthand',r'\unsure{\overline m|=}',r'resolved: \overline m','B/l23_elle_glyph.png')]
for place,earlier,decision,crop in items:review.append({'place':place,'earlier':earlier,'decision':decision,'evidence':'Main inspected crops/scan172/'+crop+'; letter and stroke evidence is recorded in the changes/three-reader tables.'})
inv=copy.deepcopy(r['B']['inventory'])
for x in inv:
 if 'near (1161' in x.get('position',''):
  x.update(kind='drawing',hand='uncertain; pen ink or reproduction mark',first_words_or_objects='isolated point below/right of union index')
 if 'L20 between' in x.get('position',''):x['element']='distinct physical point';x['first_words_or_objects']='.'
notes='''**S172-notes.** The opening continuation says that following the resistance “à fleur de peau” to its end leads to generalizing and deepening the notion of homotopy type. The next paragraph turns to sheaves of sets or modules on the étale topos of a scheme X. It calls locally constant sheaves, subject to a finiteness condition, the simplest constructible sheaves, then describes constructibility through a finite partition into locally closed constructible strata. It says that ind-objects recover all sheaves and that the constructible category appears as an inductive limit of categories associated with partitions; the sentence continues off the page.

The qualifications actually written are “pour simplifier”, “modulo une condition de finitude supplémentaire assez anodine”, “Supposant X cohérent”, and “(plus une condition de finitude…)”. No precise extra hypothesis is supplied by the transcription, and no proof or theorem check was attempted. The parenthetic abbreviation is read qct from its closed initial loop, descender, distinct c and t, rather than from expected compactness. The union and indices i∈I, X_i were inspected; the extra point near the index is reproduced without mathematical interpretation. The grammatical form “la restriction … soit loc constant” is preserved. H’s “peut … se concevoir” is unsupported where the ink reads the apparent/apparait verb, then elle- with a barred m, then comme. The accent of the verb remains uncertain.

This is author page **27**, archive pencil **172**, with no title, date or closing. The indented Parlons begins a new paragraph. Four interlinear additions retain their guide-indicated destinations; two cancellations remain visible. The first parenthesis belongs after faisceaux, not after the previous paragraph. There are no independent diagrams or margin prose. The point between X and (qui is recorded literally despite its unusual grammatical position. The much smaller point by the union index has uncertain origin and is drawn separately.'''
text=(ROOT/'records/scan172/B/reading.tex').read_text()
old=r'\makebox[0pt][r]{\raisebox{-1.3ex}{\(\unsure{\cdot}\)\hspace{0.5em}}}'
mark=r'''\raisebox{-1.7ex}[0pt][0pt]{\makebox[0pt][r]{\parbox{1.5mm}{\figure{\begin{tikzpicture}[x=1mm,y=1mm]\fill (0,0) circle[radius=.14];\end{tikzpicture}}}\hspace{.8em}}}'''
assert old in text
text=text.replace(old,mark).replace('sur $X$ \\unsure{.} (qui','sur $X$ . (qui')
viewed=['A/l01_bout_mark.png','B/l07_added_ens_modules.png','A/l08_addition_placons_les.png','A/l12_modele.png','B/l13_abbreviations.png','C/13_union_indices.png','A/l17_deleted_chaque.png','B/l18_loc_constant_cancelled.png','A/l20_isolated_point.png','A/l22_de_ind.png','B/l22_apparait.png','B/l23_elle_glyph.png']+[f'main/{s}.jpg' for s in ['01_fleur_phrase','02_type_quotes','03_developpement','04_cellules_strates_quotes','05_after_finitude']]
write_decision(172,'B',[],diffs,comparisons,unresolved,inv,notes,r['B']['abbreviations'],review,['crops/scan172/'+p for p in viewed],brief='briefs/brief_v03_scan172.md',workflow_note='All three covered 24 main baselines and four addition lines. Main reused 12 crops and made 5 targeted crops. Differences involved abbreviation stops, the threshold for resolving qct and barred m, the accent preference, and an isolated point missed by A. Identical uncertain preferred plaçons-nous and short/double TeX dash choices were excluded as macro/typesetting equivalents. The final point near the formula is drawn in a zero-width box, preserving its nonsemantic placement.',text_override=text)
add_notation([
 ('Finiteness shorthand','qu. qct; qu. sép','Scan 172 L13: dotted qu, spaces without hyphens; qct resolved from closed oval and descender followed by c and t.'),
 ('Barred même after elle-',r'$\overline m$','Scan 172 L23: two low rises under separate bar; clearer than the equals-like shorthand on scan 170, whose doubt is retained.'),
 ('Sheaf abbreviations','ens,; etc; loc constant','Scan 172 L7 addition has comma but no separate stop after ens, no stop after etc; L18 loc has no stop. Other loc. occurrences have one.'),
 ('Union index',r'$X=\bigcup\limits_{i\in I}X_i$','Scan 172 L15: index i∈I below union, low i after X; separate physical point nearby is not made mathematical notation.')
])
brief=(ROOT/'briefs/brief_v03_scan172.md').read_text().replace('Reader brief v03 — first used on scan 172','Reader brief v04 — first used on scan 173')
brief+='''\n## Clarifications introduced after scan 172\n\n- In report crop paths use `crops/scanNNN/R/name.png`, relative to result/, not `result/crops/...`. Keep each noncontiguous quoted expression as its own place rather than grouping several line numbers into one change row.\n- If H marks the same preferred reading uncertain, our explicit spelling-out of an alternative alone is not a substantive H difference. Record that retained doubt in the doubt review, without an H collation row. Resolving the uncertainty, changing the preferred reading, or changing a word/mark remains a difference.\n- Distinguish uncertainty about a point’s visible shape/presence from uncertainty about its intended role. A clearly distinct inline point can be transcribed literally without claiming a sentence boundary. A nontext point beside a formula must not become a multiplication sign or index. Reproduce such a mark in TikZ using the prescribed figure macro inside a small zero-width inline parbox/raisebox at its anchor, with coordinates and uncertain origin recorded. Do not create a new macro or promote ordinary copy grain to ink.\n- One complete insertion can be a content entry, with its attachment as a separate placement entry. Do not also count each resolved sub-doubt as a duplicate content change unless it is a genuinely separate place; still review every C doubt explicitly.\n'''
(ROOT/'briefs/brief_v04_scan173.md').write_text(brief)
with (ROOT/'records/brief_changes.md').open('a') as f:f.write('\n## v03 → v04, first used on scan 173\n\nScan 172 produced differing dot encodings, repeated content/sub-doubt rows, grouped quotation places and result-prefixed crop paths. The brief now specifies relative paths and one row per distinct place, excludes identical uncertain preferred readings as macro equivalents, and distinguishes a visible inline point from its intended role. Nontext points beside formulas use a TikZ drawing at their physical anchor.\n')
print('172 decision saved')
