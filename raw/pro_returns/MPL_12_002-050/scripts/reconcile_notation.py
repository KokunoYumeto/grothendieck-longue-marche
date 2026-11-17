from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
if (root/'frozen_hashes.json').exists(): raise SystemExit('Refusing changes after freeze')
changed=[]
for p in sorted((root/'pages').glob('*.tex')):
 s=p.read_text(); old=s; n=int(re.search(r'scan(\d+)',p.name).group(1))
 # Reinforced/double-stroke coefficient, projective-space and multiplicative-group alphabets.
 s=re.sub(r'\\mathbf\s*(?:\{([QZCGP])\}|([QZCGP]))',lambda m:r'\mathbb{'+(m[1] or m[2])+'}',s)
 if n<=8:
  s=re.sub(r'(?<![A-Za-z\\])Q(?![A-Za-z])',lambda m:r'\mathbb{Q}',s)
  s=re.sub(r'(?<![A-Za-z\\])Z(?![A-Za-z])',lambda m:r'\mathbb{Z}',s)
  s=s.replace('k=C','k=\\mathbb{C}').replace('Spec}(C)','Spec}(\\mathbb{C})')
 if n==2: s=s.replace('P^1_k',r'\mathbb{P}^1_k')
 # Ink distinguishes cursive categorical M from object M and straight ring M.
 s=re.sub(r'(?<![A-Za-z\\])M(?=\^)',lambda m:r'\mathcal{M}',s)
 s=re.sub(r'(?<![A-Za-z\\])M(?=\((?:[XYSkKC](?:_\{[^{}]+\}|_[a-z]|\x27)?|\\eta)\))',lambda m:r'\mathcal{M}',s)
 s=re.sub(r'(?<![A-Za-z\\])M(?=_(?:\{[^{}]+\}|\\(?:ell|alpha|infty)|[a-zA-Z0-9])(?:\^[+*])?\((?:X|Y|k|K|S)\))',lambda m:r'\mathcal{M}',s)
 if n==3: s=s.replace('dans $M$.','dans $\\mathcal{M}$.')
 if n==21:
  s=s.replace('10) Anneaux $\\mathcal{M}^+(X)$ et $\\mathcal{M}(X)$','10) Anneaux $\\mathrm{M}^+(X)$ et $\\mathrm{M}(X)$')
  s=s.replace('12) L\'hom $L(k)\\longrightarrow\\mathcal{M}^+(k)$','12) L\'hom $L(k)\\longrightarrow\\mathrm{M}^+(k)$')
 if n==28: s=s.replace(r'\deleted{$M$}',r'\deleted{$\mathcal{M}$}')
 if n==35: s=s.replace(r'$D_i(M)$ et $M_i$',r'$D_i(\mathcal{M})$ et $\mathcal{M}_i$')
 # Two-stroke abbreviation: literal sign retained, expansion belongs only in doubts.
 short=r'\unsure{$=$|$\overline{\mathrm m}$}'
 s=s.replace(r'\unsure{$=$|même}',short)
 for a,b in {
  17:[('de même ', 'de '+short+' ')],
  23:[('de même ', 'de '+short+' ')],
  24:[('De même,', 'De '+short+',')],
  28:[('lui-même','lui-'+short)],
  30:[('avoir même rang','avoir '+short+' rang')],
  34:[('même $',''+short+' $')],
  36:[('de même ', 'de '+short+' ')],
  38:[('on aura même','on aura '+short)],
  44:[('même mod torsion',r'\unsure{même} mod torsion')]
 }.get(n,[]): s=s.replace(a,b)
 if s!=old: p.write_text(s); changed.append(n)
print('Reconciled scans:',','.join(f'{n:03}' for n in changed))
