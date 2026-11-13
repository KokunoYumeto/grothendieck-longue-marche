from pathlib import Path
import sys, json, re, subprocess
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, mechanical_repairs, fitz
from texenv import environment

D = Path('work/layout_probes')
records = []
jobs = []
for lang in ('fr', 'en'):
    displays = []
    for package, scan, tag in [('LM_C3-473-491', 480, '12 bis'),
                               ('LM_C3-473-491', 480, '13'),
                               ('LM_C3-549-567', 554, '29')]:
        path = Path('sources/fr/texts' if lang == 'fr' else 'sources/en/packages') / (package + ('_en' if lang == 'en' else '') + '.tex')
        text = path.read_text()
        text, _ = mechanical_repairs.repair(text, package, lang)
        start = text.index(r'\scanpage{' + str(scan) + '}')
        end = text.find(r'\scanpage{', start + 1)
        section = text[start:end if end >= 0 else len(text)]
        match = next(m for m in re.finditer(r'\\\[.*?\\\]', section, re.S)
                     if r'\tag{' + tag + '}' in m[0])
        old = match[0]
        new = old
        if tag == '12 bis':
            labels = [r'{\chi=\det\circ\Theta_G}',
                      r'{\varepsilon_2=\varepsilon_\sigma\circ\Theta_\sigma}',
                      r'{\varepsilon_3(x)=\frac{\det\underline a}{\det\underline b}}']
            for label in labels:
                before = '"' + label + '"]'
                after = '"' + label + '"{yshift=3pt}]'
                assert new.count(before) == 1, (lang, tag, before)
                new = new.replace(before, after)
            reason = 'Raise the three unchanged arrow labels by 3pt so their final subscripts and denominator clear the arrowhead barbs; preserve endpoints, horizontal spacing, notation and type size.'
        elif tag == '13':
            before = r'"{(\Theta_G,\Theta_\rho,\Theta_\sigma,\chi,\varepsilon_2,\varepsilon_3)}"]'
            after = r'"{(\Theta_G,\Theta_\rho,\Theta_\sigma,\chi,\varepsilon_2,\varepsilon_3)}"{yshift=5pt}]'
            assert new.count(before) == 1, (lang, tag, before)
            new = new.replace(before, after)
            reason = 'Raise the unchanged character tuple by 5pt so it clears the injection arrowhead and adjacent product object; preserve endpoints, horizontal spacing, notation and type size.'
        else:
            before = '"{(\\chi_G,\\varepsilon_G,\\varepsilon\'_G)}"]'
            after = '"{(\\chi_G,\\varepsilon_G,\\varepsilon\'_G)}"{yshift=3pt}]'
            assert new.count(before) == 1, (lang, tag, before)
            new = new.replace(before, after)
            reason = 'Raise the unchanged character tuple by 3pt so its final subscript clears the arrowhead barb; preserve endpoints, horizontal spacing, notation and type size.'
        records.append(dict(language=lang, package=package, scan=scan, tag=tag,
                            old=old, new=new, reason=reason))
        # Macro-argument-safe ampersands are only needed in a stand-alone probe
        # if the checked package was not among the mechanical-repair inputs.
        probe = new
        probe = re.sub(r'(?<!\\)&', r'\\&', probe)
        probe = re.sub(r'\\begin\{tikzcd\}\[([^\]]*)\]',
                       lambda m: m[0] if 'ampersand replacement' in m[1] else
                       r'\begin{tikzcd}[ampersand replacement=\&,' + m[1] + ']', probe)
        if tag == '29':
            displays.append(r'\clearpage\scanpage{554}')
        displays.append(probe)
    target = D / f'scan480_554_candidate_{lang}.tex'
    target.write_text(build_readers.preamble(lang, 1) +
                      '\n\\begin{document}\\LMcote{140-3}\\scanpage{480}\n' +
                      '\n'.join(displays) + '\n\\end{document}\n')
    job = subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode',
                            '-halt-on-error', target.name], cwd=D, env=environment(),
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    jobs.append((lang, target, job))
(D / 'scan480_554_candidate.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
for lang, target, job in jobs:
    stdout, _ = job.communicate()
    target.with_suffix('.console.txt').write_text(stdout)
    log = target.with_suffix('.log').read_text(errors='replace')
    print(lang, dict(exit=job.returncode, overfull=log.count('Overfull'), missing=log.count('Missing character')), flush=True)
    if job.returncode:
        print('\n'.join(x for x in log.splitlines() if x.startswith('!') or 'Error' in x))
        raise SystemExit(job.returncode)
    for i, page in enumerate(fitz.open(target.with_suffix('.pdf'))):
        page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(35, 60, 565, 280)).save(D / f'scan480_554_candidate_{lang}_{i}.png')
