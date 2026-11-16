from page_work import save_page
text=r'''\scanpage{131}
$\underline{\overline{\mathrm V}}$\quad\deleted{$\unsure{\mathrm{IV}|\mathrm{VI}}$}
\begin{flushright}
\deleted{\uuline{Schémas de Hilbert, de Picard}}

\deleted{(sans théorie des\\
relations \unsure{intimes} avec les\\
groupes fondamentaux)}
\end{flushright}
\mspage{130}
'''
save_page(131,text,[('text','upper left in rotated reading orientation','overlined and underlined V'),('deletion','beside V','IV or VI'),('deletion','upper right title','Schémas de Hilbert de Picard'),('text','within canceled title','double-underlined Schémas de Hilbert, de Picard'),('deletion','subtitle below canceled title','(sans théorie des relations intimes avec les groupes fondamentaux)'),('text','original bottom left page number','130')],sheet_kind='cover',observations='Original whole, rotated whole, and both supplied halves read. Sparse cover has title and parenthetical subtitle canceled by slanting lines; V at left is live and has both overline and underline. Adjacent canceled Roman label and subtitle adjective enlarged and marked doubtful. No page count is present.')
