"""Assemble edition records from the verified build and its source provenance."""
from pathlib import Path
import collections,csv,hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[2];WORK=ROOT/'work';R=WORK/'records';D=WORK/'data'
sys.path.insert(0,str(Path(__file__).parent))
from build_readers import BOOKS,INDEX

def readrows(path):return list(csv.DictReader(Path(path).open(),delimiter='\t'))
def write_tsv(path,fields,rows):
 with Path(path).open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t',extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(rows)
def pathfix(s):return str(s).removeprefix('sources/')
def data(name):return json.loads((D/name).read_text())
def main():
 pks={r['package']:r for r in INDEX}
 prov={l:json.loads((WORK/'build'/(l+'_provenance.json')).read_text()) for l in ('fr','en')}
 # Authorial change tables use the checked originals, before layout encodings.
 changes={l:data('editorial_'+l+'.json')['entries'] for l in ('fr','en')}
 for g in data('glossary_edits.json'):
  changes['en'].append(dict(id=g['id'],cote=g['cote'],scan=g['scan'],package=g['package'],place=g['id'],source_path=g['source'],source_line=g['source_line'],manuscript=g['old'],corrected=g['new'],kind=g['kind'],reason=g['reason']))
 cols=['id','cote','scan','package','place','source_path','source_line','manuscript','corrected','kind','reason']
 for lang in ('fr','en'):write_tsv(R/('CHANGES_'+lang.upper()+'.tsv'),cols,changes[lang])
 before=data('layout_before_sites.json');passed=data('layout_pass_sites.json');fonts=data('font_repairs.json')['records']
 fixrows=[];mechanical=[]
 for reader,(lang,form,title) in BOOKS.items():
  for package in prov[lang]['packages']:
   for r in package['layout']:
    fixrows.append(dict(reader=reader,language=lang,package=package['package'],cote=r.get('cote',pks[package['package']]['cote']),scan=r['scan'],source_path=pathfix(r.get('source_path','')),source_line=r['source_line'],id=r.get('id',''),record_basis='explicit source repair',what_was_wrong=r['kind'],what_was_done=r['reason'],old=r.get('old',''),new=r.get('new','')))
   for r in package['mechanical']:
    row=dict(reader=reader,language=lang,package=package['package'],cote=pks[package['package']]['cote'],scan=r['scan'],source_path=pathfix(r['source_path']),source_line=r['source_line'],id=r['id'],record_basis='COMPILE.tsv mechanical repair',what_was_wrong=r['kind'],what_was_done=r['reason'],old=r.get('before',''),new=r.get('after',''))
    mechanical.append(row);fixrows.append(row)
  for r in fonts:
   if r['language']!=lang:continue
   fixrows.append(dict(reader=reader,language=lang,package=r['package'],cote=r['cote'],scan=r['scan'],source_path=r['source_path'],source_line=r['source_line'],id=r['id'],record_basis='font glyph proof',what_was_wrong='Requested bold Gamma rendered with ordinary glyph',what_was_done=r['reason'],old=r['command'],new=r['command']+'; rendering macro '+r['rendering_implementation']))
  # Reconcile every historical problem, including those fixed by note placement.
  for basis,items in [('OVERFULL_BEFORE.tsv',before),('TYPESET_PASS_CHANGES.tsv',passed)]:
   for n,r in enumerate(items,1):
    if basis=='TYPESET_PASS_CHANGES.tsv':
     original_language='en' if r.get('reader','').startswith('LaLongueMarche_English') else 'fr'
     if lang!=original_language:continue
    package=r['package'];scan=int(r['scan'])
    local=[x for q in prov[lang]['packages'] if q['package']==package for x in q['layout'] if int(x['scan'])==scan]
    specific=[x for x in local if 'empty' not in x['kind'].lower() and x['kind'] not in ('manuscript-page placement','textcircled glyph mode')]
    if specific:
     done='Source-local repairs '+', '.join(dict.fromkeys(x['id'] for x in specific))+'. '+ ' '.join(dict.fromkeys(x['reason'] for x in specific))
    elif 'footer' in str(r).lower() or ('grothendieck.umontpellier.fr' in r.get('source','')):
     done='Institutional footer omitted in every form; the independent manuscript-page marker is retained. See ARCHIVE_FOOTERS.tsv.'
    elif 'margin' in r.get('kind','').lower() or r.get('source','').startswith(r'\margin'):
     done='The note is measured against the three-line margin rule; the longer note is printed as a labelled, ruled, breakable text-block note at its source anchor. No scaling is applied.'
    else:
     done='Normal paragraph reflow with explicit source annotation groups and breakable marginal-note placement resolves this recorded box. The final full-book log and all-page ink audit verify the site; no scaling callback is used.'
    sourcepath=('fr/texts/'+package+'.tex') if lang=='fr' else ('en/packages/'+package+'_en.tex')
    fixrows.append(dict(reader=reader,language=lang,package=package,cote=r['cote'],scan=scan,source_path=sourcepath,source_line=r.get('source_line',''),id=basis.replace('.tsv','')+f'-{n:03d}',record_basis=basis,what_was_wrong=r.get('kind',r.get('what the pass did',''))+'; '+r.get('pt_too_wide',r.get('scale','')),what_was_done=done,old=r.get('source',r.get('line_text','')),new='See linked exact repair record and final-source scan.'))
 generated_path=D/'generated_heading_repairs.json'
 if generated_path.exists():
  generated=data('generated_heading_repairs.json')
  assert generated['status']=='INTEGRATED_SOURCE_INVENTORY'
  for dependency in generated['dependencies']:
   assert hashlib.sha256((ROOT/dependency['path']).read_bytes()).hexdigest()==dependency['sha256'],dependency
  fixrows.extend(generated['rows'])
 fields=['reader','language','package','cote','scan','source_path','source_line','id','record_basis','what_was_wrong','what_was_done','old','new','generator_path','generator_line','source_entry_ids','note_id','applicability']
 write_tsv(R/'TYPESETTING_FIXES.tsv',fields,fixrows);write_tsv(R/'MECHANICAL_FIXES.tsv',fields,mechanical)
 # Per-cote, per-form apparatus counts, including explicitly requested placement notes.
 lines=['# Apparatus counts','', 'Authorial variants are counted once at the effective change. Revisions wholly within a cancellation are preserved in that cancellation’s manuscript reading. No conjectural manuscript slip has been introduced. The one English glossary correction is an English-only variant.','', '| File | Cote | Deletion | Insertion | Glossary correction | Textual entries | Required layout notices | Residual doubt rows |','|---|---|---:|---:|---:|---:|---:|---:|']
 for name,(lang,form,title) in BOOKS.items():
  for cote in ('140-1','140-2','140-3','140-4'):
   es=[e for e in prov[lang]['entries'] if e['cote']==cote];co=collections.Counter(e['kind'] for e in es) if form==1 else collections.Counter()
   layoutnotes=sum(1 for p in prov[lang]['packages'] for x in p['layout'] if x.get('cote')==cote and x.get('kind') in ('landscape diagram','landscape layout','inline formula moved to display','inline formula displayed')) if form==1 else 0
   carries=sum(e['kind']=='deletion' and bool(e.get('doubts') or e.get('inherited_doubt')) for e in es) if form==2 else 0
   lines.append(f"| {name} | {cote} | {co['deletion']} | {co['insertion']} | {co['glossary consistency']} | {sum(co.values())} | {layoutnotes} | {carries} |")
 lines += ['', 'The three landscape placements and the one displayed running-text formula have the separately identified layout notices explicitly requested by the brief. They are typographic explanations, not new manuscript readings. Diplomatic and reading forms print no variant apparatus. The reading forms retain cancellation uncertainty fragments as an explicit exception to omission of the apparatus; these are the original doubt contents, not new commentary.']
 (R/'APPARATUS_COUNTS.md').write_text('\n'.join(lines)+'\n')
 summary={'typesetting_rows':len(fixrows),'mechanical_rows':len(mechanical),'historical_overfull_records':len(before),'historical_pass_records':len(passed),'changes_fr':len(changes['fr']),'changes_en':len(changes['en'])}
 (D/'record_assembly_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
