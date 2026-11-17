from workflow import save_page
save_page(8,r'''
\scanpage{8}
\texttt{/*JOB=CRAY2,ACCT=\unsure{*********|********},ALL=M06,MSGL=N}\qquad\texttt{J0429CNU}

\texttt{// JOB MSGLEVEL=(1,1),MSGCLASS=A}

\texttt{// EXEC PGM=IEFBR14}
\margin{\mspage{7}}
''',[('text','top left line 1','/*JOB=CRAY2,ACCT='),('text','top centre-right line 1','J0429CNU'),('text','top left line 2','// JOB MSGLEVEL=(1,1),MSGCLASS=A'),('text','top left line 3','// EXEC PGM=IEFBR14'),('text','bottom left pencil','7')],doubts=[('line 1 after ACCT=','********* / ********','Nine versus eight printed asterisks against striped stock','medium')],observations='Reused computer printout containing three JCL lines and job identifier. Pencil 7. No mathematical manuscript text.',sheet_kind='reused_typed')
