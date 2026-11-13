"""Run one shipped LM1 script in isolated mode (python -I).

-I keeps the script folder and the current folder off sys.path; the copied code
folder is appended (after the standard library and site-packages) only so that the
two local helper modules AB_core.py and D_finite.py, which were read beforehand,
can be imported by the scripts that need them.
"""
import os
import runpy
import sys

code_dir = os.path.abspath(sys.argv[1])
script = sys.argv[2]
sys.path.append(code_dir)
os.chdir(code_dir)
path = os.path.join(code_dir, script)
sys.argv = [path]
runpy.run_path(path, run_name="__main__")
