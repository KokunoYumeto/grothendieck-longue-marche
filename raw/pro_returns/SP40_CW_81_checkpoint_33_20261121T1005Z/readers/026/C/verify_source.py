"""Source-only reconstruction and delimiter audit. No compiler or renderer is called."""
from pathlib import Path
import json,re,hashlib

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[3]
raw=ROOT.joinpath('reading.tex').read_bytes()
text=raw.decode()
report=json.loads(ROOT.joinpath('report.json').read_text())
source_map=json.loads(ROOT.joinpath('source_map.json').read_text())
clean=re.sub(r'(?<!\\)%[^\n]*','',text)
balance=minimum=0
for i,ch in enumerate(clean):
    before=len(clean[:i])-len(clean[:i].rstrip('\\'))
    escaped=before%2==1
    if ch=='{' and not escaped:balance+=1
    if ch=='}' and not escaped:balance-=1;minimum=min(minimum,balance)
stack=[];environment_errors=[]
for match in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
    typ,environment=match.groups()
    if typ=='begin':stack.append(environment)
    elif not stack or stack.pop()!=environment:environment_errors.append(match.group())
source_errors=[];witness_errors=[];reference_errors=[]
groups={g['id'] for g in source_map['groups']}
for group in source_map['groups']:
    span=group['source_span'];fragment=raw[span['start_utf8_byte']:span['end_utf8_byte_exclusive']]
    if fragment.decode()!=group['source_exact']:source_errors.append(group['id'])
    if hashlib.sha256(fragment).hexdigest()!=group['source_sha256']:source_errors.append(group['id']+' hash')
for difference in report['differences']:
    if difference['readers_crop'] and not ROOT.joinpath(difference['readers_crop']).exists():reference_errors.append(difference['id']+' crop')
    for gid in difference.get('source_groups',[]):
        if gid not in groups:reference_errors.append(difference['id']+' '+gid)
    for name in ['C','H']:
        anchor=difference[name+'_anchor'];source=BASE.joinpath(anchor['file']).read_bytes()
        fragment=source[anchor['start_utf8_byte']:anchor['end_utf8_byte_exclusive']]
        if fragment.decode()!=difference[name] or fragment.decode()!=anchor['exact']:witness_errors.append(difference['id']+' '+name)
        if hashlib.sha256(fragment).hexdigest()!=anchor['sha256']:witness_errors.append(difference['id']+' '+name+' hash')
blank_math=[];inside=False
for i,line in enumerate(text.splitlines(),1):
    if r'\[' in line:inside=True
    if inside and not line.strip():blank_math.append(i)
    if r'\]' in line:inside=False
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
result={
 'scope':'Source-only administrative checks: no compilation, rendering, installation, image reopening, OCR, or mathematical proof/correspondence check.',
 'reading_tex_sha256':hashlib.sha256(raw).hexdigest(),
 'brace_balance':balance,'minimum_brace_depth':minimum,
 'environment_errors':environment_errors,'unclosed_environments':stack,
 'inline_dollar_count':len(re.findall(r'(?<!\\)\$',clean)),
 'display_open_count':clean.count(r'\['),'display_close_count':clean.count(r'\]'),
 'blank_physical_lines_in_display_math':blank_math,
 'source_span_errors':source_errors,'literal_witness_anchor_errors':witness_errors,'reference_errors':reference_errors,
 'unsupported_kind_values':sorted({x['kind'] for x in report['differences']}-allowed),
 'group_count':len(source_map['groups']),'sigma_occurrence_count':len(report['all_Sigma_occurrences']),
 'C_source_row_count':len(report['C_uncertainty_rows']),
 'C_source_row_ids':[x['id'] for x in report['C_uncertainty_rows']],
 'C_rows_without_local_record':[x['id'] for x in report['C_uncertainty_rows'] if not x['difference_ids']],
 'C_source_rows_resolved':sum(x['status']=='resolved' for x in report['C_uncertainty_rows']),
 'C_source_rows_retained':sum(x['status']=='retained' for x in report['C_uncertainty_rows']),
 'view_counts':report['provenance']['view_counts'],
 'differences_total':len(report['differences']),
 'proposed_diff_C_count':sum(x['diff_C'] for x in report['differences']),
 'proposed_diff_H_count':sum(x['diff_H'] for x in report['differences']),
 'literal_source_mark_counts_including_invisible_annotations':{x:len(re.findall(r'\\'+x+r'\{',clean)) for x in ['unsure','deleted','inserted','illegible']},
 'macros_seen':sorted(set(re.findall(r'\\([A-Za-z]+)',clean))),
 'recurring_ring_occurrence_count':len(report['recurring_ring_occurrences']),
 'ordinary_macros_only':not bool(re.search(r'\\(?:newcommand|renewcommand|def|gdef|let)\b',clean)),
 'note':'An even raw dollar count is a lexical delimiter check only. No visual, metric, rendered or compiler validation is claimed.'
}
result['passed']=not any([balance,minimum,environment_errors,stack,blank_math,source_errors,witness_errors,reference_errors,result['unsupported_kind_values'],result['C_rows_without_local_record']]) and result['inline_dollar_count']%2==0 and result['display_open_count']==result['display_close_count'] and result['ordinary_macros_only']
ROOT.joinpath('source_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['passed','reading_tex_sha256','group_count','sigma_occurrence_count','C_source_row_count','C_source_rows_resolved','C_source_rows_retained','differences_total','proposed_diff_C_count','proposed_diff_H_count','view_counts','literal_source_mark_counts_including_invisible_annotations']},ensure_ascii=False,indent=2))
