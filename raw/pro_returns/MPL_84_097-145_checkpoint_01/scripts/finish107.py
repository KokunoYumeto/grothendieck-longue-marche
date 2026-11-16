from record import finish
finish(107,[
('text','top','Or le deuxième est'),
('display','top','ξ0 barξ0 ξ1 barξ1'),
('insertion','under barred conjugates','barξ0=ξ3; barξ1=ξ2'),
('display','upper','ξ0 barξ0 = N_A1⊗A2/A(ξ0)'),
('display','upper','ξ1 barξ1 = N(ξ1) = overline N(ξ0)'),
('insertion','under norm argument','ξ1=σ1(ξ0)'),
('text','upper middle','donc N=N_A1⊗A2/A(ξ0), on trouve'),
('deletion','upper middle','soit'),
('display','upper middle','N barN=N_A/O(N) OK'),
('drawing','separator','short right-pointing arrow'),
('text','middle','On va axiomatiser la situation'),
('deletion','middle upper right','A1 A1,O'),
('insertion','middle before d’une','et'),
('text','middle lower','Mais on ne suppose ni que A soit'),
('deletion','middle lower before /k','sur'),
('insertion','middle lower above /k','ni même plat'),
('display','middle lower','α:k→A; λ—λ.1A'),
('text','lower','soit injective. Au lieu de cela'),
('display','lower','t_A/k=t:A→k; n_A/k=n:A→k'),
('text','lower','satisfaisant les conditions suivantes'),
('text','lower','circled a: t est linéaire'),
('insertion','lower middle under comme','t(x)=φn(x,1)'),
('text','lower right','φn forme bil. ass. à n'),
('text','bottom left','donc on a'),
('deletion','bottom before boxed formula','c’est'),
('display','bottom boxed','n(x+λ1A)=n(x)+λ²n(1)+λt(x)'),
('insertion','bottom under n(1)','1 cf. ci-dessous b)'),
('text','bottom left','106')
],r'''- Norm transitivity argument concludes by pairing the four conjugates into ξ0 barξ0 and ξ1 barξ1, using N(σ1ξ)=overline N(ξ), and “OK”. It writes ξbarξ=N(ξ) without i; scope of this identification should be checked against the earlier warning that i need not be injective.
- New axiomatization: a k-algebra behaving as a quadratic algebra but A need not be locally free, not even flat, and α:k→A need not inject. Relative trace t and norm n replace rank assumptions.
- Enumeration starts circled a: t linear, n quadratic, t(x)=φn(x,1); n(x+λ1)=n(x)+λ²n(1)+λt(x), with n(1)=1 referred forward to b. Keep a link to continuation 108 and later retractions or strengthening.''')
