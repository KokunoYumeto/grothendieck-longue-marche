"""Prepare34's scheduled capture and read-only preconditions; never capture."""
from pathlib import Path
from hashlib import sha256
import difflib
import json
import re

root=Path(__file__).resolve().parents[1]
replacements={'33':'34','32':'33','31':'32','354':'362','310':'318','115':'116',
              '9680':'10053','132920':'142600','142600':'152653','494718836':'508499680'}
pattern=r'(?<!\d)('+'|'.join(sorted(replacements,key=len,reverse=True))+r')(?!\d)'
rows=[];diffs=[]
for old_name,new_name in [('check_checkpoint33_preconditions.py','check_checkpoint34_preconditions.py'),
                          ('capture_checkpoint33.py','capture_checkpoint34.py')]:
    source=root/'code'/old_name;target=root/'code'/new_name
    assert not target.exists()
    before=source.read_text()
    after=re.sub(pattern,lambda m:replacements[m.group(0)],before)
    after=after.replace('67ad6a36bef8bc98dbf3a6db7426065765022ca95d18434e6bde60d56c24f2c0',
                        '5c68edb5a023c97cb400b506f7e1b7303f19e3cac9212947491e47793d77ef96')
    if new_name.startswith('check_'):
        after=after.replace('range(103,106)','range(106,112)').replace('range(161,165)','range(165,167)')
        after=after.replace('thirty_third_hour_research_report','thirty_fourth_hour_research_report')
    else:
        after=after.replace('datetime(2026,11,17,11,49,30','datetime(2026,11,17,12,49,30')
        # The next-due line originally contains12; change that exact assignment only.
        after=after.replace('next_due=datetime(2026,11,17,12,49,30','next_due=datetime(2026,11,17,13,49,30')
        after=after.replace('Thirty-third','Thirty-fourth').replace('thirty-third','thirty-fourth')
        after=after.replace('thirty_third_hour_research_report','thirty_fourth_hour_research_report')
        after=after.replace('All seven new formal sources','All eight new formal sources')
        after=after.replace('actual mains/CM Open','actual mains/CM Open')
        after=after.replace('2026-11-17 12:49:30 UTC','2026-11-17 13:49:30 UTC')
        old="Actual full-GT signed congruence hexagon gate closed and original CM frame criterion proved; both main problems and actual CM parity remain open."
        new="Actual first central congruence hexagon and modular conjugacy, quotient factor transporter, cyclic and coherent frame obstructions, and entire deletion/filling cohomology spaces proved; both main problems and actual CM parity remain open."
        assert old in after;after=after.replace(old,new)
        old='The full-GT signed congruence hexagon image vanishes in every modulus.\nThe original CM comparison is reduced to the stated actual r-frame sign;\nit does not assert that this sign condition holds. The unfilled source\ndouble, its exact topology and cohomology, and the complete contact-image\ncriterion retain their distinct scopes.'
        new='The same marked hexagon vanishes in the first relative-central congruence\nquotient. The relative-central pure tower and first modular quotient have\ntheir actual automorphisms and conjugacies. Quotient factor frames exist,\nbut arbitrary frame choices do not define the original character. The\nentire derived cyclic cohomology and coherent involution class retain\nthe original CM sign without deciding it. The entire deletion and filling\ncohomology spaces retain the unresolved exact contact subspace equality.'
        assert old in after;after=after.replace(old,new)
    compile(after,str(target),'exec')
    with target.open('x') as stream:stream.write(after)
    rows.append(dict(source=str(source.relative_to(root)),source_sha256=sha256(before.encode()).hexdigest(),
                     target=str(target.relative_to(root)),target_sha256=sha256(after.encode()).hexdigest()))
    diffs.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=old_name,tofile=new_name))
with (root/'records/checkpoint34_capture_helper_adaptation.json').open('x') as stream:
    json.dump(dict(capture_executed=False,archive_created=False,helpers=rows),stream,indent=2);stream.write('\n')
with (root/'records/checkpoint34_capture_helper_adaptation.diff').open('x') as stream:stream.writelines(diffs)
print(json.dumps(rows,indent=2))
