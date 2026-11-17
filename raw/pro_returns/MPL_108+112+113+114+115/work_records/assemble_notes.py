from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
OUT=HERE.parent/'MPL_108+112+113+114+115_notes.md'

def after(file, heading):
    s=(HERE/file).read_text()
    return heading+s.split(heading,1)[1]

def cote115():
    s=(HERE/'research_115_page_notes.md').read_text()
    s=s.replace('# Cote 115:', '## Cote 115:', 1)
    s=re.sub(r'^## (115-R\d+)', r'### \1', s, flags=re.M)
    s=re.sub(r'^\*\*Literal-cue check:\*\*[^\n]*\n\n', '', s, flags=re.M)
    s=s.replace('deliverable/', '')
    s=s.replace('`research_115_page_notes.literal_quote_validation.json`', '`work_records/research_115_page_notes.literal_quote_validation.json`')
    return s

pieces=[
    (HERE/'notes_front_matter.md').read_text(),
    (HERE/'research_root.md').read_text(),
    cote115(),
    after('research_new_strata_paths.md','## Earliest-occurrence questions'),
    after('research_bisite_115.md','## BISITE A'),
    after('research_residue_hua.md','## One row per supplied RESIDUE statement').split('## Additional comparison notes')[0],
    (HERE/'notes_sources.md').read_text(),
]
OUT.write_text('\n\n'.join(pieces))
print(OUT.name,OUT.stat().st_size,'bytes')
