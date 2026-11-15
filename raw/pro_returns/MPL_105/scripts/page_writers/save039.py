import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
util='''ABEGCD ABEGCR AB0D AB0R AB1D AB1R ADRESS AFFCOM
AFFKOM ALEAD ALEAR ASMPVD ATAD ATAR ATB0D ATB0R
ATB1D ATB1R ATMPBD ATMPVD AZEROD AZEROR BASYMD CADRE
CHOLOC CL2TBD CL2TBR CL2VED CL2VER COMPRE CROLOC DECAL
DECODA DET3D DGELG DILATE FOARET ICHIF IEGAL IMATAB
IMPRIA IMPTAB INVCRO INVLOC ISIGNO ISOMME MAJDCB MAXTAM
MNEMO MUPLIN MUPDB2 MXPOIR MXP01R NBARET NBDIFF NBFACE
NBMAXI NBMINI NBSOME NEWS NOM NOMAFF NOMLON NUMALP
PA PB PLMASD PLONAD PN2DDE PN2DIN PN2DPR PN2DVA
PN3DDE PN3DIN PN3DPR PN3DVA PROJEC PROLIG PROSCD PROSCR
PU PV PW PY P1 Q1 RCHLOC READRE
RENOMM SECANT SGNHEX SGNQUA SGNTET SGNTRI SOMABD SOMABR
SOMMEM TABAND TABANR TABARD TABARR TABASD TABASR TABAUD
TABAUR TABAZD TABAZR TABA0D TABA0R TABA1D TABA1R TABA2D
TABA2R TABA3D TABA3R TABA4D TABA4R TABA5D TABA5R TABA6D
TABA6R TABA7D TABA7R TABA8D TABA8R TABA9D TABA9R TABSUD
TABSUR TABSZD TABSZR TAB0D TAB0R TAB1D TAB1R TRCROI
TRFLEC TROUVE TRTATA TRTAVE TUER TYMAEL TYPCLA TYPGEL
TYPMOT VERIF'''
utsd='''AELESU AJASS CNDLN COPISD COSDB COTASD CTYTAE CTYTA1
ECAMAT ECATRI ECB ECBDCL ECCOOR ECFORC ECHYMA ECMAIL
ECMILI ECMPLR ECMUA ECNOPO ECRIA1 ECRIT1 ECRTAE ECTAE
ECTASD ECTYNO ECVISU ECVVFR ESTASF ESVVFR IAIJ1 IMAMAT
IMAMA1 IMAMA2 IMATRI IMB IMBDCL IMB1 IMCOOR IMC001
IMFORC IMHYMA IMMAIL IMMAI1 IMMILI IMMPLR IMMUA IMNOPO
IMTADE IMTAE IMTASD IMTA01 IMTYNO IMVISU IMVVFR IM1BDC
INICSD INITMP INTAR0 ISNOF5 LEAMAT LEAMMS LEATRI LEB
LEBDCL LECOOR LEFORC LEHYMA LEMAIL LEMEFI LEMILI LEMPLR
LEMUA LENOPO LETAE LETASD LETYNO LEVISU LEVVFR LRNDL1
LSVVFR MONOFO MONOF5 MONOF6 NCMUNS NDL NIVLIB NUPAG
NUPAGE PRINTR PRIN1B RACRNO REAMAT REATRI REB REBDCL
RECOOR REFORC REHYMA REMAIL REMEFI REMILI REMPLR REMUA
RENOPO RESOUR RETAE RETASD RETYNO REVISU REVVFR RSTSDE
SAUCSD SAUSDS SAUTP SDBMSC STAMD STAMR TRAMAD TRAMAR
TUERSD TUTASD VERNN VERTNN'''
unc={'ATMPBD':r'\unsure{ATMPBD|ATMPRD}','MUPDB2':r'\unsure{MUPDB2|MUPDB2}','MXPOIR':r'\unsure{MXPOIR|MXP0IR}','IHASPQE':r'\unsure{IHASPQE|IHASPRE}','IMC001':r'\unsure{IMC001|IMCOO1}','INTAR0':r'\unsure{INTAR0|INTARO}','IMTA01':r'\unsure{IMTA01|IMTAO1}'}
# The two utility tables were separately read visually; their visible entries agree.
def arr(txt,rule=False):
 lines=[]
 for row in txt.splitlines():
  words=row.split()
  lines.append('&'.join(r'\mathtt{'+unc.get(w,w)+'}' for w in words)+'&'*(8-len(words)))
 return '\\diagram{\\begin{array}{llllllll}\n'+'\\\\\n'.join(lines)+('\\\\\\hline' if rule else '')+'\n\\end{array}}\n'
s=r'\scanpage{39}'+'\n'
s+=arr('IHALLE IHAPSA IHARB IHASPQE IHAXTLST IKJRB IKJTCB OBTAIN\nOPEN RDJFCB READ SYNADAF SYNADRLS WRITE')
s+=r"\texttt{llpd 'cnu1.modulef.util'}"+'\n'+arr(util)
s+=r'\margin{utilitaires\\fortran\\146}'+'\n'
s+=r"\texttt{llpd 'cnu1.modulef.utils'}"+'\n'+arr(util,True)
s+=r"\texttt{llpd 'cnu1.modulef.utsd'}"+'\n'+arr(utsd)
s+=r'\margin{fortran\\124}'+'\n'
s+=r"\texttt{llpd 'cnu1.modulef.utsds'}"+'\n'+arr('\n'.join(utsd.splitlines()[:6]))
s+=r'\mspage{38}'+'\n'
s=s.replace(r'\unsure{MUPDB2|MUPDB2}',r'\unsure{MUPDB2|MUPOB2}')
e=[('diagram','top clipped excerpt','IHALLE IHAPSA IHARB'),('text','first block','llpd cnu1.modulef.util'),('diagram','first block','ABEGCD ABEGCR AB0D'),('margin note','right of first block','utilitaires fortran 146'),('text','second block','llpd cnu1.modulef.utils'),('diagram','second block','ABEGCD ABEGCR AB0D'),('text','third block','llpd cnu1.modulef.utsd'),('diagram','third block','AELESU AJASS CNDLN'),('margin note','right of third block','fortran 124'),('text','fourth block','llpd cnu1.modulef.utsds'),('diagram','fourth block clipped','AELESU AJASS CNDLN'),('text','bottom left','38')]
record_page(39,s,e,'reused_typed',notes='Printed utility/subroutine lists, including repeated complete utility tables and a final table cut off after six visible rows. Handwritten utilitaires/fortran and counts 146,124. A few clipped top-row names and O/0 cases are marked as doubts.')
build_doubts()
