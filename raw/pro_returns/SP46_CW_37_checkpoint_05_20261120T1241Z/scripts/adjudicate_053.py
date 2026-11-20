from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan053/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC'];ds=copy.deepcopy(A)
cm=[0,1,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21]
for i,d in enumerate(ds):
 d['readers']={'A':A[i]['reading'],'B':B[i]['reading'],'C':C[cm[i]]['reading']}
 d['c_doubt']=i in [3,7,12,13,15,17,18]
 d['marked_in_H']='yes' if any(x in str(d['h_reading']) for x in ['\\uncertain','\\ill']) else 'no'
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
 if d.get('crop'):d['crop']=f'readers/scan053/A/{Path(d["crop"]).name}'
def up(i,**kw):ds[i].update(kw)
mc=lambda s:f'crops/scan053/{s}.jpg'
up(0,crop=mc('letterhead'),scan_shows='Two printed capital lines read INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES, including the acute on É. H describes the stationery but does not transcribe its printed text.')
up(1,crop=mc('letterhead'),scan_shows='A separate short thick horizontal printed rule is centered below the second printed line; it is absent from H’s transcription.')
for i,name,numeral in [(2,'xiii','XIII'),(8,'iv','IV'),(10,'x','X'),(11,'xiv','XIV')]:
 up(i,crop=mc(name),kind='drawing or diagram',scan_shows=f'The individual diagonals/uprights read {numeral}; separate horizontal strokes are visible above and below. H’s italics convention can stand for underlining, but does not record the additional upper rule. This row concerns that graphic omission, not the italic macro itself.')
up(9,kind='drawing or diagram',scan_shows='V followed by two distinct uprights reads VII, with independent upper and lower rules. H’s italic convention for underlining does not record the additional upper rule.')
up(3,scan_shows='Large C and joined o-m-m-en-t-ai-r sequence are visible; the terminal e/s strokes are compressed into a short wavering trace. Retain Commentaires|Commentaire.')
up(4,crop=mc('quotes'),scan_shows='Two short upright strokes precede cristallin; two curved high strokes follow it, then a separate lower comma. They are paired quotation strokes, not angle-shaped guillemets.')
up(5,reading=B[5]['reading'],diff_c=True,crop=mc('bracket'),scan_shows='Both short arms project left. The long stem is nearly vertical at the top, then bends right toward the words near its foot. B’s curved path better preserves this change of direction than C’s straight diagonal; H only describes the bracket.')
up(7,scan_shows='Several heavy rising cancellation strokes cover the first letters and baseline. Small surviving loops do not determine a complete word; retain one cancelled illegible word.')
up(12,scan_shows='The word’s tall P, b and l and low ending support Problèmes. The small almost vertical accent trace does not determine grave versus acute; add Problémes as an explicit allowed alternative.')
up(13,scan_shows='The tall initial C and compressed middle lead to two reduced terminal waves before the closing parenthesis. A final s cannot be isolated securely; retain Commentaires|Commentaire.')
up(15,reading=r'\unsure{Variantes|variantes}',confidence='medium',unresolved=True,alternatives='lowercase variantes',scan_shows='The initial looped V rises above the following low a and has a broad deep bend, favouring a capital. Its case remains less secure than A judged because size varies in this handwriting; retain the lowercase alternative.')
up(17,scan_shows='An initial low cup and following joined uprights favour u-n-e; the final stroke is long and reduced. The form mes is not securely excluded. Prefer une|mes rather than C’s mes|une; H’s uncertain une is the same preferred word, but its alternative is not recorded there.')
up(18,scan_shows='Low n-o strokes precede a tall t and a compressed final e-like tail. No distinct separate s is certain; prefer note|notes rather than C’s notes|note. H’s uncertain note shares the preferred reading but does not record the plural alternative.')
for i in [6,14,16,19]:
 ds[i]['scan_shows']+=' All three readers independently confirmed this C-context inspection target on their halves or specified crop; there is no substantive witness difference.'
bold=copy.deepcopy(C[2]);bold.update(crop=mc('five'),marked_in_H='no',readers={'A':'SGA 5','B':'SGA 5','C':C[2]['reading']},scan_shows='The digit 5 is substantially heavier and more extensively retraced than the adjacent SGA letters, with a broad filled bowl and upper bar. Preserve that emphasis as textbf on this handwritten heading; this is not a claim of bold type in a typescript.')
ds.insert(2,bold)
archive=copy.deepcopy(B[20]);archive.update(diff_h=False,kind='other',crop='',marked_in_H='no',readers={'A':'Archive 52 as comment','B':B[20]['reading'],'C':C[22]['reading']},scan_shows='All three readers identify lower-left 52 as archive pagination. H’s page wrapper and the consolidated comment encode the same metadata; this is not counted as a textual difference.');ds.append(archive)
for d in ds:
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
s=(O/'readers/scan053/B/reading.tex').read_text().replace(r'SGA 5\qquad',r'SGA \textbf{5}\qquad',1)
(O/'pages/H37-01_37_scan053.tex').write_text(s)
inv=copy.deepcopy(R['B']['inventory'])
for x in inv:
 if x['hand']=='unnamed hand' and '52' not in x['first_words_or_objects']:x['hand']='his hand'
 x['kind']={'text block':'text','archive number':'text','archive pagination comment':'text'}.get(x['kind'],x['kind'])
notation=copy.deepcopy(R['B']['notation'])
notation[-1]['latex']=B[5]['reading']
notes='One manuscript leaf on the printed INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES letterhead. Three entries concern SGA 5 / XIII and comments on the crystalline case, including congruence formulae mod p; IV and the relative case, with consultation of VII and SGA 6 / X; and XIV, headed “Problèmes et Commentaires” with reader doubts, followed by a reminder about mod p and crystalline variants and an uncertain reference to “une note” concerning “th. de Katz”. No actual congruence formula or proof appears. The page has one heavily cancelled unreadable item, one grouping bracket and the printed rule. No date, authorial page number, total page count or explicit authorial doubt mark is visible. “Faire attention au cas relatif, consulter” is an editorial direction, not a statement of a verified result. The lower-left 52 is archival and appears only as a comment. Hand attribution follows the supplied dossier, not an independent authentication. Uncertainty about endings, accent direction, capitalisation and the final two words belongs to the readers, not to the author.'
out=dict(scan=53,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=['The five references XIII, IV, VII, X and XIV were read by counting the individual strokes; no expected SGA reference was substituted.','Both mod p expressions have a separate lowercase p with a descender. The abbreviation is preserved and no exponent or congruence relation is supplied.','The allusion th. de Katz is retained without deciding whether th. expands to théorème or thèse. No mathematical proof, computation or external background check was performed.'],notation=notation,abbreviations=R['B']['abbreviations'],slips=[],check_events=[],main_crops=json.loads((O/'crops/scan053/manifest.json').read_text()))
(O/'decisions/scan053.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Wrote scan 053:',len(ds),'decision rows; seven explicit C uncertainties.')
