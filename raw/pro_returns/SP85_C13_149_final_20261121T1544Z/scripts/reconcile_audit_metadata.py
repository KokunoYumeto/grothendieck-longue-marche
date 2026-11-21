"""Reconcile descriptive metadata with already-adjudicated text; never edit TeX."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')}
def read(n):
 p=R/'records'/f'149_scan{n:03}.json';return p,json.loads(p.read_text())
for n in (36,38,40,41,42,43,45,46):
 p,r=read(n)
 if n==36:
  for x in r['notation']:
   if 'n_G' in x['form']:x['form']=r'$\unsure{n_G|{}_nG|nG}$';x['evidence']='Cancelled draft, blind B08: the joined label admits lowered G, a left n, or an unindexed nG course.'
   if x['form']=='=':x['evidence']='Marginal sentence in blind B11: Y est lui = une telle courbe.'
 if n==38:
  for x in r['abbreviations']:
   if x['form']==r'\unsure{du m}':x.update(form=r'\unsure{(du m|celui-ci}',expansion='The primary reading may abbreviate du moins, with an opening parenthesis; the competing reading is celui-ci. No expansion is made in the text.')
 if n==40:
  for x in r['notation']:
   if x['form']==r'\unsure{=|\overline m}':x.update(form='=',evidence='Blind B07 resolves the two flat bars: the small initial lower-bar bend does not form m arches.')
  for x in r['abbreviations']:
   if x['form']==r'\unsure{=|\overline m}':x.update(form='=',expansion='même; two-bar shorthand resolved in the blind audit')
 if n==41:
  for x in r['notation']:
   if x['form'].startswith(r'\mathcal E_K,'):x['evidence']+=' Blind B04 preserves a separate period/prime uncertainty beside the first lowered K; this general notation entry does not settle that local mark.'
 if n==42:
  for x in r['notation']:
   if x['form'].startswith(r'\unsure{\pi_'):
    x['form']=r"\unsure{\pi_{\overline{K'}}|\pi^{\wedge}_{K'}|\pi_{\widehat K'}}\longrightarrow\unsure{\pi_{\overline K}|\pi^{\wedge}_K|\pi^{\wedge}_{\overline K}|\pi_{\widehat K}}"
    x['evidence']='Blind B04: angular retraced marks may also be hats directly on the lowered K letters; the complete map and separate primes were read together.'
 if n==43:
  for x in r['abbreviations']:
   if x['form']=='tt':x.update(form=r'\unsure{tt|$\forall$}',expansion='tout, if the paired-t reading is correct; the universal-quantifier alternative remains explicit')
  for x in r['notation']:
   if x['form']=='anabélien':x['evidence']='p03–p04 and blind B03/B04: the compact sign admits tt/forall; anabélien is underlined.'
 if n==45:
  for x in r['abbreviations']:
   if x['form']=='hom.':x.update(form='hom',expansion='homomorphisme; all three occurrences lack a terminal stop')
   if x['form']=='tt':x.update(form=r'\unsure{$\forall$|tt|$A$}',expansion='tout if the tt alternative is correct; the universal-looking sign remains graphically uncertain')
 additions={
 42:[dict(habit='A physical line-division hyphen can be lost when running text is reflowed.',places='manifeste-/ment, blind B06',scope='One separately written end-of-line hyphen on this leaf; compare reconsti-/tue on043.',witness_errors='Both witnesses omit the source hyphen. It is retained without calling it a lexical misspelling.')],
 43:[dict(habit='A physical line-division hyphen is distinct from the letters on the next line.',places='reconsti-/tue, blind B05',scope='One clear horizontal end-of-line mark, parallel to manifeste-/ment on042.',witness_errors='Both witnesses join the word without its written hyphen.')],
 45:[dict(habit='Two descenders from the preceding word can mimic an extra opening parenthesis in a bottom-edge addition.',places='ff of effectivement above the condition after i.e., blind B07 and saved p13',scope='This particular overlap; the existing outer condition parentheses remain.',witness_errors='C preserves the main parenthesis structure; the blind reading considered an additional inner pair. Tracing both descenders prevents that addition.'),dict(habit='The internal o of hom is dot-like, but no terminal point need follow m.',places='All three hom words, blind B02/B03',scope='All three occurrences on045 are independently dotless.',witness_errors='Both C and H supplied a terminal point at all three places.')],
 46:[dict(habit='A low terminal return may not distinguish a final s from the end of n or e.',places='filtration(s), modélique(s), grossière(s), blind B08',scope='All three local endings remain doubtful; this is not a rule for all plurals.',witness_errors='The first pass and both witnesses give plurals, the blind reader singulars; the ink is kept with local alternatives.')]
 }.get(n,[])
 for h in additions:
  if not any(x['habit']==h['habit'] for x in r['hand_log']):r['hand_log'].append(h)
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
assert before=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')}
with (R/'progress.log').open('a') as f:f.write('audit metadata reconciled '+datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+': notation, abbreviations and hand habits through046; no page TeX changed\n')
print('Metadata reconciled; all page TeX hashes unchanged')
