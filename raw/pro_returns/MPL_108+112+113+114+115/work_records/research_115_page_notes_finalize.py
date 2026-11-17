from pathlib import Path
import json,re,hashlib,collections
root=Path('.')
out=Path('deliverable/work_records')
jpath=out/'research_115_page_notes.json'
mdpath=out/'research_115_page_notes.md'
records=json.loads(jpath.read_text())
md=mdpath.read_text()
assert '**Literal cue (verbatim frozen TeX;' not in md, 'Already finalized; do not duplicate metadata.'
S={
'R01':(2,'reading question',r"``Correspondances'' fonctorielles"),
'R02':(3,'conjecture',r'\overset{?}{\simeq}'+'\n'+r'H_B\bigl(\Psi_*,f^\circ_!(\Phi^*)\bigr)'),
'R03':(3,'conjecture',r'\overset{?}{\simeq}\operatorname{Hom}_{\widehat A}(\unsure{f^*b},a)'),
'R04':(3,'unproved claim',r"f^*(b)=\varinjlim_{a'\text{ ds }A/b}a'^{\unsure{\circ}}"),
'R05':(3,'withdrawn in the same text',r'\deleted{\widehat B^\circ\unsure{\longrightarrow|{-}}\widehat A}'),
'R06':(4,'unproved claim',r'formée des foncteurs commutant aux $\varinjlim$.'),
'R07':(4,'unproved claim',r'\underline{\operatorname{Hom}}_A(X,Y)&\overset{\mathrm{def}}=p_{B*}\underline{\operatorname{Hom}}_{A\times B}(X,Y)'),
'R08':(4,'reading question',r'savoir $b\longmapsto{}^dX(b)=\underline{\operatorname{Hom}}_B(p_B^*(L),X)$'),
'R09':(4,'unpursued implication',r"Cas $B=A^\circ$, d'où élément canonique"),
'R10':(4,'unproved claim','est pleinement fidèle,'),
'R11':(4,'unproved claim',r"le composé est le foncteur canonique dit ``de Yoneda'' pour"),
'R12':(4,'reading question',r'\xleftarrow{\sim}'+'\n'+r'\operatorname{Hom}_{\widehat A}'),
'R13':(4,'unproved claim',r'on trouve donc $(p_B^*L)^M\simeq p_B^*L$'),
'R14':(6,'unproved claim','Toutes les flèches du diagramme sont des équivalences de catégories'),
'R15':(6,'self-flagged',r"Je suppose $I,J$ finis pour ``play safe''."),
'R16':(8,'unproved claim','paires de foncteurs adjoints'),
'R17':(8,'unproved claim',r'-- ce qui caractérise $\psi_A$ à iso unique près'),
'R18':(8,'unproved claim',r'\varphi_{A^\circ}&=\psi_A'),
'R19':(8,'unproved claim',r'iso si $\Phi\in\mathrm{Ob}\,A$ ou $\Psi\in\mathrm{Ob}\,A$'),
'R20':(8,'conjecture',r'\alpha_\Phi,\beta_\Psi$ ? Iso (si et) seulement si $\Phi$ resp. $\Psi$ est représentable ?'),
'R21':(8,'conjecture','tjrs une équivalence faible (sans doute pas).'),
'R22':(8,'conjecture',r'Les foncteurs $\varphi_A$ et $\psi_A$ transforment-ils équiv. faibles en isom ?'),
'R23':(8,'unproved claim',r'H^A(a,b)\overset{\inserted{\text{ou}}}{=}\mathrm{Hom}_A(b,a)'),
'R24':(9,'withdrawn in the same text',r'X_1\otimes X_2\simeq\mathrm{Hom}(X_1^\vee,X_2^\vee;\underline1)'),
'R25':(9,'withdrawn in the same text',r'\deleted{\unsure{A}}\quad\mathcal F(X^\vee)\ ?'),
'R26':(9,'withdrawn in the same text',r'\mathrm{Top}(A)\arrow[r,"\varphi"]&X\arrow[r,no head,"\psi"]&\mathrm{Top}(B)'),
'R27':(10,'unproved claim',r'\langle\Phi_*,f^{\circ *}(\Psi^*)\rangle_A&\simeq\langle f_!(\Phi_*),\Psi^*\rangle_B'),
'R28':(11,'reading question',r'H^x\in A^\vee\qquad H^x(\cdot)=\mathrm{Hom}_B(a,x)'),
'R29':(11,'unproved claim',r'la catégorie des triples $(H_*,H^*,\alpha)$'),
'R30':(11,'reading question',r'''H'^*(b)\arrow[u,"\varphi'_*"']'''),
'R31':(11,'unproved claim',r'Pour un foncteur pl. fid \(A\xrightarrow{\varphi}B\), on déduit un foncteur'),
'R32':(12,'unproved claim',r'$\widetilde{A^\circ}\simeq\widetilde A^\circ$ canonique'),
'R33':(12,'unproved claim',r'Il suffit que $f$ soit strict. génér. ou fon. cogénérateur.'),
'R34':(12,'conjecture',r"v=v'\circ\varphi_*\ ?"),
'R35':(12,'unproved claim',r'\unsure{la réunion} des \unsure{images} essentielles de'),
'R36':(12,'reading question',r'''B&\widetilde B\arrow[u,"\widetilde f"']&\widehat B\arrow[u,"f^*"']'''),
'R37':(14,'unproved claim',r'(Kar(A^\circ))^\circ \simeq Kar(A)'),
'R38':(14,'reading question',r'A=\widehat A\unsure{\cap|,}A^{\vee\circ}'),
'R39':(14,'self-flagged',r"et $N'-N$ n'est pas tjrs une équivalence."),
'R40':(15,'unproved claim',r'\underline{\mathrm{Hom}}(A,M)\simeq'+'\n'+r'\underline{\mathrm{Hom}}_!(\widehat A,M)\simeq'),
'R41':(15,'unproved claim',r'\mathrm{Hom}_!(\widehat A_{ab},M).'),
'R42':(15,'reading question',r'\mathrm{Hom}_!(\widehat A_{ab}'),
'R43':(15,'unproved claim',r'\text{cofaisceaux sur }A,\ \text{à val. dans }M.'),
'R44':(15,'unproved claim',r'\mathcal F(\mathcal X,M)^\circ\simeq\mathcal F^\vee(\mathcal X,M^\circ)'),
'R45':(15,'unproved claim',r'\mathcal F(\mathcal X,M)\simeq\mathcal F^\vee(\mathcal X^\circ,M)'),
'R46':(7,'reading question',r'\node at (2,-.65){$B$};'),
'C01':(2,'unpursued implication',r"``Correspondances'' fonctorielles"),
'C02':(6,'unpursued implication',r'=\underline{\mathrm{Hom}}(A^\circ,B^\circ;\mathrm{Ens})'),
'C03':(14,'unpursued implication',r"Alors on définit une catégorie $\Sigma'$"),
'C04':(11,'unpursued implication',r'H_x(a)=\mathrm{Hom}_B(a,x)'),
'C05':(6,'unpursued implication','Toutes les flèches du diagramme sont des équivalences de catégories'),
'C06':(14,'own idea','somme des sous-catégories pleines'),
}
assert len(S)==52
allowed={'conjecture','unproved claim','unpursued implication','own idea','reading question','self-flagged','withdrawn in the same text'}
validation=[]
page_contents={}
for n in records:
 key=n['id'][4:]
 scan,kind,q=S[key]
 assert kind in allowed
 src=Path(f'deliverable/pages/MPL_108+112+113+114+115_115_scan{scan:03}.tex')
 data=src.read_bytes()
 text=data.decode('utf-8')
 page_contents[src]=(data,text)
 assert q in text, (n['id'],q,str(src))
 if 'kind' in n and n['kind'] not in allowed:n['descriptive_kind']=n['kind']
 n['kind']=kind
 n['literal_quote']=q
 n['literal_quote_cote']='115'
 n['literal_quote_scan']=f'{scan:03}'
 n['literal_quote_source']=str(src)
 n['literal_quote_validation']={
  'exact_substring_match':True,
  'match_count':text.count(q),
  'first_matching_line':text[:text.index(q)].count('\n')+1,
  'source_sha256':hashlib.sha256(data).hexdigest(),
  'method':'Exact UTF-8 decoded substring; no normalization or substitutions.'
 }
 if key=='R01':n['scope_note']=True
 if key=='R46':n['ancillary']=True
 if 'quote' in n:n['quote_notation']='Analytical/modernized anchor; the separate literal_quote field is copied verbatim.'
 validation.append(dict(id=n['id'],cote='115',scan=f'{scan:03}',source_file=str(src),literal_quote=q,**n['literal_quote_validation']))
 # Keep the descriptive heading and body; insert the exact classification and literal cue underneath it.
 pat=r'^(#{2,3} '+re.escape(n['id'])+r' — [^\n]+)\n\n'
 block=('**Kind:** `'+kind+'`'+(' — ancillary scope note.' if key=='R46' else '.')+'\n\n'
        '**Literal cue (verbatim frozen TeX; cote 115, scan '+f'{scan:03}'+'):**\n\n'
        '```tex\n'+q+'\n```\n\n'
        '**Literal-cue check:** PASS — exact substring in `'+str(src)+'`.\n\n')
 md,count=re.subn(pat,lambda m:m[1]+'\n\n'+block,md,count=1,flags=re.M)
 assert count==1,n['id']
md=md.replace('**Frozen anchor:**','**Analytical anchor (may use modernized notation):**')
md=md.replace('incoming arrows A(-,x), outgoing arrows','incoming arrows B(-,x)|_A, outgoing arrows')
md=md.replace('Each numbered note has one to four sentences, a precise scan locator, a brief literal quotation or faithfully abbreviated formula, a claim-type label, and supplied-context references.',
 'Each numbered note has a one-to-four-sentence analysis, an exact kind field, a precise scan locator, a brief verbatim TeX cue checked by exact substring matching, a separately labelled analytical anchor that may use modernized notation, and supplied-context references.')
md=md.replace('The exact STRATA C.1 statement is not supplied, as detailed after the page notes.',
 'The exact STRATA C.1 statement is not supplied, as detailed after the page notes. Kind labels classify the manuscript item or comparison, not the status of an explanatory counterexample in its body; cancelled blocks are marked “withdrawn in the same text”, and the unfinished additive line is a “reading question”. All 52 literal cues passed exact substring validation against the cited frozen page fragments; the detailed checks are in `research_115_page_notes.literal_quote_validation.json`.')
# Keep the crossing-record Markdown synchronized with the final Markdown sections.
for n in records:
 if n['id'].startswith('115-C'):
  pat=r'^### '+re.escape(n['id'])+r' — ([^\n]+)\n\n(.*?)(?=^### |\Z)'
  m=re.search(pat,md,re.M|re.S)
  assert m,n['id']
  n['content']=m[2].strip()
# Source immutability check during this operation.
assert all(p.read_bytes()==data for p,(data,_) in page_contents.items())
summary={
 'record_count':len(records),'exact_substring_passes':sum(v['exact_substring_match'] for v in validation),
 'failures':0,'allowed_kind_values':sorted(allowed),
 'kind_counts':dict(collections.Counter(n['kind'] for n in records)),
 'source_files_changed':False,'records':validation}
jpath.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
mdpath.write_text(md)
(out/'research_115_page_notes.literal_quote_validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
(out/'research_115_page_notes.literal_quote_validation.txt').write_text(
 '52 / 52 exact literal-quote substring checks passed.\n'
 'No frozen source TeX was changed.\n'
 +'\n'.join(f"{v['id']} | cote115 scan{v['scan']} | PASS | {v['source_file']}" for v in validation)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='records'},ensure_ascii=False,indent=2))
