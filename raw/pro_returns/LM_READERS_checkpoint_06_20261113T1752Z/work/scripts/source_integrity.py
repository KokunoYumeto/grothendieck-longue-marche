#!/usr/bin/env python3
"""Read-only audit of the attached source package, translation units and records.

No original script is imported: common_lm.py has machine-specific import paths,
and its external comparison libraries are not included. The visible algorithms
for assembly, marks, m-bar and raised endings are reproduced below; formula
segmentation and text-box masking are independent and deliberately reported as
an independent check, separately from the supplied historical CHECKS.json.
"""
from __future__ import annotations

import collections
import csv
import difflib
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'sources'
OUT = ROOT / 'work'
APPARATUS = ('deleted', 'inserted', 'unsure', 'illegible', 'margin', 'uline', 'uuline')
OTHER_MARKS = ('texttt', 'textit', 'textbf', 'diagram', 'figure', 'textsuperscript', 'textcircled', 'fbox')
MATH_ENVS = ('tikzcd', 'tikzpicture', 'equation', 'equation*', 'align', 'align*',
             'aligned', 'gather', 'gather*', 'gathered', 'multline', 'multline*',
             'array', 'CD', 'eqnarray', 'eqnarray*', 'matrix', 'pmatrix', 'smallmatrix',
             'cases', 'split')
START = re.compile(r'\\\[|\\\(|\$\$|\$|\\begin\{(' +
                   '|'.join(re.escape(e) for e in MATH_ENVS) + r')\}')
TEXTBOX = re.compile(r'\\(text|mbox|hbox|textrm|textnormal|textup|textit|textsf|textbf|textsc)(?![A-Za-z])\s*\{')
MARKWORD = re.compile(r'\\(deleted|inserted|unsure|uline|uuline)\{([A-Za-zÀ-ÖØ-öø-ÿœŒ.\'’ -]{2,})\}')
RAISED = re.compile(r'^(?:\$|\\\()\s*(?:\{\})?\^\{?\s*(?:\\mathrm\s*\{?|\\text\{|\\textrm\{)?\s*[A-Za-z]{1,4}\s*\}?\s*\}?\s*(?:\$|\\\))$')
_M = r'\\(?:overline|bar)\{\\mathrm\{?\s*m\}?\}(?:\^\{\\mathrm\{?\s*s\}?\}|\^\{s\}|\^s|\\mathrm\{s\})?'
_SIGN = r'(?:=|\\simeq)'
MBAR = re.compile(r'^(?:\$|\\\()\s*(?:%s|\\unsure\{\s*%s\s*\}|\\unsure\{\s*%s\s*\|\s*%s\s*\}|\\unsure\{\s*%s\s*\|\s*%s\s*\})\s*(?:\$|\\\))$' % (_M, _M, _M, _SIGN, _SIGN, _M))

FORMULA_EXCEPTIONS = [
    {'unit': 'LM_P012_s111-120', 'scan': 116, 'class': 'translated connective inside a marked mathematical fragment',
     'french_fragment': r'$\nu\unsure{\le|=}0\deleted{\unsure{ou 1}}$',
     'english_fragment': r'$\nu\unsure{\le|=}0\deleted{\unsure{\text{or }1}}$',
     'assessment': 'The connective ou becomes or in a text box. The variable, inequality/equality alternatives, zero and one remain; the deletion and nested uncertainty remain. TeX tokens change; no algebraic symbol or relation is corrected.'},
    {'unit': 'LM_P018_s171-180', 'scan': 179, 'class': 'translated connective inside a mathematical formula',
     'french_fragment': r'$U\simeq\unsure{\mathbb C^*} \unsure{ou} S^1\times S^1$',
     'english_fragment': r'$U\simeq\unsure{\mathbb C^*} \unsure{\text{or}} S^1\times S^1$',
     'assessment': 'The uncertain connective ou becomes an uncertain text-box or. All variables, superscripts, products and the displayed alternatives remain. Both the historical fix and waiver incorrectly say scan 172; the literal occurrence is at scan 179.'},
    {'unit': 'LM_P042_s416-420', 'scan': 420, 'class': 'prose shorthand expanded; equality sign changed from math mode to text mode',
     'french_fragment': r'\unsure{$\overline{\mathrm m}$|$=$}',
     'english_fragment': r'\unsure{even|=}',
     'assessment': 'The two uncertainty alternatives remain. The m-bar shorthand is rendered even; the equality alternative retains the literal equals sign but loses its dollar delimiters. The historical checker calls $=$ missing because it counts math segments, not visible signs. No equals sign is dropped.'},
    {'unit': 'LM_P044_s431-440', 'scan': 440, 'class': 'two written forms of prose shorthand expanded',
     'french_fragment': r'\unsure{$\mathrm m^{\mathrm s}$|$\overline{\mathrm m}^{\mathrm s}$}',
     'english_fragment': r'\unsure{same|same}',
     'assessment': 'Both source readings are the recorded abbreviation for mêmes. The English deliberately has two same alternatives under the uncertainty mark; it retains their count but not the French graphical distinction between barred and unbarred m. The French source preserves that distinction. This is a documented lexical convention, not deletion of a mathematical parameter.'},
    {'unit': 'LM_P056_s551-560', 'scan': 557, 'class': 'prose shorthand expanded inside a TikZ diagram label',
     'french_fragment': r'\overline{\mathrm m}\ \text{grain de sel}',
     'english_fragment': r'\text{same grain of salt}',
     'assessment': 'The mathematical-looking m-bar is the word même in the diagram annotation. Its command is absorbed into the English text box. Diagram objects, arrows, indices and n-conditions remain.'},
    {'unit': 'LM_C3-321-339_s328-332', 'scan': 332, 'class': 'translated text boxes reordered around the same underlined adjective',
     'french_fragment': r'\text{unipotent }\uline{\text{régulier}}',
     'english_fragment': r'\uline{\text{regular}}\text{ unipotent}',
     'assessment': 'Display (41) has this adjective/noun order change twice. Underlining remains on régulier/regular. The algebraic expressions for the two epsilon elements are unchanged; the change is the order and wording of adjacent prose boxes.'},
    {'unit': 'LM_C3-454-472_s454-458', 'scan': 457, 'class': 'prose shorthand expanded inside a display and uncertainty alternative',
     'french_fragment': r'\unsure{\text{de}=|\text{de }\overline{\mathrm m}}',
     'english_fragment': r'\unsure{\text{of}=|\text{likewise}}',
     'assessment': 'The first reading retains its equals sign; de même in the second becomes likewise. The uncertainty alternatives, equations and all algebraic notation around them remain.'},
    {'unit': 'LM_C3-492-510_s497-501', 'scan': 497, 'class': 'prose shorthand expanded beside an equation',
     'french_fragment': r'\text{et de }\overline{\mathrm m}',
     'english_fragment': r'\text{and likewise}',
     'assessment': 'The note et de même becomes and likewise. The phi, delta, alpha, beta expressions and both defining equalities are unchanged.'},
    {'unit': 'LM_C3-644-662_s655-658', 'scan': 655, 'class': 'uppercase prose shorthand expanded outside an equation',
     'french_fragment': r'$\overline{\mathrm M}$ conclusion',
     'english_fragment': 'Same conclusion',
     'assessment': 'The capital M-bar is the recorded même shorthand at the beginning of a sentence. It becomes the capitalized English word Same. It is not a parameter removed from the preceding formula.'},
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(p):
    return p.read_text(encoding='utf-8')


def uncomment(s):
    # Same comment rule as the supplied checker; preserve offsets and line count.
    return re.sub(r'(?<!\\)%[^\n]*', lambda m: ' ' * len(m[0]), s)


def group_end(s, start):
    assert s[start] == '{'
    depth = 1
    i = start + 1
    while i < len(s):
        if s[i] == '\\':
            i += 2
            continue
        depth += (s[i] == '{') - (s[i] == '}')
        if depth == 0:
            return i + 1
        i += 1
    return None


def escaped(s, position):
    i = position - 1
    while i >= 0 and s[i] == '\\':
        i -= 1
    return (position-1-i) % 2 == 1


def scans(s):
    matches = list(re.finditer(r'\\scanpage\{([^}]+)\}', uncomment(s)))
    return [(m[1], m.start(), s[m.start():matches[i+1].start() if i+1 < len(matches) else len(s)])
            for i, m in enumerate(matches)]


def anchor_sequence(s):
    return re.findall(r'\\(scanpage|mspage)\{([^}]+)\}', uncomment(s))


def args(s, name):
    s = uncomment(s)
    out = []
    for m in re.finditer(r'\\' + name + r'(?![A-Za-z])\s*\{', s):
        end = group_end(s, m.end()-1)
        out.append(s[m.end():end-1] if end else '<UNBALANCED>')
    return out


def mark_counts(s):
    s = uncomment(s)
    out = {name: len(re.findall(r'\\' + name + r'(?![A-Za-z])', s))
           for name in APPARATUS + OTHER_MARKS}
    out['unsure-bars'] = sum(x.count('|') for x in args(s, 'unsure'))
    return out


def math_segments(s):
    """Non-overlapping outer formulas, with offsets, including drawing environments.

    Dollar closers are found at the formula's initial brace depth, so a $...$
    nested inside a text box cannot terminate its enclosing formula. Environment
    closers are paired by the same name. An incomplete segment is retained and
    reported, never silently omitted.
    """
    s = uncomment(s)
    out = []
    pos = 0
    while m := START.search(s, pos):
        if escaped(s, m.start()):
            pos = m.end()
            continue
        token = m[0]
        complete = True
        if m[1]:
            env = m[1]
            rx = re.compile(r'\\(begin|end)\{' + re.escape(env) + r'\}')
            depth = 1
            end = len(s)
            for e in rx.finditer(s, m.end()):
                depth += 1 if e[1] == 'begin' else -1
                if not depth:
                    end = e.end()
                    break
            else:
                complete = False
        else:
            close = {'\\[': '\\]', '\\(': '\\)'}.get(token, token)
            depth = 0
            p = m.end()
            end = len(s)
            while p < len(s):
                if s.startswith(close, p) and depth == 0:
                    end = p + len(close)
                    break
                if s[p] == '\\':
                    p += 2
                    continue
                depth += (s[p] == '{') - (s[p] == '}')
                p += 1
            else:
                complete = False
        out.append({'start': m.start(), 'end': end, 'text': s[m.start():end],
                    'complete': complete, 'delimiter': token})
        pos = max(end, m.end())
    return out


def space(s):
    return re.sub(r'\s+', ' ', s).strip()


def mask_textboxes(s):
    """Mask wording, retaining nested math, for the structural comparison only.

    Full formulas remain in the audit data for every independently nonidentical
    pair. Annotation counts are checked separately without masking.
    """
    out = []
    pos = 0
    while m := TEXTBOX.search(s, pos):
        end = group_end(s, m.end()-1)
        if end is None:
            break
        interior = s[m.end():end-1]
        nested = math_segments(interior)
        skeleton = '·' + ''.join('⟦' + mask_textboxes(x['text']) + '⟧' for x in nested)
        out.extend((s[pos:m.end()], skeleton, '}'))
        pos = end
    out.append(s[pos:])
    return space(''.join(out))


def mask_markwords(s):
    return MARKWORD.sub(lambda m: '\\' + m[1] + '{⁘}', s)


def prose_regions(s):
    """Locate TikZ node bodies and parbox prose, without masking their geometry."""
    regions = []
    for m in re.finditer(r'\\node(?![A-Za-z])', s):
        p = m.end()
        groups = []
        while p < len(s) and s[p] != ';':
            if s[p] == '\\':
                p += 2
                continue
            if s[p] == '{':
                e = group_end(s, p)
                if e is None:
                    break
                groups.append((p, e))
                p = e
            else:
                p += 1
        if groups:
            a, b = groups[-1]
            regions.append((a+1, b-1, 'TikZ node body'))
    for m in re.finditer(r'\\parbox(?:\[[^]]*\])*\s*\{', s):
        e = group_end(s, m.end()-1)
        if e is None:
            continue
        p = e
        while p < len(s) and s[p].isspace():
            p += 1
        if p < len(s) and s[p] == '{':
            e2 = group_end(s, p)
            if e2:
                regions.append((p+1, e2-1, 'parbox wording'))
    return sorted(regions)


def compare_prose_regions(a, b):
    ar, br = prose_regions(a), prose_regions(b)
    if not ar or len(ar) != len(br):
        return None
    def masked(s, rs):
        for start, end, kind in reversed(rs):
            s = s[:start]+'PROSE'+s[end:]
        return space(s)
    outer = masked(a, ar) == masked(b, br)
    rows = []
    for (ai, aj, ak), (bi, bj, bk) in zip(ar, br):
        af, be = a[ai:aj], b[bi:bj]
        if af == be:
            continue
        afm = [mask_markwords(mask_textboxes(x['text'])) for x in math_segments(af)]
        bem = [mask_markwords(mask_textboxes(x['text'])) for x in math_segments(be)]
        rows.append({'kind': ak, 'french': af, 'english': be,
                     'embedded_math_exact': afm == bem,
                     'primary_mark_counts_exact': all(mark_counts(af)[k] == mark_counts(be)[k] for k in APPARATUS)})
    return {'geometry_and_other_code_exact': outer, 'changed_regions': rows,
            'all_embedded_math_exact': all(r['embedded_math_exact'] for r in rows),
            'all_primary_mark_counts_exact': all(r['primary_mark_counts_exact'] for r in rows)}


def classify_differences(differences):
    by_unit = {e['unit']: e for e in FORMULA_EXCEPTIONS}
    for i, d in enumerate(differences, 1):
        d['id'] = f'INDEPENDENT-FORMULA-{i:03d}'
        if d['operation'] == 'delete' and all(RAISED.match(x['text'].strip()) for x in d['french']):
            d['classification'] = 'French abbreviation ending written out in English'
            d['disposition'] = 'Preserve source; allowed by the supplied RAISED algorithm.'
        elif d['unit'] in by_unit and any(int(x['scan']) == by_unit[d['unit']]['scan'] for x in d['french']):
            ex = by_unit[d['unit']]
            d['classification'] = ex['class']
            d['disposition'] = 'Preserve supplied English; exact historical waiver and contextual audit recorded.'
            d['approved_exception_unit'] = ex['unit']
            if len(d['french']) == len(d['english']) == 1:
                old, new = ex['french_fragment'], ex['english_fragment']
                expected = d['french'][0]['text'].replace(old, new)
                d['approved_literal_transform_reproduces_structural_target'] = (
                    old in d['french'][0]['text'] and
                    mask_markwords(mask_textboxes(expected)) ==
                    mask_markwords(mask_textboxes(d['english'][0]['text'])))
            elif d['operation'] == 'delete':
                remaining = [x['text'] for x in math_segments(ex['french_fragment']) if not MBAR.match(x['text'].strip())]
                d['approved_literal_transform_reproduces_structural_target'] = (
                    remaining == [x['text'] for x in d['french']] and not math_segments(ex['english_fragment']))
            else:
                d['approved_literal_transform_reproduces_structural_target'] = False
            if not d['approved_literal_transform_reproduces_structural_target']:
                d['classification'] = 'UNCLASSIFIED'
        elif len(d['french']) == len(d['english']) == 1:
            r = compare_prose_regions(d['french'][0]['text'], d['english'][0]['text'])
            if r and r['geometry_and_other_code_exact'] and r['all_embedded_math_exact'] and r['all_primary_mark_counts_exact']:
                d['classification'] = 'Translated prose in TikZ nodes or parbox; embedded mathematics and geometry preserved'
                d['prose_region_check'] = r
                d['disposition'] = 'Preserve source; additional grouping caused by the independent outer-environment parser.'
            else:
                d['classification'] = 'UNCLASSIFIED'
                d['prose_region_check'] = r
        else:
            d['classification'] = 'UNCLASSIFIED'
    return differences


def contextual_exceptions(manifest, waivers):
    by_pkg = {p['package']: p for p in manifest['packages']}
    out = []
    for i, entry in enumerate(FORMULA_EXCEPTIONS, 1):
        row = dict(entry)
        pkg = entry['unit'].split('_s')[0]
        row.update({'id': f'HISTORICAL-FORMULA-{i:02d}', 'package': pkg, 'cote': by_pkg[pkg]['cote'],
                    'disposition': 'Retain the supplied source; do not silently rewrite the formula or doubt.'})
        for lang, file_ in [('french', SRC/'fr/texts'/(pkg+'.tex')), ('english', SRC/'en/packages'/(pkg+'_en.tex'))]:
            body = read(file_)
            segment = next((x for x in scans(body) if int(x[0]) == row['scan']))
            offset = segment[2].find(row[lang+'_fragment'])
            row[lang+'_fragment_occurrences_on_scan'] = segment[2].count(row[lang+'_fragment'])
            row[lang+'_source'] = file_.relative_to(SRC).as_posix()
            row[lang+'_line'] = body[:segment[1]+offset].count('\n')+1 if offset >= 0 else None
            row[lang+'_context'] = segment[2][max(0, offset-150):offset+len(row[lang+'_fragment'])+150] if offset >= 0 else None
        row['historical_waivers'] = [w for w in waivers if w['unit'] == row['unit'] and 'formulas:' in w.get('fail', '')]
        out.append(row)
    return out


def comments(s):
    return re.findall(r'(?<!\\)%[^\n]*', s)


def balanced(s):
    s = uncomment(s)
    depth = 0
    i = 0
    bad = False
    while i < len(s):
        if s[i] == '\\':
            i += 2
            continue
        depth += (s[i] == '{') - (s[i] == '}')
        bad |= depth < 0
        i += 1
    begins = collections.Counter(re.findall(r'\\begin\{([^}]*)\}', s))
    ends = collections.Counter(re.findall(r'\\end\{([^}]*)\}', s))
    segments = math_segments(s)
    residue = s
    for x in reversed(segments):
        residue = residue[:x['start']] + ' ' * (x['end']-x['start']) + residue[x['end']:]
    stray = [m[0] for m in re.finditer(r'\\\[|\\\]|\\\(|\\\)|\$', residue) if not escaped(residue, m.start())]
    return {'braces_balanced': not depth and not bad, 'environments_balanced': begins == ends,
            'all_math_segments_closed': all(x['complete'] for x in segments),
            'stray_math_delimiters': stray}


def formula_audit(fr, en, uid):
    fs = math_segments(fr)
    es = math_segments(en)
    fm = [x for x in fs if MBAR.match(x['text'].strip())]
    em = [x for x in es if MBAR.match(x['text'].strip())]
    fs = [x for x in fs if not MBAR.match(x['text'].strip())]
    es = [x for x in es if not MBAR.match(x['text'].strip())]
    for all_, body in ((fs, fr), (es, en)):
        sp = scans(body)
        for x in all_:
            x['key'] = mask_markwords(mask_textboxes(x['text']))
            x['line'] = body[:x['start']].count('\n') + 1
            x['scan'] = next((n for n, pos, _ in reversed(sp) if pos <= x['start']), '')
    a = [x['key'] for x in fs]
    b = [x['key'] for x in es]
    equal = raw_equal = 0
    text_pairs = []
    differences = []
    for op, ai, aj, bi, bj in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            equal += aj-ai
            for x, y in zip(fs[ai:aj], es[bi:bj]):
                if x['text'] == y['text']:
                    raw_equal += 1
                else:
                    text_pairs.append({'unit': uid, 'scan': x['scan'], 'french_line': x['line'],
                                       'english_line': y['line'], 'french': x['text'], 'english': y['text'],
                                       'classification': 'whitespace' if space(x['text']) == space(y['text']) else 'text-mode or marked-word wording'})
        else:
            for x in fs[ai:aj]:
                x.pop('key', None)
            for x in es[bi:bj]:
                x.pop('key', None)
            differences.append({'operation': op, 'french': fs[ai:aj], 'english': es[bi:bj]})
    return {'french': len(fs), 'english': len(es), 'raw_identical': raw_equal,
            'structurally_identical': equal, 'text_or_space_pairs': text_pairs,
            'standalone_mbar_french': len(fm), 'standalone_mbar_english': len(em),
            'differences': differences,
            'incomplete_french': [x for x in fs if not x['complete']],
            'incomplete_english': [x for x in es if not x['complete']]}


def read_jsonl(path):
    return [json.loads(x) for x in read(path).splitlines() if x.strip()]


def main():
    manifest = json.loads(read(SRC/'en/MANIFEST.json'))
    checked = json.loads(read(SRC/'en/checks/CHECKS.json'))
    fixes = read_jsonl(SRC/'en/checks/FIXES.jsonl')
    waivers = read_jsonl(SRC/'en/checks/WAIVERS.jsonl')
    units = {u['id']: u for u in manifest['units']}
    failure = []
    hashes = []
    for mp in sorted(SRC.glob('*_MANIFEST.tsv')):
        for r in csv.DictReader(mp.open(encoding='utf-8'), delimiter='\t'):
            p = SRC/r['path']
            actual = p.read_bytes() if p.exists() else b''
            row = {'manifest': mp.name, 'path': r['path'], 'recorded_bytes': int(r['bytes']),
                   'actual_bytes': len(actual), 'recorded_sha256': r['sha256'], 'actual_sha256': sha(actual),
                   'pass': p.exists() and len(actual) == int(r['bytes']) and sha(actual) == r['sha256']}
            hashes.append(row)
            if not row['pass']:
                failure.append('raw manifest mismatch: '+r['path'])
    index = list(csv.DictReader((SRC/'fr/records/CURRENT_TEXT_INDEX.tsv').open(encoding='utf-8'), delimiter='\t'))
    index_hash = sha((SRC/'fr/records/CURRENT_TEXT_INDEX.tsv').read_bytes())
    packages = []
    unit_rows = []
    per_scan = []
    differences = []
    text_pairs = []
    structural_totals = collections.Counter()
    formula_record_totals = collections.Counter()
    historical_differences = []
    fix_witnesses = []
    english_units_on_disk = sorted(p.relative_to(SRC/'en/units').as_posix() for p in (SRC/'en/units').rglob('*.tex'))
    french_units_on_disk = sorted(p.stem for p in (SRC/'en/french_units').glob('*.tex'))
    expected_en = sorted(u['package']+'/'+u['id']+'.tex' for u in manifest['units'])
    expected_fr = sorted(units)
    consumed = []
    for pi, pk in enumerate(manifest['packages'], 1):
        pkg = pk['package']
        fp = SRC/'fr/texts'/(pkg+'.tex')
        ep = SRC/'en/packages'/(pkg+'_en.tex')
        fr, en = read(fp), read(ep)
        fr_parts, en_parts = [], []
        fr_raw_parts, en_raw_parts = [], []
        prev_end = 0
        pkg_units = []
        for ui, uid in enumerate(pk['units'], 1):
            consumed.append(uid)
            u = units[uid]
            fu_path = SRC/'en/french_units'/(uid+'.tex')
            eu_path = SRC/'en/units'/pkg/(uid+'.tex')
            fu, eu = read(fu_path), read(eu_path)
            fr_parts.append(fu)
            en_parts.append(u['lead'] + eu.strip('\n') + u['trail'])
            fr_raw_parts.append(fu_path.read_bytes())
            en_raw_parts.append(u['lead'].encode()+eu_path.read_bytes().strip(b'\n')+u['trail'].encode())
            usc = [x[0] for x in scans(fu)]
            ur = {'unit': uid, 'package': pkg, 'cote': pk['cote'], 'package_order': pi,
                  'unit_order_within_package': ui, 'global_order': len(consumed),
                  'start': u['start'], 'end': u['end'], 'scans': usc,
                  'recorded_unit_sha256': u['sha256'], 'actual_normalized_sha256': sha(fu.encode()),
                  'french_raw_sha256': sha(fu_path.read_bytes()), 'english_raw_sha256': sha(eu_path.read_bytes()),
                  'offsets_contiguous': u['start'] == prev_end,
                  'source_slice_exact': fr[u['start']:u['end']] == fu,
                  'unit_sha_exact': sha(fu.encode()) == u['sha256'],
                  'recorded_chars_exact': len(fu.strip('\n')+'\n') == u['chars'],
                  'scans_exact': usc == u['scans'] and usc == [x[0] for x in scans(eu)],
                  'anchors_exact': anchor_sequence(fu) == anchor_sequence(eu),
                  'comments_sequence_exact': comments(fu) == comments(eu),
                  'comments_multiset_exact': collections.Counter(comments(fu)) == collections.Counter(comments(eu)),
                  'tags_exact': args(fu, 'tag') == args(eu, 'tag'),
                  'environment_counts_exact': collections.Counter(re.findall(r'\\begin\{([^}]+)\}', uncomment(fu))) == collections.Counter(re.findall(r'\\begin\{([^}]+)\}', uncomment(eu))),
                  'illegible_arguments_exact': args(fu, 'illegible') == args(eu, 'illegible'),
                  'french_balance': balanced(fu), 'english_balance': balanced(eu),
                  'historical_check_verdict': checked.get(uid, {}).get('verdict'),
                  'historical_waiver_count': sum(w['unit'] == uid for w in waivers)}
            pkg_units.append(ur)
            unit_rows.append(ur)
            prev_end = u['end']
            for k in ('offsets_contiguous', 'source_slice_exact', 'unit_sha_exact', 'recorded_chars_exact',
                      'scans_exact', 'anchors_exact', 'comments_multiset_exact', 'tags_exact', 'environment_counts_exact', 'illegible_arguments_exact'):
                if not ur[k]:
                    failure.append(uid+': '+k)
            for lang in ('french', 'english'):
                bal = ur[lang+'_balance']
                if not all(v for k, v in bal.items() if k != 'stray_math_delimiters') or bal['stray_math_delimiters']:
                    failure.append(uid+': '+lang+' balance')
            fa = formula_audit(fu, eu, uid)
            for k in ('french', 'english', 'raw_identical', 'structurally_identical', 'standalone_mbar_french', 'standalone_mbar_english'):
                structural_totals[k] += fa[k]
            text_pairs.extend(fa['text_or_space_pairs'])
            for d in fa['differences']:
                differences.append({'unit': uid, 'package': pkg, 'cote': pk['cote'], **d})
            ur['independent_formulas'] = {k: v for k, v in fa.items() if k not in ('text_or_space_pairs', 'differences')}
            ur['independent_formulas']['difference_groups'] = len(fa['differences'])
            r = checked[uid]
            for k, v in r['formulas'].items():
                formula_record_totals[k] += v if isinstance(v, int) else len(v)
            for typ in ('changed', 'missing', 'added', 'text_only', 'raised_endings'):
                for item in r['formulas'].get(typ, []):
                    historical_differences.append({'unit': uid, 'type': typ, 'value': item,
                                                  'waivers': [w for w in waivers if w['unit'] == uid]})
            for n, fix in enumerate(fixes, 1):
                if fix['unit'] != uid:
                    continue
                old_n = eu.count(fix.get('old', '')) if fix['kind'] == 'replace' else None
                new_n = eu.count(fix.get('new', '')) if fix['kind'] == 'replace' else None
                stated_scan = re.search(r'\bscan (\d+)', fix['reason'])
                actual_scans = []
                if fix['kind'] == 'replace':
                    for hit in re.finditer(re.escape(fix['new']), eu):
                        ss = [x[0] for x in scans(eu[:hit.start()])]
                        actual_scans.append(int(ss[-1]) if ss else None)
                fix_witnesses.append({'record_number': n, **fix, 'old_occurrences_in_final_unit': old_n,
                                      'new_occurrences_in_final_unit': new_n,
                                      'replacement_witness_present': new_n is not None and new_n >= fix['count'],
                                      'stated_scan_in_reason': int(stated_scan[1]) if stated_scan else None,
                                      'actual_scans_of_replacement_witnesses': actual_scans})
        pkg_sha = sha(fp.read_bytes())
        pr = {'package': pkg, 'order': pi, 'cote': pk['cote'], 'scan_range': pk['scans'],
              'unit_order': pk['units'], 'french_package_sha256': pkg_sha,
              'english_package_sha256': sha(ep.read_bytes()),
              'recorded_french_package_sha256': pk['sha256'], 'package_raw_sha_exact': pkg_sha == pk['sha256'],
              'french_unit_concatenation_exact': ''.join(fr_parts) == fr,
              'english_unit_assembly_exact': ''.join(en_parts) == en,
              'french_unit_raw_concatenation_identical': b''.join(fr_raw_parts) == fp.read_bytes(),
              'french_package_crlf_count': fp.read_bytes().count(b'\r\n'),
              'french_raw_difference_only_newlines': b''.join(fr_raw_parts).replace(b'\r\n',b'\n') == fp.read_bytes().replace(b'\r\n',b'\n'),
              'english_unit_assembly_raw_bytes_exact': b''.join(en_raw_parts) == ep.read_bytes(),
              'recorded_chars_exact': len(fr) == pk['chars'], 'final_offset_exact': prev_end == len(fr),
              'scan_count': len(scans(fr)), 'recorded_scan_count_exact': len(scans(fr)) == pk['n_scans'],
              'scan_sequence_exact': [x[0] for x in scans(fr)] == [x[0] for x in scans(en)]}
        packages.append(pr)
        for k, v in pr.items():
            if k.endswith('_exact') and not v:
                failure.append(pkg+': '+k)
        en_scans = {x[0]: x for x in scans(en)}
        for scan, start, ft in scans(fr):
            _, estart, et = en_scans[scan]
            fc, ec = mark_counts(ft), mark_counts(et)
            diff = {k: [fc[k], ec[k]] for k in fc if fc[k] != ec[k]}
            uid = next(u['unit'] for u in pkg_units if scan in u['scans'])
            frparas = [p for p in re.split(r'\n\s*\n', uncomment(ft)) if p.strip()]
            enparas = [p for p in re.split(r'\n\s*\n', uncomment(et)) if p.strip()]
            per_scan.append({'package': pkg, 'unit': uid, 'cote': pk['cote'], 'scan': int(scan),
                             'french_line': fr[:start].count('\n')+1, 'english_line': en[:estart].count('\n')+1,
                             'french_marks': fc, 'english_marks': ec, 'differences': diff,
                             'paragraphs_french': len(frparas), 'paragraphs_english': len(enparas),
                             'waivers': [w for w in waivers if w['unit'] == uid and ('apparatus' in w.get('fail','') or 'apparatus' in w.get('fail_prefix',''))]})
    globals_ = {'index_hash_recorded': manifest['input_sha256'], 'index_hash_actual': index_hash,
                'index_hash_exact': index_hash == manifest['input_sha256'],
                'package_order_matches_index': [p['package'] for p in manifest['packages']] == [p['package'] for p in index],
                'manifest_units_in_assembly_order': consumed == [u['id'] for u in manifest['units']],
                'every_manifest_unit_used_once': collections.Counter(consumed) == collections.Counter(units.keys()),
                'english_unit_files_exact_set': english_units_on_disk == expected_en,
                'french_unit_files_exact_set': french_units_on_disk == expected_fr,
                'checks_unit_set_exact': set(checked) == set(units),
                'missing_english_units': sorted(set(expected_en)-set(english_units_on_disk)),
                'extra_english_units': sorted(set(english_units_on_disk)-set(expected_en)),
                'missing_french_units': sorted(set(expected_fr)-set(french_units_on_disk)),
                'extra_french_units': sorted(set(french_units_on_disk)-set(expected_fr))}
    for k, v in globals_.items():
        if isinstance(v, bool) and not v:
            failure.append(k)
    coverage = {}
    for cote in ('140-1', '140-2', '140-3', '140-4'):
        ns = [r['scan'] for r in per_scan if r['cote'] == cote]
        coverage[cote] = {'scan_count': len(ns), 'distinct_scans': len(set(ns)),
                          'first': min(ns), 'last': max(ns), 'continuous_order': ns == list(range(1, max(ns)+1)),
                          'duplicates': [n for n, c in collections.Counter(ns).items() if c > 1],
                          'missing': sorted(set(range(1, max(ns)+1))-set(ns))}
    differences = classify_differences(differences)
    exceptions = contextual_exceptions(manifest, waivers)
    result = {'method_version': 1, 'source_files_modified': False,
              'scope': 'Attached source records only; no external checkout or network dependencies.',
              'original_checker_dependencies_missing': ['en/scripts/der/check_units.py', 'en/scripts/der/cmp/', 'external glossary common.py'],
              'historical_source_of_record_json_present': bool(list(SRC.rglob('SOURCE_OF_RECORD.json'))),
              'raw_manifest_checks': hashes, 'global_checks': globals_, 'packages': packages, 'units': unit_rows,
              'scan_coverage': coverage, 'per_scan_marks': per_scan, 'integrity_failures': failure,
              'independent_formula_totals': dict(structural_totals), 'independent_formula_differences': differences,
              'independent_formula_text_or_space_pairs': text_pairs,
              'historical_formula_totals': dict(formula_record_totals),
              'historical_formula_exceptions': historical_differences,
              'nine_historical_formula_contextual_audits': exceptions,
              'approved_source_fix_witnesses': fix_witnesses, 'historical_waivers': waivers,
              'current_edition_glossary_edits': json.loads(read(OUT/'data/glossary_edits.json')),
              'limits': ['Historical raw model outputs are not supplied, so earlier exact replacement execution counts cannot be independently replayed.',
                         'Masking prose in a text box is a structural comparison, not a proof that its translation preserves every mathematical assertion.',
                         'The original checker cannot be executed unchanged because its imported comparison libraries are absent.',
                         'Historical public-Git equality is not reverified: source_of_record.py is supplied but its generated JSON and checkout are absent.']}
    (OUT/'data/source_integrity.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    (OUT/'data/source_integrity_differences.json').write_text(json.dumps(differences, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'raw_files': len(hashes), 'packages': len(packages), 'units': len(unit_rows),
                      'scans': len(per_scan), 'integrity_failures': failure,
                      'independent_formula_totals': dict(structural_totals),
                      'independent_difference_groups': len(differences),
                      'text_or_space_pairs': len(text_pairs),
                      'unclassified_formula_groups': sum(d['classification'] == 'UNCLASSIFIED' for d in differences),
                      'historical_formula_totals': dict(formula_record_totals)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
