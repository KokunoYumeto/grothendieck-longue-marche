from pathlib import Path
import json,copy,re
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan052/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC']
bm=[0,1,2,3,4,5,6,7,None,8,9,10,11,None,12,13,14,15,16,None,None,17,18,19,20,21,22,23,24,25,26,None,28,29,None,30,31,32,33]
cm=[0,1,2,3,4,5,6,7,None,8,9,10,11,None,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,None,30,31,None,32,33,34,35]
ds=copy.deepcopy(A)
for i,d in enumerate(ds):
 d['readers']={'A':A[i]['reading'],'B':B[bm[i]]['reading'] if bm[i] is not None else 'See full returned reading; no separate decision row.','C':C[cm[i]]['reading'] if cm[i] is not None else 'See full returned reading; no separate decision row.'}
 d['marked_in_H']='yes' if any(x in str(d.get('h_reading','')) for x in ['\\uncertain','\\ill','\\supplied']) else 'no'
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
def setd(i,**kw):ds[i].update(kw)
def cp(a,name):return f'readers/scan052/{a}/{name}.jpg'
mc=lambda name:f'crops/scan052/{name}.jpg'
setd(0,crop=mc('th'),scan_shows='Tall t and h, followed by open space; no detached full stop follows h.')
setd(1,reading=r'\unsure{supposer}',diff_c=True,diff_h=False,unresolved=True,alternatives='The compressed final strokes remain uncertain; no secure competing word.',confidence='medium',crop=cp('C','19_supposer'),scan_shows='Initial curl and two long p descenders support supposer; the o-ser sequence is very compressed and does not support removing all doubt. A and B were certain; C retained doubt.')
setd(2,crop=mc('ni'),scan_shows='A low joined n-i form with a detached dot over the final stroke; no tall crossed t.',consequential='The condition is written X ni Y lisses, not H’s X et Y: preserve the negative coordination with sans supposer.')
setd(3,crop=cp('C','01_second_numeral'),scan_shows='Heavy retraced V with a pale right upright. The upright may belong to the retraced right limb rather than an independent I; retain V|VI in that order.')
setd(4,crop=cp('C','02_faisceau_second'),scan_shows='The final u trails off before the colon; no independent crossing x follows it.')
setd(5,reading='signaler',diff_c=True,diff_h=False,unresolved=False,alternatives='',confidence='high',crop=cp('C','03_rajouter'),scan_shows='A dotted i precedes the g bowl and long left-sweeping descender; low n-a strokes lead to tall l and ending er. These strokes support signaler, not rajouter.')
setd(6,crop=cp('C','04_raisonnable'),scan_shows='Joined raison-nable sequence is visible, including tall b and l and the final e; the C doubt is resolved.')
setd(7,crop=cp('C','05_cancelled_numeral'),scan_shows='Several cancellation diagonals intersect the numeral and its transverse rules. IV, V and VI remain possible; the underlying order is not recoverable with confidence.')
setd(8,h_reading=r'\add{\emph{VI}}; note: VI below and surrounded',diff_h=True,kind='drawing or diagram',crop=cp('A','c05_cancelled_numeral'),scan_shows='The live barred VI is below the cancelled numeral. A long open U descends on its left and rises to the right of the upper deletion. The consolidated TikZ reproduces that vertical relation; C placed the replacement alongside and H only described the enclosure.')
ds[8]['readers']['B']='Inline replacement VI with its own U-shaped curve (returned reading).'
ds[8]['readers']['C']='Replacement VI below the cancelled numeral, within a long open U (returned reading).'
setd(9,crop=cp('B','04_z_faisceaux'),scan_shows='The terminal u is followed by crossed strokes of x; faisceaux is plural in the ink.')
setd(10,crop=cp('C','06_over_ou'),scan_shows='A rounded o is followed by a shallow u; no t stem or crossbar is present.',consequential='The coefficient-sheaf alternatives are joined by ou; H’s et changes their stated relation.')
setd(11,crop=cp('C','06_over_ou'),scan_shows='Dark crossing with additional faint arms lies above ou. Asterisk is preferred, plus remains possible; its reference is not identified.')
setd(12,crop=cp('C','07_before_ajouter'),scan_shows='The detached mark after the opening parenthesis has a head and a descending taper, supporting comma rather than full stop.')
setd(13,crop=mc('numero'),scan_shows='Capital N is followed by a raised small o and a separate short underline beneath that o; H’s degree sign omits the underline.')
ds[13]['readers'].update(B=r'N\textsuperscript{\uline{o}}',C=r'N\textsuperscript{\uline{o}}')
setd(14,crop=mc('ttes'),scan_shows='Two tall crossed t strokes are followed immediately by compressed e-s; there is no ou sequence. Retain abbreviation ttes.')
setd(15,crop=cp('C','08_systemes'),scan_shows='The final e/s cluster is faint and compressed. Plural is preferred, but a separate final s is not certain; retain the existing C alternative.')
setd(16,crop=cp('C','09_adiques_insertion'),scan_shows='The inserted word begins with a small a oval, then d-i-q-u-e-s; the left stroke belongs to a, not a prefixed hyphen. Remove C doubt.')
setd(17,crop=cp('C','09_adiques_insertion'),scan_shows='The curve continues beneath the inserted adiques and turns upward at the right. Its left end is not a separate opening parenthesis before dans; reproduce it as an insertion guide.')
setd(18,crop=cp('C','10_derivees'),scan_shows='Tall d and ending strokes are visible, but the compressed middle remains faint. Retain dérivées as the uncertain reading.')
for i,j,cropname in [(19,17,'20_mark_below_these'),(20,18,'21_faint_mark_centre')]:
 setd(i,reading=C[j]['reading'],crop=cp('C',cropname),scan_shows=('A pale angular left tick with a rising right branch is physically present.' if i==19 else 'A pale central branched trace and short lower marks are physically present.')+' No lexical identity or deliberate mathematical function can be established; retain an uncertain TikZ facsimile. Both witnesses omit it.')
 ds[i]['readers']['B']='Absent from returned reading and inventory.'
setd(21,crop=cp('C','11_detached_points'),scan_shows='Two isolated dark points lie on an oblique lower-left to upper-right axis. Their function is uncertain; the drawing preserves their spacing without asserting a grammatical colon.')
setd(22,crop=cp('C','12_livre'),scan_shows='An initial tall stem and very compressed following joins support livre but do not securely exclude Hom; retain both rather than resolve from the phrase.')
setd(23,crop=cp('C','13_expose'),scan_shows='The l-expo sequence is readable. Reduced terminal strokes and an acute-like rise at the right support sé, but do not make the ending secure; mark the ending only as uncertain.')
setd(24,crop=cp('C','13_expose'),scan_shows='After the edge of the word, no detached comma is visible before the next-line signaler.')
setd(25,crop=mc('ennui'),scan_shows='After l’ and e, a chain of low n-n-u joins ends in dotted i. No p descender or tall internal l of emploi is present.')
setd(26,crop=mc('trop'),scan_shows='Tall looped t, low r/o joining and a long p descender are visible; the word trop can be read without H’s doubt.')
setd(27,reading=r'\unsure{\nu|n|N}',confidence='medium',unresolved=True,alternatives=r'n; N',crop=cp('C','14_coefficients'),scan_shows='The raised angular letter has a low central join and rising right stroke, favouring nu. A faint left upright leaves n/N possible. Do not supply the expected integer exponent from the coefficient expression.',consequential='The exponent is retained as nu|n|N from its strokes; neither C’s preferred n nor H’s certain n is silently imposed.')
setd(28,crop=cp('C','14_coefficients'),scan_shows='Two separated short horizontal strokes follow the final Z; the second is longer and paler. There is no third point supporting an ellipsis.')
setd(29,reading=r'\unsure{{<}|{:}|{\in}}',diff_c=True,confidence='low',crop=cp('C','15_i_separator_eta'),scan_shows='Two heavy right-hand lobes have a faint possible angular connection to the left. A less-than shape is preferred, but colon and membership remain possible; syntactic expectation does not settle the trace.',consequential='The separator after i remains graphically ambiguous; the transcription does not normalize it to H’s colon.')
setd(30,crop=cp('C','15_i_separator_eta'),scan_shows='Short left stem, rounded connection and long right descender favour eta, with cursive y still possible. This recurring ambiguity is marked at its first occurrence only.',consequential='H’s five y letters are transcribed as the recurring eta-shaped sign, with eta|y doubt at the first occurrence.')
setd(31,crop=cp('A','c20_pt_abbreviation'),scan_shows='The short t sits above the p bowl and stem. Preserve the raised t instead of a baseline pt.')
ds[31]['readers'].update(B='pt',C='pt')
setd(32,crop=mc('generique_comma'),scan_shows='A detached tapered comma follows générique before et.')
setd(33,crop=cp('C','16_text_F_eta'),scan_shows='The lowered letter has the same short left part and long right descender as the first eta/y; no separate letter change is visible.')
setd(34,crop=cp('A','c21_loc_libre'),scan_shows='The initial l loop and a b-like stem/bowl support libre, but i and the final r-e are faint and reduced; retain a local doubt instead of relying on loc. libre as an expected phrase.')
ds[34]['readers'].update(B='libre',C='libre')
setd(35,crop=cp('C','17_sur_eta'),scan_shows='The isolated letter after sur has the same shoulder and long right descender as the recurring eta/y family.')
setd(36,crop=cp('C','17_sur_eta'),scan_shows='No detached comma follows the isolated final letter before the displayed equation.')
for i in [37,38]:setd(i,crop=cp('C','18_final_equation'),scan_shows='The lowered letter on this F matches the recurring eta-shaped family. The surrounding i stars are subscripts, and the nested parentheses and equality are visible; no algebraic correction is made.')
# Two independently raised issues not indexed in A’s list.
z=copy.deepcopy(C[25]);z.update(reading=r'\unsure{\mathbb{Z}|Z}',diff_c=True,diff_h=True,confidence='medium',unresolved=True,alternatives='single-stroke Z',crop=cp('C','14_coefficients'),marked_in_H='no',readers={'A':r'\mathbb{Z}','B':r'\mathbb{Z}','C':C[25]['reading']},scan_shows='The middle Z has close diagonal traces, less secure than the flanking doubled Z letters. Prefer double-stroke Z but retain ordinary Z as an alphabet alternative.');ds.insert(27,z)
ar=copy.deepcopy(B[27]);ar.update(crop=cp('C','15_i_separator_eta'),confidence='low',marked_in_H='no',readers={'A':r'\longrightarrow','B':B[27]['reading'],'C':r'\longrightarrow'},alternatives='incidental trace rather than a deliberate tilde',scan_shows='A faint bowed, step-like trace lies above the dark arrow shaft. It is retained as an uncertain tilde; the possibility of an incidental mark is unresolved, and no isomorphism is inferred.',consequential='An uncertain upper tilde-like trace on the inclusion arrow is recorded, without interpreting it as a mathematical assertion.');ds.insert(32,ar)
for k in [1,2]:
 ds.append(dict(place=f'Horizontal divider {k}',c_reading='TikZ curved horizontal rule',h_reading=r'\note{trait horizontal}',reading='TikZ curved horizontal rule',diff_c=False,diff_h=True,c_doubt=False,unresolved=False,alternatives='',confidence='high',kind='drawing or diagram',marked_in_H='no',scan_shows='A long slightly curved horizontal stroke separates the adjacent entries. Its shape is drawn in the consolidated text; H gives a prose note only.',crop=mc(f'divider{k}'),readers={a:'TikZ curved horizontal rule' for a in 'ABC'}))
text=(O/'readers/scan052/C/reading.tex').read_text()
text=text.replace(r'\unsure{\mathrm{VI}|\mathrm{V}}',r'\unsure{\mathrm{V}|\mathrm{VI}}',1)
text=text.replace(r'\margin{\unsure{:}}',A[21]['reading'])
text=text.replace(r"\unsure{l'exposé|l'expo}",r"l'expo\unsure{sé}")
text=text.replace(r'\unsure{Z|\mathbb{Z}}',r'\unsure{\mathbb{Z}|Z}')
text=text.replace(r'\unsure{\nu|n}',r'\unsure{\nu|n|N}')
text=text.replace(r'\longrightarrow X',r'\overset{\unsure{\sim}}{\longrightarrow} X')
text=text.replace('inclusion du pt générique',r'inclusion du p\textsuperscript{t} générique')
text=text.replace('Module loc. libre sur',r'Module loc. \unsure{libre} sur')
# Make record of the replacement exactly match its final source.
start=text.index(r'\tikz[baseline=(old.base)');end=text.index(r'\quad Reprendre',start)
ds[8]['reading']=text[start:end]
(O/'pages/H37-01_37_scan052.tex').write_text(text)
inv=copy.deepcopy(R['A']['inventory'])
for x in inv:
 x['kind']={'text block':'text','archive pagination comment':'text'}.get(x['kind'],x['kind'])
 x['hand']='his hand' if x['element']!='Archive number' else 'unnamed hand'
inv.insert(-2,dict(sheet_kind='text',hand='his hand',element='Possible upper mark on final prose arrow',kind='insertion',position='over the arrow from eta/y to X',first_words_or_objects='uncertain tilde-like trace',transcribed='yes'))
notation=copy.deepcopy(R['C']['notation'])
for x in notation:
 if x['sign']=='Coefficient exponent':x.update(latex=r'\unsure{\nu|n|N}',evidence='Low angular central join and rising right stroke; faint left upright leaves n/N possible.')
 if x['sign']=='Central coefficient Z alphabet':x.update(latex=r'\unsure{\mathbb{Z}|Z}',evidence='Close diagonal traces favour doubled Z, but their independence is less secure than in the flanking Z letters.')
notation+= [dict(sign='Raised point abbreviation',latex=r'p\textsuperscript{t}',evidence='The short t is visibly above the p bowl.',place='Entry 7: point générique'),dict(sign='Possible arrow overscript',latex=r'\overset{\unsure{\sim}}{\longrightarrow}',evidence='Faint bowed trace over dark shaft; deliberate status uncertain.',place='Entry 7 inclusion arrow')]
notes='One handwritten squared-paper leaf with seven work-list entries: weak Lefschetz with only X−Y assumed smooth; a coefficient-sheaf definition in terms of champ associé; restating SGA 4 notions in Z-ell or Q-ell sheaf language; constructions in the relatively smooth case; adic projective systems in derived categories; a warning about overly particular coefficients; and a requested identity involving D and direct image from the generic point. These are tasks or proposals, not proofs on this leaf. The explicit tentative directions are “Essayer de faire” and the alternative placement “(ou dans thèse)”. The cancelled exposé number, replacement VI and inserted adiques are retained. There is no separate title, date, authorial page number or stated total page count. The lower-left 51 is recorded only as the archive number. The source dossier attributes the notes to Grothendieck; this attribution supplies “his hand” in the inventory and is not an independent handwriting authentication. Two horizontal dividers, the numeral rules and enclosure, the insertion guide, two faint nonlexical traces and an oblique dot pair are all represented. The two faint traces and possible arrow overscript remain uncertain in function.'
maths=[r'Entry 1: ni rather than H’s et is supported by the low joined strokes and dot; the logical condition is preserved as written.',r'Entry 3: ou rather than H’s et is visible between the two coefficient-sheaf languages.',r'Entry 6: the coefficient exponent looks angular like nu, while n/N cannot be excluded. The anticipated coefficient expression did not determine the transcription.',r'Entry 7: the separator after i is ambiguous (<, colon or membership), and the faint upper arrow mark may be a tilde or incidental trace. Neither has been normalized from the expected notation for an inclusion.',r'Entry 7 and display: the five eta/y-shaped glyphs were compared and one recurring uncertainty is marked at the first occurrence. Both direct-image stars are below i. The nested parentheses and equality parse as a requested identity; no proof, computation or independent background verification was performed.']
for d in ds:
 if d.get('crop','').startswith(str(O)+'/'):d['crop']=d['crop'][len(str(O))+1:]
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
out=dict(scan=52,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=maths,notation=notation,abbreviations=R['A']['abbreviations'],slips=[],check_events=[],main_crops=json.loads((O/'crops/scan052/manifest.json').read_text()))
(O/'decisions/scan052.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Wrote final scan 052 and',len(ds),'adjudication rows; inventory',len(inv))
