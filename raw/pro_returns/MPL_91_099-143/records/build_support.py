"""Assemble the fragment and index its explicit doubt marks; never read scans/context."""
from pathlib import Path
import re, json

ROOT = Path(__file__).resolve().parents[1]
BASE = 'MPL_91_099-143'

def macros(text, name):
    for m in re.finditer(r'\\' + name + r'\{', text):
        i = m.end(); start = i; depth = 1
        while i < len(text) and depth:
            if text[i] == '{' and (i == 0 or text[i-1] != '\\'): depth += 1
            elif text[i] == '}' and (i == 0 or text[i-1] != '\\'): depth -= 1
            i += 1
        if depth: raise ValueError((name, m.start(), 'unbalanced argument'))
        yield m.start(), i, text[start:i-1]

def cell(s):
    return s.replace('\n', ' ').replace('|', '\\|')

def run():
    if (ROOT/'records/transcription.sha256').exists():
        raise RuntimeError('Transcription is frozen. Do not rebuild or edit the transcription after opening context.')
    anchors=json.loads((ROOT/'records/line_anchors.json').read_text())
    pages = sorted((ROOT/'pages').glob('*.tex'))
    combined = '\n\n'.join(p.read_text().strip() for p in pages) + '\n'
    if not combined.startswith('\\cotefile{91}'):
        combined = '\\cotefile{91}\n' + combined
    (ROOT/f'{BASE}_transcription.tex').write_text(combined)
    out = ['# Notation and doubts', '', '## Recurring notation', '',
           '| Scan anchors | Ink / sign | LaTeX treatment | Visual caution |',
           '|---|---|---|---|']
    for line in (ROOT/'records/notation.md').read_text().splitlines():
        if not line.startswith('|') or line.startswith('|---') or line.startswith('| Ink') or line.startswith('| Scan anchors'): continue
        parts = line.strip().strip('|').strip().split(' | ')
        if len(parts) == 3: parts = ['See anchor', *parts]
        if len(parts) != 4: raise ValueError(('notation columns', line))
        out.append('| ' + ' | '.join(cell(p) for p in parts) + ' |')
    out += ['', '## Doubt register', '',
            'Every explicit `\\unsure` and `\\illegible` occurrence in the page fragments is indexed below. Manuscript line bands are approximate visual locations, counted in reading orientation; diagrams and marginalia use their position instead. The separate TeX-line column gives an exact reproducible location in the individual page fragment. Handwritten line breaks inside paragraphs have not been forced into the transcription.', '',
            'Confidence concerns the first reading only. Medium means that the visible form supports that reading but leaves an unresolved stroke, ending, alphabet, or punctuation; low marks an obscured cancellation, longer conjectural reading, or a passage with no recoverable word. Alternatives are visual possibilities, not mathematical corrections. A blank alternative means that no second reading is offered.', '',
            '| File | Scan | Approximate manuscript location | TeX line | Reading | Alternative(s) | Confidence |',
            '|---|---:|---|---:|---|---|---|']
    rows=[]
    for p in pages:
        text=p.read_text(); scan=int(re.search(r'scan(\d+)',p.name)[1])
        deletions=list(macros(text,'deleted'))
        items=[('unsure',*m) for m in macros(text,'unsure')]+[('illegible',*m) for m in macros(text,'illegible')]
        for kind,a,b,arg in sorted(items,key=lambda x:x[1]):
            line=text.count('\n',0,a)+1
            location=next(v for k,v in reversed(anchors[str(scan)]) if k<=line)
            if kind=='illegible': reading=f'Physically unreadable: approximately {arg} word(s)'; alternatives=''; conf='low'
            else:
                parts=arg.split('|'); reading=parts[0]; alternatives=' / '.join(parts[1:])
                conf='low' if any(da<=a<db for da,db,_ in deletions) or len(re.findall(r'\b\w+\b',reading))>5 else 'medium'
                if (scan==114 and 'épimorphismes' in arg) or (scan==126 and 'Sous quelles' in arg) or (scan==131 and ('1\\textsuperscript' in arg or 'existe, et' in arg)) or (scan==138 and ('A\\mathfrak' in arg or '\\notin' in arg)):
                    conf='low'
            row={'file':p.name,'scan':scan,'line':line,'location':location,'reading':reading,'alternatives':alternatives,'confidence':conf,'macro':kind}
            rows.append(row)
            out.append(f'| {p.name} | {scan} | {cell(location)} | {line} | `{cell(reading)}` | `{cell(alternatives)}` | {conf} |')
    (ROOT/'records/doubts.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
    out += ['', '## Abbreviations: proposed expansions only', '',
            'These expansions aid reading; none is substituted into the transcription. Dots, accents, and variant spellings remain as seen in each page fragment.', '',
            '| Abbreviation | Proposed expansion |', '|---|---|']
    abbr=[('alg., algéb.','algébrique(s)'),('cat.','catégorie'),('cf.','confer / compare'),('Cl.','clair'),('const., cons','constructible(s)'),('cpt, cpts','compact(s)'),('C.Q.','ce qu’il fallait [démontrer]'),('dém.','démonstration'),('ens','ensemble(s)'),('épim','épimorphisme'),('fin.','finie'),('f. et s.','faut et suffit'),('gd','grand'),('gén., gén.t','général / généralement, or générique / génériquement according to the local phrase'),('géom.','géométriquement'),('hyp.','hypothèse(s)'),('i.e.','id est'),('irred.','irréductible'),('loc.','localement / local'),('mon','monomorphisme'),('N.B.','nota bene'),('noeths','noethériens'),('p.ex.','par exemple'),('pl. fid.','pleinement fidèle'),('présch.','préschéma(s)'),('proj.','projectif / projective'),('prop.','proposition'),('pt','point'),('q. cpt, q. cpts','quasi-compact(s)'),('q. séparé','quasi-séparé'),('resp.','respectivement'),('tjs','toujours'),('top.','topologie / topologique'),('trivialt','trivialement'),('tt','tout')]
    abbr += [('Alg.','Algèbre (printed reference title)'),('appl., applic.','application'),('chgt','changement'),('constr., construct.','constructible'),('cor., Cor.','corollaire'),('éd.','édition'),('élém.','élémentaire'),('En eff.','En effet'),('Esp.','espaces'),('exerc.','exercice'),('ext.','extension'),('fid.','fidèle; fidèlement according to the local phrase'),('fond.','fondamental'),('fort.','fortement'),('hom., homo','homomorphisme'),('imm., immers','immersion'),('M.L.','Mittag-Leffler (proposed expansion)'),('monom','monomorphisme'),('morph.','morphisme'),('nᵇʳᵉ','nombre'),('ouv.','ouvert'),('partic.','particulier'),('Pb','problème'),('Pr.','proposition (uncertain abbreviated heading)'),('prés.','présentation'),('q., qu., qua','quasi'),('qlc, quelc.','quelconque(s)'),('rec.','recollement(s)'),('rétrocomp.','rétrocompact'),('schém.','schématique(s)'),('sép., quasép','séparé / quasi-séparé'),('ssi','si et seulement si'),('syst.','système'),('t.q.','tel que'),('Th, th.','théorème'),('topol.','topologie / topologique'),('tot.','totalement'),('vois.','voisinages'),('équiv.','équivalence'),('nᵒ, Nᵒ','numéro')]
    abbr=[('alg.' if a=='alg., algéb.' else a,b) for a,b in abbr if a not in {'cat.','fin.','présch.'}]
    out += ['| '+a+' | '+b+' |' for a,b in abbr]
    out += ['', '## Legibility and limits', '',
            'The reused typescripts are generally more legible than the pencil and hurried handwritten pages. The most fragile readings lie in the layered deletions on scans 105–106 and 116, the faint proof on scan 122, the dense implication sketch and lower-right calculation on scan 128, the inserted qualifications on scans 131–132, and the overwritten determinant condition on scan 138. The recurring term provisionally read antifique/antifinie is retained as a doubt; no mathematical synonym has been substituted.', '',
            'All scans were read visually, with the supplied halves and enlarged crops as needed. No OCR was used. Doubt marks preserve attempts at reading; they do not certify every unmarked word. The audit record identifies later corrections made from the images. The research context remains sealed until every page has been audited and the transcription hashes have been frozen.', '']
    (ROOT/f'{BASE}_doubts.md').write_text('\n'.join(out))
    print(f'{len(pages)} pages; {len(rows)} doubt occurrences indexed')

if __name__=='__main__': run()
