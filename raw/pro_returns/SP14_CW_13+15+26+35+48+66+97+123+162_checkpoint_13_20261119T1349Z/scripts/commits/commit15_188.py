import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\handwritten{\unsure{\mathrm{m}}}',r'\handwritten{\mathrm{m}}')]
L=[dict(place='first line relation between n and n_o',c=r'\handwritten{\unsure{\mathrm{m}}}',h='absent',final=r'\handwritten{\mathrm{m}}',ink='m, head: three short downward strokes joined by two rounded humps form a small m. There is no horizontal equality bar or angled greater-than stroke. Read the visible m literally, without replacing it by the inequalities later on the sheet.',confidence='medium',kind='misread symbol or index',against_c=True,against_h=False,marked_in_H='not applicable',consequential='The opening relation is literally an m-shaped mark, not silently normalized to greater-than-or-equal.'),dict(place='first n subscript',c='unsure o/0',h='absent',final='unsure o/0 retained',ink='n_o: one round closed lower loop, without a distinguishing stroke for letter o versus zero. Repeated later loops retain the primary o.',confidence='low',kind='other',against_c=False,against_h=False,marked_in_H='not applicable'),dict(place='small marks left of lower displays and above n',c='no additional notation',h='absent',final='no additional notation retained',ink='margin1, margin2, margin3, n_dot: short black/grey crescents and points have pale torn-edge halos, unlike the violet strokes of the nearby formulas. They are treated as physical sheet/reproduction marks, not as marginal letters or a dot accent. This classification is medium confidence.',confidence='medium',kind='other',against_c=False,against_h=False,marked_in_H='not applicable')]
I=[]
def i(k,p,t,h):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','upper right','70','unnamed hand')
i('text','opening continuation','that there exists n_o(K) such that at n m n_o(K)','typewriter')
i('insertion','opening two n subscripts','o/0 and later o','unnamed hand')
i('insertion','opening relation','small m','unnamed hand')
i('display','first formula','H^i(V,K[nE])=0; i=1,2,...','unnamed hand')
i('text','before sequence','From the exact sequence','typewriter')
i('display','exact sequence','H^i(V,O_V(-E_varphi)[nE]) -> H^i(V,O_V[nE]) -> H^i(V,K[nE])','unnamed hand')
i('text','before first inequality','at n >= n_o(K), i=1,2,... we obtain:','typewriter')
i('insertion','n subscript before we obtain','o','unnamed hand')
i('display','first inequality','dim H^i(V,O_V[nE]) <= dim H^i(V,O_V(-E_varphi)[nE]).','unnamed hand')
i('text','middle connector','Since','typewriter')
i('display','first isomorphism','O_V(-E_varphi) cong O_V[-E],','unnamed hand')
i('text','middle connector','then','typewriter')
i('display','isomorphism chain','O_V(-E_varphi)[nE] cong O_V[-E][nE] cong O_V[(n-1)E].','unnamed hand')
i('text','before last inequality','Therefore, at n >= n_o(K), i=1,2,...','typewriter')
i('insertion','n subscript after Therefore','o','unnamed hand')
i('display','last inequality','dim H^i(V,O_V[nE]) <= dim H^i(V,O_V[[n-1]E]).','unnamed hand')
i('text','last continuation','Evidently, there exists such n prime that, at n >= n prime','typewriter')
commit(15,188,dict(replace=R,changes=L,inventory=I,sheet_kind='typescript',hand='typewriter and unnamed hand',observations='Whole and both halves personally viewed before C; H absent. All seven prose blocks and six displays read in head/first/seq/obtain/since/then/therefore/last crops; all formula letters, exponents i, lower V, varphi, arrows, signs, brackets and punctuation checked. Three typed K impressions enlarged individually: single main stem/arms, ordinary K retained; all handwritten H/K/O single strokes, no semantic script substitution. varphi has left cup and right loop/descender. Congruence marks have tilde over two bars. Penultimate chain uses [(n-1)E] whereas last inequality visibly uses [[n-1]E]; retained exactly. Header70 hand, archive187 comment only. No deletions, handwritten margin text or watermark found. No context consulted or mathematical check claimed.'))
