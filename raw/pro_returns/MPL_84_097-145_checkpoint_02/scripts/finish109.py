from record import finish
finish(109,[
('text','top','La formule ci-dessus pour'),
('deletion','top above first display','d’où'),
('display','top','α(n(x))=x barx'),
('text','upper','donne, si on fait x=y+z'),
('display','upper','α(n(y+z))=(y+z)overline(y+z)=y bary+z barz+y barz+z bary'),
('deletion','upper in expansion','α(x barx)'),
('insertion','under n(y+z)','n(y)+n(z)+φn(y,z)'),
('insertion','under diagonal terms','α(n(y)); α(n(z))'),
('insertion','under z bary','overline(y barz)'),
('insertion','under last two terms','τ(y barz)'),
('text','middle','donc'),
('display','middle','α(φn(y,z))=τ(y barz), i.e. α(t(y barz))'),
('deletion','middle before τ','αt'),
('text','middle','donc si α est injectif'),
('display','middle boxed','φn(y,z)=t(y barz)'),
('text','middle','i.e. la formule d’additivité pour n'),
('display','middle boxed','n(y+z)=n(y)+n(z)+t(y barz)'),
('insertion','under cross term','t(bary z)'),
('text','middle right','car t(x)=t(barx)'),
('text','lower middle','Ceci posé, on veut'),
('text','lower middle 3°','la formule précédente est vraie'),
('text','lower 4°','Une formule facultative'),
('deletion','lower rank k','2'),
('deletion','lower after et','alors on supposera'),
('text','lower parenthesis','N.B. donc k0→A injectif'),
('display','bottom boxed braced','Tr_k/k0(t(x))=Tr_A/k0(x); N_k/k0(n(x))=N_A/k0(x)'),
('margin note','bottom right first','identité entre applic. linéaires A→k0'),
('margin note','bottom right second','identité de (2n)-formes'),
('text','bottom left','108')
],r'''- The promised polarization calculation derives αφn(y,z)=αt(ybarz), and under α injective obtains φn(y,z)=t(ybarz). Condition 3° explicitly requires the latter formula “sans supposer α injectif”, so its general validity is axiomatized rather than inferred by cancelling a noninjective α.
- Condition 4° is called “Une formule facultative”: for k locally free of rank n over k0 and A locally free of rank 2n over k0, require trace/norm transitivity. Margin classifies the first as equality of linear maps A→k0 and the second as equality of degree-2n forms; n is the enumeration parameter.
- Own lead: compare the optional transitivity axiom with polynomial-law norms versus identities merely on elements; the page’s wording “identité de (2n)-formes” is stronger evidence for form identities than for pointwise tests only. Confidence medium, pending later definition and context.''')
