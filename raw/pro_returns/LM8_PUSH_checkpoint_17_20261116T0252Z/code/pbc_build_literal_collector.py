#!/usr/bin/env python3
"""Build a NEW literal-tail collector; never change the historical collector.

Every conjugation in the central presentation has a nonzero independent
tail, including pairs commuting in the finite quotient. This version retains
those literal conjugation words and uses the conservative n commute bound,
matching the independent standard GAP source collector's collection order.
"""
from pathlib import Path
import hashlib,json,subprocess
CODE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=CODE/'pbc_positive_collector.cpp';text=old.read_text()
needle='''    changed[i][j]=!(conjugates[i][j].size()==1 &&
     conjugates[i][j][0]==std::make_pair(i,1LL));
    if(changed[i][j])conjugates[i][j].push_back({n+tail,1});'''
assert text.count(needle)==1
text=text.replace(needle,'''    // Every formal conjugation has its own independent central tail.
    changed[i][j]=true;
    conjugates[i][j].push_back({n+tail,1});''')
text='// Literal formal-tail version; historical shortcut source remains unchanged.\n'+text
source=CODE/'pbc_literal_positive_collector.cpp';source.write_text(text)
exe=CODE/'pbc_literal_positive_collector'
cmd=['g++','-std=c++17','-O3',str(source),'-o',str(exe)]
r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0,(r.stdout,r.stderr)
(CODE/'pbc_literal_positive_collector_build.out').write_text(r.stdout+r.stderr)
report=dict(status='Built new literal version; comparison still required',
            historical_source_sha256=sha(old),literal_source_sha256=sha(source),
            executable_sha256=sha(exe),builder_sha256=sha(__file__),command=cmd,
            historical_source_unchanged=True,
            scope='Algorithm comparison pending. No source relation or target identity is inferred merely from this build.')
(CODE/'pbc_literal_positive_collector_build.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
