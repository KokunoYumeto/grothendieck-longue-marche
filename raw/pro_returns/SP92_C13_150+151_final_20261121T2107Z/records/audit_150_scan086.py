from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan086';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
olddec=r'\unsure{\bar T_j|T_j}';dec=r'\unsure{T_j^{\deleted{\circ}}|\dot T_j}'
oldmid=r"X_{J'}\setminus X_{J'}\cap\mathring T_{I'_0}";mid=r"X_{J'}\setminus X_{J'}\cap\unsure{\mathring T_{I'_0}|\dot T_{I'_0}}"
reps=[('Je ne suis pas très sûr',r'Je ne suis pas \unsure{très sûr|sûr}'),('vraiment essentielle','vrai-\\\nment essentielle'),(r'\mathrm{déf}',r'\mathrm{def}'),(olddec,dec),(oldmid,mid)]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
ch={x['id']:x for x in r['changes']}
ch['C01'].update(final=r'Je ne suis pas \unsure{très sûr|sûr}',confidence='medium',evidence='Je ne suis pas is readable. The small following group is partly crossed by the large initial downstroke from the preceding line; sûr is supported, but separating the proposed très from it is not secure. Retain a local très sûr/sûr doubt.',partial_resolution=True,change_type='partial doubt resolution',crop=f'crops/{pg}_blind_B02.png',box=b['B02']['coordinates'])
ch['C02']['final']=ch['C02']['final'].replace('vraiment','vrai-\\\nment')
ch['C13'].update(final=ch['C13']['final'].replace(r'\mathrm{déf}',r'\mathrm{def}').replace(olddec,dec),evidence=ch['C13']['evidence']+' Blind review: def has no detached accent. The final T decoration is a dense raised blot with a pointed upper edge, not a separate horizontal overbar; retain canceled circle/dot alternatives.',crop=f'crops/{pg}_blind_B10.png',box=b['B10']['coordinates'])
ch['C27']['final']=ch['C27']['final'].replace(oldmid,mid)
for ident,place,C,H,final,box,why in [
 ('C28','Upper marginal prose, written division of vraiment','vraiment','on (following fragment unreadable)','vrai-\\\nment','B02','A separate short horizontal hyphen follows vrai at the end of the slanted line; ment starts the next line before essentielle. Preserve the division.'),
 ('C29','Marginal T definition, unaccented def',r'\mathrm{déf}','(absent)',r'\mathrm{def}','B10','Above the e of the small definitional label is blank paper; the only tall following stroke is the f. Read def without supplying an accent.')]:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind='omission' if ident=='C28' else 'abbreviation expanded or spelling modernised',error_kind='3 omissions' if ident=='C28' else '8 abbreviation/spelling',against_C=True,against_H=(ident=='C28'),consequential=False,marked_in_H=ident=='C28',phase='blind audit'))
for d in r['decisions']:
 if d['id']=='M0694':d.update(decision='undecided',reading=r'Je ne suis pas \unsure{très sûr|sûr}',ink=ch['C01']['evidence'],crop=f'crops/{pg}_blind_B02.png',box=b['B02']['coordinates'],confidence='medium')
 if d['id']=='M0699':d.update(reading=dec,ink='The raised decoration is a dark blot, not a separate horizontal bar. It may be a canceled ring or a solid dot; the revision state is not secure.',crop=f'crops/{pg}_blind_B10.png',box=b['B10']['coordinates'])
for d in r['doubts']:
 if 'Decoration above' in d['place']:d.update(reading=dec,alternatives=['canceled circle','solid dot'],reason='The raised blot has no independent horizontal bar; a canceled circle and a dot cannot be separated under its dense retrace.')
r['doubts'].extend([
 dict(place='Opening margin, M0694 reduced final group',reading=r'\unsure{très sûr|sûr}',alternatives=['très sûr','sûr'],confidence='medium',reason=ch['C01']['evidence'],crop=f'crops/{pg}_blind_B02.png',box=b['B02']['coordinates']),
 dict(place='Lower diagram, decoration of the middle T',reading=r"\unsure{\mathring T_{I'_0}|\dot T_{I'_0}}",alternatives=['ring','dot'],confidence='medium',reason='The middle raised mark is almost filled, unlike the two open circles at either side. A minute pale centre may remain, but it does not securely decide ring versus dot.',crop=f'crops/{pg}_blind_B15.png',box=b['B15']['coordinates'])])
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
r['notes']+='\n### Blind reading corrections\n\nThe opening marginal phrase remains partly unresolved: Je ne suis pas is clear, but the reduced following group is now marked très sûr/sûr. The page visibly divides vrai- / ment. The marginal definitional label is unaccented def. The blotted decoration of the first T_j is now represented by canceled-circle/dot alternatives rather than an asserted overbar candidate. The middle T in the lower diagram also has a filled-looking raised mark and now carries a ring/dot doubt. All three diagrams retain the observed headless hooked strokes, upright relation pairs and the literal upper-right J-prime subscript. The blind alternatives did not justify replacing that written J with the expected I. No additional mathematical claim was checked by these readings.\n'
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=b[box]['first']
  for a,z in reps:f=f.replace(a,z)
  notes[box].update(changed=True,final=f)
put('B02','The exact region and rotated start/end display were read. Je ne suis pas is clear, but the small next group is partly crossed; retain très sûr/sûr. There is an actual hyphen after vrai, with ment on the following line. Ou celle is visible to the right of essentielle and is not omitted. The reduced phrase after J prec L remains uncertain; the blind on peut does not separate every letter. The final word has a p descender and a later g return, supporting passages rather than formules. Authorial39 and lower/main fragments are overlap already transcribed in their own places.',True)
put('B03','After the tall t is a small e loop before the dark terminal s return. Keep disjointes and its single independent underline. The comma at the edge is already present in the complete main line.')
put('B04','The d has its own closed oval and ascender, followed by a low a/n run and the curled final s. There is no separate round o and open c supporting donc; keep dans.')
put('B05','Two l loops follow the crossed t and low e; the long low ending finishes in a downward s return, matching the terminal return in disjointes. Keep telles.')
put('B06','The short group has a low initial loop and s join leading directly to the taller final t. No detached i dot or independent o loop supports soit/sont. Keep est.')
put('B07','After aura the next word begins with a low a and a separate tall l, followed by low o/r/s; it is alors, not donc. Both intersection expressions, primes, inclusion and final parenthesis agree.')
put('B08','The full region preserves the J-prime definition, inclusion chain and canceled X-expression. The short une has its terminal e before the following line’s inclusion. Alternate display/math wrappers do not alter the reading.')
put('B09','The exact crop and rotated view show où at the edge before the definitions; it is not omitted. Def has no accent. The canceled old expression remains uncertain as a whole; alleged extra overbar/index cannot be certified through its crossing strokes. The replacement expression is beside the canceled one on the same slanted level, after a visible semicolon, so no raised insertion attachment is imposed. The final T decoration is blotted, now canceled-circle/dot. Both first and second initial-element conditions include the short est before membership. The small a in Drap is reduced to a low join between r and p, not a demonstrably omitted letter. Limit heads, question marks, parenthetical equality and the second struck est remain as in the first reading.',True)
put('B10','The whole revised definition region was read and rotated. The label def has no accent; the final T decoration is a dense raised blot and cannot be a clean independent overbar. Keep canceled-circle/dot alternatives. The semicolon is distinct between the canceled and live formulas, whose live continuation is at the same slanted level. Rings in the next two definitions and all lower differences remain unchanged.',True)
put('B11','The middle short word after final is crossed by a heavy stroke through its low body and taller ending; it is not confidently live. Its residual identity est remains uncertain. The initial-element condition has a distinct est before membership. Drap’s middle low join is compatible with a, and the written first blank in the next line is a repetition dash. Both question and limit-arrow head are clear.')
put('B12','The top-right final subscript is a J with a lower left hook, matching the middle J and differing from the I immediately before its equality. Keep this literal J-prime. Vertical connectors end in one returning hook without a chevron; the horizontal connectors are also hooked and headless. Each lower relation consists of two uprights, with small bottom returns but no separate tilde. The lower starred row is distinct. Both cart labels are kept as written.')
put('B13','All bars, primes, zeros and objects agree. The vertical connectors have one curled lower end, not an arrowhead with two branches; the horizontal ones have a left hook and blunt right end. The drawn paths retain these forms and the two cart labels.')
put('B14','The three definitions and their primes, subscripts, bars, slashes, two commas and final stop agree. Inline versus display and bar versus overline are encoding differences only.')
put('B15','Both horizontal links have a left hook and no right arrowhead. Each lower relation is an upright pair; a separate question mark stands next to the last pair. The middle raised T mark is nearly filled, unlike its open neighbours, so add a local ring/dot doubt. All three complete expressions were reread with it.',True)
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('086: all14 differing boxes observed; four changed boxes.')
