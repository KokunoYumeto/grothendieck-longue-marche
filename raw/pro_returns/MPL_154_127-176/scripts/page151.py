from pathlib import Path
import ast
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s=r'''\scanpage{151}
$\underline{\Sigma}=(X,\Sigma)$, d'où surface cellulaire des positions relatives $X^*=\operatorname{Rel}(\underline{\Sigma})$.

Soit un sommet \inserted{$\rho$} de $X^*$, correspondant à une position relative critique \deleted{$\unsure{\Delta}$}$D_{\rho}$, soit $S_{\rho}=D_{\rho}\cap S(\Sigma)$.
\inserted{Une orientation $\unsure{\bar\omega}$ de $X^*$ correspond à une orientation $\bar\omega_{\rho}$ de $D_{\rho}$.}
Alors les \unsure{arcs sort.} de $\rho$ de $X^*$ correspondent aux \deleted{\unsure{somm.}} éléments \inserted{$(s,\omega)$} de $S_{\rho}$, \uline{munis} d'une orientation; \inserted{soit $\vec a_{s,\omega}$ l'arc}.
A un tel couple $(s,\omega)$, correspond la pos. semi-stble $(D_{\rho},s,\omega)$ \deleted{\unsure{orientée}\ \unsure{qui}} ,
\deleted{\unsure{qui provient}\ \unsure{définit l'arc}\ \unsure{dans le voisin}\ \unsure{germes} $(\rho,\unsure{\bar\omega})$ \unsure{correspond. à une} p.r. stble}
à l'arête $a_{s,\omega}$ sous-jacente : $\vec a_{s,\omega}$; soit $\vec b_{s,\omega}$ l'arête duale, orientée de façon que $(\vec a_{s,\omega},\vec b_{s,\omega})$ soit direct pour $\unsure{\bar\omega}$, donc $\vec b_{s,\omega}$ va d'une p.r. \uline{stable} vers une autre -- c'est le passage de la \unsure{générisation} de $D_{s,\omega}$ en $s$ dite ``\unsure{gauche}'' vers la gén. \unsure{vue|dite} \deleted{\unsure{gauche}}\inserted{\uline{droite}}.
'''
s+=start()+comment('Left local oriented crossing.')
s+=paths('k','1.43,6.94 3.01,6.79 7.49,6.33;2.25,5.84 3.01,6.79 4.11,8.24;3.38,5.6 3.01,6.79 2.32,8.83')
s+=path('w,dashed,->','1.43,7.08 3.01,6.79 5.83,6.41')+paths('green!40!black,dashed','1.54,7.25 2.56,7.22 3.01,6.79 4.19,6.55;1.92,6.84 2.49,6.64 3.01,6.79')
s+=path('k,->','2.73,6.64 2.8,6.48 3.12,6.49')+path('k,->','6.36,6.72 6.91,6.69')+dots('k','3.01,6.79','.07')
s+=labels([('3.13,6.33',r'\omega'),('2.98,7.1','s'),('6.33,6.08',r'D_{\unsure{\rho},s,\omega}'),('8.05,6.44',r'D_\rho'),('6.66,7.18',r'\bar\omega_{D_\rho}')])
s+=comment('Central local arrow with orientation and faint construction.')
s+=paths('p','13.81,6.64 14.81,5.55 16.02,4.38;13.91,5.19 15.79,5.83;14.79,4.65 14.81,5.55 14.9,6.73;15.68,4.78 15.35,6.64;14.02,6.46 15.35,6.64')
s+=path('k,->,line width=1.6pt','14.81,5.55 16.19,4.45')+path('k,->','15.73,5.32 15.23,4.78')
s+=path('k,->','15.15,5.61 15.12,5.29 14.84,5.32')+paths('k,dashed,->','15.12,4.77 14.39,4.96;14.39,4.96 14.04,5.89;14.14,6.02 14.48,6.53')
s+=labels([('16.94,4.35',r'\vec a_{s,\omega}=\vec a'),('15.52,5.52',r'\bar\omega=\bar\omega_\rho'),('14.93,6.05',r'\rho=\unsure{\rho_D}')])
s+=comment('Oriented edge a_L between two face regions.')
s+=paths('p','18.08,3.91 20.17,4.17;18.41,3.68 18.46,5.02 18.27,5.81;18.07,5.23 18.76,5.94 19.19,6.81 19.5,8.36;19.65,3.87 20.33,4.62 20.77,4.82 21.94,5.12;18.21,7.2 19.03,6.4 20.77,4.82 21.61,4.32;19.54,7.54 20.77,6.44 21.76,5.36;20.2,7.78 21.2,7.83 21.78,8.1;21.77,8.62 22.11,7.57 22.64,6.8;21.78,6.36 22.11,6.43 22.41,6.54;22.11,6.18 22.11,6.43 22.17,6.88 22.66,7.29')
s+=paths('k','19.03,6.4 20.77,4.82;19.03,6.4 19.11,7.54;19.03,6.4 20.07,7.21 20.61,7.87;17.4,6.51 18.44,6.45')
s+=paths('k,dashed','20.69,3.96 20.77,4.82 21.94,5.12;19.5,7.14 19.88,8.02 20.26,8.5')
s+=path('k,->','19.03,6.4 19.93,5.69')+path('k,->','20.29,5.52 20.42,5.21 20.12,5.02')
s+=labels([('19.05,4.48',r'F_{\Delta\prime}'),('20.74,6.43',r'F_{\Delta}'),('19.41,5.4','a=a_L'),('20.62,5.51',r'\bar\omega_a'),('20.01,6.07',r'\omega_a')])
s+=comment('Oriented L with point s and local rotation omega_s.')
s+=paths('p','18.05,10.04 18.62,10.91 19.23,11.69;19.04,10.12 18.62,10.91 18.01,11.93')
s+=path('k,->','16.39,11.46 18.05,11.16 18.62,10.91 21.09,10.17 23.04,9.54')
s+=path('k,->','19.1,10.64 18.82,10.49 18.49,10.54')+dots('k','18.62,10.91','.1')+labels([('19.16,10.34',r'\omega_s'),('21.55,9.84','L'),('21.78,10.32',r'\bar\omega_L')])+end()
s+=r'''
La difficulté conceptuelle n'est pas dans l'étude locale de $X^*$ en \unsure{un vois.} de $\rho$, en termes de $D$, mais dans l'étude locale de $X^*$ au voisinage d'une face, correspondant à une p.r. stble $\Delta$, mais dans la description de $X^*$ au voisinage d'une \uline{arête} \inserted{$a_L$}, correspondant à une position r. semi-stble donnée, soit $L$.
Il n'y a pas non plus de difficulté : \unsure{saisir} les faces incidentes \deleted{\unsure{la face} $F$} à $a_L$, et leur circuit des arêtes (contenant $a_L$), mais par contre : saisir les deux \inserted{(?)} sommets incidents à $a_L$.

Notons que la donnée d'une orientation \unsure{superficielle} le long de $a_L$ revient à celle d'une orientation de $L$, celle d'une orientation de $a_L$ à celle d'une orientation superficielle en le \deleted{point} sommet $s\in S_L$, donc une \uline{rive} de $L$\deleted{$\unsure{\{s\}}$} en $s$ revient à celle d'une rive de $a$ i.e. d'une des faces incidentes \unsure{à a}.

Il s'agirait donc, en termes de $(L,\omega_s)$, de reconstruire le sommet extrémité de $\vec a=(a,\omega_a)$, \deleted{\unsure{dans des termes}} si possible en termes d'une position relative critique, déduite de $L$ par ``blocage'' autour de $s$, dans le sens indiqué par l'orientation $\omega_s$ en $\uline{s}$, i.e. par la rive correspondante de $L-\{s\}$.
L'ennui, c'est qu'il y a plusieurs choix naturels qui viennent à l'esprit, et qu'il n'est pas sûr qu'aucun de ces choix ne marche!

{\ttfamily\unsure{//** CRAY6 0013 - O}}
'''
# The faint, partly overwritten printed character banner is manually read as CRAY6.
banner=[
' CCCCCCCCCC   RRRRRRRRRRR   AAAAAAAAAA   YY        YY   6666666666',
'CCCCCCCCCCCC  RRRRRRRRRRRR AAAAAAAAAAAA  YY        YY  666666666666',
'CC        CC  RR        RR AA        AA  YY      YY   66        66',
'CC            RR        RR AA        AA   YY    YY    66',
'CC            RR        RR AA        AA    YY  YY     66',
'CC            RRRRRRRRRRRR AAAAAAAAAAAA     YYYY      66666666666',
'CC            RRRRRRRRRRR  AAAAAAAAAAAA      YY       666666666666',
'CC            RR    RR     AA        AA      YY       66        66',
'CC            RR     RR    AA        AA      YY       66        66',
'CC        CC  RR      RR   AA        AA      YY       66        66',
'CCCCCCCCCCCC  RR       RR  AA        AA      YY       666666666666',
' CCCCCCCCCC   RR        RR AA        AA      YY        6666666666']
s+=r'\unsure{{\scriptsize\begin{tabular}{l}'+'\n'
for row in banner:s+=r'\texttt{'+row.replace(' ',r'\ ')+'}'+r'\\'+'\n'
s+=r'\end{tabular}}}'+'\n'
for i in range(6):s+=r'{\ttfamily ****A\quad END\quad JOB\quad13\quad CRAY6\quad- CRAY OUTPUT -\quad ROOM\quad3.24.18 PM 19 AUG 82\quad R6.PR1\quad SYS JES2\quad JOB\quad13\quad END\quad A****}'+'\\\\\n'
s+=r'\margin{150}'+'\n'
(root/'pages/MPL_154_127-176_154_scan151.tex').write_text(s)
commit(151,[('text','top left','Sigma=(X,Sigma); surface cellulaire des positions relatives'),('text','upper left','Soit un sommet rho de X*'),('insertion','above and between upper lines','rho; orientation of X*; (s,omega); soit a vector arc'),('deletion','upper text and central multiline cancellation','Delta; somm.; oriented phrase and cancelled arc construction'),('text','left middle','A un tel couple; arête duale; générisation gauche/droite'),('drawing','upper left','D_rho, s, omega; coloured dashed arcs'),('drawing','upper centre','rho; vector a; omega orientation'),('drawing','upper right centre','a_L; F_Delta and F_Delta prime'),('drawing','middle right','L; omega_L; omega_s'),('text','lower left continuing top right','La difficulté conceptuelle; deux (?) sommets incidents'),('insertion','lower left and top right','a_L; (?)'),('deletion','lower left','la face F'),('text','right column upper','Notons que la donnée; orientation superficielle; rive'),('deletion','right column','point; overwritten expression after L'),('text','right column lower','Il s’agirait donc; blocage; plusieurs choix naturels'),('deletion','right column lower','dans des termes'),('text','reverse printed heading and middle banner','CRAY6 0013 O; CRAY6 character banner'),('text','six reverse printed rows','END JOB 13 CRAY6; 3.24.18 PM 19 AUG 82'),('margin note','bottom left','150')],sheet_kind='reused_typed',observations='Whole, both halves and six enlarged prose/deletion regions visually read, plus reflected printing. The dense cancelled passage after (D_rho,s,omega) is the least secure prose and is explicitly marked by word/phrase doubts. The inserted orientation sentence is kept as an insertion rather than silently merged with adjacent live lines. Both occurrences of mais in the lower-left paragraph are retained as read, even where the discourse is surprising. The two endpoint question mark, final uncertainty about choices, and gauche/droite cancellation are preserved. CRAY6 banner is collectively unsure because manuscript strokes cover individual printed characters. No research interpretation used.')
