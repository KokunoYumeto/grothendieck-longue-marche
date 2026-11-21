"""Single-use scan018 main-reader adjudication."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan018_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b02','The capital has a distinct roof and left stem supporting Gamma; a faint diagonal retrace does not establish a different complete letter. The indexed K forms have tall stems and angular arms, matching the neighbouring capital K rather than the reduced lowercase k in prose. The raised cluster contains a compact looped left body and low right return. Retracing does not securely distinguish a, infinity, or a compressed can sequence; add the independently proposed can without forcing it.',r'$\Gamma^{\unsure{a|\infty|can}}_{\bar K/K}$')
c('b03','Both capital Pi roofs, K and double-stroked Q agree. The horizontal connector terminates in a thick nib with a short downward turn, but no independent upper arrowhead branch. Retain the plain shaft, contrasted with the separately headed B map in b11. The following low curved comma lies just beyond the crop and is visible on the full upper half; retain it.')
c('b04','The cancellation covers a tall angular initial, a small lower loop and a later upright. These do not make either Ainsi or tels completely certain. Retain the existing alternatives. The following q descender, ue and k, and the raised avec agree. Spacing between deletion and insertion is rendering-only.')
c('b05','The q descender, low u and dotted i of qui, then the tall d and later dotted i of induise, agree. Both Q forms have their inner stroke; only the first is barred. The final detached point is visible. Additional TeX braces around Q do not change the reading.')
c('b06','The small lower-left figures are 1 and 7. They belong to the thin foliation at the sheet edge, so the margin wrapper is retained; the second mspage wrapper is not evidence of another author-page number.')
c('b07','The initial small closed loop supports e rather than an initial u. After the n-like rise, a short upright and long low return may represent s, but that final letter cannot be separated securely. Preserve ens/en. There is no independently formed final e body for une, and no b or l ascender for expanded ensemble. De agrees.',r'\unsure{ens|en} de')
c('b08','The long stroke under pro is continuous with the g descender and is not an underline. Between pro and g there is a very short horizontal two-lobed ink mark; its width favours a dash, but it is too compact to exclude a point securely. Retain dash/point alternatives instead of deciding by the expected compound spelling.',r'pro\unsure{-|.}galoisiens')
c('b11','The first subscript has a straight tall stem and angular joined arms, matching the capital K elsewhere on the leaf. Both B letters and the doubled Q agree. The connector has a distinct curved upper and lower head, unlike the simple terminal nib in b03. Arrow length and redundant braces are typesetting choices.')
(R/'documentation/149_scan018_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan018.tex';s=p.read_text()
for k in ['b02','b07','b08']:
 assert first[k] in s,k;s=s.replace(first[k],ch[k]['final'])
p.write_text(s)
p=R/'reviews/149_scan018.json';r=json.loads(p.read_text());mapping={'c02':'b02','c07':'b07','c08':'b08'}
for x in r['changes']:
 if x['id'] in mapping:
  k=mapping[x['id']];x.update(final=ch[k]['final'],evidence=ch[k]['evidence'],against_C=True,confidence='low')
  if k=='b08':x['against_H']=True
for x in r['doubts']:
 if 'Gamma superscript' in x['place']:x.update(reading=r'\unsure{a|\infty|can}',alternatives=['a',r'\infty','can'],reason=ch['b02']['evidence'])
 if 'written abbreviation' in x['place']:x.update(reading=r'\unsure{ens|en}',alternatives=['ens','en'],reason=ch['b07']['evidence'],confidence='low')
r['doubts'].append({'place':'Line11, separator between pro and galoisiens','reading':r'pro\unsure{-|.}galoisiens','alternatives':['hyphen','point'],'confidence':'low','reason':ch['b08']['evidence']})
for x in r['decisions']:
 if x['id']=='M1009':x.update(reading=r'\unsure{a|\infty|can}',evidence=ch['b02']['evidence'])
for x in r.get('notation',[]):
 for f in ['written','rendering']:
  if f in x:x[f]=x[f].replace(r'\unsure{a|\infty}',r'\unsure{a|\infty|can}')
for x in r['diff_coverage']:
 if x.get('change_id') in mapping:
  k=mapping[x['change_id']];x.update(final=ch[k]['final'],reason=ch[k]['evidence'])
r['notes'].append('Independent audit: all8 differing boxes and24 token spans personally inspected. The Gamma superscript gains can as an unresolved alternative; the short group is explicitly ens/en; and the very compact separator in pro-galoisiens is now dash/point uncertain. The full upper half was rechecked for the comma immediately after the Pi map. All other differences are resolved in the adjudication table. No mathematical check was added.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
