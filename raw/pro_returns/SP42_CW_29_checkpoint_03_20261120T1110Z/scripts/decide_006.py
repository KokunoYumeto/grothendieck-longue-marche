from adjudication_helpers import *
d,rs,ts=start(6)
text=ts['R1'].replace(r'\uline{p.19 etc}\margin{!}',r'\reversemarginpar'+'\n'+r'\margin{!}\uline{p.19 etc}')
text=text.replace('p.33,34 etc ..',r'p.33,34 etc \unsure{..|:}')
text=text.replace(r'theor.9.4\quad',r'theor.9.4\unsure{.}\quad')
text=text.replace(r'J.P. M\unsure{urre}',r'J.P. Mu\unsure{rre}')
old=r'\margin{\figure{\begin{tikzpicture}\draw (0,0)--(-.05,.8);\draw (.12,-.05)--(.09,.65);\end{tikzpicture}}}'
new=r'\margin{\figure{\begin{tikzpicture}\draw (0,1.05)--(.12,0);\draw (.16,.84)--(.28,-.14);\end{tikzpicture}}}'
text=text.replace(old,new+'\n'+r'\normalmarginpar')
cropmap={1:'readers/scan006/R1/crops/07_foliation.jpg',2:'crops/scan006/01_p19_margin_underline.jpg',3:'crops/scan006/01_p19_margin_underline.jpg',4:'readers/scan006/R1/crops/01_cancelled_mark.jpg',5:'crops/scan006/02_zariski_underline.jpg',6:'readers/scan006/R2/crops/04_p33_separator.jpg',7:'crops/scan006/03_p43_gap.jpg',8:'readers/scan006/R2/crops/06_for_instance.jpg',9:'readers/scan006/R1/crops/04_fibres.jpg',10:'crops/scan006/04_p45_gap.jpg',11:'crops/scan006/05_margin_strokes.jpg',12:'readers/scan006/R1/crops/05_line_start_capitals.jpg',13:'readers/scan006/R1/crops/05_line_start_capitals.jpg',14:'readers/scan006/R1/crops/06_signature.jpg',15:'readers/scan006/R1/crops/06_signature.jpg'}
for i in range(1,16):
 r=row_from(rs['R1'],i,crop=cropmap[i])
 r['readers']={'R1':rs['R1']['differences'][i-1]['reading']}
 for k in ['R2','R3']:
  r['readers'][k]=rs[k]['differences'][(i if i<=11 else i-2)-1]['reading'] if i not in [12,13] else ('copy' if i==12 else 'manuscript')
 r['scan_shows']=r['scan_shows'].replace('Half A:','Main crop:').replace('Half B:','Main crop:')
 if i==1:r['scan_shows']='The handwritten numeral 2 is followed at lower right by a separate faint point. The main crop confirms the authorial foliation 2.; this is not the archival numeral.'
 if i==3:r.update(final=r'\margin{!}\uline{p.19 etc}',scan_shows='A tall vertical stroke and separate lower dot form ! in the left margin beside the underlined p.19 label, not beside the end of the paragraph. The final anchors it with the label and uses standard LaTeX left-margin placement.')
 if i==4:r['scan_shows']='A looped/hooked sign after one is crossed by several dark strokes; a separate live baseline period follows. The cancellation is definite, but the underlying question-mark candidate remains uncertain. The C doubt is retained.'
 if i==5:r['scan_shows']='The underline begins below Zariski and extends through topology; irreducible in has no underline. This is a difference in emphasis scope, not merely in the witnesses’ emphasis macros.'
 if i==6:r.update(final=r'\unsure{..|:}',against_c=False,confidence='medium',scan_shows='Two separate low points run down slightly to the right. Two periods are favoured, as R1, but a strongly oblique colon cannot be excluded, as C/R2/R3 retain. No long horizontal dash follows them. C’s doubt is retained.')
 if i==7:r.update(final=r'p.43 theor.9.4\unsure{.}\quad You',against_c=True,against_h=True,confidence='low',kind='misread symbol or index',scan_shows='The space before You contains no dash. In the same crop, main inspection finds a faint compact point immediately below-right of the final 4, comparable in tone with the internal decimal point. Its status as a final period rather than an incidental faint mark is unresolved, so it is retained with a local doubt. All three readers omitted this possible point; the original returns are unchanged.')
 if i==8:r['scan_shows']='The f has the same looped ascender and low body as the nearby f in satisfactory; it is lowercase for. A separate faint period precedes it.'
 if i==9:r['scan_shows']='The f, i, b and terminal s are separately visible. The two joined interior letters are compressed: re is favoured, but er remains possible. Main adopts R1/R3’s narrower doubt rather than R2/C’s whole-word scope.'
 if i==10:r['scan_shows']='A full stop follows etc; the intervening space before Is contains no horizontal dash.'
 if i==11:r.update(final=new,scan_shows='Two thin strokes stand in the left margin beside the appendix paragraph. Both descend slightly rightward; the left begins higher and is longer, and the right ends a little lower. R3’s TikZ proportions are adopted. Both C and the other readers already encode the same two-stroke drawing, so the proportional refinement is not a substantive change against C.')
 if i==12:r['scan_shows']='The open C-shaped initial is appreciably taller than the following o, with a broad upper arc. Capital C is the preferred visual reading, but an enlarged cursive lowercase c remains possible. Main retains R1’s explicit case alternatives over R2/R3’s unqualified lowercase.'
 if i==13:r['scan_shows']='The initial has a tall first ascent followed by two smaller humps. Its height favours M, while the similar first ascent in the within-line manuscript above prevents a secure case distinction. Main retains R1’s alternatives, without using sentence grammar to decide.'
 if i==14:r.update(final=r'J.P. Mu\unsure{rre}',scan_shows='J and P have identifiable stems and separate points; M is large and distinct, followed by a small open u-shaped join. The following low compressed waves do not securely separate r, r and e. Main agrees with R2/R3 in narrowing C’s doubt to rre; R1 had also included u.')
 if i==15:r.update(final=r'J.P. Mu\unsure{rre}\\',scan_shows='The final surname stroke runs continuously rightward. There is no detached point after it. H’s final signature period is not supported; C and all three readers omit it.')
 d['rows'].append(r)
d['doubts']=rs['R1']['remaining_doubts']
d['doubts'][-1].update(reading=r'J.P. Mu\unsure{rre}',reason='J.P. and Mu are identifiable; the terminal low waves do not securely separate rre.')
d['doubts'] += [dict(place='p.33,34 etc separator',reading=r'\unsure{..|:}',alternatives=[':'],confidence='medium',reason='Two low points favour periods; their slight diagonal alignment leaves an oblique colon possible.'),dict(place='After theor.9.4',reading=r'\unsure{.}',alternatives=['no final period'],confidence='low',reason='A faint compact point appears below-right of 4; its punctuation status is not certain.')]
for x in d['inventory']:
 if x['element']=='E09':x['first_words_or_objects']=r'p.33,34 etc \unsure{..|:} I did not see ... prop 7.4.'
 if x['element']=='E10':x['first_words_or_objects']=r'p.43 theor.9.4\unsure{.} You have mentioned ... constant fib\unsure{re|er}s ...'
 if x['element']=='E18':x['first_words_or_objects']=r'J.P. Mu\unsure{rre}; no final period'
d['notes']=rs['R3']['notes']
d['notes']['math_reading_decisions'] += ['The faint possible point after theor.9.4 is a punctuation doubt found in main adjudication, with no change to the theorem identifier.', 'No mathematical statement was proved, refuted or used as an established result in this page reading; CHECK_EVENTS receives no event.']
d['check_events']=[]
d['slips']=['The wording arbitrary crossings escapes and the continuation word to use else. are retained as written.']
d['workflow']=dict(brief='brief_v004_scan006.md',r1_crops=7,r2_crops=9,r3_crops=4,main_crops=5,main_reader_crops_viewed=7,feedback='Three independent whole-once and halves-once readings were compared. Main actually inspected seven existing reader crops and five new tight crops. One earlier oversized tool return attempted three images but was truncated before any was visible; it is not counted as an inspection. The foliation and cancellation were subsequently inspected successfully; the p.33 locus used R2’s existing crop. C’s four formal doubts all receive decisions. R1’s case alternatives are retained, R2/R3’s signature scope and retained separator doubt are adopted. Main alone noticed a possible final point after theor.9.4. R3’s left-margin positioning and two-stroke proportions are used. Next brief clarifies concise report indexing and physical margin-side placement; no reader return is altered.')
d['main_adjudication_complete']=True
save(d,text)
