from pathlib import Path
from datetime import datetime,timezone
import json,re
P=Path('/workspace/scratch/4770596940a0')
f=P/'out/readers/R3/scan030.tex';s=f.read_text()
a=s.index('% @ lower right, note on uniqueness')
b=s.index('% @ lower part, corollary',a)
new=r'''% @ lower right, note on uniqueness; its left separator is drawn
\margin{\figure{\begin{tikzpicture}
\node[anchor=north west,inner sep=0pt,text width=2.1cm] (uni) at (0,0) {\begin{minipage}{2.1cm}
Un peu vif, on trouve par $F'.G=G'$ un $G'$ tel que
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
 F'\arrow[r,phantom,"\preceq" description] \arrow[d,phantom,"\rotatebox{90}{$\leq$}" description]\& F\arrow[d,phantom,"\rotatebox{90}{$\leq$}" description]\\
 G'\arrow[r,phantom,"\preceq" description]\& G
\end{tikzcd}}
mais il faut vérifier encore l'\uline{unicité}
\end{minipage}};
\draw ([xshift=-2pt]uni.north west) -- ([xshift=-2pt]uni.south west);
\end{tikzpicture}}}
% @ lower right, second note; stepped left separator follows the two text portions
\margin{\figure{\begin{tikzpicture}
\node[anchor=north west,inner sep=0pt,text width=2.1cm] (intro) at (0,0) {Cela amène à dégager};
\node[anchor=north west,inner sep=0pt,text width=2.1cm] (prem) at (intro.south west) {\begin{minipage}{2.1cm}
a) $P\ll Q\ll R$ et $P\preceq R\Rightarrow P\preceq Q,\ Q\preceq R$\par
b) $P\ll Q\ll R$ \unsure{et} $P\leq R$
\end{minipage}};
\node[anchor=north east,inner sep=0pt,text width=1.5cm] (tail) at (prem.south east) {\begin{minipage}{1.5cm}
\deleted{$\Rightarrow P\unsure{\leq|<}$} $Q\leq R$ $\Rightarrow P\leq Q$
\end{minipage}};
\draw ([xshift=-5pt,yshift=3pt]prem.north west)
 .. controls ([xshift=-2pt,yshift=3pt]prem.north west) and ([xshift=-2pt]prem.north west)
 .. ([xshift=-2pt,yshift=-3pt]prem.north west)
 -- ([xshift=-2pt]prem.south west)
 -- ([xshift=-2pt]tail.north west)
 -- ([xshift=-2pt]tail.south west);
\end{tikzpicture}}}
'''
s=s[:a]+new+s[b:];f.write_text(s)
rpath=P/'out/readers/R3/scan030.json';r=json.loads(rpath.read_text())
for row in r['differences']:
    if row['confidence'] not in ('high','medium','low'): row['confidence']='medium'
who={'model':'inherited','effort':'inherited; not separately exposed','run':'R3 scan030'}
r['check_events']=[
 dict(statement_id='R3-030-M01',place='proof of c, final componentwise-inclusion argument',date='2026-11-19',who=who,type='targeted proof check',outcome='Conditional chain verified: assuming the cited figure-product componentwise-inclusion lemma, the stated equality of interior meanings, and downward closure of F′ in F, inclusion A′∩B′⊂A∩B gives A′⊂A and hence A′∈F′. Together with A′°∩B′°≠∅, this yields A′∩B′∈F′.G. No independent proof of the cited lemma is claimed.'),
 dict(statement_id='R3-030-M02',place='background lemma cited in proof of c: componentwise inclusion for figure products',date='2026-11-19',who=who,type='carried as background without fault found',outcome='The page explicitly refers to earlier theory of F.G. Its special lemma is used conditionally in M01; it was not independently proved on this page.'),
 dict(statement_id='R3-030-M03',place='R3 check of unrestricted-set analogue of the cited lemma',date='2026-11-19',who=who,type='refuted',refined_statement_id='R3-030-M02',outcome='Explicit finite counterexample: A={1,2}, B={1}, A′={1,3}, B′={1}. A∩B=A′∩B′={1}, yet 3∈A′ and 3∉A. Thus intersection inclusion alone does not imply componentwise inclusion for arbitrary sets; the manuscript’s special figure-product hypothesis is essential. This does not refute M02 or alter the transcription.')
]
r['notes_while_reading'] += ['Reading-only scope observation: the uniqueness note expressly leaves uniqueness to verify; the proposed C7₀ construction is followed by unproved obligations a), b), c). These are not entered as proof checks.','Top a/b, the P/Q/R margin statements and the φ⁻¹ formula were read and their symbols checked against ink, but no proof of those statements was performed.','Separator strokes are represented schematically in TikZ around the corresponding margin text; their role and relative step are preserved rather than treating the whole note as a closed rectangle.']
# Basic structural validation only, not TeX compilation.
stack=[]
for line in s.splitlines():
    line=line.split('%',1)[0]
    for i,ch in enumerate(line):
        if ch in '{}':
            n=0;j=i-1
            while j>=0 and line[j]=='\\': n+=1;j-=1
            if n%2: continue
            if ch=='{':stack.append(ch)
            else:
                assert stack,'unbalanced closing brace'
                stack.pop()
assert not stack,'unclosed brace'
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',s):
    if m[1]=='begin':envs.append(m[2])
    else:assert envs.pop()==m[2],m.group()
assert not envs
assert s.count('\\[')==s.count('\\]')
assert len(r['C_doubt_resolutions'])==18
assert sorted(x['occurrence'] for x in r['C_doubt_resolutions'])==list(range(1,19))
assert all(isinstance(x[k],bool) for x in r['differences'] for k in ('against_C','against_H','marked_in_H'))
assert all(Path(x).is_file() for x in r['images_viewed'])
assert s.count('\\begin{tikzcd}')==3
assert s.count('\\begin{tikzpicture}')==2
r['verification']='Structural validation passed: balanced braces/environments/displays, three tikz-cd diagrams and two TikZ separator wrappers; 18 distinct C doubt occurrences, all difference flags boolean and all 28 viewed-image paths exist. No compilation or later-page reading. All inventory items are present in the proposed text; layout of separator strokes is schematic.'
r['end_utc']=datetime.now(timezone.utc).isoformat()
rpath.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(r['differences']),'C_doubts':len(r['C_doubt_resolutions']),'resolved_C_doubts':sum(x['status']=='resolved' for x in r['C_doubt_resolutions']),'inventory':len(r['inventory']),'crops':len(r['crops']),'against_C':sum(x['against_C'] for x in r['differences']),'against_H':sum(x['against_H'] for x in r['differences']),'check_events':len(r['check_events']),'end_utc':r['end_utc']},ensure_ascii=False))
