"""Research-note typography and citation edits only; never touches frozen text."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / 'records/notes_data.py'
s = p.read_text()
s = s.replace('The Stacks Project, 2026, tags03PK and0A3J', 'The Stacks Project, 2026a, tag 0A3J; The Stacks Project, 2026e, tag 03PK')
s = s.replace('The Stacks Project, 2026, tag03R1', 'The Stacks Project, 2026b, tag 03R1')
s = s.replace('The Stacks Project, 2026, tag0A3J', 'The Stacks Project, 2026a, tag 0A3J')
s = s.replace('The Stacks Project (2026, tag0BQP)', 'The Stacks Project (2026d, tag 0BQP)')
s = s.replace('The Stacks Project (2026, Lemma21.10.1, tag03AV)', 'The Stacks Project (2026c, Lemma 21.10.1, tag 03AV)')
s = s.replace('p.60', 'p. 60').replace('proof4.7', 'proof 4.7')
s = s.replace('The assertion that H1 with', 'The assertion that H¹ with').replace('the H1 product decomposition', 'the H¹ product decomposition')
p.write_text(s)

p = ROOT / 'records/notes_standing.md'
s = p.read_text()
for a, b in [
    ('in2.6', 'in 2.6'), ('of3.5', 'of 3.5'), ('and3.7', 'and 3.7'),
    ('proof4.7', 'proof 4.7'), ('of5.2.3.1', 'of 5.2.3.1'), ('of5.15', 'of 5.15'),
    ('Proof6.4', 'Proof 6.4'), ('pp61', 'pp. 61'), ('car6.6', 'car 6.6'), ('en5.13', 'en 5.13'),
    ('of9.5.8', 'of 9.5.8'), ('in10.5.3', 'in 10.5.3'), ('for10.5.4', 'for 10.5.4'),
    ('on030', 'on 030'), ('formulas044', 'formulas 044'), ('fragment042', 'fragment 042'),
    ('equality on041', 'equality on 041'), ('clause on048', 'clause on 048'), ('indices on052', 'indices on 052'),
    ('of5.7', 'of 5.7'), ('on006', 'on 006'), ('on034', 'on 034'), ('on032', 'on 032'),
    ('entire042', 'entire 042'), ('on045', 'on 045'), ('block048', 'block 048'), ('on051', 'on 051'),
    ('SGA7', 'SGA 7'), ('Manuscript1', 'Manuscript 1'), ('pencil2', 'pencil 2'),
    ('pencil33', 'pencil 33'), ('pencil34', 'pencil 34'), ('pencil35', 'pencil 35'),
    ('pencil43', 'pencil 43'), ('pencil46', 'pencil 46'), ('pencil51', 'pencil 51'),
    ('Définition1', 'Définition 1'), ('Pages1', 'Pages 1'), ('sheets003', 'sheets 003'),
    ('numbers1', 'numbers 1'), ('are2', 'are 2'), ('on003', 'on 003'), ('and27', 'and 27'),
    ('on028', 'on 028'), ('count31', 'count 31'), ('n°316', 'n° 316'), ('leaves030', 'leaves 030'),
    ('classifies16', 'classifies 16'), ('text,12', 'text, 12'), ('of36/', 'of 36/'),
]:
    s = s.replace(a, b)
p.write_text(s)

p = ROOT / 'records/build_notes.py'
s = p.read_text()
s = s.replace("('title','body','context','reason')", "('title','body','context','reason','location')")
s = s.replace("n[key]=re.sub(r'(?<=[a-z])(?=\\d)', ' ', n[key])", "n[key]=polish(n[key])")
anchor = "records=[]\n"
helper = '''def polish(text):
 # Preserve math, identifiers and code while spacing prose and scan locators.
 chunks = re.split(r'(\\$[^$]*\\$|`[^`]*`)', text)
 for i in range(0, len(chunks), 2):
  t = chunks[i]
  t = re.sub(r'(?<=[a-z])(?=\\d)', ' ', t)
  t = re.sub(r'(?<=\\d),(?=N?\\d)', ', ', t)
  t = re.sub(r'(?<=N\\d{2}),(?=N)', ', ', t)
  t = t.replace('degrees−', 'degrees −').replace('line−', 'line −')
  t = t.replace('section2', 'section 2').replace('n°316', 'n° 316')
  t = t.replace('SGA7', 'SGA 7').replace('cf.2.3', 'cf. 2.3')
  chunks[i] = t
 return ''.join(chunks)

'''
if 'def polish(text):' not in s:
    s = s.replace(anchor, helper + anchor)
p.write_text(s)

p = ROOT / 'records/build_register.py'
s = p.read_text().replace('the standing inventories below/above', 'the preceding standing inventories')
p.write_text(s)
print('Research-note wording and formatting updated; frozen files not opened for writing.')
