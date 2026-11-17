"""Root's pre-context notation/register cleanup, after all 34 visual audits."""
from pathlib import Path
import json,csv
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
# The same visible underlining uses one requested diplomatic macro throughout.
changed=[]
for p in sorted((root/'pages').glob('*.tex')):
    old=p.read_text(); new=old.replace('\\underline{','\\uline{')
    if old!=new:
        p.write_text(new);changed.append(p.name)
(root/'MPL_116+117_transcription.tex').write_bytes(b''.join(p.read_bytes() for p in sorted((root/'pages').glob('*.tex'))))
p=root/'working/doubts.jsonl'; rows=[json.loads(s) for s in p.read_text().splitlines() if s.strip()]
translations={
'premier diagramme':('first diagram','Hom(A,M), f^M, g^M','First A overwritten; former subscripts A struck out.'),
'après et':('after et','les (deleted)','Small struck word; probable reading.'),
'première ligne barrée':('first deleted line','demander de trouver','Second verb crossed through; replaced by proposer d’obtenir.'),
'après H, mots barrés':('after H, deleted words','Pour; S’il y en a','Successive heavily crossed-out attempts.'),
'au-dessus du diagramme':('above the diagram','une définition (deleted)','relation; the enlarged audit favours définition, but cancellation obscures the middle letters.'),
'coefficient des modules':('module coefficient','k','h; cursive letter, now locally marked k|h at all three occurrences.'),
'marge près diagramme topoi':('margin beside the topos diagram','induisant (L f°*)','Possible top subscript inside the parenthesis.'),
'fin moitié gauche':('end of the left half','pas dur','pas abs.; enlarged inspection suggests a d-stem in the second word, but the rapid ending remains uncertain.'),
'après supplémentaires':('after supplémentaires','de la théorie (deleted)','Several overwritten letters.'),
'annotation oblique':('oblique annotation','les deux propriétés impliquent la commutation aux sommes et produits des g_H*','The fragments run diagonally; several words remain indistinct.'),
'variable sous intégrale':('variable under the integral','ξ','ζ; long cursive form, with the alternative retained.'),
'adjoint à, ratures':('adjoint à, cancellations','droite then gauche then gauche','Two superimposed deleted states; probable visual order.'),
'formule après devient':('formula after devient','p₀! i! ≃ p!; p₀i=p','j! and p₀j are mathematically expected, but the stroke is read as i; no mathematical correction made.'),
'marge catégories filtrantes':('margin on filtered categories','Et foncteurs cofinaux entre icelles','cofinaux is indistinct.'),
'petit encadré':('small box','diagrammes co [variants] à cat.','Fragmentary words and a connecting arrow.'),
'bord inférieur renversé':('upside-down lower edge','Théorie / Flèches [one word] flèches / fibres II','Very pale pencil beneath cancellation; one word physically unreadable.'),
'ligne 2':('line 2','de réunion A','Apparent repetition of line 4; retained.'),
'objets dans les Hom':('objects in the Hom expressions','ξ,η','ζ is an alternative for ξ; the same long cursive sign recurs on scan 022 and remains marked locally.'),
'dernière ligne':('last line','tt élément','tout élément; the visible form is abbreviated tt.'),
"tampon de réception":('reception stamp','ARRIVEE','ARRIVÉE; broken ink.'),
'P.S. dernier membre':('last clause of the P.S.','où de l’I.N.S.E.R.M.','ou; visible accent or reproduction blemish, preserved as où.'),
}
for r in rows:
    if r['line'] in translations:
        r['line'],r['reading'],r['alternatives']=translations[r['line']]
    if r['cote']==117 and r['scan']==18 and r['line']=='condition (ii)':
        r['alternatives']='X′; right edge cropped and prime indistinct.'
    if r['cote']==117 and r['scan']==19:
        r['alternatives']='Savoyaut; uncertain surname, without biographical normalization.'
    if r['cote']==117 and r['scan']==25 and r['line']=='isolated small diagram':
        r['reading']='P↓Q; p←Q'
    if r['cote']==116 and r['scan']==4 and r['line']=='replacement above asphérique':
        r['reading']='équiv. f.';r['alternatives']='équiv. h.; the audit favours f but the final letter remains uncertain.'
    if r['cote']==116 and r['scan']==5 and r['line']=='line 2':
        r['alternatives']='Earlier alternative \\equiv rejected at audit; the visible shorthand after revient au is =.';r['confidence']='high'
    if r['cote']==116 and r['scan']==7 and r['line']=='last line after au':
        r['alternatives']='Earlier alternative \\simeq rejected at audit; two straight strokes are visible.';r['confidence']='high'
    if r['cote']==117 and r['scan']==2 and r['line']=='between groups':
        r['alternatives']='Earlier alternative \\simeq rejected at audit; the same equals shorthand recurs.';r['confidence']='high'
p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
p=root/'scripts/render_doubts.py';s=p.read_text()
s=s.replace('`\\mathcal A`, `\\mathcal M`, `\\mathcal U`','`\\mathcal A`, `\\mathcal U`')
s=s.replace('| Equals-sign shorthand in prose | `$=$` | “revient au =” and “au =”; do not expand into “même”. |','| Equals-sign shorthand in prose | `$=$`, `$=^s$` | “revient au =”, “au =”, and the plural form on 117 scan 018; do not expand into “même” or “mêmes”. |')
s=s.replace('| Homotopy Hom operator | `\\operatorname{Homhot}` or local alternative | 117 scan 002 has cramped internal letters; scan 005 provides another explicit occurrence. |','| Homotopy Hom operator | `\\unsure{\\operatorname{Homht}\\|\\operatorname{Homhot}}`, `\\operatorname{Homhot}` | 117 scan 002 remains ambiguous; the clearer scan 005 does not authorize harmonizing a different visible spelling. |')
s=s.replace('| Ex., ex. | exemple |','| Ex., ex. | exemple |\n| g., dr. | gauche, droite |\n| pl. fid. | pleinement fidèle |\n| ssi | si et seulement si |\n| th. | théorie / théorème, according to context |\n| pt | point |\n| comm. | commute / commutation |\n| p. ex. | par exemple |\n| O.K. | approval / acknowledgment, as written |')
s=s.replace('The second reading is recorded page by page in `progress.log`; the context archive remains closed until the complete audit and transcription freeze.','A complete second visual reading of all 34 pages is recorded page by page in `progress.log`. This register and the recurring notation were checked before the transcription freeze and before any context contents were opened.')
p.write_text(s)
# Sort the already transcribed separator into its visual position; give audit additions stable IDs.
p=root/'MPL_116+117_inventory.csv'
with p.open(newline='') as f:
    rd=csv.DictReader(f);cols=rd.fieldnames;inv=list(rd)
sep=next(r for r in inv if r['element']=='116-003-separator');inv.remove(sep)
i=next(i for i,r in enumerate(inv) if r['element']=='116-003-06');inv.insert(i,sep)
for r in inv:
    if r['element']=='audit curved annotations':r['element']='117-002-audit-curves'
    if r['cote']=='117' and r['scan']=='8':r['sheet_kind']='text'
with p.open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=cols);wr.writeheader();wr.writerows(inv)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:f.write('notation and register consistency checked before context '+stamp+'; underlining macro unified in '+', '.join(changed)+'\n')
print('Register cleanup complete; changed underline macro in',changed)
