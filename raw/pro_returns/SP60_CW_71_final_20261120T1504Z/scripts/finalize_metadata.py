"""Final consolidation of the primary reader's metadata; never changes a page file.
Run only before the transcription freeze: render() rewrites the combined fragment.
"""
from record import *

def write_rows(name,data):
 with (ROOT/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=HEADERS[name],delimiter=',' if name.endswith('.csv') else '\t')
  w.writeheader();w.writerows(data)

def upsert(name,key,value,fields):
 data=rows(name)
 matches=[r for r in data if r[key]==value]
 if matches:
  assert len(matches)==1
  matches[0].update(fields)
 else:
  data.append({**dict.fromkeys(HEADERS[name],''),key:value,**fields})
 write_rows(name,data)

# Identify observed layers, without attributing the memoir or pencil to a person.
main='another unnamed hand (main memoir; identity unverified)'
annotation='another unnamed hand (annotation layer; identity unverified)'
invrows=rows(PREFIX+'_inventory.csv')
for r in invrows:
 s=int(r['scan']);e=r['element']
 r['hand']=main
 if r['kind']=='margin note':r['hand']=annotation
 if s==41:r['hand']='another unnamed hand (unfinished draft; identity unverified)'
 if s==46:
  r['hand']='another unnamed hand (pencil sketches; identity unverified)' if r['kind']=='drawing' else 'another unnamed hand (inverted ink fragment; identity unverified)'
 if e in ['047-04','047-12','047-14','048-11']:r['hand']=annotation
 if e=='044-06':r['hand']='another unnamed hand (inserted ink reference; enclosure unattributed)'
 if e=='040-22':r['hand']='another unnamed hand (isolated pen stroke; identity unverified)'
write_rows(PREFIX+'_inventory.csv',invrows)

# Replace stale first-page scope language with the completed cross-page comparison.
upsert('notation.tsv','notation',r'\varnothing',{
 'form_and_use':'Oval crossed by a long nearly vertical stroke, consistently denoting the empty set.',
 'places':'38–40, 42–45, 47; every empty-intersection occurrence compared in the second reading',
 'ambiguity_consistency':'The φ-like shape is used in set-valued expressions throughout. No independent scalar φ is introduced on these pages. All such signs use \\varnothing; neither 41 nor 46 contains an empty-set expression, and 48 has none.'})
upsert('notation.tsv','notation','Roman page and lemma numbers',{
 'form_and_use':'Roman numerals often have short upper and lower rules; unruled references remain unruled.',
 'places':'38–40, 42–45, 47–48: manuscript XI–XIX; lemma references XII–XXI and earlier references',
 'ambiguity_consistency':'Rules and circles are preserved occurrence by occurrence, including circled XIV on 44. The overwritten earlier folio on 39 remains uncertain. No manuscript folio is supplied for 41 or 46.'})
upsert('notation.tsv','notation',r'\operatorname{int},\operatorname{ext},\operatorname{Ext}',{
 'form_and_use':'Main text usually has lowercase int/ext; pencil formula on 38 has Ext. The first interior word in the final U formula on 43 remains Int|int.',
 'places':'38–45, 47–48; compared across both C folders during the second reading',
 'ambiguity_consistency':'Capitalization is kept by occurrence. \\mathrm and \\operatorname are equivalent typesetting choices here, not different readings. Clear U/V slips and the parent Γ/Λ switches are not regularized.'})
upsert('notation.tsv','notation','Cross-page comparison: letters, primes and indices',{
 'form_and_use':'Γ is a corner-shaped capital; Λ has two legs without a bar; A has a crossbar. Numeral 1 has a hooked head; primes are short raised strokes, sometimes nearly vertical.',
 'places':'38–45, 47–48; especially Γ/Γ′ on 43, Λ¹′ on 47, Λ¹⁽ⁿ⁾ and card A¹⁽ⁿ⁾ on 48',
 'ambiguity_consistency':'Each supplied page was checked again. Unprimed Γ and later Γ′ on 43 remain distinct. The crossed 4|1 places on 42 and 45 remain doubtful. The first Λ¹′ on 47 retains its low point and alternative exclamation reading; clear later occurrences agree. Literal A¹⁽ⁿ⁾ on 48 stays A.'})
upsert('notation.tsv','notation','Cross-page comparison: enclosures, points and underlines',{
 'form_and_use':'Words are underlined where ruled; numerals may have two rules; additions may have a surrounding curve, lower attachment rule, or notch. Isolated points are distinct from primes and from cancellation.',
 'places':'38 margin formula; 39 ditto marks; 42 enclosure and underbrace; 43 dotted x/y; 44 dotted p and word-division dot; 45 dotted minus; 47–48 annotations',
 'ambiguity_consistency':'The second reading compared these marks without assigning a mathematical meaning where none is stated. The circle over triangle on 47 denotes interior in that expression; it is not silently propagated to other triangle statements.'})
upsert('hand.tsv','habit','An empty-set sign resembles φ: a small oval with a long through-stroke.',{
 'places':'38–40, 42–45, 47; all occurrences of the empty-set notation',
 'scope':'The same set-valued use holds throughout the supplied occurrences. Orientation of the through-stroke varies; interpretation does not depend on inclination alone.',
 'witness_errors':'C repeatedly retained varnothing|phi uncertainty; resolved without changing its first reading. H’s emptyset spelling is a macro difference and is not counted.'})
upsert('hand.tsv','habit','The grave-like accent in théorème is drawn as a shallow concave arc.',{
 'places':'38 title; 40 main induction sentence',
 'scope':'These two locally ambiguous concave forms were retained; other theorem accents on 40 and 44 are flatter. No universal accent equivalence is asserted.',
 'witness_errors':'C preserved a breve/grave doubt at these two places; retained after checking rather than normalized.'})

# Correct only a documentary escape in an alternative, not the manuscript text.
ds=rows('doubt_records.tsv')
for r in ds:
 if r['scan']=='43' and r['place']=='Il y':r['alternatives']=r"\'{y}; plain y"
write_rows('doubt_records.tsv',ds)

(ROOT/'abbreviations.md').write_text('''## Abbreviations and short forms

Expansions below are editorial explanations only; none has been inserted into the transcription. Mathematical single-letter names are listed in the notation table rather than expanded in the text.

| Written form | Scans / place | Probable meaning or limit |
|---|---|---|
| cf. | 38, 42, 47 | confer; compare / see the cited remark or lemma |
| coroll. | 38, opening reference | corollaire |
| resp. | 38–39, 42–45 | respectivement |
| def. | 40, 44–45, 47 | définition; the page's numeral and spacing are retained |
| i.e. | 44, interior visibility | id est; c'est-à-dire |
| nb | 47, pencil addition to XX | nombre; only n and b are written |
| c.q.f.d. | 38–40, 45, 47–48 | ce qu'il fallait démontrer |
| c.q.s.d. | 43, proof ending | Probably intended as a proof-ending formula like c.q.f.d.; no secure literal expansion of the written s is established. The s is retained. |
| etc | 47, parenthetic disk argument | et cetera; the preceding run of points remains as written |
| int, Int | 38–45, 47–48 | intérieur; the capital I on 43 remains doubtful |
| ext, Ext | 38–40, 42–45, 47–48; capital form in pencil on 38 | extérieur; capitals are preserved by occurrence |
| card | 40, 44, 48 | cardinal, the number of elements of the indicated finite set; missing cardinal operators elsewhere are not supplied |
| s. (doubtful) | 48, last line of the pencil criticism | Possibly an abbreviated ses, but both the reading and expansion remain uncertain; the alternative ses is retained in place. |

The notation J-polygone is retained as a defined class invoked by the memoir. Its full definition is outside this excerpt, so no expansion is supplied here. The mathematical names E(Γ), S(Γ), A(Γ), and R_{Λ²} are respectively used for the convex envelope, vertices, edges, and the explicitly defined closed interior region; these roles follow the supplied pages.
''',encoding='utf-8')
(ROOT/'legibility.md').write_text('''## Legibility, witness coverage, and limits

Most of the main text is readable, including the repeated formulas, small endpoint indices, and ordinary insertions. The principal difficulties are retraced superscripts, densely cancelled tokens, flat or curved accent marks, the slanted pencil annotations, and the final flourished signature. A large enlarged crop does not recover ink completely buried by hatching. The least secure readings remain visibly marked in the transcription and in the remaining-doubts table: especially the cancellations on 38, 43 and 47; the overwritten 4/1 exponents on 42 and 45; the first dotted Λ¹′ on 47; the last line of the pencil criticism and the signature on 48. No identity is inferred from that signature.

The main memoir and the marginal annotation layers have different visible appearances. H calls the memoir another hand, but that editorial description is not a verified personal attribution. The inventory and hand log use unnamed hands with layer descriptions. They do not establish that all additions are by one annotator or that any specific hand is Grothendieck's. The two sketches on 46 and the inverted fragment also remain unattributed.

C provides the continuous diplomatic text and most of the already marked cancellations and doubts. Many of its first readings were retained after direct comparison, while the changed places include unmarked omissions of rules, points and attachment lines as well as doubtful words or indices. H supplies source annotations on only 38, 47 and 48, with short quotation locators; its main-body descriptions are editorial synopses. Its missing source blocks are coverage gaps, not failed attempts at the omitted readings. Recoveries from H's illegibility placeholders are sometimes only partial and remain doubtful. The feedback file separates those counts; witness agreement was never treated as evidence in place of the scan.

The primary reader completed both readings of all 11 scans in order. Scans 38–40, 42–45 and 47–48 carry manuscript folios XI–XIX; 41 is an unfinished unnumbered fragment and 46 an unnumbered sketch sheet. This observed sequence is not a source declaration of the memoir's total length. Scan 41's writing and scan 46's fragment are inverted relative to their archival numbers. The date on 48 is 15 July 1976, Montpellier. No material beyond the supplied pages was researched, no OCR was used, and no TeX compilation was performed.

Clear source irregularities are preserved: the g endpoint on 39, the repeated exterior index on 40, the opposing inclusion on 41, the Γ/Γ′ and U/V changes on 43, the repeated V on 44, the common-chord problems and final self-exterior index on 45, the endpoint mismatch on 47, and the set/cardinal expressions on 48. Notes distinguish targeted checks, conditional arguments and counterexamples from steps merely read or left unproved. They are not a certification of the manuscript's proofs.
''',encoding='utf-8')

p=ROOT/(PREFIX+'_notes.md');s=p.read_text(encoding='utf-8')
s=s.replace('Pencil adds “non consécutifs si p = nb de cotés de Γ ≥4,” and “interieurs des”.','Pencil adds “non consécutifs si p = nb de cotés de Γ ≥4,”; a separate interlinear insertion supplies “interieurs des”.')
# Keep the second-reading addition under its own scan instead of after scan 48.
extra='\n### Second-reading addition — scan 44\n\nThe last word is divided after `autre`, with a separate raised dot before `ment` resumes on the next line. The dot is retained without interpreting its purpose; 044-C08.\n'
s=s.replace(extra,'')
s=s.replace('\n## Scan 45\n',extra+'\n## Scan 45\n')
p.write_text(s,encoding='utf-8')

# Make refined-statement identifiers explicit in event types, leaving the actual
# first-reading timestamps and outcomes intact.
ev=rows('CHECK_EVENTS.tsv')
for r in ev:
 ident=r['statement_id']
 refinements={'043-N1':'043-N1-refined','043-N3':'043-N3-refined','045-N1':'045-N1-refined','045-N2':'045-N2-refined','047-N2 / closed-triangle inclusion':'047-N2-R','048-N2':'048-N2-R'}
 if ident in refinements:r['type']='refuted, with refined statement id '+refinements[ident]
write_rows('CHECK_EVENTS.tsv',ev)
if not any(r['statement_id']=='045-N4 / conditional disk step' for r in ev):
 event('045-N4 / conditional disk step','targeted proof check','Conditional local step: if x lies on Λ¹ and in the open exterior of Λ², choose a sufficiently small admissible disk contained in that exterior; the local boundary property supplies a point of intΛ¹. An interior polygonal path is available under the stated connected-open interior hypothesis. The false earlier boundary-separation premise is not certified.')

# Rebuild H's exact projection after any decision edits.
hr=[]
for r in rows('decisions.tsv'):
 if r['against_H']=='yes':
  n=int(r['scan']); assert n in (38,47,48)
  hr.append(dict(zip(HEADERS[PREFIX+'_collation.tsv'],['J71-05' if n<=42 else 'J71-06',n-1,n,r['place'],r['H'],r['C'],r['final'],r['scan_shows'],r['kind'],r['marked_in_H'],r['confidence']])))
write_rows(PREFIX+'_collation.tsv',hr)
render()
print('Metadata consolidated; page files unchanged. Combined fragment regenerated before freeze.')
