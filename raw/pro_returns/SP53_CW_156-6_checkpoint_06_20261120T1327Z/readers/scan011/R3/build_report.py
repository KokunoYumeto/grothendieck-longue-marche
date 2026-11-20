import json
from pathlib import Path
from datetime import datetime, timezone

base=Path('/workspace/scratch/42e661864e98')
out=base/'out/readers/scan011/R3'
source=str(base/'source/SP53_CW_156-6_scans/J156-6-02_156-6_scan011.jpg')
manifest=json.loads((out/'crop_manifest.json').read_text())

def ev(crop=None, box=None):
    if crop is not None:
        m=manifest[crop-1]
        return dict(crop='readers/scan011/R3/'+m['name']+'.jpg',crop_box=m['box'],crop_source=source)
    return dict(crop=None,crop_box=box,crop_source=source)

rows=[]
def d(place,c,h,reading,ac,ah,kind,marked,confidence,evidence,crop=None,box=None,math='No mathematical correction is inferred.'):
    rows.append(dict(id=f'R3-011-D{len(rows)+1:02d}',place=place,c=c,h=h,reading=reading,against_C=ac,against_H=ah,kind=kind,marked_in_H=marked,confidence=confidence,evidence=evidence,mathematical=math,**ev(crop,box)))

# Substantive readings, including uncertainty removal, are collated in page order.
d('Axiomes, first line, ens',r'\unsure{ens}','ens.', 'ens',True,True,'other','no','high','The first loop and two reduced humps form ens; the intervening white space before de contains no full stop. C uncertainty is removed and H’s stop is not retained.',1)
d('Axiomes, base ds une',r'\unsure{ds}',"d'une",'ds une',True,True,'misread word','no','high','After the looped d is a detached curved reduced s extending through the letter-height zone, rather than an apostrophe. A separate une follows.',2)
d('Axiomes, first family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\mathfrak{F}',r'\unsure{\mathcal{F}|\mathfrak{F}}',True,True,'misread symbol or index','no','medium','A long sloping top arm and separate curved middle arm cross a single curved stem. Identity F is secure; correspondence with a calligraphic or fraktur typeface is not. The supplied notation candidates are retained, with first-candidate use subsequently.',3,math='Alphabet uncertainty only; the collection’s identity is not altered.')
d('Axiomes, first M',r'M',r'\mathcal{M}',r'\unsure{\mathcal{M}|M}',True,True,'misread symbol or index','no','medium','The M has a broad rising entry, two tall peaks, a rounded trough and a long terminal downstroke. Its handwritten identity is clear, but ordinary versus calligraphic typeface is not determined by this occurrence.',3,math='Alphabet uncertainty only; subsequent occurrences use the first candidate by the stated convention.')
d('Axiomes, On trouve des données','données',r'\ill{}','données',False,True,r'readable ink left as \ill{}','yes','medium','The initial looped d, two reduced medial groups, raised acute above the ending and final horizontal es group support données. No alternate word is supplied from mathematical expectation.',4)
d('Axiomes, simples sur F',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,'misread symbol or index','no','medium','Half a shows the same two-arm family F as its first occurrence. This is subsequent use of the first alphabet candidate, not a claim that the fraktur alternative has been disproved.',box=[1318,431,1419,514],math='Recurring family alphabet; see the first-occurrence uncertainty.')
d('Axiomes, canceled plus',r'\deleted{\unsure{plus}}',r'\struck{plus}',r'\deleted{plus}',True,False,'other','no','high','The long p descender, looped l, low u and final s remain readable beneath the cancellation. H already records its deletion correctly.',5)
d('Axiomes, sophistiquées',r'\unsure{sophistiquées|sophistiqués}','sophistiqués','sophistiquées',True,True,'misread word','no','high','After the q descender and u, an accented é is followed by a distinct terminal e/s group. The feminine ending is read from those strokes, not supplied to agree with données.',5)
d('Axiomes, axiomes essentiels','essentiels',r'\uncertain{naturels}','essentiels',False,True,'misread word','yes','high','Two reduced initial groups precede the tall t, the small i mark and the looped l; the sequence reads essentiels and does not begin with the n-a-t group required by naturels.',6)
d('Axiomes, quand on reste',r'\unsure{reste|entre}','reste',r'\unsure{reste|entre}',False,True,'other','no','medium','A low initial cup, a long reduced middle stroke and a late crossed t favor reste. The compressed initial group does not securely exclude entre, so C’s actual alternative is retained.',7)
d('Axiomes, plus ou moins',r'\unsure{plus ou moins}','plus ou moins','plus ou moins',True,False,'other','no','medium','Plus is fully formed. Between it and the recognizable m/o/i/n/s sequence are a small closed mark and short return corresponding to ou. The group is faint but present.',7)
d('Axiomes, dans F before le plus',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,'misread symbol or index','no','medium','The terminal family F has the recurring top arm, middle arm and bent stem seen on half a. Subsequent first-candidate alphabet use follows the first marked occurrence.',box=[1600,700,1673,801],math='Recurring alphabet uncertainty, without change to the statement.')
d('Axiomes, le plus after the comma',r'\unsure{le|les}','et les','le',True,True,'misread word','no','high','The line begins with one looped l and its short e return. There is no preceding et, and no separate terminal s is visible before plus.',8)
d('Axiomes, transparent',r'\unsure{transparent|transparents}','transparents','transparent',True,True,'misread word','no','high','The ending is the long reduced n followed by the final elevated t stroke. No additional s follows it. The resulting singular wording is preserved despite the earlier plural axiomes.',8)
d('Axiomes, parenthetic pareil pour M',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','no','medium','Half a shows the same two-peak handwritten M as at the first occurrence. The first calligraphic candidate is used here under the page’s explicitly retained initial uncertainty.',box=[1458,904,1568,986],math='Typeface uncertainty only; the author’s question is unchanged.')
d('Underlined Sur F heading',r'\uline{Sur $\mathcal{F}$}',r'\emph{Sur} $\mathfrak{F}$',r'\uline{Sur $\mathcal{F}$}',False,True,'omission','no','high','The single continuous underline extends from beneath Sur into the F’s lower footprint. H’s underline representation covers only Sur. The family alphabet continues the first marked choice.',box=[214,1100,423,1223],math='Underline scope and recurring alphabet only.')
d('(1.16), date punctuation','(20. juin)','(20 juin)','(20. juin)',False,True,'other','no','high','A distinct small ink point separates 20 and juin inside the parentheses. It is visible before the tall j; there is no terminal point after the note’s final relation sign.',9)
d('(1.16)b, dated note',r"Non, \unsure{par mon nouveau point de vue} ça n'implique plus $\ll$",r"Non, \ill{} nouveau \ill{} \ill{} que pour $\ll$",r"Non, par mon nouveau point de vue ça n'implique plus $\ll$",True,True,'misread word','yes','medium','The upper line has the p descender and short ar, mon, nouveau, point de vue. The lower line begins with ça and a separate negative n’, continues through the q descender of implique, then plus and two straight left angles. The visible sequence is not que pour. The arrow to b) is present, as both witnesses already recognize.',9,math='The note explicitly denies that option b) still implies the relation \\ll under the author’s new viewpoint; no proof of that denial is attempted.')
d('(1.16)c, canceled symbol before et',r'\deleted{\unsure{F|\mathcal{F}}}','[note: un signe biffé avant et]',r'\deleted{\unsure{F|\mathcal{F}}}',False,True,'omission','no','low','Several oblique cancellation strokes obscure a stem with cross-arm remnants. F is plausible but its alphabet cannot be recovered. H’s note correctly records the canceled sign’s presence; only the tentative underlying reading is added here.',10,math='No missing formula symbol is replaced by illegible; explicit symbol candidates remain.')
d('(1.16)c, map source family',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,'misread symbol or index','no','medium','Half b shows the upright family F with a broad top and middle arm immediately before the plain rightward arrow. The page’s first alphabet uncertainty applies.',box=[819,1397,889,1468],math='Recurring alphabet choice only.')
d('(1.16)c, power-set argument',r'\mathrm{P}(\mathcal{F})',r'\mathrm{P}(\mathfrak{F})',r'\mathrm{P}(\mathcal{F})',False,True,'misread symbol or index','no','medium','The P has a plain stem and upper bowl. Its parenthesized F is read with the recurring family alphabet; the parentheses and P itself agree in both witnesses.',box=[947,1393,1085,1468],math='No change to the power-set map beyond the already marked family alphabet.')
d('(1.16)c, scope of underbrace','brace under et and the map','note: brace attached to \\ll, et, and the map','brace under et and the map',False,True,'insertion or placement','no','high','In half b the underbrace begins below et around x744, well to the right of the canceled sign and the \\ll at x540–601, and ends below the map. H correctly identifies the brace but extends its scope too far left.',box=[731,1484,1077,1536],math='The verbal incidence gloss is attached to et plus the map in the visible layout; its content is not altered.')
d('(1.16)c, parenthetic notée','notée','notion','notée',False,True,'misread word','no','high','After no and the crossed t are a raised accent and two small terminal e strokes, with no final n. The mapsto arrow, tilde, comma and le are clear and agree otherwise.',11)
d('(1.16)c, déployement',r'\unsure{déployement|déploiement}','déploiement','déployement',True,True,'abbreviation expanded or spelling modernised','no','high','The middle character after o has a long diagonal descender below the baseline and no i dot. It is y. The initial acute is separately visible above é.',12)
d('(1.16)c, vu comme partie de family F',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,'misread symbol or index','no','medium','The terminal F within the closing parenthesis is the recurring family letter, with heavier retracing in this small occurrence. It follows the first marked alphabet choice.',box=[1607,1475,1673,1546],math='Recurring alphabet uncertainty only.')
d('(1.16)c, canceled lower noun',r'\unsure{description|désignation}',r'\struck{\ill{}}',r'\deleted{\unsure{description|désignation}}',False,True,r'readable ink left as \ill{}','yes','low','Below the inserted relation phrase are a tall initial d, heavily crossed medial strokes, a deep looped descender and later t/i-like strokes. Description is the stronger reading, but the cancellation prevents exclusion of désignation. Both witnesses already recognize the cancellation.',13)
d('(1.16)c, inserted upper relation phrase',r"\inserted{relation \unsure{de type|d'inc.}}",r"relation d'inc\supplied{idence}",r"\inserted{relation \unsure{d'inc.|d'inc}}",True,True,'abbreviation expanded or spelling modernised','no','medium','Relation is clearly written above the canceled noun. Its continuation has d, an apostrophe, short i/n strokes and an open c; there is no spelled-out idence and no type. A small raised terminal point may belong to the abbreviation or the crossing stroke, so stop/no-stop alternatives remain. The whole revised phrase is also crossed.',13)
d('(1.16), H editorial transition after canceled gloss','[absent]','; sous c),','[not transcribed as manuscript text]',False,True,'text not on the page','no','high','The right gloss ends in cancellation strokes and white space. No semicolon or words sous c) are written there. H uses these as a layout explanation, which is credited as editorial rather than transferred into the diplomatic page.',13)
d('(1.16), quote glyphs around F est une strate de G',r"``$F$ est une strate de $G$''",'« F est une strate de G »',r"``$F$ est une strate de $G$''",False,True,'other','no','high','Half b shows paired short raised strokes at the opening and closing of the phrase. They are not lateral angled guillemets.',box=[711,1618,1270,1692])
d('(1.16), F belongs to M in the incidence gloss',r'F\in M',r'F\in\mathcal{M}',r'F\in\mathcal{M}',True,False,'misread symbol or index','no','medium','The small M after membership has the same two-peaked cursive form. Subsequent use of the first candidate follows the initial M uncertainty. The underlined et and F≤G are separately read and agree.',box=[801,1667,947,1735],math='Alphabet choice only; incidence still requires both membership and the order relation.')
d('Lower paragraph, canceled Je',r'\deleted{\unsure{Je}}',r'\struck{Je}',r'\deleted{Je}',True,False,'other','no','high','The lower hooked stem belongs to J and the adjoining loop/return is e. Horizontal and oblique strokes cross the group. H already reads the word and cancellation correctly.',14)
d('Lower paragraph, ces points', 'ces points','ce point',r'\unsure{ces points|ce point}',True,True,'misread word','no','medium','The reduced demonstrative and point(s) ending favor plural ces points, but their short terminal returns cannot be securely separated into an added s. Both singular/plural alternatives are therefore retained rather than deciding from reference or grammar.',14)
d('Lower paragraph, fondamentales dans family F',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,'misread symbol or index','no','medium','Half b shows the family F’s wide upper flourish and bent stem after dans. It follows the first marked alphabet choice on this page.',box=[929,1878,1024,1970],math='Recurring alphabet uncertainty only.')
d('Lower paragraph, en écrivant',r'\unsure{on écrira|en écrivant}',r'en \uncertain{incluant}','en écrivant',True,True,'misread word','yes','medium','The opening is the small open e followed by n. The next word has an independently raised acute, the é/c sequence, reduced medial strokes and a final tall t, favoring écrivant over écrira and excluding the opening of incluant.',15)
d('(1.17), first F operand','F','F',r'\unsure{F|\mathbb{F}}',True,True,'misread symbol or index','no','medium','Two enclosed/retraced upright strokes occur between the top and middle arms, then merge into a single lower stem. A retraced ordinary F is favored, but a deliberately doubled F cannot be ruled out from the ink. No deletion is inferred.',17,math='The doubled-form alternative is preserved without silently changing the intended variable or repairing the definition.')
d('(1.17), above equivalence arrow',r'\unsure{\mathrm{dfn}|\mathrm{déf}}',r'\mathrm{dfn}',r'\mathrm{dfn}',True,False,'other','no','high','A looped d is followed directly by a tall f with a descender and a final short n shoulder. There is no separate accented e between d and f.',16,math='The short label dfn is retained without expansion.')
d('(1.17), beneath left side of equivalence arrow',r'\unsure{\mathrm{par}}','[absent]',r'\unsure{\mathrm{par}}',False,True,'omission','no','low','A long descending loop and adjacent small curved strokes sit below and overlap the left end of the arrow. They plausibly spell par, but their overlap with the arrow prevents certainty. The mark cannot simply be discarded.',16,math='This uncertain under-arrow text is kept separate from the clearly read dfn label; no logical content is supplied.')
d('(1.17), quote glyphs around F incident à G',r"``$F$ incident à $G$''",'« F incident à G »',r"``$F$ incident à $G$''",False,True,'other','no','high','Half b shows paired raised strokes on each side of the verbal relation, as in the earlier incidence gloss. They are not lateral guillemets. The grave in à is visible.',box=[879,1974,1267,2047])
d('(1.17), final F belongs to M',r'F\in M',r'F\in\mathcal{M}',r'F\in\mathcal{M}',True,False,'misread symbol or index','no','medium','The final M at the right edge again has two high peaks and a curved entry. It uses the first candidate established at the initially marked M; no bar, subscript or additional condition is visible.',box=[1579,1968,1678,2038],math='Alphabet choice only. F≤G and F∈M are the author’s two stated conditions.')

c_doubts=[]
def cd(place,c,reading,disposition,evidence,crop):
    c_doubts.append(dict(place=place,c=c,reading=reading,disposition=disposition,evidence=evidence,**ev(crop)))
cd('Axiomes, ens',r'\unsure{ens}','ens','resolved','Readable compressed e/n/s; no stop before de.',1)
cd('Axiomes, ds',r'\unsure{ds}','ds','resolved','A reduced curved s follows the d; it is not an apostrophe.',2)
cd('Axiomes, first family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\unsure{\mathcal{F}|\mathfrak{F}}','retained','Letter identity is secure, typographic alphabet is not. Existing notation-table candidates are used, supported by the wide top arm and curved middle arm.',3)
cd('Axiomes, canceled plus',r'\deleted{\unsure{plus}}',r'\deleted{plus}','resolved','p descender, l loop, u and s survive the strike.',5)
cd('Axiomes, sophistiquées',r'\unsure{sophistiquées|sophistiqués}','sophistiquées','resolved','A distinct e/s group follows accented é after qu.',5)
cd('Axiomes, reste',r'\unsure{reste|entre}',r'\unsure{reste|entre}','retained','Low beginning, reduced middle and late crossed t favor reste but do not exclude entre.',7)
cd('Axiomes, plus ou moins',r'\unsure{plus ou moins}','plus ou moins','resolved','Both small components of ou are present between the legible flanking words.',7)
cd('Axiomes, le',r'\unsure{le|les}','le','resolved','Looped l and short e return; no additional s before plus.',8)
cd('Axiomes, transparent',r'\unsure{transparent|transparents}','transparent','resolved','Final tall t has no following s; singular is kept as written.',8)
cd('(1.16)c, canceled symbol',r'\deleted{\unsure{F|\mathcal{F}}}',r'\deleted{\unsure{F|\mathcal{F}}}','retained','Dense oblique hatching leaves a stem and cross-arm remnants, insufficient to resolve the alphabet.',10)
cd('(1.16)c, déployement',r'\unsure{déployement|déploiement}','déployement','resolved','The long diagonal y descender and absence of i dot are decisive.',12)
cd('(1.16)c, canceled lower noun',r'\unsure{description|désignation}',r'\unsure{description|désignation}','retained','The deep medial descender and later t favor description; crossing strokes obscure the earlier letter sequence.',13)
cd('(1.16)c, inserted continuation',r"\unsure{de type|d'inc.}",r"\unsure{d'inc.|d'inc}",'retained','The letters read d’inc, excluding de type. The small final raised point remains ambiguous between an abbreviation stop and a cancellation-stroke remnant.',13)
cd('(1.16)b, dated note phrase',r'\unsure{par mon nouveau point de vue}','par mon nouveau point de vue','resolved','Separate par, mon, nouveau and point de vue groups survive in the rising upper line.',9)
cd('Lower paragraph, canceled Je',r'\deleted{\unsure{Je}}',r'\deleted{Je}','resolved','Hooked J and right-hand e remain under the cross strokes.',14)
cd('Before (1.17), en écrivant',r'\unsure{on écrira|en écrivant}','en écrivant','resolved','Open initial e/n, accented next initial and final t support en écrivant.',15)
cd('(1.17), below arrow',r'\unsure{\mathrm{par}}',r'\unsure{\mathrm{par}}','retained','A descending loop with adjacent curved marks remains entangled with the left arrowhead.',16)
cd('(1.17), above arrow',r'\unsure{\mathrm{dfn}|\mathrm{déf}}',r'\mathrm{dfn}','resolved','Direct d-f-n sequence, tall f descender, no accented e.',16)

inventory=[]
def inv(element,kind,pos,first):
    inventory.append(dict(element=element,kind=kind,position=pos,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('Manuscript page number','text','top center, y25–50','10')
inv('Continued sentence','text','upper left, y95–159','ci inspirent.')
inv('Underlined heading','text','upper left, y190–264','Axiomes')
inv('Opening paragraph','text','upper body, y191–1051','On peut prendre pour ens de base ds une axiomatique des ateliers')
inv('Canceled comparative word','deletion','upper body, x237–415, y587–679','plus')
inv('Parenthetic authorial question','text','end of upper paragraph, y920–1036','(ou peut-être pareil pour M ?)')
inv('Underlined collection heading','text','middle left, y1120–1215','Sur F')
inv('Introduction to structure choices','text','middle, y1102–1290','on peut prendre comme structure de base, au choix')
inv('Display label, left brace and alternatives a–c','display','middle left, y1300–1490','(1.16); a) ≤, ≪; b) ≤, ≼; c) ≪')
inv('Dated objection','margin note','right of a/b, y1300–1405; rising handwriting',"(20. juin) Non, par mon nouveau point de vue ça n'implique plus ≪")
inv('Pointer from dated objection to b','margin note','x726–805, y1357–1390','left-pointing arrow to b)')
inv('Canceled sign in c','deletion','x665–710, y1412–1479','F / calligraphic F')
inv('Map in choice c','display','x737–1078, y1400–1468','et F → P(F)')
inv('Map notation and deployment gloss','text','right of c, y1380–1546','(notée F ↦ F-tilde, le déployement de F vu comme partie de F)')
inv('Brace attaching incidence gloss','display','x743–1065, y1491–1529','underbrace beneath et and map')
inv('Incidence relation gloss','display','below c, y1535–1735',"i.e. la relation d'incidence; ``F est une strate de G''; (i.e. F∈M et F≤G)")
inv('Canceled right-hand i.e. gloss','deletion','right middle, y1545–1609','i.e. la description/désignation')
inv('Earlier cancellation within right-hand gloss','deletion','right middle, x1275–1490, y1565–1609','description/désignation')
inv('Above-line replacement, itself later canceled','insertion','right middle, x1312–1615, y1546–1586',"relation d'inc.")
inv('Canceled lower paragraph opening','deletion','x233–298, y1788–1873','Je')
inv('Lower paragraph','text','lower body, y1749–1984','Avant de préciser ces points/ce point, je vais grouper dans un diagramme les six relations fondamentales dans F, en écrivant')
inv('Incidence definition and label','display','bottom, y1980–2092',"(1.17); F ◁ G; dfn above equivalence, par? below; ``F incident à G'' i.e. F≤G et F∈M")

unresolved=[
 dict(place='First family F',reading=r'\mathcal{F}',alternatives=[r'\mathfrak{F}'],confidence='medium',evidence='Letter identity F is clear; handwritten typeface correspondence remains uncertain in crop 03.'),
 dict(place='First M',reading=r'\mathcal{M}',alternatives=['M'],confidence='medium',evidence='Cursive peaks and rounded entry do not uniquely distinguish ordinary from calligraphic M in crop 03.'),
 dict(place='quand on reste',reading='reste',alternatives=['entre'],confidence='medium',evidence='The compressed low initial and middle strokes remain ambiguous after crop 07.'),
 dict(place='Canceled sign in (1.16)c',reading='F',alternatives=[r'\mathcal{F}'],confidence='low',evidence='Hatching obscures most letter structure in crop 10; cancellation itself is definite.'),
 dict(place='Canceled lower noun in right gloss',reading='description',alternatives=['désignation'],confidence='low',evidence='Deep looped descender and later t support description, but the earlier sequence is crossed out in crop 13.'),
 dict(place='Stop after inserted d’inc',reading="d'inc.",alternatives=["d'inc"],confidence='medium',evidence='The tiny raised terminal mark may be punctuation or a remnant of the cancellation line in crop 13.'),
 dict(place='Lower paragraph singular/plural wording',reading='ces points',alternatives=['ce point'],confidence='medium',evidence='Reduced terminal returns do not securely determine both s endings in crop 14.'),
 dict(place='First F operand of (1.17)',reading='F',alternatives=[r'\mathbb{F}'],confidence='medium',evidence='The doubled upper upright merges to one lower stem in crop 17; retracing is favored, intentional doubling remains possible.'),
 dict(place='Below the equivalence arrow of (1.17)',reading='par',alternatives=['unresolved word/arrow-overlap reading'],confidence='low',evidence='A p-like descending loop and smaller strokes overlap the left arrowhead in crop 16; no unique reading is recoverable.')
]

view_log=[
 dict(image=source,role='whole',viewed_utc='2026-11-20 10:54:22 UTC'),
 dict(image=str(base/'source/SP53_CW_156-6_scans/J156-6-02_156-6_scan011_a.jpg'),role='half_a',viewed_utc='2026-11-20 10:54:29 UTC'),
 dict(image=str(base/'source/SP53_CW_156-6_scans/J156-6-02_156-6_scan011_b.jpg'),role='half_b',viewed_utc='2026-11-20 10:54:53 UTC')]
view_times=['10:56:37']*3+['10:56:54']*3+['10:57:11']*3+['10:57:44']*3+['10:58:12']*3+['10:59:20']*2
for m,t in zip(manifest,view_times):
    view_log.append(dict(image=str(out/(m['name']+'.jpg')),role='crop',viewed_utc='2026-11-20 '+t+' UTC'))

report=dict(
 scan=11,reader='R3',status='complete',started_utc='2026-11-20 10:54:20 UTC',finished_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 model_identity='not exposed',model_effort='not exposed',view_log=view_log,differences=rows,c_doubts=c_doubts,s_rows=[],inventory=inventory,
 notes=[dict(
 content='The page continues a previous sentence and then discusses possible underlying sets for an axiomatization of ateliers: the family F, M, or L. It contrasts the simplicity of the data with transparency of the essential axioms. It gives three proposed structures on F in (1.16), annotates choice b) with a dated objection, explains a map to a power set through deployment and incidence, and introduces the incidence relation in (1.17) before an intended diagram of six fundamental relations. The intended diagram is not drawn on this page.',
 math_reading_decisions='The two straight left-angle signs are \\ll; the curved order sign with curved lower rule is \\preccurlyeq. P is plain upright here. The map has a simple right arrow and the element notation has an initial vertical bar and tilde. The brace begins under et, not under \\ll. The incidence triangle is closed and points left. The defining equivalence has clear dfn above and an uncertain par-like mark below. The same conjunction F≤G and F∈M appears in the incidence gloss and definition. Singular le plus transparent is retained literally. No mathematical repair is made for typography, compressed prose, the canceled sign, or the doubled/retraced F.',
 author_doubts=["(ou peut-être pareil pour M ?)","(20. juin) Non, par mon nouveau point de vue ça n'implique plus ≪"],
 titles_dates_counts='Manuscript page number 10. Underlined titles Axiomes and Sur F. A dated note reads 20. juin, with no year. Two labeled displays, (1.16) and (1.17); three alternatives a), b), c); the prose announces six fundamental relations. No archive pencil number, separate drawing, actual diagram, or typed sheet text is present.'
 )],
 check_events=[
 dict(statement_id='scan011-axiomatic-base-comparison',type='carried as background without fault found',outcome="Read as the author's assertion; no mathematical verification performed."),
 dict(statement_id='scan011-1.16-choices-and-dated-objection',type='carried as background without fault found',outcome="Read as the author's proposal and later objection; no mathematical verification performed."),
 dict(statement_id='scan011-1.17-incidence-definition',type='carried as background without fault found',outcome="Read as the author's definition; no mathematical verification performed. Matching the two written conjunctions was a transcription comparison, not a proof check.")],
 notation_proposals=[
 dict(sign='family F',latex=r'\unsure{\mathcal{F}|\mathfrak{F}}',ink='Wide sloping top arm, curved middle arm and single bent stem; first occurrence crop 03, recurring throughout.',alternatives=[r'\mathfrak{F}']),
 dict(sign='collection M',latex=r'\unsure{\mathcal{M}|M}',ink='Broad curved entry, two high peaks, rounded trough and long downstroke; crop 03 and later half views.',alternatives=['M']),
 dict(sign='power-set P',latex=r'\mathrm{P}',ink='Plain upright and upper bowl in (1.16)c; no ornament beyond handwriting.',alternatives=[]),
 dict(sign='subdivision order',latex=r'\preccurlyeq',ink='Curved upper cusp and separate curved lower rule in row b), read in half b.',alternatives=[]),
 dict(sign='incidence',latex=r'\triangleleft',ink='Closed leftward triangle with tall right edge in crop 17.',alternatives=[]),
 dict(sign='first F of (1.17)',latex=r'\unsure{F|\mathbb{F}}',ink='Two upper upright strokes merge to one lower stem; crop 17. No cancellation stroke is inferred.',alternatives=[r'\mathbb{F}'])],
 abbreviations=[dict(form='ens',expansion='ensemble'),dict(form='ds',expansion='dans'),dict(form='i.e.',expansion='id est'),dict(form='dfn',expansion='définition'),dict(form="d'inc.",expansion="d'incidence")],
 unresolved=unresolved,brief_feedback=[]
)
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(rows),'c_doubts':len(c_doubts),'inventory':len(inventory),'unresolved':len(unresolved),'actual_crops':len(manifest),'actual_image_views':len(view_log),'finished_utc':report['finished_utc']},ensure_ascii=False))
