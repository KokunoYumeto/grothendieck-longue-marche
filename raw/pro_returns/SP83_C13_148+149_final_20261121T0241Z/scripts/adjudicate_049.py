"""Main reader's explicit decisions after viewing all thirteen second crops."""
from pathlib import Path
import json
from datetime import datetime, timezone
R=Path(__file__).resolve().parents[1]
p='148_scan049'
cmp={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
evidence={
'B01':'The dark heading has a 5 and closing parenthesis. The difference is only the manuscript-page wrapper.',
'B02':'The short group after opération has a looped d followed by e, not en. The last low stroke of somme does not securely isolate or exclude a terminal s; the first uncertainty is retained.',
'B03':'The cancelled short group after X remains est under uncertainty. Gamma and full-height MD, the double implication, and tilde over Sigma are visible. The readings differ in text/math wrappers and font coding only.',
'B04':'The relation has a wavy upper and straight lower stroke; both pi subscripts are 0. Gamma MD is on the baseline and Sigma bears a tilde. Delimiter and font coding do not change the reading.',
'B05':"On the oblique marginal baseline after est, the crop shows a separate looped d, low onn, accented é, then a descending p and ar: donné par. Both witnesses and the first reading omit these words. The opening has d’un without a separate e; indice begins with a dotted i, without l-apostrophe; H has a raised 1. The cancelled lower formula remains uncertain. The first curved-link geometry is retained.",
'B06':'The item has a small looped a with a closing parenthesis. After the dash, dotted i and a small e-shaped curve with stops support i.e., not ici. The diagonal cancellations leave the old category/star unresolved; the live phi-shaped empty-set sign and boundary formula agree.',
'B07':'The inserted adjective has the compact l-i-b-r-e-s sequence, not the longer extérieures. The crossed word after MD has q with descender and low ue; que is retained. The insertion line attaches before tous les sommets, and Ce graphe sits over crossed Il. The left edge touches the first insertion but the visible remainder and first crop record preserve toutes.',
'B08':'Both A accents have rightward heads and the two relations are simeq and equals. The upper map label has a short stem and shoulder r, without the descender of rho. The final superscript touches the vector accent: its open/angled strokes do not securely distinguish sigma from a star. Sigma remains first, following the local involution notation, but the exponent is now explicitly uncertain.',
'B09':'After correspond there are two colon dots, then initial c, a tall h, low oi, a dotted i and a final r: choisir. The second line reads situation and donnée with the compact donn group, not a longer replacement. The first wording is retained.',
'B10':'The first object is A=A with lowered 0; a downward arrow reaches S and a rightward gamma-labelled arrow reaches N. A dark terminal point lies to the right of N. The competing encodings position the same point through different macro boundaries.',
'B11':'There are five dark vertices and respectively 3,0,0,4,1 rays. The third label has the shallow cursive 2; the last has a compact angular 4 consistent with the numbered sequence, rather than an additional letter label. The tiny white centre of the g3 dot is a paper gap, not a separately outlined open vertex. The enclosure ends in a left-pointing lower head. Equivalent approximate geometry is retained.',
'B12':"The long stroke through type (g,nu) d’une continues beneath structure; it is one cancellation stroke, not a separate intentional underline of structure. Le cas d’une lies above the cancelled opening and keeps its probable insertion state. The old participle has a D-like initial and remains doubtful; the thin line across the raised caractérisé leaves its cancellation uncertain. A lower par is crossed with the old le genre, and a second par la donnée des is written above that line: the deletion and insertion scopes are corrected. The compact card c is lower case; the lifted i.e. S={s} attaches at S=1. No additional surface can be read in the crossed opening.",
'B13':'The pale lower-left number is an open angular 4 followed by a two-loop 8; only the page-number wrapper differs.'}
dec={b:{'choice':'keep_first','viewed':True,'evidence':evidence[b]} for b in evidence}
changes={
'B05':[(r'\uline{genre total} est',r'\uline{genre total} est donné par')],
'B08':[(r'\vec A^\sigma',r'\vec A^{\unsure{\sigma|*}}')],
'B12':[(r'\uline{structure}','structure'),(r'par \deleted{\unsure{le genre}} la donnée des',r'\deleted{par \unsure{le genre}} \inserted{par la donnée des}')]
}
pagepath=R/'pages'/f'{p}.tex'
page=pagepath.read_text()
for b,replacements in changes.items():
    final=cmp[b]['first']
    for old,new in replacements:
        assert old in final,(b,old)
        assert old in page,(b,old)
        final=final.replace(old,new)
        page=page.replace(old,new)
    dec[b].update(choice='reading',reading=final)
pagepath.write_text(page)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json'; rec=json.loads(rp.read_text())
byid={x['id']:x for x in rec['changes']}
for num,b in [(19,'B08'),(24,'B12'),(28,'B12')]:
    row=byid[f'{p}-{num:02}']
    row['evidence']+=' Independent audit: '+evidence[b]
    row['crop']=f'crops/{p}_second_{b}.png'
byid[p+'-19']['final']=r'A\ (\simeq\vec A=\vec A^{\unsure{\sigma|*}})'
byid[p+'-19']['confidence']='medium'
byid[p+'-24']['final']=r"\inserted{Le cas d'une} structure connexe"
byid[p+'-24']['evidence']=evidence['B12']
byid[p+'-28'].update(c=r'par \deleted{\unsure{le genre}} la donnée des',h='par la donnée de',final=r'\deleted{par \unsure{le genre}} \inserted{par la donnée des}',diff_c=True,diff_h=True,kind='insertion or placement',error_kind='Insertions put in the wrong place',confidence='medium',evidence=evidence['B12'])
rec['changes'].append(dict(id=p+'-34',place='Oblique margin, after genre total est',c='absent',h='absent',final='donné par',diff_c=True,diff_h=True,kind='omission',error_kind='Omissions',evidence=evidence['B05'],crop=f'crops/{p}_second_B05.png',box=[18,625,601,1592],confidence='high',marked_in_h=False,consequential=False))
rec['doubts'].append(dict(place='first diagram, exponent of final vector A',reading=r'\sigma',alternatives='*',confidence='medium',reason='The superscript touches the vector accent; its outline is not sufficient to decide sigma against a star in isolation. The local involution notation favours sigma without eliminating the visual doubt.'))
for x in rec['inventory']:
    if x['element']=='E27': x['first_words_or_objects']=r'\deleted{par \unsure{le genre}}'
rec['inventory'].append(dict(element='E30',sheet_kind='text',hand='his hand',kind='insertion',position='Bottom paragraph, above cancelled par le genre',first_words_or_objects=r'\inserted{par la donnée des}',transcribed='yes'))
rec['notes'].append(dict(id=p+'-N09',text='Independent audit restores donné par after est in the oblique genus note, a phrase absent from both witnesses. It removes an inferred underline under structure: the line belongs to the cancellation of the preceding old phrase. It distinguishes the crossed lower par le genre from the raised par la donnée des. The final vector-A superscript in the first diagram is now sigma|star under uncertainty. These are visual decisions, not mathematical corrections.'))
rec['second_main_review']={'viewed_boxes':list(evidence),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json'}
rp.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
