from pathlib import Path
import json,sys,copy
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from record_audit import build_revision,stable_changes
key='B10-03_10_scan054';out=Path('SP02_CW_10+12');s=json.loads((out/f'documentation/audit_sessions/{key}_audit001.json').read_text());r=json.loads((out/f'documentation/page_records/{key}.json').read_text());c=stable_changes(r,key);t=(out/f'pages/{key}.tex').read_text()
p=dict(audit_id=s['audit_id'],baseline_page_sha256=s['baseline_page_sha256'],audit_reading_complete=True,audit_inventory_confirmed=True,edits=[],upsert_changes=[])
def edit(old,new,count=1):p['edits'].append(dict(old=old,new=new,count=count))
def update(i,**kw):
 z=copy.deepcopy(c[i]);z.update(kw);p['upsert_changes'].append(z)
edit('Théorème 11.16.',r'Théorème \handwritten{11.16}.')
edit(r'So\unsure{i|e}ent',r'So\unsure{e|i}ent')
edit('e_o',r'e_{\unsure{o|0}}',t.count('e_o'))
edit('a_i^o',r'a_i^{\unsure{o|0}}')
edit(' I$, autrement dit',r' I$, autre-\linebreak ment dit')
old_margin=r'\draw[rotate=-25] (0,0) ellipse (1.3 and 2);'
new_margin=r'\draw[rotate=25] (-1,1.3) .. controls (.3,1.65) and (1.8,1.6) .. (1.85,.4) .. controls (1.9,-.6) and (.6,-1.4) .. (-.8,-1.4) .. controls (-1.6,-1.4) and (-2,-1.1) .. (-2,-.7);'
edit(old_margin,new_margin)
old_join=r'\draw (1,0.8) .. controls (-0.5,1.5) and (-1,0) .. (1,0.2);'
new_join=r'\draw (1,.8) .. controls (.3,1.25) and (-.7,1.1) .. (-.8,.45);\draw (-.8,.25) .. controls (-.4,.05) and (.4,.1) .. (1.15,.3);'
edit(old_join,new_join,2)
axiome=r"L'axio\begin{tikzpicture}[x=1cm,y=1cm,baseline=(a.base)]\node[inner sep=0pt] (a) at (0,0) {\unsure{m|n}};\draw (-.12,.05)--(.18,.16);\end{tikzpicture}e"
edit("L'axiome",axiome)
smallmark=r'\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw[thin] (0,.02)--(.18,-.01);\end{tikzpicture}}}'
edit('si on pose $', 'si on pose '+smallmark+'$')
update(3,final=r'So\unsure{e|i}ent',shows='The third position has a clearly rounded e-like body and crossbar, together with an i dot and stem. The visible body favours e; the overprinting does not establish the order of the two impressions. The uncertainty is retained without grammatical normalization.',crop='audit-Soient')
update(12,final=r'pas à \unsure{l|la} ligne in an open enclosing curve',shows='The upright enlarged note has pas à, then a looped l with a short trailing turn; an additional a remains insecure. The enclosure starts above pas, bends around the right and bottom, and stops at the left page edge. No closing left arc is visible.',crop='audit-same-line;audit-margin-wide;audit-margin-upright')
for i,cr in [(13,'audit-join-1'),(14,'audit-join-2')]:update(i,final='Two separated curved strokes in TikZ',shows='A gap separates the left end of the upper curved stroke from the beginning of the lower return. Both strokes are reproduced independently, rather than joined through the gap.',crop=cr,against_C=True)
update(22,place='all round basis indices and coefficient exponent',final=r'\unsure{o|0} at every occurrence',shows='The first basis index, the exterior-product vector, the exponent of a_i, and both vectors in the sigma sentence all use an upright closed oval with no secure distinction between letter o and digit zero. Each occurrence is qualified in place.',crop='audit-index;audit-basis;audit-e-wedge;audit-coefficients;audit-sigma-values',against_C=True)
rows=[('physical line division in quotient paragraph','autrement','autrement',r'autre-\linebreak ment','The hyphen is visible after autre at the right edge; ment starts the following physical line.','audit-autre-division;audit-notons','high','other'),('overworked letter in final axiome','axiome','axiome',axiome,'The position after axio has dense overlapping upright and arched strokes, with an oblique stroke crossing its upper part. The visible body favours m but n remains possible; the crossing stroke is drawn without asserting an unsupported correction sequence.','audit-axiome','medium','misread word'),('faint short mark left of sigma formula','omitted','omitted','short oblique dash in TikZ, function unresolved','A short grey stroke is visible to the left of the sigma definition. It is preserved without assigning punctuation or a mathematical function; an incidental surface mark remains possible.','audit-thin-mark;audit-exterior2','low','drawing or diagram')]
for no,row in enumerate(rows,27):
 place,C,H,final,shows,crop,confidence,kind=row;p['upsert_changes'].append(dict(id=key+f'-L{no:03}',place=place,C=C,H=H,final=final,shows=shows,crop=crop,confidence=confidence,against_C=True,against_H=True,marked_in_H=False,kind=kind,consequential=False))
p['remaining_doubts']=copy.deepcopy(r['remaining_doubts'])
for d in p['remaining_doubts']:
 if d['line']=='opening word':d.update(reading='Soeent',alternatives='Soient',comment='Rounded body and crossbar favour e; superposed i dot and stem remain, with no secure impression order.')
 if d['line']=='first basis index':d.update(line='all round basis indices and coefficient exponent',comment='Every occurrence is qualified in place; no typed oval distinguishes o from zero securely.')
p['remaining_doubts'] += [dict(line='final axiome overworked letter',reading='m',alternatives='n',confidence='medium',comment='Overtyping and the oblique crossing do not establish the underlying character or correction order.'),dict(line='short grey mark left of sigma',reading='short stroke',alternatives='incidental surface mark',confidence='low',comment='Preserved as a drawing without assigning meaning.')]
p['inventory_patches']={}
for v in r['inventory_resolved']:
 if v['hand'] in ['unknown','unnamed hand']:p['inventory_patches'].setdefault(v['element'],{}).update(hand='another unnamed hand')
for el in ['join-1','join-2']:p['inventory_patches'].setdefault(el,{}).update(first_words_or_objects='upper curved stroke and separate lower return')
p['inventory_patches'].setdefault('same-line',{}).update(first_words_or_objects='pas à l|la ligne in open enclosure')
p['inventory_extra']=[]
for el,hand,kind,pos,words in [('archive','another unnamed hand','margin note','bottom left','archive folio 53 retained in comment'),('heading-number','his hand','text','theorem heading','11.16'),('axiome','another unnamed hand','drawing','last line, overworked m/n','overlapping letter with oblique crossing'),('thin-mark','another unnamed hand','drawing','left of sigma definition','short faint stroke')]:p['inventory_extra'].append(dict(scan='10:054',sheet_kind='typescript',hand=hand,element='audit-'+el,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
p['notation_updates_add']=[dict(sign='handwritten statement numbers',form=r'\handwritten{11.16}',attestations='10/054 theorem heading',status='read')]
p['crops_upsert']=json.loads(Path('work/audit10_054_crops.json').read_text())
p['observations']='Root completed the ordered second reading after viewing the whole source and both actual supplied halves before opening the text. All 45 fresh crops were personally inspected, including the rotated manuscript number, the marginal instruction at two additional rotations, every disagreement and doubt, all consequential formulas, cancellations and insertions. The dense quotient formula has all the parentheses transcribed: the first closing curve touches the tensor sign but is present. The three cancelled Exp. prefixes, cancelled section sign, clipped ad, readable cancelled sat, deleted character clause and parenthesis, unaccented inserted ideal, absent period before Alors, baseline composition o, two-dot basis ellipsis, double-bar inequalities and final reference 4.7.2 are retained from the ink. The handwritten theorem number is tagged and inventoried without a macro-only collation row. The opening overprint now prefers its visible e body before i; all repeated round indices and the coefficient exponent carry their local uncertainty. The physical autre-/ment division is restored. Both paragraph join marks are split at their visible left gaps, and the marginal enclosure remains open. The overworked letter in axiome and the separate short grey mark are preserved with doubts. All inventory elements were checked top to bottom; manuscript 22 and archive folio 53 remain distinct. Eight doubt entries remain. No context or proof checking was used.'
Path('work/audit10_054.json').write_text(json.dumps(p,ensure_ascii=False,indent=2));_,new=build_revision(p,s,r,t);Path('work/audited10_054.tex').write_text(new)
print('edits',len(p['edits']),'upserts',len(p['upsert_changes']),'fresh crops',len(p['crops_upsert']))
