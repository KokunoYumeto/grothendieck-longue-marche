"""Assemble the human-readable apparatus from adjudicated page records.

This script never reads images and makes no reading decisions.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv,json,re,hashlib,difflib,argparse,html

W=Path(__file__).resolve().parents[1]
P='SP49_CW_109'

def md(v):
    if v is None:return '— (no H text)'
    return str(v).replace('|','&#124;').replace('\n','<br>')

def literal(v):
    if v is None:return md(v)
    return '<code>'+html.escape(str(v)).replace('|','&#124;').replace('\n','</code><br><code>')+'</code>'

def write_tsv(path,fields,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore')
        writer.writeheader();writer.writerows(rows)

def build():
    records=[json.loads(p.read_text()) for p in sorted((W/'records').glob('scan*.json'))]
    stats=[];coll=[];inv=[];events=[];notes=['# Notes while reading\n\nThese notes concern only the supplied pages. Textual observations are reports of the ink, not independent verification of the author’s mathematical claims. Actual mathematical checks are distinguished in CHECK_EVENTS.tsv. No outside sources were consulted.\n']; sections=[]; doubts=[];abbr=[];consequential=[]
    for rec in records:
        n=rec['scan'];changes=rec['decisions'];status=rec['hua_has']
        s={'scan':f'{n:03}','C':0,'H':0}
        for k in ['C','H']:
            for conf in ['high','medium','low']:s[k+'_'+conf]=0
        sec=[f'## Scan {n:03}\n',f"Three independent readers: {', '.join(rec['readers'])}. Brief: {rec['brief']}. H: {status}.\n"]
        sec+=['| Place | Witness C | Witness H | Final reading | Readers A / B / C | Scan evidence and crop | Confidence |','| --- | --- | --- | --- | --- | --- | --- |']
        for d in changes:
            if d.get('diff_c'):
                s['C']+=1;s['C_'+d['confidence']]+=1
            if d.get('diff_h'):
                assert status=='text',f'H rows forbidden for scan {n}'
                s['H']+=1;s['H_'+d['confidence']]+=1
                coll.append({'folder':rec['folder'],'their_page':n-1,'our_scan':n,'line':d['place'],'their_reading':d.get('h',''),'codex_reading':d['c'],'final_reading':d['final'],'scan_shows':d['evidence']+'; '+', '.join(d.get('crops',[])),'kind':d['kind'],'marked_in_H':'yes' if d.get('marked_in_H') else 'no','confidence':d['confidence']})
            readers=d.get('readers',{})
            rr='; '.join(k+': '+str(readers.get(k,'see full reading')) for k in 'ABC')
            evidence=d['evidence']+(' Crops: '+', '.join(d['crops']) if d.get('crops') else '')
            sec.append('| '+' | '.join([md(d['place']),literal(d['c']),literal(d.get('h')),literal(d['final']),md(rr),md(evidence),d['confidence']])+' |')
            if d.get('consequential'):consequential.append(f"- Scan {n:03}, {d['place']}: {d['consequential']}")
        if not changes:sec.append('| No reading changes | — | — | — | Agreement | The three page readings confirmed the witnesses where present. | — |')
        sec.append('\n### Decisions on witness C doubt marks\n')
        sec+=['| Place | C mark | Decision | Evidence |','| --- | --- | --- | --- |']
        for d in rec.get('c_doubts',[]):sec.append('| '+' | '.join(md(d.get(k,'')) for k in ['place','c','decision','evidence'])+' |')
        if not rec.get('c_doubts'):sec.append('| None on this page | — | — | — |')
        sec.append('\n### Still unresolved\n')
        if rec.get('doubts'):
            for d in rec['doubts']:
                sec.append(f"- {md(d['place'])}: {literal(d['reading'])}; alternatives: {md(d.get('alternatives','none further'))}; {d['confidence']}. {md(d.get('reason',''))}")
                doubts.append({'scan':n,**d})
        else:sec.append('None.\n')
        if rec.get('equivalences'):
            sec.append('\n### Equivalent encodings excluded from counts\n')
            sec.extend('- '+x for x in rec['equivalences'])
        sec.append('\nCoverage: '+rec.get('coverage','See the retained reader reports.'))
        sections.append('\n'.join(sec))
        stats.append(s)
        inv.extend({'scan':n,**x} for x in rec['inventory'])
        notes.append(f'## Scan {n:03}\n')
        notes.extend(f"- [N{n:03}.{i}] {s}" for i,s in enumerate(rec['notes'],1))
        notes.append('')
        abbr.extend({'scan':n,**x} for x in rec.get('abbreviations',[]))
        events.extend(rec.get('check_events',[]))
    total={k:sum(s[k] for s in stats) for k in ['C','H','C_high','C_medium','C_low','H_high','H_medium','H_low']}
    count=['| Scan | Changes vs C | C high / medium / low | Changes vs H | H high / medium / low |','| --- | ---: | --- | ---: | --- |']
    for s in stats:count.append(f"| {s['scan']} | {s['C']} | {s['C_high']} / {s['C_medium']} / {s['C_low']} | {s['H']} | {s['H_high']} / {s['H_medium']} / {s['H_low']} |")
    s=total;count.append(f"| **Total** | **{s['C']}** | {s['C_high']} / {s['C_medium']} / {s['C_low']} | **{s['H']}** | {s['H_high']} / {s['H_medium']} / {s['H_low']} |")
    intro='# Consolidated transcription: changes and decisions\n\nCounts refer to meaningful reading loci, including removed or revised doubt marks, and exclude macro-syntax equivalence. A shared locus can count against both witnesses. Retained C doubts do not count as changes. A decision row may also record a rejected reader proposal while retaining both witnesses; such rows contribute zero to the change counts. H description-only pages have no collation rows. The three reader columns preserve competing readings, including when the final adjudication retains a doubt.\n\n'+'\n'.join(count)+'\n\n## Consequential corrections affecting mathematics\n\n'+('\n'.join(consequential) if consequential else 'None recorded in the completed pages so far.')+'\n\n'
    (W/f'{P}_changes.md').write_text(intro+'\n\n'.join(sections)+'\n')
    write_tsv(W/f'{P}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
    with (W/f'{P}_inventory.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],extrasaction='ignore');writer.writeheader();writer.writerows(inv)
    (W/f'{P}_notes.md').write_text('\n'.join(notes)+'\n')
    doubttext=(W/'notation.md').read_text()+'\n## Remaining doubts\n\n| Scan | Place | Reading | Alternatives | Confidence | Evidence |\n| --- | --- | --- | --- | --- | --- |\n'
    for d in doubts:doubttext+='| '+' | '.join(md(d.get(k,'')) for k in ['scan','place','reading','alternatives','confidence','reason'])+' |\n'
    doubttext+='\n## Abbreviations encountered\n\nExpansions here are interpretations only; they never replace the written abbreviations.\n\n| Form | Likely expansion or sense | Scan and place |\n| --- | --- | --- |\n'
    grouped={}
    for a in abbr:
        key=(a['form'],a['expansion']);grouped.setdefault(key,[]).append(f"{a['scan']:03}: {a.get('place','')}")
    for (form,expansion),loc in grouped.items():doubttext+='| '+' | '.join(md(s) for s in [form,expansion,'; '.join(loc)])+' |\n'
    legibility=W/'records/legibility.md'
    doubttext+='\n## Legibility and comparison of witnesses\n\n'+(legibility.read_text() if legibility.exists() else 'Review in progress. The page-specific remaining doubts above identify the least certain readings.')+'\n'
    (W/f'{P}_doubts.md').write_text(doubttext)
    write_tsv(W/'CHECK_EVENTS.tsv',['statement_id','date','who_model_effort_run','type','outcome'],events)
    if records:
        texts=[]
        for r in records:
            text=(W/'pages'/r['filename']).read_text()
            text=re.sub(r'\\cotefile\{109\}\s*','',text)
            texts.append(text.rstrip()+'\n')
        (W/f'{P}_transcription.tex').write_text('\\cotefile{109}\n'+'\n'.join(texts))
    diff=[]
    for r in records:
        c=(W/'inputs'/f"{r['scan']:03}"/'C.tex').read_text().splitlines(keepends=True)
        final=(W/'pages'/r['filename']).read_text().splitlines(keepends=True)
        diff.extend(difflib.unified_diff(c,final,fromfile='witness_C/'+r['filename'],tofile='pages/'+r['filename']))
    (W/'records/witness_C_unified.diff').write_text(''.join(diff))
    (W/'records/counts.json').write_text(json.dumps({'pages':stats,'total':total,'completed':len(records),'inventory_elements':len(inv),'remaining_doubts':len(doubts),'H_rows':len(coll)},indent=2))
    readme=f'''# SP49_CW_109 — second diplomatic pass

Status at this build: {len(records)} of 27 supplied scan pages adjudicated. Completed scans: {', '.join(f"{r['scan']:03}" for r in records)}.

## Deliverables

- pages/: one final LaTeX fragment per completed scan, using the supplied filenames.
- SP49_CW_109_transcription.tex: concatenated fragments with one cote marker and no preamble.
- PREAMBLE.tex: the unchanged supplied macro definitions.
- SP49_CW_109_changes.md: decisions, C/H comparisons, reader alternatives, crop evidence and confidence counts.
- SP49_CW_109_collation.tsv: only substantive differences from H where H has actual transcribed text (scans 009–011).
- SP49_CW_109_doubts.md: the cumulative notation table, unresolved readings, abbreviation interpretations and legibility assessment.
- SP49_CW_109_inventory.csv: complete element inventory for adjudicated pages.
- SP49_CW_109_notes.md and CHECK_EVENTS.tsv: page content and actual mathematical checks, with limits and provenance.
- progress.log: start, sequential page completion, checkpoint receipts, and eventual freeze/recheck hashes.
- SP49_CW_109_workflow.md and briefs/: reader instructions, revisions and crop accounting.
- readers/, crops/, records/, scripts/: original independent returns, visual evidence, structured main-reader decisions and reproducible assembly/checking scripts.

## Reading method and limits

Three fresh independent readers examine each page, in supplied scan order. Each sees the whole and both supplied halves once, then a tight crop for each place still open. The main reader compares the full returns and adjudicates disagreements on crops. Models: GPT-6 Astra Pro for the main reader and subagents; reasoning effort is not exposed and is not inferred. No OCR, PDF text recognition, outside transcription or web research is used. No human verification is claimed.

Current counts: {total['C']} changed C loci, {total['H']} H collation loci, {len(doubts)} unresolved readings, {len(inv)} inventoried elements, {len(events)} mathematical check events. These are diplomatic comparison counts, not error-rate estimates: they include literal quote shapes and revised uncertainty marks. H has only descriptions for the other 24 scans.

## Restoring a checkpoint

The archive contains all work documentation written at its creation, but excludes the original attachments, scans, witnesses, derived convenience input copies and older checkpoint ZIPs. Restore its contents under a work/ directory and make the supplied source folders available in the sibling source/ directory. scripts/setup.py can recreate the excluded inputs from those attached sources without replacing existing progress, notation or mathematical events. It finishes with the corrected header-aware context extractor and restores each archived notation snapshot. Retain the supplied same-page clarification/addendum documents; their rationale is recorded in the workflow. Use state.json and progress.log to identify the next scan and the brief actually in force; archived notation snapshots preserve what each completed reader received. A checkpoint may include unfinished reader work for the current page. Do not mark that page complete until all three returns and main adjudication are finished.

scripts/build.py assembles apparatus from records/scanNNN.json. scripts/validate.py performs static LaTeX balance and completeness checks, without compilation. scripts/commit_page.py enforces page order. scripts/freeze.py requires all 27 pages and a documented notation audit before hashing; its check mode verifies the frozen files. Checkpoints are prepared only when the 45-minute interval is due, and a save receipt is acknowledged only after persistence succeeds. Older checkpoint ZIPs are never overwritten or nested.
'''
    (W/'README.md').write_text(readme)
    print(json.dumps({'completed':len(records),'changes':total,'inventory_elements':len(inv),'remaining_doubts':len(doubts),'H_rows':len(coll)}))

if __name__=='__main__':build()
