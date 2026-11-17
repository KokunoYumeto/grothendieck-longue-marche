from record import finish
finish(106,[
('text','top','ayant les propriétés suivantes'),
('display','upper','a) N(x1⊗x2)=NA1(x1)NA2(x2)'),
('display','upper','b) φN(ξ,η)=Tr(ξ barη)'),
('deletion','upper middle','On aura de'),
('text','upper middle','i.e.'),
('display','middle','N(ξ+η)=N(ξ)+N(η)+Tr(ξ barη)'),
('deletion','middle before N','φ'),
('text','middle','On, pour ∀ξ∈A1⊗A2'),
('deletion','middle','aura alors'),
('display','middle boxed','i(N(ξ))=ξ barξ'),
('display','middle boxed with left brace','N(σ1⊗id(ξ))=N(id⊗σ2(ξ))=overline N(ξ); N(barξ)=N(ξ)'),
('margin note','left diagonal boxed','Noter aussi N(iη)=η²'),
('text','lower middle','De plus, on a'),
('display','lower middle boxed','N_A/O(N_A1⊗A2/A(ξ))=N_A1⊗A2/O(ξ)'),
('text','lower middle','sans compter la formule plus bénigne'),
('display','lower middle boxed','Tr_A/O(Tr_A1⊗A2/A(ξ))=Tr_A1⊗A2/O(ξ)'),
('text','lower','Prouvons p.ex. la première des deux dernières. La'),
('deletion','lower left','deuxième'),
('text','lower','Posons'),
('display','lower','σ1=σA1⊗idA2; σ2=idA1⊗σ2; σ3=σ1σ2'),
('deletion','lower left above ξ','ξ'),
('deletion','lower left','Soit'),
('display','lower','ξ=ξ0∈A'),
('deletion','lower','on doit vérifier'),
('insertion','lower','ξi=σi(ξ)'),
('text','bottom','on constate qu’on ait'),
('display','bottom','N_A1⊗A2/O(ξ)=ξ0 ξ1 ξ2 ξ3 with grouping brackets'),
('text','bottom left','105')
],r'''- Two defining clauses a), b) continue the norm proposition from 105: values on pure tensors and polarization by Tr(ξ barη). These determine the four diagonal and six off-diagonal coefficients in a four-generator basis, although only a,b are explicitly numbered here.
- Further identities: iNξ=ξbarξ, equivariance under the two factor involutions, N(barξ)=Nξ, marginal N(iη)=η², transitivity of norm and trace. “Prouvons p.ex. la première des deux dernières” begins a proof of norm transitivity by the four conjugates ξ0,ξ1,ξ2,ξ3, continued on 107.
- Reading issues to keep: the second id subscript in the equivariance display looks A2, where A1 might be expected; the assignment σ2=id_A1⊗σ2 is circular on the page. No mathematical correction is made.''')
