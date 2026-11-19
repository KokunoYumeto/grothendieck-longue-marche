#!/usr/bin/env python3
"""Documentary audit of the three C-notes files against frozen page TeX only."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,json,re

OUT=Path(__file__).resolve().parents[1]
PAGES={n:next((OUT/'pages').glob(f'*scan{n:03}.tex')) for n in range(2,26)}
TEXT={n:p.read_text() for n,p in PAGES.items()}
quotes=[];events=[];items=[]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def q(scan,words):
    assert words in TEXT[scan],(scan,words)
    line=TEXT[scan].count('\n',0,TEXT[scan].index(words))+1
    quotes.append({'scan':scan,'tex_line':line,'quote':words})
    if '\n' in words:
        return f'\n\n```tex\n{words}\n```\n\n(scan {scan:03}, beginning at TeX line {line})'
    return f'`{words}` (scan {scan:03}, TeX line {line})'

def event(identifier,outcome):
    events.append({'statement_id':'SP31-CNA-'+identifier,'date':now,'who':'GPT-6 Astra Pro; effort not supplied; SP31 documentary C-notes audit /root/validation_tools',
                   'type':'used and rechecked in this run','outcome':'Documentary comparison with frozen TeX only; no image rereading or mathematical proof check. '+outcome})

def item(identifier,origin,decision,claim,body):
    items.append((identifier,decision))
    event(identifier,decision.upper()+': '+claim+' '+body.split('\n')[0])
    return f'### {identifier} — {decision.upper()}\n\nC source: `{origin}`. Original item: {claim}\n\n{body}\n'

def cell(s):return str(s).replace('|',r'\|').replace('\n','<br>')

parts=['# Audit of witness C’s research-note items',
       f'\nDocumentary audit completed {now}. The authority for all quotations below is the transcription frozen at 2026-11-19 21:46:48 UTC. Source references use archive scan numbers; TeX line numbers refer to the frozen page files.\n',
       'This audit checks what C’s notes report, how the author marks a step, and whether the same text subsequently answers, revises or abandons it. “Self-answered” and “addressed” describe the manuscript’s presentation; they do not certify a mathematical proof. No RESULTS_STATE result is used here.\n',
       'The original notes are `codex/J156-3-01/J156-3-01_notes.md`, `codex/J156-3-02/J156-3-02_notes.md`, and `codex/J156-3-03/J156-3-03_notes.md` in the supplied witnesses. Abbreviations C01, C02 and C03 below refer to those files.\n',
       '## 1. Every original item about unverified or provisional steps\n']

parts.append(item('C01-U01','C01 line 7','keep','Scan003 asks whether the moderated complement determines T and whether an inclusion reverses.',
    q(3,r'Question : $T$ est-il connu quand on \unsure{connait|connaît} $C_{\mathcal L}(T)$ ?')+' The same margin continues '+q(3,"l'inverse est-il vrai ? Oui,")+', and the lower NB asserts '+q(3,r'$T$\deleted{\unsure{est}} est connu quand on \unsure{connait|connaît} $C(T)$')+'. Keep this as a question that the author answers on the same page, not as an unanswered item; the sketch’s validity is outside this documentary check.'))
parts.append(item('C01-U02','C01 line 8','keep','Scan004 anticipates recovery of datum c from b and of b from the two-point data.',
    q(4,'Je prévois que les axiomes impliquent')+' introduces both stated expectations, and '+q(4,r'\uline{Axiomes provisoires :}')+' remains the live heading. Scans011–016 subsequently develop recovery for the tronçon/biorder setting, whereas scan017 still asks for the intrinsic axioms; do not turn that special-case development into a completed general axiom system.'))
parts.append(item('C01-U03','C01 line 9','keep','Scan006 reserves judgment about the finiteness hypotheses.',
    q(6,'peut-être\nprovisoires')+' qualifies the finiteness hypotheses immediately before Dec₁ and Dec₂. This is a live provisional-status reservation, not a statement that either axiom has been disproved, and no explicit removal of that reservation appears later in these24 pages.'))
parts.append(item('C01-U04','C01 line 10','keep','Scan008 orders a rewriting beyond the case of a line and leaves a marginal sentence unfinished.',
    q(8,"refaire, sans se borner à une ligne : sous tronçon fermé d'un tronçon.")+' is retained, and the final words really are '+q(8,"le bord d'un tronçon est défini Comme des")+'. Add the later history: scan018 takes up closed sub-tronçons and relative frontier, while scan025 returns to the terminology and cancels a boundary-definition block; the instruction is acted on, but the initial marginal sentence is not completed in place.'))
parts.append(item('C01-N01','C01 line 12','keep','No other explicit verification request is listed for002,005,007,009; “Axiome” on005 is a label.',
    'Keep this negative statement in its narrow local sense. '+q(2,'Je voudrais définir une autre axiomatique')+' is a programmatic opening, and '+q(5,r'\uline{Axiome}')+' labels an assumption; neither is an unfulfilled proof-check instruction. The editorial `\\unsure` marks on these pages must not be counted as questions written by the author.'))
parts.append(item('C02-U01','C02 line 5','keep','Scan017, circled2, asks for explicit axioms on the ternary relation and the decomposition data.',
    q(17,r'\textcircled{2} Il faudrait expliciter')+' remains live. The number of “quelle(s) condition(s)” and the biordonné/biordonnien ending remain explicitly uncertain in the frozen TeX, so C’s linguistic caution should be retained; scans018–025 do not supply the requested complete intrinsic axiom list.'))
parts.append(item('C02-U02','C02 line 6','keep','The order-reconstruction question on013 leads to a lemma and a proof on014; the older remaining-to-prove sentence is struck.',
    q(13,'quand a-t-on')+' leads to the displayed inequality, and '+q(14,'Donc il faut simplement vérifier le')+' introduces the lemma. The proof ends with '+q(14,r'$x\leq u\leq v$\quad OK')+', while '+q(14,r'\deleted{il reste à prouver $u\leq v$}')+' is canceled. Keep it under “verification undertaken and authorially completed,” not as a still-live “il reste à prouver” obligation.'))
parts.append(item('C03-U01','C03 line 7','keep','Scan023 leaves the T₀ question for an arbitrary tronçon open.',
    q(23,"je ne sais si c'est")+' is completed by '+q(23,'le cas pour tout tronçon')+'. The preceding positive assertion continues the ficelle-lieux case from scan022; it must not be promoted to a theorem for every tronçon. No answer to the general question is recorded by scan025.'))
parts.append(item('C03-U02','C03 line 8','correct','Scan023 also asks about sobriety and the generic-point condition, with an A voir note.',
    'Keep the mathematical question, but update the literal quotation to the frozen form: '+q(23,r'\margin{\unsure{A|À} voir,}')+'. The live question is '+q(23,"ni si un tronçon, avec sa top. canonique, est sobre")+', followed by '+q(23,r'tte partie fermée \uline{irréductible} aurait un pt générique \dots')+'. The accent and punctuation of the short marginal tag should not silently be normalized to C’s unqualified sentence form.'))
parts.append(item('C03-U03','C03 line 9','keep','Scan023 asks for the converse of the closed-point conclusion in the totally ordered case.',
    q(23,'les pts sont fermés (réciproque ?)')+' is an explicit live question. Its immediate attachment is to closed points; C does not justify transferring the question mark to the following separatedness assertion, and these24 pages give no explicit answer to that converse.'))
parts.append(item('C03-U04','C03 line 10','keep','Scan024 asks the interval-closure equality after a canceled first wording.',
    q(24,'Aura-t-on')+' introduces '+q(24,r'\overline{]a,b[}&=[a,b]\quad ?')+'. Preserve the distinction between the canceled first wording and this live question; its setting is the topology proposed immediately above as the upper bound of two topologies. Link it to the failed argument lower on024 and the return to the first topology on025, rather than listing it as an untouched open assertion in the final chosen topology.'))
parts.append(item('C03-U05','C03 line 11','keep','Scan024 asks the lower-ray closure equality with a lower-endpoint qualification.',
    q(24,r'\overline{\mathcal L_{<a}}&=\mathcal L_{\leq a}\quad ?')+' is retained, as is the insertion '+q(24,r'\inserted{(a\ne\unsure{o|0}_{L})}')+'. C correctly preserves the o/0 uncertainty; the equality is asked, not proved, and belongs to the same subsequently abandoned topology experiment as the neighboring questions.'))
parts.append(item('C03-U06','C03 line 12','keep','Scan024 asks the upper-ray closure equality and questions its upper-endpoint qualification.',
    q(24,r'\overline{\mathcal L_{>a}}&=\mathcal L_{\geq a}\quad ?')+' and '+q(24,"si $a$ n'est pas plus grand élément ?")+' both retain their question marks. No separate resolution of this equality is written before the change of course on025.'))
parts.append(item('C03-U07','C03 line 13','keep','Scan024 attempts an endpoint-neighborhood argument, then declares the proposed step false and supplies a sketch.',
    q(24,'à prouver (p. ex.)')+' introduces the attempted endpoint claim, but the author then writes '+q(24,"Mais c'est faux déjà pour un ens. de lieux associé à une ficelle topologique")+'. The margin specifies '+q(24,r'Il faut avoir que $a\in\complement[x,y]$ mais $]a,b[\,\subset [x,y]$')+'. Record a failed/withdrawn route in the same text; neither C’s summary nor this audit is an independent verification of the sketch.'))
parts.append(item('C03-N01','C03 line 15','correct','C says018–022 and025 carry no further explicit question or reservation and treats the other marginal notes as qualifications.',
    'Retain the narrower finding that these pages add no further explicit interrogative of the same kind, but qualify the carryover: scan021 replaces the canceled ordinary-difference formulation by a moderated-complement formulation, and025 both changes course and cancels the proposed boundary-definition/examples block. In particular, '+q(25,'Finalement, on travaillera avec la top. définie d\'abord')+' and '+q(25,'néanmoins par abus de langage')+' are substantive scope decisions, not an absence of revision. Scan020’s double-recurrence annotation is a stated proof method, not a request to verify the argument.'))

parts.append('## 2. Every original title/date/numbering row\n\nThis table also supplies the proposed consolidated register of headings and manuscript numbers. An internal heading is not a separate title sheet.\n\n| C item and original line | Scan / manuscript number | Decision | Frozen evidence and qualification |\n|---|---|---|---|')
title_data=[
(2,'C01-T01',18,'correct',r'\uline{Réseaux}\ldots\ via découpages.','The same sheet carries (8 Juin 86) and GF with underlined III; replace C’s unresolved abbreviation description by the frozen GF reading.'),
(3,'C01-T02',19,'keep',None,'Continuation; no date or separate title.'),
(4,'C01-T03',20,'keep',r'\uline{Axiomes provisoires :}','Internal heading; no date.'),
(5,'C01-T04',21,'keep',r'\inserted{Ex 1}','The same sheet also has the live Axiome label and the discrete-network structure heading; no date.'),
(6,'C01-T05',22,'keep',r'\margin{Finitude}','Dec₁ and Dec₂ are live labels; the earlier Partie modérée fermée definition heading is canceled. No date.'),
(7,'C01-T06',23,'correct',r'\uline{Ex \deleted{\unsure{1}}2}','The live example number is2; the uncertain1 belongs to deleted ink. Drop C’s alternative of a live1.'),
(8,'C01-T07',24,'keep',r'\uline{Partie} \uline{modérée}','The earlier Tronçons/Tronçon word remains uncertain. These are internal labels, not a title sheet.'),
(9,'C01-T08',25,'keep',r'\uline{Définition}\quad Un ens. ordonné','The prior Proposition and Définition/Segment formulations are canceled. No date.'),
(10,'C02-T01',20,'keep',None,'Number9; no title sheet, date or page-total statement.'),
(11,'C02-T02',21,'keep',None,'Number10; no title sheet, date or page-total statement.'),
(12,'C02-T03',22,'keep',None,'Number11; no title sheet, date or page-total statement.'),
(13,'C02-T04',23,'keep',None,'Number12 retains an uncertainty between one and two following points; the numeral itself is12.'),
(14,'C02-T05',24,'keep',None,'Number13; no title sheet, date or page-total statement.'),
(15,'C02-T06',25,'keep',None,'Number14; no title sheet, date or page-total statement.'),
(16,'C02-T07',26,'keep',None,'Number15; no title sheet, date or page-total statement.'),
(17,'C02-T08',27,'keep',None,'Number16; no title sheet, date or page-total statement.'),
(18,'C03-T01',21,'keep',r'\uline{Partie fermée} \uline{modérée} de $I$','The opening Sous tronçon has fermé I inserted. Preserve the written I in this heading.'),
(19,'C03-T02',22,'keep',r'\uline{Th}','Th, Def and marginal Ex are present; no date.'),
(20,'C03-T03',23,'keep',r'\uline{Cor}','Prop, Cor, Ex and marginal Dém, Rem, Attention are present; no date.'),
(21,'C03-T04',24,'keep','Partie loc. fermée modérée','The Th label follows; no date.'),
(22,'C03-T05',25,'keep','(9 juin)','The date follows the wavy division and is followed by the circled1 topology entry. No year is written in this date.'),
(23,'C03-T06',26,'keep',None,'No new date, title or section heading; the A/À voir note is a verification tag.'),
(24,'C03-T07',27,'keep',None,'No new date, title or section heading; Aura-t-on is a question introduction.'),
(25,'C03-T08',28,'keep',r'\uline{sous-tronçon \inserted{fermé} large}','The earlier sous-tronçons word is also underlined. The canceled lower boundary block must not be treated as a live definition.'),
]
for scan,identifier,cline,decision,heading,qualification in title_data:
    ms=re.search(r'\\mspage\{',TEXT[scan]);assert ms
    # First-page line references preserve the nested uncertainty on scan013.
    first_line=TEXT[scan].splitlines()[0]
    ms_number=str(scan-1)
    evidence=(q(scan,heading)+' ' if heading else '')+qualification+' Manuscript-number marker: '+q(scan,r'\mspage{'+(r'12\unsure{..|.}' if scan==13 else ms_number)+'}')
    parts.append('| '+' | '.join(map(cell,[identifier+f' / C note line {cline}',f'{scan:03} / {ms_number}',decision.upper(),evidence]))+' |')
    items.append((identifier,decision));event(identifier,decision.upper()+': '+qualification)

parts.append('\n## 3. Every original global metadata assertion\n')
global_items=[
('C01-G01','C01 line27','No separate title sheet in002–009.','Keep:002 begins the chapter and immediately continues into mathematical text on the same sheet.'),
('C01-G02','C01 line27','No explicit total page count in002–009.','Keep: the manuscript numerals1–8 are individual page numbers, not an authored total-count statement.'),
('C01-G03','C01 line27','Eight numbered manuscript pages are visible in the batch.','Keep: scans002–009 carry manuscript numbers1–8 consecutively.'),
('C01-G04','C01 line27','No second date occurs in that batch.','Keep with its batch scope: the later (9 juin) on022 means this cannot become a global claim that the consolidated packet has only one written date.'),
('C02-G01','C02 line12','No title sheet in010–017.','Keep: all eight are continuation sheets of mathematical notes.'),
('C02-G02','C02 line13','No written date in010–017.','Keep with its batch scope; the dates on002 and022 lie outside this C batch.'),
('C02-G03','C02 line14','No statement of a total page count in010–017.','Keep:9–16 are page numerals, not a total count.'),
('C02-G04','C02 line16','The author’s numbering is consecutive.','Keep: the displayed manuscript numbers are9–16 in archive-scan order, with the trailing punctuation doubt on12 retained.'),
('C03-G01','C03 line30','No title sheet in018–025.','Keep with the supplied-page scope; the new dated topology discussion starts within022.'),
('C03-G02','C03 line30','No authored total page count in018–025.','Keep: no 8 pages or24 pages statement is carried by these sheets.'),
('C03-G03','C03 line30','The eight sheets are numbered17 through24.','Keep: these are consecutive manuscript numbers on scans018–025.'),
]
for identifier,origin,claim,reason in global_items:
    parts.append(item(identifier,origin,'keep',claim,reason+' The individual-number and heading evidence is registered in section2.'))

parts.append('## 4. Proposed standing section: author-marked uncertainty and its subsequent status\n\n### Still-live questions or provisional reservations in this packet\n\n'+
'''- **Scan004 — anticipated reconstruction and provisional axioms.** Keep the two expectations concerning c from b and b from the two-point data, while distinguishing the later tronçon reconstruction from a completed general axiom system (C01-U02).
- **Scan006 — provisional finiteness.** The reservation concerns the imposed finiteness hypotheses; no explicit withdrawal of that reservation follows (C01-U03).
- **Scan017 — intrinsic axioms still to be written.** The ternary relation and two-point decomposition presentations require explicit conditions (C02-U01).
- **Scan023 — arbitrary-tronçon T₀ and sobriety questions.** Keep the two separate questions and the generic-point parenthesis, with the A/À voir reading left marked (C03-U01 and U02).
- **Scan023 — converse concerning closed points.** Keep the parenthetical question separately from the following separatedness assertion (C03-U03).

### Self-answered, addressed later, or withdrawn within the text

- **Scan003 — self-answered on the same sheet.** The complement-recovery question receives the author’s affirmative answer and a reiterating NB. Its mathematical validity is not certified by that documentary status (C01-U01).
- **Scan008 →018 and025 — reworking taken up, with further revision.** The instruction to leave the line-only case is followed by the closed-sub-tronçon discussion; the boundary formulation remains a site of revision (C01-U04).
- **Scans013–014 — verification followed by an author proof.** Preserve the live question and lemma request, but do not revive the canceled remaining-to-prove sentence after the proof’s OK (C02-U02).
- **Scans024–025 — a proposed topology and a failed closure route.** Keep all three closure questions as questions asked in that experiment; record the author’s failure diagnosis and the ensuing return to the first topology. Do not silently transfer the three questions to the final chosen topology (C03-U04 through U07).
''')

parts.append('\n### Additional status items needed beyond C’s summaries\n')
additions=[
('A01','Scan011 →016: the anticipated recovery is pursued in a special setting.',
 q(11,'Je dis que l\'on récupère la structure dé')+' introduces the biorder-recovery claim, and scan016 concludes '+q(16,'On gagne !')+'. This is the manuscript’s claimed success for the reconstruction developed there; the intrinsic-axiom request on017 remains separate.'),
('A02','Scan015 →016: an announced demonstration is subsequently carried out.',
 q(15,'On va voir maintenant comment la connaissance')+' leads into the three-component comparison and '+q(16,'On gagne !')+'. Add this to the record of announced-and-addressed steps, not to the list of still-open tasks.'),
('A03','Scan015: a colon/question-mark reading must not become a certain author question.',
 q(15,r'R(a,b,c)\unsure{\mathord{:}|\mathord{?}}')+' carries an editorial alternative in the frozen transcription. It is a reading question, not documentary evidence of a definite extra self-flagged question mark.'),
('A04','Scan021: ordinary difference is replaced by moderated complement.',
 q(21,r'\deleted{Alors $\exists$ une plus petite partie fermée modérée \inserted{$Z$} contenant $X\setminus Y$.}')+' is canceled. The live formulation introduces C_mod(Y,X) and a least closed moderate set containing that set; record a changed formulation without asserting that this documentary change by itself proves the earlier assertion false.'),
('A05','Scan022: the singleton-closed discussion is revised into a warning.',
 q(22,r"\uline{n'est pas} \inserted{\uline{néc$^{\mathrm t}$}} \uline{fermé}")+' is the live conclusion after canceled trial wording. This is a substantive qualification, not an additional unresolved interrogative.'),
('A06','Scan025: the topology experiment is set aside and closed terminology is qualified.',
 q(25,'Finalement, on travaillera avec la top. définie d\'abord')+' and '+q(25,'néanmoins par abus de langage')+' should accompany the scan024 failure in the standing account. The terminology remains live even though topological closedness is not being asserted for every named sub-tronçon.'),
('A07','Scan025: the boundary definition and its examples are canceled.',
 q(25,r'\deleted{\partial T=}')+' begins the canceled lower display, and the later '+q(25,r'\deleted{\partial[a,b]=\{a,b\}}')+' belongs to the canceled example block. Report this as withdrawn draft material; neither the proposed definition nor its four examples should be quoted as a live conclusion on025.'),
('A08','Scan020: a proof-method note and a negative warning are not open verification requests.',
 q(20,'double récurrence sur nb de comp. conn. de $X$ et de $Y$')+' records a proposed proof method, while '+q(20,'C\'est déjà faux ds le cas standart $L=[0,1]$ !')+' records the author’s rejection of a general closure extension. These deserve the main research notes’ unproved-claim/example treatment, but should not be mislabeled as author requests to check a step.'),
]
for identifier,title,body in additions:
    parts.append(f'#### {identifier} — {title}\n\n{body}\n')
    event(identifier,title+' '+body.split('\n')[0])

parts.append('## 5. Proposed standing section: titles, dates and counts\n\n'+
    'The chapter-opening sheet is scan002, manuscript page1. Its title is '+q(2,r'\uline{Réseaux}\ldots\ via découpages.')+', its date is '+q(2,'(8 Juin 86)')+', and its corner inscription includes '+q(2,r'GF\,\uline{III}')+'. It is not a separate blank title sheet: the axiomatic discussion begins below it.\n\n'+
    'The second written date is '+q(22,'(9 juin)')+' on scan022, manuscript page21, after the dividing stroke and before the topology discussion. That entry carries no year; the earlier86 should not be silently inserted into its quotation.\n\n'+
    'The24 supplied scans002–025 bear consecutive manuscript numbers1–24; scan013 retains uncertainty about the point(s) after12. There is **no authored statement of a total page count** and no separate title sheet in the supplied packet. The internal headings are registered in section2.\n')

counts=Counter(decision for _,decision in items)
parts.insert(4,'**Audit coverage:**50 original C-note items (15 uncertainty/status items,24 title/numbering rows,11 global metadata assertions): '+', '.join(f'{value} {key}' for key,value in sorted(counts.items()))+'. No original item is dropped wholesale; corrections qualify the quotation or carryover status. Eight additional documentary status items are supplied below.\n')
assert len(items)==50,len(items)
assert len(events)==58,len(events)
parts.append('## 6. Check-event scope and quotation verification\n\nEvery quoted fragment was checked as an exact substring of the frozen page TeX before this file was written. The companion `C_notes_CHECK_EVENTS.tsv` records documentary checks of the50 original items and8 additions; it does not claim image checking, proof checking, or independent mathematical verification. The proposed standing sections reuse those same checked items.\n')
document='\n'.join(parts)+'\n'
# Add prose spacing without changing file identifiers, TeX or quoted formulas.
document=re.sub(r'\b(Scan|Scans|scan|scans|these|the|all|through|numbers|number|numbering|pages|page|for|on|items|occurrences|note|line|and)(?=\d)',r'\1 ',document)
document=document.replace('items,24','items, 24').replace('rows,11','rows, 11')
(OUT/'research/C_notes_audit.md').write_text(document,encoding='utf-8')
with (OUT/'research/C_notes_CHECK_EVENTS.tsv').open('w',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(events)
(OUT/'research/C_notes_quote_checks.json').write_text(json.dumps({'checked_at_utc':now,'exact_quote_count':len(quotes),'quotes':quotes,'original_item_count':len(items),'decisions':counts},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'original_items':len(items),'decisions':counts,'additional_items':8,'exact_quotes_verified':len(quotes),'check_events':len(events)},ensure_ascii=False))
