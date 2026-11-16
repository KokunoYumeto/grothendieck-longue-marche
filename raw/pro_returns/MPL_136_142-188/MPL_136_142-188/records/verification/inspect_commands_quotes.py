"""Mechanical command/quote inventory of an immutable compilation snapshot."""
from pathlib import Path
import re,csv,json,collections,argparse
from tex_macro_extract import mask_comments,argument_span,extract_file,TRACKED,escaped
EDITORIAL={'cotefile','scanpage','mspage','deleted','inserted','margin','uline','uuline','diagram','figure','unsure','illegible'}
DEFINITION_COMMANDS={'def','gdef','edef','xdef','newcommand','renewcommand','providecommand','DeclareRobustCommand','usepackage','documentclass'}
OTHER_STATE_COMMANDS={'cancel','bcancel','xcancel','sout','st','hl','strikeout','overstrike','unclear','uncertain','added','removed','addition','deletion','marginnote','msline','annotation'}
QUOTE_COMMANDS={'textquotedbl','textquotedblleft','textquotedblright','textquoteleft','textquoteright','guillemotleft','guillemotright','og','fg'}
TABLES={'array','tikzcd','matrix','pmatrix','bmatrix','Bmatrix','vmatrix','Vmatrix','smallmatrix','tabular','tabular*'}

def bracket_span(s,pos):
 while pos<len(s) and s[pos].isspace():pos+=1
 if pos>=len(s) or s[pos]!='[':return None
 start=pos;braces=0;brackets=1;pos+=1
 while pos<len(s):
  if not escaped(s,pos):
   if s[pos]=='{':braces+=1
   elif s[pos]=='}':braces-=1
   elif not braces and s[pos]=='[':brackets+=1
   elif not braces and s[pos]==']':
    brackets-=1
    if not brackets:return start,pos
  pos+=1
 return None

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--compile-run',type=Path)
 args=p.parse_args();base=Path(__file__).resolve().parent
 run=args.compile_run or Path((base/'latest_compile_run.txt').read_text().strip())
 snapshots=json.loads((run/'snapshots.json').read_text())
 commands=[];quotes=[];flags=[];malformed_envs=[]
 for item in snapshots:
  path=Path(item['snapshot_path']);raw=path.read_text();s=mask_comments(raw)
  scan=int(re.search(r'scan(\d+)\.tex$',item['page'])[1])
  records,_=extract_file(path);envstack=[];envranges=[];options=[]
  tokens=list(re.finditer(r'\\([A-Za-z@]+|.)',s))
  for token in tokens:
   name=token[1];line=s.count('\n',0,token.start())+1
   commands.append({'scan':scan,'page':item['page'],'line':line,'command':'\\'+name})
   if name in DEFINITION_COMMANDS or name in OTHER_STATE_COMMANDS:
    flags.append({'scan':scan,'line':line,'command':'\\'+name})
   if name in {'begin','end'}:
    span=argument_span(s,token.end())
    if span:
     env=s[span[0]+1:span[1]]
     if name=='begin':envstack.append((env,token.start()))
     elif envstack and envstack[-1][0]==env:
      en,start=envstack.pop();envranges.append((en,start,span[1]+1))
     else:malformed_envs.append({'scan':scan,'line':line,'issue':'unmatched environment boundary'})
   if name in {'arrow','ar'}:
    span=bracket_span(s,token.end())
    if span:options.append(span)
  quote_tokens=[]
  for token in tokens:
   if token[1] in QUOTE_COMMANDS:quote_tokens.append((token.start(),token.end(),'command','\\'+token[1]))
  for token in re.finditer(r'`{2,}|\x27{2,}|["“”„‟«»]',s):
   # Escaped literal quotes are already visible as control symbols in commands.
   if not escaped(s,token.start()):quote_tokens.append((token.start(),token.end(),'literal',raw[token.start():token.end()]))
  for start,end,typ,form in sorted(quote_tokens):
   line=s.count('\n',0,start)+1
   envs=[en for en,a,b in sorted(envranges,key=lambda x:x[1]) if a<=start<b]
   containers=[m['macro'] for m in records if m['start']<start<m['end']]
   inside_options=any(a<=start<=b for a,b in options)
   if inside_options:classification='tikz_arrow_option_syntax'
   elif any(en in TABLES for en in envs):classification='inside_table_or_diagram_environment'
   else:classification='outside_table_and_arrow_options'
   a=raw.rfind('\n',0,start)+1;b=raw.find('\n',end)
   if b<0:b=len(raw)
   quotes.append({'scan':scan,'page':item['page'],'line':line,'form_type':typ,'exact_form':form,'classification':classification,'environments':';'.join(envs),'wrappers':';'.join(containers),'source_line':raw[a:b]})
 def save(name,rows,fields):
  with (run/name).open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 save('command_occurrences.csv',commands,['scan','page','line','command'])
 save('quote_occurrences.csv',quotes,['scan','page','line','form_type','exact_form','classification','environments','wrappers','source_line'])
 counts=collections.Counter(r['command'] for r in commands)
 save('command_counts.csv',[{'command':c,'count':n,'editorial':c[1:] in EDITORIAL} for c,n in sorted(counts.items())],['command','count','editorial'])
 editorial={m:counts['\\'+m] for m in sorted(EDITORIAL)}
 quote_counts=collections.Counter((r['exact_form'],r['classification']) for r in quotes)
 textquotedbl=[r for r in quotes if r['exact_form']=='\\textquotedbl']
 outside=[r for r in textquotedbl if r['classification']=='outside_table_and_arrow_options']
 summary={'snapshot_run':str(run),'pages':len(snapshots),'distinct_control_sequences':len(counts),'editorial_counts':editorial,'other_state_or_definition_commands':flags,'environment_parse_issues':malformed_envs,'textquotedbl_occurrences':len(textquotedbl),'textquotedbl_outside_tables':len(outside),'quote_form_counts':[{'form':form,'classification':c,'count':n} for (form,c),n in sorted(quote_counts.items())]}
 (run/'commands_quotes_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
 lines=['# Mechanical command and quotation-form check','',f'Snapshot: `{run.name}`. All source hashes are in `compiled_sources.sha256`.','',f'Checked {len(snapshots)} page fragments; {len(counts)} distinct control sequences.','', '## Editorial commands','', '| Command | Count |','|---|---:|']
 for name,n in editorial.items():lines.append(f'| `\\{name}` | {n} |')
 lines+=['',f'Other candidate state-marking or definition commands flagged: {len(flags)}.','', '## Double-quote command occurrences','',f'`\\textquotedbl`: {len(textquotedbl)} occurrences; {len(outside)} outside table/diagram environments and arrow options. Classification is syntactic and does not identify manuscript intent.','']
 for r in textquotedbl:
  lines += [f"Scan {r['scan']}, TeX line {r['line']}; {r['classification']}; environments `{r['environments']}`:",'','```latex',r['source_line'],'```','']
 lines+=['## Exact quote forms','', '| Form | Syntactic context | Count |','|---|---|---:|']
 for (form,c),n in sorted(quote_counts.items()):lines.append(f'| `{form}` | {c} | {n} |')
 lines+=['','Every occurrence, including source lines, is retained in `quote_occurrences.csv`. Literal double quotes in TikZ arrow options are recorded separately from other source positions. No visual judgment about quotation marks was made.','']
 (run/'commands_quotes_report.md').write_text('\n'.join(lines))
 (base/'latest_commands_quotes_report.txt').write_text(str(run/'commands_quotes_report.md')+'\n')
 print(json.dumps({k:v for k,v in summary.items() if k!='quote_form_counts'},ensure_ascii=False,indent=2))
 print('Exact quote-form counts:')
 for (form,c),n in sorted(quote_counts.items()):print(repr(form),c,n)

if __name__=='__main__':main()
