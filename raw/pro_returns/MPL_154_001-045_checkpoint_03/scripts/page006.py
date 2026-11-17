from workflow import save_page
zero=[
'           00000000',
'         0000000000',
'       00      0000',
'      00     00 00',
'     00    00  00',
'    00   00   00',
'   00  00    00',
'  00 00     00',
' 0000      00',
'000       00',
'0000000000',
'00000000']
C=[' CCCCCCCCCC','CCCCCCCCCCCC','CC        CC','CC','CC','CC','CC','CC','CC','CC        CC','CCCCCCCCCCCC',' CCCCCCCCCC']
R=['RRRRRRRRRRR','RRRRRRRRRRRR','RR        RR','RR        RR','RR        RR','RRRRRRRRRRRR','RRRRRRRRRRR','RR    RR','RR     RR','RR      RR','RR       RR','RR        RR']
A=[' AAAAAAAAAA','AAAAAAAAAAAA','AA        AA','AA        AA','AA        AA','AAAAAAAAAAAA','AAAAAAAAAAAA','AA        AA','AA        AA','AA        AA','AA        AA','AA        AA']
Y=['YY        YY','YY        YY',' YY      YY','  YY    YY','   YY  YY','    YYYY','     YY','     YY','     YY','     YY','     YY','     YY']
T=[' 2222222222','222222222222','22        22','          22','          22','         22','       22','     22','   22',' 22','222222222222','222222222222']
def charfigure(blocks,step):
 s='\\figure{%\n\\begin{tikzpicture}[x=.11cm,y=.17cm]\n'
 bychar={}
 for b,rows in enumerate(blocks):
  for y,row in enumerate(rows):
   for x,ch in enumerate(row):
    if ch!=' ': bychar.setdefault(ch,[]).append(f'{x+b*step}/{-y}')
 for ch,positions in bychar.items():
  s+='\\foreach \\x/\\y in {'+','.join(positions)+'}{\\node[inner sep=0pt,font=\\ttfamily\\tiny] at (\\x,\\y) {'+ch+'};}\n'
 return s+'\\end{tikzpicture}%\n}\n'
tex=r'''
\scanpage{6}
\margin{\mspage{5}}
\texttt{//*\quad CRAY2\quad 0429\qquad \unsure{1|I}}
'''+charfigure([zero]*4,14)+charfigure([C,R,A,Y,T],14)+r'''
\diagram{%
\begin{array}{llllllllllll}
\texttt{****A}&\texttt{START}&\texttt{JOB}&\texttt{429}&\texttt{CRAY2}&\texttt{ROOM}&\texttt{4.30.42 PM 16 AUG 82}&\texttt{R6.PR1}&\texttt{SYS JES2}&\texttt{JOB 429}&\texttt{START}&\texttt{A****}\\
\texttt{****A}&\texttt{START}&\texttt{JOB}&\texttt{429}&\texttt{CRAY2}&\texttt{ROOM}&\texttt{4.30.42 PM 16 AUG 82}&\texttt{R6.PR1}&\texttt{SYS JES2}&\texttt{JOB 429}&\texttt{START}&\texttt{A****}\\
\texttt{****A}&\texttt{START}&\texttt{JOB}&\texttt{429}&\texttt{CRAY2}&\texttt{ROOM}&\texttt{4.30.42 PM 16 AUG 82}&\texttt{R6.PR1}&\texttt{SYS JES2}&\texttt{JOB 429}&\texttt{START}&\texttt{A****}\\
\texttt{****A}&\texttt{START}&\texttt{JOB}&\texttt{429}&\texttt{CRAY2}&\texttt{ROOM}&\texttt{4.30.42 PM 16 AUG 82}&\texttt{R6.PR1}&\texttt{SYS JES2}&\texttt{JOB 429}&\texttt{START}&\texttt{A****}\\
\texttt{****A}&\texttt{START}&\texttt{JOB}&\texttt{429}&\texttt{CRAY2}&\texttt{ROOM}&\texttt{4.30.42 PM 16 AUG 82}&\texttt{R6.PR1}&\texttt{SYS JES2}&\texttt{JOB 429}&\texttt{START}&\texttt{A****}\\
\texttt{****A}&\texttt{START}&\texttt{JOB}&\texttt{429}&\texttt{CRAY2}&\texttt{ROOM}&\texttt{4.30.42 PM 16 AUG 82}&\texttt{R6.PR1}&\texttt{SYS JES2}&\texttt{JOB 429}&\texttt{START}&\texttt{A****}
\end{array}%
}
\texttt{DERNIERE MISE A JOUR DE JOURNAL : 11-08-82}

\texttt{ATTENTION ...........}

\texttt{1. ARRET DE L'ORDINATEUR LE MARDI 17 AOUT DE 7 H A 8 H.}

\diagram{%
\begin{array}{ll}
\texttt{]}&\texttt{2. UNE MODIFICATION SYSTEME NOUS CONTRAINDRA A DETRUIRE}\\
\texttt{]}&\quad\texttt{LE CONTENU DU DISQUE SPOOL LE MARDI 17 AOUT A 6 HEURES}\\
\texttt{]}&\quad\texttt{VEUILLEZ RECUPERER VOS SORTIES EN ATTENTE AVANT CETTE}\\
\texttt{]}&\quad\texttt{DATE. MERCI DE VOTRE COMPREHENSION.}\\
\texttt{]}&\texttt{3. UN ARRET EXCEPTIONNEL POUR PREPARER L'ARRIVEE DE NOUVELLES}\\
\texttt{]}&\quad\texttt{UNITES AURA LIEU DU VENDREDI 20 AOUT A 17H 30 AU LUNDI}\\
\texttt{]}&\quad\texttt{23 AOUT A \unsure{9H|3H}.}
\end{array}%
}
'''
save_page(6,tex,[('text','pencil margin, original bottom left','5'),('text','printed header (rotated reading orientation)','//* CRAY2 0429 1'),('drawing','printed top banner','four zero-character glyphs'),('drawing','printed central banner','CRAY2 in C R A Y 2 characters'),('text','job-header row 1','****A START JOB 429 CRAY2'),('text','job-header row 2','****A START JOB 429 CRAY2'),('text','job-header row 3','****A START JOB 429 CRAY2'),('text','job-header row 4','****A START JOB 429 CRAY2'),('text','job-header row 5','****A START JOB 429 CRAY2'),('text','job-header row 6','****A START JOB 429 CRAY2'),('text','below job header','DERNIERE MISE A JOUR'),('text','notice heading','ATTENTION ...........'),('text','notice 1','ARRET DE L’ORDINATEUR'),('text','notice 2, four lines with ]','UNE MODIFICATION SYSTEME'),('text','notice 3, three lines with ]','UN ARRET EXCEPTIONNEL')],doubts=[('printed header last character','1 / I','Serif glyph ambiguous','medium'),('final notice time','9H / 3H','First digit faint and loop unclear','medium'),('character banners','all repeated characters transcribed by manual visual count','Counts and exact column spacing are lower-confidence than prose; no OCR used','medium')],observations='Reused computer printout, rotated 90° for reading after whole and both original halves were inspected. Printed job timestamp 16 AUG 82; journal update 11-08-82. Notices concern interruptions on 17 and 20–23 August. These are dates on reused stock, not dates assigned to the mathematical notes. Pencil 5 at original bottom-left; no mathematical manuscript prose.',sheet_kind='reused_typed')
