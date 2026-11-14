"""Record the actual mathematical, TeX and PDF-verification runtimes."""
from pathlib import Path
import json
import subprocess
import sys
import sympy
import numpy
import fitz
import PIL

def version(command):
    result=subprocess.run(command,text=True,capture_output=True,check=False)
    lines=(result.stdout+'\n'+result.stderr).strip().splitlines()
    return lines[0] if lines else f'exit {result.returncode}'

data={'python':sys.version,'sympy':sympy.__version__,'numpy':numpy.__version__,
      'PyMuPDF':fitz.VersionBind,'Pillow':PIL.__version__,
      'g++':version(['g++','--version']),
      'luahbtex':version(['luahbtex','--version']),
      'bibtex':version(['bibtex','--version']),
      'pdftoppm':version(['pdftoppm','-v'])}
text=json.dumps(data,indent=2)+'\n'
Path(__file__).with_name('runtime_versions.json').write_text(text)
print(text,end='')
