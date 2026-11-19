import sys
sys.path.insert(0,'out/scripts');from work import commit
L=[dict(place='faint upper-right mark',c='unsure 4/V',h='absent',final='unsure 4/V retained',ink='margin: two reddish vertical/oblique traces meet near a faint transverse mark. Shape and colour do not securely distinguish 4, V, or an incidental mark; the C doubt is retained rather than promoted to a confident reading.',kind='other',confidence='low',against_c=False,against_h=False,marked_in_H='not applicable')]
I=[]
def i(k,p,t,h='typewriter'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','upper right','1.4.68')
i('margin note','far upper right','unsure 4/V','unnamed hand; attribution uncertain')
i('text','upper left heading','underlined D I V E R S')
i('text','second heading','underlined CANDIDATS')
i('text','first candidate bullet','. TAFT')
i('text','second candidate bullet','. Scientifiques Russes')
i('text','request line','- A la demande de M. MICHEL, revoir les dossiers de :')
i('text','six separate names','DASGUPTA; OKABAYASHI; ROCKMORE; SHIMA; SOMMER; YOKOO')
i('diagram','lower suggestion in two aligned lines','- Suggestion M. MICHEL : ( polonais / ) indiens')
commit(15,136,dict(changes=L,inventory=I,sheet_kind='list',hand='typewriter',observations='Whole image and both halves personally viewed before C; H has no text. Every line and name reread in enlarged crops, including literal initial A without accent and separate opening/closing parenthesis on successive rows. Date and both underlines checked. Isolated tiny dark flecks away from baselines inspected in dots crop; not securely textual punctuation and not added. Pencil archive135 remains comment only. No context consulted.'))
