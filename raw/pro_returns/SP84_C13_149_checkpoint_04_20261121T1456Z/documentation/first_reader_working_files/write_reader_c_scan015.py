from pathlib import Path
import json
root=Path('/workspace/scratch/4644e52611c0')
boxes=json.loads((root/'work/reader_c_scan015_boxes.json').read_text())
z=r'\unsure{Z|\mathcal Z}'
le=r'\unsure{\deleted{son}le|le}'
groupoid=r'\Pi_{\deleted{\bar K/}\unsure{K|\deleted{K}}}'
parenthesis=r'(\unsure{ou le|où le} topos $B_K$)'
tex=r'''\scanpage{15}
\mspage{7}
voir que $\operatorname{Centr}_{\pi}(\pi')=\{1\}$, i.e. le

\uline{Corollaire} Soit $\pi$ un groupe profini, extension successive de groupes profinis libres. Alors le centralisateur \inserted{$ZFORM$ dans $\pi$} de tout sous-groupe ouvert $\pi'$ de $\pi$ est réduit à $\{1\}$.

Par dévissage on est ramené au cas d'un groupe \inserted{profini} \uline{libre}. \inserted{On sait que $\pi'$ est donc libre.} OPS $\pi'$ invariant, et on admet que LEFORM centre d'un groupe profini libre est réduit à $1$.
\margin{à vérifier}
Donc $ZFORM\longrightarrow\pi/\pi'$ est injectif, donc $ZFORM$ est fini, et on admet que dans un groupe profini libre, il n'y a pas d'élément d'ordre fini $\neq1$ \margin{à vérifier} --- ce qui achève la démonstration.

\uline{Scholie} Le fait que $E_{\bar K/K}$ soit \deleted{\unsure{sans}}\inserted{à} \deleted{\unsure{torsion|tors.}}\inserted{centre} trivial peut s'exploiter, en disant que le groupoïde $GROUPOID$ \inserted{PARENTHESIS} est connu à équivalence près, \deleted{\unsure{que l'on|question}}\inserted{défini à isom} unique près, quand on connaît le groupe \uline{extérieur} associé à $E_{\bar K/K}$. Les hom
\margin{14}
'''.replace('ZFORM',z).replace('LEFORM',le).replace('GROUPOID',groupoid).replace('PARENTHESIS',parenthesis)
(root/'edition/reviews/149_scan015.tex').write_text(tex,encoding='utf-8')

def crop(n):return f'crops/149_scan015_{n}.png'
def change(id,place,C,H,final,evidence,n,confidence,against_C,against_H,kind,category,marked=False,mathematical=False):
    return dict(id=id,place=place,C=C,H=H,final=final,evidence=evidence,crop=crop(n),box=boxes[n],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=category,marked_in_H=marked,mathematical=mathematical)
changes=[
 change('c01','L8, between que and centre',r'\unsure{le|son}',r'\struck{?} le',le,'The tall loop of l and a low e-like continuation are visible. Additional crowded ink remains at the left and baseline of that live le. A short s-like curve can be distinguished, but a complete underlying son cannot be read letter by letter. The proposed first branch records a possible overwritten son and the second branch leaves le alone; the correction state and underlying word remain explicitly uncertain. There is no securely isolated source question mark.','c02','low',True,True,'deletion state','Struck text',marked=True),
 change('c02','Second left marginal note, beside L13',r'\margin{à vérifier} after achève la démonstration',r'\marginal{à vérifier} after \neq1',r'\neq1\ \margin{à vérifier}\ --- ce qui achève la démonstration','The note occupies the left margin opposite the line élément d’ordre fini ≠1 — ce qui, with a diagonal baseline. Its à, accent, v, accented e, tall descending f and final low run are readable. It is associated with the order-finite assertion before the concluding clause, rather than attached after démonstration.','c06','high',True,False,'insertion or placement','Insertions put in the wrong place',mathematical=True),
 change('c03','L16, cancelled word replaced above by centre',r'\deleted{\unsure{torsion|tors.}}',r'\struck{\ill{}}',r'\deleted{\unsure{torsion|tors.}}','The cancelled run has an initial tall t, an o-like oval and short r/s-like forms. Later low loops and the terminal dark point are crossed by the cancellation and do not securely distinguish torsion from the abbreviation tors. A fuller reading than H’s blank is possible, but the word and its ending remain doubtful. The raised centre is separate and clear.','c08','low',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True),
 change('c04','L16, punctuation after s’exploiter',"s'exploiter, en","s'exploiter en","s'exploiter, en",'A separate short dark oblique comma lies after the final run of exploiter and before the next en. It is above the inserted parenthesis and does not belong to its leader.','c09','high',False,True,'omission','Omissions'),
 change('c05','Raised parenthesis above L17, after the groupoid symbol',r'\inserted{(ou le topos $B_K$)}',r'\add{(associé type $B_K$)}',r'\inserted{'+parenthesis+'}','The small opening strokes comprise an o-like loop, a short u-like form, and a tall l with reduced following e. A detached short stroke above this compact run may be an accent, hence the local ou/où uncertainty. The next word has a tall t, a low o, a descending p and o/s-like ending, supporting topos. There is no long letter sequence matching associé, and type would not account for the visible initial and final forms. B with low K and the closing parenthesis are present.','c09','medium',False,True,'misread word','Words',mathematical=True),
 change('c06','L17, extension index of the groupoid symbol',r'\Pi_{\deleted{\bar K/}K}',r'\Pi_{\bar K/K}',groupoid,'The long curved stroke belongs to the inserted parenthesis: it runs beneath that phrase and bends down on the right to its attachment after the groupoid. Separately, short zigzag hatching crosses the extension index beneath that leader. A barred first K, the separator and a final K remain visible. The hatching cancels the first part of the index, but its right edge overlaps the top of the final K, so the cancellation boundary is not fully secure. The final K is retained live in the first reading and possibly cancelled in the alternative; the leader itself is not counted as a strike.','c10','medium',False,True,'deletion state','Struck text',mathematical=True),
 change('c07','L18, cancelled phrase below défini à isom',r"\deleted{\unsure{que l'on|question}}",r'\struck{\ill{}}',r"\deleted{\unsure{que l'on|question}}",'A q-like initial loop with descender, a low joined run, a later tall stem and final low strokes survive beneath a long cancellation. They allow the two proposed readings but do not establish an apostrophe, every interior letter, or a complete question. The phrase remains unresolved rather than being asserted as fully readable. The raised replacement défini à isom is separately visible.','c11','low',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True),
 change('c08','L19, live words unique près following the raised replacement',r'\inserted{défini à isom} unique près',r'\add{défini à isom unique près}',r'\inserted{défini à isom} unique près','Unique près is written on the next ordinary body baseline at the left, with the same scale and spacing as quand on connaît that follows it. It is not part of the smaller raised phrase on the right. The letters of unique, its q descender, and the p/r/è/s sequence of près are visible.','c12','high',False,True,'insertion or placement','Insertions put in the wrong place'),
 change('c09','Extreme lower left, separate foliation',r'\margin{14}','(nothing)',r'\margin{14}','The first digit has an oblique entry and a single tall stem, hence 1. The second has the open angular body and right descending stroke of 4. Both are smaller, thinner and paler than the author’s top number 7 and the main writing.','c13','high',False,True,'omission','Omissions')
]

def decision(id,reading,evidence,n,decision='undecided',confidence='low'):
    return dict(id=id,decision=decision,reading=reading,evidence=evidence,crop=crop(n),box=boxes[n],confidence=confidence)
decisions=[
 decision('M0997',z,'The inserted symbol has two rounded rightward lobes and a sweeping lower leftward foot. It repeats the two later centralizer forms. The page supplies no separate angular Z with which to establish an intended plain-versus-calligraphic alphabet distinction; the two renderings remain open.','c01'),
 decision('M0998',le,'The live l loop and e-like continuation are readable; extra crowded strokes to the left and below could belong to a cancelled or overwritten son, but that old word is not fully recoverable. Both the underlying word and correction state are kept uncertain.','c02',decision='other'),
 decision('M0999',z,'The whole mapping expression was inspected: the 3-shaped source letter, a right-pointing shaft, pi, separator and pi-prime are present. The repeated rounded letter still does not settle the font choice Z versus calligraphic Z.','c03'),
 decision('M1000',z,'After donc the same rounded upper turn and broad lower lobe recur. This confirms the identity of the symbol across the page, but not a contrast between ordinary and calligraphic Z.','c04')
]

def inv(id,kind,position,first,hand='principal handwritten text'):
 return dict(scan=15,sheet_kind='text',hand=hand,element=id,kind=kind,position=position,first_words_or_objects=first,transcribed='yes')
inventory=[
 inv('n01','text','Upper center, above L1','7','author numbering, larger and darker'),
 inv('p01','text','L1, continuation above the corollary','voir que'),
 inv('p02','text','L2–L5, headed by underlined Corollaire','Corollaire Soit'),
 inv('i01','insertion','Above L4; curved leader attaches after centralisateur',r'\inserted{$'+z+r'$ dans $\pi$}'),
 inv('p03','text','L6–L14, proof paragraph','Par dévissage'),
 inv('i02','insertion','Above L7, between groupe and libre',r'\inserted{profini}'),
 inv('i03','insertion','Above the right part of L7, between libre and OPS',r"\inserted{On sait que $\pi'$ est donc libre.}"),
 inv('d01','deletion','L8, possible overwritten material within the crowded word before centre',le),
 inv('m01','margin note','Left of L8–L9, diagonal','à vérifier'),
 inv('m02','margin note','Left of L13, diagonal','à vérifier'),
 inv('p04','text','L15–L20, headed by underlined Scholie','Scholie Le fait que'),
 inv('d02','deletion','End of L15, below the replacement à',r'\deleted{\unsure{sans}}'),
 inv('i04','insertion','Above the cancelled word at the end of L15',r'\inserted{à}'),
 inv('d03','deletion','Start of L16, below centre',r'\deleted{\unsure{torsion|tors.}}'),
 inv('i05','insertion','Above the cancelled word at the start of L16',r'\inserted{centre}'),
 inv('d04','deletion','L17, extension index of the groupoid; final boundary uncertain',groupoid),
 inv('i06','insertion','Above L17; long curved leader attaches after the groupoid',r'\inserted{'+parenthesis+'}'),
 inv('d05','deletion','Right end of L18, below the raised replacement',r"\deleted{\unsure{que l'on|question}}"),
 inv('i07','insertion','Above the cancelled phrase at the right of L18',r'\inserted{défini à isom}'),
 inv('n02','text','Extreme lower left','14','thin smaller foliation hand')
]
notes=[
 'Reader: GPT-6 Astra Pro; effort is not exposed; run SP84_C13_149. The whole page and each supplied half were personally read once, followed by the saved crops c01–c13. No external research, OCR or TeX compilation was performed.',
 'Line count 31: twenty ordinary body rows L1–L20, seven separate interlinear insertion rows, two diagonal marginal-note rows, and two number rows (author 7 and foliation 14). The possible overwritten word in L8 is on the ordinary body row, not counted again.',
 'S015.1 (L1–L5): The page concludes with Centr_pi(pi-prime) = {1}, then states a corollary about the centralizer of an open subgroup in a profinite group given as a successive extension of free profinite groups. This records the manuscript’s assertion without repairing its hypotheses.',
 'S015.2 (L6–L14): The proof reduces to a free profinite group, inserts that pi-prime is free, assumes pi-prime invariant, and invokes two admitted assertions: trivial center and absence of nonidentity finite-order elements. Both admissions carry an explicit à vérifier in the left margin. The writer uses the injection of the centralizer into pi/pi-prime in the argument. This is a description of the source, not an independent verification.',
 'S015.3 (L15–L20): The Scholie revises sans torsion to à centre and discusses recovering the groupoid, or the associated topos wording as actually written, from the exterior group attached to E_{bar K/K}. It changes a cancelled phrase to défini à isom, while unique près remains ordinary main-line text. The page ends with Les hom.',
 'No mathematical check was performed by this reader. The parent is documenting its separate checks at final adjudication. Nothing in the present transcription is emended on mathematical grounds; checks is intentionally empty.',
 'The rounded centralizer symbol is the same at all three occurrences, but the page does not securely distinguish Z from calligraphic Z. All three font doubts are retained; no numeral 3 is inferred from the shape.',
 'The tall l and low e-like continuation before centre are live. Additional crowded ink remains. The son hypothesis and even its overwritten/deleted state are not fully established, hence the whole local alternative rather than a claim that son has been read through the strike.',
 'The long curved stroke beneath the parenthetical topos insertion is an insertion leader. A distinct short zigzag marks cancellation in the groupoid index. They are not conflated. The final K is preserved in the first reading because it remains visible, with explicit doubt whether the edge of the cancellation also includes it.',
 'The cancelled sans, torsion/tors., and que l’on/question remain doubtful because not every internal letter is plain. In the torsion/tors. run, the dark terminal point may belong to an abbreviated ending; no fuller unmarked reading is asserted. Two small dots lower and to the right of that cancellation have no secure textual attachment and are not promoted to punctuation.',
 'The parenthetical phrase has small ou/le-like strokes and a possible detached accent, retained as ou le / où le. Topos and B_K are clearer. The source comma after s’exploiter is separate from that insertion.',
 'Underlines are visible beneath Corollaire, libre, Scholie and extérieur and are retained. H’s bold heading conventions are treated as presentation rather than different source words.',
 'The author’s larger dark 7 is at the top center. The thin small 14 at the lower left is a distinct foliation hand, not another author page number. No date is visible.',
 'All agreed numeric contexts received audit coordinates without optional first-reader crops. Foliation 14 received c13 because H omits it materially. Crops c05 and c06 are rotated clockwise 21 and 25 degrees respectively; recorded boxes use original page coordinates.',
 'Audit boxes cover every insertion and cancellation, both margins, all three doubtful Z formulas, the whole groupoid formula with uncertain cancellation, the disputed words and punctuation, and every pen numeral: 7, the four occurrences of 1 (including two brace-enclosed ones and the inequality), and foliation 14.'
]
hand=[
 dict(habit='The centralizer letter is written as a rounded form resembling 3.',pages=[15],consistency='The inserted name and both later occurrences share the upper turn and broad lower lobe. The page does not provide a contrast that proves plain versus calligraphic Z.',misread='H prints plain Z at all three places; C records an alphabet doubt. The doubt is retained rather than normalized from the mathematical role.'),
 dict(habit='Compact interlinear writing can reduce le to a tall stroke and a low return.',pages=[15],consistency='The parenthetical ou/le-like opening and the crowded word before centre show this reduction, but the latter also has additional obscured ink.',misread='H’s long associé type phrase does not fit the short parenthetical strokes; the exact opening and possible accent remain doubtful.'),
 dict(habit='A long curved leader can pass over a formula without cancelling it.',pages=[15],consistency='The Z dans pi insertion and the topos parenthesis both have curved leaders. The topos leader is distinct from short hatching within the adjacent subscript.',misread='The groupoid-index correction requires separating leader ink from cancellation; H leaves the full extension index live, while C fixes a narrower cancellation boundary.'),
 dict(habit='Heavy cancellation can preserve only the initial loop and fragments of low joins.',pages=[15],consistency='Observed in sans, torsion/tors. and the phrase replaced by défini à isom. None is generalized to other words.',misread='H leaves the latter two as illegible. C’s proposed readings are retained only as explicit doubts because complete letter sequences do not survive plainly.'),
 dict(habit='The separate foliation hand is smaller and thinner than the author numbering.',pages=[15],consistency='The lower-left 14 has thin open angular strokes; the top 7 is larger and darker. Only these local examples are asserted.',misread='H omits 14; it remains a marginal foliation rather than an author header.')
]
notation=[
 dict(written='Centr with lower pi and pi-prime in parentheses',rendering=r'\operatorname{Centr}_{\pi}(\pi\prime)',meaning='Centralizer notation, with the result written as {1}.',evidence='L1 shows the lower pi, prime after the argument pi, equality sign, and two braces around 1.'),
 dict(written='rounded 3-shaped centralizer letter',rendering=z,meaning='The centralizer in pi of the open subgroup pi-prime, named by the insertion.',evidence='c01, c03 and c04 show the repeated rounded form; alphabet distinction remains unresolved.'),
 dict(written='pi and pi-prime',rendering=r'\pi,\pi\prime',meaning='The profinite group and its open subgroup in the corollary.',evidence='Corollary and proof: the prime is a separate elevated stroke, including after OPS and in the denominator of the mapping target.'),
 dict(written='right-pointing shaft',rendering=r'\longrightarrow',meaning='The mapping from the centralizer to pi/pi-prime that the text calls injective.',evidence='c03 shows a distinct filled right end; the small entry turn at the left does not establish an additional bar or a separate left arrowhead.'),
 dict(written='E with extension index bar K/K',rendering=r'E_{\bar K/K}',meaning='The group mentioned at the start and end of the Scholie.',evidence='L15 and L20 show an E, a bar above the first subscript K, a separator, and a second K.'),
 dict(written='capital Pi with a cancelled extension index',rendering=groupoid,meaning='The groupoid named in the Scholie; the cancellation boundary remains doubtful.',evidence='c10: two large Pi legs, a barred first K, separator and final K, with short hatching separate from the insertion leader.'),
 dict(written='B with low K',rendering=r'B_K',meaning='The topos in the inserted parenthesis.',evidence='c09: capital B with two lobes and a distinct lower K before the closing parenthesis.')
]
abbreviations=[
 dict(form='Centr',expansion='centralisateur',place='L1, operator name'),
 dict(form='i.e.',expansion='id est',place='L1, after the equality'),
 dict(form='OPS',expansion='on peut supposer',place='L7, before pi-prime invariant'),
 dict(form='tors. (alternative only)',expansion='torsion',place='Cancelled word at the start of L16'),
 dict(form='isom',expansion='isomorphisme',place='Raised replacement above L18; no stop added'),
 dict(form='hom',expansion='homomorphismes',place='L20, terminal Les hom; no continuation supplied')
]
doubts=[
 dict(place='Above L4, inserted centralizer name',reading=z,alternatives=['Z',r'\mathcal Z'],confidence='low',reason='The rounded form repeats but supplies no secure alphabet contrast; c01.'),
 dict(place='L8, word before centre',reading=le,alternatives=[r'\deleted{son}le','le'],confidence='low',reason='Live le is readable, but the additional ink does not establish all of son or a definite correction state; c02.'),
 dict(place='L10, domain of the mapping',reading=z,alternatives=['Z',r'\mathcal Z'],confidence='low',reason='Whole mapping inspected; same unresolved rounded centralizer form, c03.'),
 dict(place='L10, after donc at the right',reading=z,alternatives=['Z',r'\mathcal Z'],confidence='low',reason='Same upper turn and lower lobe; no local alphabet contrast, c04.'),
 dict(place='End of L15, cancelled word',reading=r'\deleted{\unsure{sans}}',alternatives=['sans'],confidence='low',reason='The initial s and a-like oval survive, but n/s contours merge partly with the cancellation; no unmarked reading is asserted, c07.'),
 dict(place='Start of L16, cancelled word',reading=r'\deleted{\unsure{torsion|tors.}}',alternatives=['torsion','tors.'],confidence='low',reason='Initial t/o and short middle forms are visible; the later loops and terminal point do not settle full word versus abbreviation, c08.'),
 dict(place='Raised parenthesis above L17',reading=r'\unsure{ou le|où le}',alternatives=['ou le','où le'],confidence='medium',reason='Small o/u-like and l/e-like strokes are more plausible than H’s long phrase, but reduced shapes and a possible detached accent remain uncertain, c09.'),
 dict(place='L17, final K in the cancelled index',reading=r'\unsure{K|\deleted{K}}',alternatives=['K',r'\deleted{K}'],confidence='medium',reason='The hatching reaches the upper part of the last K; its visible lower strokes do not alone settle the cancellation boundary. The long curved insertion leader is separate, c10.'),
 dict(place='L18, cancelled phrase',reading=r"\deleted{\unsure{que l'on|question}}",alternatives=["que l'on",'question'],confidence='low',reason='A q-like initial, joined run, later tall stroke and ending remain, but neither complete phrase nor apostrophe is secure, c11.')
]

def audit(id,kind,b,reading):return dict(box=id,kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading)
audit_boxes=[
 audit('b01','number',[755,38,810,90],r'\mspage{7}'),
 audit('b02','formula',[650,80,1055,180],r'$\operatorname{Centr}_{\pi}(\pi\prime)=\{1\}$'),
 audit('b03','insertion',boxes['c01'],r'\inserted{$'+z+r'$ dans $\pi$}'),
 audit('b04','number',[1265,520,1365,615],r'$\{1\}$'),
 audit('b05','insertion',[675,730,910,855],r'\inserted{profini} \uline{libre}'),
 audit('b06','insertion',[940,700,1600,770],r"\inserted{On sait que $\pi'$ est donc libre.}"),
 audit('b07','text',[995,875,1105,950],le),
 audit('b08','margin note',boxes['c05'],r'\margin{à vérifier}'),
 audit('b09','number',[1390,975,1455,1045],'$1$'),
 audit('b10','formula',boxes['c03'],'$'+z+r'\longrightarrow\pi/\pi\prime$'),
 audit('b11','formula',boxes['c04'],'donc $'+z+'$'),
 audit('b12','margin note',boxes['c06'],r'\margin{à vérifier}'),
 audit('b13','formula',[945,1395,1095,1495],r'$\neq1$'),
 audit('b14','deletion',[1475,1635,1605,1715],r'\deleted{\unsure{sans}}\inserted{à}'),
 audit('b15','deletion',[315,1805,515,1895],r'\deleted{\unsure{torsion|tors.}}\inserted{centre}'),
 audit('b16','text',[1290,1830,1340,1875],','),
 audit('b17','formula',[1180,1815,1640,1995],'$'+groupoid+r'$ \inserted{'+parenthesis+'} est'),
 audit('b18','deletion',[1255,1950,1665,2090],r"\deleted{\unsure{que l'on|question}}\inserted{défini à isom}"),
 audit('b19','text',[315,2100,720,2220],'unique près,'),
 audit('b20','number',boxes['c13'],r'\margin{14}')
]
diff_coverage=[
 dict(row=1,classification='macro-only',change_id='',reason='scanpage 15 and H’s editorial p. marker are metadata. The source author number 7 is independently retained.'),
 dict(row=2,classification='editorial-only',change_id='',reason='de l’auteur belongs to H’s editorial note, not to the handwritten line.'),
 dict(row=3,classification='reading-agrees',change_id='',reason='H’s Z is the first C alternative. The source alphabet distinction remains unresolved, so the uncertainty is retained in M0997 and doubts without a separate substantive change.'),
 dict(row=4,classification='material',change_id='c01',reason='The crowded ink around live le is not a securely readable literal question mark; the possible correction state is represented explicitly.'),
 dict(row=5,classification='material',change_id='c01',reason='Rather than choosing a bare son or bare le with certainty, the possible overwritten son and the live le are represented in a local state alternative.'),
 dict(row=6,classification='reading-agrees',change_id='',reason='H agrees with the first Z reading; the unresolved font alternative remains in M0999 and doubts.'),
 dict(row=7,classification='reading-agrees',change_id='',reason='H agrees with the first Z reading; the unresolved font alternative remains in M1000 and doubts.'),
 dict(row=8,classification='material',change_id='c02',reason='The second à vérifier note is beside the finite-order assertion before the concluding clause. Dash length alone is a rendering distinction.'),
 dict(row=9,classification='material',change_id='c02',reason='The same margin placement difference is accounted for once, with attachment before ce qui achève.'),
 dict(row=10,classification='material',change_id='c03',reason='H’s illegible cancelled run permits the uncertain torsion/tors. reading, but the ending remains unresolved.'),
 dict(row=11,classification='material',change_id='c04',reason='A separate comma follows s’exploiter.'),
 dict(row=12,classification='material',change_id='c05',reason='The short ou/le-like opening followed by topos fits the visible strokes; H’s long associé/type wording does not.'),
 dict(row=13,classification='material',change_id='c07',reason='The cancelled phrase retains partial readable ink but neither que l’on nor question can be resolved fully.'),
 dict(row=14,classification='material',change_id='c09',reason='The separate lower-left foliation 14 is present and omitted by H. A mandatory omission crop c13 is supplied.')
]
report=dict(scan=15,reader='/root/reader_c',lines_read=31,changes=changes,decisions=decisions,inventory=inventory,notes=notes,checks=[],hand=hand,notation=notation,abbreviations=abbreviations,doubts=doubts,audit_boxes=audit_boxes,diff_coverage=diff_coverage)
(root/'edition/reviews/149_scan015.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote 149_scan015.tex and 149_scan015.json')
print(f'{len(changes)} changes; {len(decisions)} mark decisions; {len(inventory)} inventory rows; {len(audit_boxes)} audit boxes; {len(diff_coverage)} difference rows')
