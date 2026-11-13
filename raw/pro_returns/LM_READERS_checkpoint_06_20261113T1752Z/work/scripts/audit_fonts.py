r"""Inventory source bold-Gamma commands whose rendering requires repair.

Source commands are unchanged. The edition implements boldsymbol through the
configured Unicode math alphabet so requested bold Greek is not silently
substituted by a regular glyph. No unrelated mathematical notation is changed.
"""
import csv,json,re,collections
from pathlib import Path
import editorial

REASON=("The source explicitly requests a bold Gamma. The amsbsy mathversion-based implementation falls back to the regular configured math font; the original probe renders both Gamma and boldsymbol{Gamma} as U+0393. The Unicode math alphabet symbf selects the font's actual bold upright Gamma U+1D6AA, preserving orientation and restoring the requested weight. The source command and reading remain unchanged.")

def inventory():
    with Path('sources/fr/records/CURRENT_TEXT_INDEX.tsv').open() as f:index=list(csv.DictReader(f,delimiter='\t'))
    rows=[]
    for lang in ('fr','en'):
        for item in index:
            package=item['package'];source=('fr/texts/'+package+'.tex' if lang=='fr' else 'en/packages/'+package+'_en.tex')
            text=(Path('sources')/source).read_text();mask=editorial.blank_comments(text);seq=collections.Counter()
            for m in re.finditer(r'\\boldsymbol\s*\{',mask):
                end=editorial.brace_end(text,m.end()-1);argument=text[m.end():end-1]
                if argument!=r'\Gamma':raise ValueError('An additional boldsymbol argument requires explicit review')
                scan=editorial.at_scan(text,m.start());seq[scan]+=1
                rows.append({'id':f"FONT-{lang.upper()}-{item['cote']}-s{scan:03d}-B{seq[scan]:03d}",
                             'language':lang,'package':package,'cote':item['cote'],'scan':scan,
                             'source_path':source,'source_line':text.count('\n',0,m.start())+1,
                             'command':text[m.start():end],'source_argument':argument,
                             'rendering_implementation':r'\symbf{#1}',
                             'kind':'restore requested bold mathematical glyph','reason':REASON})
    return rows

def main():
    rows=inventory();counts=dict(collections.Counter(r['language'] for r in rows))
    assert counts=={'fr':65,'en':65},counts
    out={'source_sites':len(rows),'source_sites_by_language':counts,
         'implementation':r'\renewcommand\boldsymbol[1]{\symbf{#1}}',
         'source_commands_changed':False,
         'probe':{'ordinary_Gamma':'U+0393','existing_boldsymbol_Gamma':'U+0393',
                  'symbf_Gamma':'U+1D6AA','symbfup_Gamma':'U+1D6AA',
                  'font':'Latin Modern Math','compile_exit_code':0,
                  'source_confirmation':'fr/texts/LM_P032.tex, cote 140-2, scan 314, line 46: the author explicitly distinguishes the bold letter.'},
         'records':rows}
    Path('work/data/font_repairs.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    fields=['id','language','package','cote','scan','source_path','source_line','command','source_argument','rendering_implementation','kind','reason']
    editorial.write_tsv(Path('work/records/FONT_REPAIRS.tsv'),fields,rows)
    print(json.dumps({'source_sites':len(rows),'by_language':counts,'source_commands_changed':False},indent=2))

if __name__=='__main__':main()
