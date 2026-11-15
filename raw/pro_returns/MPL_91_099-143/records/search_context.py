"""Per-note literal/regex searches of the supplied text context; no scan processing."""
from pathlib import Path
import subprocess,json,re
ROOT=Path(__file__).resolve().parents[1]
CTX=ROOT.parent/'context'
queries={
'RN099-01':['géométrique','pro-schématique','quasi-schématique','descent'],
'RN101-01':['épimorph','coquotient','finite limits','effectivity','descent'],
'RN101-02':['factoris','épim','monom','effectivity'],
'RN102-01':['système projectif','subgroup','centralizer','profinite'],
'RN104-01':['constructible topology','retrocompact','rétrocompact','Acons'],
'RN105-01':['locally closed','constructible pieces','rétrocompact'],
'RN106-01':['generic point','irréductible','constructible topology'],
'RN107-01':['antifique','antifinie','local','constructible topology'],
'RN108-01':['rétrocompact','constructible sets','rational map'],
'RN109-01':['quasi.compact','basis','retrocompact','constructible'],
'RN110-01':['constructible sets','Greenberg','verify'],
'RN110-02':['constructible sets','proper','Acons'],
'RN111-01':['constructible topology','affine','Acons'],
'RN111-02':['monomorph','constructible','image'],
'RN113-01':['constructible pieces','partitions','geometric application',r'\bHom\b'],
'RN114-01':['full.faith','Cons Aff',r'\bInd\b',r'\bHom\b'],
'RN115-01':['Acons','partitions','homeomorph'],
'RN115-02':['Acons','colimit','constructible topology'],
'RN116-01':['constructible topology','compact','T_0'],
'RN118-01':['Néron','Greenberg','flasque',r'\bHom\b'],
'RN118-02':['proscheme','Pro\\(Sch','flasque','fully faithful'],
'RN120-01':[r'\bInd\b',r'\bHom\b','quasi.separ','locally compact'],
'RN122-01':['affine','compact','locally closed','Acons'],
'RN126-01':['thick','épais','Greenberg'],
'RN126-02':['thick','maximal','Greenberg'],
'RN126-03':['noether','noeth','closure','constructible'],
'RN128-01':['Mittag','M\\.L\\.','thick','Greenberg'],
'RN128-02':['ideal','closure','finite type','thick'],
'RN131-01':['DVR','valuation','proper','Greenberg'],
'RN131-02':['generically separable','thick','Greenberg'],
'RN131-03':['étale','etale','exists','Greenberg'],
'RN132-01':['bounded','simple','smooth','constructible sets'],
'RN132-02':['91-greenberg-rational-maps-constructible','complete discrete','smooth','piecewise'],
'RN134-01':['Laurent','A\\(\\(t\\)\\)','unit','representable'],
'RN135-01':['immersion','Laurent','component','irreducible'],
'RN135-02':['isomorphism','Laurent','transition'],
'RN135-03':['nilpot','reduced','Acons','Laurent'],
'RN136-01':[r'Pro\(|pro-préschéma|pro-prescheme',r'\bHom\b','finite presentation','Serre','Néron'],
'RN136-02':['Greenberg','piecewise',r'\bHom\b','finite index'],
'RN138-01':['nilpot','infinitesimal','truncat','Greenberg'],
'RN140-01':['automorph','coordinate','Greenberg','translation'],
'RN142-01':['tangent','derivation','affine space','V_1'],
'RN142-02':['composition','polynomial','coordinate','Greenberg'],
'RN142-03':['determinant','automorph','coordinate'],
'RN142-04':['nilpot','truncat','coordinate','Greenberg'],
'RN100-01':['inverse limit','projective','subgroup','continuous'],
'RN119-01':['exterior algebra','wedge','graded','symplectic'],
'RN123-01':['exterior algebra','Lefschetz','Φ₀'],
'RN127-01':['cohomolog',r'\bLie\b','derivation','LM1 D.11'],
'RN129-01':['envelop','derivation',r'\bLie\b','p-alg'],
'RN139-01':['formal group','symplectic',r'\bLie\b'],
'RN139-02':['truncat','formal',r'\bLie\b','Greenberg'],
'RN141-01':['Jacobian','formal',r'\bLie\b','homomorph'],
'RN143-01':['orthogonal','Cayley','symplectic','formal'],
'RN139-03':['symplectic','2n','formal group'],
'RNCTX-01':['DVR','proper extension','valuation','FLAGGED_149 C3','F17.1','F17.7'],
'TITLE-INDEX':['Greenberg','Néron','page','pp.'],
'PLAN-CROSSWALK':['K_G','residue','duality','intersection','S19','Hom','Greenberg'],
'OPEN-DISPOSITION':['LM7 E.23','FLAGGED_149 B9','LM1 D.11','LM4 D.12','LM4 F.7'],

}
reports=[]
for ident,terms in queries.items():
 args=['rg','--json','-n','-i']
 for term in terms:args += ['-e',term]
 args += [str(CTX)]
 run=subprocess.run(args,text=True,capture_output=True)
 assert run.returncode in (0,1),(ident,run.stderr)
 hits=[]
 for line in run.stdout.splitlines():
  x=json.loads(line)
  if x.get('type')!='match':continue
  d=x['data'];txt=d['lines']['text'].strip();entry=re.search(r'^- \*\*(.*?)\*\*',txt)
  hits.append({'file':str(Path(d['path']['text']).relative_to(CTX)),'line':d['line_number'],'entry':entry[1] if entry else 'README/section text','excerpt':txt[:180]})
 reports.append({'id':ident,'queries':terms,'hits':hits})
(ROOT/'records/context_searches.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in reports))
md=['# Per-note searches of supplied context','','Search scope: the two files actually supplied, README.md and notes/RESULTS_STATE.md. The latter contains excerpts, several already truncated in the source. A missed literal term is a bounded search result, not a mathematical exclusion. Referenced underlying reports were not included in the ZIP.','']
for r in reports:
 md += ['## '+r['id'],'','Queries: '+ '; '.join('`'+q+'`' for q in r['queries']), '']
 if r['hits']:
  md += ['| Supplied file:line | Entry / location |','|---|---|']
  md += ['| '+h['file']+':'+str(h['line'])+' | '+h['entry'].replace('|','\\|')+' |' for h in r['hits']]
 else:md += ['No literal hit in the supplied files.']
 md += ['']
(ROOT/'records/context_searches.md').write_text('\n'.join(md))
print('Searched',len(reports),'note queries across both context files.')
for r in reports:
 print(r['id'],':',', '.join(dict.fromkeys(h['entry'] for h in r['hits'])))
