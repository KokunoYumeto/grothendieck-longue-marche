from save_page import save_page
save_page(52,r'''\scanpage{52}
% archive foliation: 51
\deleted{
(i.e. l'\unsure{Albanese} à isogénie près) d'une \unsure{surface} $X$ (sur $k$ alg. clos) sera \unsure{connue} quand on connaît $X$ dans $L(k)$ seulement .....

\deleted{\diagram{\begin{tikzcd}
L_i(K)/L_{i-1}(K) \arrow[r] & \unsure{M_i(K)/M_{i-1}(K)}
\end{tikzcd}}}

\unsure{Notons} que l'hom
\diagram{\begin{tikzcd}
L_i(K)/L_{i-1}(K) \arrow[r] & D_iM^+(K)/D_{i-1}M^+(K)
\end{tikzcd}}
prend ses valeurs dans l'image de $M_i^+(K)$ modulo $D_{i-1}M^+(K)$, \deleted{\unsure{de}} \inserted{i.e.} dans \unsure{la|le} \unsure{partie primitive}. On peut se demander \inserted{si} \deleted{\unsure{le}}

\fbox{\diagram{\begin{tikzcd}
L_i(K)/L_{i-1}(K) \arrow[r] & \deleted{\unsure{\sigma_i(K)}}\mathbf{Z}^{\unsure{\sigma_i(K)}}
\end{tikzcd}}}.

est injectif, ou bijectif, du moins mod torsion....
}
''',[
('top; continuation cut by scan edge','text',"(i.e. l'Albanese à isogénie près) d'une surface X"),
('upper','diagram','L_i(K)/L_{i-1}(K) -> M_i(K)/M_{i-1}(K); individually cancelled'),
('upper-middle','text',"Notons que l'hom"),
('middle','diagram','L_i(K)/L_{i-1}(K) -> D_i M^+(K)/D_{i-1} M^+(K)'),
('middle-lower','text',"prend ses valeurs dans l'image; On peut se demander"),
('lower','diagram','boxed L_i(K)/L_{i-1}(K) -> Z^{sigma_i(K)}'),
('lower','text','est injectif, ou bijectif, du moins mod torsion')],sheet_kind='cancelled_draft',remarks='Entire text traversed by a long diagonal cancellation. Whole page, both halves, enlarged top and middle inspected. No text reconstructed beyond the top edge.')
