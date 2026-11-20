from record import *
s=46
src=ROOT.parent/'source/SP60_CW_71_witnesses/codex/J71-06/pages/J71-06_71_scan046.tex'
t=src.read_text(encoding='utf-8').replace('% margin note written sideways\n','')
(ROOT/'pages'/src.name).write_text(t,encoding='utf-8')
change(s,'046-R01','inverted fragment, initial bracket','deleted ]? before [s,s′]∩','No source text','same','Scan 46 crop (1195,2193,1585,2268), rotated 180°: both left-pointing short strokes remain beside the stronger right-pointing feet of [. An underlying ] is possible, but extended serif-like strokes cannot be excluded. The final cap has no operand.','low',record_type='crop decision')
doubt(s,'inverted fragment, overwritten opening bracket','deleted ]','','low',reason='Short left projections survive beside the live [, but the earlier bracket is not certain.')
inv(s,[('drawing','middle-right, upper of two figures','seven-cornered outline, s′,s,s″, two dashed connections'),('drawing','below upper figure','four-cornered concave outline'),('drawing','lower blank area','isolated short vertical stroke'),('margin note','lower right, inverted 180 degrees','ment [s,s′]∩'),('deletion','inverted fragment, first bracket','underlying ]?')])
notation('Square brackets and cap in unfinished fragment','[s,s′]∩ with no right operand','46','Initial [ has possible overwritten ]; no continuation supplied.')
note(s,"""**Sheet:** no manuscript folio or heading; archival number 45. Two pencil polygon sketches occupy the lower right half, with a short isolated stroke below. The upper outline has seven corners, labels s′, s, s″ and two dashed connections; the lower has four corners and no labels. Boundary vertices, the attachments of both dashed paths, and the three labels were compared twice with the reproduction. The faint reverse-looking curve to the left of the upper drawing aligns with show-through from the opposite page, rather than a third foreground figure.

The ink fragment at the foot is inverted 180° and reads “ment [s,s′]∩”, with a possible older ] beneath the opening [. It ends without an operand. Its orientation and unfinished state are preserved in the metadata; it is not joined to scan 45’s proof or completed from context. H has no source transcription for this page.

No mathematical proposition or authorial question is written on this sheet, and no proof check is claimed for interpreting its drawings. The pencil hand’s identity cannot be established from the diagrams.""")
done(s)
