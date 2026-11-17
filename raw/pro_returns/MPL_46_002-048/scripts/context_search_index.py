"""Research-only context lookup, run strictly after the transcription freeze."""
from pathlib import Path
import re, json

ROOT=Path(__file__).resolve().parents[1]
CTX=ROOT.parent/'context'
assert 'transcription frozen ' in (ROOT/'progress.log').read_text()
groups={
 'programme_witness':['Fourier','compatibil','Jacob','Hodge','Néron','Matsusaka','Picard','cycles'],
 'torsors_lang':['torseur','Lang','gerbe','coïncidence','rigidification','non dégénérée'],
 'unit_modules':['locale liberté','type fini','Fitting','Filting','p-structure'],
 'frobenius_geometry':['Frob','préschémas','homéomorph','infinitésimal','voisinage','Symm'],
 'cartier_picard':['Cartier','logarith','p-torsion','p^A','p^B','Dieudonn','Verschiebung'],
 'etale_topos':['étale','topos','topologie','équivalence','trivialité','fonctoriel'],
 'brauer_linear_systems':['Brauer','Séveri','Severi','systèmes linéaires','descente','grassmann','incidence'],
 'reused_typescripts':['uniforme','Coxeter','graphes','Tribu','injectifs','divisible'],
}
source=CTX/'MPL_16+47+54+44_transcription.tex'
s=source.read_text();blocks=[];cote=None
markers=list(re.finditer(r'\\(cotefile|scanpage)\{([^}]+)\}',s))
for j,m in enumerate(markers):
 if m.group(1)=='cotefile':cote=m.group(2);continue
 end=markers[j+1].start() if j+1<len(markers) else len(s)
 blocks.append((cote,m.group(2),s[m.end():end]))
out={'source':source.name,'groups':{}}
lines=['# Context search index','',
       'Research-only textual searches after the freeze; hits are leads, not proof or paleographic verification.',
       'The main notes also cite exact subsections in Hua’s modernised reading. Oda’s printed PDF has a separate inspected-page record in oda_cartier.md.','']
for name,terms in groups.items():
 hits=[]
 for cote,scan,block in blocks:
  matches=[term for term in terms if term.casefold() in block.casefold()]
  if matches:hits.append({'cote':cote,'scan':int(scan),'terms':matches})
 hua=[];section='Opening'
 for line in (CTX/'hua_project'/'46.modern.tex').read_text().splitlines():
  if re.match(r'\\(?:sub)?section\*',line):section=line
  if any(t.casefold() in line.casefold() for t in terms) and section not in hua:hua.append(section)
 out['groups'][name]={'queries':terms,'old_transcription_hits':hits,'hua_sections':hua}
 lines += [f'## {name}','', 'Queries: '+', '.join(terms)+'.','',
           'Context transcription: '+('; '.join('{}:{:03d} ({})'.format(h['cote'],h['scan'],', '.join(h['terms'])) for h in hits) or 'No matching text')+'.','',
           'Hua subsection hits:',''] + ['- '+x for x in hua]+['']
dest=ROOT/'records'/'research';dest.mkdir(exist_ok=True)
(dest/'context_search_index.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(dest/'context_search_index.md').write_text('\n'.join(lines)+'\n')
print('Wrote context-search index for',len(groups),'topic families.')
