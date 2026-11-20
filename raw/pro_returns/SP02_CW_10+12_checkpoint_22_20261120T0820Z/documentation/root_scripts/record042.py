import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-02',10,42);ch=r.change
r.edit(r'\unsure{opérateurs|opératerus}',r'\unsure{opératerus|opérateurs}')
r.edit(r'\mathbb{H}',r'\unsure{\mathbb{H}|H}')
r.edit(r'i\handwritten{\geq}j',r'i\handwritten{\geqslant}j')
r.edit(r'\deleted{\unsure{l\'exp|l\'ex}}'.replace('\\\'','\''),r'\deleted{l\'exp}'.replace('\\\'','\''))
r.edit(r'\deleted{\unsure{concernant|couvrant}}',r'\deleted{concernant}')
r.edit('8.8.2, 8.8.3 et','8.8.2, 8 8.3 et')
r.edit('résulte de la propriété',r'résulte de l\deleted{\unsure{j|f}}a propriété')
r.edit(r'sous $\unsure{G}\inserted',r'sous $G\inserted')
def margin(formula,upper):
 start=r'}\margin{\figure{\begin{tikzpicture}[x=.5cm,y=.5cm]\node at (0,0) {$'+formula+r'$};'
 if upper:
  path=r'\draw (1.5,1.2) -- (1.3,.6) .. controls (.3,.8) and (-.7,.85) .. (-1.1,.7) -- (-1.2,.5);\draw (-1.5,.25) .. controls (-1.7,-.1) and (-2,-.3) .. (-1.5,-.7) .. controls (-.6,-1) and (.3,-.4) .. (1,-.7) .. controls (1.35,-.9) and (1.4,-1.1) .. (1.45,-1.5);'
 else:
  path=r'\draw (1.5,1.2) .. controls (1.9,.2) and (.7,.8) .. (-.5,.5) .. controls (-2,.3) and (-2,-.7) .. (-1.3,-.8) .. controls (-.3,-1) and (.5,-.8) .. (1.2,-.9) .. controls (1.5,-1) and (1.6,-1.2) .. (1.7,-1.4);'
 return start+path+r'\end{tikzpicture}}}\uline{'
old=r'sous $\deleted{\unsure{G|H}}\inserted{G=G_j\handwritten{\times}_{S_j}S}$'
new=r'sous $\deleted{\unsure{H|G}}$'+margin(r'G=G_j\handwritten{\times}_{S_j}S',True)
r.edit(old,new)
old=r'sous $\deleted{\unsure{G_i}}\inserted{G_i=G_j\handwritten{\times}_{S_j}S_i}$'
new=r'sous $\deleted{\unsure{G_i}}$'+margin(r'G_i=G_j\handwritten{\times}_{S_j}S_i',False)
r.edit(old,new)
ch('manuscript number','10','omitted','10','Handwritten 1 and closed oval 0.','number','omission')
ch('first split word',r'\unsure{opérateurs|opératerus}','opérateurs',r'\unsure{opératerus|opérateurs}','Right overtyped letter resembles u, before final s; preceding thick letter resembles r. Reversed typed ending remains first reading, with uncertainty.','operators','misread word','medium',True,True)
ch('base-change H',r'\mathbb{H}','H',r'\unsure{\mathbb{H}|H}','H has doubled thick strokes compared with nearby ordinary H_j; overprinting versus deliberate alphabet cannot be decided.','H','misread symbol or index','medium',True,True)
ch('first cancelled group',r'\deleted{\unsure{G|H}}',r'\struck{\ill{}}',r'\deleted{\unsure{H|G}}','Two long straight lower uprights suggest H beneath the dense hatching; G cannot be excluded.','cancel-G','readable ink left as \\ill{}','low',True,True,True)
for p,f in [('upper marginal replacement',r'G=G_j\times_{S_j}S'),('lower marginal replacement',r'G_i=G_j\times_{S_j}S_i')]:
 ch(p,'formula inline as insertion; outline omitted','formula marginal; outline omitted','marginal formula with TikZ enclosure','Typewritten formula in the left margin, enclosed by an irregular open-right pencil curve; geometry now reproduced.','margins','drawing or diagram','high',True,True)
ch('first parenthetical live G',r'\unsure{G}','G','G','Large G outline still readable below the cancelled inserted formula.','cancel-above','other','medium',True,False)
ch('cancelled inserted formula',r'\inserted{\deleted{\unsure{G=G_j\times_{S_j}S}}}',r'\struck{\ill{}} in baseline text',r'\inserted{\deleted{\unsure{G=G_j\times_{S_j}S}}}','Above-line G, equals and second G remain visible; subscripts and product heavily covered; entire formula remains doubtful.','cancel-above','insertion or placement','low',False,True,True)
ch('first parenthesis closure',r'\unsure{)}',')',r'\unsure{)}','Dense correction crossing the place of closing parenthesis; no isolated complete parenthesis recoverable.','cancel-above','other','low')
ch('comparison',r'\geq',r'\geqslant',r'\geqslant','Lower comparison stroke is distinctly slanted parallel to the lower arm.','statement','other','high',True,False)
ch('second cancelled group',r'\deleted{\unsure{G_i}}',r'\struck{\ill{}}',r'\deleted{\unsure{G_i}}','Initial G curve visible, but lower index buried in black diagonal strokes.','cancel-Gi','readable ink left as \\ill{}','low',False,True,True)
ch('assertion','underlined','no underline','underlined','Single rules beneath all six physical lines.','statement','omission')
ch('topology phrase','double underline','italic','double underline','Heavy second line directly under topology phrase, over the ordinary paragraph rule.','statement','other')
ch('second EGA number','8.8.3','8.8.3','8 8.3','The two initial eights are separated by a blank; the first dot is absent even at 5x.','ref-spacing','misread symbol or index','high',True,True)
ch('after EGA citation',r"\deleted{\unsure{l'exp|l'ex}}",r'\struck{\ill{}}',r"\deleted{l'exp}",'Distinct p descender after l-ex traces; final X is cancellation, not an added letter.','lexp','readable ink left as \\ill{}','high',True,True,True)
ch('la before propriété','la','la',r'l\deleted{\unsure{j|f}}a','A light tall stroke with upper dot/hook and lower leftward descender survives under the dark a; probable overwritten j, with f alternative.','la','omission','medium',True,True)
ch('cancelled word before couvrants',r'\deleted{\unsure{concernant|couvrant}}',r'\struck{\ill{}}',r'\deleted{concernant}','Ten typed letters c-o-n-c-e-r-n-a-n-t visible between X overstrikes.','couvrant','readable ink left as \\ill{}','high',True,True,True)
ch('lower-half pen drawing','TikZ intersecting strokes','omitted','TikZ intersecting strokes','Long descending nearly vertical line crosses the alternating broad lobes of a second pen stroke; no labels.','drawing','drawing or diagram')
for p,rd,alt,co in [('operators','opératerus','opérateurs','medium'),('first H',r'\mathbb{H}','H','medium'),('first cancelled group','H','G','low'),('cancelled inserted formula',r'G=G_j\times_{S_j}S','','low'),('first parenthesis',')','','low'),('second cancelled group','G_i','','low'),('under a in la','deleted j','deleted f','medium')]:r.doubt(p,rd,alt,co)
r.r['crops']=json.loads(Path('work/crops042.json').read_text())
r.crop('ref-spacing',[1139,613,1235,651],scale=5);r.crop('la',[622,681,675,724],scale=5)
for el,pos in [('upper-outline','around upper marginal formula'),('lower-outline','around lower marginal formula')]:
 r.r['inventory_extra'].append(dict(scan='10:042',sheet_kind='typescript',hand='unnamed hand',element=el,kind='drawing',position=pos,first_words_or_objects='irregular open-right enclosing pencil curve',transcribed='yes'))
r.notation('retraced capital H',r'\mathbb{H} | H','10/042 base-change H; compare retraced H on 10/041','ambiguous')
r.r['inspection_note']='Whole then both halves viewed; every body line, marginal formula, cancellation and drawing enlarged; C inventory matched and two omitted enclosing curves added. Shared witness omissions found in EGA punctuation and overwritten character under a. All C uncertainties resolved or explicitly retained.'
r.save('work/record042.json')
