from pathlib import Path
import subprocess,json,copy,re,sys
run=Path(__file__).resolve().parent
original=run.parent/'code'
p=subprocess.run([sys.executable,str(run/'d_arithmetic_free_characters.py')],cwd=run,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
(run/'d_arithmetic_free_characters.out').write_text(p.stdout)
assert p.returncode==0,p.stdout
a=json.loads((original/'d_arithmetic_free_characters.json').read_text());b=json.loads((run/'d_arithmetic_free_characters.json').read_text())
ca=copy.deepcopy(a);cb=copy.deepcopy(b)
ca['summary'].pop('elapsed_seconds');cb['summary'].pop('elapsed_seconds')
assert ca==cb
clean=lambda text:re.sub(r'("elapsed_seconds": )[^,}\n]+',r'\1<TIME>',text)
assert clean((original/'d_arithmetic_free_characters.out').read_text())==clean(p.stdout)
result={'status':'PASS','fresh_program_exit_code':p.returncode,'complete_json_equal':True,'complete_stdout_equal':True,'excluded_paths':['/summary/elapsed_seconds'],'input_files':['d_arithmetic_correction_graph.json','d_arithmetic_affine_base.json'],'source':'Copied complete source and two exact immutable inputs; no other local mathematical dependency.'}
(run/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
