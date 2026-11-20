from pathlib import Path
import json,csv,datetime
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'review/scan004_review.json').read_text());t=(R/'review/scan004_proposed.tex').read_text()
old=r'\uline{\deleted{\unsure{pré}} \unsure{premières}}'
heading=r'\uline{\unsure{pre|pré}\deleted{\unsure{l|li}}mières}'
assert old in t
t=t.replace(old,heading).replace(r'F\vee\unsure{C|G}',r'F\vee C').replace(r"\uline{fine}\unsure{''}",r'\uline{fine}')
km={
'spurious punctuation in H':'text not on the page','word':'misread word','words':'misread word','resolved C doubt':'other',
'numeral decoration':'other','word omission/addition':'text not on the page','alphabet doubt retained':'misread symbol or index',
'struck word doubt retained':'misread word','punctuation':'other','notation word':'misread symbol or index',
'heading with unresolved overwrite':'deletion state (struck given live or live given struck)','alphabet':'misread symbol or index',
'word doubt retained':'misread word','word joining':'other','accent':'other','underline extent':'other',
'marginal words':r'readable ink left as \ill{}','quotation shape and underlining':'other','insertion attachment':'insertion or placement',
'deletion and insertion state':'deletion state (struck given live or live given struck)','abbreviation retained':'abbreviation expanded or spelling modernised',
'whole-formula doubt retained':'misread symbol or index','connector versus punctuation':'insertion or placement','ending':'misread word',
'words and resolved C doubt':'misread word','marginal word doubt retained':'misread word','label form':'other',
'formula letter':'misread symbol or index','sign placement':'other','underlining and quotation shape':'other','deleted material':'omission'}
cs=[]
for c in d['changes']:
 c['reader_kind']=c['kind'];c['kind']=km[c['kind']];c['crop']=c['crop'].removeprefix('out/')
 if c['id'] in ['S004-004','S004-008','S004-035','S004-038']:c['against_C']=False
 c['consequential']=c['id'] in ['S004-013','S004-023','S004-027','S004-038','S004-039','S004-043']
 if c['id']=='S004-014':
  c.update(final=heading,against_C=True,against_H=True,confidence='low',scan_shows='The live initial p-r-e sequence is left of the dark crossing; the continuation mières is to its right. The cancellation is internal at the junction, not a separate cancelled pré preceding another complete word. A tall narrow underlying stroke can be l or li, but the crossing prevents a letter-by-letter recovery. The possible first accent and cancelled letters remain explicitly doubtful. There is no full préliminaires sequence.')
 if c['id']=='S004-039':
  c.update(final=r'F\vee C',confidence='high',scan_shows='The complete expression has F, a low vee, and a large open C. Its bottom stroke ends without the inward return or descending terminal present on the neighboring explicit G forms in rows (a) and (b). C’s primary C is retained and its doubt removed on this whole-expression crop. The mathematical context calls for the other argument G; the clear written C is not repaired.')
 if c['id']=='S004-045':
  c.update(final=r'figure ``\uline{intersection} \uline{fine} (quand elle existe) : Inf pour $\ll$.',against_C=True,confidence='high',scan_shows='Both words have separate underlines. A pair of raised opening strokes precedes intersection. The space after fine and before the opening parenthesis contains no pair of closing quotation strokes; the visible high loop above fine belongs to the Inf descender from the preceding line. The closing marks supplied by both witnesses are omitted.')
 cs.append(c)
# Each separate source location gets its own record.
x=next(c for c in cs if c['id']=='S004-025');cs.remove(x)
for i,word in enumerate(['figure','engendrée','réunion','somme'],1):
 a=dict(x);a['id']=f'S004-025-{i}';a['place']='row (a), '+word+' typography'
 a['C']=r'\uline{'+word+'}' if i==1 else "``\\uline{"+word+"}''"
 a['H']=word if i==1 else '« '+word+' »'
 a['final']=a['C'];a['scan_shows']='A separate horizontal underline lies below '+word+'.'+(' Raised paired quotation ticks enclose the word; they are not guillemet chevrons.' if i>1 else '')
 cs.append(a)
x=next(c for c in cs if c['id']=='S004-042');cs.remove(x)
for i,(letter,crop,box) in enumerate([('a','a_formula',[377,1528,884,1638]),('b','b_formula',[382,1879,922,2018]),('c','c_formula',[380,2094,947,2209]),('d','d_formula',[366,2220,563,2313])],1):
 a=dict(x);a.update(id=f'S004-042-{i}',place='row ('+letter+'), circled label',C='circled '+letter+(' (letter doubtful)' if i>2 else ''),H='('+letter+')',final=r'\textcircled{\scriptsize '+(r'\unsure{'+letter+'}' if i>2 else letter)+'}',crop='crops/scan004_'+crop+'.png',box=box,scan_shows='A continuous oval encloses the letter, rather than two separate parentheses.'+(' The inner form touches the enclosing stroke and remains uncertain.' if i>2 else ' The inner letter is readable.'))
 cs.append(a)
x=next(c for c in cs if c['id']=='S004-047');cs.remove(x)
for i,(place,crop,box) in enumerate([('row (d), subscript','d_formula',[366,2220,563,2313]),('row (d), prose occurrence','d_text',[969,2209,1650,2343])],1):
 a=dict(x);a.update(id=f'S004-047-{i}',place=place,crop='crops/scan004_'+crop+'.png',box=box,scan_shows='The F has the curved lower hook of the defining script capital. The same script/calligraphic mapping is retained, with uncertainty registered at the first occurrence; H chooses a Gothic font.')
 cs.append(a)
d['changes']=sorted(cs,key=lambda c:c['id'])
d['doubts']=[x for x in d['doubts'] if x['place'] not in ['heading: cancelled material and its scope','heading: live word','row (b), F∨C/G','row (c), closing paired quotation mark after fine']]
d['doubts'].insert(2,dict(place='heading, prefix and internal cancellation',reading=r'\unsure{pre|pré}\deleted{\unsure{l|li}}mières',alternatives=['possible accent above initial e','one or two cancelled letters at the junction'],confidence='low',reason='Live pre and final mières surround the cancellation. Its exact underlying letters and overwritten accent remain unclear. This corrects C’s deletion boundary without claiming to recover every cancelled stroke. Crop crops/scan004_heading.png [348,728,892,831].'))
for e in d['inventory']:
 old=e['kind']
 if 'note' in e['element']:e['kind']='margin note'
 elif 'operation' in e['element'] or e['element'] in ['primitive data','axiom']:e['kind']='display'
 else:e['kind']='text'
 if e['element']=='addition to operation (b)':e['kind']='insertion'
 if e['element']=='cancelled short group':e['kind']='deletion'
d['inventory'] += [
 dict(element='Cancellation after L',kind='deletion',position='Opening block, after lieux L',first_words_or_objects='ou/de/ce, uncertain'),
 dict(element='Internal heading cancellation',kind='deletion',position='Between pre and mières',first_words_or_objects='l/li, uncertain'),
 dict(element='Cancelled marginal heading',kind='deletion',position='First lower left note',first_words_or_objects='Question, uncertain'),
 dict(element='Replacement marginal heading',kind='insertion',position='Above cancelled Question',first_words_or_objects='NB.')]
d['root_adjudication']={'reader':'GPT-6 Astra Pro root; effort not exposed','viewed':'whole image once, both halves once, all thirty saved reader crops','decisions':['Corrected heading cancellation boundary: pre is live; a narrow cancelled group lies before mières. Exact letters and possible first accent remain uncertain.','Removed unsupported closing quotes after intersection fine; the high adjacent stroke belongs to the preceding Inf.','Resolved the large C in the row-(b) existence condition from its flat open form, retaining the written letter although G is mathematically expected.','Retained small c/G, alphabet, crowded row-label and cancelled-word doubts.','Preserved source singular endings and abbreviations, and accepted the insertion attachment to row (b).']}
fix={
'page_number':'3','reste_muet':'je suis resté muet','reference':r'GF $\underline{\overline{\mathrm{VI}}}$',
'comme_figure':'comme figure','lieux_deleted':r"l'ens. des lieux $\unsure{L|\mathcal L}$ \deleted{\unsure{ou|de|ce}}",
'cela_quon_a':"cela signifie qu'on a un",'ensembliste_close':'ensembliste),','mulomb':r'$\mathrm{mulomb}(F)$',
'heading':r'\uline{Données} '+heading+' :',
'figure_alphabet':r'$\unsure{\mathscr F|\mathcal F}$ ensemble de figures',
'relation':r"\unsure{rellation|relation} d'\uline{inclusion} \unsure{de|des} figures",
'inclusion_formula':r"$F\leq G\ \overset{\text{\unsure{déf|def}}}{\Longleftrightarrow}\ F\ \text{sous figure de }G$",
'raffinement_formula':r'$F\ll G\ \overset{\text{def}}{\Longleftrightarrow}\ F\ \text{raffine }G$',
'axiom':r'\uline{At} 0 $F\leq G\Longrightarrow F\ll G$',
'margin_at4':r'\margin{NB. Ce sera aussi contenu dans \uline{At}~4 plus bas}',
'axiome':"-- axiome si évident que je ne l'avais pas inclus dans les axiomes numérotés.",
'a_formula':r'\textcircled{\scriptsize a} $F\vee G$ ou $F\cup G$',
'a_quotes':r'''\uline{figure} ``\uline{engendrée}'' ou ``\uline{réunion}'' ou ``\uline{somme}'' : c'est le sup''',
'a_exists':r"au sens de $\leq$ (quand il existe\unsure{)|\}} -- auquel cas c'est aussi un sup pour $\ll$",
'margin_question':r"\margin{\deleted{\unsure{Question}}\inserted{NB.} : Si $(F,G)$ ont un sup pour $\ll$ (c'est tjrs le cas dans le cas ensembliste $\mathrm{Fig}(L)$), ce n'est pas néc. un sup pour $\leq$}",
'margin_tilde':r'\margin{\uline{NB} $\widetilde{F\cap G}=\widetilde F\cap\widetilde G$}',
'b_formula':r'\textcircled{\scriptsize b} $F\wedge G$ ou $F\cap G$ $(=\mathrm{Inf}^{\leq}(F,\unsure{c|G}))$',
'b_text':r"figure \uline{intersection}\inserted{ou Inf pour $\leq$} -- existe toujours \unsure{(|et (}$\overline{\mathrm m}$ pour familles infinie (non vide)) ; quand en $=$ temps $F\vee C$ existe, alors c'est aussi le Inf pour $\ll$.",
'margin_existe':r'\margin{\uline{NB} Existe dans le cas ensembliste $\mathrm{Fig}(L)$ et dans le cas \unsure{mechisé|méchisé}}',
'c_formula':r'\textcircled{\scriptsize\unsure{c}} $F\mathbin{\ldotp}G$ $(=\mathrm{Inf}^{\ll}(F,c))$',
'c_text':r'''figure ``\uline{intersection} \uline{fine} (quand elle existe) : Inf pour $\ll$.''',
'deleted_short':r'\deleted{\unsure{G|CG}}',
'd_formula':r'\textcircled{\scriptsize\unsure{d}} $\varnothing_{\mathscr F}$',
'd_text':r'figure vide : plus petit élément de $\mathscr F$ (pour $\leq$ \uline{et} pour $\ll$)',
'opening_start':'(et'}
bs=[]
for b in d['second_boxes']:
 old=b['box'];key=old.removeprefix('scan004_');b['reading']=fix[key];b['source_box_id']=old;b['box']=f'B{len(bs)+1:03d}'
 if key.startswith('margin'):b['kind']='entire marginal note; include any cancellations, additions and formulae'
 elif key in ['heading','deleted_short','lieux_deleted']:b['kind']='text with cancellation; read visible live and cancelled ink'
 elif key in ['figure_alphabet','inclusion_formula','raffinement_formula','axiom','a_formula','b_formula','c_formula','d_formula']:b['kind']='whole mathematical expression with its label and attached text'
 elif key=='b_text':b['kind']='whole text block and insertion; include mathematical expression'
 elif key=='page_number':b['kind']='handwritten number'
 else:b['kind']='word or phrase; include visible punctuation and underlining'
 bs.append(b)
d['second_boxes']=bs
(R/'review/scan004_final.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(R/'pages/H156-01_156-7_scan004.tex').write_text(t)
base=R/'second/H156-01_156-7_scan004'
for suffix,cols in [('_boxes.tsv',['box','kind','x0','y0','x1','y1']),('_first.tsv',['box','reading'])]:
 with Path(str(base)+suffix).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(bs)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'review/root_visual_log.tsv').open('a') as f:
 for p in sorted((R/'crops').glob('scan004_*.png')):f.write(f'4\tcrops/{p.name}\t{now}\troot direct crop inspection\n')
 f.write(f'4\twhole + a + b\t{now}\troot layout and continuous reading\n')
print(len(cs),'records;',len(bs),'blind boxes')
