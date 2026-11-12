import sys, runpy
sys.dont_write_bytecode = True
code_dir, script = sys.argv[1], sys.argv[2]
sys.path.append(code_dir)
sys.argv = [script] + sys.argv[3:]
runpy.run_path(script, run_name="__main__")
