from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan090';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
def bracket(term,label):return r'\underset{'+label+r'}{\begin{tikzpicture}[baseline=(term.base)]\node[inner sep=0pt] (term) {$'+term+r'$};\draw ([yshift=-1pt]term.south west) -- ([yshift=-3pt]term.south west) -- ([yshift=-3pt]term.south east) -- ([yshift=-1pt]term.south east);\end{tikzpicture}}'
a84=r'\underbrace{\bar J\cap\widetilde J}_{\substack{\Vert\,\mathrm{déf}\\B(J)}}';z84=bracket(r'\bar J\cap\widetilde J',r'\substack{\Vert\,\mathrm{déf}\\B(J)}')
aK=r'\underbrace{\bar K\cap\widetilde K}_{B(K)}';zK=bracket(r'\bar K\cap\widetilde K','B(K)')
aJ=r'\underbrace{\bar J\cap\widetilde J}_{B(J)}';zJ=bracket(r'\bar J\cap\widetilde J','B(J)')
reps=[(r'que \deleted{\unsure{pour}} $','que $'),('aussi alors,',r'aussi, \unsure{donc|alors},'),(r'de $I$. \uline{C}',r'de $I$, \uline{C}'),(r'\deleted{\unsure{une propriété}}',r'\deleted{\unsure{une propriété|une prop.|une top.}}'),(a84,z84),(aK,zK),(aJ,zJ),(r"\deleted{\unsure{l'inclusion}}",r"\deleted{\unsure{inclusion|l'inclusion}}"),(r'\inserted{avec $J\prec K$,}',r'\inserted{\unsure{avec|on a} $J\prec K$,}'),(r'enfin \deleted{\unsure{et}} $K$',r'enfin \deleted{\unsure{et|\ell|\xi}} $-\unsure{K|K\prime}$'),(r"I'\unsure{\subset|=}\bar K",r"I'\unsure{=|\subset}\bar K"),(r"I'\subset\widetilde J$ \deleted{\unsure{et}}",r"I'\subset\widetilde J$ \deleted{\unsure{et|donc}}")]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
ch={x['id']:x for x in r['changes']}
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
ch['C02'].update(final=r'aussi, \unsure{donc|alors},',against_C=True,evidence='A detached comma follows aussi. The next word has a tall opening and low joined ending, favouring donc but not securely excluding alors; that local uncertainty is retained. H has the unwritten expansion dans ce cas.',crop=f'crops/{pg}_blind_B01.png',box=b['B01']['coordinates'],confidence='medium')
ch['C27'].update(final='(no independent canceled main word)',against_C=True,kind='text not on the page',error_kind='9 not on page',evidence='The rotated full marginal crop shows these strokes on the oblique tels que line, ending in its q descent and closing set brace. There is no separately recoverable main-line pour or independent canceled word; the marginal wording is already transcribed once in84.',crop=f'crops/{pg}_blind_B04.png',box=b['B04']['coordinates'],confidence='medium')
ch['C19']['final']=r"I'\unsure{=|\subset}\bar K"
ch['C20']['final']=r'\deleted{\unsure{et|donc}}'
ch['C17']['final']=r'enfin \deleted{\unsure{et|\ell|\xi}}'
for ident,place,C,H,final,box,why,kind,ek in [
 ('C29','End of opening de I phrase','de $I$.','de $I$.','de $I$,','B01','The final dark mark has a short descending tail. Preserve the comma before the next C\'est sentence.','other','10 other'),
 ('C30','After enfin and the canceled short sign, before K',r'\deleted{\unsure{et}} K',r'\struck{et} en fait K',r'\deleted{\unsure{et|\ell|\xi}} -\unsure{K|K\prime}','B13','A separate short horizontal rule lies in the blank immediately before K. The crossed sign and tiny upper-right traces remain doubtful; the definite dash was absent from both witnesses.','misread symbol or index','1 symbols/indices'),
 ('C31','(84), lower bracket beneath bar J cap tilde J',a84,'horizontal definition equality',z84,'B04','The lower stroke has turned-up ends and a continuous bottom without a central brace cusp. The vertical paired strokes, déf and B(J) remain below it.','drawing or diagram','4 diagrams/drawings'),
 ('C32','(86), lower bracket above B(K)',aK,aK,zK,'B08','The lower annotation is a shallow square-ended bracket: two short upturned end strokes and one bottom line, without a central cusp.','drawing or diagram','4 diagrams/drawings'),
 ('C33','(86), lower bracket above B(J)',aJ,aJ,zJ,'B08','The right-hand lower annotation has the same two upturned ends and straight bottom, without the central point of a brace.','drawing or diagram','4 diagrams/drawings')]:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind=kind,error_kind=ek,against_C=True,against_H=True,consequential=False,marked_in_H=False,phase='blind audit'))
r['doubts']=[x for x in r['doubts'] if x['place']!='Opening canceled word']
for d in r['doubts']:
 for a,z in reps:d['reading']=d['reading'].replace(a,z)
 if d['place']=="First lower I\\prime relation":d.update(reading=r"I'\unsure{=|\subset}\bar K",alternatives=['=',r'\subset'],reason='The two near-parallel strokes resemble the linked prose equals sign below, but their curved left junction still admits subset. No mathematical correction is made.')
 if d['place']=='First canceled lower et':d.update(reading=r'\deleted{\unsure{et|\ell|\xi}}',alternatives=['et',r'\ell',r'\xi'],reason='Several looped and horizontal strokes overlap. The former two-letter et and a single crossed looped sign are both possible.')
 if d['place']=='Second canceled lower et':d.update(reading=r'\deleted{\unsure{et|donc}}',alternatives=['et','donc'],reason='The initial loop and upright survive, followed by a long thick low run; that run may contain further letters, so donc is not excluded.')
r['doubts'] += [dict(place='Opening word after aussi',reading=r'\unsure{donc|alors}',alternatives=['donc','alors'],confidence='medium',reason='Tall opening stroke and compact ending favour donc; the pen joins do not securely exclude a plus l of alors.',crop=f'crops/{pg}_blind_B01.png',box=b['B01']['coordinates']),dict(place='Inserted hypothesis, word before J prec K',reading=r'\unsure{avec|on a}',alternatives=['avec','on a'],confidence='medium',reason='The tiny low groups are crossed by dense joins; the opening dot/loop and later short return do not securely separate a single avec from on a.',crop=f'crops/{pg}_blind_B11.png',box=b['B11']['coordinates']),dict(place='K after enfin and canceled short sign',reading=r'\unsure{K|K\prime}',alternatives=['K',r'K\prime'],confidence='medium',reason='Two minute upper-right traces are visible near K, but no continuous prime stroke is secure; preserve the uncertainty.',crop=f'crops/{pg}_blind_B13.png',box=b['B13']['coordinates'])]
r['inventory']=[x for x in r['inventory'] if x['element']!='Opening crossed word']
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
r['notes']+='\n### Blind reading corrections\n\nRotation of the full84 margin shows that the dense group after the main opening que belongs to the oblique tels que formula; the duplicated hypothetical canceled pour is removed. A comma follows aussi, the next word remains donc/alors, and the opening sentence ends de I with a comma. The lower annotation in84 and both lower annotations in86 have upturned ends without a brace cusp and are encoded accordingly. A separate short dash precedes K after enfin and the canceled short sign. The tiny possible prime there, the canceled words, and the lower relation =/subset remain uncertain. The visible prose equals sign and the descending g of égalité are retained without an invented underline.\n'
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=b[box]['first']
  for a,z in reps:f=f.replace(a,z)
  if box=='B01':f=f.replace('de $I$.','de $I$,')
  notes[box].update(changed=True,final=f)
put('B01','The full exact crop and rotated B04 show that the apparent canceled pour belongs to the slanted marginal tels que, not a separate main word. Remove its duplicate. A detached comma follows aussi; the next compact word is left donc/alors. The final mark after I has a downward comma tail. Both full conditions and the implication agree, and the marginal fragment appears once in84.',True)
put('B02','The full exact crop shows the short underline only beneath C. The live raised article is une; propriété continues on the main baseline with sym. and passage. The old crossed wording does not securely distinguish une propriété, une prop. or une top., so retain all locally. The live passage has its descending g and terminal e trace; it is not securely pass. The interlinear Toute intersection fragment is already in the following addition.',True)
put('B03','The crossed first mathematical glyph is dense and uncertain, but a separate intersection arch, tilde and following J remain visible. Retain the local first-glyph doubt rather than replace the whole expression by B(J). The following Soient fragment is overlap; the canceled bandes remains uncertain because its middle lies under the strike.')
put('B04','The complete exact crop was viewed upright and in its45-degree rotation. All of84 agrees, including tels que, both inequalities, the vertical pair and déf. The bracket below the left expression has upturned ends but no central cusp, so encode that shape. The large attachment brace belongs to the added prose. Main-text fragments in the second reading are overlap and are already transcribed.',True)
put('B05','The tight exact crop shows the lower crossed b-like stem and covered middle, with live parties raised above. Keep bandes locally uncertain; the upper canceled formula is overlap already transcribed in the preceding insertion.')
put('B06','Both ends of the doubled implication shaft are headed. The prec relation, left85, déf, the two inclusions, bar K and tilde J agree. The display wrapper and text-versus-math upright déf syntax are representational.')
put('B07','The exact crop confirms l\'ens without a stop and the calligraphic P(I). Braces around the mathcal argument do not change the glyph.')
put('B08','The full formula, both doubled headed implications, bar/tilde scopes and the two labels agree. Both lower strokes have upturned ends and straight bottoms without central cusps; encode square-ended brackets. The preceding la relation is only overlapping prose.',True)
put('B10','The crossed word starts in a short dotted upright and no independently secure tall l/apostrophe. Retain inclusion/l\'inclusion uncertainty; the raised replacement domination and final stop are clear.',True)
put('B11','The tiny initial low groups do not securely distinguish avec from on a. Restore local uncertainty while retaining J prec K, the comma and leader attachment after bandes. The maintenant and soit I fragments are adjacent-line overlap.',True)
put('B12','The number closes with a nearly straight downstroke and lower left return but has no decisive upper bracket arm, so keep )/]. The whole set-builder, t.q. stops, bar K, tilde J and both equals signs agree. The surrounding par J cup K and dans I-prime are overlap.')
put('B13','The crossed short form has overlapping looped and horizontal strokes, permitting et/ell/xi. A separate low horizontal rule is plainly present before K and is restored. Tiny upper-right marks do not form a secure continuous prime, so keep K/Kprime uncertainty. Enfin has a tall f and joined final in.',True)
put('B14','The left relation resembles the linked prose equals sign in B15, but its curved join also admits subset; retain the uncertainty with equals preferred. The next inclusion is open and clear. The canceled following run may contain et or donc; neither is certified. The final i.e. remains.',True)
put('B15','The two connected horizontal bars are the author\'s prose equals sign. The low stroke under égalité is the returning descender of g, not an underline. Both parentheses and the exclamation mark agree; i.e. at the edge overlaps the preceding line.')
put('B17','A detached low curved comma follows the connected ainsi. Its dot is above i, not a word gap for on a. Retain ainsi, with the full final equality, tilde J, bar K and final stop. The upper dans is previous-line overlap.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('090: all15 differing boxes viewed; eight changed boxes.')
