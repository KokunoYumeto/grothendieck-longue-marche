from record_page import record
rows=[
['[name redacted] J.','27°','7.10.39','1.10.62','5°éch.','1.01.77\n(avec 2a 8m21j.','4a 8m 21j','6°éch.','1.01.79','-'],
['[name redacted] Ch.','30° 4°','7.05.41','1.12.61','4°éch.','1.10.77\n(avec 9m)','2a','5°éch.','-','1.01.79'],
['[name redacted] P.','49°','2.10.41','1.10.63','3°éch.','1.04.77','1a 9m','4°éch.','1.01.79','1.04.79'],
['[name redacted] P.','49°','23.10.33','1.12.68','5°éch.','1.01.79\n(avec 3 a)','3a','6°éch.','1.07.79','-'],
['[name redacted] J.','24°','23.08.42','1.10.77','2°éch.','1.06.78','7m','3°éch.','1.09.79','-'],
['[name redacted] J.','21° 2°','17.12.37','1.11.63','5°éch.','1.01.76\n(avec 4m 23j)','3a 4m 23j','6°éch.','1.03.79','-'],
['[name redacted] F.-','18° 2°','29.03.35','1.06.64','5°éch.','1.02.75','3a 11m','6°éch.','1.01.79','-'],
['[name redacted] B.','29°','8.03.45','1.10.77','1°éch.','1.10.77','1a 3m','2°éch.','1.01.79','1.10.79'],
['[name redacted] A.','23°','27.12.40','1.10.74','3°éch.','1.01.78','1a','4°éch.','1.04.79','-'],
['[name redacted] P.','24°','28.06.31','1.07.59','5°éch.','1.01.74\n(avec 3m)','5a 3m','6°éch.','1.01.79','1.10.79'],
['[name redacted] J.J.','30° 4°','2.04.39','1.10.60','4°éch.','1.01.78','1a','5°éch.','1.04.79','-'],
['[name redacted] H.','21°','19.04.40','1.10.63','5°éch.','1.01.79\n(avec 4a 1m)','4a 1m','6°éch.','1.01.79','-'],
['[name redacted] J.P.','23°','5.07.39','1.11.64','5°éch.','1.04.76','2a 9m','6°éch.','1.10.79','-'],
['[name redacted] M.','27°','15.05.41','1.10.64','3°éch.','1.10.78\n(avec 1a)','1a 3m','4°éch.','1.01.79','1.10.79'],
['SANS A.','31° 1°','14.12.39','1.10.60','4°éch.','1.04.77','1a 9m','5°éch.','1.01.79','1.04.79'],
['[name redacted] DE LA\nFUENTE B.','50°','22.07.37','1.10.61','4°éch.','1.01.77','2a','5°éch.','-','1.01.79'],
['[name redacted] P.','27° 2°','1.10.39','1.11.63','5°éch.','1.01.77\n(avec 9m 6j)','2a 9m 6j','6°éch.','1.10.79','-']]
headers=['Noms et Ordre\nde présentation','Section\nC.C.U.','Date de\nnaissance',"Date d'entrée\ndans l'Enseign.\nsupérieur",'Classement\nactuel',"Date dernière\npromotion\nd'échelon",'Ancienneté au\n31-12-1978\n(échelon)','Classe\net échelon\nproposés','Choix','Ancienneté']
def cell(s):
 parts=s.split('\n')
 if len(parts)>1:return r'\begin{array}{l}'+r'\\'.join(r'\text{'+p+'}' for p in parts)+r'\end{array}'
 return r'\text{'+s+'}'
tex=r'''\scanpage{18}
\begin{center}
UNIVERSITE DES SCIENCES\\
ET TECHNIQUES\\
DU LANGUEDOC

PROFESSEURS SANS CHAIRE ET MAITRES DE CONFERENCES

PROPOSITIONS RELATIVES A L'AVANCEMENT POUR L'ANNEE 1979
\end{center}
\uline{Service du Personnel}\qquad/MV

\diagram{\begin{array}{|l|c|c|c|c|c|c|c|c|c|}
\hline
'''
tex+=' & '.join(cell(h) for h in headers)+r'\\\hline'+'\n'
for row in rows:tex+=' & '.join(cell(x) for x in row)+r'\\'+'\n'
tex+=r'''\hline
\end{array}}
% archive foliation: 17
'''
elements=[('text','heading left','UNIVERSITE DES SCIENCES ET TECHNIQUES DU LANGUEDOC'),('text','heading right','PROFESSEURS SANS CHAIRE ET MAITRES DE CONFERENCES'),('text','heading right second line',"PROPOSITIONS RELATIVES A L’AVANCEMENT POUR L’ANNEE 1979"),('text','above table','Service du Personnel /MV'),('diagram','table header','Noms et Ordre ... Ancienneté')]
elements += [('diagram',f'table row {i+1}',r[0].replace('\n',' ')) for i,r in enumerate(rows)]
record(18,tex,elements,'''Typed personnel advancement table for 1979, Université des Sciences et Techniques du Languedoc, Service du Personnel /MV. It records seventeen people and ten columns; transcribed as a complete array. The dates explicitly include seniority at 31-12-1978, but the sheet alone does not date every handwritten neighbouring calculation. No handwritten mathematical content is present. Archive foliation 17 is not an authorial page count.''',sheet_kind='reused_typed')
