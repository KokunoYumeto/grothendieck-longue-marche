# Scan 009 — reader source crosswalk

Text-only collation: 129 source issues (A41/B43/C45), 17 inline C doubts, four actual H ill marks, 26 current-context table rows, 63 countable physical places and 9 noncounted context/metadata registers.

Each physical comparison place counts at most once against C and once against H. Broad reader issues may map to several distinct letters or layout places, but no broad duplicate row is retained. Whole canceled phrases include their nested doubtful endings/articles. Doubt removal, refinement and reordering count as changes. Equivalent TeX macros or ordinary spacing do not. H doubt flags follow the actual four ill marks, not nearby reader paraphrases. Noncounted context/metadata registers have no discrepancy counts.

All H cells below are verbatim excerpts from the supplied H.tex. Omission/placement explanations are separate notes. A missing standalone issue is filled from that reader's complete returned text and checked log with explicit provenance, never from the other readers.

## Reader differences requiring main attention

- Plus cancellation: A/C select live plus; B retains both states.
- The brace has a long rising return in B/C's code; A's log observes it but A's code retains the ordinary underbrace.
- B introduces prés/près; A/C retain près. A resolves description; B/C retain description/descripteur.
- A27 retains n-prime / n^{4} / bare n for the second paired-family index; B/C choose n-prime.
- B35 alone draws a separate point above-right of the later equality. A/C's text omits a separate point, without an explicit visual denial.
- The canceled stability word has three reordered alternatives in A, four in B, and C's original three in C. A/B select entre.; C retains entre./entre.

## Physical comparison places

| Key | Place | Witness C | Witness H (verbatim) | Reader A | Reader B | Reader C | Source issues |
|---|---|---|---|---|---|---|---|
| folio | Own folio at top centre | \mspage{2} | \page{8}\note{sa page 2} | 2; own handwritten folio | 2; own handwritten folio | 2; own handwritten folio | A: complete text/log; B: complete text/log; C: complete text/log |
| opening_old_x | First membership, older x under xi | \deleted{x}\xi | \xi \in I_n(n') | \deleted{x}\xi | \deleted{x}\xi | \deleted{x}\xi | A: A01; B: B01; C: 01 |
| opening_J1 | First membership, J_n(n-prime) | J_n(n') | I_n(n') | J_n(n') | J_n(n') | J_n(n') | A: A01; B: B02; C: 02 |
| opening_clause_placement | Second i.e. clause, baseline placement | i.e. \(x\in J_n,\ \tau_n(x)=n'\) | \add{i.e.\ $x \in I_n$, $\tau_n(x) = n'$} | Second i.e. clause on the original baseline; no insertion leader | Second i.e. clause on the original baseline; no insertion leader | Second i.e. clause on the original baseline; no insertion leader | A: A02; B: B03; C: 03 |
| opening_J2 | Second i.e. clause, object after x in | x\in J_n | x \in I_n | J_n | J_n | J_n | A: A02; B: B02; C: 02 |
| opening_notation | Opening two i.e. abbreviations and xi/x/tau notation | i.e. on a, pour \(\deleted{x}\xi\in J_n(n')\) i.e. \(x\in J_n,\ \tau_n(x)=n'\) | i.e.\ on a, pour $\xi \in I_n(n')$ \add{i.e.\ $x \in I_n$, $\tau_n(x) = n'$} | Both top i.e. stops; xi first, ordinary x in the following membership and tau_n(x); n-prime | Both top i.e. stops; xi first, ordinary x in the following membership and tau_n(x); n-prime | Both top i.e. stops; xi first, ordinary x in the following membership and tau_n(x); n-prime | A: complete text/log; B: complete text/log; C: complete text/log |
| evaluation | Opening evaluation identity | u_\xi(d_{n'})=\xi . | u_\xi(d_{n'}) = \xi. | u_\xi(d_{n'})=\xi . | u_\xi(d_{n'})=\xi . | u_\xi(d_{n'})=\xi . | A: complete text/log; B: complete text/log; C: complete text/log |
| De | Canceled opening word De | \deleted{De} | De plus, | \deleted{De} | \deleted{De} | \deleted{De} | A: A03; B: B04; C: 04 |
| plus | Opening plus and cancellation status | \unsure{plus,&#124;\deleted{plus,}} | plus, | plus, | \unsure{plus,&#124;\deleted{plus,}} | plus, | A: A03; B: B05; C: 05 |
| fword_encore | Uncertain f-word and readable encore before on a | \unsure{fort&#124;faut&#124;fut} encore, | De plus, \ill{} on a : | \unsure{fort&#124;faut&#124;fut} encore, | \unsure{fort&#124;faut&#124;fut} encore, | \unsure{fort&#124;faut&#124;fut} encore, | A: A04; B: B06; C: 06 |
| upper_brace | Underbrace at on a and attached lower insertion | \(\underbrace{\text{on a :}}\) \inserted{\(u_\xi\) induit un \unsure{isom&#124;iso}} | on a : $u_\xi$ induit un | Ordinary underbrace retained in TeX; log observes a long rising right return; attached lower insertion | Custom trace of notched brace with long rising right return and lower insertion | Custom trace of notched brace with long rising right return and lower insertion | A: A05; B: B09; C: 07 |
| isom | Last word of upper inserted phrase | \unsure{isom&#124;iso} | isomorphisme | isom; no final point | isom; no final point | isom; no final point | A: A06; B: B07; C: 08 |
| phantom_deleted | Gap between un and isom | un \unsure{isom&#124;iso} | un \struck{\ill{}} isomorphisme | No independent canceled word between un and isom | No independent canceled word between un and isom | No independent canceled word between un and isom | A: A07; B: B08; C: 08 |
| upper_source_J | Upper isomorphism, source object | J_{n'}\xrightarrow | I_{n'} \overset{\sim} | J_{n'} | J_{n'} | J_{n'} | A: A08; B: B10; C: 09 |
| upper_label | Upper isomorphism, u_xi above tilde | \xrightarrow{\overset{u_\xi}{\sim}} | \overset{\sim}{\longrightarrow} | u_xi above tilde above right-pointing arrow | u_xi above tilde above right-pointing arrow | u_xi above tilde above right-pointing arrow | A: A08; B: B10; C: 09 |
| upper_target_J | Upper isomorphism, parenthesized target object | (J_n)_{\leq\xi} | (I_n)_{\leq \xi} | (J_n)_{\leq\xi} | (J_n)_{\leq\xi} | (J_n)_{\leq\xi} | A: A08; B: B10; C: 09 |
| upper_stop | Right of upper isomorphism target | (J_n)_{\leq\xi}\) | (I_n)_{\leq \xi}$. | No terminal point | No terminal point | No terminal point | A: A08; B: B10; C: 09 |
| lorsque_n | Lorsque, first n and its prime | \unsure{n'&#124;n}=n | n' = n | n'=n | n'=n | n'=n | A: A09; B: B11; C: 10 |
| lorsque_J | Lorsque, singleton object J_{n,n} | J_{n,n}=\{d_n\} | I_{n,n} = \{d_n\} | J_{n,n}=\{d_n\} | J_{n,n}=\{d_n\} | J_{n,n}=\{d_n\} | A: A10; B: B11; C: 11 |
| identity_J | Identity display, target of id | \mathrm{id}_{J_n} | \mathrm{id}_{I_n} | \mathrm{id}_{J_n} | \mathrm{id}_{J_n} | \mathrm{id}_{J_n} | A: A11; B: B12; C: 12 |
| families_J | La connaissance, first indexed family | (J_n)_{n\in\mathbb N} | (I_n)_{n \in \mathbb{N}} | (J_n)_{n\in\mathbb N} | (J_n)_{n\in\mathbb N} | (J_n)_{n\in\mathbb N} | A: A12; B: B13; C: 13 |
| families_register | La connaissance, N and tau family | \mathbb N,\ (J_n)_{n\in\mathbb N},\ (\tau_n)_{n\in\mathbb N} | \mathbb{N}$, $(I_n)_{n \in \mathbb{N}}$,<br>$(\tau_n)_{n \in \mathbb{N}}$ | \mathbb N and (\tau_n)_{n\in\mathbb N}; doubled/barred N | \mathbb N and (\tau_n)_{n\in\mathbb N}; doubled/barred N | \mathbb N and (\tau_n)_{n\in\mathbb N}; doubled/barred N | A: complete text/log; B: complete text/log; C: complete text/log |
| rho | Map-family letter rho | \rho_{n,n'} | \varphi_{n,n'} | \rho_{n,n'} | \rho_{n,n'} | \rho_{n,n'} | A: A13; B: B14; C: 14 |
| family_pair_first | Map-family indexing pair, first member | (n',\deleted{\unsure{n'&#124;m}}n) | (n,n') \in \mathbb{N} | n' as first pair member | n' as first pair member | n' as first pair member | A: A14; B: B14; C: 14 |
| family_pair_second | Map-family indexing pair, overwritten second member | \deleted{\unsure{n'&#124;m}}n | (n,n') \in \mathbb{N} | \deleted{\unsure{n'&#124;m}}n | \deleted{\unsure{n'&#124;m}}n | \deleted{\unsure{n'&#124;m}}n | A: A14; B: B14; C: 15 |
| category_replacement | Raised la catégorie above reconstruction cancellation | \inserted{la catégorie} | la catégorie | \inserted{la catégorie}; following M and à live | \inserted{la catégorie}; following M and à live | \inserted{la catégorie}; following M and à live | A: A17; B: B17; C: 18 |
| cancelled_approx | First long canceled reconstruction phrase | \deleted{à peu de \unsure{chose&#124;choses} près} | \struck{\ill{}} la catégorie | \deleted{à peu de \unsure{chose&#124;choses} près} | \deleted{à peu de \unsure{chose&#124;choses} près} | \deleted{à peu de \unsure{chose&#124;choses} près} | A: A15; B: B15; C: 16 |
| cancelled_essential | Second long canceled reconstruction phrase | \deleted{essentiellement \unsure{la&#124;le} sous-catégorie pleine} | \struck{\ill{}} la catégorie | \deleted{essentiellement \unsure{la&#124;le} sous-catégorie pleine} | \deleted{essentiellement \unsure{la&#124;le} sous-catégorie pleine} | \deleted{essentiellement \unsure{la&#124;le} sous-catégorie pleine} | A: A16; B: B16; C: 17 |
| cancelled_il | Short canceled fragment before équiv | \deleted{\unsure{il&#124;à}} | \struck{l'équi} | \deleted{il} | \deleted{il} | \deleted{il} | A: A18; B: B18; C: 19 |
| equiv | Live abbreviation équiv | \unsure{équiv&#124;équiva} | équivalence | équiv | équiv | équiv | A: A19; B: B19; C: 20 |
| pres_accent | Accent on près after équiv | près, il manque | près ; il manque | près | \unsure{prés&#124;près} | près | A: A20; B: B20; C: 21 |
| pres_stop | Punctuation after près | près, il manque | près ; il manque | Comma after près | Comma after près | Comma after près | A: A20; B: B20; C: 21 |
| condition_insertion | Raised condition replacing old noun | \inserted{condition} | \add{condition} | \inserted{condition} | \inserted{condition} | \inserted{condition} | A: A21; B: B21; C: 22 |
| description | Canceled noun beneath condition | \deleted{\unsure{description&#124;descripteur}} | \struck{\ill{}} \add{condition} | \deleted{description} | \deleted{\unsure{description&#124;descripteur}} | \deleted{\unsure{description&#124;descripteur}} | A: A21; B: B21; C: 22 |
| composer | Verb following pour | pour composer | pour comprendre | pour composer | pour composer | pour composer | A: A22; B: B22; C: 23 |
| hom_1 | First hom abbreviation | les hom | les homs. | hom without s or stop | hom without s or stop | hom without s or stop | A: A23; B: B23; C: 24 |
| standart | Quoted designation at right edge | ``\unsure{standart&#124;standard} | « standard » | ``standart; two opening ticks, terminal t, no closing ticks | ``standart; two opening ticks, terminal t, no closing ticks | ``standart; two opening ticks, terminal t, no closing ticks | A: A24; B: B23; C: 25 |
| middle_J | Object after entre les | entre les \(J_n\) | entre<br>les $I_n$ | J_n | J_n | J_n | A: A25; B: B24; C: 26 |
| middle_ie | Middle i.e before ceux | i.e ceux | i.e.\ ceux | i.e without final stop | i.e without final stop | i.e without final stop | A: A26; B: B24; C: 27 |
| paired_J_letter | Inline family before Donc, object letter | J_{n',\unsure{n&#124;n'}} | I_{n',n} | J | J | J | A: A27; B: B25; C: 28 |
| paired_J_second_index | Inline family before Donc, second index | J_{n',\unsure{n&#124;n'}} | I_{n',n} | J_{n',\unsure{n'&#124;n^{4}&#124;n}} | J_{n',n'} | J_{n',n'} | A: A27; B: B25; C: 28 |
| Donc | Canceled word before On considère | \deleted{\unsure{Donc&#124;Don}} | \struck{Donc} | \deleted{Donc} | \deleted{Donc} | \deleted{Donc} | A: A28; B: B26; C: 29 |
| situation | Clause introducing diagram | On considère une situation | On considère<br>leurs compositions | On considère une situation | On considère une situation | On considère une situation | A: A29; B: B27; C: 30 |
| diagram_eta_top | Diagram, eta above middle object | \& \& \eta \& \& \xi | \note{sur le feuillet, $y$ et $\xi$ sont écrits au-dessus de $I_{n'}$ et de<br>$I_n$ avec le signe d'appartenance, et la ligne $n'' \leq n' \leq n$ court<br>sous le diagramme} | \eta above middle object | \eta above middle object | \eta above middle object | A: A30; B: B29; C: 31, 33 |
| diagram_xi_top | Diagram, xi above right object | \& \& \eta \& \& \xi | \note{sur le feuillet, $y$ et $\xi$ sont écrits au-dessus de $I_{n'}$ et de<br>$I_n$ avec le signe d'appartenance, et la ligne $n'' \leq n' \leq n$ court<br>sous le diagramme} | \xi above right object | \xi above right object | \xi above right object | A: A30; B: complete text/log; C: 33 |
| diagram_membership_left | Diagram, turned membership over middle object | \rotatebox{90}{\(\in\)} | \note{sur le feuillet, $y$ et $\xi$ sont écrits au-dessus de $I_{n'}$ et de<br>$I_n$ avec le signe d'appartenance, et la ligne $n'' \leq n' \leq n$ court<br>sous le diagramme} | \rotatebox{-90}{\(\in\)}; downward-open arch | \rotatebox{-90}{\(\in\)}; downward-open arch | \rotatebox{-90}{\(\in\)}; downward-open arch | A: A31; B: B30; C: 33, 34 |
| diagram_membership_right | Diagram, turned membership over right object | \rotatebox{90}{\(\in\)} | \note{sur le feuillet, $y$ et $\xi$ sont écrits au-dessus de $I_{n'}$ et de<br>$I_n$ avec le signe d'appartenance, et la ligne $n'' \leq n' \leq n$ court<br>sous le diagramme} | \rotatebox{-90}{\(\in\)}; downward-open arch | \rotatebox{-90}{\(\in\)}; downward-open arch | \rotatebox{-90}{\(\in\)}; downward-open arch | A: A31; B: B30; C: 33, 34 |
| diagram_J_left | Diagram, left object | J_{n''} | I_{n''} | J_{n''} | J_{n''} | J_{n''} | A: A30; B: B28; C: 32 |
| diagram_eta_arrow | Diagram, first-arrow subscript eta | u^{n'}_{\eta} | u_y^{n'} | u^{n'}_{\eta} | u^{n'}_{\eta} | u^{n'}_{\eta} | A: A30; B: B29; C: 31 |
| diagram_J_middle | Diagram, middle object | J_{n'}\arrow | I_{n'} \arrow | J_{n'} | J_{n'} | J_{n'} | A: A30; B: B28; C: 32 |
| diagram_geometry | Diagram, unequal arrow spans and crossing second label | \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.8em,row sep=small]<br> \& \& \eta \& \& \xi\\[-.8em]<br> \& \& \rotatebox{90}{\(\in\)} \& \& \rotatebox{90}{\(\in\)}\\<br> J_{n''}\arrow[rr,"u^{n'}_{\eta}"] \& \& J_{n'}\arrow[rr,"u_\xi^n"] \& \& J_n\\<br> n'' \& \leq \& n' \& \leq \& n<br>\end{tikzcd}} | \begin{tikzcd}[column sep=small, row sep=small, nodes={font=\scriptsize}]<br>I_{n''} \arrow[r, "u_y^{n'}"] & I_{n'} \arrow[r, "u_\xi^n"] & I_n<br>\end{tikzcd} | Longer second interval; second label at pos=.35 with description,yshift=.8ex; 1.4em before order row | Longer second interval; first/second labels pos=.32/.27, second yshift=-.3em; .5em before order row | Longer second interval; second label yshift=-1.1ex; ordinary order-row spacing | A: A32; B: B32; C: 35 |
| diagram_J_right | Diagram, right object | \& \& J_n | & I_n | J_n | J_n | J_n | A: A30; B: B28; C: 32 |
| diagram_lower_row | Diagram, lower n-double-prime <= n-prime <= n row | n'' \& \leq \& n' \& \leq \& n | \note{sur le feuillet, $y$ et $\xi$ sont écrits au-dessus de $I_{n'}$ et de<br>$I_n$ avec le signe d'appartenance, et la ligne $n'' \leq n' \leq n$ court<br>sous le diagramme} | n'' <= n' <= n below corresponding objects; no separate canceled predecessor at middle n' | n'' <= n' <= n below corresponding objects; no separate canceled predecessor at middle n' | n'' <= n' <= n below corresponding objects; no separate canceled predecessor at middle n' | A: A32; B: B31; C: 33 |
| ondoit | Formula introduction beneath diagram | on doit avoir | on doit avoir | on doit avoir | on doit avoir | on doit avoir | A: complete text/log; B: complete text/log; C: complete text/log |
| composite_eta1 | Composite display, eta in left product | u_\xi^n\,u_\eta^{n'} | u_\xi^n\, u_y^{n'} | u_\eta^{n'} | u_\eta^{n'} | u_\eta^{n'} | A: A33; B: B34; C: 36 |
| old_zeta | Older subscript beneath result zeta | \deleted{\unsure{\xi&#124;a}}\zeta | u_\zeta^n | \deleted{\unsure{a&#124;\xi}}\zeta | \deleted{\unsure{a&#124;\xi}}\zeta | \deleted{\unsure{a&#124;\xi}}\zeta | A: A34; B: B33; C: 37 |
| composite_eta_arg | Evaluation display, eta argument | u_\xi^n(\eta) | u_\xi^n(y) | \eta | \eta | \eta | A: A33; B: B34; C: 36 |
| composite_point | Separate point above-right of later equality | u_\xi^n(\eta)= | u_\xi^n(y) = | No separate point encoded in returned equality; no standalone point issue | Separate small point traced above-right of equality, without a mathematical role | No separate point encoded in returned equality; no standalone point issue | A: complete text/log; B: B35; C: complete text/log |
| composite_eta2 | Evaluation display, eta in right product | (u_\xi^n\,u_\eta^{n'})(d_{n''}) | (u_\xi^n\, u_y^{n'})(d_{n''}) | u_\eta^{n'} | u_\eta^{n'} | u_\eta^{n'} | A: A33; B: B34; C: 36 |
| composition_register | Composite display, remaining xi/zeta/d and equality notation | \qquad\text{où}\quad \zeta=u_\xi^n(\eta)= | \qquad \text{où } \zeta = u_\xi^n(y) = | xi/zeta distinct; exponents n/n-prime; d_{n-double-prime}; parentheses and equality bars checked | xi/zeta distinct; exponents n/n-prime; d_{n-double-prime}; parentheses and equality bars checked | xi/zeta distinct; exponents n/n-prime; d_{n-double-prime}; parentheses and equality bars checked | A: complete text/log; B: complete text/log; C: complete text/log |
| cancel_stability | Canceled word before live stabilité | \deleted{\unsure{stabilité&#124;composition&#124;stabilis}} | \struck{compatibilité} | \deleted{\unsure{composition&#124;stabilité&#124;stabilis}} | \deleted{\unsure{composition&#124;stabilité&#124;compatibilité&#124;stabilis}} | \deleted{\unsure{stabilité&#124;composition&#124;stabilis}} | A: A35; B: B36; C: 38 |
| hom_lower | Lower prose, hom admissible endings | d'hom admissible | d'homs.\<br>admissibles | d'hom admissible; singular without abbreviation point | d'hom admissible; singular without abbreviation point | d'hom admissible; singular without abbreviation point | A: A36; B: B37; C: 39 |
| entre | Lower prose, entre and adjacent point | \unsure{entre&#124;entre.} | pour les | entre. | entre. | \unsure{entre.&#124;entre} | A: A37; B: B38; C: 40 |
| lower_J | Lower prose, J before par composition | \(J_n\) par composition. | $I_n$ par composition. | J_n | J_n | J_n | A: A38; B: B39; C: 41 |
| M0_replacement | Raised Soit M_0 introduction | \inserted{Soit \(M_0\) la catégorie définie par} | Soit $M_0$ la catégorie définie par | \inserted{Soit \(M_0\) la catégorie définie par} | \inserted{Soit \(M_0\) la catégorie définie par} | \inserted{Soit \(M_0\) la catégorie définie par} | A: A40; B: B41; C: 43 |
| cancel_final | Final canceled sentence ending | \deleted{Il est évident que la \unsure{catég&#124;caté}} | \struck{Il est évident que la cat.} | \deleted{Il est évident que la \unsure{catég&#124;caté}} | \deleted{Il est évident que la \unsure{catég&#124;caté}} | \deleted{Il est évident que la \unsure{catég&#124;caté}} | A: A39; B: B40; C: 42 |
| final_register | Final definition, Ob/M_0/N/Hom and case relations | \mathrm{Ob}\,M_0=\mathbb N,\quad \mathrm{Hom}_{M_0}(n',n)= | \mathrm{Ob}\,M_0 = \mathbb{N},<br>\qquad<br>\mathrm{Hom}_{M_0}(n', n) = | Ob M_0=N; Hom_{M_0}(n',n); slashed empty set and n' not<=n, then n'<=n | Ob M_0=N; Hom_{M_0}(n',n); slashed empty set and n' not<=n, then n'<=n | Ob M_0=N; Hom_{M_0}(n',n); slashed empty set and n' not<=n, then n'<=n | A: complete text/log; B: complete text/log; C: complete text/log |
| final_hom | Second case, hom abbreviation | \text{ens. des hom. admissibles} | \text{ens.\ des homs.\ admissibles } | ens. des hom. admissibles; no s in hom | ens. des hom. admissibles; no s in hom | ens. des hom. admissibles; no s in hom | A: A41; B: B42; C: 44 |
| final_J_source | Second case, source J_n-prime | J_{n'}\to J_n | I_{n'} \to I_n | J_{n'} | J_{n'} | J_{n'} | A: A41; B: B42; C: 45 |
| final_J_target | Second case, target J_n | J_{n'}\to J_n | I_{n'} \to I_n | J_n | J_n | J_n | A: A41; B: B42; C: 45 |
| final_layout | Second case, two-line arrangement | &\text{ens. des hom. admissibles}\\<br> &\qquad J_{n'}\to J_n\quad\text{si }n'\leq n | \text{ens.\ des homs.\ admissibles } I_{n'} \to I_n & \text{si } n' \leq n | ens. des hom. admissibles on its own line; J-to-J map and condition below | ens. des hom. admissibles on its own line; J-to-J map and condition below | ens. des hom. admissibles on its own line; J-to-J map and condition below | A: A41; B: B43; C: 45 |
| archive | Archive numeral at lower left | % archive sheet number: 8 | \page{8} | 8; archive numeral | 8; archive numeral | 8; archive numeral | A: complete text/log; B: complete text/log; C: complete text/log |

## Every C doubt

| ID | Exact alternatives | Physical key | Status |
|---|---|---|---|
| C01 | plus,&#124;\deleted{plus,} | plus | pending main adjudication |
| C02 | fort&#124;faut&#124;fut | fword_encore | pending main adjudication |
| C03 | isom&#124;iso | isom | pending main adjudication |
| C04 | n'&#124;n | lorsque_n | pending main adjudication |
| C05 | n'&#124;m | family_pair_second | pending main adjudication |
| C06 | chose&#124;choses | cancelled_approx | pending main adjudication |
| C07 | la&#124;le | cancelled_essential | pending main adjudication |
| C08 | il&#124;à | cancelled_il | pending main adjudication |
| C09 | équiv&#124;équiva | equiv | pending main adjudication |
| C10 | description&#124;descripteur | description | pending main adjudication |
| C11 | standart&#124;standard | standart | pending main adjudication |
| C12 | n&#124;n' | paired_J_second_index | pending main adjudication |
| C13 | Donc&#124;Don | Donc | pending main adjudication |
| C14 | \xi&#124;a | old_zeta | pending main adjudication |
| C15 | stabilité&#124;composition&#124;stabilis | cancel_stability | pending main adjudication |
| C16 | entre&#124;entre. | entre | pending main adjudication |
| C17 | catég&#124;caté | cancel_final | pending main adjudication |

## Every H doubt mark

| ID | Actual macro | Physical keys |
|---|---|---|
| H01 | \ill{} | fword_encore |
| H02 | \ill{} | phantom_deleted |
| H03 | \ill{} | cancelled_approx, cancelled_essential |
| H04 | \ill{} | description |

## Context coverage

- **CTX01 — Xi/eta/zeta, d and arrow direction**: opening_old_x, opening_notation, evaluation, upper_label, upper_target_J, diagram_eta_top, diagram_xi_top, diagram_eta_arrow, composite_eta1, old_zeta, composite_eta_arg, composite_eta2, composition_register.
- **CTX02 — N/M/M_0 and J/tau/rho alphabets**: families_J, families_register, rho, family_pair_first, family_pair_second, category_replacement, M0_replacement, final_register, final_J_source, final_J_target.
- **CTX03 — Abbreviations, stops and opening quotation**: opening_notation, identity_J, isom, equiv, hom_1, standart, middle_ie, hom_lower, final_register, final_hom.
- **CTX04 — Final empty-set slash and inequalities**: final_register, final_layout.
- **CTX05 — First xi and later ordinary x occurrences**: opening_old_x, opening_J1, opening_clause_placement, opening_J2, opening_notation.
- **CTX06 — F-word before encore without supplied extra word**: fword_encore.
- **CTX07 — Unmatched opening ticks and terminal t**: standart.
- **CTX08 — Final Ob/Hom notation and cases**: final_register, final_hom, final_J_source, final_J_target, final_layout.
- **CTX09 — Own folio and archive numeral**: folio, archive.
- **CTX10 — Current C audit corrections, placements and equality speck**: De, plus, upper_brace, family_pair_second, category_replacement, cancelled_approx, cancelled_essential, cancelled_il, description, condition_insertion, Donc, diagram_membership_left, diagram_membership_right, diagram_lower_row, old_zeta, composite_point, cancel_stability, entre, M0_replacement, cancel_final.

## Inventory union in physical order

All A29/B33/C29 inventory entries map once to physical parents. B's disputed plus cancellation is inventoried once as text with uncertain status; its separate brace drawing is beside the parent annotation. B35's extra point is adjacent to the lower display. The union has31 physical entries. Archive8 is text in an unattributed archival hand.

| Order | Element | Kind | A/B/C source rows | Status |
|---|---|---|---|---|
| 1 | E01: manuscript folio | text | 1 / 1 / 1 | pending |
| 2 | E02: opening inline clause | text | 2 / 2 / 2 | pending |
| 3 | E03: older x beneath xi | deletion | 3 / 3 / 3 | pending |
| 4 | E04: evaluation display | display | 4 / 4 / 4 | pending |
| 5 | E05: upper isomorphism | diagram | 5 / 10 / 8 | pending |
| 6 | E06: upper prose and plus cancellation-status candidate | text | 6 / 5,7 / 5 | pending |
| 7 | E07: canceled De | deletion | 7 / 6 / 6 | pending |
| 8 | E31: brace beneath on a with rising return | drawing | — / 9 / — | pending |
| 9 | E08: attached upper insertion | insertion | 8 / 8 / 7 | pending |
| 10 | E09: Lorsque paragraph | text | 9 / 11 / 9 | pending |
| 11 | E10: identity display | display | 10 / 12 / 10 | pending |
| 12 | E11: reconstruction paragraph and families | text | 11 / 13,18,22 / 11 | pending |
| 13 | E12: overwritten family-index component | deletion | 12 / 14 / 12 | pending |
| 14 | E13: raised category replacement | insertion | 13 / 17 / 15 | pending |
| 15 | E14: first canceled reconstruction phrase | deletion | 14 / 15 / 13 | pending |
| 16 | E15: second canceled reconstruction phrase | deletion | 15 / 16 / 14 | pending |
| 17 | E16: canceled fragment before équiv | deletion | 16 / 19 / 16 | pending |
| 18 | E17: condition replacement | insertion | 17 / 20 / 18 | pending |
| 19 | E18: old noun beneath condition | deletion | 18 / 21 / 17 | pending |
| 20 | E19: Donc cancellation | deletion | 19 / 23 / 19 | pending |
| 21 | E20: composition chain | diagram | 20 / 24 / 20 | pending |
| 22 | E21: on doit avoir | text | 21 / 25 / 21 | pending |
| 23 | E22: composition equation | display | 22 / 26 / 22 | pending |
| 24 | E30: point beside composite equality | drawing | — / — / — | pending |
| 25 | E23: older result index under zeta | deletion | 23 / 27 / 23 | pending |
| 26 | E24: stability explanation | text | 24 / 28 / 24 | pending |
| 27 | E25: canceled word before stabilité | deletion | 25 / 29 / 25 | pending |
| 28 | E26: M_0 definition replacement | insertion | 26 / 30 / 26 | pending |
| 29 | E27: canceled assertion | deletion | 27 / 31 / 27 | pending |
| 30 | E28: final object and Hom definition | display | 28 / 32 / 28 | pending |
| 31 | E29: archive sheet number | text | 29 / 33 / 29 | pending |

Reader A records no mathematical checks. B records one targeted conditional evaluation check; C records its background assumption and one targeted conditional check. These actual events are preserved unchanged. The six original main events are imported only after explicit source confirmation. This assembler performs no proof, audit or re-proof.
