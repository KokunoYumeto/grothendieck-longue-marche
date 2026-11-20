import json
from pathlib import Path

ROOT=Path('/workspace/scratch/8f839dff4bf0')
WORK=ROOT/'SP74_C13_143+145_work'
packet=json.loads((ROOT/'reader_packets/143_scan010.json').read_text())
accepted_report=json.loads((WORK/'reviews/143_scan010_accepted.json').read_text())
before=(WORK/'pages/143_scan010.tex').read_text()
C,H=packet['witness_C'],packet['witness_H']

edits=[
    (r'base\ldots',r'base..\unsure{.}.'),
    ('relation entre pts de',r'relation entre p\textsuperscript{ts} de'),
    (r"\widetilde{\mathfrak X}'(I)\mathbin{-}I",r"\widetilde{\mathfrak X}'(\unsure{\Delta|I})\mathbin{-}I"),
]
candidate=before
for old,new in edits:
    assert candidate.count(old)==1,(old,candidate.count(old))
    candidate=candidate.replace(old,new,1)

crops={
    'upper-margin':('crops/143_scan010_readerC_upper-margin.png',[20,345,390,775]),
    'lower-margin':('crops/143_scan010_readerC_lower-margin.png',[18,1285,322,1817]),
    'final-maps':('crops/143_scan010_readerC_final-maps.png',[602,1998,1430,2220]),
    'diagram-label':('crops/143_scan010_readerC_diagram-label.png',[1060,510,1510,636]),
    'normalisations':('crops/143_scan010_readerC_normalisations.png',[595,728,1155,831]),
    'extension':('crops/143_scan010_readerC_extension.png',[324,1350,1240,1588]),
    'operations':('crops/143_scan010_main_operations.png',[220,1830,1590,2010]),
}

findings=[]
def finding(place,old,new,reason,confidence,crop,ac,ah,c,h,kind,consequential=False,marked=False,certainty=False,rows=None):
    assert old in before,(place,'before')
    assert new in candidate,(place,'after')
    assert c in C,(place,'C',c)
    assert h=='[no witness]' or h in H,(place,'H',h)
    path,box=crops[crop]
    findings.append(dict(place=place,before=old,after=new,reason=reason,confidence=confidence,crop=path,box=box,
                         against_C=ac,against_H=ah,C=c,H=h,kind=kind,consequential=consequential,
                         marked_in_H=marked,decision_updates=[],certainty_only=certainty,
                         accepted_difference_rows=rows or []))

finding('Upper oblique margin: continuation points after base',r'base\ldots',r'base..\unsure{.}.',
        'The reused rotated crop shows two dark compact points, a shorter soft-edged gray mark, and a final dark compact point after base. The gray mark is in the same continuation sequence and spacing, but is appreciably paler than the three dark points. It may be a faint writing point or a non-textual mark. The proposed text preserves the three secured points and marks only the intervening possible fourth point as uncertain; it does not assert four certain dots.',
        'low','upper-margin',True,True,r'des corps de base\ldots',r'\ill{} \ill{} \ill{}…','omission',marked=True,
        rows=[dict(row=5,place='Upper oblique margin, end of note',revision='Retain the recovered words; replace the unqualified three-dot encoding by three secured points plus the locally doubtful intervening point if main accepts this evidence.')])
finding('Lower oblique margin: raised letters in the abbreviation pts','relation entre pts de',r'relation entre p\textsuperscript{ts} de',
        'The p has a long descending stem. The compact ts group is written high to its right, above the line on which the following de rests. The proposed change preserves that raised abbreviation rather than expanding it. The accepted first-pass evidence already called these letters small raised ts, but the accepted fragment flattened them into baseline pts.',
        'medium','lower-margin',True,True,'relation entre pts de','\\ill{}\n\\ill{}','insertion or placement',marked=True,
        rows=[dict(row=13,place='Lower oblique margin, opening words',revision='The letter reading is retained; encode the raised ts described by the existing evidence.')])
finding('Final display, first map: argument inside the first pair of parentheses',r"\widetilde{\mathfrak X}'(I)\mathbin{-}I",r"\widetilde{\mathfrak X}'(\unsure{\Delta|I})\mathbin{-}I",
        'Inside the first pair of parentheses the small argument has an acute apex, two sides converging upward, and a low horizontal foot. Its left side is close to the opening parenthesis, which joins the low stroke. The visible outline favors a triangular Delta-like reading, while a compressed serifed I remains possible. The separate I in the codomain and the I in display (4) have distinct upper and lower horizontal bars. Delta is preferred from the visible apex and sides, at low confidence. I remains an alternative from the joined parenthesis/base and the same local set notation. No definite source slip is asserted; the preference concerns only this occurrence.',
        'low','final-maps',True,True,r"\widetilde X'(I)\mathbin{-}I",r"\widetilde{\mathfrak{X}}'(I) \to I",'misread symbol or index',consequential=True,certainty=False,
        rows=[dict(row=19,place='(5), first map',revision='The bare connector, tilde, and prime remain confirmed. Qualify the argument-I clause locally rather than lowering the certainty of the entire connector reading.')])

confirmed=[]
def confirm(place,text,ink,crop='page',category=None):
    path,box=('page',None) if crop=='page' else crops[crop]
    confirmed.append(dict(place=place,text=text,ink=ink,crop=path,box=box,error_sheet_category=category))

confirm('Top pagination',r'\mspage{5}','The pale upper-right numeral has the upper turn and lower curved body of 5. No writer identity is inferred.','page','digits and hand attribution')
confirm('Opening line',"d'où",'The d, apostrophe and short accented word are present; no extra punctuation follows.','page','words and accents')
confirm('Display (1), all objects',r"1\longrightarrow G'\longrightarrow\mathcal G'\longrightarrow\Gamma",'The first G has a compact round body, the second has a long looped descender, and both have distinct high primes. Gamma has a cap and one long upright, without a prime. The initial 1 is a single upright numeral.','page','symbols and indices')
confirm('Display (1), all three connectors','Three rightward arrows','The first two heads have obvious upper/lower branches. The last head is a compressed raised endpoint, distinct from the flat-ended strokes later on this same sheet.','page','arrows and decorations')
confirm('Line before diagram (2)','et un germe de relèvement','The short words et un, the long-descending g of germe, de, and the accented relèvement are present; no added sentence or stop is supplied.','page','complete prose line')
confirm('Diagram (2), all three objects and both arrows',r"\mathcal G'\to\Gamma;\quad\Gamma'\to\mathcal G'",'The G-prime is above-left, Gamma above-right, and Gamma-prime below-right. The horizontal arrow points right and the diagonal arrow points up-left. Both primes are separate high strokes.','page','diagram objects, directions and primes')
confirm('Diagram (2), vertical relation',r'\cup','The U-shaped sign is isolated between the two Gamma objects. Its left upright is longer than its right; there is no connecting shaft or arrowhead.','diagram-label','drawing geometry')
confirm('Diagram (2), short label','ss-gp ouvert','Two small connected s forms precede one hyphen. Only g and p follow before ouvert; there is no written continuation roupe. The label belongs inside the diagram.','diagram-label','abbreviations and placement')
confirm('Below diagram (2), H parenthetical sentence','No repeated separate sentence','The whole-page and half views show no second parenthesized Gamma-prime subset Gamma sentence below the diagram. H restates the drawn relation editorially.','page','text not on the page')
confirm('Upper margin, lexical content','pour mémoire : relation avec variations des corps de base','The rotated crop has the initial v and the extended -tions/-ons ending of variations, and readable des corps de base below. Both points of the colon after mémoire are distinct. M0662 remains the accepted other reading variations; the terminal continuation count is separately reported.','upper-margin','words, accents, punctuation and original MARKS')
confirm('Choisissons line',r'\uline{Choisissons} (cf normalisations plus bas)','Choisissons has a separate underline. The f of cf descends without a following dot. Normalisations ends in a separate hooked s after the long n-stroke; plus bas and both parentheses remain.','normalisations','underlining, abbreviation and plural ending')
confirm('Choice numeral',r'\textcircled{$\overline{\underline{\mathrm{III}}}$}','Three vertical numeral strokes are inside an oblique ellipse, with an independent short upper rule and lower rule. None is a replacement parenthesis.','page','drawing and numbering')
confirm('Cover choice and punctuation',r"\uline{un rev. universel} $\widetilde{\mathfrak X}'$ de $\mathfrak X'$,",'The underline runs below un rev. universel. A separate stop follows rev. The first looped X has a tilde and prime; the second has a prime but no tilde. A descending comma follows the second X.','page','abbreviation, underline, hats/primes and punctuation')
confirm('Short line and deletion before the identity',r"d'où \deleted{posons}",'The second d’où remains live. A horizontal strike passes through posons; the word is recoverable and is not omitted.','page','deletion state')
confirm('Fundamental-group identity',r"\pi_1(\mathfrak X')=\operatorname{Aut}(\widetilde{\mathfrak X}'/\mathfrak X')",'The pi has low 1, and the three X forms each have high primes. Only the numerator X carries a separate tilde. The two short equality bars, slash, Aut letters and paired parentheses are visible. No extra argument or index is added.','page','complete formula and each upper/lower mark')
confirm('Line after the fold','On trouve alors','The initial O is a loop, n follows, and trouve and alors are separately written. This is live prose, without a strike or insertion.','page','complete prose line')
confirm('Heading (3)',r"(3) \deleted{(3)} structure d'extension",'The live (3) lies farther left. A second parenthesized 3 survives beneath oblique crossing strokes before structure. The latter is a full word with two tall t strokes and continued low letters, not str. followed by a stop. The apostrophe in d’extension is separate.','extension','deletion, abbreviation and numbering')
confirm('Extension (3), objects and marks',r"1\longrightarrow\pi_1(\mathfrak X')\longrightarrow\unsure{\mathcal E|\Sigma}'\longrightarrow\mathcal G'\mathbin{-}1",'The initial and terminal 1s, low 1 on pi, X-prime, prime on the rounded extension glyph and prime on the long-descending G are present. The extension glyph has two open rounded turns; its alphabet remains the shared E/Sigma doubt.','extension','all symbols and indices')
confirm('Extension (3), four connector shapes','Three rightward heads, then a bare shaft','The first two right endpoints project beyond the shaft. The extension-letter-to-G connector ends in a small raised triangular head. The G-to-1 connector has a flat rounded stop without head branches.','extension','arrows and bare connectors')
confirm('Lower margin, wording',r"pour mémoire : relation entre pts de $\mathfrak X'(\overline{\mathbf Q})$ et scindages partiels de l'extension (3)\ldots",'The rotated crop supports all these words, the two-point colon, scindages with a long g descender, partiels with its final s, and de l’extension (3). Three continuation marks follow the final parenthesis; the first is elongated. The raised ts placement is a separate finding.','lower-margin','complete marginal text and suspension count')
confirm('Lower margin, mathematical expression',r"\mathfrak X'(\overline{\mathbf Q})",'A distinct high short prime stands between the looped X and opening parenthesis. The Q has a closed rounded body, a lower-right tail and a separate upper bar. The lower-right stroke belongs to Q, not an added comma.','lower-margin','prime, bar and letter structure')
confirm('Display (4), all contents',r"\unsure{\mathcal E|\Sigma}'\text{-ensembles};\quad\widetilde{\mathfrak X}'(I),\ \widetilde{\mathfrak X}'(J)",'The initial rounded group letter has a prime and one hyphen before ensembles. A left brace joins two rows. Each X has a distinct tilde and prime. I has upper and lower bars; J has a long right stem and lower turn. Both arguments have parentheses.','page','brace, two rows, all accents and arguments')
confirm('Operations line (5)',r"Opérations de E' sur I,J via G', et",'The small accent above the e of Opérations is visible. The first action letter has a prime. I and J are full-height arguments with a comma between them. The long-descending G has a separate prime and is followed by a comma; et finishes the line.','operations','accent, primes, comma and full prose')
confirm('Applications continuation',r"E'\text{-applications}",'The rounded group prefix repeats on the next line with a high prime, one hyphen, and the full word applications. No expansion or extra punctuation is supplied.','operations','operator prefix and spelling')
confirm('Final brace and both connector strokes','Two-row left brace; two headless horizontal connectors','The upper and lower strokes have rounded or flat stopping ends without head branches. The left brace has one central inward cusp and joins the two rows. The tiny disconnected points above the lower connector do not supply a letter or arrowhead.','final-maps','diagram geometry and non-textual points')
confirm('Final first map, secured features',r"\widetilde{\mathfrak X}'(I)\mathbin{-}I",'The X has a distinct upper tilde and high prime. The separate codomain I has a top bar, descending stem and low foot. The connector is bare. The argument inside the first parentheses is separately qualified as I/Delta.','final-maps','tilde, prime, codomain and connector')
confirm('Final second map and quotient',r"\widetilde{\mathfrak X}'(J)\mathbin{-}J\simeq\widetilde{\mathfrak X}'(J)/\pi_1",'Both X occurrences have high primes and separate tildes. All three J forms have the same upper turn/right stem/lower return. The comparison sign is one upper wave over one straight lower bar, followed by the quotient slash and pi with a low single 1. There is no argument after the final pi_1.','final-maps','every argument, comparison sign and index')
confirm('Bottom pagination',r'\mspage{9}','The pale lower-left numeral has a small upper loop and curved descender. It is retained as 9; the pencil hand is unnamed.','page','digits and hand attribution')

remaining=[
    dict(place='The extension/action-group glyph, four occurrences in (3), (4), and twice in (5)',reading=r"\unsure{\mathcal E|\Sigma}'",
         alternatives='calligraphic E / capital Sigma, each primed',confidence='low',
         reason='Each occurrence has the same rounded double-turn form and a distinct prime. Local rounding favors E but does not uniquely identify the alphabet. The shared uncertainty remains; no new source distinction is introduced.',
         existing_remaining_doubt='The extension/action-group glyph, four occurrences in (3), (4), and twice in (5)',status='retained; confidence aligned to current shared notation',
         crops=[crops['extension'][0],crops['operations'][0]],box=None),
    dict(place='Upper margin: possible fourth continuation point',reading=r'base..\unsure{.}.',alternatives='four writing points / three writing points with an intervening non-textual mark',confidence='low',
         reason='Three compact dark points are secured. The intervening gray short mark is aligned but paler, so its status is retained as a local doubt rather than a definite fourth dot.',
         crop=crops['upper-margin'][0],box=crops['upper-margin'][1],status='new local doubt'),
    dict(place='First final-map argument',reading=r'\unsure{\Delta|I}',alternatives='triangular Delta-like graph / compressed I',confidence='low',
         reason='An acute apex and converging sides differ from the separately barred I elsewhere on the same page; the opening parenthesis touches the low stroke. The visible triangular outline favors Delta at low confidence; I remains possible from the local notation and joined parenthesis, without declaring a definite source slip.',
         crop=crops['final-maps'][0],box=crops['final-maps'][1],status='new local symbol alternative, Delta preferred from the visible outline'),
]

report=dict(
    key='143_scan010',reader='A',stage='second reading',first_reader='C',
    image_views=['original','half1','half2']+[crops[k][0] for k in crops],
    findings=findings,confirmed=confirmed,remaining_doubts=remaining,
    notes=[
        dict(id='143_scan010-auditA-N1',text='The complete original was viewed once, followed by both existing native halves once each. Every prose line, display, marginal line, deletion, rule, brace, arrow and numbered object was checked against the accepted text and both witnesses. Seven existing crops were reused; no new crop or enlarged half was made.'),
        dict(id='143_scan010-auditA-N2',text='The page writes the extension and lift diagram, chooses a universal covering object, gives a fundamental-group automorphism identity, then writes another extension, actions on I and J, and two final connector expressions. These are source statements, not assertions independently proved by this audit.'),
        dict(id='143_scan010-auditA-N3',text='The three findings are local: a possible extra suspension point, raised abbreviation letters, and a qualification of one argument glyph. The deletion states posons and the duplicate (3), the full word structure, the ss-gp abbreviation, the circled/ruled III, and all accepted arrow-versus-bar distinctions are confirmed.'),
        dict(id='143_scan010-auditA-N4',text='M0662 remains resolved as variations, with medium confidence. Its initial v and the prolonged -tions/-ons ending are visible in the existing rotated crop. No original MARKS decision is changed by this audit.'),
        dict(id='143_scan010-auditA-N5',text='The existing E/Sigma remaining-doubt entry is retained rather than removed. Its alphabet confidence is low under the current shared notation. Accepted pure-alphabet difference rows 17 and 18 use medium confidence; these should be aligned to low if main updates report metadata. Mixed rows 12 and 16 contain independently secured arrows/accents as well as the alphabet doubt and should not have all evidence weakened indiscriminately.'),
        dict(id='143_scan010-auditA-N6',text='No source text is proposed for the isolated tiny points above the lower final connector: they do not form a supported label or punctuation in that position. The possible upper-margin fourth point is treated differently because it lies within an explicit continuation sequence, but its paler color is kept as a doubt.'),
        dict(id='143_scan010-auditA-N7',text='The two pencil pagination numerals are retained without attribution. No other page image, packet or report was inspected in this second-reading assignment.'),
    ],
    check_events=[
        dict(statement_id='143_scan010-fundamental-identity',type='carried as background without fault found',outcome='The written pi_1 = Aut identity was transcribed and its visible primes, tilde, slash and low index checked. No covering-space argument or independent proof was performed.'),
        dict(statement_id='143_scan010-extensions-and-lift',type='carried as background without fault found',outcome='The displayed group labels and drawn links were read without inferring exactness or adding heads from their expected mathematical role.'),
        dict(statement_id='143_scan010-final-I-J-notation',type='carried as background without fault found',outcome='The common I/J labels on the same sheet were used to retain I as an alternative at the compressed argument. The preferred Delta follows the visible triangular outline, not a mathematical repair. The quotient statement was not independently checked.'),
    ],
    hand_log=[
        dict(habit='Compact arrowheads can be reduced to one raised triangular shoulder.',places='Last arrow of (1), horizontal arrow of (2), and middle link from the extension glyph to G in (3).',scope='Each endpoint inspected; the final link of (3) and both last maps remain genuinely bare.',misreadings='No change from accepted text; the distinction is independently confirmed.'),
        dict(habit='The letters ts in the points abbreviation sit high after the descending p.',places='Lower oblique margin, pts de.',scope='One occurrence in this page audit; proposed raised encoding is medium confidence.',misreadings='Accepted text and C flatten the letters, although accepted row13 already describes raised ts; H leaves the opening unread.'),
        dict(habit='Continuation marks can vary in darkness and elongation.',places='Upper-margin ending after base and lower-margin ending after (3).',scope='Upper ending has three secured dark points and one paler aligned candidate; lower ending has three marks, the first elongated.',misreadings='A conventional ldots can conceal a fourth possible point; the doubtful mark must not be promoted to certain source ink.'),
        dict(habit='One compressed argument I has a triangular, apex-like outline and touches the opening-parenthesis stroke.',places='First map in the final two-row display.',scope='One local occurrence only; the I in display (4), operations line and codomain is separately barred.',misreadings='Both witnesses and accepted text give I without qualification. Delta is the preferred visible form at low confidence, with compressed I explicit as an alternative; no definite new mathematical symbol or authorial slip is asserted.'),
        dict(habit='The recurring rounded extension/action glyph admits E and Sigma.',places='(3), (4), and both prefixes in (5).',scope='All four occurrences individually inspected; each carries a high prime.',misreadings='Current shared preferred E plus explicit Sigma alternative is retained, with low alphabet confidence.'),
        dict(habit='The looped X varies in how fully its upper loop closes.',places='Cover choice, identity, extension, lower margin, display (4), and final maps.',scope='All twelve occurrences checked; all twelve primes and seven tildes retained in their actual positions.',misreadings='No new alphabet distinction is inferred from the more open X in the last quotient.'),
    ],
    inventory_additions=[],
    inventory_checked=[dict(element=e['element'],position=e['position'],status='checked against original/halves; relevant crop where listed in confirmed') for e in accepted_report['inventory']],
    decision_checks=[dict(id='M0662',accepted_decision='other',accepted_reading='variations',audit_result='confirmed',confidence='medium',crop=crops['upper-margin'][0],box=crops['upper-margin'][1])],
    report_adjustments=[
        dict(target='remaining_doubts: extension/action-group glyph',before_confidence='medium',after_confidence='low',reason='The current shared notation treats this unresolved alphabet identification consistently as low confidence. The proposed fragment itself is unchanged at all four occurrences.'),
        dict(target='accepted changes rows 17 and 18: pure acting-letter E/Sigma rows',before_confidence='medium',after_confidence='low',reason='These rows concern only the still-open alphabet, with preferred E, against_C=false, against_H=true, consequential=false. Mixed rows 12 and16 contain other evidence and are not blanket downgraded.'),
    ],
    mark_inventory=dict(X_occurrences=12,X_primes=12,X_tildes=7,plain_G_primes=1,calligraphic_G_primes=4,extension_glyph_primes=4,Gamma_primes=1,pi_low_1_occurrences=3,Q_overbars=1,
                        note='Counts are a supplement to the locus-specific checks, not a substitute for them. The first final-map argument remains locally qualified.'),
    workflow=dict(original_view_count=1,native_half_view_counts=[1,1],reused_crop_count=len(crops),new_crop_count=0,
                  reused_crops=[dict(path=p,box=b) for p,b in crops.values()],other_page_material_opened=False,ocr=False,external_research=False,tex_compilation=False,accepted_files_modified=False),
)

for f in findings:
    assert all(d.get('id') in {m['id'] for m in packet['marks']} for d in f['decision_updates'])
for path,box in crops.values(): assert (WORK/path).exists()
assert len(confirmed)==28
assert len(report['inventory_checked'])==21
assert all(f['before'] in before and f['after'] in candidate for f in findings)
tex_path=WORK/'reviews/143_scan010_auditA.tex'
json_path=WORK/'reviews/143_scan010_auditA.json'
tex_path.write_text(candidate)
json_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(candidate=str(tex_path),report=str(json_path),findings=len(findings),confirmed=len(confirmed),reused_crops=len(crops),new_crops=0),ensure_ascii=False))
