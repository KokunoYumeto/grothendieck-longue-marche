from pathlib import Path
out=Path('/workspace/scratch/17347c1714f0/out/readers/scan007/R1')
s=Path('/workspace/scratch/17347c1714f0/packets/scan007/C.tex').read_text()
changes={
 r'\unsure{\varphi|\phi}':r'\varphi',
 r'\text{\unsure{ordonné}}':r'\text{ordonné}',
 r'\unsure{\partial|\delta}X_i':r'\partial X_i',
 r'\unsure{i_{k_{i-1}}|i_{ki-1}|i_{k-1}}':r'i_{k_{i-1}}',
 r'\deleted{\unsure{\partial}}\Delta':r'\deleted{\partial}\Delta',
 r'\unsure{\mathord{-}|\supset|\longrightarrow}':r'\unsure{\supset|\mathord{-}}',
 r'\partial X_{\unsure{i_k|k}}':r'\partial X_{i_k}',
 r'X_{\unsure{j_k|i_k}}':r'X_{i_k}',
 r'\deleted{\unsure{\cap d\'}}':r'\deleted{\cap d\'}',
 r'X_{i_{\unsure{\alpha|2}}}':r'X_{i_\alpha}',
 r'\deleted{\updownarrow}':r'\deleted{\unsure{\downarrow|\updownarrow}}',
 r'\unsure{\pi_0|\Pi_0}':r'\pi_0',
}
# Apostrophes require ordinary raw double-quoted literals.
changes.pop(r'\deleted{\unsure{\cap d\'}}')
changes[r"\deleted{\unsure{\cap d'}}"]=r"\deleted{\cap d'}"
for a,b in changes.items():
 if a not in s: raise RuntimeError('Missing source '+a)
 s=s.replace(a,b)
s=s.replace('% Faint three-armed trace immediately above the first boundary symbol.',r'''% Small faint arc below the upper-right union; no legible character.
\draw[gray!55,very thin] (1124,575) .. controls (1130,569) and (1138,566) .. (1144,572);
% Faint three-armed trace immediately above the first boundary symbol.''')
s=s.replace('% Continuous fine oblique through the working, and shorter counterstroke at the foot.',r'''% Two faint, unlabelled strokes below the lower-right operator.
\draw[gray!45,very thin] (1232,1843) .. controls (1244,1844) and (1254,1846) .. (1260,1850);
\draw[gray!35,very thin] (1233,1860) .. controls (1245,1862) and (1253,1859) .. (1258,1859);
% Continuous fine oblique through the working, and shorter counterstroke at the foot.''')
s=s.replace('% archive sheet number: 6','% archive pencil sheet number: 6; no author page-number claim')
(out/'reading.tex').write_text(s)
print(s)
