#!/usr/bin/env python3
"""Typesetting-only corrections after the preserved second checkpoint08 build."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT = Path(__file__).resolve().parent.parent


def main():
    saved = ROOT/'research/checkpoint08_second_typesetting_prior_passages.json'
    assert not saved.exists()
    old,records = {},{}
    for name in ('sections/E_a6_full_agent.tex','sections/D_return_prime_agent.tex'):
        p=ROOT/name
        original=p.read_text()
        old[name]=original
        text=original
        if name.endswith('E_a6_full_agent.tex'):
            text=re.sub(r'(?<!\\)\\$',lambda m:'\\\\',text,flags=re.MULTILINE)
            text=text.replace(r'\subsection{The full $A_6$ Ferrari source, its solvable layers, and the cubic Kummer comparison}',
                              r'\subsection{The full \texorpdfstring{$A_6$}{A6} Ferrari source, its solvable layers, and the cubic Kummer comparison}')
        else:
            text=text.replace(r'\texttt{bc\_return\_prime\_model.py}',r'\texttt{bc\_return\_prime\_\allowbreak model.py}')
            text=text.replace(r'\texttt{bc\_return\_prime\_centralizers.py}',r'\texttt{bc\_return\_prime\_\allowbreak centralizers.py}')
        assert text!=original
        records[name]={'before_sha256':sha256(original.encode()).hexdigest(),
                       'after_sha256':sha256(text.encode()).hexdigest()}
        p.write_text(text)
    saved.write_text(json.dumps(old,indent=2)+'\n')
    result={'typesetting_only':True,'preserved_build':'checkpoint08_second_failure',
            'prior_passages':str(saved.relative_to(ROOT)),'files':records}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
