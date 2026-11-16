from pathlib import Path
import csv,hashlib,json
root=Path(__file__).resolve().parents[1]
workspace=root.parent
items=[(f'{p}.{i}',f'Task {p}.{i}') for p,n in [('A',12),('B',13),('C',8),('D',2)] for i in range(1,n+1)] + [(f'L.{i}',f'Lead {i}') for i in range(1,10)]
with (root/'FERMAT_SUCCESSOR_results.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['id','statement','status','where_proved','depends_on','answers (lead or task)','notes'])
 for i,t in items: w.writerow([i,t,'Open','','',t,'Research in progress; no completion claim.'])
(root/'FERMAT_SUCCESSOR_report.md').write_text('INCOMPLETE\n\n# Research record\n\n| Task or lead | Statement | State |\n|---|---|---|\n'+''.join(f'| {t} | {i} | Under examination; not settled. |\n' for i,t in items)+'\n## Session\n\nResearch started 2026-11-16 at approximately 00:49 UTC. The attached prompt and archive are the task inputs. All inherited mathematical claims require verification.\n\n## Corrections under examination\n\n- LM6 E.8: a cusp Tate parameter has a leading constant. The assertion that its Kummer class is divisible by the Fermat exponent requires correction.\n- The density issue described in LM6 D.6 concerns Porowski (2026), not Section 8 of the supplied October 6 local preprint.\n')
(root/'FERMAT_SUCCESSOR_references.bib').write_text('% Verified means opened during this run, not merely labelled verified in an inherited file.\n')
(root/'records'/'session.json').write_text(json.dumps({'start_utc':'2026-11-16T00:49:00Z','prompt_sha256':hashlib.sha256((workspace/'upload/PROMPT(20261116-005003).md').read_bytes()).hexdigest(),'archive_sha256':hashlib.sha256((workspace/'upload/FERMAT_SUCCESSOR_background.zip').read_bytes()).hexdigest()},indent=2)+'\n')
print('Created evolving report, statement register, bibliography and input identity record.')
