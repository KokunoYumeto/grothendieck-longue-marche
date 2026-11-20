"""Metadata-only reconciliation of already recorded audit decisions.

Does not read images, choose readings, or modify transcription or blind TSVs.
"""
from pathlib import Path
from datetime import datetime,timezone
import json
W=Path(__file__).resolve().parents[1]
changes=[]
def load(pg):return json.loads((W/'reports'/f'{pg}.json').read_text())
def save(pg,r):
 (W/'reports'/f'{pg}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');changes.append(pg)
def inv(r,key):return next(e for e in r['inventory'] if str(e['element'])==key)
pg='145_scan028';r=load(pg)
e=inv(r,'lifting-display');e['first_words_or_objects']=e['first_words_or_objects'].replace(r'\unsure{\dot\tau}',r'\dot\tau')
r['hand_habits'][1]['scope']='Three local occurrences. Audit B12 resolves the dotted tau; the connector before sigma_1 remains doubtful. No independent deleted predecessor is established.';save(pg,r)
pg='145_scan030';r=load(pg);e=inv(r,'18');e['first_words_or_objects']=e['first_words_or_objects'].replace('les éléments ',r'les \unsure{éléments|élémts} ');save(pg,r)
pg='145_scan031';r=load(pg)
inv(r,'right-annotation-header')['first_words_or_objects']=r'\unsure{\deleted{i.e.}|i.e.} ou encore'
e=inv(r,'canceled-right-header');e['first_words_or_objects']=r'\unsure{\deleted{i.e.}|i.e.}';e['position']='x1001-1064 y651-682; cancellation state uncertain';save(pg,r)
pg='145_scan033';r=load(pg)
if len(r['notes'])>20:
 assert all(isinstance(x,str) and len(x)==1 for x in r['notes'][8:])
 r['notes']=r['notes'][:8]+[''.join(r['notes'][8:])]
e=inv(r,'E13');e['first_words_or_objects']=e['first_words_or_objects'].replace(r'_{\mathrm{lac}}',r'_{\unsure{\mathrm{lac}|\mathrm{loc}}}');save(pg,r)
pg='145_scan034';r=load(pg)
r['abbreviations'][2].update(form=r'\unsure{p.r.|p.v.}',expansion='par rapport, if the first reading p.r. is correct; the alternative remains unexpanded')
r['notes'][0]=r['notes'][0].replace('Two insertions specify seules données and mais ils s’explicitent ainsi before quand.','Two insertions specify an uncertain seules/formelles before données, and mais ils s’explicitent ainsi before quand.');save(pg,r)
pg='145_scan035';r=load(pg)
inv(r,'E07')['first_words_or_objects']=r'\deleted{\unsure{extérieurs|secteurs}}'
e=inv(r,'E11');e['first_words_or_objects']=e['first_words_or_objects'].replace('qui remonte ',r'qui \unsure{rem.te|remonte} ')
inv(r,'E13')['first_words_or_objects']=r'\unsure{On|\deleted{On}} peut dire aussi que le sous-; final tuple and subgroup assertion'
inv(r,'E16')['first_words_or_objects']=r'\unsure{ss-|sous-}\uline{groupe}\unsure{.}';save(pg,r)
pg='145_scan036';r=load(pg)
r['notes'][0]=r['notes'][0].replace('Formula (14) has a dark paired-dot trace absent from both witnesses, retained as an unsure colon because its textual status is uncertain.','Formula (14) has a dark paired-dot trace absent from both witnesses; audit B16 resolves the two separately visible aligned points as a definite colon.');save(pg,r)
pg='147_scan003';r=load(pg)
e=inv(r,'E10');e['first_words_or_objects']=e['first_words_or_objects'].replace('la MDT-structure',r'la \unsure{MDT|MOT}-structure')
e=inv(r,'E11');e['first_words_or_objects']=e['first_words_or_objects'].replace('Structure MDT analytique',r'Structure \unsure{MDT|MPT} analytique')
e=inv(r,'E12');e['first_words_or_objects']=e['first_words_or_objects'].replace('déploiement','déployement').replace('des groupoïdes fondamentaux',r'\unsure{des|du} \unsure{groupoïde|groupoïdes} \unsure{fondamental|fondamentaux}')
r['abbreviations'][3]['form']=r'\unsure{MDT|MOT}; \unsure{MDT|MPT}';save(pg,r)
pg='147_scan007';r=load(pg)
inv(r,'E06')['first_words_or_objects']=r'\unsure{avec|et} (canceled)'
inv(r,'E15')['first_words_or_objects']='(pour les isos)'
r['abbreviations'][4].update(form='iso; isos',expansion='isomorphismes',places='147_scan007 baseline (pour les iso); final inserted (pour les isos)')
r['hand_habits'][2]['places']=r['hand_habits'][2]['places'].replace('pour les iso','pour les isos')
for i in (5,6):r['notes'][i]=r['notes'][i].replace('(pour les iso)','(pour les isos)').replace('pour les iso);','pour les isos);')
save(pg,r)
pg='147_scan008';r=load(pg);inv(r,'Soit_overwork')['first_words_or_objects']=r'Soit $\unsure{X|S}$ une';save(pg,r)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(W/'reports/metadata_reconciliation.md').write_text('# Metadata reconciliation\n\n'+now+'\n\nA read-only metadata review identified stale inventory excerpts, abbreviation labels and historical notes after the committed blind-audit decisions. Root reconciled those fields with the authoritative pages and audit decisions. The malformed scan033 notes array was repaired by joining its trailing single-character entries into the original paragraph. No transcription, first reading, second reading or box list was changed by this reconciliation.\n\nReports updated: '+', '.join(changes)+'. The two scan004 inventory updates (uncertain un state and contenu/courbe) were applied separately before this review.\n')
with (W/'progress.log').open('a') as f:f.write('metadata reconciled '+now+': notes formatting and stale inventory/abbreviation excerpts; no transcription or blind TSV changes\n')
print('Metadata reconciled:',', '.join(changes))
