from workflow import save_page,ROOT,utc
tex=r'''\scanpage{10}
\mspage{$6'$}

En plus de ces $5$ variantes $\mathcal X_0,\mathcal X_1,\mathcal X'_1,\mathcal X_2,\mathcal X_3$ il y a \inserted{bien entendu} les revêtements de ces cartes (ramifiés pour les trois premières) principaux de groupe $D_{2n}$, associés aux $\operatorname{Pol}(D)$. Ce sont les revêtements $\widetilde{\mathcal X}_i$ qui sont les déploiements ultimes.

Les surfaces les plus utiles me semblent ici $\mathcal X'_1,\mathcal X_2,\mathcal X_3$ et leurs revêtements $\widetilde{\mathcal X}'_1,\widetilde{\mathcal X}_2,\widetilde{\mathcal X}_3$. Peut-être peut-on se passer des $\mathcal X_2,\mathcal X_3$ et leurs tildés, au profit des $\mathcal X'_1$ et $\widetilde{\mathcal X}'_1$, d'autant que $\mathcal X'_1$ s'envoie bien dans $X$ comme prévu --- je \inserted{ne} suis pas tout à fait \unsure{convaincu} des \unsure{collisions|collages}, \deleted{\unsure{ayant quelque}}\inserted{en usage} \unsure{qd}, comment ça se passe au voisinage du bord d'une face supercritique.

\margin{9}
'''
# Printer notices are read after rotating the sheet; all text and border rows retained.
lines=[
'*'*80,
'*JESNEWS DU 02/08/1982 C63 CADARACHE'+ ' '*45+'*',
'*'*80,
'*      DEPUIS LE 1/7/82 LES ALIAS DES COMMANDES LIBRARIAN                      *',
'*             LIBGET (LG) ET LIBSAVE (LS) SONT SUPPRIMES,                     *',
'*             POUR EVITER UNE POSSIBILITE DE CONFLIT AVEC                    *',
'*             LE MEME ALIAS DES COMMANDES STANDARD IBM.                     *',
'*      ********                                                             *',
'* ATTENTION                                                                 *',
'*   MISE EN SERVICE LE VENDREDI 30/7/82 A 8H00 DE LA DEUXIEME PHASE DE G4F    *',
'*     SUR 168 CADARACHE.                                                     *',
"*     ELLE PERMET D'UTILISER DANS LA CDE. KEEP TSO ET DANS LA PROCEDURE KEEP  *",
"*     BATCH UNE POSSIBILITE D'AFFECTATION DE TYPE DE SAUVEGARDE AU NIVEAU DU *",
'*     FICHIER.CETTE POSSIBILITE EST VIVEMENT CONSEILLEE.                      *',
'*     POUR PLUS AMPLES INFORMATIONS VOIR NOTE TECHNIQUE CISI MVS140,LA NOTE  *',
'*     MVS 143 ETANT SUPPRIMEE.                                               *',
'*                                                                            *',
"* EXEMPLES D'UTILISATION:                                                    *",
'*                                                                            *',
'*  BATCH:  DSN=NOM.DU.FICHIER.A.SAUVEGARDER,DELAY=TYPE DE SAUVEGARDE           *',
'*                                                                            *',
'*  TSO:                                                                     *',
"*  K DA('NOM DU FICHIER A SAUVEGARDER') DELAY(TYPE DE SAUVEGARDE)             *",
'*                                                                            *',
'*  TYPES DE SAUVEGARDE:                                                      *',
'*                                                                            *',
'*      W       SAUVEGARDE HEBDO.                                             *',
'*      D       SAUVEGARDE JOURNALIERE.                                        *',
'*      NOS     SAUVEGARDE MENSUELLE.                                          *',
'*      *       PARAMETRE PAR DEFAUT.                                         *',
'*                                                                            *',
'*'*80,
'',
'*'*67,
'*                                                                 *',
'*                  - J E S N E W S  F R 1 -      LE 06/08/82      *',
'*                                                                 *',
'*'+'-'*65+'*',
'*                                                                 *',
'*  DEPUIS LE LUNDI 12 JUILLET 82, LES CLASSES DE TRAVAUX D ET E      *',
'*  SERONT ETENDUES POUR UNE TAILLE MEMOIRE SUPERIEURE A 1024 K       *',
'*  SE REPORTER A LA NOTE TECHNIQUE MVS141.                          *',
'*                                                                 *',
'*'+'-'*65+'*',
"*  A PARTIR DU LUNDI 9 AOUT 1982 , IL SERA POSSIBLE D'IMPRIMER       *",
'*  SUR XEROX 9700 (DESTINATION SAC) DES FICHIERS UTILISANT LE        *',
'*  COUPLE DE JEUX DE CARACTERES : (GS15,GT15)                        *',
'*'*67]
tex+='\n\\begin{tabular}{@{}l@{}}\n'
for line in lines:
    if line:
        s=line.replace(' ','\\ ').replace('C63',r'\unsure{C63|C68}')
        tex+=r'\texttt{'+s+r'}\\'+'\n'
    else: tex+=r'\\'+'\n'
tex+='\\end{tabular}\n'
e=[('text','hand top','6′; En plus de ces 5 variantes'),('insertion','hand top line 2','bien entendu'),('text','hand middle','Les surfaces les plus utiles'),('insertion','hand lower','ne'),('deletion','hand lower','ayant quelque'),('insertion','hand lower','en usage'),('margin note','bottom left','9'),('text','print top after rotation','JESNEWS DU 02/08/1982'),('text','print first notice','DEPUIS LE 1/7/82'),('text','print second notice','ATTENTION; MISE EN SERVICE'),('text','print examples','EXEMPLES D’UTILISATION; BATCH; TSO'),('text','print backup types','TYPES DE SAUVEGARDE; W; D; NOS; *'),('text','print lower heading','J E S N E W S F R 1; LE 06/08/82'),('text','print memory notice','DEPUIS LE LUNDI 12 JUILLET 82'),('text','print character notice','A PARTIR DU LUNDI 9 AOUT 1982'),('drawing','print borders','asterisk and dash borders')]
d=[('hand last paragraph','convaincu; collisions/collages; qd','Rapid strokes and heavy deletion; the noun and abbreviated transition are especially uncertain.','low'),('hand deleted lower line','ayant quelque','The underlying words are crossed through; this is a tentative recovery.','low'),('print header','C63/C68','The final printer digit has a blurred lower loop.','medium'),('print border rows','80 and 67 asterisks','Border character counts and horizontal spacing are approximate; the notices themselves are fully transcribed.','low')]
save_page(10,tex,e,d,'Explicit “Peut-être peut-on se passer…” asks whether X2 and X3 and their covers are dispensable in favor of X′1. The final “je ne suis pas tout à fait convaincu…” is a self-flagged boundary-gluing issue, with uncertain noun. Dihedral principal covers D_2n and ultimate deployments are asserted. Printed 1982 computer notices belong to reused stock; manuscript page is 6′.',sheet_kind='reused_typed')
with (ROOT/'progress.log').open('a') as f:f.write(f'154 scan 011 omitted as blank in supplied image package {utc()}\n')
