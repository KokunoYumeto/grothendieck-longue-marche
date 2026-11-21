from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work'); p='149_scan079'
rp=w/'readers'/p/'report.json'; r=json.loads(rp.read_text()); pp=w/'pages'/f'{p}.tex'; t=pp.read_text()
t=t.replace(r'\pi_1(U_\eta)',r'\pi_1(U_{\unsure{\eta|k}})').replace('les vérifier !',r'\unsure{les|le} vérifier !'); pp.write_text(t)
for c in r['changes']:
 if c['place']=='local_target':
  c.update(final=r'\pi_1(U_{\unsure{\eta|k}})',confidence='medium',evidence='Blind review: the very small subscript has a short rising stroke and a forked/hooked right leg; its resolution does not establish the long eta descender securely. The neighbouring full-size k is looped, but this does not exclude a compressed k. Eta remains the preferred reading, with k retained explicitly.',crop='second_149_scan079_B002.png',box=[305,135,1145,315])
 if c['place']=='last_caution':
  c.update(final=r'il faudrait quand même \unsure{les|le} vérifier !',confidence='medium',evidence='The short initial i and taller looped l support lowercase il; quand has a descending q, même its circumflex, and vérifier the v/é/r/i/f/i/e/r strokes. Blind review leaves the article ending open: the small final curl can be s or the return of e. Retain les first but mark le as an alternative. The exclamation stem and dot are present.',crop='second_149_scan079_B015.png',box=[22,1800,300,2130])
r['unresolved'] += [dict(place='local_target',reading=r'\pi_1(U_{\unsure{\eta|k}})',alternatives=[r'\eta','k'],confidence='medium'),dict(place='last_caution_article',reading=r'\unsure{les|le}',alternatives=['les','le'],confidence='medium')]
r['notes'] += '\n\nBlind-reading adjudication: the target subscript in (12) now retains eta/k doubt, and the final marginal article retains les/le doubt. These are changes of certainty, not silently changed words. Both page-number readings agree: the dark upper 39 is the manuscript page number; the thin lower 78 remains a marginal foliation number. All 18 token-different boxes were reviewed on their saved second crops.\n'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
e={
'B002':'The map label retains its straight upright and branching kappa/k ambiguity. The target subscript is tiny, with a short forked/hooked right leg, so eta/k remains open; the adjacent larger k alone cannot settle it. The right arrowhead and two upright equality strokes are visible; T_infinity(k), indices and (12) agree.',
'B003':'Only a short rounded d/u-like group lies under the strike. There is neither room nor an independent g descender for change. Retain the doubtful short du and its cancelled state.',
'B004':'The word before section consists of low connected u/n/e strokes, not the four-letter avec outline. Section ends in n, without another s. Retain une section.',
'B005':'After d/o and the low double-n run, the accent and an extra terminal e-return support donnée. No final s is present. Retain donnée rather than repairing its agreement to donné.',
'B006':'A large 2 is followed by raised ième and the p descender of espèce; the closing quote ticks follow. Extension contains crossed x/t and the low n run; there is no descending g for catégorie. Retain the first reading.',
'B007':'The third connector, between E_U and E_S, has a distinct small triangular head. The remaining connectors are flat shafts. The letters and end 1s agree; no doubt over the entire formula is needed.',
'B008':'The upper addition begins classe and ends de, with its leader attaching after une. Its pi has the shared bar and two legs used elsewhere here, not an R bowl. The lower subgroup cluster remains doubtful because the g return and possible closing arc overlap. The proposed R-conj./des and additional R group letters are not independently established.',
'B009':'The opening word remains crossed by nearby marginal writing, so the existing fermés/libre doubt is retained; locaux is not established letter by letter. L has the small i and round 0 index. The word after it has a tall d and the longer ans run, supporting dans rather than de.',
'B010':'After suppose a q descender, apostrophe and low on run are visible. The proposed pris/fini lacks its necessary letter pattern. Retain qu’on.',
'B011':'The line has p.ex. with its stops, then an opening curve, a short j descender and e, followed by p/r/é/s/u/m/e. There is one closing parenthesis, not a second close or cf/G. Retain (je présume).',
'B012':'The top élémen- joins taire, whose crossed t and a/i/r/e are visible. Both car. groups include a terminal r return and stop. The final line has a separate se followed by a tall b and orne, not a bien. Retain the first text and the line-end hyphen.',
'B013':'The initial star and En fait lie inside the cancelled block. Pi is the local two-legged form, not R. The letters support situations fibrées, then on trouve une ext. du pi_1 de la base par le pi_1 de la fibre. No independent comma after besoin, extra si, or cat. is established. The end comme remains doubtful under cancellation. Keep the full cancelled span.',
'B014':'After the written equals sign, the low s/a/n/s run supports sans, without a d ascender. The small index is 1, despite the mathematical difficulty. The ending reads Cette extension admet alors followed by a detached star and pi_1(U); the proposed h/hom divides the word and reference mark incorrectly. The extra exclamation point is not separable from crossing contextual ink. Retain the live note as written.',
'B015':'The first i is short and the following l tall, supporting lowercase il. Quand même and vérifier are readable, and the exclamation stem/dot are distinct. The article has an ambiguous terminal curl: retain les first, but add le as an explicit alternative.',
'B016':'The upper word has a tall looped b and no crossed t, supporting courbe rather than courts. The cancelled elementary word ends in e with no independent final s. Preserve the deletion and replacement as recorded.',
'B017':'X occupies the same upper insertion baseline as lisse et propre sur S and belongs inside that addition. The leader joins the added clause to the main line; the extra avec is surrounding context already transcribed. Retain the comma after S inside the addition and T fini étale in the base line.',
'B018':'Both readings give 39. The crop shows two open curved lobes of 3 and the closed upper loop with long descending leg of 9. The difference is only the manuscript-page wrapper, which is retained.',
'B019':'Both readings give 78. The thin 7 has a slanted top and descending stem, and 8 has two joined loops. The margin wrapper records its placement and is retained; no numeral change.'}
d={k:dict(evidence=v,changed=k in ['B002','B015']) for k,v in e.items()}
d['B002']['final']=cs['B002']['first'].replace(r'U_\eta',r'U_{\unsure{\eta|k}}')
d['B015']['final']=cs['B015']['first'].replace('les vérifier',r'\unsure{les|le} vérifier')
(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
