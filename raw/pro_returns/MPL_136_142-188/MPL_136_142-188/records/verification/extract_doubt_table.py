#!/usr/bin/env python3
"""Losslessly extract every balanced unsure/illegible macro; optionally render a draft table.

Default outputs stay in verification. No transcription or final doubts file is modified.
Confidence is supplied by the visual reader, never inferred from source syntax.
"""
from pathlib import Path
import argparse,csv,json,hashlib,html,collections
from tex_macro_extract import extract_file,top_level_pipes

def cell(value):
    # Entities protect table separators while retaining the displayed characters.
    # The JSON and CSV keep the exact unescaped source strings as the authority.
    return '<code>'+html.escape(str(value),quote=False).replace('|','&#124;').replace('\n','&#10;')+'</code>'

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path('/workspace/scratch/fce80d805cc4/MPL_136_142-188'))
    p.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'doubt_extraction')
    p.add_argument('--confidence-map',type=Path,help='CSV with id,confidence; optional source_sha256 and split_pipes (yes/no)')
    p.add_argument('--markdown',type=Path,help='Optional draft-table output; omit to produce only lossless extraction files')
    args=p.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    assignments={}
    if args.confidence_map:
        with args.confidence_map.open(newline='',encoding='utf-8') as f:
            for row in csv.DictReader(f):
                if row['confidence'] not in {'high','medium','low',''}:
                    raise ValueError('Confidence must be high, medium, low, or blank')
                assignments[row['id']]=row
    rows=[];errors=[];counts=collections.Counter()
    for path in sorted((args.root/'pages').glob('*.tex')):
        macros,problems=extract_file(path);errors.extend(problems)
        digest=hashlib.sha256(path.read_bytes()).hexdigest()
        for m in macros:
            if m['macro'] not in {'unsure','illegible'}:continue
            counts[m['macro']]+=1
            offsets,parts=top_level_pipes(m['argument'])
            assignment=assignments.get(m['id'],{})
            if assignment.get('source_sha256') and assignment['source_sha256']!=digest:
                raise ValueError('Stale confidence assignment for '+m['id'])
            use_split=assignment.get('split_pipes','yes')!='no'
            if m['macro']=='illegible':
                reading=m['source'];alternatives='';review=False
            elif use_split:
                reading=parts[0];alternatives='|'.join(parts[1:]);review=bool(offsets) and not assignment.get('split_pipes')
            else:
                reading=m['argument'];alternatives='';review=False
            row={
                'id':m['id'],'file':m['cote'],'scan':m['scan'],'tex_line':m['line'],'tex_end_line':m['end_line'],
                'page_file':m['filename'],'macro':m['macro'],'raw_macro':m['source'],'raw_argument':m['argument'],
                'reading':reading,'alternatives':alternatives,'confidence':assignment.get('confidence',''),
                'top_level_pipe_offsets':offsets,'candidate_parts':parts,'pipe_review_required':review,
                'container_ids':m['container_ids'],'source_sha256':digest,
            }
            # This identity preserves even repeated or empty alternative segments.
            assert '|'.join(parts)==m['argument']
            rows.append(row)
    if errors:
        raise ValueError('Malformed tracked macros: '+json.dumps(errors))
    unknown=set(assignments)-{r['id'] for r in rows}
    if unknown:raise ValueError('Confidence IDs absent from current extraction: '+','.join(sorted(unknown)))
    (args.output_dir/'doubt_occurrences.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['id','file','scan','tex_line','tex_end_line','page_file','macro','raw_macro','raw_argument','reading','alternatives','confidence','top_level_pipe_offsets','candidate_parts','pipe_review_required','container_ids','source_sha256']
    csv_path=args.output_dir/'doubt_occurrences.csv'
    with csv_path.open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
        for row in rows:
            writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v for k,v in row.items()})
    with csv_path.open(newline='',encoding='utf-8') as f:
        reread=list(csv.DictReader(f))
    assert [r['raw_argument'] for r in reread]==[r['raw_argument'] for r in rows]
    assert [r['raw_macro'] for r in reread]==[r['raw_macro'] for r in rows]
    with (args.output_dir/'confidence_assignments_blank.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=['id','confidence','split_pipes','source_sha256']);writer.writeheader()
        for row in rows:
            writer.writerow({'id':row['id'],'confidence':row['confidence'],'split_pipes':'','source_sha256':row['source_sha256']})
    if args.markdown:
        lines=['# Doubt-table extraction draft','','Every occurrence is retained separately. Confidence blanks and literal-pipe candidates require the sole visual reader’s assignment. Exact original strings remain in the accompanying JSON/CSV. This is an extraction preview, not the final doubts file.','','| File | Scan page | TeX line | Reading | Alternatives | Confidence | Occurrence |','|---|---:|---|---|---|---|---|']
        for row in rows:
            line=str(row['tex_line'])+(('–'+str(row['tex_end_line'])) if row['tex_end_line']!=row['tex_line'] else '')
            lines.append('| '+' | '.join([row['file'],str(row['scan']),line,cell(row['reading']),cell(row['alternatives']),row['confidence'] or 'unassigned',row['id']])+' |')
        args.markdown.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    summary={'pages':len(list((args.root/'pages').glob('*.tex'))),'unsure':counts['unsure'],'illegible':counts['illegible'],'total':len(rows),'pipe_candidates':sum(bool(r['top_level_pipe_offsets']) for r in rows),'pipe_review_required':sum(r['pipe_review_required'] for r in rows),'confidence_unassigned':sum(not r['confidence'] for r in rows),'csv_roundtrip_exact':True}
    (args.output_dir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
