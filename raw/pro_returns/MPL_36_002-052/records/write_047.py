from save_page import save
tex=r'''
\scanpage{47}
\begin{flushright}biextensions de\\faisceaux de groupes\end{flushright}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\fill (6,0) circle (.045);\end{tikzpicture}}
\margin{46}
'''
e=[('text','upper right, two lines','biextensions de faisceaux de groupes'),('drawing','upper middle-right','isolated filled dot'),('margin note','bottom left','46')]
save(47,tex,e,[], 'Title/cover “biextensions de faisceaux de groupes”; no written page count. A single isolated ink dot is retained without assigning it mathematical meaning.',sheet_kind='cover')
