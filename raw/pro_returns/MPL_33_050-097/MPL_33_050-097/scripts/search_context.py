"""Reproducible, per-note literal/regex searches of the two supplied context files.
No files named by RESULTS_STATE but absent from the ZIP are treated as read.
"""
from pathlib import Path
import subprocess
root=Path(__file__).resolve().parents[1]
context=root.parent/'context'
queries={
'N01':r'SGA|monodrom|fundamental|S19',
'N02':r'immersion|adjoin|factoris',
'N03':r'cohomologie locale|support|Gamma|Γ',
'N04':r'étale|etale|immersion',
'N05':r'variance|image inverse|C\(Y\)',
'N06':r'puret|dualit|fondament',
'N07':r'changement de base|Verdier|dualit',
'N08':r'born|cohomological.dimension|Artin',
'N09':r'lissifi|compactifi|ample',
'N10':r'classe.*fond|fond.*classe|cycle|WG H9',
'N11':r'Lichtenbaum|factoris|raffin|coherent',
'N12':r'trace|transit|classe.*fond',
'N13':r'transit|cocycle|coheren',
'N14':r'compactifi|type fini|S19',
'N15':r'trace|dualit|WG H9',
'N16':r'décal|shift|codimension|WG H9',
'N17':r'Gysin|trace|dualit',
'N18':r'twist|dimension relative|virtual|WG H9',
'N19':r'Gysin|transit|admet',
'N20':r'counit|co-unité|trace|adjoin',
'N21':r'adjoin|quasi.project|ample|formulaire',
'N22':r'trois compos|coheren|compatibil',
'N23':r'born|bounded|D\^',
'N24':r'projection|RHom|Hom',
'N25':r'projection|tensor|locally.free|localement.libre',
'N26':r'changement.de.base|proper|lisse|S19',
'N27':r'Ext|induction|constructib',
'N28':r'constructib|filtration|dévis|deviss',
'N29':r'locally.constant|loc..constant|induction|smooth',
'N30':r'coheren|cocycle|transit|S19',
'N31':r'normalis|normaliz|dimension|WG H9',
'N32':r'projection|RHom|adjoin',
'N33':r'puret|Gabber|régulier|regular',
'N34':r'Perfect.Categories|Sheaves|Lawvere|Freyd',
'N35':r'small|compact|finitely.present|petit',
'N36':r'projective|small|générat|generator',
'N37':r'stalk|fibre|faisceau|sheaf',
'N38':r'AB5|perfect|filtered|filtrant',
'N39':r'injectiv|Tohoku|Tôhoku|reflect',
'N40':r'root|racine|limit|limite',
'N41':r'torsion|Z_p|cyclic|cyclique',
'N42':r'Lawvere|Freyd|right.root|left.root',
'N43':r'E_?8|root|racine|positiv|WG2',
'N44':r'E_?8|alpha|simple|WG2',
'N45':r'E_?8|root|racine|WG2',
'N46':r'F_?4|Weyl|240|1152|lattice',
'N47':r'391|Bourbaki|titre|title|WG2',
'N48':r'19\.6|regular|régulier|filtration|WG2',
'N49':r'sépar|separat|noeth|19\.7',
'N50':r'associat|projectiv|19\.7|induction',
'N51':r'diagram|orientation|19\.6',
'N52':r'1011|19\.6\.4|folio|page',
'N53':r'algèbre|algebra|module|19\.6',
'N54':r'graded|gradu|projector|WG2',
'N55':r'Kähler|Kahler|homotop|holomorph',
'N56':r'homotop|project|holomorph',
'N57':r'Fredholm|singular.integral|harmonic|symbol',
'N58':r'Kähler|Kahler|Fredholm|analytic|111|73',
'N59':r'LM7 E\.23|LM4 D\.12|LM4 F\.7|LM7_PUSH C\.6|INTAKE LM7',
'N60':r'WG H9|Mordell|Hodge.index|Lefschetz.pencil',
'N61':r'WG2|projector|graded|Lefschetz',
'N62':r'Referee|review|referee|Status|claim|MPL_142|MPL_14',
'N63':r'S19|title|page|scan|Only.this.README',
'N64':r'SGA|S19|lissifi|compactifi|Verdier',
'N65':r'compatibil|vérifi|verify|S19|dualit',
'N66':r'stalk|skyscraper|Hom|fibre|sheaf',
'N67':r'order|ordre|root|sheaf|category',
'N68':r'restriction|stalk|diagram',
'N69':r'sheaf|faisceau|gluing|recollement',
'N70':r'E_?8|root|racine|alpha',
'N71':r'sheafification|reflect|sheaf|faisceau',
'N72':r'S19|ordre|order|folio|page|transit',
}
lines=['# Per-note context searches','','Only README.md and notes/RESULTS_STATE.md were present in the supplied ZIP. Each note has its own search below. Hits on a broad word are not evidence of a matching theorem; the notes assess relevance. Source files merely listed in RESULTS_STATE were not supplied or read.','']
for key,q in queries.items():
 result=subprocess.run(['rg','-n','-i','--regexp',q,str(context/'README.md'),str(context/'notes/RESULTS_STATE.md')],capture_output=True,text=True)
 assert result.returncode in (0,1),result.stderr
 lines.extend([f'## {key}',f'Pattern: `{q}`',''])
 hits=result.stdout.strip().splitlines()
 if not hits:lines.append('No literal or regex match in supplied context.')
 for h in hits:
  h=h.replace(str(context)+'/','');parts=h.split(':',2)
  lines.append('- '+':'.join(parts[:2])+': '+parts[2][:230]+(' [excerpt truncated]' if len(parts[2])>230 else ''))
 lines.append('')
(root/'records/context_queries.md').write_text('\n'.join(lines))
print(len(queries),'per-note context searches completed and recorded.')
