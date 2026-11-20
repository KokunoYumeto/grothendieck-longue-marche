import json
from pathlib import Path

P=Path(__file__).resolve().parent
D=[]
def add(id,loc,C,reading,evidence,confidence,kind,changed,status=None,crop=None,box=None):
    D.append(dict(id=id,location=loc,C=C,H=None,reading=reading,evidence=evidence,
                  confidence=confidence,kind=kind,diff_C=changed,diff_H=False,
                  C_doubt_status=status,readers_crop=crop,
                  bbox={"source":"full","xyxy":box}))

add("A01","Second implication: Car",r"\text{car }",r"\text{Car }",
    "Initial open C rises well above following a and r; its capital curve is visible on half a. Nearby final c in donc is shorter.",
    "high","misread word",True,box=[546,225,634,276])
add("A02","First isolated struck line",
    r"\deleted{donc si $\unsure{p\ne1|p\ne q}$}",
    r"\deleted{donc si $\unsure{p\ne1|p\ne q}$}",
    "Tall d, onc and si survive. The p-like descending stem and comparison strokes survive, but the final upright/angled group is crossed repeatedly. Its lower shape does not settle 1 versus q.",
    "low","other",False,"retained","02_first_struck_line.png",[94,383,482,455])
add("A03","Mark above ou p=1, below p premier",
    r"\inserted{ou $p=1$}","Same addition below premier, with small filled triangular mark immediately above",
    "Half a shows a compact dark left-pointing wedge above ou. The triangle is reproduced while its guiding function remains uncertain.",
    "medium","omission",True,box=[580,543,757,634])
add("A04","Deleted parenthesis on l'impose sans risque / si p=1",
    r"\deleted{(on l'impose sans risque si $p=1$)}",
    "Same deleted words and parentheses, with two rising diagonal cancellation strokes",
    "Half a shows two separate obliques, one crossing the left/lower si area toward impose and another from the lower middle toward the right end of risque. Underlying words and both tall parentheses are legible.",
    "high","drawing or diagram",True,box=[891,594,1345,709])
add("A05","Second existential line: second letter",
    r"\unsure{\zeta|\delta}",r"\unsure{\zeta|\delta}",
    "Sloping upper stroke turns sharply into a rounded lower hook with a small closed end. Its raised repetition has the same form. Zeta remains the first candidate, delta survives as an alternative.",
    "medium","other",False,"retained","03_second_letter.png",[575,875,1152,981])
add("A06","Cancelled subscript under a prime",
    r"a_{\deleted{\unsure{0}}}'",r"a_{\deleted{\unsure{0}}}'",
    "The a and prime are clear. A compact filled black patch at the right foot of a occupies subscript height; an independent zero contour cannot be isolated. Zero remains a doubtful candidate.",
    "low","other",False,"retained","04_cancelled_subscript.png",[267,1043,708,1146])
add("A07","Numerical example bracket and long rules",
    "Three-sided border in separate margin picture; two independent rules",
    "Open-right bracket whose left edge meets the shared upper long rule, with second rule below hypothesis",
    "Half b shows a top boundary reaching toward the right edge and left vertical down to the first page-wide rule. This rule continues across the example's bottom. The lower hypothesis rule is separate. The shared geometry is drawn explicitly.",
    "high","drawing or diagram",True,box=[17,1205,1386,1436])
add("A08","Cancelled word before on a",
    r"\deleted{\unsure{alors}}",r"\deleted{\unsure{alors}}",
    "Tall l and rounded/angled remnants survive below zigzag crossings. The group supports alors; overlapping black strokes still obscure initial and terminal contours.",
    "low","other",False,"retained","06_on_a_addition.png",[547,1384,994,1470])
add("A09","Pale equation after on a",
    r"\inserted{$p=q,\ {\unsure{a|\alpha}}'=\gamma$}",
    r"\inserted{$p=q,\ {\unsure{a|\alpha}}'=\gamma$}",
    "Pale p=q and comma are legible. Under the prime is a small oval with short right continuation; a remains primary, alpha remains possible. Equality and looped gamma follow clearly.",
    "medium","other",False,"retained","06_on_a_addition.png",[547,1384,994,1470])
add("A10","Cancelled p-like entry before lower q squared",
    r"\deleted{\unsure{p^{2}|p}}",r"\deleted{\unsure{p^{2}|p}}",
    "Descending stem and right bowl support p. A compact group above/right could preserve exponent 2 but merges with cancellation. The enlarged strokes do not settle p squared versus p.",
    "low","other",False,"retained","07_lower_cancelled_p.png",[96,1444,451,1545])
add("A11","Pale absurde car q nondivisibility a",
    r"\deleted{\text{ou }p=1\Longrightarrow p=1}\ \inserted{\text{absurde car }q\nmid a}",
    "Same insertion placed above cancelled ou p=1 implies p=1",
    "Pale absurde car runs directly above the rising cancellation; q crossed-bar a stands above final dark p=1. The transcription places this addition above its target.",
    "high","insertion or placement",True,None,"08_lower_overlap.png",[450,1448,837,1598])
add("A12","First lower ou p=1 cancellation",
    r"\deleted{\text{ou }p=1}","Same deleted wording with paired cancellation passes and hooked return",
    "Two close passes through the phrase join in a rounded return at the right of 1. Both passes and the return are drawn.",
    "high","drawing or diagram",True,None,"08_lower_overlap.png",[450,1448,837,1598])
add("A13","Final cancelled q and raised q alpha minus 1",
    r"{\deleted{q}}^{q\alpha-1}","Cancelled q with intact q alpha minus 1 raised above and right",
    "Cancelled glyph has a round head and long descending right stem crossed by two rising looped strokes. Above, q, tall alpha, minus and 1 are individually legible. Their physical raised placement is drawn without mathematical reconstruction.",
    "high","other",True,"resolved","09_final_replacement.png",[516,1577,739,1700])
add("A14","Detached stroke upper-left of l'ensemble",
    "No separate mark",r"\unsure{/} immediately before and above l'ensemble",
    "A short detached rising dark stroke is visible just left of the tall initial l. Its slash-like shape is supported; its attachment to the letter, role and hand remain unresolved.",
    "low","omission",True,None,"10_right_note.png",[847,1533,870,1554])

I=[]
def inv(n,k,pos,first,hand="another unnamed hand"):
    I.append(dict(sheet_kind="text",hand=hand,element=f"008.A.{n:02d}",kind=k,
                  position=pos,first_words_or_objects=first,transcribed="yes"))
rows=[
(1,"text","top","Supposons que q alpha-alpha prime ne 0 alors"),
(2,"display","first two implications","(1) implies p divides sum; implies p divides q a^(q-1)"),
(3,"deletion","endpoint of second implication","ne 0 before >0"),
(4,"text","below first implications","or p divides b prime et b prime divides b^q"),
(5,"deletion","isolated struck line","donc si p ne 1 / p ne q"),
(6,"display","next implication","(1) implies p divides q donc ... p=q"),
(7,"deletion","within preceding display","p=1 ou"),
(8,"text","Donc si line","Donc si p ne q p premier ... alpha prime=q alpha"),
(9,"insertion","below premier","ou p=1"),
(10,"drawing","above ou p=1","small filled triangle"),
(11,"deletion","upper-right two-line parenthesis","(on l'impose sans risque si p=1)"),
(12,"drawing","over that parenthesis","two separate oblique cancellations"),
(13,"text","first existential line","Donc exists b_0 in N star et exists gamma in N"),
(15,"text","above fold","de plus b_0 divides b et si b=b_0 b double prime"),
(16,"text","below fold first line","De meme exists a_0 in N star et exists zeta/delta in N"),
(17,"text","continuation below fold","avec a_0 divides a et si a=a_0 a double prime"),
(18,"text","product and coprimality line","or a bowl_1 b implies a prime bowl_1 b prime"),
(19,"deletion","under a prime","black patch with doubtful zero candidate"),
(20,"text","before c display","Je suppose desormais que zeta=0 donc a prime=a_0^q"),
(21,"display","above upper rule, left","Donc c=b+a_0^q=a+q^gamma b_0^q"),
(22,"margin note","right of c display","pour q=2 on a, a_0=b_0=1, gamma=1, b=4, a=3, c=5"),
(23,"drawing","example and hypothesis","open-right bracket, connected upper rule, separate lower rule"),
(24,"text","between rules","Je fais l'hypothese suivante si q premier et 1<=i<q alors q divides C_q^i"),
(25,"text","below lower rule","alors Si q>=3 et q alpha-alpha prime>=2 ... on a"),
(26,"deletion","before on a","doubtful alors"),
(28,"display","lower pair of implications","q^2 divides q a^(q-1); q divides a^(q-1)"),
(29,"deletion","before lower q squared","p squared / p"),
(30,"deletion","after first lower q a^(q-1)","ou p=1"),
(31,"drawing","through first lower ou p=1","paired cancellation passes with hooked return"),
(32,"deletion","second lower implication endpoint","ou p=1 implies p=1"),
(34,"text","last line","Donc gamma=0 ou gamma=... (sous reserve que l'hypothese est vraie)"),
(35,"deletion","after final gamma equality","q"),
(36,"text","raised above cancelled q","q alpha - 1"),
(37,"drawing","through final q","two rising looped strokes and lower tail"),
(38,"margin note","lower right","C'est peut-etre interessant car ici 2 est mis a part dans l'ensemble des nombres premiers"),
(40,"drawing","right of final parenthesis and note","bent upward/leftward return arrow")]
for row in rows: inv(*row)
inv(14,"margin note","right of first existential line","q nondivisibility b_0","undetermined hand")
inv(27,"insertion","pale text after on a","p=q, a prime / alpha prime=gamma","undetermined hand")
inv(33,"insertion","above second lower cancellation","absurde car q nondivisibility a","undetermined hand")
inv(39,"text","upper-left of l'ensemble","qualified detached slash-like mark","undetermined hand")
inv(41,"text","bottom left","archive 7, retained only as a comment","undetermined hand")
I.sort(key=lambda x:x["element"])

alternatives={
"A02":[r"p\ne q"],"A05":[r"\delta"],"A06":["unrecovered subscript; zero only a candidate"],
"A08":["word obscured by cancellation"],"A09":[r"\alpha'=\gamma"],
"A10":["p without recovered exponent"],"A14":["detached onset of l; role unresolved"]}
doubts=[dict(location=d["location"],reading=d["reading"],alternatives=alternatives[d["id"]],
             confidence=d["confidence"],reason=d["evidence"],crop=d["readers_crop"])
        for d in D if d["id"] in alternatives]
specs=json.loads((P/"crop_plan.json").read_text())
report=dict(
scan="008",reader="A",start_utc="2026-11-20 11:20:53 UTC",end_utc=None,
full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
differences=D,doubts=doubts,inventory=I,
notes={
"page_content":"Handwritten divisibility deductions and factorizations, queried coprimality expressions, the writer's assumption, a numerical example, ruled hypothesis, altered lower implications, qualified final line and right note.",
"authors_own_uncertainty":["alors b_0 bowl-with-1 b double prime ?","alors a_0 bowl-with-1 a double prime ?","Je suppose désormais que","Je fais l'hypothése suivante","(sous réserve que l'hypothése est vraie)","C'est peut-être interessant"],
"title_date_page_counts":"No title, date or manuscript page numeral supplied. Bottom-left archive numeral 7 is retained only in a comment.",
"hand_attribution":"Main dark hand follows packet attribution as another unnamed hand; identity was not independently established. Pale additions and the detached stroke use undetermined hand.",
"mathematics_led_reading_decisions":"No mathematical calculation, proof check or correspondence was used to settle ink. Written statements and qualifications are transcribed without repair. Formula placements were inspected visually.",
"C_doubt_map":{"First isolated struck line":"A02 retained","Second existential line":"A05 retained","Before second bowl in or a…":"A06 retained","Above last two implications":"A08 retained","After (1)⇒ in lower left":"A10 retained","End of final line":"A13 resolved","Lower line, light addition after on a":"A09 retained"},
"source_section_accounting":"Six notation rows are not additional doubts. Repeated zeta/delta notation maps to A05. Final cancelled-q row is an actual doubt despite no unsure macro. Interessant and hypothése rows are slips retained, not original doubts, per section metadata supplied by root.",
"slips_checked":["Crop 05: rising acute in first hypothése retained.","Crop 11: rising acute in final hypothése and réserve retained.","Crop 10: no detached acute over interessant; unaccented spelling retained. Peut-être and à preserved."],
"physical_features":"Horizontal fold crosses between existential passages. Bracket, rules, cancellations, additions, return arrow and archive numeral are recorded. No supported character was recovered from the small irregular dark area at extreme upper right.",
"view_attestation":{"whole_image_views":1,"half_a_views":1,"half_b_views":1,"crop_images_created":11,"crop_views":11,"recrops":0,"full_dimensions":[1404,1721],"half_a_dimensions":[1404,940],"half_b_dimensions":[1404,941],"half_a_origin_in_full":[0,0],"half_b_origin_in_full":[0,780],"order":"UTC start, assigned textual packet/preamble/notation, whole once, a once, b once, eleven local crops each once. No OCR, internet, other pages/readers or delegation."}},
notation=[
{"location":"first expansion","sign":"sum and binomial indices","latex":r"\sum_{i=1}^{q-1}C_q^i a^i b'^{q-i-1}+b'^{q-1}","evidence":"Dotted i at each position; q below C; both prime marks inspected on half a."},
{"location":"coprimality expressions","sign":"shallow bowl over small hooked 1","latex":r"\mathrel{\underset{1}{\smile}}","evidence":"Open bowl and separate low hooked numeral visible at each occurrence."},
{"location":"existential lines","sign":"double-stroked N with and without star","latex":r"\mathbb N^*,\mathbb N","evidence":"Doubled left stroke; star after a_0,b_0 memberships, absent after Greek-letter memberships."},
{"location":"first existential statement and repetitions","sign":"gamma","latex":r"\gamma","evidence":"Forked top returns into narrow lower loop."},
{"location":"second existential statement","sign":"qualified zeta/delta","latex":r"\unsure{\zeta|\delta}","evidence":"Sloping top and rounded hooked lower part; A05 remains qualified."},
{"location":"pale notes","sign":"crossed divisibility bar","latex":r"\nmid","evidence":"Separate oblique crosses upright bar."},
{"location":"ruled hypothesis","sign":"inequality and binomial indices","latex":r"1\leqslant i<q,\ C_q^i","evidence":"Lower diagonal under first comparison; dotted i; q below C."},
{"location":"second implication endpoint","sign":"cancelled comparison","latex":r"\deleted{\ne0}>0","evidence":"Crop 01 supports overwritten two-bar/crossed-stem sign and oval zero; live >0 follows. Confirmation creates no invented C difference."},
{"location":"factorization continuations","sign":"double primes","latex":r"b'',a''","evidence":"Two distinct raised strokes after each letter."},
{"location":"two hypothése occurrences","sign":"acute","latex":"hypothése","evidence":"Separate rising accents in crops 05 and 11."}],
check_events=[],
crops=[dict(path=n,bbox=b,rotation=r,purpose=p,viewed_once=True,source="source/SP40_CW_81_scans/J81-01_81_scan008.jpg",processing="autocontrast, LANCZOS to 2800 px, UnsharpMask") for n,b,r,p in specs],
brief_feedback=[
"Original C_doubts section headers were absent; root's section-metadata clarification was applied.",
"Final raised q alpha minus 1 is drawn physically rather than assigning an unestablished algebraic role to its placement.",
"Detached stroke by l'ensemble supports a shape candidate; attachment to l remains uncertain."],
counts=dict(difference_rows=len(D),rows_with_diff_C=sum(d["diff_C"] for d in D),rows_with_diff_H=0,original_C_doubt_loci=7,original_C_doubts_resolved=1,original_C_doubts_retained=6,unresolved_loci=len(doubts),inventory_items=len(I),crops=11))
report["end_utc"]="2026-11-20 11:35:24 UTC"
report["notes"]["validation"]="Final TeX/report consistency checked: seven original doubt decisions, seven unsure loci, H absent throughout, all eleven crop paths exist, 41 inventory items, balanced braces and paired drawing/display environments. A pdflatex syntax attempt could not start because pdflatex.fmt is unavailable; no compilation success is claimed."
report["notes"]["authors_own_uncertainty"][0]=r"alors $b_0\mathrel{\underset{1}{\smile}}b''$ ?"
report["notes"]["authors_own_uncertainty"][1]=r"alors $a_0\mathrel{\underset{1}{\smile}}a''$ ?"
(P/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
