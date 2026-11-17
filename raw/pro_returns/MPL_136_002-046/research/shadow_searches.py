"""Research-only context search ledger; never writes manuscript files."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
CONTEXT=ROOT.parent/'context'
FILES=[CONTEXT/'notes/RESULTS_STATE.md', CONTEXT/'hua_project/136.modern.tex']+sorted((CONTEXT/'same_cote_136').glob('*_notes.md'))
QUERIES={
 'SH01':r'Lucas|Kummer|aucune retenue|no.carry|coefficient argument|coefficient-uniform',
 'SH02':r'lemme 2|tous les.*égaux|x_N|x_\{N\+1\}|sparse|N.?=.?.?2',
 'SH03':r'binomial.constant|degree.zero binomial|prime.local|Ouf|localise en chaque',
 'SH04':r'hom.family.constant|fully faithful|pleinement fidèle|finite.tail full',
 'SH05':r'Bijectivit|bijection|sous.ens|systèmes|familles',
 'SH06':r'tensoriel est sur|otimes_S|H05|scan.?023',
 'SH07':r'engendr|principal|S\^\{\+\(N\)\}|augmentation ideal|I/I\^2',
 'SH08':r'pi_N|adjoint à droite|right adjoint|equalizer',
 'SH09':r'troncature.*elle.même|d.autant plus gross|truncation|q_\{N',
 'SH10':r'nonnegative|degrés.*geq.?.?0|all.Z.graded|negative components',
 'SH11':r'chaîne d.adjoints|suite de quatre|inclusion.*adjoint|i_N.*dashv|adjunction ladder',
 'SH12':r'elementwise|extension.closed|I/I\^2|negligible classes|g1034|g1035|encore une',
 'SH13':r'infinite quotient|g1080|localizing Serre|varphi_\{0|varphi_.*infty|N71',
 'SH14':r'136-shadow-full-faithfulness|nonnegative unit|isomorphisme en degrés|negative components|Laurent',
 'SH15':r'Ext.*vanish|higher vanishing|exact left adjoint|g1041|corollaire annoncé|annonce encore un corollaire',
 'SH16':r'binomial.shadow.existsUnique|weighted rigidity|Le théorème sur|stronger unit',
 'SH17':r'Bézout|gcd 1|premiers entre eux|span.choose.eq.top',
 'SH18':r'c_\{k,k-i\}|c_\{i,k-i\}|ces deux coefficients|binomial coefficient',
 'SH19':r'localisé|localise|localization at every|mathbb\{Z\}_\{\(p\)\}',
 'SH20':r'Lemme 1\.1|quotients|quotient de|divisibilité|withdrawn',
 'SH21':r'présentation plus simple|cofinal|p\^r - 1|p\^\{r\+1\} - 1|not.dvd.choose.pow',
 'SH22':r'unités|tous nuls|c_\{i,k-i\}|weighted rigidity',
 'SH23':r'barrée de longs|retenues|Lemme 2|lemme commun|aucune retenue',
 'SH24':r'compatible avec multiplication|compatible à la multiplication|monoidal|g1048|weighted products',
 'SH25':r"V,Y|v,s|développe|coefficient-uniform|w'",
}

source_lines={str(p):p.read_text(encoding='utf-8').splitlines() for p in FILES}
def metadata(path,line_number):
    lines=source_lines[path]
    section=''
    source=''
    for idx in range(line_number-1,-1,-1):
        line=lines[idx]
        if line.startswith('#') or re.match(r'\\(?:sub)*section\*?\{',line):
            section=line
            for candidate in lines[idx+1:min(len(lines),idx+8)]:
                if candidate.startswith('**Source:') or candidate.startswith('**Cote'):
                    source=candidate
                    break
            break
    return section,source

ledger={
 'scope':'Supplied extracted context only, searched after the root recorded transcription freeze. No scans viewed and no transcription changed.',
 'selection':'All matches were counted. At most 12 representative hits per note are retained, prioritizing the relevant shadow sections, then Results State. This is a bounded hit ledger, not a claim of exhaustive semantic coverage.',
 'sources':[{ 'file':str(p.relative_to(CONTEXT)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in FILES],
 'notes':[]
}
for ident,pattern in QUERIES.items():
    result=subprocess.run(['rg','--no-heading','--line-number','--ignore-case','--color','never',pattern,*map(str,FILES)],text=True,capture_output=True)
    if result.returncode not in (0,1):
        raise RuntimeError(result.stderr)
    hits=[]
    counts={}
    for raw in result.stdout.splitlines():
        path,line,text=raw.split(':',2)
        line=int(line)
        relative=str(Path(path).relative_to(CONTEXT))
        counts[relative]=counts.get(relative,0)+1
        section,source=metadata(path,line)
        score=0
        if relative=='hua_project/136.modern.tex' and (580<=line<=751 or 1780<=line<=1993): score=3
        if relative=='same_cote_136/MPL_136_235-281_notes.md' and (172<=line<=386 or 644<=line<=672): score=3
        if relative=='notes/RESULTS_STATE.md': score=2
        hits.append({'file':relative,'line':line,'section':section,'manuscript_source_as_given':source,'hit':text[:400],'hit_truncated':len(text)>400,'_priority':score})
    selected=sorted(hits,key=lambda h:(-h['_priority'],h['file'],h['line']))[:12]
    for hit in selected: hit.pop('_priority')
    ledger['notes'].append({'id':ident,'pattern':pattern,'total_matching_lines':len(hits),'counts_by_file':counts,'selected_hits':selected})

out=ROOT/'research'
out.mkdir(exist_ok=True)
(out/'shadow_searches.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=['# Shadow research: supplied-context search ledger','',ledger['scope'],'',ledger['selection'],'','All note identifiers correspond to `shadow_notes_draft.md`; full patterns, source hashes, per-file counts, and bounded excerpts are in `shadow_searches.json`.','']
for note in ledger['notes']:
    md += [f"## {note['id']}",'',f"Pattern: `{note['pattern']}`",'',f"Matching lines: {note['total_matching_lines']}; files: "+'; '.join(f"{key} ({value})" for key,value in note['counts_by_file'].items())+'.','']
    for hit in note['selected_hits'][:5]:
        md.append(f"- `{hit['file']}`:{hit['line']} — {hit['section']} — {hit['hit'].strip()[:220]}")
    md.append('')
(out/'shadow_searches.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(f"Saved{len(QUERIES)} per-note supplied-context searches; total matching lines:",sum(n['total_matching_lines'] for n in ledger['notes']))
