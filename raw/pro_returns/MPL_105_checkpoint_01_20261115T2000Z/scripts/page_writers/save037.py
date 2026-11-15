import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{37}
\margin{UTDE\\UTIL\\UTSD}
\texttt{llpd 'cnu1.modulef.utda'}
\diagram{\begin{array}{llllllll}
\mathtt{AFMDES}&\mathtt{CLOSE}&\mathtt{CUTTER}&\mathtt{DYNAM}&\mathtt{ECRDIR}&\mathtt{ECR1}&\mathtt{FLIPFLOP}&\mathtt{INCANO}\\
\mathtt{INCAPA}&\mathtt{INDUNI}&\mathtt{IVIRT}&\mathtt{LAYOUT}&\mathtt{LECDIR}&\mathtt{LEC1}&\mathtt{LISTPDS}&\mathtt{MDES}\\
\mathtt{MESSAGE}&\mathtt{NUMALP}&\mathtt{OPEN}&\mathtt{TRANSLAT}&\mathtt{UPDATE}&&&
\end{array}}
\margin{$\unsure{1|I}$\\$\unsure{B|\beta}$}
\margin{21}
\texttt{llpd 'cnu1.modulef.utdas'}
\diagram{\begin{array}{llllllll}
\mathtt{AFMDES}&\mathtt{CLOSE}&\mathtt{CUTTER}&\mathtt{DYNAM}&\mathtt{ECRDIR}&\mathtt{FLIPFLOP}&\mathtt{INCANO}&\mathtt{INDUNI}\\
\mathtt{IVIRT}&\mathtt{LAYOUT}&\mathtt{LECDIR}&\mathtt{LISTPDS}&\mathtt{MDES}&\mathtt{MESSAGE}&\mathtt{NUMALP}&\mathtt{OPEN}\\
\mathtt{TRANSLAT}&\mathtt{UPDATE}&&&&&&\\\hline
\end{array}}
\margin{$\unsure{\Pi|\Omega}$}
\texttt{llpd 'cnu1.modulef.utde'}
\diagram{\begin{array}{llllllll}
\mathtt{AFMDES}&\mathtt{CLOSE}&\mathtt{CUTTER}&\mathtt{DEFDIR}&\mathtt{DYNAM}&\mathtt{ECPDIR}&\mathtt{ECP1}&\mathtt{ECRDIR}\\
\mathtt{ECRF0}&\mathtt{ECR1}&\mathtt{ECTDIR}&\mathtt{ERLIBR}&\mathtt{FERDIR}&\mathtt{FLIPFLOP}&\mathtt{INCANO}&\mathtt{INCAPA}\\
\mathtt{INDUNI}&\mathtt{INIDIR}&\mathtt{INITI}&\mathtt{IVIRT}&\mathtt{LAYOUT}&\mathtt{LECDIR}&\mathtt{LECTAB}&\mathtt{LECTUD}\\
\mathtt{LECTUI}&\mathtt{LECTUK}&\mathtt{LECTUT}&\mathtt{LECTU1}&\mathtt{LECTU2}&\mathtt{LECTU3}&\mathtt{LECTU4}&\mathtt{LECTU5}\\
\mathtt{LECT10}&\mathtt{LECVAL}&\mathtt{LEC1}&\mathtt{LEPDIR}&\mathtt{LEP1}&\mathtt{LETDIR}&\mathtt{LISTPDS}&\mathtt{MDES}\\
\mathtt{MESS}&\mathtt{MESSAGE}&\mathtt{NBLIGN}&\mathtt{NBMACH}&\mathtt{NBMOTS}&\mathtt{NUMALP}&\mathtt{OPEN}&\mathtt{OUVDIR}\\
\mathtt{POLIBR}&\mathtt{TRANSLAT}&\mathtt{UPDATE}&&&&&
\end{array}}
\margin{51}
\texttt{llpd 'cnu1.modulef.utdes'}
\diagram{\begin{array}{llllllll}
\mathtt{ECTDIR}&\mathtt{ERLIBR}&\mathtt{INCANO}&\mathtt{INITI}&\mathtt{LECTAB}&\mathtt{LECTUD}&\mathtt{LECTUI}&\mathtt{LECTUK}\\
\mathtt{LECTUT}&\mathtt{LECTU1}&\mathtt{LECTU2}&\mathtt{LECTU3}&\mathtt{LECTU4}&\mathtt{LECTU5}&\mathtt{LECT10}&\mathtt{LECVAL}\\
\mathtt{LETDIR}&\mathtt{MESS}&\mathtt{NBLIGN}&\mathtt{POLIBR}&&&&\\\hline
\end{array}}
\margin{20}
\texttt{llpd 'cnu1.modulef.utdf'}
\diagram{\begin{array}{llllllll}
\mathtt{DEFDIR}&\mathtt{ECPDIR}&\mathtt{ECP1}&\mathtt{ECRF0}&\mathtt{FERDIR}&\mathtt{INIDIR}&\mathtt{LEPDIR}&\mathtt{LEP1}\\
\mathtt{NBMACH}&\mathtt{NBMOTS}&\mathtt{OUVDIR}&&&&&
\end{array}}
\margin{$\unsure{1|I}$\\$\unsure{B|\beta}$}
\margin{11}
\texttt{llpd 'cnu1.modulef.utdfs'}
\diagram{\begin{array}{llllllll}
\mathtt{DEFDIR}&\mathtt{ECPDIR}&\mathtt{ECRF0}&\mathtt{FERDIR}&\mathtt{INIDIR}&\mathtt{LEPDIR}&\mathtt{NBMACH}&\mathtt{NBMOTS}\\
\mathtt{OUVDIR}&&&&&&&\\\hline
\end{array}}
\margin{$\unsure{\Omega|\Pi}$}
\texttt{llpd 'cnu1.modulef.utdm'}

\texttt{TSC0185I ANGIVET BIBLIOTEK (PDS) HAR INGA MEDLEMMAR}

\texttt{llpd 'cnu1.modulef.utdms'}
\diagram{\begin{array}{llllllll}
\mathtt{\$RETURN}&\mathtt{\$SAVE}&\mathtt{\$STOP}&\mathtt{\pounds COMDIR}&\mathtt{\pounds DBDAM}&\mathtt{\pounds DBSAM}&\mathtt{\pounds DES}&\mathtt{CALL}\\
\mathtt{CAMLST}&\mathtt{CHECK}&\mathtt{CLOSE}&\mathtt{DCBD}&\mathtt{FREEMAIN}&\mathtt{GETMAIN}&\mathtt{IECSDSL1}&\mathtt{IECTDECB}\\
\mathtt{IEFASCTB}&\mathtt{IEFASIOT}&\mathtt{\unsure{IEFJFCRN|IEFJFCBN}}&\mathtt{IEFTIOT1}&\mathtt{IEZBITS}&\mathtt{\unsure{IEZDEB|IEZDER}}&\mathtt{IEZJSCR}&\mathtt{IHACDE}\\
\multicolumn{8}{l}{\illegible{8}}
\end{array}}
\mspage{36}
'''
e=[('margin note','handwritten above listing','UTDE UTIL UTSD')]
for p,cmd,op in [('first','utda','AFMDES CLOSE CUTTER'),('second','utdas','AFMDES CLOSE CUTTER'),('third','utde','AFMDES CLOSE CUTTER'),('fourth','utdes','ECTDIR ERLIBR INCANO'),('fifth','utdf','DEFDIR ECPDIR ECP1'),('sixth','utdfs','DEFDIR ECPDIR ECRF0')]:
 e.extend([('text',p+' block',"llpd cnu1.modulef."+cmd),('diagram',p+' block',op)])
e.extend([('margin note','first block left','1 B'),('margin note','first block right','21'),('margin note','second block left','Pi'),('margin note','third block right','51'),('margin note','fourth block right','20'),('margin note','fifth block left','1 B'),('margin note','fifth block right','11'),('margin note','sixth block left','Omega'),('text','seventh block','llpd cnu1.modulef.utdm'),('text','seventh block','TSC0185I ANGIVET BIBLIOTEK'),('text','eighth block','llpd cnu1.modulef.utdms'),('diagram','eighth block','$RETURN $SAVE $STOP'),('text','cut bottom edge','unrecoverable cut-off next row'),('text','bottom left','36')])
record_page(37,s,e,'reused_typed',notes='Printed module/member lists with handwritten UTDE UTIL UTSD, small left signs, and right counts 21,51,20,11. These are counts beside code lists, not explicit manuscript page totals. The next printed row is cut off at the physical scan edge; only tips of characters survive, represented by a word-count illegibility mark.')
build_doubts()
