from record import *
k='120_scan002';crop='120_scan002 (700,35,1545,300)'
t=r'''\scanpage{2}
\margin{\unsure{1978|1778}}
\uline{\deleted{\unsure{Structure|Structures}}\inserted{Topologie} modérée}

(Autour de l'Eloge)
\mspage{1}
'''
commit(k,t,[('faint pencil after the four digits',r'\illegible{1}','[H absent]','[no additional word]','The gray vertical trace adjoins/underlies the inked initial S; it does not form a separately bounded word.','medium','text not on the page','yes','no','n/a','',crop),('cancelled title word',r'\unsure{Structures}','[H absent]',r'\unsure{Structure|Structures}','The initial Str- and medial -uctur- survive the hatching, but the final e/s is crossed and overlaps the descender of Topologie.','low','misread word','yes','no','n/a','',crop)],[
 ('M0449','undecided',r'\unsure{1978|1778}','Four faint pencil figures are present; the second lacks a sufficiently firm upper loop to settle 9 against 7.',crop,'low'),
 ('M0450','other','[no text]','No separately bounded word follows the four figures; the isolated trace lies under the cancelled initial.',crop,'medium')],
 ['margin note|upper title left|uncertain 1978/1778','deletion|upper right original heading|uncertain Structure/Structures','insertion|above cancelled heading|Topologie','text|upper right heading|modérée (underlined with heading)','text|below heading in pencil|(Autour de l’Eloge)','margin note|bottom left|1'],
 'Cover/title sheet: “Topologie modérée” replaces a cancelled “Structure(s)”. The pencil subtitle is “(Autour de l’Eloge)”. Four faint figures may read 1978 or 1778; this is not promoted to a secure date. Bottom pagination: 1. No mathematical statement is checked on this sheet. H has no transcription for it.',
 habits=['The cover combines dark ink cancellation and insertion with much fainter pencil date/subtitle. The last letters of the struck heading overlap the descender of the inserted word; no general final-s rule can be inferred.'],notation=[('underlined heading with insertion','A single long underline belongs to the heading as a whole; Topologie sits above the cancelled first word.')],doubts=[('upper left pencil figures',r'\unsure{1978|1778}','9 or 7 in second position','low'),('cancelled first title word',r'\unsure{Structure|Structures}','terminal s obscured','low')],sheet='cover')
