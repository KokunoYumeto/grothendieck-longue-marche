from pathlib import Path
import subprocess,json,re
ROOT=Path(__file__).resolve().parents[1]
CONTEXT=ROOT.parent/'context'
queries={
 'R01-R02':r'reflexive|double dual|thesis|module|plat',
 'R03':r'foncteur|fibre|étale',
 'R04-R12':r'descente|changement de base|Corrections|SGAD|Raynaud',
 'R05-R07':r'Steinberg|Kostant|normal form|regular|perfect|parfait|racines',
 'R08-R10':r'Moishezon|projectivity|hyperplane|ample|polarisation|restriction|exacte',
 'R11':r'adjoint|Hom|injectif',
 'R13-R15':r'lusin|dyadi|polon|distribution|Bourbaki|limite projective|séparé',
 'R16':r'anab|Galois|foncteur|S15|LM7 E.23',
 'FR19b-FR20b':r'\bCM\b|norme|conjugaison|corps|p\^\{|1/4|Taniyama|Shimura',
 'standing_unverified':r'vérifi|À voir|Question|probab|conject|Giraud|présum|admis|ultérieure',
 'standing_titles':r'titre|pages|page counts|page|Summary|§102|§1.1 #3',
}
files=[CONTEXT/'README.md',CONTEXT/'notes/RESULTS_STATE.md',CONTEXT/'MPL_16+47+54+44_transcription.tex',CONTEXT/'MPL_16+47+54+44_notes.md']
out={}
for q,pattern in queries.items():
 results=[]
 for f in files:
  p=subprocess.run(['rg','-n','-i',pattern,str(f)],capture_output=True,text=True)
  assert p.returncode in (0,1),(f,p.stderr)
  lines=f.read_text().splitlines(); cote=scan=None; locations={}
  for n,l in enumerate(lines,1):
   c=re.search(r'\\cotefile\{([^}]+)',l); s=re.search(r'\\scanpage\{([^}]+)',l)
   if c: cote=c[1]
   if s: scan=s[1]
   locations[n]=(cote,scan)
  hits=[]
  for hit in p.stdout.splitlines():
   n,txt=hit.split(':',1); n=int(n); c,s=locations[n]
   hits.append({'line':n,'cote':c,'scan':s,'text':txt})
  results.append({'file':str(f.relative_to(CONTEXT.parent)),'hits':hits})
 out[q]={'pattern':pattern,'results':results}
(ROOT/'records/research_context_search.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print({q:sum(len(r['hits']) for r in x['results']) for q,x in out.items()})
