"""Prepare, then explicitly install the reviewed revision512 repair batch.

Default execution writes only staged files under work/layout_probes.  The
--commit switch is reserved for the coordinated source-write release.  Every
candidate/validation hash is pinned by layout_pending_batch.json; manuscript
sources are never written.
"""
from pathlib import Path
from collections import Counter
import argparse, hashlib, importlib, json, subprocess, sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'work/scripts'))
import build_readers, mechanical_repairs, layout_repairs

BASE_SHA = '490fca7ed09114abba7ba087915e58a6ba9f9a1aeb0adc960414173495d1f1a4'
D = ROOT/'work/layout_probes'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def identifier(row, name):
    if 'id' in row:
        return row['id']
    cote = layout_repairs.COVERAGE[row['package']]['cote']
    suffix = {
        'scan441_eq117': 'L1', 'scan443_520_labels': 'L1',
        'scan408_eq44': 'L1', 'scan637_blue_note': 'L1',
        'section12': 'H12', 'sectionII': 'HII', 'remarque221': 'HRemark',
        'section565': 'H6', 'scan419_circled3': 'H3', 'cancelled_tags': 'CT1',
    }.get(name)
    if name == 'scan449_labels':
        suffix = 'L1' if str(row['tag']) == '137' else 'L2'
    if suffix is None:
        raise ValueError(('Explicit stable ID required', name, row['scan']))
    return f'{cote}-{row["scan"]}-{suffix}'


VIEWS = {}
def source_views(package, language):
    key = package, language
    if key not in VIEWS:
        raw = build_readers.raw_package(package, language)
        mechanical, _ = mechanical_repairs.repair(raw, package, language)
        VIEWS[key] = [layout_repairs.repair(t, package, language, include_pagination=False)[0]
                      for t in (raw, mechanical)]
    return VIEWS[key]


def inverse_ampersand(text):
    # This extra syntax is accepted only if it matches the complete raw span
    # exactly once.  It is not a runtime normalization or search fallback.
    return (text.replace(r'[ampersand replacement=\&,', '[')
            .replace(r'[ampersand replacement=\&]', '')
            .replace(r'\&', '&'))


def normalize(row, name, stage):
    options = row.get('variants', [{'old': row.get('old'), 'new': row.get('new')}])
    options = [dict(old=p['old'], new=p['new']) for p in options]
    for p in list(options):
        inv = {k: inverse_ampersand(v) for k, v in p.items()}
        if inv not in options:
            options.append(inv)
        normalized = {k: mechanical_repairs.repair(v, row['package'], row['language'])[0]
                      for k, v in p.items()}
        if normalized not in options:
            options.append(normalized)
    used = []
    for text in source_views(row['package'], row['language']):
        matches = [p for p in options if text.count(p['old']) == 1]
        if len(matches) != 1:
            raise ValueError(('Expected one literal candidate in source view', name,
                              row['language'], row['scan'], len(matches)))
        if matches[0] not in used:
            used.append(matches[0])
    ident = identifier(row, name)
    kind = row.get('kind', 'diagram label clearance')
    if name == 'cancelled_tags':
        kind = 'cancelled equation-tag presentation'
    if stage == 'pagination':
        kind = row.get('kind', 'section-heading pagination')
    result = dict(id=ident, language=row['language'], package=row['package'],
                  scan=int(row['scan']), kind=kind, reason=row['reason'],
                  variants=used, candidate_source=name)
    if stage == 'after_geometry':
        result['stage'] = 'after_geometry'
    else:
        result['tag'] = str(row.get('tag', ident.rsplit('-', 1)[-1]))
        result['source_pattern'] = row.get('source_pattern',
            'Visually confirmed exact source heading or tagged introduction; accepted paired constrained-placement probe')
    return result


POST_FUNCTION = '''def repair_after_geometry(text,package,language):
    """Replay the explicitly accepted literal refinements after local geometry.

    Targets are fixed source spans, shared by all three forms; no runtime
    fitting, generic label movement or suppression of overflow is involved.
    """
    records=[];present={n for n,a,b in _scan_ranges(text)}
    for target in json.loads((ROOT/'work/data/layout_label_clearances.json').read_text()):
        if target.get('stage')!='after_geometry':continue
        if target['package']!=package or target['language']!=language or target['scan'] not in present:continue
        def fix(t):
            matches=[p for p in target['variants'] if t.count(p['old'])==1]
            if len(matches)!=1:raise ValueError(f'Expected one exact post-geometry patch: {package} {language} {target["id"]}; found {len(matches)}')
            patch=matches[0]
            result,local=_edit(t,patch['old'],patch['new'],target['reason'],kind=target['kind'])
            for r in local:r['id']=target['id']
            return result,local
        text=_replace_scan(text,target['scan'],fix,records,package,language)
    return text,records


'''

FINALIZER_ADDITION = '''    additions=Path('work/data/layout_pagination_additions.json')
    if additions.exists():
        for extra in json.loads(additions.read_text()):
            # Each stored syntax must still match a raw/mechanical source view;
            # the final replay also rejects any overlap with an earlier pair.
            for mechanical in [False,True]:
                t=view(extra['package'],extra['language'],mechanical)
                matches=[p for p in extra['variants'] if t.count(p['old'])==1]
                assert len(matches)==1,(extra['id'],extra['language'],mechanical,'literal pagination addition')
            rows.append(extra)
'''


def prepare():
    module_path = ROOT/'work/scripts/layout_repairs.py'
    assert sha(module_path) == BASE_SHA, 'The revision512 base module has changed; do not rebase silently.'
    manifest = json.loads((ROOT/'work/data/layout_pending_batch.json').read_text())
    label_data = json.loads((ROOT/'work/data/layout_label_clearances.json').read_text())
    existing_ids = {(r['id'], r['language']) for r in label_data}
    extras = []; added = []; replaced = []
    for item in manifest['items']:
        path = ROOT/item['candidate']; validation = ROOT/item['validation']
        assert sha(path) == item['candidate_sha256'], path
        assert sha(validation) == item['validation_sha256'], validation
        status = json.loads(validation.read_text())['status']
        assert 'PASS' in status or 'CLEARED' in status, (path, status)
        raw_rows = json.loads(path.read_text())
        rows = raw_rows['records'] if isinstance(raw_rows, dict) else raw_rows
        for row in rows:
            if item['stage'] == 'replace_existing':
                indices = [i for i, r in enumerate(label_data)
                           if (r['id'], r['language']) == (row['id'], row['language'])]
                assert len(indices) == 1
                original = label_data[indices[0]]
                assert original['old'] == row['old'] and original['new'] == row['previous_new']
                original['new'] = row['new']; original['reason'] = row['reason']
                original['kind'] = row['kind']
                replaced.append(dict(id=row['id'], language=row['language']))
                continue
            target = normalize(row, item['name'], item['stage'])
            if item['stage'] == 'after_geometry':
                assert (target['id'], target['language']) not in existing_ids
                label_data.append(target); existing_ids.add((target['id'], target['language']))
            elif item['stage'] == 'pagination':
                extras.append(target)
            else:
                raise ValueError(('Unsupported integration stage', item))
            added.append(dict(id=target['id'], language=target['language'], stage=item['stage']))
    assert len({(r['id'], r['language']) for r in extras}) == len(extras)
    module = module_path.read_text()
    filter_anchor = "        if (target['package'],target['scan'],target['language'])!=(package,scan,language):continue"
    assert module.count(filter_anchor) == 1
    module = module.replace(filter_anchor, "        if target.get('stage','before_geometry')!='before_geometry':continue\n" + filter_anchor)
    anchor = 'def repair_tag_bindings(text,package,language):'
    assert module.count(anchor) == 1
    module = module.replace(anchor, POST_FUNCTION+anchor)
    anchor = '    records+=pair_records\n    if include_pagination:'
    assert module.count(anchor) == 1
    module = module.replace(anchor, '    records+=pair_records\n    text,post_records=repair_after_geometry(text,package,language)\n    records+=post_records\n    if include_pagination:')
    finalizer = (D/'finalize_tag_bindings.py').read_text()
    anchor = "    rows.sort(key=lambda r:(r['package'],r['scan'],r['language'],r['id']))"
    assert finalizer.count(anchor) == 1 and 'layout_pagination_additions.json' not in finalizer
    finalizer = finalizer.replace(anchor, FINALIZER_ADDITION+anchor)
    audit = (ROOT/'work/scripts/audit_layout_repair_integrity.py').read_text()
    audit = audit.replace('Needspace baselineskip allowbreak', 'Needspace baselineskip par nobreak allowbreak')
    old = "def commands(t):return Counter(x for x in re.findall(r'\\\\([A-Za-z@]+)',t) if x not in ALLOW)"
    new = "def commands(t):\n # The source-local cancelled-tag wrapper has the same semantic tag argument.\n t=t.replace(r'\\LMcancelledtag',r'\\tag')\n return Counter(x for x in re.findall(r'\\\\([A-Za-z@]+)',t) if x not in ALLOW)"
    assert audit.count(old) == 1
    audit = audit.replace(old, new)
    anchor = " obj['local_size_gate']=audit_layout_sizes.audit(records)"
    assert audit.count(anchor) == 1
    audit = audit.replace(anchor,
        " obj['presentation_command_projection']={'LMcancelledtag':'tag','reason':'The exact source-local wrapper preserves the original equation-tag argument; its form-dependent parentheses are presentation only.'}\n"+anchor)
    staged = {
        'work/scripts/layout_repairs.py': module,
        'work/data/layout_label_clearances.json': json.dumps(label_data,ensure_ascii=False,indent=2)+'\n',
        'work/data/layout_pagination_additions.json': json.dumps(extras,ensure_ascii=False,indent=2)+'\n',
        'work/layout_probes/finalize_tag_bindings.py': finalizer,
        'work/scripts/audit_layout_repair_integrity.py': audit,
    }
    for dest, contents in staged.items():
        path = D/('staged_'+Path(dest).name); path.write_text(contents)
        if path.suffix == '.py':
            compile(contents, str(path), 'exec')
    proposal = dict(status='STAGED_NOT_INSTALLED', base_module_sha256=BASE_SHA,
                    additions=len(added), replacement_records=len(replaced),
                    pagination_additions=len(extras), expected_total_records=512+len(added),
                    pending_candidates=manifest['pending_candidates'],
                    added=added, replaced=replaced,
                    files=[dict(destination=dest, staged=str((D/('staged_'+Path(dest).name)).relative_to(ROOT)),
                                sha256=sha(D/('staged_'+Path(dest).name))) for dest in staged])
    (D/'staged_integration_summary.json').write_text(json.dumps(proposal,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:proposal[k] for k in ['status','additions','replacement_records','pagination_additions','expected_total_records','pending_candidates']}),flush=True)
    return staged, proposal


def run(script, *args):
    subprocess.run([sys.executable, str(ROOT/script), *args], cwd=ROOT, check=True)


def commit(staged, proposal):
    assert not proposal['pending_candidates'], 'Outstanding probes prevent source integration.'
    backup = D/'revision512_dependency_backup'; backup.mkdir(exist_ok=False)
    preserved = set(staged) | {
        'work/data/layout_expected_matches.json',
        'work/data/layout_geometry_expected_matches.json',
        'work/data/layout_tag_bindings.json',
        'work/data/layout_diagram_targets.json',
        'work/data/layout_cancelled_cells.json',
        'work/data/layout_release_checkpoint.json',
        'work/data/final_build_inputs.json',
        'work/data/layout_repairs_applied.json',
        'work/data/layout_semantic_command_audit.json',
    }
    for dest in sorted(preserved):
        path = ROOT/dest
        if path.exists():
            (backup/path.name).write_bytes(path.read_bytes())
    for dest, contents in staged.items():
        (ROOT/dest).write_text(contents)
    importlib.reload(layout_repairs)
    counts = Counter()
    for lang in ('fr','en'):
        for pkg in layout_repairs.COVERAGE:
            _, records = layout_repairs.repair(build_readers.raw_package(pkg,lang),pkg,lang,include_pagination=False)
            for r in records:
                if r['kind'] not in ('empty diagram cell','manuscript-page placement','paired marginal notes'):
                    counts[lang,pkg,r['scan']] += 1
    def expected(counter):
        return [dict(language=lang,package=pkg,scan=scan,expected_changes=n)
                for (lang,pkg,scan),n in sorted(counter.items())]
    (ROOT/'work/data/layout_geometry_expected_matches.json').write_text(json.dumps(expected(counts),indent=2)+'\n')
    run('work/layout_probes/inventory_tag_patterns.py')
    run('work/layout_probes/finalize_tag_bindings.py','--commit')
    for r in json.loads((ROOT/'work/data/layout_tag_bindings.json').read_text()):
        counts[r['language'],r['package'],r['scan']] += 1
    (ROOT/'work/data/layout_expected_matches.json').write_text(json.dumps(expected(counts),indent=2)+'\n')
    for script in ['layout_repairs.py','write_layout_exact_manifest.py','audit_layout_repair_integrity.py','reconcile_pagination_repairs.py']:
        run('work/scripts/'+script)
    actual = json.loads((ROOT/'work/data/layout_repairs_applied.json').read_text())
    assert len(actual) == proposal['expected_total_records'], (len(actual),proposal['expected_total_records'])
    proposal['status'] = 'INSTALLED_EXACT_REPLAY_AND_AUDITS_PASSED_AWAIT_SHARED_GUARDS_AND_LAST_BUILD'
    proposal['actual_total_records'] = len(actual)
    (ROOT/'work/data/layout_batch_integration_result.json').write_text(json.dumps(proposal,ensure_ascii=False,indent=2)+'\n')
    print(proposal['status'],len(actual),flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--commit',action='store_true'); args=parser.parse_args()
    staged, proposal = prepare()
    if args.commit:
        commit(staged, proposal)
