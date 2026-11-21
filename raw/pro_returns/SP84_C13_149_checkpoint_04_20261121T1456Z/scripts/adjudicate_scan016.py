"""Single-use scan016 crop adjudication; no mathematical normalization."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan016_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b03','On and voit agree: the latter has its i dot and crossed t. The following looped d ends in one long reduced e return with a downward nib, without an independently formed terminal s. Retain de.')
c('b04','The two separate horizontal bars agree exactly; the second merely supplies math delimiters. The literal equals-shaped abbreviation is retained without expanding it.')
c('b05','The terminal is a thick downward nib turn attached to the horizontal shaft, with neither an upper oblique branch nor a pointed vertex. Retain the plain link, contrasting with the distinctly two-sided curved arrowhead in b11. Both B letters, the first K prime and second unprimed K agree; dollars are syntax.')
c('b06','The tiny first curved mark and long low second run do not securely distinguish ou from en/on. Preserve these alternatives instead of choosing the conjunction by context. The following d has its loop and one reduced e return, with no separate s body.',r'\unsure{ou|en|on} de')
c('b07','The two Pi roofs and tall legs, first index prime, K indices and final comma agree. The link terminates in a rounded nib with no pointed vertex or independent upper branch, unlike b11. Retain the plain shaft; math delimiters are syntax.')
c('b08','The right-hand live continuation starts with a tall unlooped l, has no dot for a following i, and ends in reduced c/e-like strokes. It supports the tentative lence ending rather than bien. The long descender in the overlapping left part is compatible with q of équivalence, but its adjacent letters cannot all be separated from the older strokes. Keep the qualified live reading and only the tentative iso prefix plus unreadable older remainder. A complete cancelled récipro. cannot be established independently through those overlaps.')
c('b09','The first short group has a curved rising entry, a reduced middle and a detached terminal dark point. Its compression does not securely distinguish the proposed sera from dc.; retain that doubt instead of expanding a short group silently. En particulier ainsi agrees. The final looped d is followed by one low u-run, without a separate s.',r'\unsure{sera|dc.} en particulier ainsi du')
c('b10','Morphisme ends in a low e return without an additional s-shaped unit. The next word ends in a tall looped l, also without a following s. The small vowel immediately before that l is too compressed to distinguish a from e securely, so structural/structurel is left open.',r'morphisme \unsure{structural|structurel}')
c('b11','The B map has a separate curved head with both upper and lower branches; retain the arrow. Both indices and the inner Q stroke agree. The following two low marks match b06 and permit ou/en/on; preserve the same ambiguity here.',r'$B_K\longrightarrow B_{\mathbb Q}$ \unsure{ou|en|on}')
c('b12','Both complete Pi terms, the K and double-stroked Q indices and final comma agree. The shaft has only a short terminal nib, with no separate pointed head comparable to b11. Retain the plain link.')
c('b13','A compact detached dot sits over the short low stroke immediately before q. There is no separate slanted grave accent or visible e loop there, so intrinsiquement remains the literal reading. The long lower curve is its attachment leader. Comme un is baseline context included only in the first scope.')
c('b15','Both E forms have three arms and the indices are K and doubled Q. The link ends in a short upright tick across the shaft, without either diagonal of an arrowhead. Retain the plain link and the separate final point; no left mapsto bar is present.')
c('b16','The word has a small initial oval with a rising return, two tall f strokes, a detached mark and a highly reduced ending. The rising return could belong to a compressed d, while the terminal strokes do not securely separate né from rent. Preserve affiné/différent rather than resolve this from the preferred prose. Peu and the final comma agree.',r'peu \unsure{affiné|différent},')
c('b17','The left capital has a heavy roof/stem and lighter middle and lower arms; its existing E/Gamma uncertainty remains. The extra parallel contour is irregular retracing, insufficient to establish a deliberate double-struck alphabet. On the right, lighter middle/lower traces are also visible beside the dark roof and stem, so Gamma alone is too definite: add E as an alternative. The barred first K, slash and final K are clear. No old/new correction sequence can be established.',r'\unsure{E|\Gamma}=\unsure{\Gamma|E}_{\bar K/K}')
c('b18','The insertion begins with a small closed oval below its separate accent, supporting à rather than an exclamation point. Isom unique près and the upper comma agree. The lower two-leg sign is small relative to the tall K indices and matches the established lowercase kernel pi. Both insertion leaders remain separate; neither is a parenthesis. After fixés a detached low curved mark is visible below the final letter return, supporting the final comma. Et Gamma agrees.')
(R/'documentation/149_scan016_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan016.tex';s=p.read_text()
for k in ['b06','b09','b10','b11','b16','b17']:
 assert first[k] in s,k;s=s.replace(first[k],ch[k]['final'])
p.write_text(s)
p=R/'reviews/149_scan016.json';r=json.loads(p.read_text())
mapping={'c04':'b06','c07':'b09','c08':'b10','c09':'b11','c13':'b16','c14':'b17'}
for x in r['changes']:
 if x['id'] in mapping:
  k=mapping[x['id']];x.update(final=ch[k]['final'],evidence=ch[k]['evidence'],against_C=True,confidence='low')
for x in r['doubts']:
 if 'left capital' in x['place']:x['reason']=ch['b17']['evidence']
for k,place,reading,alts in [
 ('b06','Main line6, word before de groupoïdes',r'\unsure{ou|en|on}',['ou','en','on']),
 ('b09','Main line10, short word after Il en',r'\unsure{sera|dc.}',['sera','dc.']),
 ('b10','Main line11, adjective after morphisme',r'\unsure{structural|structurel}',['structural','structurel']),
 ('b11','Main line11, word after the B map',r'\unsure{ou|en|on}',['ou','en','on']),
 ('b16','Main line15, word after peu',r'\unsure{affiné|différent}',['affiné','différent']),
 ('b17','Main line18, indexed capital on the right',r'\unsure{\Gamma|E}_{\bar K/K}',[r'\Gamma', 'E'])]:
 r['doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'low','reason':ch[k]['evidence']})
for x in r['diff_coverage']:
 for cid,k in mapping.items():
  if x.get('change_id')==cid:x['final']=ch[k]['final']
r['notes'].append('Independent audit: all15 differing boxes and39 token spans personally inspected. Six boxes gain explicit uncertainty: both ou/en/on groups; sera/dc.; structural/structurel; affiné/différent; and the indexed Gamma/E on the right. Plain shafts are retained after direct comparison with the distinct arrowhead in b11. The overwritten équivalence reading remains qualified, without completing the obscured older layer. No mathematical check was added.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
