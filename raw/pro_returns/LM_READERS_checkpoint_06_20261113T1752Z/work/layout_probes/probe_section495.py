"""Extend the existing section49 reservation; keep source dependencies frozen."""
from pathlib import Path
import copy, hashlib, inspect, json, re, subprocess, sys
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, editorial, mechanical_repairs, layout_repairs, fitz
from instrument_marks import deinstrument
from texenv import environment

D = Path('work/layout_probes')
PACKAGE = 'LM_C3-492-510'
OLD = r'\Needspace{6\baselineskip}'
NEW = r'\Needspace{18\baselineskip}'
OLD_MATCH = r"reservation=re.search(r'(\\Needspace\{6\\baselineskip\})\s*$',scan_text)"
NEW_MATCH = r"reservation=re.search(r'(\\Needspace\{(?:6|18)\\baselineskip\})\s*$',scan_text)"
jobs = []; candidates = []; deferrals = []; semantic = []

for lang in ('fr', 'en'):
    raw = build_readers.raw_package(PACKAGE, lang)
    text, mechanical = mechanical_repairs.repair(raw, PACKAGE, lang)
    text, layout = layout_repairs.repair(text, PACKAGE, lang)
    record = next(r for r in layout if r['id'] == '140-3-495-N1')
    assert record['new'].count(OLD) == text.count(OLD) == 1
    newtext = text.replace(OLD, NEW)
    newrecord = copy.deepcopy(record)
    newrecord.update(previous_new=record['new'], new=record['new'].replace(OLD, NEW),
        reason='Before scan495, extend the existing reservation from six to eighteen baselines so section49, its unchanged marginal notes, the first I) paragraph and display1 remain together. The assembler defers the reservation past scan494 apparatus and retained-doubt matter. No source wording, note, or mathematical notation changes.')
    path = Path('sources') / record['source_path']
    newrecord['source_file_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    candidates.append(newrecord)

    annotations = []
    for source in (text, newtext):
        annotations.append(editorial.annotate(source, PACKAGE, lang))
    fields = ('id','kind','manuscript','corrected','corrected_tex','math_mode','inherited_doubt')
    projections = [[{k:e.get(k) for k in fields} for e in obj[1]] for obj in annotations]
    assert projections[0] == projections[1]
    semantic.append(dict(language=lang, variants=len(projections[0]), exact_variant_projection=True,
                         source_change_only=OLD+' -> '+NEW))

    # Exercise the actual assembler function in private globals and a probe-only
    # output directory. No cache, source-mark, or manuscript artifact is touched.
    fn = inspect.getsource(build_readers.assemble_language)
    assert fn.count(OLD_MATCH) == 1
    namespace = dict(vars(build_readers))
    private_work = D / 'section495_assembly_check'
    private_work.mkdir(exist_ok=True)
    ann, entries, meta = annotations[1]
    probe_layout = [newrecord if r['id']=='140-3-495-N1' else r for r in layout]
    namespace.update(WORK=private_work,
        package_data=lambda package, language, stage, ann=ann, entries=entries, meta=meta, probe_layout=probe_layout:
            (ann, entries, meta, {'package':PACKAGE, 'language':lang, 'layout':probe_layout}))
    exec(fn.replace(OLD_MATCH, NEW_MATCH), namespace)
    assembled, *_ = namespace['assemble_language'](lang, 'probe', {PACKAGE})
    plain = deinstrument(assembled)
    if isinstance(plain, tuple): plain = plain[0]
    previous = plain.index(r'\scanpage{494}')
    target = plain.index(r'\scanpage{495}')
    between = plain[previous:target]
    assert between.count(NEW) == 1 and between.rstrip().endswith(NEW)
    assert between.index(r'\end{LMapparatus}') < between.index(NEW)
    assert between.index(r'\LMcarryover') < between.index(NEW)
    assert OLD not in between
    deferrals.append(dict(language=lang, status='PASS',
        exactly_one_reservation=True, after_preceding_apparatus=True,
        after_preceding_retained_doubts=True, directly_before_scan495=True))

    start = text.index(OLD)
    end = text.index(r'\]', start) + 2
    opening = text[start:end]
    for variant, source in [('before', opening), ('after', opening.replace(OLD, NEW))]:
        body, entries, _ = editorial.annotate(source, PACKAGE, lang)
        parts = [build_readers.preamble(lang, 1), r'\begin{document}\LMcote{140-3}']
        fixtures = []
        for form in (0,1,2):
            for spare in (90,170,260):
                ident = f'{lang}-{form}-{spare}'
                fixtures.append(dict(id=ident, language=lang, form=form, spare=spare))
                parts += [rf'\clearpage\LMform={form}\noindent Fixture {ident}.\par',
                          rf'\vspace*{{\dimexpr\textheight-{spare}pt-\baselineskip\relax}}',
                          body, r'\par\noindent End of opening definition.\par']
        parts += [r'\end{document}']
        target = D / f'section495_{variant}_{lang}.tex'
        target.write_text('\n'.join(parts))
        proc = subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],
                                cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        jobs.append((lang,variant,target,fixtures,proc))

candidate = dict(records=candidates,
    generator_patch=dict(path='work/scripts/build_readers.py', old=OLD_MATCH, new=NEW_MATCH,
        scope='Existing LM_C3-492-510 scan494 non-baseline deferral only.',
        reason='Recognize the extended eighteen-baseline reservation while retaining compatibility with the historical six-baseline record; place either after all generated preceding-scan matter.'),
    assembler_deferral_checks=deferrals, semantic_checks=semantic)
(D/'section495_candidate.json').write_text(json.dumps(candidate,ensure_ascii=False,indent=2)+'\n')

proof = []
for lang,variant,target,fixtures,proc in jobs:
    stdout,_ = proc.communicate(); target.with_suffix('.console.txt').write_text(stdout)
    log=target.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=proc.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'))
    print(lang,variant,counts,flush=True)
    assert counts==dict(exit=0,overfull=0,missing=0)
    doc=fitz.open(target.with_suffix('.pdf'));texts=[p.get_text() for p in doc]
    for fixture in fixtures:
        first=next(i for i,t in enumerate(texts) if f"Fixture {fixture['id']}." in t)
        last=next(i for i in range(first,len(doc)) if 'End of opening definition.' in texts[i])
        heading='Homomorphismes de' if lang=='fr' else 'Homomorphisms of'
        opener='I) Considérons' if lang=='fr' else 'I) Consider'
        note='préliminaire' if lang=='fr' else 'preliminary'
        hp=[i for i in range(first,last+1) if heading in texts[i]]
        ip=[i for i in range(first,last+1) if opener in texts[i]]
        np=[i for i in range(first,last+1) if note in texts[i]]
        dp=[i for i in range(first,last+1) if '(1)' in texts[i]]
        assert all(len(x)==1 for x in (hp,ip,np,dp)),(fixture,hp,ip,np,dp)
        page=doc[hp[0]]
        hs=page.search_for(heading);y=min(r.y0 for r in hs)
        clip=fitz.Rect(50,max(0,y-25),590,min(page.rect.height,y+300))
        image=D/f"section495_{variant}_{fixture['id']}.png"
        page.get_pixmap(matrix=fitz.Matrix(2,2),clip=clip).save(image)
        proof.append(dict(**fixture,variant=variant,compile=counts,
            heading_page=hp[0]+1,note_page=np[0]+1,opener_page=ip[0]+1,definition_page=dp[0]+1,
            attached=hp==ip==np==dp,image=image.as_posix(),
            image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(),status='PENDING_VISUAL'))
after=[p for p in proof if p['variant']=='after']
assert all(p['attached'] for p in after),[p for p in after if not p['attached']]
(D/'section495_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL',
    assembler_deferral_checks=deferrals,semantic_checks=semantic,probes=proof),ensure_ascii=False,indent=2)+'\n')
print('After attachments',sum(p['attached'] for p in after),'/',len(after),flush=True)
