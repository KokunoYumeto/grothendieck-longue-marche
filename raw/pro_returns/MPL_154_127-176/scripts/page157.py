from pathlib import Path
from tikz import *
from commit_page import commit

def _mpl157_public_node_hooks(_mpl157_tex):
    """Apply the authorized public node-hook insertion to the known scan 157 output."""
    import hashlib as _mpl157_hashlib
    _mpl157_data = _mpl157_tex.encode('utf-8')
    _mpl157_digest = _mpl157_hashlib.sha256(_mpl157_data).hexdigest()
    if _mpl157_digest == '0c51f80e68cabc1f9f6f70a192d545517e3fa9c892772716d85f233f3987bcfb':
        return _mpl157_tex
    if _mpl157_digest != '275e6e1004a9b02b467d2467f59b398141455bae76ff390643e5a8cdd0d659c5':
        raise RuntimeError('Unexpected scan 157 output; review the explicit node-hook repair guard.')
    _mpl157_lines = _mpl157_data.splitlines(keepends=True)
    _mpl157_needle = b'\\begin{tikzpicture}['
    _mpl157_insert = b'execute at begin node={\\ifmmode$\\fi},execute at end node={\\ifmmode$\\fi},'
    for _mpl157_line in (141, 151, 173):
        if _mpl157_lines[_mpl157_line - 1].count(_mpl157_needle) != 1:
            raise RuntimeError('Expected nested picture opening was not found exactly once.')
        _mpl157_lines[_mpl157_line - 1] = _mpl157_lines[_mpl157_line - 1].replace(_mpl157_needle, _mpl157_needle + _mpl157_insert, 1)
    _mpl157_fixed = b''.join(_mpl157_lines)
    if _mpl157_hashlib.sha256(_mpl157_fixed).hexdigest() != '0c51f80e68cabc1f9f6f70a192d545517e3fa9c892772716d85f233f3987bcfb':
        raise RuntimeError('Node-hook repair differs from the approved tested bytes.')
    return _mpl157_fixed.decode('utf-8')

root=Path(__file__).resolve().parents[1]
def cross(x,y,up=.8,down=.9,width=.27):
 return paths('orange!85!red,line width=3.5pt',f'{x-width},{y-up} {x},{y} {x+width},{y+down};{x+width},{y-up} {x},{y} {x-width},{y+down}')
def tiny(up=True,left=True):
 t=start()+path('g,dashed','0,0 2.35,0')+path('g',f'0,{-.55 if not up else .55} 1.65,{-.55 if not up else .55}')+cross(1,0,.9,.9,.3)
 t+=path('g,->,line width=2.3pt',f'1.92,{.3 if up else -.3} 1.92,{-.65 if up else .65}')
 t+=path('g,->,line width=2.3pt',f'{2.7 if left else 2.15},.32 {2.05 if left else 2.8},.32')
 if left:t+=labels([('2.6,.67',r'-\omega^*')])
 return t+end()
def pairreverse():
 t=start()+path('g','0,0 3.9,0')+cross(.5,-.25,.5,.85,.27)+cross(2.8,-.8,.4,1.4,.33)+path('g,<-,line width=2.5pt','.89,.1 1.48,.1')+labels([('1.2,.5',r'-\omega^*'),('3.3,-.4','T'),('4.4,0',r'\sim')])
 t+=path('g','5.2,-.2 9.25,-.2')+cross(5.95,0,.8,.7,.3)+cross(8.15,-.85,.4,1.5,.32)+path('g,<-,line width=2.5pt','6.2,-.42 6.82,-.42')+labels([('6.6,.15',r'-\omega^*'),('8.65,-.6','T')])
 t+=path('p','-.35,-1.1 -.52,0 -.35,.8')+path('p','9.65,-1.1 9.84,-.15 9.65,.8')
 return t+end()
s=r'''\scanpage{157}
{\ttfamily\unsure{DATA SETS PICTURE}}
\diagram{\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|l|}
\hline
\ttfamily DDNAME&\ttfamily DESTINATION&\ttfamily CLASS&\ttfamily COPIES&\ttfamily RECORD-NB&\ttfamily BYTES-NB&\ttfamily FORM&\ttfamily FCB&\ttfamily UCS&\ttfamily SPIN&\ttfamily HOLD&\\\hline
\ttfamily SYSMSG&\unsure{\ttfamily JES2}&\unsure{6}&A&1&104&\unsure{856}&\ttfamily STD.& & & &\\\hline
\end{tabular}}
\[
\begin{aligned}
\rho_s&=\sigma_2\sigma_1\qquad\sigma_1\\
\rho_f&=\sigma_1\sigma_0\qquad\sigma_1=\rho_f\sigma_0\\
\rho_s\rho_f&=\sigma
\end{aligned}
\]
'''
s+=start()
# Two alternatives of a solid oriented passage (upper left).
s+=path('g','7.97,2.84 9.36,2.68 11.08,2.69')+cross(8.67,3.17,.95,.82,.36)+cross(10.32,2.08,.37,1.24,.27)+path('g,->','9.32,2.89 9.87,2.89')+labels([('10.69,2.28','T'),('12.15,2.65',r'\sim')])
s+=path('g','12.84,2.72 13.74,2.69 15.11,2.75')+cross(13.21,2.38,.58,1.12,.22)+cross(14.68,2.24,.42,1.3,.3)+path('g,->','13.67,2.99 14.08,3.06')+labels([('14.99,2.47','T')])
# Alternatives of a dashed passage (upper right).
s+=path('g,dashed','17.73,3.56 18.6,3.48 19.65,3.22 20.92,2.55')+cross(18.31,2.91,.65,1.01,.31)+cross(20.48,2.78,.56,.92,.29)+paths('g,->','20.82,2.37 20.82,1.97;20.83,2.77 21.31,2.57')+labels([('17.93,3.17','T'),('22.61,3.27',r'\sim')])
s+=path('g,dashed','23.98,3.16 24.97,3.18 26.23,3.31 27.93,3.13')+cross(24.39,2.63,.5,1.05,.31)+cross(26.29,3.34,1.13,.69,.44)+paths('g,->','26.99,3.06 27.79,3.02;26.99,3.52 27.02,3.92')+labels([('24.04,2.86','T')])
# Parenthesized pair with a triangle-free interval.
s+=paths('g','17.16,6.25 19.26,6.1 21.4,5.98;22.88,6.23 24.38,6.11 26.16,5.91')+paths('g,dashed','17.33,5.78 20.08,5.69;23.05,5.57 25.83,5.35')
s+=cross(18.03,5.73,.85,1.02,.3)+cross(19.61,5.08,.29,1.43,.31)+cross(23.48,5.58,.79,1.18,.36)+cross(25.56,6.69,1.77,.35,.44)
s+=paths('p','19.34,5.52 19.72,5.31;19.3,5.66 19.77,5.41;19.29,5.81 19.83,5.51;19.24,5.97 19.86,5.65;25.2,6.04 25.6,6.37;25.24,6.18 25.55,6.44;25.34,6.37 25.52,6.52')
s+=paths('g,->','20.17,5.94 20.73,5.94;26.06,5.76 26.65,5.7')+paths('k,<->','18.26,6.31 19.14,6.28;23.81,6.29 25.12,6.18')
s+=labels([('17.78,6.0','T'),('20.08,5.88',r"T'"),('23.15,5.94','T'),('26.03,6.23',r"T'"),('21.96,5.73',r'\sim'),('18.74,6.43',r'\unsure{l.p.r.}')])
s+=paths('p','17.14,4.98 16.83,6.29 17.35,7.23;27.58,4.81 27.76,6.05 27.32,7.24')
s+=paths('k','18.54,6.4 18.79,7.02 19.88,7.33;24.58,6.31 24.18,7.12 22.07,7.45')
s+=r'\node[align=center] at (21.16,7.69) {parcours\\ libre de\\ triangles};'+'\n'
s+=paths('k,->','12.54,10.13 14.08,7.63 14.57,5.34 13.4,4.34 12.28,4.07;12.4,10.79 14.37,8.96 16.83,6.48')+paths('k','12.46,10.04 12.61,10.15;12.34,10.69 12.47,10.8')+labels([('13.9,5.39',r'\rho_s'),('14.86,7.88',r'\rho_f')])
# Left black/pencil local orientation sketch.
s+=paths('p','1.37,8.67 2.99,8.29 4.23,8.21 5.98,7.14;3.33,7.79 4.23,8.21 6.31,9.17;2.12,8.01 2.27,9.5 2.49,11.17;2.27,9.5 2.99,8.29 3.27,8.86 4.07,10.07; .8,10.46 2.27,9.5 4.23,8.21')
s+=paths('k,->','2.45,9.37 4.17,8.25;4.07,10.07 2.99,8.31;3.5,9.43 3.0,8.69;3.8,8.85 4.29,8.48;3.62,8.93 3.6,8.65 3.34,8.59;4.19,9.95 4.09,9.74 3.71,9.78')
s+=paths('p','2.62,9.18 3.16,8.85;2.68,9.04 3.09,8.74;2.75,8.88 3.04,8.59')+labels([('6.64,6.9',r'\Delta_s'),('2.99,8.15',r"\sigma_{D'}"),('4.3,10.06',r'\sigma_D'),('4.27,9.6',r'\omega'),('3.14,9.64',r'\beta'),('4.09,8.86',r'\alpha')])
s+=r'\node[anchor=west] at (6.27,8.4) {$\alpha,\beta,\omega$ croisés};'+'\n'
# Large lower-left oriented crossing.
s+=path('g','1.26,13.29 3.59,12.98 6.59,12.62')+path('g,dashed','1.39,13.87 3.94,13.61 6.24,13.45')+path('g','1.37,14.45 3.77,14.2 6.47,13.96')+cross(3.9,13.65,1.76,2.17,.65)
s+=paths('g,->,line width=3pt','4.81,13.76 4.8,13.14;5.38,13.51 6.21,13.43')+paths('k,->','4.81,13.76 4.8,13.14;5.38,13.51 6.21,13.43;5.73,12.59 6.25,12.53;5.78,14.16 6.22,14.13;3.56,13.24 3.32,13.65 3.59,14.01')
s+=dots('w','5.73,12.59','.05')+labels([('6.74,13.36',r'D_0'),('6.63,14.02','D'),('7.15,12.54',r"D'"),('6.11,12.24',r'\omega^*'),('5.04,13.17',r'\beta^*'),('3.16,13.85',r'\alpha^*'),('4.06,13.72','s'),('3.95,14.46','T')])+end()
# Mathematical transformation arrows in tikz-cd; drawings are explicit node contents.
up=tiny(False,False);right=tiny(True,True);down=tiny(False,True);pair=pairreverse()
s+='\\diagram{\\begin{tikzcd}[ampersand replacement=\\&,row sep=2.5em,column sep=3em]\n'
s+='\\begin{gathered}'+up+r'\\(D_0,-\beta^*,\omega^*)\end{gathered} \& \\'+'\n'
s+='{} \\& \\begin{gathered}'+right+r'\\(D_0,\beta^*,-\omega^*)\end{gathered} \\'+'\n'
s+=r'(D_0,\beta^*\omega^*) \arrow[uu,"\sigma",mapsto] \arrow[ur,"\sigma_0",mapsto] \arrow[r,"\sigma_1",mapsto] \arrow[dr,"\sigma_2",mapsto] \& '+pair+r' \\'+'\n'
s+='\\& \\begin{gathered}'+down+r'\\(D_0,-\beta^*,-\omega^*)\end{gathered}'+'\n'+r'\end{tikzcd}}'+'\n'
s+=r'''
$\alpha^*,\beta^*,\omega^*$ \uline{non} croisés
\[
\omega^*=-\alpha^*\wedge\beta^*\qquad
\omega=\alpha\wedge\beta
\]
$\sigma_0$ donc change $\alpha$ en $-\alpha$, en gardant $\sigma_D,\sigma_{D'},\beta$.

$\sigma_2$ échange $\sigma_D$ et $\sigma_{D'}$, change $\beta$ en $-\beta$, garde $\alpha$.
\margin{156}
'''
(root/'pages/MPL_154_127-176_154_scan157.tex').write_text(_mpl157_public_node_hooks(s))
commit(157,[('text','faint reused printing upper band','DATA SETS PICTURE'),('diagram','faint printing upper band','DDNAME DESTINATION CLASS COPIES RECORD-NB BYTES-NB FORM FCB UCS SPIN HOLD; SYSMSG'),('display','upper left','rho_s=sigma2sigma1; rho_f=sigma1sigma0; rho_s rho_f=sigma'),('drawing','upper left pair','two equivalent solid green passages at orange crossings; T'),('drawing','upper right pair','dashed green passages and paired directions; T'),('drawing','upper right middle','parenthesized pair T,T-prime; intervals'),('text','right middle','parcours libre de triangles'),('drawing','centre','curved rho_s and oblique rho_f arrows'),('drawing','left middle','Delta_s, sigma_D, sigma_D-prime, alpha,beta,omega'),('text','beside left sketch','alpha,beta,omega croisés'),('drawing','lower left','D-prime,D0,D; alpha-star,beta-star,omega-star;s;T'),('diagram','central lower','D0 beta-star omega-star and four sigma transformations with drawing nodes'),('text','bottom left','alpha-star,beta-star,omega-star non croisés'),('display','bottom left','omega-star=-alpha-star wedge beta-star; omega=alpha wedge beta'),('text','bottom middle','sigma0 donc change alpha; sigma2 échange'),('margin note','bottom left','156')],sheet_kind='reused_typed',observations='Whole, both halves, enlarged prose and mirrored printed table inspected. All stars, minus signs and transformations copied from the ink. The base triple lacks a clearly visible comma between beta-star and omega-star and retains that spacing. Croisés/non croisés checked at enlargement. Central formal transformation graph is tikz-cd with actual TikZ drawing nodes, not prose stand-ins. Top printed table is exceptionally faint and overwritten; doubtful field readings marked. Separate rho arrows retain their unlabelled lower ends.')
