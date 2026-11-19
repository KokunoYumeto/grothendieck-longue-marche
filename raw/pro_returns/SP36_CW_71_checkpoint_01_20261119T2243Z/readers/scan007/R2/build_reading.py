from pathlib import Path
root=Path('/workspace/scratch/17347c1714f0/out/readers/scan007/R2')
s=Path('/workspace/scratch/17347c1714f0/packets/scan007/C.tex').read_text()
changes={
 r'\unsure{\varphi|\phi}':r'\varphi',
 r'\text{\unsure{ordonné}}':r'\text{ordonné}',
 r'\unsure{\partial|\delta}X_i':r'\partial X_i',
 r'\unsure{i_{k_{i-1}}|i_{ki-1}|i_{k-1}}':r'\unsure{i_{k_{i-1}}|i_{ki-1}}',
 r'\deleted{\unsure{\partial}}\Delta':r'\deleted{\partial}\Delta',
 r'\unsure{\mathord{-}|\supset|\longrightarrow}':r'\unsure{\supset|\mathord{-}}',
 r'\partial X_{\unsure{i_k|k}}':r'\partial X_{i_k}',
 r'\deleted{\unsure{\cap d\'}}':r'\deleted{\cap d\'}',
 r'i_{\unsure{\alpha|2}}':r'i_{\alpha}',
 r'\deleted{\updownarrow}':r'\deleted{\unsure{\downarrow|\updownarrow}}'
}
# Apostrophes in the deleted suffix are literal TeX prime characters.
changes.pop(r'\deleted{\unsure{\cap d\'}}')
changes[r"\deleted{\unsure{\cap d'}}"]=r"\deleted{\cap d'}"
for old,new in changes.items():
 if old not in s: raise ValueError('missing '+old)
 s=s.replace(old,new)
s=s.replace('% Faint three-armed trace immediately above the first boundary symbol.',
 '% Faint short arc, then the three-armed trace above the first boundary symbol.\n\\draw[gray!60,very thin] (1121,575) .. controls (1129,568) and (1139,565) .. (1144,574);')
s=s.replace('% Continuous fine oblique through the working, and shorter counterstroke at the foot.',
 '% Two faint short traces below the initial sign of the right-hand equality.\n\\draw[gray!45,very thin] (1231,1845) .. controls (1242,1845) and (1252,1847) .. (1264,1850);\n\\draw[gray!45,very thin] (1229,1858) .. controls (1241,1858) and (1250,1859) .. (1261,1860);\n% Continuous fine oblique through the working, and shorter counterstroke at the foot.')
(root/'reading.tex').write_text(s)
print('Wrote reading.tex')
