"""Single-use scan015 decisions following personal crop inspection."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan015_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b01','The dark upper numeral has the cap, long diagonal stem and crossbar of 7. Retain the author-page wrapper; the second gives the same digit without that metadata.')
c('b02','Both two-leg signs match the small kernel pi forms on the preceding pages. Capitalizing only the first sign is not supported by a distinct letter size or alphabet contrast. Operatorname versus mathrm and TeX braces are representation differences; the prime, equality and singleton agree.')
c('b03','The insertion begins with a separate three-shaped letter with upper turn and lower bowl. It is distinct from the much longer curved attachment leader below the phrase; it cannot be omitted as a leader fragment. Retain its Z/script-Z uncertainty and the following dans pi. The last letter is the same kernel pi form as b02.')
c('b07','The tall loop is l; its low continuation and terminal hook can be le or les. A dark s-like remnant at the left and retraced baseline also allow, but do not establish, an overwritten son. Preserve uncertainty in both the ending and the correction state. Que and centre are surrounding context included only by the second reader.',r'\unsure{\deleted{son}le|le|les}')
c('b08','The diagonal marginal text has accented a, v, accented e, dotted i, a long descending f and the remaining low run of vérifier. Both readings agree on the words; retain the marginal wrapper.')
c('b10','The first letter has the same rounded upper turn and lower bowl as the inserted centralizer name, without an alphabet contrast sufficient to choose ordinary or script Z. Reordering those alternatives changes no visible reading. The rightward arrowhead, quotient slash, two pi signs and prime agree.')
c('b11','Donc and the following rounded Z form are visible. The two readers retain the same ordinary/script alphabet alternatives in reverse order; keep the established order.')
c('b12','The second marginal note repeats the accented a, v/e/i, long f and final run. Its diagonal location is marginal, so the wrapper is retained. No lexical disagreement remains.')
c('b13','Two horizontal bars are crossed by a near-vertical curved stroke, followed by a hooked upright 1. Ne and neq are equivalent TeX commands for these same marks.')
c('b14','Under the horizontal strike the initial s, closed a, single n shoulder and terminal s return remain distinguishable. Read the cancelled sans without a residual word doubt. The separate raised a has a clear grave accent and remains inserted.',r'\deleted{sans}\inserted{à}')
c('b15','The cancelled run begins with tall t, oval o and compressed r/s. The remaining loops allow torsion or an abbreviated tors. Immediately to the right is a compact two-lobed punctuation mark, allowing colon or point; the two farther dots below-right are separate and are not appended to the text. Keep that punctuation inside the uncertain cancelled run. The raised centre is clear.',r'\deleted{\unsure{torsion|tors}\unsure{:|.}}\inserted{centre}')
c('b17','The raised parenthesis starts with an o/u-like run and tall l with reduced e, not the longer cate sequence; a detached accent remains uncertain. The next word has crossed t, low o, descending p and os ending, supporting topos rather than type/types. B is followed below by a K with diagonal arms, not a two-leg pi. The long curve below the phrase bends down as its insertion leader, separate from zigzag cancellation across barred K and slash in the groupoid index. The last K is only partly overlapped, so its existing live/cancelled uncertainty remains. Est and both parentheses are visible.')
c('b18','The cancelled line starts with an open curve followed by a descending loop, then a long obscured run and a later tall stem. Equivalence is a possible reading alongside que l’on/question, but the strike prevents a secure complete word. Above it, the replacement begins d-e-f; no separate acute accent over e is secure. Its final dotted i has a low continuation that could be terminal e. Preserve defini/definie without supplying an accent. The remaining à isom is distinct and agrees.',r"\deleted{\unsure{que l'on|question|équivalence}}\inserted{\unsure{defini|definie} à isom}")
c('b20','The small pale lower-left digits are 1 and open 4. They differ in scale and hand from the dark author number 7; retain the foliation as a margin item.')
(R/'documentation/149_scan015_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan015.tex';s=p.read_text()
repls={first['b07']:ch['b07']['final'],first['b14']:ch['b14']['final'],first['b15']:ch['b15']['final'],first['b18']:ch['b18']['final']}
for a,b in repls.items():assert a in s,a;s=s.replace(a,b)
p.write_text(s)
p=R/'reviews/149_scan015.json';r=json.loads(p.read_text())
for x in r['changes']:
 if x['id']=='c01':x.update(final=ch['b07']['final'],evidence=ch['b07']['evidence'])
 if x['id']=='c03':x.update(final=ch['b15']['final'].split(r'\inserted')[0],evidence=ch['b15']['evidence'],against_C=True)
 if x['id']=='c07':x.update(final=ch['b18']['final'],evidence=ch['b18']['evidence'],against_C=True)
 if x['id']=='c08':x['final']=r'\inserted{\unsure{defini|definie} à isom} unique près';x['against_C']=True;x['evidence']+=' Independent audit b18 leaves the replacement ending and absent accent explicit.'
for x in r['doubts']:
 if x['place']=='L8, word before centre':x.update(reading=ch['b07']['final'],alternatives=[r'\deleted{son}le','le','les'],reason=ch['b07']['evidence'])
 if x['place']=='Start of L16, cancelled word':x.update(reading=ch['b15']['final'].split(r'\inserted')[0],alternatives=['torsion','tors',':','.'],reason=ch['b15']['evidence'])
 if x['place']=='L18, cancelled phrase':x.update(reading=r"\deleted{\unsure{que l'on|question|équivalence}}",alternatives=["que l'on",'question','équivalence'],reason=ch['b18']['evidence'])
r['doubts']=[x for x in r['doubts'] if x['place']!='End of L15, cancelled word']
r['doubts'].append({'place':'Raised replacement above L18, first word','reading':r'\unsure{defini|definie}','alternatives':['defini','definie'],'confidence':'low','reason':ch['b18']['evidence']})
b=next(x for x in r['audit_boxes'] if x['box']=='b14');coords=[b[k] for k in ('x0','y0','x1','y1')]
r['changes'].append({'id':'audit_b14_sans','place':'End of L15, cancelled word','C':r'\deleted{\unsure{sans}}','H':r'\struck{sans}','final':r'\deleted{sans}','evidence':ch['b14']['evidence'],'crop':'crops/149_scan015_second_b14.png','box':coords,'confidence':'high','against_C':True,'against_H':False,'kind':'resolved uncertainty','error_category':'Struck text','marked_in_H':False,'mathematical':False})
r.setdefault('resolved_observations',[]).append({'place':'End of L15, cancelled word','reading':r'\deleted{sans}','reason':ch['b14']['evidence']})
for x in r['inventory']:
 if x['element']=='d01':x['first_words_or_objects']=ch['b07']['final']
 if x['element']=='d02':x['first_words_or_objects']=r'\deleted{sans}'
 if x['element']=='d03':x['first_words_or_objects']=ch['b15']['final'].split(r'\inserted')[0]
 if x['element']=='d05':x['first_words_or_objects']=r"\deleted{\unsure{que l'on|question|équivalence}}"
 if x['element']=='i07':x['first_words_or_objects']=r'\inserted{\unsure{defini|definie} à isom}'
r['notes'].append('Independent audit: all14 differing boxes and36 token spans personally inspected. Four boxes change: le/les and correction-state uncertainty; cancelled sans resolved; punctuation and abbreviation ambiguity in the cancelled torsion run; expanded uncertainty in the cancelled phrase and replacement defini/definie. The centralizer symbol is distinct from its leader, and ou/où le topos B_K remains the supported inserted phrase. No new mathematical check was performed during this reading audit.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
