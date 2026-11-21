"""Single-use application of scan012 main-reader visual adjudications."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan012_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b01','After q/u, the small e loop continues into an additional terminal low run with a downward hook: the plural s is present. Two elevated ticks occur on each side of the word. Keep the plural and paired quotation marks; the second uncertainty does not identify an equally supported singular ending.')
c('b02','The q loop and descender and following u are clear, but the final short upright has no independently clear dot and could be the compressed return of e. Retain qui|que; the second doubtful qui does not resolve the alternative.')
c('b03','A complete lower oval and tail coexist with an upright and two K-like diagonals under the bar. A single R would not explain that complete lower oval. Retain the Q/K overstrike with both possible cancellation orders. The final double-stroked C and the words de and dans agree; mathbb braces are syntax.')
c('b04','Both Q letters have internal doubling and overbars; the relation has a wave above a bar and the final low zero is a closed oval. The only disagreement is mathbb bracing.')
c('b05','The upper glyph is an open C with inner stroke, not an oval Q with a tail. The lower glyph has a loop/doubled left side and a curled rightward foot: Q is favored, but k and the second reader’s C cannot be excluded from the merged strokes. Add C to the lower alternatives. No independent insertion leader or distinct strike establishes the second reading’s correction order, so retain neutral vertical placement. Both low indices, eta bar, parentheses and terminal comma agree.',first['b05'].replace(r'\unsure{\mathbb Q|k}',r'\unsure{\mathbb Q|k|\mathbb C}'))
c('b06','The initial small loop/open form leads into an n-like shoulder and long return. Neither the final u form nor an accent is sufficiently isolated to resolve où. Keep en|où rather than only the second doubtful où.')
c('b08','The letters through complex are recognizable beneath the cancellation, but its final stroke joins the last e-like loop and downward hook. A separate final s cannot be excluded securely. Adopt the second reading’s localized singular/plural doubt while retaining the definite cancellation.',r'\deleted{\unsure{complexe|complexes}}')
c('b11','The initial two-leg kernel sign is angular, but is used in the same indexed position as the small pi already compared on scans009–011; its shape alone does not establish capital Pi. Keep the established lowercase notation. Every pi_1, both leftward limit arrows and i indices, the underbrace label pi_i without an equals sign, the two wave-over-bar relations, barred letters and final completion wedge agree. Moving the label (13) outside an aligned wrapper, dollars, and mathbb braces are representation only.')
c('b12','In the rotated crop the sequences interprétation and particulière remain identifiable by their tall t strokes, p descenders and endings; the second adds doubt without an alternative. After a the low u return has no separate crossing pair for x, supporting au rather than aux. The compressed middle of pour/pr remains unresolved. Both final K letters have tall stems and diagonals, and the low zero is a separate oval; the small entrance curl is not a separate hat. Retain the whole marginal note, including its original uncertainty. The horizontal (12)/(13) context is excluded, and the dash/wrapper/mathbb differences are syntax.')
c('b13','The cancellation leaves a long p descender, a possible central a loop and a small terminal r-like upturn. The final upturn has no independent closed oval supporting pro. The middle remains too crossed to distinguish par from pr; retain those alternatives and the deletion.')
c('b14','Both readings identify the same raised n. Its V-shaped attachment leader ends between the baseline de and groupes. The first transcription includes those visible context words, while the second transcribes just the inserted letter; retain the full first scope.')
c('b15','The short left stroke is heavily inked, the following run is compressed and almost horizontal, and a detached mark lies above that run. This permits a compressed ici, but the small left loop and upper mark also allow où. Reopening the wider original c13 does not isolate enough letter bodies to decide. Replace the previously medium-confidence ici with explicit ici|où; do not decide from the sentence’s grammar.',r'\unsure{ici|où}')
c('b16','Two thin numeral strokes each have an oblique entry and a near-vertical shaft: 11. Their position and lighter hand identify marginal foliation. The second omitted only the margin wrapper.')
(R/'documentation/149_scan012_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan012.tex';s=p.read_text().replace(r'\unsure{\mathbb Q|k}',r'\unsure{\mathbb Q|k|\mathbb C}').replace(r'\deleted{complexe}',r'\deleted{\unsure{complexe|complexes}}').replace('(ici $n=',r'(\unsure{ici|où} $n=');p.write_text(s)
p=R/'reviews/149_scan012.json';r=json.loads(p.read_text());cs={x['id']:x for x in r['changes']}
def box(b):
 q=next(q for q in r['audit_boxes'] if q['box']==b);return[q[k] for k in ('x0','y0','x1','y1')]
cs['c03']['final']=cs['c03']['final'].replace(r'\unsure{\mathbb Q|k}',r'\unsure{\mathbb Q|k|\mathbb C}')
cs['c03'].update(evidence=ch['b05']['evidence'],crop='crops/149_scan012_second_b05.png',box=box('b05'))
cs['c12'].update(final=r'\unsure{ici|où}',evidence=ch['b15']['evidence'],confidence='low',against_C=True,against_H=True,crop='crops/149_scan012_second_b15.png',box=box('b15'))
r['changes'].append({'id':'audit_b08_plural','place':'L8, cancelled complexe(s)','C':r'\deleted{complexe}','H':r'\struck{complexe}','final':r'\deleted{\unsure{complexe|complexes}}','evidence':ch['b08']['evidence'],'crop':'crops/149_scan012_second_b08.png','box':box('b08'),'confidence':'low','against_C':True,'against_H':True,'kind':'misread word','error_category':'Struck text','marked_in_H':False,'mathematical':False})
for d in r['decisions']:
 if d['id']=='M0979':d.update(reading=d['reading'].replace(r'\unsure{\mathbb Q|k}',r'\unsure{\mathbb Q|k|\mathbb C}'),evidence=ch['b05']['evidence'],crop='crops/149_scan012_second_b05.png',box=box('b05'))
for d in r['doubts']:
 if d['place']=='L6, extra low glyph beneath C':d.update(reading=r'\underset{\unsure{\mathbb Q|k|\mathbb C}}{\mathbb C}',alternatives=[r'\mathbb Q','k',r'\mathbb C'],reason=ch['b05']['evidence'])
 if d['place']=='L20, final parenthesis':d.update(reading=r'\unsure{ici|où}',alternatives=['ici','où'],confidence='low',reason=ch['b15']['evidence'])
r['doubts'].append({'place':'L8, cancelled word before commun','reading':r'\deleted{\unsure{complexe|complexes}}','alternatives':['complexe','complexes'],'confidence':'low','reason':ch['b08']['evidence']})
for x in r['inventory']:
 if x['element']=='d02':x['first_words_or_objects']=r'\deleted{\unsure{complexe|complexes}}'
for x in r['diff_coverage']:
 if x['row']==5:x['reason']='H omits a visible low glyph beneath C; the independent audit retains Q/k/C as alternatives for that lower glyph.'
 if x['row']==16:x['reason']='The independent audit leaves ici|où explicitly unresolved; neither witness settles the compressed strokes.'
r['notes'].append('Independent audit: all13 differing boxes and all50 token spans were adjudicated against saved enlargements. Three boxes change: the lower glyph gains C as an alternative, cancelled complexe(s) gains explicit ending uncertainty, and ici becomes ici|où. The plural géométriques, Q/K overlap, margin au and K/K_0, lowercase pi and inserted n are retained. The independent readings remain frozen, including their differing scope and TeX syntax.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
with (R/'reader_assignments.tsv').open('a') as f:f.write('second\t023\treader_b\tsecond/149_scan023_boxes.tsv\n')
