import sys,re
from pathlib import Path
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
old=Path('MPL_105_work/pages/MPL_105_105_scan021.tex').read_text()
arrays=re.findall(r'\\diagram\{\\begin\{array\}\{l\}.*?\\end\{array\}\}',old,re.S)
# Each visible glyph row of scan041 was checked against these typeset characters.
banner=arrays[1].splitlines()
banner[10]=banner[10].replace(r'DD\phantom{00000000}DD\phantom{00}00',r'DD\phantom{0000000}DD\phantom{000}00')
line=r'\texttt{****A\phantom{000}END\phantom{000}JOB\phantom{0}637\phantom{0}PREDONTA\phantom{000000000000000000000000}ROOM\phantom{000000}11.28.14\phantom{0}AM\phantom{0}22\phantom{0}APR\phantom{0}82\phantom{00}R6.PR1\phantom{0000}SYS\phantom{0}JES2\phantom{0}JOB\phantom{00}637\phantom{000}END\phantom{000}A****}'
s='\\scanpage{41}\n'+arrays[0]+'\n\n'+'\n'.join(banner)+'\n\n\\diagram{\\begin{array}{l}\n'+('\\\\\n'.join([line]*6))+'\n\\end{array}}\n\\mspage{40}\n'
e=[('diagram','printed upper banner','four slanted zeros'),('diagram','printed middle banner','PREDONTA')]+[('text',f'printed record row{i}','****A END JOB 637 PREDONTA ROOM 11.28.14 AM 22 APR 82') for i in range(1,7)]+[('text','bottom left','40')]
record_page(41,s,e,'reused_typed',notes='Job banner PREDONTA, six identical END records JOB637 dated22APR82 11.28.14AM. Four slanted zero glyphs and 12-row letter banner visually checked; D row10 is shortened relative to rows4-9. No additional header/footer text is visible.')
build_doubts()
