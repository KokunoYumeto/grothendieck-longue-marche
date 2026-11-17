"""Build final reading apparatus from the audited, pre-context source."""
from pathlib import Path
import re,csv,collections,shutil
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
assert 'transcription frozen' not in (ROOT/'progress.log').read_text()
PAGES=sorted((ROOT/'pages').glob('*.tex'))

def group(s,start):
    depth=1;i=start+1
    while i<len(s):
        if s[i]=='\\':
            m=re.match(r'\\(?:[A-Za-z]+|.)',s[i:]);i+=len(m.group());continue
        if s[i]=='{':depth+=1
        elif s[i]=='}':
            depth-=1
            if not depth:return s[start+1:i],i+1
        i+=1
    raise ValueError('unbalanced group')
def macros(s,names):
    for m in re.finditer(r'\\('+ '|'.join(names)+r')\s*\{',s):
        start=s.index('{',m.start());body,end=group(s,start)
        yield m.group(1),body,m.start(),end

def esc(x):return str(x).replace('|',r'\|').replace('\n',' ').replace('\r','')
def third(pos,s):
    q=pos/max(1,len(s));return 'upper third' if q<.34 else ('middle third' if q<.67 else 'lower third')
def loc(pos,s):
    nums=list(re.finditer(r'\((\d{1,2}[a-z\x27]*)\)',s[:pos]))
    near=('; after/near ('+nums[-1][1]+')') if nums else '; opening'
    return third(pos,s)+near+'; TeX line '+str(s.count('\n',0,pos)+1)

# Root's last ink-based abbreviation check, before freeze.
p=ROOT/'pages/MPL_64_078-115_64_scan106.tex';s=p.read_text()
s=s.replace(r'les v\textsuperscript{ts} de',r'les \unsure{v\textsuperscript{ts}|p\textsuperscript{ts}} de');p.write_text(s)
p=ROOT/'pages/MPL_64_078-115_64_scan080.tex';s=p.read_text()
s=s.replace(r'\wedge_{\mu_4}}',r'\wedge_{\unsure{\boldsymbol{\mu}|\mu}_4}}',1);p.write_text(s)

# Preserve the contemporaneous first-pass apparatus, then standardize final inventory.
inv=ROOT/'MPL_64_078-115_inventory.csv'
if not (ROOT/'records/inventory_working.csv').exists():shutil.copy2(inv,ROOT/'records/inventory_working.csv')
old=list(csv.DictReader((ROOT/'records/inventory_working.csv').open()))
final=[]
kindmap={'formula':'display','corollary':'text','proposition':'text','proof':'text','lemma':'text','heading':'text','annotation':'text','rule':'drawing','separator':'drawing'}
skip={'rule','separator','deletion','insertion','correction','margin','margin note','diagram','figure','drawing'}
for p in PAGES:
    scan=int(re.search(r'scan(\d+)',p.name)[1]);s=p.read_text()
    manual=[r for r in old if int(r['scan'])==scan and r['kind'] not in skip]
    entries=[]
    for idx,r in enumerate(manual):
        rr=dict(r);rr['kind']=kindmap.get(rr['kind'],rr['kind']);rr['sheet_kind']='cover' if scan==101 else 'text'
        first=r['first_words_or_objects']; pos=None
        # Use a literal heading/opening or written equation number as an anchor when available.
        if first in s:pos=s.index(first)
        else:
            eq=re.match(r'\((\d+[^)]*)\)',first)
            if eq and '('+eq[1]+')' in s:pos=s.index('('+eq[1]+')')
        if pos is None:
            words=re.findall(r'[A-Za-zÀ-ÿ]{3,}',first)
            for n in range(min(5,len(words)),1,-1):
                pat=r'.{0,18}?'.join(map(re.escape,words[:n]))
                m=re.search(pat,s,re.I|re.S)
                if m:pos=m.start();break
        if pos is None:pos=int((idx+.5)/max(1,len(manual))*len(s))
        entries.append((pos,0,rr))
    for name,body,pos,end in macros(s,['deleted','inserted','margin','diagram','figure']):
        kind={'deleted':'deletion','inserted':'insertion','margin':'margin note','diagram':'diagram','figure':'drawing'}[name]
        where=loc(pos,s)
        if name=='margin':
            m=re.search(r'% margin position: ([^\n]+)\n\s*$',s[:pos])
            if m:where=m[1]+'; '+where
        first=re.sub(r'\s+',' ',body).strip()
        if len(first)>180:first=first[:177]+'…'
        rr=dict(cote='64',scan=str(scan),sheet_kind='cover' if scan==101 else 'text',element='',kind=kind,position=where,first_words_or_objects=first,transcribed='yes')
        entries.append((pos,1,rr))
    for j,(_,_,r) in enumerate(sorted(entries,key=lambda x:(x[0],x[1])),1):
        r['element']=f'{scan:03d}-{j:03d}';final.append(r)
with inv.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']);w.writeheader();w.writerows(final)

# Current-state doubts are exhaustive; superseded draft readings stay in the working record.
doubt=ROOT/'MPL_64_078-115_doubts.md'
if not (ROOT/'records/doubts_working.md').exists():shutil.copy2(doubt,ROOT/'records/doubts_working.md')
notations=[
('Quotation marks',r"``...''",'Double handwritten quotation marks; no normalization to guillemets.'),
('Prime and star',r"i',\kappa',\wp';\ \mu_4^*",'Primes and stars distinguished; no prime silently substituted for an exclamation mark.'),
('Angular twisting superscript',r'^{\unsure{\sharp}}','Scans 80–97: lightning/4-like hand sign. The identification with a sharp sign is uncertain; the same doubtful encoding is used throughout.'),
('Small b superscript',r'M^b','Scan 80 (23). Small b-like sign; not silently changed to a musical flat.'),
('Ordinary Greek mu',r'\mu','Scans 78–80 first paragraph, 97–99 and scalar coefficient on 112–113; ordinary mu retained.'),
('Double-stem Greek mu',r'\unsure{\boldsymbol{\mu}|\mu}','Scans 80–96 and the right member μ4*(k) on 97. The ink resembles a blackboard mu; bold is the closest standard-LaTeX approximation, explicitly flagged as an alphabet doubt, not an exact facsimile glyph.'),
('Underlined orientation omega',r'\underline{\omega}_{\underline J}','Underlining retained where visible; often the index J is also underlined.'),
('Angular J / underlined J',r'J,\ \underline J','Finite set and relative notation distinguished by the written underline, without inferring it from the role.'),
('Sigma and punctured Sigma',r'\Sigma_J,\ \Sigma_J^*','Capital Greek sigma; star kept when visible.'),
('Underlined O',r'\underline O','Sheaf notation; not automatically replaced with calligraphic O.'),
('Ordinary T and double-stem T',r'T,\ \mathbb T_0','Double-stem universal bundle glyph checked on 86,89–93; ordinary tangent T remains distinct.'),
('Double-stem D and prime',r'\mathbb D_3,\ \mathbb D_3\prime','Scans 90–93. The raised mark is a prime; no factorial/exclamation interpretation supplied.'),
('Ornate permutation-group glyph',r'\unsure{\mathfrak S|\mathcal G}','Scans 84,89–91: strongly looped G-like form. Gothic S remains tentative and the same alternative is retained at each occurrence.'),
('Subscript on U',r'U_{03},\ U_{0,3}','Comma retained or absent according to the local writing; scan 80 was corrected from an initial V reading against the ink.'),
('Underlined U with uncertain subscript',r'\underline U_{\unsure{t|4}}','Scan 78; not resolved from later mathematics.'),
('Contracted product',r'\wedge,\ \wedge_{\mu_2},\ \wedge_{\mu_4}','Wedge-shaped product sign retained, including where it could be mistaken for an isomorphism mark.'),
('Tensor signs and powers',r'\otimes,\ ^{\otimes2},\ ^{\otimes(-2)}','Tensor sign distinguished from ×; local doubtful powers remain in place.'),
('Dual/check accents',r'\check F,\ \check\nu,\ \check\kappa,\ \check\delta,\ \check f','Scans 97–99 and 103–108. A small v above a letter is a check accent; the standalone operation is rendered ∨.'),
('Script L',r'\mathcal L_{E/S}','Legendre torsor; not a Greek letter.'),
('Plain F versus calligraphic F',r'F_t,\ \mathcal F_n','The line in V_J and section-IV function spaces use different handwritten alphabets.'),
('Square-U aggregate sign',r'\unsure{\coprod}','Scan 102: literal shape retained; no replacement with a direct-sum sign from the graded-algebra context.'),
('Tangent module t and tangent vector',r'\underline t_E,\ t_E,\ \delta','Underlining follows the ink; tangent t is distinguished from the moduli parameter t where written.'),
('Derivation symbols',r'\Theta_\delta,\ \delta_n','Capital loop-and-bar theta and lowercase delta checked across 102–115.'),
('Principal-part epsilon',r'\varepsilon_n','The same open epsilon shape on 102,105–106,115; harmonized from the draft epsilon/varepsilon font variation before freeze.'),
('Character chi',r'\chi_4','Scan 92; chi, not x.'),
('Small raised circle/zero',r'g^0','Scan 92: retained as 0; typography does not settle whether the author intended a small circle.'),
('Psi families',r'\psi^\omega(\delta),\ \psi_i^\omega(\delta)','Omega is superscript; i is a separate subscript.'),
('Weierstrass function',r'\wp,\ \wp\prime','The handwritten p-like function symbol is consistently rendered wp. Scan 108 (33) retains the single-prime reading with a double-prime alternative.'),
('Root coordinates',r'\unsure{\xi|\zeta}_i','Curled Greek form compared on 93,96,114–115; the residual xi/zeta doubt is explicit throughout 114–115.'),
('Torsion labels',r'e_i,\ \unsure{\varepsilon_i|e_i}','Latin e on 106–107; the heavier open form on 114 is tentatively epsilon, with e explicitly offered; 115 has the clear open epsilon.'),
('Headless lines',r'\arrow[r,no head],\ \mathbin{-}','No arrowhead is supplied solely because a map is expected.'),
]
lines=['# Notation table\n','| Handwritten sign / usage | LaTeX | Evidence and caution |','|---|---|---|']
lines += ['| '+esc(a)+' | `'+esc(b)+'` | '+esc(c)+' |' for a,b,c in notations]
lines += ['\n# Reading doubts\n',
'This table indexes every current `\\unsure` and `\\illegible` occurrence in the frozen-source candidate. Locations give an approximate vertical band and a nearby written equation/reference, followed by the exact page-file TeX line for navigation; they are not a count of manuscript lines. Repeated signs are listed repeatedly so an uncertain alphabet or exponent is never silently treated as certain elsewhere. The first reading is the diplomatic reading; alternatives are not corrections.\n',
'| Cote | Scan | Approximate line / location | Reading | Alternatives | Confidence |','|---|---|---|---|---|---|']
count=0
for p in PAGES:
    scan=int(re.search(r'scan(\d+)',p.name)[1]);s=p.read_text()
    for name,body,pos,end in macros(s,['unsure','illegible']):
        if name=='illegible':reading=f'Physically unreadable, estimated {body} word(s)';alt='No secure reading after enlarged inspection';conf='low'
        else:
            # Only top-level vertical bars separate offered alternatives.
            depth=0;split=None;i=0
            while i<len(body):
                if body[i]=='\\':
                    m=re.match(r'\\(?:[A-Za-z]+|.)',body[i:]);i+=len(m.group());continue
                if body[i]=='{':depth+=1
                elif body[i]=='}':depth-=1
                elif body[i]=='|' and depth==0:split=i;break
                i+=1
            reading=body if split is None else body[:split];alt='No distinct alternative proposed' if split is None else body[split+1:]
            deleted_context=any(n=='deleted' and a<=pos<b for n,_,a,b in macros(s,['deleted']))
            conf='low' if deleted_context else 'medium'
            if scan in (99,109,110,111) and ('third' in loc(pos,s)) and len(body)>8:conf='low'
        lines.append('| '+' | '.join(esc(x) for x in [64,scan,loc(pos,s),reading,alt,conf])+' |');count+=1
lines += ['\n## Residual alphabet and page-state cautions\n',
'- Scans 114–115: the root-coordinate letter is consistently read ξ after comparison with the earlier ξ on scans 93 and 96; ζ remains a possible alphabet identification. This doubt is marked at every affected occurrence and concerns the glyph family, not the numerical indices or the root identities.\n- Scan 111: the dense parenthetical insertion and its crossing strokes are less secure than the surrounding proof. Scan 109 has overlapping changes of nouns and a corrected final phrase. Both are marked in place.\n- The blackboard-like μ and angular twisting sign are not claimed to be exact font facsimiles. Their distinction from ordinary μ and ordinary prime/star marks is explicit in the table and source.\n',
'## Abbreviations encountered\n',
'Expansions below are interpretive aids only. None has been expanded in the transcription.\n',
'| Written form | Probable expansion / meaning | Caution |','|---|---|---|']
abbr=[('iso, iso., isom, isom.','isomorphisme','Final stop varies in the ink.'),('corr.','correspondance / correspondant','Depends on grammar; en corr. 1–1 is correspondence.'),('ens.','ensemble',''),('i.e., i.e','id est','As written, including missing stop.'),('NB','nota bene',''),('car., car','caractéristique',''),('car. rés.','caractéristique résiduelle',''),('rev.','revêtement',''),('inv.','inversible',''),('tr, Tr','trace','Mathematical label rather than an expanded noun.'),('objt','objet',''),('géom.','géométrique',''),('tte','toute','Tentative reading.'),('ép.','épinglage',''),('can., can','canonique',''),('tors.','torseur(s)',''),('à g.','à gauche',''),('tautol.','tautologique',''),('car. can.','caractère canonique',''),('s-groupe','sous-groupe',''),('pts','points',''),('alg. clos','algébriquement clos',''),('équiv.','équivalent(es)',''),('él.','élément(s)',''),('val.','valeurs','à val. dans'),('RR','Riemann–Roch','Name of the cited formula.'),('ass. comm.','associative, commutative',''),('hom','homomorphisme',''),('gén.','généralement',''),('OPS, ops','on peut supposer','Probable expansion; lowercase/capitalization retained.'),('vts / pts, with raised ts','points?','First letter is uncertain on scan 106; no confident expansion supplied.'),('O.K.','okay','As written.'),('cor.','corollaire',''),('prop., Propos.','proposition',''),('lin, lin., lint with raised t','linéaire / linéairement','Context dependent.'),('cqfd.','ce qu’il fallait démontrer',''),('sym.','symétriques',''),('f. et s.','faut et suffit',''),('autom., auto.','automorphisme(s)',''),('SSS','si et seulement si','Capital form retained.'),('tjrs','toujours',''),('mb','membre',''),('multiplic.','multiplication',''),('rat.','rationnelle',''),('comb. lin.','combinaison linéaire',''),('vect.','vecteur(s)',''),('indép.','indépendant(s)',''),('pr','pour','Tentative reading in scan 114 margin.'),('catég','catégorie','Cancelled unfinished form.')]
lines += ['| '+' | '.join(esc(x) for x in row)+' |' for row in abbr]
lines += ['\n## Legibility and reliability\n',
'All 38 full scans and their 76 supplied halves were read directly by the main transcriber without OCR, followed by a second visual reading of every page after all drafts existed. The main text is usually recoverable, but the hand is very compressed, and sparse strokes often do not determine word endings or tiny indices. The least secure areas are cancelled writing, the clipped lower note on scan 84, the crowded upper-right note on scan 99, the overwritten lower lines on scan 109, both diagonal notes on scan 110, and the insertion on scan 111. Enlarged and rotated crops were used for those areas.\n',
'Confidence labels concern readings, not mathematical validity. Medium means a plausible ink reading with a live doubt; low means strongly overwritten, clipped, or otherwise weakly resolved. No uncertain reading is labelled high merely because it would give a familiar theorem. The transcription preserves apparent mistakes, incomplete formulas, duplicate words and unfinished arguments. The working apparatus and audit log preserve superseded first-pass readings, so they should not be mistaken for the current text.\n',
'All manuscript page numbers are separate from archive foliation. Scan 101 is a title sheet; no author page number has been supplied on scan 114 where none is visible.\n']
doubt.write_text('\n'.join(lines))
(ROOT/'MPL_64_078-115_transcription.tex').write_text(''.join(p.read_text()+'\n' for p in PAGES))
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:f.write(f'final apparatus rebuilt {now}: {len(final)} inventory rows; {count} current uncertainty occurrences; historical first-pass apparatus retained in records.\n')
print('Inventory',len(final),collections.Counter(r['kind'] for r in final),'doubt occurrences',count)
