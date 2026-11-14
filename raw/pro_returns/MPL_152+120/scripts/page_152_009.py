from record_page import save_page
save_page(152,9,r'''
{\ttfamily\scriptsize
\begin{tabular}{l}
J E S 2\quad J O B\quad L O G\quad --\quad S Y S T E M\quad E 3 3 3\quad --\quad N O D E\quad E 3 3 3\\[1ex]
16.39.12 J1125CNU\quad\$ J1125*PREDONTA STARTED - INIT 10 - CLASS Q - SYS E333\\
16.39.14 J1125CNU\quad DSN CISI.PROD.CSSBATCH.V1.YY01\\
16.39.14 J1125CNU\quad CSS2090 - JOB INPUT FILE TEMPORARILY FULL - PLEASE TRYAGAIN LATER\\
16.39.14 J1125CNU\quad SMF RECORD 153-1 (CLOSE) WRITTEN\\
16.39.15 J1125CNU\quad\$ J1125*PREDONTA ENDED\\[1ex]
------ JES2 JOB STATISTICS ------\\[1ex]
\quad 19 MAY 82 JOB EXECUTION DATE\\[1ex]
\hspace{1cm}26 CARDS READ\\[1ex]
\hspace{1cm}93 SYSOUT PRINT RECORDS\\[1ex]
\hspace{1cm}0 SYSOUT PUNCH RECORDS\\[1ex]
\hspace{.5cm}0.05 MINUTES EXECUTION TIME
\end{tabular}}
\mspage{\unsure{8|2}}
''',[
('text','lower half, upside down printed heading','JES2 JOB LOG -- SYSTEM E333 -- NODE E333'),('text','printed line 1','16.39.12 J1125CNU $ J1125*PREDONTA STARTED'),('text','printed line 2','16.39.14 J1125CNU DSN CISI.PROD.CSSBATCH.V1.YY01'),('text','printed line 3','16.39.14 J1125CNU CSS2090'),('text','printed line 4','16.39.14 J1125CNU SMF RECORD 153-1'),('text','printed line 5','16.39.15 J1125CNU $ J1125*PREDONTA ENDED'),('text','printed section heading','------ JES2 JOB STATISTICS ------'),('text','printed statistics line 1','19 MAY 82 JOB EXECUTION DATE'),('text','printed statistics line 2','26 CARDS READ'),('text','printed statistics line 3','93 SYSOUT PRINT RECORDS'),('text','printed statistics line 4','0 SYSOUT PUNCH RECORDS'),('text','printed statistics line 5','0.05 MINUTES EXECUTION TIME'),('text','bottom left manuscript number','8 / 2')
],kind='reused_typed',observations='Reused job-log printout, no mathematical handwriting. Explicit printed date “19 MAY 82 JOB EXECUTION DATE”; not a manuscript date. The bottom handwritten number resembles a narrow 8, with 2 retained as an alternative.')
