"""Replay and token-count checks for the explicit local layout patch set.

Command counts complement, rather than replace, source-local mathematical and
visual review. Raw source offsets always refer to the immutable ZIP contents.
"""
from pathlib import Path
from collections import Counter
from hashlib import sha256
import re,json
import layout_repairs
import audit_layout_sizes
ROOT=Path(__file__).resolve().parents[2]
ALLOW=set('LMlayoutnotice LMmathnotice LMnotelabel LMpagefigure LMpairedmargins Needspace baselineskip par nobreak allowbreak arraycolsep begin diagram end enspace fontsize footnotesize noindent parbox qquad quad rule scalebox selectfont shortstack text textit'.split())
MARKS='scanpage mspage unsure illegible deleted inserted margin'.split()
def commands(t):
 # The source-local cancelled-tag wrapper has the same semantic tag argument.
 t=t.replace(r'\LMcancelledtag',r'\tag')
 return Counter(x for x in re.findall(r'\\([A-Za-z@]+)',t) if x not in ALLOW)
def main():
 results=[];records=[];paired={lang:set() for lang in ['fr','en']}
 for lang,folder,suffix in [('fr','fr/texts',''),('en','en/packages','_en')]:
  for package in layout_repairs.COVERAGE:
   path=ROOT/'sources'/folder/(package+suffix+'.tex');raw_bytes=path.read_bytes();raw=raw_bytes.decode('utf-8');initial=path.read_text();final,local=layout_repairs.repair(initial,package,lang)
   before,after=commands(initial),commands(final)
   differences={k:after[k]-before[k] for k in before.keys()|after.keys() if after[k]!=before[k]}
   assert not differences,(lang,package,differences)
   mark_counts={k:len(re.findall(r'\\'+k+r'\b',initial)) for k in MARKS}
   assert mark_counts=={k:len(re.findall(r'\\'+k+r'\b',final)) for k in MARKS},(lang,package,'marks')
   for r in local:
    assert raw[r['source_offset_start']:r['source_offset_end']]==r['source_old'],r['id']
    assert raw_bytes[r['source_byte_start']:r['source_byte_end']].decode('utf-8')==r['source_old'],r['id']
    assert r['expected_match_count']==1,r['id'];paired[lang].add(r['id'])
   records+=local
   results.append(dict(language=lang,package=package,source_sha256=sha256(raw_bytes).hexdigest(),semantic_command_count_differences=differences,source_mark_counts=mark_counts,local_changes=len(local),source_character_and_byte_offsets_valid=True))
 assert paired['fr']==paired['en'],paired['fr']^paired['en']
 obj=dict(description='Counts of named TeX commands except the explicit layout-only allowlist, before and after local layout repair; this complements exact patch replay and human mathematical review and is not a proof of mathematical equivalence.',layout_only_allowlist=sorted(ALLOW),package_language_pairs=len(results),total_local_changes=len(records),paired_stable_ids_equal=True,all_source_marks_preserved=True,all_raw_source_offsets_valid=True,results=results)
 obj['presentation_command_projection']={'LMcancelledtag':'tag','reason':'The exact source-local wrapper preserves the original equation-tag argument; its form-dependent parentheses are presentation only.'}
 obj['local_size_gate']=audit_layout_sizes.audit(records)
 (ROOT/'work/data/layout_semantic_command_audit.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
 print(len(results),'package-language inputs;',len(records),'local records; all named mathematical commands, source marks and raw source offsets preserved')
if __name__=='__main__':main()
