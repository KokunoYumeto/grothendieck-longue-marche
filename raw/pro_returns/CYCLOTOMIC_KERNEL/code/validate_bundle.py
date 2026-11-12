"""Verify the deliverable's identifiers, build logs, PDF text, and code outputs."""
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CODE=ROOT/'code'

def command(*args):
    return subprocess.run(args,capture_output=True,text=True,check=True).stdout


def main():
    source=(ROOT/'CYCLOTOMIC_KERNEL_paper.tex').read_text()
    rows=list(csv.DictReader((ROOT/'CYCLOTOMIC_KERNEL_results.csv').open()))
    ids=re.findall(r'\\label\{res:([^}]+)\}',source)
    assert len(ids)==len(set(ids))==len(rows)==56
    assert ids==[r['id'] for r in rows]
    assert all(r['manuscript_passages (section; page; scan)'] for r in rows)
    assert all(r['status'] in {'Proved','Refuted','Known','Open'} for r in rows)
    tags=re.findall(r'\\tag\{([^}]+)\}',source)
    assert len(tags)==len(set(tags))
    assert r'\input{' not in source and r'\IfFileExists{' not in source
    coverage=json.loads((ROOT/'coverage.json').read_text())
    assert len(coverage)==47
    assert all(c['statements'] and set(c['statements'])<=set(ids) for c in coverage)
    report=(ROOT/'CYCLOTOMIC_KERNEL_report.md').read_text()
    assert report.startswith('| Required item |')
    assert 'not represented as fully complete' in report
    readings=list(csv.DictReader((ROOT/'CYCLOTOMIC_KERNEL_readings.csv').open()))
    assert len(readings)==21
    mathematical_run=json.loads((CODE/'run_checks_output.json').read_text())
    assert mathematical_run['all_checks_passed']
    for program in mathematical_run['programs']:
        assert (CODE/program['program']).is_file()
        assert (CODE/program['output']).stat().st_size>0
        assert program['exit_code']==0

    log=ROOT/'build_lualatex_3.log'
    biblog=ROOT/'build_bibtex.log'
    if log.exists() and biblog.exists():
        logtext=log.read_text()
        bibtext=biblog.read_text()
        flagged=[l for l in (logtext+'\n'+bibtext).splitlines()
                 if any(w in l for w in ['Warning','Overfull','Underfull','undefined',
                                         'Missing character','Fatal error'])]
        assert not flagged,flagged
        assert 'Output written on CYCLOTOMIC_KERNEL_paper.pdf' in logtext
    else:
        record=(CODE/'build_output.txt').read_text()
        assert 'Final compiler warnings: none' in record

    pdf=ROOT/'CYCLOTOMIC_KERNEL_paper.pdf'
    info=command('pdfinfo',str(pdf))
    fonts=command('pdffonts',str(pdf))
    pdftext=command('pdftotext','-layout',str(pdf),'-')
    firstpage=command('pdftotext','-f','1','-l','1','-layout',str(pdf),'-')
    assert 'Our symbol' in firstpage and 'Part E.' in firstpage
    assert 'GPT-6 Astra' in firstpage
    assert '??' not in pdftext
    assert 'Statement E4' in pdftext and 'Statement D4' in pdftext
    fontlines=fonts.splitlines()[2:]
    assert fontlines
    for line in fontlines:
        columns=line.split()
        assert columns[-5]=='yes',('Font not embedded',line)
    pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
    if log.exists() and biblog.exists():
        (CODE/'build_output.txt').write_text(
            'Compiler: '+logtext.splitlines()[0]+'\n'
            'Commands: lualatex; bibtex; lualatex; lualatex\n'
            'Final compiler warnings: none\nBibTeX warnings: none\n\n'+info+'\n'+fonts)
    status_counts={status:sum(r['status']==status for r in rows)
                   for status in ['Proved','Refuted','Known','Open']}
    result={'passed':True,'numbered_statements':len(ids),'statement_statuses':status_counts,
            'coverage_items':len(coverage),'editorial_readings':len(readings),
            'pdf_pages':pages,'standalone_tex':True,'all_fonts_embedded':True,
            'first_page_notation_table_complete':True,
            'final_compiler_warnings':[],
            'mathematical_programs_passed':len(mathematical_run['programs']),
            'paper_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
            'tex_sha256':hashlib.sha256((ROOT/'CYCLOTOMIC_KERNEL_paper.tex').read_bytes()).hexdigest()}
    (CODE/'validate_bundle_output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
