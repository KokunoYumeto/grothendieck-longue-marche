from editorial import *
import sys, re
scan=int(sys.argv[1]); m=MAP[scan]
print('WITNESS C\n'+(SOURCE/m['codex_file']).read_text())
print('\nC DOUBTS AND NOTATION ROWS FOR THIS SCAN')
for line in (SOURCE/'codex'/m['folder']/(m['folder']+'_doubts.md')).read_text().splitlines():
    if re.search(r'\b0*'+str(scan)+r'\b',line): print(line)
print('\nC NOTES FOR THIS SCAN')
for line in (SOURCE/'codex'/m['folder']/(m['folder']+'_notes.md')).read_text().splitlines():
    if re.search(r'\b0*'+str(scan)+r'\b',line): print(line)
h=(SOURCE/m['hua_file']).read_text()
parts=re.split(r'\\page\{(\d+)\}',h)
print('\nWITNESS H (coverage '+m['hua_has']+')')
for i in range(1,len(parts),2):
    if parts[i]==m['their_page']: print(parts[i+1].split('\\end{document}')[0])

