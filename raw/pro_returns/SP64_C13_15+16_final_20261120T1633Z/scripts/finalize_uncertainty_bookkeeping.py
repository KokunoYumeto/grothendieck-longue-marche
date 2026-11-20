"""Primary-reader reconciliation after both complete visual readings."""
from workflow import *
HEADERS['certainty_only.tsv']=['scan','line','old_mark','reading','evidence','confidence']
extra=[
 ('15/183','cancelled dupliquer',r'\unsure{dupliquer|d\'expliciter}'.replace("\\'","'"),'dupliquer','The cancelled baseline retains the d, u, p descender, following l and q descender; the inserted démultiplier is a separate line.','medium'),
 ('15/183','cancelled F before G',r'\unsure{F|G}','F','The struck letter retains an upright and two horizontal arms before the live G.','medium'),
 ('15/185','cancelled classes de',r'\unsure{classes de}','classes de','Both words remain legible below the strike in the polarisation paragraph.','high'),
 ('15/187','cancelled u(s-prime)',r'\unsure{u(s\')|v(s\')}'.replace("\\'","'"),"u(s')",'The rounded u body precedes the parenthesised argument beneath the strike.','medium'),
 ('15/191','first cancelled On',r'\unsure{On}','On','A closed capital O and short n are visible before the live On dispose.','medium'),
 ('15/191','cancelled de t.f. sur',r'\unsure{\text{de t.f. sur}|\text{déf.}}',r'\text{de t.f. sur}','The struck line between X and the replacement k est un retains the separated short forms and sur.','medium'),
 ('15/191','cancelled Witt letter in (iii)',r'\unsure{\mathbb{W}}',r'\mathbb{W}','The angular double W remains visible under the hatch before k.','medium'),
 ('15/191','second cancelled On',r'\unsure{On}','On','The small hatched capital O and following n precede the live On utilise.','medium'),
 ('15/191','cancelled soit un',r'\unsure{soit un}','soit un','The two struck words survive before the live ait plus.','medium'),
 ('15/193','cancelled aie',r'\unsure{aie}','aie','The cancelled word has a, a dotted short i, and final e; no terminal t is supplied.','medium'),
 ('15/193','cancelled il est',r'\unsure{il est}','il est','The two struck groups remain visible after x in X at the right end of the line.','medium'),
 ('15/193','cancelled sont',r'\unsure{sont}','sont','The struck word starts the next line before si k est alg. clos.','medium'),
 ('15/193','cancelled est in notation (ii)',r'\unsure{est}','est','The short e-s-t sequence remains beneath the strike after x.','medium'),
 ('16/003','cancelled par before donnée',r'\unsure{par}','par','The p descender and joined ar remain under the strike before donnée.','medium'),
]
rows=readrows('certainty_only.tsv')
seen={(r['scan'],r['line']) for r in rows}
for values in extra:
 if values[:2] not in seen:rows.append(dict(zip(HEADERS['certainty_only.tsv'],values)))

# Retaining/narrowing the same alternatives or changing their priority alone is
# documented as certainty, rather than counted as a substantive change to C.
certainty_places={
 ('15','183','line 8, cancelled words and replacement'),
 ('15','183','line 12, second component'),
 ('15','183','line 13, type qualifier'),
 ('15','193','H notation in parenthesis'),
 ('16','014','suffix after (6.1)')
}
cr=readrows('changes_records.tsv'); kept=[]
for r in cr:
 if r['kind']=='deletion state':r['kind']='deletion state (struck given live or live given struck)'
 if (r['cote'],r['scan'],r['place']) in certainty_places:
  rows.append(dict(zip(HEADERS['certainty_only.tsv'],[r['cote']+'/'+r['scan'],r['place'],r['C'],r['final'],r['scan_shows']+' Only the uncertainty alternatives or their priority change against C. Crop: '+r['crop'],r['confidence']])))
  r['against_C']='no'
 if r['against_C']=='yes' or r['against_H']=='yes':kept.append(r)
write_rows('changes_records.tsv',kept)
hr=readrows(PREFIX+'_collation.tsv')
for r in hr:
 if r['kind']=='deletion state':r['kind']='deletion state (struck given live or live given struck)'
write_rows(PREFIX+'_collation.tsv',hr)
rank={c+'/'+s:i for i,(c,s) in enumerate(ORDER)}
write_rows('certainty_only.tsv',sorted(rows,key=lambda r:rank[r['scan']]))
log('uncertainty bookkeeping '+now()+': backfilled fourteen early struck-text certainty resolutions; five C alternative-narrowing/priority adjustments excluded from substantive C counts; two abbreviated kind labels expanded to the specified vocabulary')
rebuild()
