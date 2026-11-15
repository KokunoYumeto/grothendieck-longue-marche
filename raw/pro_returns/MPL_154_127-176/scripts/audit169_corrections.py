from pathlib import Path
p=Path(__file__).resolve().parents[1]/'pages/MPL_154_127-176_154_scan169.tex'
s=p.read_text()
a=s.index(r'\diagram{\begin{tabular}')
b=s.index(r'\begin{flushleft}\ttfamily',a)
s=s[:a]+r'''\diagram{\begin{tabular}{|r|r|r|r|r|r|r|r|r|r|r|r|r|r|r|r|}\hline
\multicolumn{2}{|c|}{STEP}&\multicolumn{2}{c|}{TIME}&\multicolumn{12}{c|}{NUMBER OF EVENTS}\\\hline
NO&CORE&TIO&TCPU&\unsure{3330}&\unsure{3330-1}&3340&3350&\unsure{2250}&\unsure{T/8-16}&\unsure{3400|3380}&SPOOL&\unsure{VIO}&\unsure{SYSIN}&SYSOUT&C.U\\\hline
1&84&18&16&\unsure{1}&3&0&0&0&0&\unsure{0}&\unsure{0|1}&\unsure{0}&\unsure{40}&\unsure{0001078|0001178}&170\\\hline
\multicolumn{2}{|c|}{TOTALS}&18&16&\unsure{1}&3&0&0&0&0&\unsure{0}&\unsure{0|1}&\unsure{0}&\unsure{40}&\unsure{0001078|0001178}&170\\\hline
\end{tabular}}
\diagram{\begin{tabular}{|r|l|l|r|r|r|r|r|r|r|r|r|r|r|r|r|r|}\hline
\multicolumn{4}{|c|}{STEP}&\multicolumn{4}{c|}{PAGING}&\multicolumn{2}{c|}{SWAP}&\multicolumn{2}{c|}{VIO}&\multicolumn{4}{c|}{CORE SETUP}&\unsure{TIME}\\\hline
NO&NAME&PGM&\unsure{C.C.U|T.C.U}&SRB&IN&OUT&N&P.OUT&P.IN&P.IN&P.OUT&TOP&OM&TU&TM&\unsure{ELAPS}\\\hline
1&C55BATCH&CRBATCH&170&\unsure{2}&\unsure{2}&0&0&0&0&0&0&\unsure{248|240}&0&0&0&5\\\hline
\multicolumn{3}{|c|}{TOTALS}&400&2&2&0&0&0&0&0&0&\unsure{248|240}&0&0&0&5\\\hline
\end{tabular}}
'''+s[b:]
s=s.replace(r'\unsure{VS2.03.8}',r'\unsure{VS2.03.8G|VS2.03.86}')
s=s.replace(r'\unsure{0.1}',r'\unsure{0,1|0.1}')
s=s.replace('SYSOUT = 018000 XCP',r'SYSOUT = \unsure{0180000} XCP')
s=s.replace(r'\unsure{000178}',r'\unsure{0001078|0001178}')
s=s.replace(r'\margin{168}',r'\margin{\mspage{168}}')
lines=s.splitlines()
selected=[]
for line in lines:
 if (line.startswith(r'\draw[p] plot[smooth cycle] coordinates {(20.99,8.08)') or line.startswith(r'\draw[r] plot[smooth] coordinates {(20.98,8.19)') or line.startswith(r'\draw[r] plot[smooth] coordinates {(21.55,8.18)')):
  selected.append(line)
assert len(selected)==3
block='\\deleted{\\begin{scope}\n'+'\n'.join(selected)+'\n\\end{scope}}'
s=s.replace(selected[0],block)
for line in selected[1:]:
 # Remove the later duplicate, keeping the copy within the new scope.
 pos=s.rfind(line);s=s[:pos]+s[pos+len(line):]
p.write_text(s)
