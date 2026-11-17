"""Bounded text searches supporting scope statements and source-flag inventory.

These searches supplement the completed visual reading. They cannot prove that
an equivalent concept is absent merely because a chosen word does not occur.
"""
from pathlib import Path
from datetime import datetime, timezone
import subprocess
import json

ROOT=Path(__file__).resolve().parent.parent
files=sorted(str(p) for p in (ROOT/'pages').glob('*.tex'))
queries={
 'B6_universality_terms':r'B[eé]ly|Biel|Белый|toute[s]?\s+.*courbe|chaque\s+.*courbe|obtiendr|cartograph',
 'faithfulness_and_regularity_terms':r'fid[eèé]l|injectif|réguli|regular',
 'congruence_ring_and_M05_terms':r'congru|biicosa|icosa|M_\{?0,?5|X\s*[\(\{]\s*(7|11)|anneau',
 'author_verification_terms':r'vérifi|facile|on prouve|on.*prouve|évident|devra|aurait|voudrait|élucider|probable|conject|\?',
 'titles_and_counts':r'pages|Pages|Titre|titre|Paradigme|spéciaux|spécial|groupoïdes|Sous groupes',
}
out={
 'checked_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'scope':'42 frozen page files only; no OCR; no changes',
 'caution':'Negative lexical hits do not prove conceptual absence; final notes rely on the completed single-reader visual audit and positive context comparisons.',
 'queries':{},
}
for label,pattern in queries.items():
 r=subprocess.run(['rg','-n','-i','--no-heading','--color','never','-e',pattern,*files],text=True,capture_output=True)
 assert r.returncode in (0,1),(label,r.stderr)
 hits=[x.replace(str(ROOT)+'/', '') for x in r.stdout.splitlines()]
 out['queries'][label]={'pattern':pattern,'matching_lines':len(hits),'hits':hits}
(ROOT/'research_records'/'scope_searches.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print({k:v['matching_lines'] for k,v in out['queries'].items()})
