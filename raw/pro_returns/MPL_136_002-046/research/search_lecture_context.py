"""Post-freeze, text-only context search ledger for lecture research notes."""
from pathlib import Path
import subprocess, json, hashlib
from datetime import datetime, timezone

base=Path(__file__).resolve().parents[2]
context=base/'context'
queries={
'L001':r'Historique|Plan conf|plan de la conf|lecture plan',
'L002':r'Poincaré|Cartan|Historical',
'L003':r'Sullivan|sauf erreur|finite.type',
'L004':r'acyclique|représentable|analytiques réelles',
'L005':r'ths contre|strict.*commutat|anticomm|unweighted',
'L006':r'origine|simplexe de taille|sum X_i.*1',
'L007':r'résolution de.*S|simplexe de taille|rank.one',
'L008':r'pas un isomorphisme|unfiltered|en général|general triple',
'L009':r'complémentaire|weightwise|bigrad',
'L010':r'alternée pour le degré total|alterné pour le degré extérieur|weight.*parity',
'L011':r'homotope.*0|contract|arbitrary functor',
'L012':r'p = 0|p.*neq 0|complementary.degree.zero',
'L013':r'boundary degree|dernier|truncation|dimension shifting',
'L014':r'H\^0|H\^q|Les ombres|weightwise',
'L015':r'binomial coefficient|structures multiplicatives|ordinary cup product',
'L016':r'ombre|reconstitue|full.faithful|g1031',
'L017':r'raffinant|compatible avec multiplication|g1048|derived unit',
'L018':r'T.?-.?1|rationaliz|rationalis|Sullivan|produits infinis|infinite product',
'L019':r'produits infinis|infinite product|finite.*simplex|completion',
'L020':r't.?-.?1|triple|en marge|specializ',
'L021':r'importante|divided.power.*structure|PD.*structure',
'L022':r'boundar|descend|differential compatibility|cohomolog.*operation',
'L023':r'virtuel|admissible|g1004|quasi.isom',
'L024':r'simplement connexe|homotopy recovery|homotopy.*type|@305',
'L025':r'Steenrod|Whitney|claims #243|automorphism',
'L026':r'modèles minimaux|minimal.model|Sullivan',
'L027':r'Künneth|Kunneth|plat|flatness',
'L028':r'coalgèbre|copuiss|corepresent|duale',
'L029':r'base.change|extension de.*base|integral tensor|base-ring',
'L030':r'quelconques|colimit|inductives|homotopy.colimit',
'L031':r'complété|completed|reflex|finite support',
'L032':r'topos|Anneau|ringed|Faisceautisation',
'L033':r'flasque|flabby|résolution|resolution',
'L034':r'cosimplic|Deligne|De Rham condition',
'L035':r'paracompact|souvenirs|local hypothesis',
'L036':r'dT|multiplication.*noyau|Koszul|résolution de.*k',
'L037':r'compatible|est faux|square.zero|transported product',
'L038':r'multiplicative.*cohom|invariant.*universel|universal.*invariant',
'L039':r'ignore|homotopy|plus fins|candidate',
'L040':r'semi.simplic|Delta.*inj|degenera|PRETOT A\.12|TOTASPH C\.10',
'L041':r'Eilenberg|Steenrod|cohérence|monoidal|monoïdal',
'L042':r'binomial|Horel|@304|Int\(',
'L043':r'operatorname\{Hom\}.*mathbb\{Z\}|version homologique|coefficient algebras|N51',
'L044':r'inclusion diagonale|sous.module diagonal|Phi|Psi',
}
files=sorted(p for p in context.rglob('*') if p.is_file())
ledger={'created_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
'scope':'Text-only searches of supplied context after freeze; no scan access; matches are leads, not verified conclusions.',
'input_sha256':{str(p.relative_to(context)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'notes':{}}
summary=['# Lecture-note context searches','', 'Each note was searched across every supplied context text file. This index records counts and file/line locators; the companion JSON preserves the complete matching lines and offsets. A lexical hit is not an endorsement of the source claim.','', '| Note | Query | Matches | Files | First matching lines by file |','|---|---|---:|---:|---|']
for note, query in queries.items():
    run=subprocess.run(['rg','-n','-i','--json',query,str(context)],capture_output=True,text=True)
    if run.returncode not in (0,1): raise RuntimeError(run.stderr)
    hits=[]
    for line in run.stdout.splitlines():
        record=json.loads(line)
        if record['type']!='match': continue
        data=record['data']; path=Path(data['path']['text'])
        hits.append({'file':str(path.relative_to(context)),'line':data['line_number'],'text':data['lines']['text'].rstrip(),'offset':data['absolute_offset']})
    ledger['notes'][note]={'query':query,'status':'matches' if hits else 'no-match','match_count':len(hits),'hits':hits}
    by_file={}
    for hit in hits: by_file.setdefault(hit['file'],[]).append(hit['line'])
    locators='; '.join('`'+filename+':'+','.join(map(str,lines[:3]))+('…' if len(lines)>3 else '')+'`' for filename,lines in by_file.items())
    summary.append('| '+note+' | `'+query.replace('|',r'\|')+'` | '+str(len(hits))+' | '+str(len(by_file))+' | '+locators+' |')
out=Path(__file__).parent
(out/'lecture_searches.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
(out/'lecture_searches.md').write_text('\n'.join(summary)+'\n')
print(f'{len(queries)} per-note searches saved; all 8 supplied context files in search scope.')
for key,item in ledger['notes'].items(): print(key,item['match_count'])
