from record_page import save_page
save_page(152,12,r'''
\begin{tabular}{rlll}
\texttt{1}&\texttt{//PREDONTA}&\texttt{JOB '*********,00000000C','\hspace{4em}',}&\texttt{JOB 1125}\\
&\texttt{//}&\texttt{MSGLEVEL=(1,1)}&\\
\texttt{2}&\texttt{//}&\texttt{EXEC CSSBATCH}&\\
\texttt{3}&\texttt{XXCSSBATCH}&\texttt{PROC REG=100K,P=''}&\texttt{00010000}\\
\texttt{4}&\texttt{XXCSSBATCH}&\texttt{EXEC PGM=CRBATCH,REGION=\&REG,PARM=\&P}&\texttt{00020000}\\
\texttt{5}&\texttt{XXSTEPLIB}&\texttt{DD DSN=CISI.PROD.CSSBATCH.V1.YY01,DISP=SHR}&\texttt{00030003}\\
\texttt{6}&\texttt{XXSYSUT1}&\texttt{DD DSN=\&\&SYSUT1,UNIT=\unsure{SYSTSO|SYSTS0},SPACE=(TRK,30),DISP=(NEW,DELETE)}&\texttt{00031006}\\
\texttt{7}&\texttt{XXSYSUDUMP}&\texttt{DD SYSOUT=*}&\texttt{00040000}\\
\texttt{8}&\texttt{XXCRJIF}&\texttt{DD DSN=SYS1.CR.JIF,DISP=SHR}&\texttt{00050000}\\
\texttt{9}&\texttt{XXSYSIN}&\texttt{DD DDNAME=CRAYIN}&\texttt{00060000}\\
\texttt{10}&\texttt{//CRAYIN}&\texttt{DD *}&
\end{tabular}
\mspage{11}
''',[
('text','top printed row 1','1 //PREDONTA JOB; JOB 1125'),('text','top continuation','// MSGLEVEL=(1,1)'),('text','top row 2','// EXEC CSSBATCH'),('text','top row 3','XXCSSBATCH PROC REG=100K,P; 00010000'),('text','top row 4','XXCSSBATCH EXEC PGM=CRBATCH; 00020000'),('text','top row 5','XXSTEPLIB DD DSN=CISI.PROD.CSSBATCH.V1.YY01; 00030003'),('text','top row 6','XXSYSUT1 DD DSN=&&SYSUT1; 00031006'),('text','top row 7','XXSYSUDUMP DD SYSOUT=*; 00040000'),('text','top row 8','XXCRJIF DD DSN=SYS1.CR.JIF; 00050000'),('text','top row 9','XXSYSIN DD DDNAME=CRAYIN; 00060000'),('text','top row 10','//CRAYIN DD *'),('text','bottom left handwritten page number','11')
],kind='reused_typed',observations='Reused printed job-control listing; handwritten sheet number 11, no mathematical writing. All eleven printed lines, including the unnumbered continuation, are retained.')
