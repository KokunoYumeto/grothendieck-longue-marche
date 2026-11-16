"""Additional item-level context searches after the frozen transcription."""
import datetime
import json
from search_context import search, ROOT

queries = {
    'D01': r'cohomolog|Amitsur|acycl',
    'D07': r'acycl|Amitsur|dim.*coh|Tate',
    'D09': r'Cartier|Frobenius|Verschiebung',
    'D17': r'Matlis|injective hull|enveloppe injective|injectif',
    'D19': r'bounded|borné|cohérent|coherent',
    'D21': r'\\theta|θ',
    'D28': r'compatib|vérifier|zero section',
    'D29': r'stalk|fibre|injective hull|enveloppe injective',
    'R11': r'fid.*plat|flat|platitude|localisation',
}
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
records=[]
for note, pattern in queries.items():
    hits=search(pattern)
    records.append(dict(note=note, utc=stamp, scope='supplied context .md/.tex/.txt files, excluding PDF image data', pattern=pattern, count=len(hits), hits=hits))
    print(note, len(hits), sorted(set(f"{h['cote']}:{h['scan']}" for h in hits if h['cote'])))
(ROOT/'records/research_root_supplement_searches.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in records), encoding='utf-8')
