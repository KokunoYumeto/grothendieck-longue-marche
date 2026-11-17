from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit import audited,doubt
p=Path(__file__).resolve().parents[1]/'pages/MPL_108+112+113+114+115_115_scan003.tex'
s=p.read_text().replace(r'\underset{\wedge}{b^\circ}',r'\underset{\wedge}{b}')
start=s.index(r'\diagram{\begin{tikzcd}[column sep=small,row sep=large]')
end=s.index(r'\end{tikzcd}}',start)+len(r'\end{tikzcd}}')
s=s[:start]+r'''\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&&{}&&&&{}\\
{}&\deleted{\widehat A^\circ-\widehat B}\arrow[ddl,no head]\arrow[dr,no head]
&&\deleted{\widehat B^\circ-\widehat A}\arrow[dl,no head]\arrow[drrr,no head]&{}&&\\
&&\deleted{\widehat A,\widehat B}\arrow[uu,no head]\arrow[dll,no head,"\deleted{\widehat A}"']
\arrow[rrrr,no head,"\deleted{\widehat B}"]&&&&\deleted{A^\vee,\widehat B}\arrow[uu,no head]\arrow[dll,no head,"\deleted{A^\vee}"]\\
\deleted{\widehat A,B^\vee}\arrow[uu,no head]\arrow[rrrr,no head,"\deleted{B^\vee}"']&&&&\deleted{A^\vee,B^\vee}\arrow[uu,no head]&&
\end{tikzcd}}'''+s[end:]
s=s.replace(r'\arrow[uuu,bend left=10]',r'\arrow[uu,bend left=10]').replace(r'\arrow[uuu,bend right=20]',r'\arrow[uu,bend right=20]')
p.write_text(s)
doubt(115,3,'pencil prism','six labelled vertices, four vertical headless stubs','faint lines now retained separately from apex connections','medium')
audited(115,3,'Both orientations, halves and enlarged prism/wheel re-read. Corrected phantom circle on b in live H_B formula; rebuilt prism endpoint geometry and restored four vertical stubs; wheel side arrows now meet upper corner objects. Printed 29-line listing rechecked.')
