from pathlib import Path
import re

root = Path('/workspace/scratch/89f8415d3ab0')
path = root / 'deliver/MPL_81_038-055+154_046-076_notes.md'
s = path.read_text()

replacements = {
    'The subdivisions': 'The subdivisions',
    'a dual subdivision, and sign rules': 'a subdivision described by a doubt-marked “duales/doubles,” and sign rules',
    'The four-scheme subscript and the temporal-symmetry pair retain literal doubts':
        'The four-scheme subscript is doubtful, while the temporal-symmetry pair has a literal order mismatch',
    'The modernization summarizes them in a coherent construction, but that synthesis cannot remove the frozen doubts or supply the global verification.':
        'The modernization gives a more coherent presentation while retaining the double-cover question and its uncertain readings, so it supplies no missing global verification.',
    'uncertain inserted $\\mathbb D^+_{2n}\\simeq\\mathbb Z/(2n)$ in the even case':
        '$\\mathbb D^+_{2n}$, followed by the uncertain inserted identification $\\simeq\\mathbb Z/(2n)$, in the even case',
    'using the separate cancelled scan160 formula, rather than claiming merely to decipher an additional symbol on046.':
        'using the separate cancelled scan160 formula, whose skeleton superscript is itself doubtful ($X_1^a\\mid X_1^0$) and is normalized to $X_1$ in the modernization, rather than claiming merely to decipher an additional symbol on046.',
    'the cancelled051 count does not finish its concluding construction (051:54–57)':
        'the cancelled051 draft states a cardinality of $\\nu(s)$ and then leaves a further deleted “et il y a” clause unfinished (051:54–57)',
    'The recurrence on056:159–162 and the definition continuing beyond076 are incomplete written developments':
        'The recurrence on056:159–162, the cancelled “Si on fait” ending at061:6, and the definition continuing beyond076 are incomplete written developments',
    'Intrinsic description of the indicated characters remains a task.':
        'Values of the indicated characters and representations remain to be made explicit.',
    '119:41–76': '119:41–48,60–76',
    'N127 X01–X03,151/154':
        'N127 X01–X03,151:2–9,76–82;153:153–165;154:31–44;158 opening',
    'N127 X02/C03,154':
        'N127 X02,154:31–44 with158 opening, and C03,154:75–78',
    'N127 G04/G09,151, and N077 O06,088/093':
        'N127 G04,151:2,77 and160:5–12,68–74, and G09,151:4–9,76–82; N077 O06,088:24–29,091:31–36,092:2–12,093:70–76,119:30–32',
    'N127 P05/G11,155–156 and176':
        'N127 P05,155 heading with133/156/176 sequences, and G11,176:3–8',
}
for a, b in replacements.items():
    s = s.replace(a, b)

needle = '|047:44 | “Peut-être”'
if needle in s:
    s = s.replace(needle, '|046:54 | Deleted “suffit”; inserted doubt-marked “faut” | Sufficiency is withdrawn; on the preferred replacement reading the condition is necessary. |A05 |\n' + needle)
needle = '|060:23→061:4–6 |'
if needle in s:
    s = s.replace(needle, '|059:28–30 | “A vrai dire”; “Donc il vaut mieux” | The setting and starting position are qualified; the intervening “est conclusif / n’est conclusif” remains a reading doubt. |B09–B10 |\n' + needle)
needle = '|066:6 |'
if needle in s:
    s = s.replace(needle, '|066:4 | “Non, c’est vrai pour $a\'$” within deletion | The a-gluing assertion is corrected to a′ inside a cancelled paragraph. |D03/Q11 |\n' + needle)

# Improve prose spacing without changing code, mathematics, URLs or identifiers.
protected = re.compile(r'(`[^`]*`|\$\$[\s\S]*?\$\$|\$[^$\n]*\$|https?://\S+)')
prefixes = r'The|the|all|All|on|from|to|and|with|of|in|at|by|dated|scans|scan|page|pages|cote|cotes|order|section|sections|built|downloaded|written|June|November|January|August|rank|Vol\.|pp\.|p\.'
months = r'January|February|March|April|May|June|July|August|September|October|November|December'
parts = protected.split(s)
for i in range(0, len(parts), 2):
    t = parts[i]
    t = re.sub(r'\b(' + prefixes + r')(?=\d)', r'\1 ', t)
    t = re.sub(r'(\d)(' + months + r')\b', r'\1 \2', t)
    t = re.sub(r'(\d)(' + months + r')(?=\d)', r'\1 \2', t)
    t = re.sub(r'\b(' + months + r')(?=\d)', r'\1 ', t)
    t = re.sub(r'(\d)(UTC|PM|AM|AUG)(?=\b|\d)', r'\1 \2', t)
    t = re.sub(r'\b(AUG)(?=\d)', r'\1 ', t)
    t = re.sub(r',(?=\S)', ', ', t)
    t = re.sub(r'\bThere are(?=\d)', 'There are ', t)
    t = t.replace('There are22', 'There are 22')
    parts[i] = t
path.write_text(''.join(parts))
print(path.name)
print('bytes', path.stat().st_size)
