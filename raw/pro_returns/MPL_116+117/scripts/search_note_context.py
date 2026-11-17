#!/usr/bin/env python3
"""Run recorded lexical context searches for every research-note item.

This is a discovery/traceability record, not OCR and not an absence proof.
It opens only the supplied text context, never images or frozen transcription.
"""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT.parent / 'context'
WORKING = ROOT / 'working'
notes = (ROOT / 'MPL_116+117_notes.md').read_text()
queries = {
'Q01':r'W\(7|Hot 7|reversib|cube',
'Q02':r'totalement.*asph|totally.*aspherical|filtrant|filtered',
'Q03':r'Theorem A|Théorème A|Loc.*3 bis|relative.*A',
'Q04':r'Der 1|dérivateur|Hot 1|jointly detect',
'Q05':r'Mapping|recollement|gluing|crossing arrows',
'N01':r'topos total|triples|recollement|gluing',
'N02':r'pour tout faisceau|coefficient|cohomolog',
'N03':r'rétraction|retraction|mapping cylinder|mapping.path',
'N04':r'réciproque|fort asphérique|left.exact left adjoint',
'N05':r'cohomologie relative|support.*sequence|cofiber|mod.*X',
'N06':r'équivalence faible|équiv.*faible|two.out.of.three|asphérique',
'N07':r'localement constant|locally constant|tautolog',
'N08':r'Sierpinski|Top.*Delta|open subtopos|downsets|down.sets',
'N09':r'accessible|deux inclusions|both inclusions|exact à gauche',
'N10':r'presheaf|bifoncteur|bifunctor|9\.5\.10',
'N11':r'collage|crossing arrows|profunctor|bifoncteur',
'N12':r'filtrante|fibrant|comma|strict fibre',
'N13':r'tot.*0.asph|total.*aspher|localisation',
'N14':r'Homhot|Homht|internal Hom|Hom internes',
'N15':r'holim|intégrant|cointegration|cointégration',
'N16':r'path.category|zigzag|hammock|homotopies entre',
'N17':r'On a sans doute|mapping space|mapping complex|Hom.*simplicial',
'N18':r'troncature|truncat|K.theory|triangles exacts|additif',
'N19':r'Hom internes|Homhot|tensor|multiplicative',
'N20':r'contravariant|variance|jointly detect|préciser',
'N21':r'produits finis|infinite.*product|Hot 1|produits quelconques',
'N22':r'première intégration|barré|presheaf|univers',
'N23':r'Hot 2|Hot 3|Fubini|cofibrant|cointégration',
'N24':r'opposition|opposite|dualité|two.cell',
'N25':r'commut.*adjoint|Kan extensions do not|weak.*preserv|morphisme.*théor',
'N26':r'adjunction.equivalence|counit|co.unité|Gurski|two.out.of.three',
'N27':r'spéciales|special|troisième|common.*present|enhancement',
'N28':r'non encore|finitude|nonaccessible|fundamental localizer',
'N29':r'Si pourtant|exact à gauche|quasi.isom|derived',
'N30':r'coinvariant|exact à gauche|Kan extensions do not|quasi.isom',
'N31':r'Hot 4|base.change|changement de base|cofibrant',
'N32':r'transposées|mates|exchange|coherence',
'N33':r'Hot 5|fully faithful|pl.*fid|support images',
'N34':r'Hot 6|localisation|S\^2|rectif',
'N35':r'je présume|cofinalité|adjunction|cofinal',
'N36':r'adjoint à gauche|adjoint à droite|unit|counit|cofinal',
'N37':r'catégories filtrantes|Cat.colimit|filtered|exactness',
'N38':r'Hot 7|surjectif|gluing|recollement|W\(7',
'N39':r'coherent gluing|pseudopullback|lax.pullback|strongness',
'N40':r'lacets|loop|Puppe|homotopy.cartesian',
'N41':r'derivator|derivateur|dérivateur|cointegration|integrat',
'N42':r'six.functor|six opérations|internal Hom|duality formalism',
'N43':r'proper|smooth|duality|cohomological dimension',
'N44':r'Totally aspheric asphericity structures|134.8|106.107|relative Theorem A',
'NR01':r'finite monoid|bounded homology|universal group|finite type',
'NR02':r'Miller|cohomological bound|residually finite',
'NR03':r'Kan.Thurston|small quotients|E\.17|KT_',
'NR04':r'uncount|S2COUNT|homotopy retract|D\.6',
'NR05':r'RP.*2|34 arrows|G\.8',
'NR06':r'census|fewest arrows|G\.14|G\.15|P_?2',
'NR07':r'reversible|spectra|RP.*infty|POLES F\.14',
'NR08':r'W\(7|Theorem 2|Théorème 2|37.object|acyclic',
'NR09':r'trefoil|Loc.*7 F|W_Z|W_k',
'NR10':r'simply connected|Ch\(Y|fixed.origin|total',
'NR11':r'Isbell|Mitchell|Delta.*inj|Δ_inj|36ter',
'NR12':r'Conjecture 7\.1|RP.*2|Atiyah|Miller',
'NRK1':r'Isbell|Mitchell|affine|Aff_',
'NRK2':r'Nielsen|Harvey|uniqueness',
'NRK3':r'localiseur spécial|localisateur.*spécial|accessible fundamental|4\.2\.22',
'H01':r'EXIT_TOWER|SECTIONS_OVER_Q|LM4_SUCCESSOR|ANABELIAN_SUCCESSOR|FINMON|S2COUNT',
'H02':r'GALOIS B\.13|nonaccessible|tout localisateur fondamental|cité de mémoire'
}
inherit = {
'S01':'N04','S02':'N09','S03':'N17','S04':'N18','S05':'N18','S06':'N19','S07':'N27',
'S08':'N20','S09':'N23','S10':'N21','S11':'N27','S12':'N28','S13':'N29','S14':'N31',
'S15':'N31','S16':'N35','S17':'N37','S18':'N38','S19':'N06','S20':'N22','S21':'N34',
'R01':'N09','R02':'N03','R03':'N12','R04':'N15','R05':'N23','R06':'N21','R07':'N31',
'R08':'N29','R09':'N35','R10':'N26','R11':'N26','R12':'N07','R13':'N18',
'O01':'N37','O02':'N38','O03':'N28','O04':'N19','O05':'NR07','O06':'N27','O07':'N20',
'O08':'Q03','O09':'Q03','O10':'Q01','O11':'Q02','O12':'N07','O13':'N11','O14':'Q02',
'O15':'N10','O16':'N26','O17':'N44','O18':'N28'
}
for key, parent in inherit.items():
    queries[key] = queries[parent]
queries.update({
'T01':r'Mapping cone|Mapping.cône',
'T02':r'Relation entre morphismes|recollement.*topos',
'T03':r'Structure des dérivateurs|déc.*83|décembre 1983',
'T04':r'24\.11\.83|24 novembre|novembre 1983',
'T05':r'Théorie.*variance.*homotopique|La variance',
'T06':r'pages 5 à 11|pages 13 à 20|pagination|authorial|foliation',
'T07':r'Flèches|Théorie|barré',
'T08':r'1981|19 juin|30 juin|thèse',
'T09':r'1981|comptab|reused|réemploy',
'T10':r'15 avril|28 avril|1983.1984|DEA|D\.E\.A',
'T11':r'30 Mars|13 Avril|11.*AVR|ministère',
'T12':r'19 pages|Pages 1|page count|pagination|scans 2'
})

note_ids = set(re.findall(r'^### ((?:Q|N|R|H)\d{2}|NR(?:\d{2}|K[123])) —', notes, re.M))
note_ids.update(re.findall(r'^\| ((?:S|T|O)\d{2})(?: —| \|)', notes, re.M))
assert set(queries) == note_ids, (set(queries)-note_ids, note_ids-set(queries))
catalog = json.loads((WORKING/'context_catalog.json').read_text())
stop = set('the a an of and or for with from in to as all every is are by its their this that not no does do only two three both under without'.split())
for line in (WORKING/'comparisons_dss.txt').read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    identifier, topic, scans, kind, note = line.split(' || ')
    words = [w for w in re.findall(r'[A-Za-z][A-Za-z-]+', topic) if w.lower() not in stop]
    queries[identifier] = '|'.join([re.escape(identifier)] + [re.escape(w) for w in words[:6]])
assert len(queries) == 385

def run(item):
    identifier, pattern = item
    cmd = ['rg', '-n', '-i', '--glob', '*.md', '--glob', '*.tex', '-e', pattern, str(CONTEXT)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    assert p.returncode in (0,1), (identifier, p.stderr)
    found = []
    counts = Counter()
    for line in p.stdout.splitlines():
        path, number, text = line.split(':', 2)
        rel = str(Path(path).relative_to(CONTEXT))
        counts[rel] += 1
        found.append(dict(file=rel,line=int(number),excerpt=text[:550]))
    # Prefer the direct contextual interpretative files; preserve file counts
    # for the rest rather than implying their every match was read.
    def rank(x):
        f=x['file']
        if f.startswith('hua_project/'): return (0,f,x['line'])
        if f=='notes/RESULTS_STATE.md': return (1,f,x['line'])
        if f=='DOSSIER_STATEMENTS_WITH_STATUS.md': return (2,f,x['line'])
        if f=='NEW_RESULTS.md': return (3,f,x['line'])
        return (4,f,x['line'])
    selected=[]
    perfile=Counter()
    for hit in sorted(found, key=rank):
        if perfile[hit['file']] < 2:
            selected.append(hit)
            perfile[hit['file']]+=1
        if len(selected)==10: break
    return dict(id=identifier,pattern=pattern,command='rg -n -i --glob *.md --glob *.tex -e PATTERN context',
                matching_lines=len(found),files=dict(sorted(counts.items())),sample_matches=selected)

with ThreadPoolExecutor(max_workers=4) as pool:
    records=list(pool.map(run,queries.items()))
out=dict(created_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
         purpose='Lexical discovery log for every note; matches are not claims of correctness, novelty or exhaustive reading.',
         note_count=len(note_ids),dossier_count=255,query_count=len(records),records=records)
(WORKING/'context_search_log.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'Context searches recorded: {len(records)} ({len(note_ids)} named notes + 255 DSS comparisons).')
print('Zero-match items:', ', '.join(r['id'] for r in records if not r['matching_lines']) or 'none')
