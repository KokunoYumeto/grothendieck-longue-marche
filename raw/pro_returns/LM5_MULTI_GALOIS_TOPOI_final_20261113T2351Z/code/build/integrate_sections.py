from pathlib import Path
import csv, re, shutil, sys, json

BASE = Path('/workspace/scratch/36f9c078cbe9')
OUT = BASE / 'deliverable'
parts = set(sys.argv[1] if len(sys.argv) > 1 else 'ABCDE')
source_dirs = ['root', 'spheres', 'foundations']
if 'F' in parts:
    source_dirs.append('montpellier')

for part in sorted(parts):
    source = BASE / 'work' / ('root' if part in 'BC' else 'spheres' if part == 'D' else 'foundations' if part in 'AE' else 'montpellier') / (part + '.tex')
    if part == 'F' and (BASE / 'work/montpellier/F_assembled.tex').exists():
        source = BASE / 'work/montpellier/F_assembled.tex'
    content = source.read_text()
    if part == 'E' and (BASE / 'work/foundations/E_additional_reconstruction.tex').exists():
        content += '\n' + (BASE / 'work/foundations/E_additional_reconstruction.tex').read_text()
        content += '\n' + (BASE / 'work/foundations/E_variable_shape_comparison.tex').read_text()
    if part == 'B' and (BASE / 'work/root/B_background_audit.tex').exists():
        marker = re.search(r'\\paragraph\{B\.4\b', content)
        content = content[:marker.start()] + (BASE / 'work/root/B_background_audit.tex').read_text() + '\n' + content[marker.start():]
    if part == 'F' and source.name != 'F_assembled.tex':
        local = (BASE / 'work/montpellier/F_local.tex').read_text()
        inv = (BASE / 'work/montpellier/F_invariance.tex').read_text()
        content = content.replace('\\subsection{Additional arithmetic tests and coherent limits}', local + '\n\\subsection{Additional arithmetic tests and coherent limits}')
        # Insert invariance immediately before F.43 if the writer has reached it.
        match = re.search(r'\\paragraph\{F\.43\b', content)
        if match:
            content = content[:match.start()] + inv + '\n' + content[match.start():]
        else:
            content += '\n' + inv
    if part == 'F':
        completion_audit = BASE / 'work/foundations/F43_completion_audit.tex'
        if completion_audit.exists():
            marker = re.search(r'\\paragraph\{F\.44\b', content)
            if marker:
                content = content[:marker.start()] + completion_audit.read_text() + '\n' + content[marker.start():]
        content += '\n' + (BASE / 'work/root/F_source_audit.tex').read_text()
        if (BASE / 'work/montpellier/F49.tex').exists():
            content += '\n' + (BASE / 'work/montpellier/F49.tex').read_text()
        if (BASE / 'work/montpellier/F50.tex').exists():
            content += '\n' + (BASE / 'work/montpellier/F50.tex').read_text()
        if (BASE / 'work/foundations/F51.tex').exists():
            content += '\n' + (BASE / 'work/foundations/F51.tex').read_text()
    content = content.replace('\\cite{', '\\citep{')
    content = content.replace('\\texttt{LM8\\_LIE\\_APPROXIMATIONS\\_background.zip}', '\\path{LM8_LIE_APPROXIMATIONS_background.zip}')
    code_owner = 'root' if part in 'BC' else 'foundations' if part in 'AE' else 'spheres' if part == 'D' else 'montpellier'
    def qualify_code(m):
        name = m.group(1)
        for owner in [code_owner] + [x for x in source_dirs if x != code_owner]:
            if '/' not in name and (BASE / 'work' / owner / 'code' / name.replace('\\_', '_')).exists():
                return '\\texttt{code/' + owner + '/' + name + '}'
        return m.group()
    content = re.sub(r'\\texttt\{code/([^}]+)\}', qualify_code, content)
    content = re.sub(r'\\texttt\{(code/[^}]+)\}', lambda m: '\\path{' + m.group(1).replace('\\_', '_') + '}', content)
    content = re.sub(r'\\begin\{proof\}.*?\\end\{proof\}', lambda m: m.group().replace('\\hfill$\\square$', ''), content, flags=re.S)
    (OUT / 'sections' / (part + '.tex')).write_text(content)

result_files = [BASE / 'work/root/B_results.csv', BASE / 'work/root/C_results.csv', BASE / 'work/spheres/results.csv', BASE / 'work/foundations/results.csv']
result_files += [BASE / 'work/foundations/E_additional_results.csv']
if 'F' in parts:
    result_files += [BASE / 'work/montpellier/results.csv', BASE / 'work/montpellier/local_results.csv', BASE / 'work/montpellier/invariance_results.csv']
    result_files += [BASE / 'work/root/source_audit_results.csv', BASE / 'work/montpellier/F49_results.csv']
    result_files += [BASE / 'work/montpellier/F50_results.csv']
    result_files += [BASE / 'work/foundations/F51_results.csv']
rows = []
fields = None
for path in result_files:
    if not path.exists():
        continue
    with path.open(newline='') as f:
        reader = csv.DictReader(f)
        fields = fields or reader.fieldnames
        for row in reader:
            if row['id'].split('.')[0] not in parts:
                continue
            row['status'] = next((s for s in ['Proved','Refuted','Known','Open'] if row['status'].startswith(s)), row['status'])
            p = row['id'].split('.')[0]
            row['where_proved'] = f'sections/{p}.tex, {row["id"]}'
            rows.append(row)
rows = list({r['id']:r for r in rows}.values())
rows.sort(key=lambda x: (x['id'].split('.')[0], int(x['id'].split('.')[1])))
with (OUT / 'LM5_MULTI_GALOIS_TOPOI_results.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader(); writer.writerows(rows)

reading_files = [BASE / 'work/root/readings.csv', BASE / 'work/spheres/readings.csv', BASE / 'work/foundations/readings.csv']
if 'F' in parts:
    reading_files += [BASE / 'work/montpellier/readings.csv', BASE / 'work/montpellier/local_readings.csv', BASE / 'work/montpellier/invariance_readings.csv']
    reading_files += [BASE / 'work/root/source_audit_readings.csv', BASE / 'work/montpellier/F49_readings.csv']
    reading_files += [BASE / 'work/foundations/F51_readings.csv']
rrows, rfields = [], None
for path in reading_files:
    if not path.exists():
        continue
    with path.open(newline='') as f:
        reader = csv.DictReader(f); rfields = rfields or reader.fieldnames
        rrows.extend(reader)
rrows = list({tuple((k,r.get(k,'')) for k in rfields):r for r in rrows}.values())
with (OUT / 'LM5_MULTI_GALOIS_TOPOI_readings.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=rfields)
    writer.writeheader(); writer.writerows(rrows)

bibfiles = [BASE / ('work/' + d + ('/references_all.bib' if d == 'montpellier' and (BASE / 'work/montpellier/references_all.bib').exists() else '/references.bib')) for d in source_dirs]
if 'F' in parts:
    bibfiles += [BASE / 'work/montpellier/local_refs.bib', BASE / 'work/montpellier/invariance_refs.bib']
    bibfiles += [BASE / 'work/foundations/F43_completion_references.bib']
    bibfiles += [BASE / 'work/montpellier/F50_references.bib']
    bibfiles += [BASE / 'work/foundations/F51_references.bib']
entries, identity, aliases = {}, {}, {}
for path in bibfiles:
    if not path.exists():
        continue
    for m in re.finditer(r'(?ms)^@(\w+)\{([^,]+),\s*\n.*?^\}', path.read_text()):
        entry = m.group(); key = m.group(2).strip()
        doi = re.search(r'\bdoi\s*=\s*\{([^}]+)\}', entry, re.I)
        url = re.search(r'\burl\s*=\s*\{([^}]+)\}', entry, re.I)
        ident = ('doi:' + doi.group(1).lower()) if doi else ('url:' + url.group(1).rstrip('/')) if url else 'key:' + key
        if url and url.group(1).endswith('/exodromy_book.pdf'):
            ident = 'work:Exodromy2020'
        prior = identity.get(ident)
        if prior and prior != key:
            aliases[key] = prior
            continue
        if key in entries:
            # Preserve the first integrated citation identity; originals are retained below.
            continue
        entries[key] = entry
        identity[ident] = key
(OUT / 'LM5_MULTI_GALOIS_TOPOI_references.bib').write_text('\n\n'.join(entries.values()) + '\n')
for part in parts:
    path = OUT / 'sections' / (part + '.tex')
    txt = path.read_text()
    for alias, target in aliases.items():
        txt = txt.replace('{' + alias + '}', '{' + target + '}')
    # Every numbered manuscript response carries its coordinate in the paper,
    # in addition to the machine-readable register.
    part_rows = {r['id']:r for r in rows if r['id'].startswith(part + '.')}
    for m in reversed(list(re.finditer(r'\\paragraph\{([A-F]\.\d+)\b',txt))):
        pos = txt.index('{',m.start()); depth=1; end=pos+1
        while depth:
            if txt[end]=='{' and txt[end-1]!='\\': depth+=1
            if txt[end]=='}' and txt[end-1]!='\\': depth-=1
            end+=1
        next_para = txt.find('\\paragraph{',end)
        span = txt[end:next_para if next_para>=0 else len(txt)]
        if re.search(r'\\textit\{Manuscript',span[:750]):
            continue
        coord = part_rows[m.group(1)]['manuscript_passages (section; folio; scan)']
        coord = coord.replace('§',r'\S ').replace('&',r'\&').replace('_',r'\_').replace('%',r'\%')
        txt = txt[:end] + '\n\\textit{Manuscript: ' + coord + '.}\n' + txt[end:]
    txt = re.sub(r'(?=\\paragraph\{[A-F]\.\d+\s*\()', lambda m: '\\Needspace{5\\baselineskip}\n', txt)
    path.write_text(txt)

for d in source_dirs:
    src = BASE / 'work' / d
    dest = OUT / 'source_parts' / d
    dest.mkdir(parents=True, exist_ok=True)
    for path in sorted(src.iterdir()):
        if path.is_file() and path.suffix in {'.tex', '.md', '.csv', '.bib', '.json'}:
            shutil.copy2(path, dest / path.name)
    if (src / 'code').exists():
        shutil.copytree(src / 'code', OUT / 'code' / d, dirs_exist_ok=True)
if 'F' in parts:
    for prefix in ['local','invariance']:
        for path in (BASE / 'work/montpellier').glob(prefix + '*'):
            if path.is_file():
                shutil.copy2(path, OUT / 'source_parts/montpellier' / path.name)
for name in ['missing_sources_additional_search.json']:
    if (BASE / 'work/root' / name).exists():
        shutil.copy2(BASE / 'work/root' / name, OUT / 'source_parts/root' / name)

print(json.dumps({'integrated_parts':sorted(parts),'statements':len(rows),'readings':len(rrows),'bibliography_entries':len(entries),'bibliography_aliases':aliases},indent=2))
