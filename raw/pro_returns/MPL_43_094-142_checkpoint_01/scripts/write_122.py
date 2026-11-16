from page_work import save_page
text=r'''\scanpage{122}
\begin{flushright}
Corps de classes\\
et dualité\\
des \uline{Courbes Algébriques}
\end{flushright}
\mspage{121}
'''
save_page(122,text,[('text','upper right title','Corps de classes et dualité des Courbes Algébriques'),('text','bottom left page number','121')],sheet_kind='cover',observations='Whole and both halves read. One three-line title at upper right; Courbes Algébriques alone underlined. No count or date visible. Lower half contains only the pencil page number.')
