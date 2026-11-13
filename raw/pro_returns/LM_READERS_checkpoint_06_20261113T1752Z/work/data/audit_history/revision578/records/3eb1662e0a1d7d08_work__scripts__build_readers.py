#!/usr/bin/env python3
"""Build seven self-contained LuaLaTeX books from the supplied package records.

Run from the directory containing sources/ and work/. Source files remain
unchanged. Reversible stages and byte hashes are recorded for each package.
"""
from pathlib import Path
import argparse,collections,csv,hashlib,json,re,sys,subprocess,concurrent.futures,os,time
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(Path(__file__).parent))
import editorial,mechanical_repairs
from texenv import environment
SCRIPTS=Path(__file__).parent
WORK=ROOT/'work';DATA=WORK/'data';RECORDS=WORK/'records'
BOOKS={
 'LM_FR_diplomatique':('fr',0,'Édition diplomatique'),
 'LM_FR_corrige_apparat':('fr',1,'Texte corrigé avec apparat'),
 'LM_FR_texte_de_lecture':('fr',2,'Texte de lecture'),
 'LM_EN_corrected_apparatus':('en',1,'Corrected text with apparatus'),
 'LM_EN_reading':('en',2,'Reading text'),
 'LM_FR_master_annotated':('fr',1,'Master annoté'),
 'LM_EN_master_annotated':('en',1,'Annotated master'),
}
INDEX=list(csv.DictReader((ROOT/'sources/fr/records/CURRENT_TEXT_INDEX.tsv').open(),delimiter='\t'))
CREDITS=json.loads((DATA/'frontmatter.json').read_text())
GLOSS=json.loads((DATA/'glossary_edits.json').read_text())

def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def esc(s):
 table={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','#':r'\#','%':r'\%','&':r'\&','_':r'\_','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
 return ''.join(table.get(c,c) for c in str(s))

def preamble(lang,form):
 t=(SCRIPTS/'book_preamble.tex').read_text()
 cyr='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
 defs='\n'.join(r'\newunicodechar{'+c+r'}{{\cyrfont\char"'+f'{ord(c):04X}'+'}}' for c in cyr)
 t=t.replace('% CYRILLIC DEFINITIONS',defs)
 t=t.replace('% LUA CODE',r'\begin{luacode*}'+'\n'+(SCRIPTS/'book_links.lua').read_text()+'\n'+r'\end{luacode*}')
 t=t.replace(r'\LMform=1',r'\LMform='+str(form),1)
 if lang=='fr':
  t=t.replace(r'\setcounter{tocdepth}{1}',r'\renewcommand\contentsname{Sommaire}'+'\n'+r'\setcounter{tocdepth}{1}')
 if lang=='en':
  labels={'LMlanguage':'en','LMnotelabel':'Marginal note','LMappheading':'Apparatus for this scan','LMdoubtheading':'Uncertainty retained from cancelled passages','LMmanuscriptlabel':'Manuscript','LMcorrectedlabel':'Text','LMreasonlabel':'Reason','LMomittedlabel':'omitted','LMinsertedlabel':'insertion integrated','LMlayoutlabel':'Diagram continued on the landscape page'}
  for k,v in labels.items():t=re.sub(r'\\newcommand\\'+k+r'\{[^}]*\}',lambda m:'\\newcommand\\'+k+'{'+v+'}',t)
 return t

def frontmatter(lang,form,title):
 c=CREDITS
 out=[r'\begin{titlepage}\centering',r'{\Large '+esc(c['author'])+r'\par}',r'\vspace{2cm}',r'{\huge '+esc(c['title'])+r'\par}',r'\vspace{.6cm}{\Large 1981\par}',r'\vspace{1.5cm}{\LARGE '+esc(title)+r'\par}',r'\vspace{1cm}',esc(c['archive'])+r'\par',r'Cotes 140-1, 140-2, 140-3, 140-4\par',r'1\,588 scans\par\vfill',r'13 novembre 2026\par' if lang=='fr' else r'13 November 2026\par',r'\end{titlepage}']
 if lang=='fr':
  out += [r'\section*{Note sur cette édition}',r"Ce volume réunit les notes de recherche d'Alexander Grothendieck de 1981, conservées aux archives de l'Université de Montpellier : cote 140-1, brouillon (37 scans); cote 140-2, pages 1--292 (575 scans); cote 140-3, pages 293--650 (696 scans); cote 140-4, pages 650bis--787 (280 scans). Les 116 paquets du texte vérifié sont présents, dans l'ordre des scans. Cette édition part des transcriptions et des contrôles joints; elle ne propose aucune nouvelle lecture des images."]
  if form==0:
   out += [r"Le texte diplomatique conserve les suppressions en gris, les ajouts en bleu-vert, les soulignements, les abréviations et les graphies du texte vérifié. La présentation matérielle des notes et des formules est réparée sans normaliser la notation. Les lignes institutionnelles ajoutées par l'archive au pied des scans ne sont pas manuscrites et ne sont pas reproduites; le numéro de page manuscrit reste à sa place."]
  else:
   out += [r"Le texte corrigé suit l'état final explicite de l'auteur : les passages biffés quittent le texte courant et les ajouts sont intégrés, en bleu-vert. Chaque intervention est identifiée dans le master annoté et dans le relevé des changements. Les lectures douteuses et illisibles ne sont ni résolues ni supprimées. Aucune normalisation des lettres, indices ou flèches n'est faite."]
   if form==1:out += [r"L'apparat placé à la fin de chaque scan donne la lecture du manuscrit, l'état retenu, la nature et la raison de chaque différence. Les petits repères d et i renvoient aux suppressions et aux insertions de ce scan. Une intervention entièrement à l'intérieur d'un passage biffé est comprise dans l'entrée de cette suppression. L'apparat n'est pas un commentaire mathématique."]
   else:out += [r"Cette forme de lecture omet l'apparat des variantes et les mots dont la biffure est certaine. Les indications de scan et de page sont en marge. Les doutes contenus dans les passages supprimés restent visibles sous forme de fragments liés, signalés par un poignard au lieu concerné et rassemblés à la fin du scan. Ils préservent l'incertitude de la transcription sans rétablir les passages biffés dans la phrase. Les lignes institutionnelles au pied des scans sont omises; les numéros manuscrits sont conservés."]
  out += [r"Tout passage bleu, toute indication rouge \textnormal{[illeg.\ n]} et toute marque de scan ouvre le scan correspondant dans le visualiseur de Montpellier. Une note de trois lignes au plus, si elle tient dans la colonne prévue, reste en marge; une note plus longue est placée à son point d'insertion dans le bloc de texte, en petit corps, avec un filet et l'indication \emph{Note marginale}. Les formules trop larges sont réparées à des endroits identifiés dans la source; les diagrammes qui l'exigent sont disposés en paysage. Les abréviations et la notation propres à l'auteur, notamment Sl, Gl, Autext et le double $\Gamma$, sont conservées."]
 else:
  out += [r'\section*{About this edition}',r"This volume contains Alexander Grothendieck's research notes of 1981, held in the Montpellier archive: cote 140-1, a draft (37 scans); cote 140-2, manuscript pages 1--292 (575 scans); cote 140-3, pages 293--650 (696 scans); and cote 140-4, pages 650bis--787 (280 scans). All 116 packages and all 245 translation units are included in scan order. This edition works from the supplied transcription, translation and checking records; it proposes no new reading of the handwriting.",r"The corrected text follows the author's explicit final state. Cancelled words leave the running text; insertions are integrated and shown in teal. Every difference is recorded in the annotated master. The translation follows the supplied English package texts and glossary, with one documented correction from ``structure with loops'' to ``loop structure''. The author's letters, indices, arrows and forms such as Sl, Gl, Autext and the doubled $\Gamma$ remain unchanged. Doubtful and illegible readings are retained."]
  if form==1:out += [r"The apparatus at the end of each scan gives the manuscript reading, the adopted text, the kind of intervention and its reason. Small d and i references identify deletions and insertions within the scan. Revisions entirely inside a cancelled passage belong to that cancellation's entry. The apparatus supplies no mathematical commentary."]
  else:out += [r"This reading form omits the variant apparatus and certainly cancelled wording. Scan and manuscript-page numbers are confined to the margin. Uncertainty inside cancelled passages remains visible in linked fragments, indicated by a dagger at its original place and collected at the end of the scan. These uncertainty fragments preserve the transcription's doubts without restoring cancelled passages to the sentence. The archive's institutional footer is omitted; each independently transcribed manuscript number remains."]
  out += [r"Every blue passage, red \textnormal{[illeg.\ n]} marker and scan mark links to its scan in the Montpellier viewer. A marginal note stays in the margin when it fits the note column in at most three lines. Longer notes appear at their insertion point in the text block, in small type, with a rule and the label \emph{Marginal note}. Wide formulae and diagrams have repairs at identified source locations. Diagrams needing more room appear on landscape pages."]
 out += [r'\subsection*{'+('Production et crédits' if lang=='fr' else 'Production and credits')+'}',esc(c['required_credit_transcription'])+r'.\par']
 if lang=='en':out += [esc(c['required_credit_translation'])+r'.\par']
 out += [esc(c['required_credit_edition'])+r'.\par',esc(c['additional_prior_ai_credit_'+lang])+r'\par',r'\subsection*{'+('Sources et travaux antérieurs' if lang=='fr' else 'Sources and earlier work')+'}',esc(c['archive'])+r'. \url{'+c['archive_url']+r'}\par',esc(c['witness_policy_'+lang]),r'\begin{itemize}']
 out += [r'\item '+esc(w)+'.' for w in c['witnesses_'+lang]]
 out += [r'\end{itemize}',r'\subsection*{'+('Droits' if lang=='fr' else 'Rights')+'}',esc(c['rights_'+lang]),r'\clearpage',r'\tableofcontents',r'\clearpage']
 return '\n\n'.join(out)+'\n'

def raw_package(package,lang):
 p=ROOT/'sources'/('fr/texts' if lang=='fr' else 'en/packages')/(package+('_en' if lang=='en' else '')+'.tex')
 return p.read_text()

def package_data(package,lang,stage):
 raw=raw_package(package,lang)
 t,mechanical=mechanical_repairs.repair(raw,package,lang)
 layout=[]
 import layout_repairs
 if stage!='baseline':
  t,layout=layout_repairs.repair(t,package,lang)
 else:
  t,layout=layout_repairs.repair_empty_cells(t,package,lang)
 # Exact editorial annotations are generated from the common transformed source.
 key=sha(t+Path(editorial.__file__).read_text())
 cache=DATA/'cache'/stage/lang;cache.mkdir(parents=True,exist_ok=True)
 jf=cache/(package+'.json');tf=cache/(package+'.tex')
 if jf.exists() and tf.exists() and json.loads(jf.read_text()).get('key')==key:
  obj=json.loads(jf.read_text());annotated=tf.read_text();entries=obj['entries'];meta=obj['meta']
 else:
  annotated,entries,meta=editorial.annotate(t,package,lang)
  tf.write_text(annotated);jf.write_text(json.dumps({'key':key,'entries':entries,'meta':meta},ensure_ascii=False))
 if lang=='en':
  for g in GLOSS:
   if g['package']!=package:continue
   assert annotated.count(g['old'])==g['expected_occurrences'],g
   annotated=annotated.replace(g['old'],r'\var{'+g['old']+'}{'+g['new']+'}{glossary consistency}{'+g['id']+'}')
   entries.append(dict(id=g['id'],package=package,cote=g['cote'],scan=int(g['scan']),source_line=g['source_line'],source_path=g['source'],place=g['id'],manuscript=g['old'],corrected=g['new'],corrected_tex=g['new'],kind=g['kind'],reason=g['reason'],argument=g['old'],math_mode=False,doubts=[],parent_id='',inherited_doubt=False))
 provenance={'package':package,'language':lang,'source_sha256':sha(raw),'layout_source_sha256':sha(t),'master_body_sha256':sha(annotated),'scan_sequence':re.findall(r'\\scanpage\{(\d+)\}',raw),'mechanical':mechanical,'layout':layout,'variants':len(entries)}
 return annotated,entries,meta,provenance

def mathwrap(content,entry):return r'\('+content+r'\)' if entry.get('math_mode') else content

def apparatus(entries,lang):
 if not entries:return ''
 out=[r'\ifnum\LMform=1',r'\begin{LMapparatus}']
 for e in entries:
  original=e['manuscript']
  if e.get('inherited_doubt'):original=r'\LMdoubtcopy{'+original+'}'
  original=mathwrap(original,e)
  if e['kind']=='deletion':corrected=r'\emph{\LMomittedlabel}'
  elif e['kind']=='insertion':corrected=r'\emph{\LMinsertedlabel}'
  else:corrected=e['corrected']
  kind={'deletion':'suppression','insertion':'insertion'}.get(e['kind'],e['kind']) if lang=='fr' else e['kind']
  out.append(r'\LMentry{'+e['id']+'}{'+esc(kind)+'}{'+original+'\n}{'+corrected+'}{'+esc(e['reason'])+'}{}')
 out += [r'\end{LMapparatus}',r'\fi']
 carry=[e for e in entries if e['kind']=='deletion' and (e.get('doubts') or e.get('inherited_doubt'))]
 if carry:
  out += [r'\ifnum\LMform=2',r'\par\smallskip\begingroup\footnotesize\Needspace{4\baselineskip}\csname @beginparpenalty\endcsname=10000\relax\noindent\textcolor{gray}{\rule{.2\linewidth}{.35pt}}\par\nobreak',r'\noindent\textit{\LMdoubtheading.}\par\nobreak']
  for e in carry:
   if hasattr(editorial,'carryover'):contents=editorial.carryover(e)
   elif e.get('inherited_doubt'):contents=mathwrap(r'\unsure{'+e['manuscript']+'}',e)
   else:contents=r'\quad '.join(mathwrap(d['raw'],d) for d in e['doubts'])
   out.append(r'\LMcarryover{'+e['id']+'}{'+contents+'\n}')
  out += [r'\par\endgroup\smallskip',r'\fi']
 return '\n'.join(out)+'\n'

def assemble_language(lang,stage,wanted=None):
 rows=[r for r in INDEX if not wanted or r['package'] in wanted]
 pieces=[];allentries=[];provenance=[];metas=[];cote=None
 for row in rows:
  pkg=row['package'];ann,entries,meta,prov=package_data(pkg,lang,stage)
  allentries+=entries;provenance.append(prov);metas.append(meta)
  if cote!=row['cote']:
   cote=row['cote'];pieces += [r'\clearpage\LMcote{'+cote+'}',r'\section*{Cote '+cote+r'}\addcontentsline{toc}{section}{Cote '+cote+'}']
  pieces += ['% BEGIN PACKAGE '+pkg,r'\ifnum\LMform<2\Needspace{11\baselineskip}\subsection*{Scans '+row['scans'].replace('-','--')+r'}\fi']
  ms=list(re.finditer(r'\\scanpage\{(\d+)\}',ann))
  if ms and ms[0].start():pieces.append(ann[:ms[0].start()])
  for i,m in enumerate(ms):
   end=ms[i+1].start() if i+1<len(ms) else len(ann)
   scan_text=ann[m.start():end].rstrip()
   deferred_spacing=''
   # This recorded source-local reservation belongs immediately before scan
   # 495, after any generated apparatus or residual-doubt block for scan494.
   if pkg=='LM_C3-492-510' and int(m[1])==494 and stage!='baseline':
    reservation=re.search(r'(\\Needspace\{(?:6|18)\\baselineskip\})\s*$',scan_text)
    if reservation:
     deferred_spacing=reservation.group(1)
     scan_text=scan_text[:reservation.start()].rstrip()
   pieces.append(scan_text+'\n')
   es=[e for e in entries if e['scan']==int(m[1])]
   pieces.append(r'\LMflushnotes\LMflushpages'+'\n'+apparatus(es,lang))
   placements=[r for r in prov['layout'] if r.get('scan')==int(m[1]) and (r.get('kind') in ('landscape layout','landscape diagram','inline formula displayed','inline formula moved to display') or r.get('id') in ('140-2-302-D1','140-2-344-D1','140-3-561-D1','140-2-348-M1'))]
   if placements:
    pieces += [r'\ifnum\LMform=1',r'\par\begingroup\footnotesize']
    for r in placements:
     reason=r.get('reason','')
     if lang=='fr':
      reason=('Diagramme reporté sur une page en paysage, avec un repère à son emplacement; les objets, flèches et lectures restent identiques.' if 'landscape' in r.get('kind','') else 'Formule du texte courant disposée sur deux lignes, avec un repère à son emplacement; les symboles et lectures restent identiques.')
     pieces.append(r'\noindent\texttt{'+r.get('id','')+r'} \textit{'+('Disposition' if lang=='fr' else 'Layout placement')+'}. '+esc(reason)+r'\par')
    pieces += [r'\endgroup\fi']
   if deferred_spacing:pieces.append(deferred_spacing)
  pieces += ['% END PACKAGE '+pkg]
 body='\n'.join(pieces)+'\n'
 from instrument_marks import instrument
 body,mark_records=instrument(body)
 (WORK/stage/(lang+'_source_marks.json')).parent.mkdir(exist_ok=True)
 (WORK/stage/(lang+'_source_marks.json')).write_text(json.dumps(mark_records,ensure_ascii=False))
 return body,allentries,provenance,metas

def build(args):
 selected=list(BOOKS) if not args.books else args.books.split(',')
 needed={BOOKS[b][0] for b in selected};wanted=set(args.packages.split(',')) if args.packages else None
 output=WORK/args.stage;output.mkdir(exist_ok=True)
 for lang in sorted(needed):
  body,entries,prov,meta=assemble_language(lang,args.stage,wanted)
  suffix='_'+args.label if args.label else ''
  for book in [b for b in selected if BOOKS[b][0]==lang]:
   _,form,title=BOOKS[book]
   name=book+suffix
   tex=preamble(lang,form)+'\n'+r'\hypersetup{pdftitle={'+esc(CREDITS['title']+' — '+title)+r'},pdfauthor={Alexander Grothendieck}}'+'\n'+r'\begin{document}'+'\n'
   if not args.no_frontmatter:tex+=frontmatter(lang,form,title)
   tex+='% COMMON MASTER BODY SHA256 '+sha(body)+'\n'+body+r'\end{document}'+'\n'
   (output/(name+'.tex')).write_text(tex)
   print('WROTE',name,len(tex.encode()),'bytes',len(prov),'packages',flush=True)
  (output/(lang+suffix+'_provenance.json')).write_text(json.dumps({'body_sha256':sha(body),'packages':prov,'entries':entries,'metadata':meta},ensure_ascii=False,indent=2)+'\n')
 if args.compile:
  def run(book):
   name=book+('_'+args.label if args.label else '')
   stdout=[]
   for run_number in range(1,args.runs+1):
    r=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',name+'.tex'],cwd=output,env=environment(),capture_output=True,text=True)
    stdout.append('RUN '+str(run_number)+'\n'+r.stdout+r.stderr)
    if run_number==1 and args.runs>1:
     (output/(name+'.pass1.log')).write_bytes((output/(name+'.log')).read_bytes())
    if r.returncode:break
   (output/(name+'.stdout')).write_text('\n'.join(stdout))
   print('COMPILE',name,r.returncode,(r.stdout+r.stderr)[-500:],flush=True)
   return r.returncode
  with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as ex:results=list(ex.map(run,selected))
  return 1 if any(results) else 0
 return 0

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--stage',default='build');ap.add_argument('--books');ap.add_argument('--packages');ap.add_argument('--label');ap.add_argument('--compile',action='store_true');ap.add_argument('--jobs',type=int,default=2);ap.add_argument('--runs',type=int,default=2);ap.add_argument('--no-frontmatter',action='store_true');args=ap.parse_args();raise SystemExit(build(args))
