from audit import *
k='120_scan015'
replace_text(k,[
 (r'\node[draw,ellipse] {IV}',r'\node[draw,ellipse] {$\overline{\underline{\mathrm{IV}}}$}'),
 (r'(idem dans $\operatorname{Esp}_{\mathcal M_*}$',r'(idem dans $\underrightarrow{\operatorname{Esp}}_{\mathcal M_*}$')
])
add_changes(k,[R('section numeral decorations','circled IV','(IV)','circled IV with upper and lower bars','Inside the enclosing oval, separate heavy horizontal bars extend over and under both letters of IV.','drawing or diagram','yes','yes',crop='120_scan015 (559,26,690,111)')])
revise_change(k,'ordinary category in parenthesis',final='Esp with a lower right arrow and subscript M_*',scan_shows='A separate low shaft ends in a right-pointing tip beneath Esp. There is no upper arrow. A small branched terminal stroke follows the M.',diff_C='yes',crop='120_scan015 (971,1970,1117,2099)',confidence='medium',consequential='The parenthetical category also bears a lower right arrow; the decoration is retained even where the prose suggests a comparison with ordinary moderate spaces.')
p=ROOT/(PREFIX+'_notes.md');s=p.read_text();s=s.replace('the ordinary category in the parenthesis lacks the upper mark.','the category in the parenthesis lacks the upper mark but, as the second audit confirms, does have a lower right arrow.');p.write_text(s)
p=ROOT/(PREFIX+'_hand_log.md');s=p.read_text();s=s.replace('ordinary Esp in the parenthesis lacks the upper mark.','Esp in the parenthesis lacks the upper mark but has a lower right arrow (confirmed in the second audit).');p.write_text(s)
# Expand an already-present certainty record; no new reading or count.
rows=readtsv('CERTAINTY.tsv')
for r in rows:
 if r['page']=='120_scan011' and r['place']=='opening cancelled name':
  r['C']=r'\unsure{$\operatorname{Esp}$}';r['final']=r'$\operatorname{Esp}$'
rewrite_tsv('CERTAINTY.tsv',rows)
finish(k,'Reread the whole page and the existing rotated lower-margin crop. Its compressed continuation remains uncertain. Two newly examined decorations are restored: the bars over and under IV inside the oval, and the lower right arrow beneath the parenthetical Esp. Both main ind-category names retain their upper double arrow and lower arrow. The ordinary-space interpretation of the parenthetical phrase is not used to erase its visible lower arrow.',habits='The circled IV has bars over and under the numeral. The three Esp names in the main body of this leaf do not all have the same decoration: the first and last have upper double arrows and lower right arrows; the parenthetical occurrence has the lower right arrow only. Both witnesses missed that lower decoration.',notation=[('parenthetical Esp on 015','Lower right arrow only; no upper double arrow. This occurrence is retained even though the surrounding comparison may suggest ordinary Esp.')])
