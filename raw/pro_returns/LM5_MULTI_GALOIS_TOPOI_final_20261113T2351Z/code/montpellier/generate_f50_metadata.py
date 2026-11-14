from pathlib import Path
import csv,re

base=Path(__file__).resolve().parents[1]
headers=['id','statement','status','where_proved','depends_on',
         'manuscript_passages (section; folio; scan)',
         'depends_on_doubtful_reading (scan, alternatives)','notes']
row=['F.50',
     'Every subfield of a finitely generated extension of Qab satisfies pinned etale reconstruction after universal-homeomorphism localization.',
     'Proved','F50.tex, F.50',
     'F.46-F.47; Tsujimura2022 Proposition1.2(ii) and4.9; Tsujimura2020 Theorem3.1; AmorosoZannier2000 Theorem1.1; Stacks037J,037Q,00TP; CHW2024 Theorem4.18',
     'MPL149; section2; folio25v; scan52; intermediate-base reconstruction',
     'None',
     'All finite constant extensions stay inside finitely generated ambient fields. Free multiplicative quotients via divisors; explicit arithmetic-model CRT; uniform finite-etale division sections; and the high-degree argument with transcendental coefficients are fully proved. Independently audited by root, foundations and spheres.']
with (base/'F50_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(headers);w.writerow(row)

main=base/'references.bib'
blocks=re.split(r'(?m)(?=^@\w+\{)',main.read_text())
keys={'StacksFGConstants','StacksSmoothSpread'}
separate=[];retained=[]
for block in blocks:
    m=re.match(r'@\w+\{([^,]+),',block)
    (separate if m and m.group(1) in keys else retained).append(block)
if separate:
    (base/'F50_references.bib').write_text(''.join(separate))
    main.write_text(''.join(retained))
assert set(re.findall(r'(?m)^@\w+\{([^,]+),',(base/'F50_references.bib').read_text()))==keys
print('F50_results.csv: one exact-schema Proved row.')
print('F50_references.bib: two additional verified source entries, separate from main bibliography.')
print('F.50 is deliberately not appended to F_assembled.tex; the parent merges F.48-F.50 separately.')
