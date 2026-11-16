from pathlib import Path
import os,subprocess,json
base=Path(__file__).resolve().parents[2]/'work'/'primary'
env=os.environ.copy()
env['TEXMF']='{/usr/share/texlive/texmf-dist,/usr/share/texmf}'
commands=[['dvi2tty','-w','100',str(base/'kisin_author.dvi')],
          ['dvipdfmx','-q','-o',str(base/'kisin_author.pdf'),str(base/'kisin_author.dvi')]]
for command in commands:
 result=subprocess.run(command,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if command[0]=='dvi2tty':(base/'kisin_author.txt').write_text(result.stdout)
 print(json.dumps({'command':command,'returncode':result.returncode,'stderr':result.stderr[-3000:]}))
if (base/'kisin_author.pdf').exists():
 import fitz
 with fitz.open(base/'kisin_author.pdf') as document:
  document[1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(base/'kisin_author_p2.png')
 print('Rendered primary author manuscript page 2.')
