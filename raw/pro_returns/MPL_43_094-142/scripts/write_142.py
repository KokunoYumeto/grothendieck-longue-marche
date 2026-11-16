from page_work import save_page
text=r'''\scanpage{142}
\begin{flushright}
Dualité de Tate-\\
Cassels
\end{flushright}
\mspage{141}
'''
elements=[('text','top right','Dualité de Tate-Cassels'),('text','bottom left','141')]
save_page(142,text,elements,sheet_kind='cover',observations='Whole and both supplied halves inspected. Two-line title and manuscript sheet number only; no written page count.')
