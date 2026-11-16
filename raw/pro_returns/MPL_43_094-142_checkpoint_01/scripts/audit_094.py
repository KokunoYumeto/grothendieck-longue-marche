from audit_work import audit_page
changes=[(r'\unsure{presque} compacts',r'\unsure{flasques} compacts'),(r'morphismes de transition \unsure{finis}',r'morphismes de transition \unsure{affines|finis}'),(r'\mathcal T_S$ !}',r'''\mathcal T_S$ !}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw(0,4.5)..controls(.9,5.1)and(.7,3.7)..(.9,3.1)..controls(1.4,1.1)and(.7,.8)..(-.1,0);
\end{tikzpicture}}''')]
audit_page(94,changes,notes='Re-read whole page and enlarged first definition and transition adjective. First adjective now flasques, with doubt; the transition adjective is affines/finis, unresolved. Added the visible long enclosure stroke around the left margin. Other formulas, cancellation and insertion checked line by line.',extra_elements=[('drawing','around left marginal note','long curved enclosure stroke')])
