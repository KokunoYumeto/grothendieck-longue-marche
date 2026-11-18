#!/usr/bin/env python3
"""Reproducible, bounded textual searches of the supplied post-freeze context."""
from pathlib import Path
import json
import re
import subprocess

root = Path(__file__).resolve().parents[2]
context = root / 'MPL_64_116-157_context'
out = Path(__file__).resolve().parent
queries = {
 'L01': r'épinglage|Legendre|échelon.*4',
 'L02': r'suite exacte|F_t|tautologique',
 'L03': r'varphi_i|poids|Gauss.Manin|Cartier',
 'L04': r'lambda_i|Delta_0|condition b|condition.*proportionnal',
 'L05': r'colin.ar|distincts|points d.ordre 4|det.*pmatrix',
 'T01': r'Torelli|réseau|demi.plan',
 'T02': r'varphi\^\{-1\}|inverse|antilinéaire',
 'T03': r'C.est faux|orientation|conjuguée',
 'T04': r'anti.?holomorphe|analytiquement naturel|famille analytique',
 'T05': r'tau_.*infty|échange de|action à gauche|action à droite',
 'T06': r'semi.direct|demi.direct|groupe.*direct|c\\tau\+d',
 'T07': r'topos modulaire|revêtement universel|orbifold|coarse',
 'T08': r'rang.*1|rg.*1|rang.*2|Pi_.*ab',
 'T09': r'action extérieure|Autext|Out.*F_?2|Nielsen',
 'T10': r'rigidification différentielle|fibré tangent|Hodge',
 'T11': r'points.*ordre.*2|opère.*librement|stabilisat|centre universel',
 'T13': r'poids|sous.espaces propres|impair|euclidienne',
 'T14': r'caract.ristique.*trois|car.*3|1728|exceptionnel',
 'G01': r'produits dans une extension|semi.direct|u.x.u|G_0',
 'U08': r'sauf erreur|je pr.sume|admis|suffisante',
 'T12': r'automorphismes.*ellipt|LM4 D.12|LM6 A.22|LM7_PUSH E.3',
 'U01': r'Je voudrais|canoniquement|Legendre',
 'U02': r'Dieu sait|il faudra|condition c',
 'U03': r'C.est faux|orientation',
 'U04': r'analytiquement naturel|anti.?holomorphe',
 'U05': r'expliciter l.action|action extérieure',
 'U06': r'points.*ordre.*2|opération.*libre',
 'U07': r'autre explication|sauf erreur|vérifier',
 'C01': r'Relations entre|M_?\{?11|M_?\{?04',
 'C02': r'Approche transcendante|21 pages|22 pages|21.*p\.',
 'C03': r'théorie transcendante|première mouture|seconde mouture',
 'C04': r'normalité|quadratiques|Appendice',
 'C05': r'PAPPALARDO|Hydrologie|novembre 1980',
 'C06': r'JAMBON|LANGAGE ALGORITHMIQUE|décembre 1980',
 'C07': r'Surveillance des examens|JUIN 1981|Amphi',
 'R01': r'orthodoxes|marteaux|Corollaire',
 'R02': r'fl.che verticale|multiplication par|zeta|xi',
 'R03': r'ordre inverse|ordre du raisonnement|première mouture|seconde mouture',
 'R04': r'première mouture|seconde mouture|ordre des pages'
}
report=['# Root per-note context searches', '',
        'Executed after transcription freeze; search hits are documentary leads, not proof checks.',
        'Each regex was run with rg against the entire supplied context directory.',
        'For readability this report retains at most three hits per file and eight files per note; the total hit count includes omitted hits.',
        'Main-note comparisons name the relevant file and scan or section; no hit is treated as proof merely because it is present.', '']
summary=[]
for note, pattern in queries.items():
    p=subprocess.run(['rg','-n','-i','--json','-e',pattern,str(context)],text=True,capture_output=True)
    if p.returncode not in (0,1):
        raise RuntimeError(p.stderr)
    matches=[json.loads(row)['data'] for row in p.stdout.split('\n')
             if row and json.loads(row)['type']=='match']
    hits=[f"{m['path']['text']}:{m['line_number']}:{m['lines']['text'].rstrip()}"
          for m in matches]
    byfile={}
    for hit in hits:
        rel=hit.replace(str(context)+'/', '', 1)
        name=rel.split(':',1)[0]
        byfile.setdefault(name,[]).append(rel)
    report += [f'## {note}', '', f'Query: {pattern}', '', f'Total matching lines: {len(hits)}.', '']
    for name, rows in list(byfile.items())[:8]:
        for row in rows[:3]:
            report.append('- '+row[:750])
    if not hits: report.append('- No literal match; absence is limited to this query and supplied text.')
    report.append('')
    summary.append({'id':note,'hits':len(hits),'files':list(byfile)})
(out/'root_context_searches.md').write_text('\n'.join(report)+'\n')
(out/'root_context_search_summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(summary,indent=2,ensure_ascii=False))
