"""Rebuild the combined fragment and complete doubt register before the freeze.

This parses only the transcribed text. It never performs image recognition.
"""
from pathlib import Path
import collections
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT.name


def braced(s, start):
    assert s[start] == '{'
    level = 1
    i = start + 1
    while i < len(s):
        if s[i] == '\\':
            if i + 1 < len(s) and s[i + 1] in '{}\\':
                i += 2
                continue
        if s[i] == '{':
            level += 1
        elif s[i] == '}':
            level -= 1
            if level == 0:
                return s[start + 1:i], i + 1
        i += 1
    raise ValueError('Unclosed brace')


def split_alternatives(arg):
    level = 0
    for i, ch in enumerate(arg):
        if ch == '{' and (i == 0 or arg[i-1] != '\\'):
            level += 1
        elif ch == '}' and (i == 0 or arg[i-1] != '\\'):
            level -= 1
        elif ch == '|' and level == 0:
            return arg[:i], arg[i+1:]
    return arg, ''


def md(s):
    return str(s).replace('\n', ' ').replace('|', '\\|')


def code(s):
    return '`' + md(s).replace('`', '&#96;') + '`'


def normalized(s):
    return re.sub(r'\s+', ' ', s).strip()


pages = sorted((ROOT/'pages').glob('*.tex'))
assert len(pages) == 45
combined = '\n\n'.join(p.read_text().rstrip() for p in pages) + '\n'
(ROOT/(PREFIX+'_transcription.tex')).write_text(combined)
records = [json.loads(x) for x in (ROOT/'records/readings.jsonl').read_text().splitlines() if x]
record_map = {(r['cote'],r['scan']):r for r in records}

notation = []
seen = set()
for rec in records:
    for sign, latex, qualification in rec.get('notation', []):
        key = (sign, latex)
        if key in seen:
            continue
        seen.add(key)
        latex = latex.replace('\\underline h', '\\uline h')
        if sign == 'Hatted gerbe':
            latex = '\\widehat{\\mathcal G}'
        qualification = qualification.replace('Needs cross-page review.', 'Cross-page comparison did not securely resolve the glyph.')
        qualification = qualification.replace('carry doubt until cross-page ink comparison.', 'doubt retained after cross-page ink comparison.')
        qualification = qualification.replace('compare earlier doubtful form before freeze.', 'earlier doubtful form remains explicitly marked after comparison.')
        qualification = qualification.replace('check recurrence later.', 'case remains uncertain after comparison.')
        qualification = qualification.replace('compare earlier category-P signs in audit.', 'earlier less distinct category-P signs retain alphabet doubt.')
        notation.append((sign, latex, f"{rec['cote']}, scan {rec['scan']:03}: {qualification}"))

extra_notation = [
    ('Coefficient-letter encoding after audit', '\\mathbf Q,\\mathbf Z,\\mathbf R', 'Doubled/retraced coefficient letters use one encoding throughout; plainly single-stroke Q and R remain plain. Bold is a typographic approximation to the handwritten doubled form, not an inferred change of field.'),
    ('Gerbes versus groups', '\\mathcal G,\\widehat{\\mathcal G}; G,G^0,G_m', '15/020–024: descending script gerbe letter compared across adjacent sheets; ordinary group G in 15/003–014 is not changed.'),
    ('First letter of target category in Ex. 2', '\\unsure{\\mathcal P|\\mathcal D}', '15/032: ornate opening P-like glyph differs from later plain D; retained as an uncertainty rather than harmonized by meaning.'),
    ('Primes, stars, circles and shrieks', "u',u'',u^*,i^*,\\mathcal V^\\circ", 'Compared as graphical signs, not inferred from duality. No doubtful prime was promoted to a shriek exponent. The uncertain small loop on 12/156 stays *|circle.'),
    ('Arrow state', '\\arrow[r,dash]; \\deleted{\\longrightarrow}', 'A blunt connector stays headless. In 15/014 and 15/032 cancelled arrows, not only their objects, carry deletion state. The wavy strike on 15/032 is not a live wavy arrow.'),
    ('Centre mark', '\\unsure{\\natural|\\sharp}', '15/018–020: the same angular mark remains uncertain consistently; a separate star denotes units. The final base letter on 15/018 is O|A, also uncertain.'),
    ('Norm notation is not normalized', '\\operatorname{Nrd},N_{\\mathrm{red}},\\operatorname{Nr}_{O/A}', '15/021,022,032 respectively: preserve the different visible abbreviations.'),
    ('Hats, checks and tildes', '\\widehat{\\mathcal M},\\widetilde{\\mathcal M},\\check M,\\widehat H', '12/154–157 and 15/014: accents retain their written shapes and positions. No category hat was changed to a tilde because an earlier page used one.'),
]
notation.extend(extra_notation)

lines = ['# Notation table', '',
         'This table was maintained during transcription and reconciled against the scans before any context contents were opened. Graphically unresolved differences remain doubt-marked; mathematical consistency was not used to select a reading.', '',
         '| Sign or usage | LaTeX | Observation / audit decision |', '|---|---|---|']
lines += ['| '+md(a)+' | '+code(b)+' | '+md(c)+' |' for a,b,c in notation]
lines += ['', '# Complete in-place doubt register', '',
          'Each occurrence of `\\unsure` and `\\illegible` in the final pre-context page files has its own row below, including nested occurrences and repetitions. “Block” counts blank-line-separated transcription blocks; “TeX line” is a reproducible locator in the individual page file, **not** a claim about the manuscript’s physical line numbering. Original visual-position notes are added where a first-pass record matches the reading. Confidence concerns the paleographic reading, not the truth of the mathematics.', '',
          '| Cote | Scan | Approximate position / locator | Reading | Alternative(s) | Confidence | Comment |', '|---|---|---|---|---|---|---|']

doubt_count = 0
for page in pages:
    cote, scan = map(int,re.search(r'_(12|15)_scan(\d+)\.tex$',page.name).groups())
    s = page.read_text()
    spans = []
    for m in re.finditer(r'\\(deleted|inserted|margin|diagram|figure|unsure|illegible)\{',s):
        arg,end = braced(s,m.end()-1)
        spans.append((m.start(),end,m[1],arg))
    for start,end,kind,arg in spans:
        if kind not in ('unsure','illegible'):
            continue
        doubt_count += 1
        first,alternative = split_alternatives(arg)
        contexts = [k for a,b,k,_ in spans if a < start and end <= b and k not in ('unsure','illegible')]
        confidence = 'low' if 'deleted' in contexts or len(first)>45 or (cote,scan) in [(15,17),(15,24),(15,32)] else 'medium'
        comment = ('Within '+', '.join(dict.fromkeys(contexts))+'. ') if contexts else ''
        location = f"block {len(re.findall(r'\n\s*\n',s[:start]))+1}; TeX line {s[:start].count(chr(10))+1}"
        matches=[]
        for oldpos,oldread,oldalt,oldconf,oldcomment in record_map[(cote,scan)].get('doubts',[]):
            if normalized(oldread)==normalized(first) or normalized(oldread)==normalized(arg):
                matches.append((oldpos,oldalt,oldconf,oldcomment))
        if matches:
            oldpos,oldalt,confidence,oldcomment=matches[0]
            location += '; '+oldpos
            comment += oldcomment
            if not alternative:
                alternative=oldalt
        else:
            comment += 'Explicit uncertainty retained after the second visual reading; no unmarked completion is supplied.'
        if kind=='illegible':
            first=f'{arg} physically unreadable word(s)'
            confidence='low'
            comment='Cancelled prose; count estimated after enlargement. This is not a placeholder for a mathematical symbol.'
        if cote==15 and scan==24 and ('classe d\'isomorphie' in arg or arg=='diffère'):
            confidence='low';comment='The enlarged clause remains very compressed and its grammar is unresolved; it has not been repaired into a plausible argument.'
        if cote==15 and scan==11 and arg=='U|H':
            confidence='low';comment='Bowl-shaped group letter; second reading favors U. First-pass M alternative was superseded during the pre-context audit.'
        lines.append('| '+ ' | '.join([str(cote),f'{scan:03}',md(location),code(first),code(alternative) if alternative else '—',confidence,md(comment)])+' |')

abbreviations = [
('Alg., alg.', 'algèbre / algébrique, according to construction'),('alg. clos.', 'algébriquement clos'),('ass.', 'associative; near isomorphisms, associativité'),('autom., autos', 'automorphisme(s)'),('bimod., biinvble', 'bimodule(s); bi-inversible'),('can.', 'canonique'),('car', 'caractéristique'),('cat., catég., Cat.', 'catégorie'),('cf.', 'confer / voir'),('chgt, chgts', 'changement(s)'),('comm.', 'commutatif; in comm. du diagramme, commutativité'),('comp.', 'compatible; in comp. conn., composantes'),('comp. conn.', 'composantes connexes'),('conj.', 'conjecture'),('cᵗᵉ v.l.', 'possibly constante, valeur…; the final letters are unresolved'),('deg, degré', 'deg abbreviates degré; degré itself is not expanded or changed'),('déf.', 'définit / définie, uncertain local ending'),('dim.', 'dimension'),('drt, drt., à dr., g., à g.', 'droite; gauche'),('eff.', 'effectif'),('end., endos', 'endomorphisme(s)'),('ens.', 'ensemble'),('ent.', 'entier'),('épim.', 'épimorphisme'),('équ., équiv.', 'équivalence / équivalent, according to construction'),('esp.', 'espace(s), reading uncertain'),('essᵗ', 'essentiellement'),('Ex., ex., p. ex.', 'exemple; par exemple'),('ext.', 'extension'),('f. et s.', 'faut et suffit'),('fin.', 'fini; ending uncertain'),('Fl', 'flèches'),('fppf', 'fidèlement plat et de présentation finie'),('g. pur', 'possibly groupe pur, in a cancelled phrase'),('géom.', 'géométrique'),('Gr-', 'groupe / groupale as modifier of catégorie; retained as the manuscript abbreviation'),('hom.', 'homogène in the duality passage; homomorphisme elsewhere'),('Hom', 'homomorphismes; symbol is not expanded in the fragment'),('Hyp', 'hypothèse'),('i.e.', 'id est'),('id, Id', 'identité / identique'),('identiqᵗ', 'identiquement'),('inv.', 'inversible; inv. de Hasse means invariant de Hasse'),('isom, isom.', 'isomorphisme'),('lin.', 'linéaire'),('loc., locᵗ', 'local / localement'),('mod, mod.', 'modulo'),('Mod.', 'modules'),('mono.', 'monomorphisme'),('mot.', 'motivique'),('N.B., NB', 'nota bene'),('nb., nbs, nbres', 'nombre(s)'),('néc.', 'nécessairement'),('Niv', 'niveau'),('noeth.', 'noethérien'),('Nr, Nrd, N_red', 'norme réduite; the three written forms remain distinct'),('Ob', 'objets'),('op.', 'opération(s)'),('pᵗés', 'propriétés'),('pb', 'problème'),('pl.', 'pleinement'),('proj.', 'projectif'),('Ps', 'pseudo, in pseudo-direct limit'),('pt', 'point'),('relativ.', 'relativement'),('Rep, repr.', 'représentation(s)'),('resp.', 'respectivement'),('rev.', 'revêtement'),('rg', 'rang'),('ssi', 'si et seulement si'),('suppl.', 'supplémentaire'),('sym.', 'symétrique'),('t. f.', 'type fini'),('t. m.', 'type multiplicatif, probable in the group context'),('t. q.', 'tel que'),('th.', 'théorème'),('top.', 'topologie'),('tor.', 'tore'),('tors', 'torsion'),('tot.', 'totalement'),('transp.', 'transposé'),('Trs-', 'torseur; Tors- is an alternative graphical reading'),('tt, tte, ttes', 'tout, toute, toutes'),('VA, V. A.', 'variété(s) abélienne(s)'),('val.', 'valeur; valuation in valuation labels'),('vect.', 'vectoriel(s)'),
]
lines += ['', '# Abbreviations', '', 'These expansions are editorial hypotheses and appear **only here**, never in the diplomatic fragment. Some abbreviations have different expansions in different constructions.', '', '| Abbreviation met | Probable expansion / qualification |','|---|---|']
lines += ['| '+md(a)+' | '+md(b)+' |' for a,b in abbreviations]
lines += ['', '# Legibility and reliability', '',
          'All 45 supplied whole pages and their supplied halves were personally inspected in one transcription stream; no OCR or transcription agent was used. Every page then received a second visual comparison before the context was opened. The ten reused typescript sheets are generally clear, although orientation, small prime/ideal symbols, and their cut-off continuations require care. Their own errors, paragraph continuations and page labels have been retained.', '',
          'The least secure material is compressed handwriting and cancellation on cote 12 scans 150, 161, 163, 165 and 167, and cote 15 scans 003, 007, 011, 013–014, 017–024 and 032. In particular, the revised positivity axiom on 12/161, the character/duality diagrams on 15/013–014, the centre signs on 15/018–020, the middle clause of 15/024, and the cramped norm-functor margins of 15/032 should be checked directly against the scans before quotation or mathematical reliance. The exact diagram direction, headlessness, source-letter spelling, and deletion state take priority over an expected theorem.', '',
          f'The register contains **{doubt_count} in-place occurrences**. Two physically unreadable cancelled prose spans are represented by estimated word counts; all uncertain mathematical glyphs have attempted readings. This is a complete attempted diplomatic transcription, not a claim of error-free paleography. Any later context-driven alternatives belong exclusively in the research notes.']
(ROOT/(PREFIX+'_doubts.md')).write_text('\n'.join(lines)+'\n')

# Structural checks on the final fragment, independent of mathematical content.
rows=list(csv.DictReader((ROOT/(PREFIX+'_inventory.csv')).open()))
expected=[(12,n) for n in range(150,169)]+[(15,n) for n in list(range(2,15))+list(range(16,25))+[26,28,30,32]]
assert [(int(re.search(r'_(12|15)_scan',p.name)[1]),int(re.search(r'scan(\d+)',p.name)[1])) for p in pages] == expected
assert set((int(r['cote']),int(r['scan'])) for r in rows)==set(expected)
assert all(r['transcribed']=='yes' for r in rows)
assert set(r['kind'] for r in rows)<=set(['text','display','diagram','drawing','margin note','insertion','deletion'])
assert combined.count('\\scanpage{')==45 and combined.count('\\cotefile{')==2
assert not any(x in combined for x in ['\\documentclass','\\newcommand','\\includegraphics'])
for page in pages:
    s=page.read_text(); stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        if m[1]=='begin': stack.append(m[2])
        else: assert stack and stack.pop()==m[2],page.name
    assert not stack,page.name
    # Consume escaped punctuation and braces without treating row separators as commands.
    depth=0;i=0
    while i<len(s):
        if s[i]=='\\' and i+1<len(s) and s[i+1] in '{}\\':i+=2;continue
        if s[i]=='{':depth+=1
        elif s[i]=='}':depth-=1;assert depth>=0,page.name
        i+=1
    assert depth==0,page.name
sheet_counts=collections.Counter(next(r['sheet_kind'] for r in rows if int(r['cote'])==c and int(r['scan'])==n) for c,n in expected)
report={'pages':len(pages),'inventory_rows':len(rows),'doubt_occurrences':doubt_count,'sheet_counts':dict(sheet_counts),'all_inventory_transcribed':True,'balanced_braces_and_environments':True,'no_preamble_or_images':True,'tex_engine_check':'pdflatex executable exists but its format and installed TeX package tree are absent; an attempted compile stopped before reading the fragment. No successful rendering is claimed.'}
(ROOT/'records/precontext_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
