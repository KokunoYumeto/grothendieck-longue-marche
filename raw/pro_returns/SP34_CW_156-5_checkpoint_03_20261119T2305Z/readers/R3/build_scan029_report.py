from pathlib import Path
from datetime import datetime, timezone
import json

b=Path('/workspace/scratch/4770596940a0')
out=b/'out/readers/R3'
c=b/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan029.tex'
t=c.read_text()
t=t.replace(r'\unsure{F|\mathcal F}', 'F')
t=t.replace(r'\deleted{\unsure{F}}G',r'\deleted{F}G')
t=t.replace(r'\unsure{s\'apparente}',r'\unsure{s\'apparente|l\'apparente}') if False else t.replace("\\unsure{s'apparente}","\\unsure{s'apparente|l'apparente}")
t=t.replace(r'\unsure{la propriété|la présentation}',r'\unsure{la priorité|la propriété|la présentation}')
(out/'scan029.tex').write_text(t)
crops=json.loads((out/'scan029_crops.json').read_text())
D=[]
def add(place,C,H,reading,ink,confidence,kind,crop,ac=False,ah=True,mh=False):
    k=f'R3-029-D{len(D)+1:02}'
    D.append(dict(id=k,place=place,C=C,H=H,reading=reading,ink=ink,confidence=confidence,
                  kind=kind,crop=crop,against_C=ac,against_H=ah,marked_in_H=mh))
    return k

add('first heading','underlined Proposition','bold Proposition','underlined Proposition',
    'A horizontal line follows the base of the heading; ordinary handwritten letters carry no independent bold state.',
    'high','other','proposition')
q1=add('first proposition, F',r'\unsure{F|\mathcal F}','F','F',
    'Straight upright, upper arm and shorter middle arm; no script loop or lower return.',
    'high','other','proposition',True,False)
add('first proposition, after the relation','on ... l’appelle','qu’on appelle','on ... l’appelle',
    'The pronoun is a low rounded mark and horizontal n-like stroke; there is no preceding qu. A separate tall l and apostrophe precede appelle.',
    'high','misread word','top_call')
q2=add('first proposition, damaged older letter before l’appelle',r'\deleted{\unsure{y|l}}','omitted',r'\deleted{\unsure{y|l}}',
    'A short upper hook and descending trace survive in a brown damaged/erased patch. The patch prevents distinguishing the two candidates or securely separating erasure from physical damage; C’s conservative deleted reading is retained.',
    'low','omission','top_call')
add('first proposition, quotation marks','``figure intersection\'\'','« figure intersection »','``figure intersection\'\'',
    'Two small pen strokes at each end, not angled guillemets.',
    'high','misread symbol or index','proposition')
add('warning, emphasis','underlined n’est pas','unmarked n’est pas','underlined n’est pas',
    'Separate horizontal line underneath the three-word phrase.',
    'high','omission','warning')
q3=add('warning, interlinear insertion',r'\inserted{\unsure{en général}}',r'\add{en général}',r'\inserted{\unsure{en général}}',
    'A low en-like wave, descending g loop, raised accent and compressed final run sit above the line. The phrase remains probable but its middle letters are compressed.',
    'medium','other','insertion')
add('warning, la figure','live la figure','deleted la figure','live la figure',
    'The curved stroke passes above la and points from the interlinear addition to its insertion point. It does not cancel the baseline phrase.',
    'high','deletion state (struck given live or live given struck)','warning')
q4=add('warning, cancelled word after F cap G',r'\deleted{\unsure{intersection|inter.}}',r'\struck{\ill{}}',r'\deleted{\unsure{intersection|inter.}}',
    'An initial dotted trace, a central tall t-like peak and terminal point survive the dense horizontal strike. Neither the full word nor an abbreviation is settled.',
    'low','readable ink left as `\\ill{}`','deleted_warning',False,True,True)
add('warning, following prose','en se rappelant','où on rappelle','en se rappelant',
    'Two short groups en and se precede the r, paired p descenders and tall l of rappelant; the end has an upward t-like stroke.',
    'high','misread word','warning')
q5=add('warning, older F underneath G',r'\deleted{\unsure{F}}G','G',r'\deleted{F}G',
    'A separate inner upright with two rightward bars survives inside the larger curved G. Its form matches the adjacent plain F.',
    'high','omission','warning_symbols',True,True)
q6=add('warning, power-set letter',r'\unsure{\mathfrak P|\mathscr P|\mathbb P}',r'\mathfrak P',r'\unsure{\mathfrak P|\mathscr P|\mathbb P}',
    'Long upright through an angular upper enclosure and low leftward curl. The overdrawn hand does not decide among the three alphabet renderings.',
    'low','misread symbol or index','warning_symbols')
add('warning, L in live power-set expression','L',r'\mathcal L','L',
    'Short angled upright and rightward foot, without a looped script capital outline.',
    'high','misread symbol or index','warning_symbols')
add('warning, L in cancelled power-set expression','L',r'\mathcal L','L',
    'The separately inspected struck occurrence again has a diagonal upright and lower foot; the long horizontal crossing is a deletion stroke.',
    'medium','misread symbol or index','warning_symbols')
add('middle, article before F.G','le F.G','la F.G','le F.G',
    'Tall l followed by a short low return, rather than an open a bowl.',
    'high','misread word','notion')
add('middle, after En fait','ça marche','se construit','ça marche',
    'The first small group has a descending c/cedilla form and oval a. The second has low m/a/r/c strokes and one tall h peak, not the sequence constr-uit.',
    'high','misread word','notion_phrase')
q7=add('lower paragraph, verb following double relation',r"\unsure{s'apparente}","l'apparente",r"\unsure{s'apparente|l'apparente}",
    'The first stroke is nearly upright with a bent lower end and a detached apostrophe. The retraced pp and ending -arente support apparente, but the initial s/l is not settled by its reduced shape.',
    'low','misread word','verb',True,True)
q8=add('lower paragraph, deleted phrase and its position',r'\deleted{\unsure{la propriété|la présentation}} before à une propriété de',
    r'\struck{\ill{}} after à une propriété de',
    r'\deleted{\unsure{la priorité|la propriété|la présentation}} before à une propriété de',
    'A looped la-like group, clear p descender, early raised dot and tall ending before é remain. Only one p descender is clear, permitting priorité; the dense rule leaves propriété/présentation possible. The deleted phrase is to the left of à une, on the preceding part of that line.',
    'low','insertion or placement','deleted_lower',True,True,True)
q9=add('lower paragraph, quoted underlined word',r'\unsure{modération|médiation}',r'\uncertain{demi-treillis}',r'\unsure{modération|médiation}',
    'Initial low m/o-like strokes precede a distinct d. The raised accent after the d and a later tall t favour modération; compressed middle strokes leave médiation open. No demi-treillis sequence or hyphen is identifiable.',
    'low','misread word','moderation',False,True,True)
add('lower paragraph, formatting of quoted word','double pen-stroke quotes and underline','guillemets, no underline','double pen-stroke quotes and underline',
    'Two short strokes mark both ends, with a distinct horizontal line below the word.',
    'high','omission','moderation')
add('foot, cancelled heading','underlined Propriété','bold Proposition','underlined Propriété',
    'A p/r sequence followed by the short -priété ending and an acute mark; no long -position run. A separate underline lies beneath it.',
    'high','misread word','foot')
add('foot, first relation and H extra deleted fragment','F-prime preceq F',r'F-prime \struck{\ill{}} preccurlyeq F','F-prime preceq F; no independently recoverable deleted token',
    'The relation has a heavily retraced upper loop and two lower curved strokes. No separate older letter or word can be isolated from that overtrace. This is retained as the curved relation glyph, with the uncertainty about its overtrace recorded here.',
    'low','other','foot_order',False,True,True)
q10=add('foot, locally deleted group after F',r'\deleted{\unsure{, et des}}',r'\struck{\ill{}}',r'\deleted{\unsure{, et des}}',
    'Comma-like downstroke, a small crossed t-like peak, then a looped tall d and short terminal run under two cancellation lines; exact letters remain weak.',
    'low','readable ink left as `\\ill{}`','foot_order',False,True,True)
q11=add('foot, parenthetical first word',r'\unsure{Immédiat|Immédit|immédite}',r'\uncertain{Immédiat}',r'\unsure{Immédiat|Immédit|immédite}',
    'Initial barred I-like stroke, mm waves, acute and d loop are visible. The low letters immediately before the final tall t intersect a cancellation diagonal, so the exact ending stays unresolved.',
    'medium','other','immediat',False,True,True)
add('foot, word after sur in parentheses','supports',r'\ill{}','supports',
    'Initial s, low u, two long p stems, rounded o/r and final t/s survive; one p is crossed by the diagonal but is not lost.',
    'high','readable ink left as `\\ill{}`','foot_words',False,True,True)
add('foot, induite emphasis','underlined induite','italic/emphasized induite','underlined induite',
    'A long horizontal underline runs beneath the word, distinct from the cancellation diagonal.',
    'high','other','foot_words')
add('foot, final preposition','sur un raffinement','par un raffinement','sur un raffinement',
    'The surviving short curved beginning and low u-like wave fit sur. The apparent long initial descender belongs to the diagonal cancelling the block; it does not establish a p.',
    'medium','misread word','foot_words')
add('foot, state of the complete three-line statement','whole statement inside deleted','statement rendered live with a following editorial note','whole statement deleted; no editorial sentence',
    'Several long oblique strokes cross all three lines, beyond the local deletion after F. The explanatory note in H has no handwritten counterpart.',
    'high','deletion state (struck given live or live given struck)','foot')

qs=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11]
cd=[dict(occurrence=i,difference_id=k,status=('resolved' if i in (1,5) else 'retained, alternatives broadened' if i in (7,8) else 'retained')) for i,k in enumerate(qs,1)]
I=[]
def inv(kind,position,content):
    I.append(dict(scan='029',sheet_kind='text',hand='his hand',element=f'R3-029-I{len(I)+1:02}',kind=kind,position=position,first_words_or_objects=content,transcribed='yes'))
inv('text','top centre','manuscript number 28')
inv('deletion','top left','Alors')
inv('text','below false start','Ainsi')
inv('text','top proposition, three lines','underlined Proposition; On a construit un Inf ... figure intersection F.G')
inv('deletion','top proposition before l’appelle','damaged older y|l')
inv('text','upper warning, two lines','Attention, ce n’est pas ... la figure F cap G ... en se rappelant ...')
inv('insertion','above warning before la figure','en général')
inv('deletion','warning after F cap G','intersection|inter.')
inv('deletion','warning, inside corrected G','older F')
inv('deletion','warning at right edge','G subset P(L)')
inv('text','middle paragraph, three lines','Nous n’allons considérer cette F cap G ... les deux coïncident !')
inv('text','middle paragraph, four lines','Donc la bonne notion ... le F.G. En fait, ça marche ... figures, et')
inv('display','middle below figures','absolute support of meet over i in I equals intersection of supports')
inv('text','lower paragraph, four lines','Cette propriété d’existence ... s’apparente|l’apparente ... propriété de modération|médiation')
inv('deletion','lower paragraph before à une','la priorité|la propriété|la présentation')
inv('text','lower paragraph quoted last word','underlined modération|médiation with double quotation marks')
inv('deletion','foot, entire three-line statement','underlined Propriété; Si F-prime preceq F ... Subdivision induite sur un raffinement.')
inv('deletion','foot, local deletion after F','comma, et des')

notes=[
 dict(id='R3-029-N1',text='The page names F.G the infimum of F and G for the double relation, distinguishes it from the set-theoretic intersection F cap G in general, restricts the latter discussion to compatible figures, and claims equality in that case. It then says ça marche for an arbitrary family and writes the support-of-meet identity. These claims are transcribed; this sheet supplies no new proof of the arbitrary-family assertion.'),
 dict(id='R3-029-N2',text='The deleted final property uses the curved subdivision relation, not the double relation of the infimum statement. It says F-prime preceq F implies F-prime.G preceq F.G, followed by the uncertain word Immédiat and the clear words sur supports. The notes preserve this as a cancelled claim, not a checked theorem.'),
 dict(id='R3-029-N3',text='An abstract meet is monotone for its defining preorder: if A-prime <= A, then A-prime meet G is a lower bound of A and G and hence lies below A meet G. This argument alone does not prove the manuscript’s final property, because it uses a different relation. This distinction prompted separate inspection of both curved signs and both double signs.'),
 dict(id='R3-029-N4',text='Conditionally, if subdivision preserves supports and the displayed binary support formula holds, then |F-prime.G|=|F-prime| intersect |G|=|F| intersect |G|=|F.G|. This verifies only the support consequence suggested by sur supports; it does not establish the subdivision relation itself.'),
 dict(id='R3-029-N5',text='The word after propriété de is kept as modération|médiation from the visible m/d/t sequence and accents; no lattice terminology is substituted for it. The reduced initial of s’apparente also allows l’apparente. The deleted phrase before à une permits priorité in addition to C’s two candidates; it is not moved after de as in H.'),
 dict(id='R3-029-N6',text='No verb is supplied in où F et G compatibles. The distinct F cap G in the middle paragraph and dotted F.G elsewhere were read separately. Manuscript number 28 is visible; there is no date, title sheet or page-count statement, and no diagram, drawing or independent margin note. No OCR, external research, other-reader files or adjudications were consulted.')
]
who='GPT-6 Astra Pro; effort inherited, not separately exposed; R3 scan029'
date=datetime.now(timezone.utc).date().isoformat()
checks=[
 dict(statement_id='R3-029-N3',date=date,who=who,type='targeted proof check',outcome='By the lower-bound property A-prime meet G <= A-prime and <= G. Transitivity with A-prime <= A makes it a lower bound of A,G, so it is <= A meet G. This checks the abstract same-preorder result only, not the page’s distinct subdivision relation.'),
 dict(statement_id='R3-029-N4',date=date,who=who,type='targeted proof check',outcome='Substituting equality of supports into the binary support-intersection formula gives equal product supports. Both premises are explicitly conditional here; no geometric subdivision conclusion was verified.'),
 dict(statement_id='R3-029-N1',date=date,who=who,type='carried as background without fault found',outcome='The claimed infima, arbitrary-family formula and compatible-figure identification were read as premises/assertions. They were not independently proved in this run.')
]
report=dict(scan='029',reader='R3',model='GPT-6 Astra Pro (inherited)',effort='inherited; not separately exposed',
 start_utc=(out/'scan029_start.txt').read_text().strip(),end_utc=datetime.now(timezone.utc).isoformat(),
 source_C=str(c),source_H=str(b/'working/H/scan029.tex'),
 images_viewed=[str(b/'source/SP34_CW_156-5_scans'/f'J156-5-04_156-5_scan029{s}.jpg') for s in ('','_a','_b')]+[x['path'] for x in crops],
 image_order='Whole page first, then a, then b; all nineteen recorded crops subsequently emitted and visually inspected. Two lower crops rotated three degrees clockwise for reading.',
 crops=crops,crop_reference_convention='Each differences.crop is a name in crops; recipes contain absolute source/path, pixel bbox, rotation and scale.',
 reading_file=str(out/'scan029.tex'),differences=D,C_doubt_resolutions=cd,
 S_decisions=[dict(decision='no applicable scan029 row',source='source/SP34_CW_156-5_sweep3/readings/156-5_CORRECTIONS.tsv',evidence='Filtered where fields for scan029 and manuscript page28; no applicable row.')],
 inventory=I,remaining_doubts=[dict(difference_id=k) for i,k in enumerate(qs,1) if i not in (1,5)]+[dict(difference_id=D[21]['id'],issue='retraced first curved relation does not disclose an independently readable older token')],
 notation=[
  dict(place='first proposition and lower paragraph',reading=r'\ll',ink='Two separate left-pointing wedges; not a curved subdivision sign.'),
  dict(place='cancelled final property',reading=r'F\prime\preceq F; F\prime.G\preceq F.G',ink='Curved upper order shapes with separate lower bars; first is retraced. Primes are high and the product marks low.'),
  dict(place='support display',reading=r'\left|\bigwedge_{i\in I}F_i\right|=\bigcap_{i\in I}|F_i|',ink='Angular wedge at left, round arch at right, dotted short i in both limits and both F subscripts; barred capital I.'),
  dict(place='warning',reading=r'F,\deleted{F}G\subset\unsure{\mathfrak P|\mathscr P|\mathbb P}(L)',ink='Open curved subset; two bars in the older F inside G; P alphabet remains ambiguous; L angular in both occurrences.'),
  dict(place='named terms',reading='double backtick/apostrophe quotes; underline on modération|médiation',ink='Two small strokes at each end, not guillemets.'),
  dict(place='abbreviation',reading='Inf',ink='Capital barred I, low n and long descending f; no expansion in text.')
 ],notes_while_reading=notes,check_events=checks,
 difference_boolean_convention='Flags compare text, uncertainty and meaningful manuscript state, excluding macro spelling alone. C doubt resolution rows refer to differences by ID; retained rows can have both flags false.',
 legibility='Main prose, the support display and principal order signs are legible. The least secure areas are damaged ink before l’appelle, short heavily deleted phrases, the script P alphabet, the reduced initial of apparente, the quoted lower term, and the crossed parenthetical adjective.',
 verification='No compilation performed. Page reread against the complete LaTeX; all C doubt occurrences and the H differences identified are recorded. No later scan opened.')
(out/'scan029.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(dict(differences=len(D),C_doubts=len(cd),inventory=len(I),crops=len(crops),against_C=sum(x['against_C'] for x in D),against_H=sum(x['against_H'] for x in D)))
