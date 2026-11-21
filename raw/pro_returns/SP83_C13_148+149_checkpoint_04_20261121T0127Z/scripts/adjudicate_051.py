from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan051'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
E={
'B01':'The dark current digit has the upper bar, diagonal descent and transverse bar of 7. A separate older closed loop survives underneath; candidate 6 remains uncertain. The second reading does not account for that overwritten layer. The original black top edge limits certainty about the old digit, not the presence of the revision.',
'B02':"The group after the parenthesis has ou, then a q-descender, apostrophe and on before dispose; on peut disposer does not fit the word divisions or ending. The small sign after correspondant has an upper stroke/dot and a lower compact mark, so à versus colon is newly left explicit. The raised de is clear but its insertion state remains uncertain. L’une ends with a small e turn; the single dash after omega(a) is not an equality pair.",
'B03':'The verb after ordinaire ends in the compact que group, without an additional ons sequence: indique. The next line has en followed by the broad m, small a, dotted i and ns of mains, not réserve. The a-in-A expression agrees.',
'B04':'The crossed short word after décrire has surviving low humps, but the strike obscures its internal letters. Both aussi and comme remain possible outlines; neither is resolved. The polygon labels Pa and Ra and both unpunctuated ens abbreviations are clear.',
'B05':"The pronoun before donner has the tall looped l and low a of la, rather than se. The following word has d-apostrophe, em, high bl and accented ending, d’emblée. The last live article is un without a separate e. Under the strike, qui serait is visible; a d-like ascender, low un and t-bearing final group continue to favour dans un contour, but the cancelled wording remains doubtful and is not replaced by an invented certain ensemble/système.",
'B06':'The underlined phrase has contour with its internal t and the longer combinatoire with the b/n/t sequence; it does not read autre condition. The word before the quotation has an initial p-descender and tall l, supporting plutôt rather than dits. The R has both its lower bar and upper rightward arrow. De repères and avec une remain as first read.',
'B07':'The double-stem D, infinity, sigma indices 0/1, raised squares, equality signs and terminal 1 agree. Only the outer math delimiters differ.',
'B08':'A single rightward arrow labelled epsilon goes from double-stem D-infinity to brace-enclosed plus/minus 1. The independent diagram wrapper represents the same symbols.',
'B09':'Both R occurrences carry lower bars and upper arrows. The first has raised plus and lowered cursive l, repeated after vector A. Using l versus ell and reversing nesting of underline/vector macros changes no written symbol; the established l convention is retained.',
'B10':'The first line ends des; the next has contours with a small final s. The last adjective ends in a tall t followed directly by the point, without an s. Des contours correspondant is therefore retained without grammatical regularization.',
'B11':'The note begins with vector A and lowered cursive l. After recollement a separate curling s-like end descends; the outer closing parenthesis occurs on the next line. The final prose group is looped l followed by low es, not a capital C with an a index. The overwritten sign before X remains unresolved under partial uncertainty. The first note wording and anchor are retained.',
'B12':'The pale lower-left folio has a curved 5 followed by an oval 0. The mspage wrapper records the same 50.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
rs={'B02':[(r'correspondant à un',r'correspondant \unsure{à|:} un')],'B04':[(r'\deleted{\unsure{aussi}}',r'\deleted{\unsure{aussi|comme}}')]}
pp=R/'pages'/f'{p}.tex';page=pp.read_text()
for b,repls in rs.items():
 s=C[b]['first']
 for a,z in repls:
  assert a in s and a in page,(b,a)
  s=s.replace(a,z);page=page.replace(a,z)
 D[b].update(choice='reading',reading=s)
pp.write_text(page)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
for x in r['changes']:
 if x['id']==p+'-08':x.update(final=r'\deleted{\unsure{aussi|comme}}',evidence=E['B04'],crop=f'crops/{p}_second_B04.png')
for x in r['doubts']:
 if x['place']=='cancelled word after décrire':x.update(reading=r'\deleted{\unsure{aussi|comme}}',alternatives='aussi; comme; internal letters obscured',reason=E['B04'])
r['doubts'].append(dict(place='opening parenthesis, after correspondant',reading=r'\unsure{à|:}',alternatives='à; colon',confidence='medium',reason='The compact lower mark and separated upper stroke do not securely distinguish the reduced accented letter from two-dot punctuation.'))
r['notes'].append(dict(id=p+'-N-audit',text='Independent crop comparison retains the literal des contours correspondant and the overwritten upper folio layer. It leaves à versus colon explicit after correspondant and adds comme as an alternative to the already doubtful cancelled aussi; neither uncertainty-only change adds a witness-error count. The local vector/underline nesting and l/ell spelling are typographical equivalents.'))
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json'}
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
