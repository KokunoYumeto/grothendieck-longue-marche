"""Rebuild supporting registers from the final pre-context page fragments.
No OCR, image reading, contextual correction, or reading inference occurs here.
This script never rewrites a page file or the combined transcription.
"""
from pathlib import Path
import re,csv,json
ROOT=Path(__file__).resolve().parents[1]
PAGES=sorted((ROOT/'pages').glob('*.tex'))

def commands(s,names):
    out=[]
    for m in re.finditer(r'\\('+'|'.join(names)+r')\s*\{',s):
        start=m.end();depth=1;i=start
        while i<len(s) and depth:
            if s[i]=='\\':
                j=i
                while j<len(s) and s[j]=='\\':j+=1
                if (j-i)%2 and j<len(s) and s[j] in '{}':i=j+1;continue
                i=j;continue
            if s[i]=='{':depth+=1
            if s[i]=='}':depth-=1
            i+=1
        if depth:raise ValueError(f'Unbalanced {m.group(1)} at {m.start()}')
        out.append(dict(name=m.group(1),start=m.start(),end=i,body=s[start:i-1],line=s.count('\n',0,m.start())+1))
    return out

def compact(s,n=200):
    s=re.sub(r'%[^\n]*','',s)
    s=re.sub(r'\\(?:scanpage|cotefile|mspage)\{[^}]*\}','',s)
    return re.sub(r'\s+',' ',s).strip()[:n]

def cell(s):return str(s).replace('|','&#124;').replace('\n',' ').replace('<','&lt;').replace('>','&gt;')

def confidence(scan,c):
    if c['name']=='illegible':return 'low'
    b=c['body']
    if scan in [59,67,68,70,72,75,76,77,79,81,82,89,93,95]:return 'low'
    if len(b)>36 or (' ' in b and scan not in [61,62,63,64,65,66,74,78,96]):return 'low'
    return 'medium'

all_doubts=[];inventory=[]
kind={'deleted':'deletion','inserted':'insertion','margin':'margin note','diagram':'diagram','figure':'drawing'}
for p in PAGES:
    scan=int(re.search(r'scan(\d+)',p.name).group(1));s=p.read_text()
    typ='cover' if scan==81 else 'reused_typed' if scan>=82 else 'text'
    events=[]
    for c in commands(s,list(kind)):
        events.append((c['start'],c['end'],kind[c['name']],c['body'],c['line']))
    for m in re.finditer(r'\\\[([\s\S]*?)\\\]',s):
        events.append((m.start(),m.end(),'display',m.group(1),s.count('\n',0,m.start())+1))
    # Every paragraph with live text outside whole-block markup is a text block.
    # Macro elements are enumerated separately, including nested cancellations.
    for m in re.finditer(r'(?s)(?:\A|\n\s*\n)(.*?)(?=\n\s*\n|\Z)',s):
        a,b=m.span(1);block=m.group(1)
        shadow=list(block)
        for c in commands(s,['deleted','inserted','margin','diagram','figure']):
            if a<=c['start'] and c['end']<=b:
                shadow[c['start']-a:c['end']-a]=' '*(c['end']-c['start'])
        probe=''.join(shadow)
        probe=re.sub(r'\\\[[\s\S]*?\\\]','',probe)
        probe=re.sub(r'%[^\n]*','',probe)
        probe=re.sub(r'\\(?:scanpage|cotefile|mspage)\{[^}]*\}','',probe)
        probe=re.sub(r'\\(?:par|noindent|rule)\b(?:\{[^}]*\})*','',probe)
        if re.search(r'[A-Za-zÀ-ÿ]',probe):
            events.append((a,b,'text',block,s.count('\n',0,a)+1))
    # Macro before containing text only when they have the same starting point.
    events.sort(key=lambda e:(e[0],e[1]))
    for j,e in enumerate(events,1):
        inventory.append(dict(cote=91,scan=scan,sheet_kind=typ,element=j,kind=e[2],position=f'page-fragment line {e[4]}',first_words_or_objects=compact(e[3]),transcribed='yes'))
    for c in commands(s,['unsure','illegible']):
        if c['name']=='illegible':reading=f"{c['body']} unreadable word(s)";alternatives='No secure reading after magnification; see page and audit.'
        else:
            q=c['body'].split('|');reading=q[0];alternatives=' | '.join(q[1:]) if len(q)>1 else 'No second reading securely proposed.'
        all_doubts.append(dict(file='91.pdf',scan=scan,line=c['line'],reading=reading,alternatives=alternatives,confidence=confidence(scan,c)))

original=ROOT/'records/inventory_before_final_reconciliation.csv'
if not original.exists():original.write_bytes((ROOT/'MPL_91_059-098_inventory.csv').read_bytes())
with (ROOT/'MPL_91_059-098_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']);w.writeheader();w.writerows(inventory)

parts=[(ROOT/'records/notation.md').read_text(),'## Doubt register\n\nThe table below enumerates every uncertainty or unreadable-word macro in the frozen page text. Locations are line numbers in the individual page fragment (not the combined file); they locate the corresponding manuscript passage approximately. Confidence describes the reading, not its mathematical plausibility. `low` also covers highly compressed words and overwritten phrases for which an alternative cannot responsibly be invented.\n\n| File | Scan | Approximate location | Reading | Alternatives / limitation | Confidence |\n|---|---|---|---|---|---|']
for d in all_doubts:parts.append('| '+' | '.join(cell(d[k]) for k in ['file','scan','line','reading','alternatives','confidence'])+' |')
parts.append('''
## Checked readings that remain surprising

These are additional checks, not proposed repairs.

| File | Scan | Location | Reading | Alternative deliberately not supplied | Confidence |
|---|---|---|---|---|---|
| 91.pdf | 69 | First Hom computation | `(\\mathfrak X,\\underline W(T))`, with a transposition stroke | Reading only the inferred transposed order | high |
| 91.pdf | 70 | Last line | plain X; W without superscript a | Expected Gothic X or W^a | medium |
| 91.pdf | 73 | Local factorisation chain | plain X_i | Gothic target inferred from the argument | medium |
| 91.pdf | 87 | Final partition condition | no visible word finie | Adding finiteness from later criteria | high |
| 91.pdf | 88 | Exercise 5b | pour tout z in U; pi(z) nonzero | Adding z nonzero | high |
| 91.pdf | 88 | Exercise 6b pairing | primes on both arguments | Removing one prime to give a dual-basis formula | high |
| 91.pdf | 90 / 92 | Exercise 5 / exercise 3 | sl(V) / gl(V), respectively | Making the Lie-algebra names uniform | high |
| 91.pdf | 93 | Definition and later proof | Y_beta-alpha, later Y_alpha-beta | Uniformizing the index order | high |
| 91.pdf | 94 | Norm display | first bound <1; last bound ≤1 | Equalizing the two signs | high |
| 91.pdf | 97 | Transition condition and comparison | double implication; u_ij; right arrow with tilde | Reversing indices or replacing the clear arrow by an equality | high |
| 91.pdf | 98 | Proposition 25 | base de filtre sur E | Replacing E by the expected G | high |

## Abbreviations encountered

Expansions below are editorial suggestions in this register only. They do not expand the transcription.

| Written form | Suggested expansion / meaning |
|---|---|
| tt, tte, ttes | tout, toute, toutes, according to the actual form |
| pt | point |
| ens, ens., Ens | ensemble(s); category of sets when capitalized in a formula |
| Sch, Schs, sch., schém. | schéma(s), or schématique(s), according to context |
| présch | préschéma(s) |
| loc., loc. libre, loc. fermé | localement; localement libre; localement fermé |
| qu., qu-, quasi-cpt., qu. cpt, qu compt | quasi; quasi-compact |
| qu sép, quasi-sép. | quasi-séparé |
| géom. | géométriquement / géométrique |
| aff., affines | affine(s), where abbreviated |
| ss-, ss, ss-catégorie, s.-famille | sous-, sous-catégorie, sous-famille |
| ss-jacents | sous-jacents |
| covar. | covariant(e) |
| Hom, hom | homomorphisme(s), set/functor of morphisms |
| App cons, appl. constructibles, cons | applications constructibles; constructible-set functor notation |
| isom., isom | isomorphisme |
| imm., immers. | immersion |
| morph., morphisme | morphisme where abbreviated |
| Prop., prop., prop | proposition |
| Cor., Cor, cor. | corollaire |
| Th., th. | théorème |
| Pb | problème |
| N.B. | nota bene |
| i.e. | id est / c'est-à-dire |
| p. ex. | par exemple |
| resp. | respectivement |
| cf. | confer / voir |
| etc | et cetera; retained only where written |
| hyp. | hypothèse |
| tq. | tel que |
| ssi | si et seulement si |
| il faut et s. | il faut et il suffit |
| génér. | générateur(s) |
| coeffs. | coefficients |
| syst., syst. fond. | système, système fondamental |
| pet. fam. | petite famille (only an alternative reading on 82) |
| nb | nombre |
| noeth. | noethérien(ne) |
| rec. | recouvrement |
| quelc. | quelconque |
| ouv. | ouverte (cancelled on 78) |
| constr. | constructible(s) |
| prés. finie | présentation finie (uncertain cancelled reading on 95) |
| lim. | limite(s) |
| ét. | étale |
| Esp. vect. top. | espace vectoriel topologique |
| fini / finie in abbreviations | finite; ending is not standardized |
| comp. connexes | composantes connexes |
| mb | membre |
| chgt. | changement |
| ch. | unresolved abbreviation on 59; possibly champ/changement, no confident expansion |
| fais. / faisc. | faisceau(x), tentative on 67 / cancelled on 65 |
| comm. | commutatif / commutative |
| alg. | algèbre / algébrique; category suffix when used in Hom |
| Alg. | reference to Algèbre in the printed report |
| Chap., chap. | chapitre |
| exerc. | exercice |
| éd. | édition |
| mod. | modulo |
| pl. fid. | pleinement fidèle |
| inv. | inverse(s) |
| Évidem. | évidemment, tentative on 91 |
| cqf | likely cqfd / ce qu'il fallait démontrer; the final d was not supplied |
| n°, nᵒˢ | numéro, numéros |
| E.V.T. | Espaces vectoriels topologiques (suggested title abbreviation in the printed text) |
| l.c.q. / l.c.p. | unresolved abbreviation after Notons on 89; no responsible expansion |
| bis-bis / bis-idem | uncertain repetition shorthand on 71, not expanded |
| M with an overbar; = in prose | shorthand for même / même chose, depending on the phrase |

## Legibility and limits of trust

The typed faces are substantially more legible than the handwriting, but include torn edges, incomplete continuations and literal apparent errors. The handwritten main arguments are usually readable; dense cancellations, tiny additions, compressed word endings and sloping marginal notes are much less secure. The least trustworthy passages are the opening and final sentences of 59; cancelled text on 61–62; compressed wording on 67–68; the final expression on 70; the overwritten opening and third indices on 71–72; the boxed note on 75; the n(s) note and deleted text on 76; the clipped footnote on 77; the Greenberg margin on 79; the cancelled title on 81; the opening of 82; the boxed qualification on 84; and the heavily revised/angled text on 89, 93 and 95.

Every supplied whole image and both supplied halves were inspected in the first pass. All 38 retained pages were reread in the audit, with further crops, rotations or magnification for difficult passages. No OCR was used, and no page was delegated. Seven `\\illegible` occurrences (ten estimated words in total) remain where the ink is obliterated or clipped after magnification; mathematical symbols instead receive tentative readings. The seven occurrences include the clipped final footnote on 77; their counts are estimates, not inferred missing sentences.

Drawings, boxes and connecting strokes are TikZ reconstructions. Their shape and relative arrangement are approximate, especially the overlapping cancelled arrows on 89 and the long marginal connection on 93; they should not be mistaken for facsimiles. Display spacing follows typesetting needs, and line breaks within prose paragraphs need not match the scan. The final inventory locates each text paragraph, displayed formula and markup element by its individual-fragment line, including nested insertions/deletions.

`records/doubts.jsonl`, `records/precontext_observations.md` and the earlier inventory are working history. They are superseded where this register or `records/visual_audit.md` records a changed reading. In particular, early guesses at reverse-side typewriting on 82 were removed once the actual printed face on 83 was read; printed material is transcribed once, on its supplied printed face. Those earlier guesses must not be treated as a second transcription.
''')
(ROOT/'MPL_91_059-098_doubts.md').write_text('\n'.join(parts))
(ROOT/'records/final_doubts.json').write_text(json.dumps(all_doubts,ensure_ascii=False,indent=2)+'\n')
print(f'{len(PAGES)} pages; {len(inventory)} inventory elements; {len(all_doubts)} uncertainty entries')
