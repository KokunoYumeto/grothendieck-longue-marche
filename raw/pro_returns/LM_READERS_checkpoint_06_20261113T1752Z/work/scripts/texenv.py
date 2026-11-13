"""Build environment; a complete TeX Live needs no local restoration."""
from pathlib import Path
from functools import lru_cache
import os, subprocess
RUNTIME=Path(__file__).resolve().parents[1]/'runtime'

@lru_cache(maxsize=1)
def system_texmf_trees():
    """Discover installed trees without copying machine-specific paths."""
    trees=[]
    for variable in ('TEXMFDEBIAN','TEXMFDIST','TEXMFMAIN'):
        result=subprocess.run(['kpsewhich','-var-value='+variable],capture_output=True,text=True)
        value=result.stdout.strip()
        if value and value not in trees:trees.append(value)
    return trees

def environment(force=False):
    env=os.environ.copy()
    env['SOURCE_DATE_EPOCH']='1794528000'
    env['FORCE_SOURCE_DATE']='1'
    if force or (RUNTIME/'formats/lualatex.fmt').exists():
        env['TEXMF']='{'+','.join([str(RUNTIME/'texmf'),*system_texmf_trees()])+'}'
        env['TEXMFVAR']=str(RUNTIME/'var');env['TEXMFCONFIG']=str(RUNTIME/'config');env['TEXMFCACHE']=str(RUNTIME/'cache')
        env['TEXFORMATS']=str(RUNTIME/'formats')+'//:'
        env['TEXMFOUTPUT']=str(RUNTIME/'cache')
    env['max_print_line']='2000';env['error_line']='254';env['half_error_line']='120'
    return env
