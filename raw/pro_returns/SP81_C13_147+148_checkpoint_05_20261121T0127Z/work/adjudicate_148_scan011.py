from pathlib import Path
from datetime import datetime, timezone
import csv, json, subprocess, sys

root=Path(__file__).resolve().parents[1];p='148_scan011'
f={r['box']:r['reading'] for r in csv.DictReader((root/'second'/f'{p}_first.tsv').open(),delimiter='\t')}
s={r['box']:r['reading'] for r in csv.DictReader((root/'second'/f'{p}_second.tsv').open(),delimiter='\t')}
rp=root/'work'/f'{p}_final.json';report=json.loads(rp.read_text());assert not report.get('audit')
final=dict(f)
trans=r'\unsure{transitivem\textsuperscript{t}|transitivement}'
mut=r'\unsure{mutuellem\textsuperscript{t}|mutuellement}'
final['B02']=f['B02'].replace('transitivement',trans)
final['B06']=r'\deleted{\unsure{en ce cas|en cor|en cov} \unsure{torseur|C par}} \inserted{\unsure{le|ce|un} torseur}'
final['B13']=f['B13'].replace('(tels que',r'(\unsure{tels que|tel que}')
final['B16']=f['B16'].replace(r'\unsure{mutuellement|mutuellem\textsuperscript{t}}',mut)
e={
'B02':'The initial transiti- sequence is followed by a compressed low joining run and a terminal stroke rising above that run. The full -vement ending is not separately exposed. The contracted transitivem with raised t is preferred, while the full transitivement remains an explicit alternative. The Z/6Z and opère are unchanged.',
'B03':'The open first curve after the set expression joins the low a/r components, supporting car without an added parenthesis. The following verb has a descending p and final e. The short trivialt abbreviation has no separately exposed full ement sequence; the single horizontal dash remains as observed. The subscript S has the same broad upper/lower curved body as the S elsewhere on the page.',
'B04':'The left subscript 2, the X with its low S, set-difference stroke and zero are present. The quotient has Z/6Z, a slash before plus-minus one, a raised wave over the lower relation bar, and Z/3Z. Case serialization and math wrappers account for the token differences; the source S form is retained consistently.',
'B05':'The canceled initial curve and descender remain compatible with the existing doubtful conj. boundary. The live word after générateur exposes the p descender and its later linked ending through terminal t, so correspondant is retained. The next tiny sign comprises upper oblique marks over a lower bar, supporting the existing relation doubt. The broad curled symbol with a detached overbar matches the zeta form checked in the definition and lattice labels on scan 009. The separate narrow descending glyph retains j|zeta. The fraction visibly has 2 pi over 6 with no supplied i, and there is no extra closing parenthesis beyond the one already represented.',
'B06':'The strike crosses a low initial en and the following small linked cluster; the latter permits ce cas, cor or cov without exposing all letters. The right canceled cluster includes an open curve and a later tall descending stroke with low returns; the first torseur and blind C par both remain candidates. Above the strike the determiner has a short raised initial curve and a low return, leaving le, ce and un open; the following torseur is legible. These are local uncertainties about existing ink; the cancellation and raised replacement remain distinct in position.',
'B07':'Two detached vertically aligned marks after s’identifie support the first colon. At associant the two short old strokes are crossed by the oblique shaft beneath the raised a-like loop; the existing literal TikZ preserves these strokes without assigning an old equals sign or a complete former word. The following ssociant is exposed.',
'B08':'Before chaque the two detached marks favor the existing colon alternative; the a interpretation remains uncertain. The last word of the first baseline begins with a short rising r, has a long looped y descender and ends in low o/n, supporting rayon. The next line reads ou plutôt. The detached raised closing parenthesis remains horizontally after dans and before X_S; its intended attachment remains unresolved.',
'B09':'The abbreviation ens has no terminal point. The interlinear subset sign and Z/6Z are connected after Z/3Z. Beneath the connector are low s/u/r strokes supporting sur. The written subscript S is consistent with the other occurrences on the page.',
'B10':'The baseline reads est de card 3, il s’obtient en prenant. The different math wrapper around the numeral changes no reading.',
'B11':'The b/a/r/y strokes are visible immediately after les. Their heavy low retracing leaves the source state uncertain, as already recorded in the first reading; the separate word proposed by H has no exposed independent position. The blind reading gives the same preferred noun, and the local uncertainty remains.',
'B12':'The initial bi/ba, descending y, central joined sequence, tall t and final q/u/e of bibarycentrique are exposed. The whole word and its surrounding parenthesis were checked; the first resolved reading is retained.',
'B13':'The open medial c, tall l and accented ending support cerclés. In the following phrase, the ending after tel is compressed into a low terminal run; tels que remains first, with tel que as an explicit alternative. The opening parenthesis remains before the phrase.',
'B14':'The formula has a detached dark overbar over the same broad zeta-shaped body found on scan 009 and in B05. The initial 1, minus, parentheses, slash and 3 are separately exposed. The following etc has no end point. Epinglé has its p and g descenders, tall l and accented ending; the first reading is retained.',
'B15':'The initial and later descenders in paquets support p and q, followed by the tall t and terminal s. Both readings give deux paquets de 3; the wrapper around 3 accounts for the difference.',
'B16':'After the paired tall l strokes, a low joined run terminates in a raised heavily retraced t, without separately exposed full -ment letters. The contracted mutuellem with raised t becomes preferred, with mutuellement retained. Congrus has one long descending g region followed by a short r/u/s run; a second descender and separate j dot for conjugués are unexposed. Sous has the four low components already recorded, followed by plain Gamma. Donnant|donnent remains open at its compressed middle vowel.',
'B17':'The visible final baseline retains deux éléments (symétriques) de X_S, d’ordre 3, including the final comma. The S has the same low curved shape used throughout this page. Math wrappers and case serialization account for the difference.'}
pp=root/'pages'/f'{p}.tex';page=pp.read_text()
for b in ['B02','B06','B13','B16']:
 assert page.count(f[b])==1,(b,page.count(f[b]))
 page=page.replace(f[b],final[b])
pp.write_text(page)
for ch in report['changes']:
 if ch['id']==p+'-04':
  ch['final']=final['B06'];ch['evidence']+=' Blind audit: '+e['B06'];ch['crop']=p+'_second_B06.png';ch['box']=[925,652,1481,785];ch['confidence']='low'
for ident,place,c,h,reading,boxid,coords in [
 ('22','line 1, compressed ending of transitivement','transitivement','transitivement',trans,'B02',[250,116,1538,239]),
 ('23','line 16, compressed ending of mutuellement',r'\unsure{mutuellement}','mutuellement',mut,'B16',[201,2136,1612,2260])]:
 report['changes'].append(dict(id=p+'-'+ident,place=place,C=c,H=h,final=reading,evidence=e[boxid],crop=p+'_second_'+boxid+'.png',box=coords,confidence='medium',kind='abbreviation expanded or spelling modernised',error_sheet_kind='Abbreviations expanded, spelling modernised',differs_C=True,differs_H=True,marked_in_H=False,consequential=False))
for d in report['decisions']:
 if d['id']=='M0105':d['reading']=mut;d['evidence']+=' Blind audit: '+e['B16'];d['crop']=p+'_second_B16.png [201,2136,1612,2260]'
for d in report['doubts']:
 if d['place']=='line 5, beginning of lower cancellation':d['reading']=final['B06'];d['alternatives']='en ce cas | en cor | en cov; torseur | C par; raised le | ce | un';d['reason']=e['B06']
 if d['place']=='line 16, terminal sequence of mutuellement':d['reading']=mut;d['alternatives']='mutuellement';d['reason']=e['B16']
report['doubts'].extend([
 dict(place='line 1, compressed ending of transitivement',reading=trans,alternatives='transitivement',confidence='medium',reason=e['B02']),
 dict(place='line 13, terminal letters in tels que',reading=r'\unsure{tels que|tel que}',alternatives='tel que',confidence='medium',reason=e['B13'])
])
report['abbreviations'].extend([dict(form=r'transitivem\textsuperscript{t}',expansion='transitivement (full-word alternative retained in place)'),dict(form=r'mutuellem\textsuperscript{t}',expansion='mutuellement (full-word alternative retained in place)')])
report['hand'].append(dict(habit='A long low run followed by a raised retraced t compresses the adverb ending; not all full -ment letters are separately exposed.',places='148_scan011 B02 and B16; compare 148_scan013 compressed adverb ending after its independent audit',scope='These observed occurrences only; no blanket expansion of every adverb.',witness_errors='C and H give full transitivement and mutuellement; the contracted readings are now preferred with the full forms retained as alternatives.'))
report['notes']+='\nBlind audit: the low runs and raised terminal strokes favor contracted transitivem with raised t and mutuellem with raised t; the full-word alternatives remain. The lower cancellation and raised determiner before torseur retain narrower local alternatives. The broad barred zeta in the two formulas was compared with the scan 009 definition and labels; the narrow j|zeta glyph and the source fraction without i remain unchanged.'
rp.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
diffs=json.loads((root/'second'/f'{p}_comparison.json').read_text())['differences'];choices=[]
for d in diffs:
 b=d['box'];changed=final[b]!=f[b]
 choices.append(dict(box=b,choice='literal' if changed else 'first',**({'final':final[b]} if changed else {}),changed=changed,evidence=e[b],confidence='low' if b=='B06' else ('medium' if b in ['B02','B05','B08','B11','B13','B16'] else 'high')))
(root/'work'/f'{p}_audit_choices.json').write_text(json.dumps(dict(reader='audit_a',choices=choices),ensure_ascii=False,indent=2)+'\n')
stamp=datetime.now(timezone.utc).isoformat()
with (root/'work/root_views.tsv').open('a') as out:
 for b in range(1,19):out.write(f'{stamp}\t{p}_second_B{b:02d}.png\tRoot personally displayed and inspected the complete blind crop before adjudication.\n')
subprocess.run([sys.executable,str(root/'scripts/prepare_audit_decisions.py'),p],check=True)
subprocess.run([sys.executable,str(root/'scripts/record_audit.py'),p],check=True)
