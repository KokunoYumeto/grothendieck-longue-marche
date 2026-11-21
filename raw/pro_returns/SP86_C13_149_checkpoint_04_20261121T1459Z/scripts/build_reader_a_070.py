from pathlib import Path
import json
base=Path('/workspace/scratch/9d0bd22e5d3a')
out=base/'work/SP86_C13_149/readings'
manifest=json.loads((out/'149_scan070_crop_manifest.json').read_text())
crops={v['id']:v for v in manifest}
tex=(base/'packets/149_scan070/C.tex').read_text()
tex=tex.replace(r'\unsure{\overline m|\overset{m}{=}}',r'\overline m')
tex=tex.replace(r'E_{U_{\unsure{\eta|K}}}-E_{U_S}',r'E_{U_K}\unsure{-|\longrightarrow}E_{U_S}')
tex=tex.replace(r'E_K\longrightarrow E_S',r'E_K\twoheadrightarrow E_S')
tex=tex.replace('partout défini i.e.',r'partout \unsure{défini|defini} i.e.')
tex=tex.replace(r'\unsure{section}','section')
(out/'149_scan070.tex').write_text(tex)
R=dict(page='149_scan070',scan=70,reader='reader_a',line_count=18,changes=[],decisions=[],inventory=[],doubts=[],notes=[],check_events=[],hand=[],notation=[],abbreviations=[],audit_boxes=[],diff_coverage=[],deletion_insertion_review=[],open_issues=[],viewed=['page','top half','bottom half']+[v['path'] for v in manifest])
def change(id,p,place,C,H,final,evidence,confidence,ac,ah,kind,category,marked=False,consequential=False):
    R['changes'].append(dict(id=id,place=place,C=C,H=H,final=final,evidence=evidence,crop=crops[p]['path'],box=crops[p]['box'],confidence=confidence,against_C=ac,against_H=ah,kind=kind,error_category=category,marked_in_H=marked,consequential=consequential))
change('P01a','P01','main line 1, schém. relatif','schém.','schéma','schém.',
'The short word has s, a low c, tall h, a low e with a detached accent, then the compressed m body and a separate dark stop. There is no final a after that m. The abbreviation and its stop are preserved.',
'high',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised')
change('P01b','P01','main lines 1 and 9–18, U forms; representative opening equality',r'U=U_S; U and indexed U throughout',r'\mathcal{U}=\mathcal{U}_S; \mathcal{U} throughout',r'U=U_S; U and indexed U throughout',
'The opening capitals have open entry strokes, a broad lower turn, and an ascending right stroke; neither has a closed upper-left loop. The same open form was inspected in the main text and P06/P09/P10/P12/P15/P16. Plain U preserves the locally observed alphabet. The established plain-E rendering is treated separately and is not counted in this row.',
'high',False,True,'misread symbol or index','Symbols and indices')
quote=chr(96)*2+"élémentaire''"
change('P02','P02','main line 2, quotation strokes around élémentaire',quote,'« élémentaire »',quote,
'Two short raised strokes open the word and two short raised strokes close it. They are preserved by the double-backtick/double-apostrophe convention. The following source dash is one horizontal stroke; two versus three TeX hyphens in C/H are excluded from the material count.',
'high',False,True,'misread symbol or index','Other')
change('P03','P03','main line 5, lui- shorthand (M1189)',r'lui-$\unsure{\overline m|\overset{m}{=}}$','lui-même',r'lui-$\overline m$',
'After lui- the lower body makes a low curved bowl, an interior upward cusp, and a long flattened right tail. That compressed m shape is comparable with the terminal m in schém. (P01) and hom (P08). A separate horizontal bar lies above it. The crop supplies the bar and m body, with no additional equals-sign level. M1189 resolves to its first reading; H expands the abbreviation.',
'medium',True,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised')
change('P07','P07','between main lines 12 and 13, nested words after composé de',r'\inserted{(composé de \inserted{la section} ...)}',r"un relèvement \add{\uncertain{de section}} de l'hom.; \add{(composé de ...)}",r'\inserted{(composé de \inserted{la section} ...)}',
"The small phrase begins with a tall looped l and a closed a, followed by s-e-c-t-i-o-n. Its thin attachment descends into the gap after composé de and before the first E_K. The de in the main line above independently belongs to un relèvement de l'hom. The small phrase is retained at its physical nested attachment, with la rather than H's de.",
'high',False,True,'insertion or placement','Insertions put in the wrong place',True)
change('P08','P08',"main line 12, l'hom surjectif","l'hom","l'hom.","l'hom",
"The crop shows tall l, detached apostrophe, tall h, rounded o, and compressed terminal m. Its last stroke runs right and turns down slightly. There is a clear gap before surjectif and no separate stop in that gap.",
'high',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised')
change('P09','P09','first relation in parenthetical insertion, connector',r'E_K-E_{U_{\unsure{\eta|K}}}',r'\mathcal{E}_K\to\mathcal{E}_{\mathcal{U}_K}',r'E_K-E_{U_{\unsure{\eta|K}}}',
"Between the complete left E_K and right indexed E there is one short horizontal stroke. Its right cap turns down, without a separately visible upper/lower pair of arrowhead wings. The diagonal above the left E belongs to the nested insertion attachment; the long line underneath is the outer insertion leader. C's unheaded connector is retained. The nested index remains independently eta/K and is not counted as an established H error.",
'high',False,True,'misread symbol or index','Symbols and indices',False,True)
change('P10','P10','second inserted relation, left nested index (M1192)',r'E_{U_{\unsure{\eta|K}}}',r'\mathcal{E}_{\mathcal{U}_K}',r'E_{U_K}',
'The small index beneath the left U has an upright component, a diagonal upper branch rising right, and a separately descending lower branch. The split remains visible under the nearby prose descender and decides K. The whole expression was read, including ordinary U, right E_{U_S}, closing parenthesis, and the independent connector uncertainty.',
'high',True,False,'misread symbol or index','Symbols and indices',False,True)
change('P11','P11','main line 13, complete first E_K to E_S relation',r'E_K\longrightarrow E_S',r'\mathcal{E}_K\to\mathcal{E}_S',r'E_K\twoheadrightarrow E_S',
'The horizontal shaft terminates in a small pointed wedge with upper and lower returns. A larger detached > lies immediately to its right. P16 supplies the local comparison: its shaft end is elongated and rounded, followed by one detached head. Both objects and indices are read in this crop. Root and reader agree on two heads at medium confidence.',
'medium',True,True,'misread symbol or index','Symbols and indices',False,True)
change('P13','P13','main line 14, final word and following space','défini','définie,',r'\unsure{défini|defini}',
'The body ends in n followed by dotted i and its short low terminal stroke. The space to the right supplies neither another e body nor a comma. These ending and punctuation departures from H are high confidence. The e is flattened, and the faint marks above it do not isolate a confidently detached accent: that separate accent uncertainty is retained in place and is uncounted against C.',
'high',False,True,'misread word','Words')
change('P14a','P14','main line 15, live section (M1193)',r'\unsure{section}',r'\uncertain{section}','section',
'The live word shows sinuous s, joined low e and c, tall crossed t, dotted i, rounded o, and trailing n. The cancellation starts after this word. The long thin descender entering from above belongs to the preceding line and does not cancel section. The readable live word resolves M1193.',
'high',True,True,'other','Words',True)
change('P14b','P14','main line 15, canceled material after live section',r'section \deleted{\unsure{rationnelle}}',r'\struck{\uncertain{section partout définie}} \uncertain{section}',r'section \deleted{\unsure{rationnelle}}',
"The heavy cancellation crosses one compact word cluster after live section. Short initial curves, internal uprights and low final strokes remain, but the heavy horizontal and retraced ink obscures the complete sequence. C's rationnelle remains doubtful; the crop does not supply three separated canceled words section partout définie. The live-before-canceled order and strike scope are clear.",
'medium',False,True,'deletion state','Struck text',True)
change('P17','P17','thin bottom-left foliation',r'\margin{69}','(nothing)',r'\margin{69}',
'The left digit has a long upper entry descending into a closed lower loop, giving 6. The right digit has a closed upper loop and descending curved stem, giving 9. The small thin inscription is in another hand and is preserved as a margin number.',
'high',False,True,'omission','Omissions')
def decision(id,dec,reading,evidence,p,confidence):
    c=crops[p]
    R['decisions'].append(dict(id=id,cote='149',scan='70',decision=dec,reading=reading,evidence=evidence,crop=c['path']+' ('+','.join(map(str,c['box']))+')',confidence=confidence))
decision('M1189','first',r'\overline m','Separate upper bar over a compressed lower m with low bowl, interior cusp and flat tail; compare local m at P01/P08. No third horizontal level is supplied.','P03','medium')
decision('M1190','undecided',r'\unsure{\eta|K}','The whole E_U expression is visible. The nested index has a left upright, joined rising diagonal and right descending hook. Its connected outline permits eta, while closed-angle K in secure E_K at P09/P11 prevents resolution.','P06','medium')
decision('M1191','undecided',r'\unsure{\eta|K}','The first inserted relation is read in full. Its right nested index is joined and eta-like; the left E_K in the same crop also uses a closed joined K. The leader crosses below the small index. These strokes leave eta/K unresolved.','P09','medium')
decision('M1192','alternative','K','The left nested index in the second inserted relation has a discernible upper diagonal and separate lower branch at its upright. The split decides K; the obscured connector is an independent local doubt.','P10','high')
decision('M1193','first','section','All seven letter bodies are readable in the live word. The heavy strike begins only after the trailing n. The stroke entering from above is a descender.','P14','high')
decision('M1194','undecided',r'\unsure{\eta|K}','The left nested index is joined and eta-like; adjacent right E_K has a clear upper diagonal and separate lower branch. P11 nevertheless shows secure joined K. The locally varying outlines leave this index unresolved.','P15','medium')
def inv(id,kind,pos,first,hand='his hand'):
    R['inventory'].append(dict(element=id,kind=kind,position=pos,first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes'))
inv('E01','text','18 main lines, approximately x=285–1665, y=80–2335','Reprenons le cas de U=U_S')
inv('E02','insertion','above main line 9; P05 (900,1000,1105,1140)','f')
inv('E03','insertion','between main lines 12 and 13, x=650–1665, y=1440–1680; leader to after main E_K→E_{U_S}',r'(composé de ... E_K-E_{U_{\unsure{\eta|K}}} avec E_{U_K}\unsure{-|\longrightarrow}E_{U_S})')
inv('E04','insertion','small nested phrase above the opening of E03; P07','la section')
inv('E05','deletion','main line 15, after live section; P14',r'\unsure{rationnelle}')
inv('E06','margin note','bottom-left corner; P17 (20,2280,82,2345)','69','another hand')
def doubt(place,reading,alts,confidence,reason):
    R['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence=confidence,reason=reason))
doubt('main line 10, nested index (M1190; P06)',r'\unsure{\eta|K}',r'\eta | K','medium','Connected outline permits eta; secure closed-angle K in P09/P11 supplies the competing local letter form. No mathematical identification is used to choose.')
doubt('first inserted relation, right nested index (M1191; P09)',r'\unsure{\eta|K}',r'\eta | K','medium','The same crop contains secure left E_K with joined outline; the right small index and crossing leader do not settle the alternatives.')
doubt('second inserted relation, connector (P10)',r'\unsure{-|\longrightarrow}',r'- | \longrightarrow','medium','A short horizontal endpoint turns down, but the long prose descender merges with the region where an upper wing would have to be separated. K is resolved independently. This is uncertainty only; neither witness connector is counted as an established error here.')
doubt('main line 14, accent in final word (P13)',r'\unsure{défini|defini}','défini | defini','medium','Letter bodies and absence of final e/comma are readable. Above flattened e, no dark detached accent can be isolated from faint surrounding marks. This added accent uncertainty is uncounted against C.')
doubt('main line 15, canceled word (P14)',r'\deleted{\unsure{rationnelle}}','rationnelle; remaining letter sequence obscured','low','The thick cancellation hides enough bodies that rationnelle cannot be resolved. The live section and single canceled cluster are secure. This nested doubt has no supplied MARKS ID and is absent from decisions[].')
doubt('main line 16, nested index before sur E_K (M1194; P15)',r'\unsure{\eta|K}',r'\eta | K','medium','Adjacent E_K is split while the nested index is joined. Secure joined K at P11 prevents resolution from that local comparison.')
R['notes']=[
"070-S1 — Source description: the opening resumes U=U_S, written as a schém. relatif sur S, with the qualifications “s'il le faut” and “pour fixer les idées”. The passage names K as corps de fonctions and refers to diagramme 5. These are transcribed source statements, without an external identification or proof check.",
"070-S2 — Source objective: after introducing inserted f and the section expressions, the author writes “Je veux montrer que”. The ensuing source sentence compares its section expressions and begins an annulment condition. This leaf ends at “s'annule sur”; no continuation is supplied.",
"All 18 physical main lines were read against both witnesses on the native halves, including agreed words, accents, apostrophes, punctuation, signs, brackets and indices. The autograph head is unnumbered. The only marginal number is thin 69 in another hand.",
"The whole page and each native half were viewed once. Seventeen first-pass crops were saved once. Existing unresolved P10/P11/P13 displays were revisited for final graphical comparisons; no second crop was made.",
"The recurring two-lobed E is represented by plain E under the supplied notation convention. H's mathcal E wrapper alone contributes no material error. U forms were compared locally and retained as open ordinary U.",
"The long outer leader runs beneath the inserted formulas and attaches after the second main relation. A small separate point after the closing parenthesis supplies the period before Je. No second stop is supplied at the leader endpoint.",
"The three retained eta/K marks record local uncertainty. H's K remains within their alternatives, so those token-diff rows are not counted as established H errors. The two prose-dash TeX length differences are also excluded.",
"Root reviewed all seventeen crops and agreed on barred m, K at M1192, live section, double head at P11, and remaining narrow connector/accent doubts. No mathematical use, proof or refutation was performed; check_events is empty."
]
def hand(form,obs,places,scope,errors):
    R['hand'].append(dict(form=form,observation=obs,places=places,scope=scope,witness_errors=errors))
hand('compressed m and barred-m shorthand','The m can reduce to a low bowl, an interior cusp and extended flat tail. In lui- a separate stroke lies above that body.','P01 schém.; P03 lui-shorthand; P08 hom','These three local forms; no abbreviation expansion in source text.','H expands schém. and the barred-m shorthand; M1189 resolves to first.')
hand('joined or split K','Secure E_K includes a closed joined angle at P09/P11 and clearer split branches at P12/P15/P16. Tiny nested K at P10 has a separate lower branch. Joined eta-like indices at P06/P09/P15 remain doubtful.','P06, P09–P12, P15–P16','Every disputed index and locally secure K was compared; no uniform replacement of all four nested indices.','M1192 resolves to K. M1190/M1191/M1194 remain undecided; H is not charged with an established error there.')
hand('two-lobed E','Two broad curved lobes, middle turn and lower terminal stroke are rendered plain E under the supplied recurring-sign convention.','P06, P09–P12, P15–P16 and agreed body occurrences','All observed E on this page.','H mathcal E rendering alone excluded.')
hand('ordinary open U','The entry and lower bowl remain open; no closed upper-left loop. Size decreases in nested indices without an observed alphabet change.','opening equality, main line 9, P06/P09/P10/P12/P15/P16, remaining body U','All U forms on this leaf visually inspected.','H uses mathcal U wrappers; retained plain U, represented by P01 comparison.')
hand('arrowhead and thick shaft end','P11 has a pointed shaft-end wedge with paired returns plus a larger detached head. P16 has a rounded elongated cap plus one detached head; P12 has one head. P10 remains overlapped.','P09–P12, P16','Each relation inspected separately at both ends.','Both witnesses give only one head at P11. H supplies an arrow at P09; P10 is undecided.')
hand('leaders, descenders, cancellation','f leader enters after rationnelle. la section leader enters after composé de. Outer leader attaches after second main relation. P14 upper descender crosses by the live word; heavy strike begins in the following cluster.','P05/P07/P09/P10/P12/P14','Physically traced strokes on this leaf.','H misreads and relocates la section and gives an incorrect canceled phrase/order.')
hand('accent over flattened e','The e in final défini is low; marks above it are too faint to isolate a detached accent. Terminal dotted i and following blank are secure.','P13','This occurrence only.','H supplies final e/comma; new accent doubt uncounted against C.')
hand('thin foliation 69','6 has lower loop and long entry; 9 has upper loop and descending tail.','P17','Another hand, separate from the main autograph.','H omits the foliation.')
R['notation']=[
dict(form=r'U=U_S',meaning='Equality explicitly written in the opening description of a schém. relatif sur S.',places='main line 1'),
dict(form='K',meaning='Named corps de fonctions by the source.',places='main lines 6–7'),
dict(form='f',meaning="Inserted letter naming the source's section rationnelle de U sur S.",places='above main line 9; reused in main line 14'),
dict(form=r'\mathbb{Q}',meaning='The Q after lisse sur has a separate internal diagonal disconnected from its lower-right tail.',places='main line 6, P04'),
dict(form=r'E_K\twoheadrightarrow E_S',meaning='Relation called hom surjectif in the source; two heads transcribed from the visible wedge and detached larger head.',places='main lines 12–13, P11'),
dict(form=r'E_{U_{\unsure{\eta|K}}}',meaning='Nested expression in three positions; local index forms leave eta/K unresolved.',places='main lines 10/16; first inserted relation'),
dict(form=r'E_{U_K}\unsure{-|\longrightarrow}E_{U_S}',meaning='Second inserted relation; K is legible and connector is partly overlapped.',places='P10')
]
R['abbreviations']=[
dict(written='schém.',expansion='schéma',places='main line 1, P01; expansion here only'),
dict(written=r'\overline m',expansion='même',places='lui- shorthand, main line 5, P03'),
dict(written='hom',expansion='homomorphisme',places='main line 12, P08; no stop supplied'),
dict(written='i.e.',expansion='id est',places='main lines 15/17; source short form retained'),
dict(written='ssi',expansion='si et seulement si',places='main lines 16/17; source short form retained')
]
def audit(id,kind,coords,reading):
    R['audit_boxes'].append(dict(box=id,kind=kind,coords=coords,reading=reading))
audit('B01','C/H word disagreement',crops['P01']['box'],r'$U=U_S$ schém.')
audit('B02','C/H word disagreement',crops['P02']['box'],quote+r' sur $S$ --')
audit('B03','lower confidence departure',crops['P03']['box'],r'lui-$\overline m$')
audit('B04','handwritten number',[850,425,1045,540],r'$\pi_1$')
audit('B05','handwritten number',[705,918,805,1000],'5.')
audit('B06','insertion',crops['P05']['box'],r'\inserted{$f$}')
audit('B07','formula with doubt',crops['P06']['box'],r'$E_{U_{\unsure{\eta|K}}}$')
audit('B08','insertion',crops['P07']['box'],r'\inserted{la section}')
audit('B09','insertion',[650,1440,1665,1680],r'\inserted{(composé de \inserted{la section} $E_K-E_{U_{\unsure{\eta|K}}}$ avec $E_{U_K}\unsure{-|\longrightarrow}E_{U_S}$)}.')
audit('B10','C/H word disagreement',crops['P08']['box'],"l'hom")
audit('B11','formula with doubt',crops['P09']['box'],r'$E_K-E_{U_{\unsure{\eta|K}}}$')
audit('B12','formula with doubt',crops['P10']['box'],r'$E_{U_K}\unsure{-|\longrightarrow}E_{U_S}$')
audit('B13','lower confidence departure',crops['P11']['box'],r'$E_K\twoheadrightarrow E_S$')
audit('B14','C/H word disagreement',crops['P13']['box'],r'\unsure{défini|defini}')
audit('B15','struck passage',crops['P14']['box'],r'section \deleted{\unsure{rationnelle}}')
audit('B16','formula with doubt',crops['P15']['box'],r'$E_{U_{\unsure{\eta|K}}}$ sur $E_K$')
audit('B17','margin note',crops['P17']['box'],r'\margin{69}')
coverage=[
('editorial page marker',"70 belongs to C's scanpage wrapper, not source ink."),
('material; P01a','Source schém. has abbreviation stop; H expands it.'),
('material; P02','Paired quotation strokes; no drawn guillemets.'),
('equivalent typography','One source prose dash, rendered by two versus three TeX hyphens.'),
('material; P03','Barred m; C choice resolves to first, H expands it.'),
('certainty only',"M1190 retains eta/K; H's K is within the alternatives."),
('equivalent typography','Second prose dash is one source stroke; TeX dash length explains extra token.'),
('material; P07','Small phrase is la section with leader after composé de, not after un relèvement.'),
('material; P08','No stop after hom.'),
('material; P07','Same nested la section belongs inside the parenthetical insertion.'),
('material; P09','First inserted connector has one unheaded stroke, no separate paired wings.'),
('certainty only','M1191 retains eta/K; local joined K comparison prevents resolution.'),
('material; P10','M1192 resolves to K from its split branches.'),
('certainty only','Second inserted connector retains dash/arrow alternatives under prose descender.'),
('material; P13','No final e/comma. New accent uncertainty alone is uncounted against C.'),
('material; P14a/P14b','Live section before one canceled cluster; rationnelle remains marked. H canceled phrase/order differ.'),
('certainty only','M1194 retains eta/K; joined and split secure K forms are both visible locally.'),
('material; P17','Thin foliation 69 is preserved as a margin number in another hand.')
]
R['diff_coverage']=[dict(row=i+1,status=s,reason=r) for i,(s,r) in enumerate(coverage)]
R['deletion_insertion_review']=[
'C insertion f: long stem, cross-stroke and hooked entry/exit; distinct curved leader descends between rationnelle and de U. Scope is one letter; P05/B06.',
'C outer insertion: independent opening/closing parentheses enclose composé de ... avec ... . The thin long leader passes beneath the formulas and attaches after main E_K→E_{U_S}. The period follows the inserted parenthesis. Scope retained in full; P07/P09/P10/P12/B09.',
"C nested la section: small phrase lies above the outer opening; its leader enters after composé de, before E_K. Both words retain inserted status there; P07/B08. H's de section after un relèvement differs from the observed letters and attachment.",
'C deletion rationnelle: heavy strike begins after live section and crosses the next compact cluster. The upper descender does not delete section. rationnelle remains unsure because letter bodies are hidden; P14/B15. The nested doubt has no supplied MARKS ID.'
]
R['open_issues']=[
'M1190/P06: joined nested index remains eta/K.',
'M1191/P09: first inserted right nested index remains eta/K.',
'P10: connector remains dash/arrow under prose descender; M1192 K resolved separately.',
'P13: accent remains défini/defini; final e/comma absent.',
'P14: canceled rationnelle tentative; live section and strike scope settled.',
'M1194/P15: last joined nested index remains eta/K.'
]
(out/'149_scan070.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=R['page'],changes=len(R['changes']),decisions=len(R['decisions']),crops=len(manifest),audit_boxes=len(R['audit_boxes']),open_issues=len(R['open_issues']),against_C=sum(x['against_C'] for x in R['changes']),against_H=sum(x['against_H'] for x in R['changes'])),ensure_ascii=False))

