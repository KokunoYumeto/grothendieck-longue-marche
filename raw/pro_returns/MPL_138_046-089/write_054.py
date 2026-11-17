from workflow import save_page
save_page(54,r'''
\scanpage{54}
% archive foliation: 53
\diagram{\begin{tikzcd}
\widetilde X_2\arrow[dr]&{}\arrow[l,very thick]&\\
&X_4&\unsure{X_8}\arrow[l]
\end{tikzcd}}

% Printed letterhead below is upside down relative to the handwritten diagram.
UNIVERSITÉ DES SCIENCES

ET TECHNIQUES DU LANGUEDOC

\rule{1cm}{.4pt}

INSTITUT DE MATHEMATIQUES

Place Eugène Bataillon

34060 MONTPELLIER CEDEX

\rule{1cm}{.4pt}

Montpellier, le
''',[
('diagram','upper left','X tilde_2; X_4; X_8; arrow from blank'),
('text','upside-down lower right letterhead','UNIVERSITÉ DES SCIENCES ET TECHNIQUES DU LANGUEDOC'),
('text','upside-down lower right institute and address','INSTITUT DE MATHEMATIQUES; Place Eugène Bataillon; 34060 MONTPELLIER CEDEX'),
('text','upside-down lower left','Montpellier, le')],sheet_kind='reused_typed')
