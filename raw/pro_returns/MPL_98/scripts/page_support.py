import json, pathlib, subprocess, sys
BASE=pathlib.Path(__file__).resolve().parents[1]
def save(scan,tex,elements,sheet_kind='text',doubts=None,abbreviations=None,notes_candidates=None):
    data=dict(scan=scan,tex=tex,elements=elements,sheet_kind=sheet_kind,doubts=doubts or [],abbreviations=abbreviations or [],notes_candidates=notes_candidates or [])
    subprocess.run([sys.executable,str(BASE/'scripts'/'record_page.py')],input=json.dumps(data,ensure_ascii=False),text=True,check=True)
