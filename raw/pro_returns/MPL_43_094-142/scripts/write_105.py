from page_work import save_page
text=r'''\scanpage{105}
\mspage{104}
\uline{REFERENCES}

\noindent 1. M.F. Atiyah, ``Complex analytic connections in fibre bundles''
Trans. Amer. Math. Soc.

\noindent 2. M.F. Atiyah and F. Hirzebruch, ``Riemann-Roch theorems for
differentiable manifolds'', Bull. Amer. Math. Soc. 65 (1959\unsure{)}
p.276-281.

\noindent 3. M.F. Atiyah and J.A. Todd ``On complex Stiefel manifolds'',
Proc. Camb. Phil. Soc. (1960)

\noindent 4. A. Borel and J-P. Serre. ``Groupes de Lie et puissances
réduites de Steenrod'', American J. of Math. 75 (1953) 409-48.

\noindent 5. S.S. Cairns, ``On the triangulation of regular loci''.
Ann. of Math. 35 (1934) 579-87.

\noindent 6. A. Dold and R. Lashof, ``Principal quasifibrations and fibre
homotopy equivalence of bundles'' Illinois J. of Math. 3 (1959) 285-305.

\noindent 7. F. Hirzebruch, ``A Riemann-Roch theorem for differentiable
manifolds'', Séminaire Bourbaki (1959) No.177.

\noindent 8. I.M. James, ``The intrinsic join'', Proc. London Math. Soc
(3), 8 (1958) 507-35.

\noindent 9. I.M. James, ``Cross-sections of Stiefel manifolds'', ibid
536-47.

\noindent 10. I.M. James, ``Spaces associated with Stiefel manifolds'',
ibid (3) 9 (1959) 115-40.

\noindent 11. J. Milnor and E.H. Spanier (to appear)

\noindent 12. J.P.Serre, ``Homologie singulière des espaces fibrés'',
Ann. of Math.54 (1951) 425-505.

\noindent 13. E.H. Spanier and J.H.C. Whitehead ``Duality in homotopy
theory'' Mathematika, 2 (1955) 56-80.

\noindent 14. N. Steenrod ``The topology of fibre bundles''
(Princeton Univ. Press, 1951).

\noindent 15. R. Thom, ``Espaces fibrés en sphères et carrés de Steenrod'',
Ann. Sco. Ecole Norm. Sup. 69 (1952) 109-182.

\noindent 16. R. Thom, ``Quelques propriétés globales des variétés
differentiables Comment. Math. Helv. 28 (1954) 17-86.
'''
e=[('text','rotated top archive folio','104'),('text','rotated heading','REFERENCES')]
for i,name in enumerate(['M.F. Atiyah','M.F. Atiyah and F. Hirzebruch','M.F. Atiyah and J.A. Todd','A. Borel and J-P. Serre','S.S. Cairns','A. Dold and R. Lashof','F. Hirzebruch','I.M. James The intrinsic join','I.M. James Cross-sections','I.M. James Spaces associated','J. Milnor and E.H. Spanier','J.P.Serre','E.H. Spanier and J.H.C. Whitehead','N. Steenrod','R. Thom Espaces fibrés','R. Thom Quelques propriétés'],1):
 e.append(('text',f'rotated reference {i}',name))
save_page(105,text,e,sheet_kind='reused_typed',observations='Whole scan then rotated whole and both original halves read without OCR. Bibliography transcribed as printed, including “Sco.” in item 15, unaccented “differentiables” and no visible closing quotation in item 16. Closing parenthesis of the date at the clipped edge in item 2 is doubtful; the visible p.276-281 line is retained.')
