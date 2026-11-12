"""Build the standalone paper and combined source audit from preserved parts.

Run assemble_ledgers.py first. No mathematical assertion is inferred here.
All statement/source links come from the authored results ledger.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / 'sections'


def tex_escape(value):
    substitutions = {'\\':r'\textbackslash{}', '&':r'\&', '%':r'\%',
                     '$':r'\$', '#':r'\#', '_':r'\_', '{':r'\{',
                     '}':r'\}', '~':r'\textasciitilde{}', '^':r'\textasciicircum{}'}
    return ''.join(substitutions.get(c,c) for c in value)


def human_passage(value):
    parts=[]
    for part in value.split(' | '):
        bits=[b.strip() for b in part.split(';')]
        if len(bits)==3 and bits[0].isdigit():
            parts.append(f'Section {bits[0]}, manuscript pp. {bits[1]}, scans {bits[2]}')
        elif len(bits)==3 and bits[0]=='LM34':
            parts.append(f'La Longue Marche, section 34, manuscript p. {bits[1]}, scan {bits[2]}')
        else:
            parts.append(part)
    return tex_escape('; '.join(parts))


def main():
    rows=list(csv.DictReader((ROOT/'CYCLOTOMIC_KERNEL_results.csv').open()))
    rows_by_id={r['id']:r for r in rows}
    inserted=[]
    included=[]

    def include(name):
        path=ROOT/name
        assert path.is_file(),f'Missing required source: {name}'
        value=path.read_text()
        labels=list(re.finditer(r'\\label\{res:([^}]+)\}',value))
        for j in reversed(range(len(labels))):
            match=labels[j]
            end=labels[j+1].start() if j+1<len(labels) else len(value)
            if r'\passage{' not in value[match.end():end]:
                ident=match.group(1)
                passage=human_passage(rows_by_id[ident]['manuscript_passages (section; page; scan)'])
                value=value[:match.end()]+'\n'+r'\passage{'+passage+'}\n'+value[match.end():]
                inserted.append(ident)
        included.append(name)
        return '\n% BEGIN '+name+'\n'+value+'\n% END '+name+'\n'

    master=(PARTS/'paper_master.tex').read_text()
    source=re.sub(r'\\IfFileExists\{([^}]+)\}\{\\input\{\1\}\}\{\}',
                  lambda m:include(m.group(1)),master)
    source=re.sub(r'\\input\{([^}]+)\}',lambda m:include(m.group(1)),source)
    assert r'\input{' not in source and r'\IfFileExists{' not in source
    labels=re.findall(r'\\label\{res:([^}]+)\}',source)
    assert len(labels)==len(set(labels))==len(rows)
    assert set(labels)==set(rows_by_id)
    (ROOT/'CYCLOTOMIC_KERNEL_paper.tex').write_text(source)

    bib_names=['A_agent_refs.bib','B_agent_refs.bib','D_agent_refs.bib','root_refs.bib']
    bib='\n\n'.join((PARTS/n).read_text().strip() for n in bib_names)+'\n'
    keys=re.findall(r'@\w+\{([^,]+),',bib)
    assert len(keys)==len(set(keys))
    cited=set()
    for match in re.finditer(r'\\(?:cite|nocite)(?:\[[^\]]*\])?\{([^}]+)\}',source):
        cited.update(k.strip() for k in match.group(1).split(','))
    assert cited<=set(keys),('Undefined bibliography keys',cited-set(keys))
    entries=re.split(r'(?=@\w+\{)',bib)
    assert all('verified' in x.lower() for x in entries if x.strip())
    (ROOT/'CYCLOTOMIC_KERNEL_references.bib').write_text(bib)

    audit=['# CYCLOTOMIC_KERNEL: source and proof audit',
           '',
           'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 12 November 2026. '
           'Verification means the stated version and specified passages were opened; '
           'it does not mean that an inaccessible publisher version was inspected. '
           'No claim of priority is made.',
           '',
           'The requested Stix publisher-text collation remains unfinished. '
           'The supplied 2008 version and the 2012 author manuscript are the versions '
           'used for mathematical content. The source records below retain that limitation.',
           '']
    for n in ['A_agent_sources.md','B_agent_sources.md','D_agent_sources.md','root_sources.md']:
        audit.extend([(PARTS/n).read_text().strip(),''])
    (ROOT/'CYCLOTOMIC_KERNEL_source_audit.md').write_text('\n'.join(audit))
    output={'standalone_source':True,'numbered_statements':len(labels),
            'bibliography_entries':len(keys),'cited_keys':len(cited),
            'undefined_citations':[], 'source_parts':included,
            'passage_annotations_added':len(inserted)}
    (ROOT/'code/prepare_paper_output.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':
    main()
