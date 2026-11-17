#!/usr/bin/env python3
"""Read-only, per-note targeted searches of the supplied post-freeze context.

Runs ripgrep, records every match count and a bounded navigation sample. It does
not rewrite, interpret, or normalize any transcription. The full supplied files
remain the context; selected hits are navigation aids, not replacement evidence.
"""
from pathlib import Path
import datetime, json, re, subprocess

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
CONTEXT = WORK.parent / 'context_opened'
FILES = [
    'README.md', 'notes/RESULTS_STATE.md',
    'MPL_16+47+54+44_transcription.tex',
    'MPL_16+47+54+44_notes.md', 'MPL_16+47+54+44_doubts.md',
    'hua_project/README.md', 'hua_project/58.modern.tex',
]
QUERIES = {
'N01': r'Rationalité|primaire|355|358|extension des scalaires|generic freeness',
'N02': r'Du local au global|Lemme 4|Peut se renforcer|dernier N',
'N03': r'fournissons la connexité|noethérien.*connexe|Lemme 4',
'N04': r'géométriquement|fibres spéciales|unibranche|quadratique|nombres',
'N05': r'équidimension|excellence|excellente|réduction facile|conjecture',
'N06': r'K - n|K.*n.*k|équidimension|dimensions|ponctué|épointé',
'N07': r'Variante|universellement|fibres géométriques|unibranche',
'N08': r'Hansen|Deligne|morphisme.*P|th.*local|hyperplans',
'N09': r'Introduction et plan|non.*propre|immersion ouverte|profondeur|completion',
'N10': r'Grauert|1958|Serre|nullité',
'N11': r'Le fil du dossier|plan|pureté|quasi.factoriel|WG2.*1.1',
'N12': r'Lef|Leff|LG.*faible|voisinage|stricte|Exemples|tout de suite',
'N13': r'injective|injectif.*n\+1|split|résolution|projectif.*affine',
'N14': r'famille|cinq|five|i=n\+1|générat|Confiance',
'N15': r'probablement|voisinage|quasi.projectif|LG.*faible',
'N16': r'Ass|profondeur|depth|Question|closure',
'N17': r'cohomologie locale|local cohomology|support|profondeur|58-local',
'N18': r'Pseudolimite|Précaution|colimite|catégories|conclusion pratique',
'N19': r'étales|structures d.alg|multiplication|LM6 F.6',
'N20': r'pureté|voisinages|fondamental|LM6 F.6|Lefschetz',
'N21': r'Pic|Lambda|Cartier|fixed factor|facteur fixe',
'N22': r'pleinement fidèle|équivalence de catégories|automorph|classes|foncteur',
'N23': r'Lambda|H.1|H.2|annul|injection|Pic',
'N24': r'Permanence|Corollaire 1|Théorème 1|58-lef',
'N25': r'plat sur.*Y|plat.*X|lettre se lit|Permanence',
'N26': r'complexe parfait|borné|EGA.*7.7|Rf|58-lef',
'N27': r'vérifions pas|algébris|algebr|support propre|effectiv',
'N28': r'Corollaire 2|fidèles|fidèle|projectifs et plats',
'N29': r'localement libre|voisinage|support propre|58-lef',
'N30': r'quasi.projectivité|quasi.projectif|omise|exception|Permanence',
'N31': r'essentielles|exemples|propreté|platitude|Permanence',
'N32': r'quotient|complétude|C_.*Phi|t.adique|Une forme locale',
'N33': r'points fermés|condition plus forte|marge|dim.*bar|58-local',
'N34': r'min\(2|min\(2,|Hom|target|G.*profondeur|58-local',
'N35': r'dévissage|non.*div|torsion|reste à faire|diagramme',
'N36': r'associé|dimension.*1|58-local|cohérent',
'N37': r'T_1|comparaison affine|c\x27|ne sont pas dans le dossier',
'N38': r'on a gagné|images directes|cohérent|satur|reflex|hull',
'N39': r'valuation discrète|sans restriction|pas plein|Bbbk.*x.*z|58-local',
'N40': r'Les questions|type fini|torsions positives|Finitude',
'N41': r'initiale|injectif|surjectif|alpha_i|dualité',
'N42': r'Ext|voisinage.*Z|B_n|profondeur|dualité',
'N43': r'gratte.ciel|skyscraper|implication|type fini|réciproque',
'N44': r'Mittag|régulier|limite|épaississ|thickening',
'N45': r'B_n|Sous les conditions|conditions.*\*|gratte.ciel|skyscraper',
'N46': r'pas nécessaires|suffisantes|profondeur|sharp',
'N47': r'Finitude|F\(-m\)|A.*i|torsions',
'N48': r'Finitude|cohérent|A.*n|longueur finie|finite length',
'N49': r'g_\*|C_n|n\+1|profondeur|torsions positives',
'N50': r'seules|points de.*U|pts de.*U|bord|boundary',
'N51': r'3\.2|3\.1|recycl|réemploi|dactylograph|typescript|bigr',
'N52': r'338|371|idéaux|extérieure|réemploi|dactylograph',
'N53': r'Brauer|Witt|Dieudonn|caractéristique zéro|group algebra',
'N54': r'Spec.*z|Proj.*z|mot.*Spec|cône projectif',
'N55': r'primés|tildés|deux fois|Pic.*0|Brouillons',
'N56': r'seminormal|seminormal|contraction|R_0|Pic.*0',
'N57': r'cuspid|cusp|t.2.*t.3|seminormal|line bundle',
'N58': r'cohomologie locale|mathcal\{O\}.*\*|parafactoriel|X.*local',
'N59': r'parafactoriel|factoriel|dimension.*2|notions intermédiaires',
'N60': r'genre|Rosenlicht|normalisation|normalization|delta|A01',
'N61': r'EXIT_TOWER|A\.5|ANABELIAN_149_PUSH B\.5|stable graph|Dehn|strat',
'N62': r'8\.7\.5|8\.8\.6|EGA.*II|vérifié|section',
'N63': r'anneau des sections|Pic.*Z|section|cône|f_\*',
'N64': r'faudrait supposer|factoriel|seminormal|section nulle|surjectivité',
'N65': r'Fourier|compatibilité|admettre le lemme 2|Poincar|Pontryagin',
'N66': r'F7|F8|Koszul|actual comparison map|particular map|unit',
'N67': r'Th\. 1|N\(|Alb|D08|D13|kernel',
'N68': r'Th\. 2|Betti|D09|dim.*J|half',
'N69': r'Th\. 3|identifier pour|dualit|D08|D10|D11',
'N70': r'Th\. 4|A prouver|positive|D13|WG H9',
'N71': r'Th\. 5|Néron|Neron|D12|WG H9|signe près',
'N72': r'Th\. 6|facteur fixe|fixed.factor|Lefschetz|P\^i',
'N73': r'Th\. 7|Matsusaka|numérique|tau|D14',
'N74': r'12\.8\.1964|Programme de travail|prouvé grand.chose|earlier',
'N75': r'Oda|Dieudonné|de Rham|D01|D02|D03|D04|D05',
'N76': r'WG2.*1\.1|Book II|Abstract Lefschetz|standard conjectures|motif',
'N77': r'LM6 F\.6|higher.dimensional|number.fields|fondamental',
'N78': r'1962|1964|1968|chronolog|laboratoire|SGA',
'N79': r'58-local|Raynaud|Une forme locale|points fermés|Hom',
'N80': r'58-lef-permanence-projective-flat|58-local-hom-comparison-depth-off-y|waiting|vérifions pas',
'T01': r'Couples de|Lefschetz.Grauert|couverture|27',
'T02': r'Applications|morphismes projectifs|morphismes propres|53',
'T03': r'355|358|338|371|133|134|Etat 2|état 2',
'T04': r'III|Introduction|plan|Corollaire.*3\.2|page.*66',
'T05': r'44 pages|19 pages|Pages 1|66 pages|pagination|page n|scan n',
}

def location(lines, number, name):
    prefix = lines[:number]
    if name.endswith('_transcription.tex'):
        cotes = [re.search(r'\\cotefile\{([^}]+)\}', x) for x in prefix]
        scans = [re.search(r'\\scanpage\{([^}]+)\}', x) for x in prefix]
        c = next((m.group(1) for m in reversed(cotes) if m), '?')
        s = next((m.group(1) for m in reversed(scans) if m), '?')
        return f'cote {c}, scan {s}'
    if name.endswith('58.modern.tex'):
        sec = next((x.strip() for x in reversed(prefix) if re.match(r'\\(?:sub)*section', x)), 'front matter')
        return sec
    return next((x.strip() for x in reversed(prefix) if x.startswith('#')), 'front matter')

out = ['# Per-note context search ledger', '',
       'UTC: '+datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'), '',
       'Read-only ripgrep searches run after freeze. Counts cover every match; navigation samples show at most three hits per file. The main notes cite the relevant section/scan after substantive reading, not merely the first hit. Oda was separately checked in the PDF, as documented in `context_questions_review.md`. No manuscript images or frozen files are modified by this script.', '']
manifest = {}
for key, pattern in QUERIES.items():
    out += [f'## {key}', '', f'Query: `{pattern}`', '']
    records = []
    for name in FILES:
        path = CONTEXT / name
        result = subprocess.run(['rg', '--json', '-i', '-e', pattern, str(path)], capture_output=True, text=True)
        if result.returncode not in (0,1):
            raise RuntimeError(f'{key}: {result.stderr}')
        matches = [json.loads(x)['data'] for x in result.stdout.splitlines() if json.loads(x)['type']=='match']
        records.append({'file':name, 'match_count':len(matches), 'line_numbers':[m['line_number'] for m in matches]})
        out.append(f'- `{name}`: **{len(matches)} matching lines**.')
        lines = path.read_text(encoding='utf-8-sig').splitlines()
        for m in matches[:3]:
            n = m['line_number']; content = m['lines']['text'].strip().replace('`','′')
            content = content[:260] + (' … [navigation sample truncated]' if len(content)>260 else '')
            loc = location(lines,n,name).replace('`','′')
            out.append(f'  - L{n}; {loc}: `{content}`')
    manifest[key] = {'query':pattern,'files':records}
    out += ['', 'Interpretive outcome: see the corresponding item in `MPL_58_020-067_notes.md`; a zero count is only a lexical search result, not an archive-wide absence claim.', '']
(HERE/'context_searches.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
(HERE/'context_search_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'queries':len(QUERIES),'files_per_query':len(FILES),'all_searches_completed':True,'ledger_bytes':(HERE/'context_searches.md').stat().st_size}))
