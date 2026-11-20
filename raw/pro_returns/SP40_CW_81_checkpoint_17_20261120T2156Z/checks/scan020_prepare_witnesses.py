#!/usr/bin/env python3
"""Exact current C/H source scopes for scan020 public locus readings."""
from pathlib import Path
import hashlib
import json
import re
import sys
sys.dont_write_bytecode=True
from scan020_prepare_sources import span

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
T={w:(BASE/f'packets/020/{w}.tex').read_text() for w in 'CH'}


def exact(w,literal,reading=None,occurrence=0,marked=None):
    text=T[w]
    starts=[m.start() for m in re.finditer(re.escape(literal),text)]
    assert len(starts)>occurrence,(w,literal,occurrence)
    at=starts[occurrence]
    if marked is None: marked=w=='H' and (r'\uncertain' in literal or r'\ill{' in literal)
    return dict(reading=reading or literal,
        source=span(f'packets/020/{w}.tex',text,at,at+len(literal),source_sha256_utf8=hashlib.sha256(text.encode()).hexdigest()),
        complete_inspected_source=span(f'packets/020/{w}.tex',text),marked_in_H=bool(marked),
        marked_scope=('The local H placeholder/uncertainty explicitly covers this selected source locus.' if marked else
                      'No H uncertainty or ill marker covers this exact local source component.'))


def absent(w,anchor,description,occurrence=0,marked=False):
    value=exact(w,anchor,description,occurrence,marked)
    value['absence_scope']='The described separately represented mark is absent from the exact complete source; anchoring context is provenance only.'
    return value


def both(c,h=None):
    return {'C':exact('C',c),'H':exact('H',h or c)}


W={
 'CONVENTION':both(r'\scanpage{20}',r'\page{19}'),
 'RING1':both(r'\Pi_I^{\unsure{\circ|0}}',r'\Pi_I^0'),
 'RING2':both(r'\Pi_J^\circ',r'\Pi_J^0'),
 'PI-PREDECESSOR':{'C':exact('C',r'\deleted{\Pi}U_{J,i}',r'\deleted{\Pi}'),
    'H':absent('H',r'$U_{J,i}$, et de plus','No Pi predecessor represented beneath the opening U.')},
 'CLAS-WORD':{'C':exact('C',r'\unsure{clas.|deux}'),'H':exact('H','les deux parmi','deux')},
 'CLAS-POINT':{'C':exact('C',r'\unsure{clas.|deux} parmi','A terminal point is present in the primary clas. candidate; the printed deux alternative has no terminal point.'),
    'H':absent('H','les deux parmi','No terminal point represented after deux.')},
 'PAIR-INDEX':both(r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+',r'\Sigma_i^+'),
 'POSITIVE-SIGMA-HEAD':{
    'C':absent('C',r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+','Ordinary Sigma macro; no separate upper-head-run path represented.'),
    'H':absent('H',r'\Sigma_i^+','Ordinary Sigma macro; no separate upper-head-run path represented.')},
 'PAIRED-REMAINDER':both(r'U_{J,i}\cap\Sigma_i^-'),
 'NEGATIVE-SIGMA-HEAD':{w:absent(w,r'\Sigma_i^-',r'Ordinary \Sigma_i^-; no separate upper-head-run, point or lower-hook path represented.') for w in 'CH'},
 'UPPER-PROSE':both('qui sont non vides. Or les deux classes en question sont non vides, car'),
 'CANCELLED-SIGMA':{'C':exact('C',r'\deleted{$\unsure{\Sigma_i|\Sigma_j}$}'),
    'H':exact('H',r'\struck{\ill{}}',occurrence=0)},
 'CANCELLED-SIGMA-HEAD':{'C':absent('C',r'\deleted{$\unsure{\Sigma_i|\Sigma_j}$}','Ordinary cancelled Sigma alternatives; no separate upper-head-run path represented.'),
    'H':exact('H',r'\struck{\ill{}}','The complete cancelled group is one struck ill placeholder; no separate upper-head-run path represented.',occurrence=0)},
 'VOISINAGE-POINT':{w:absent(w,'est un voisinage de','No separately represented point in the gap after voisinage.') for w in 'CH'},
 'E-INDEX':{'C':exact('C',r'E_{\unsure{i|j}}'),'H':exact('H','voisinage de $E_i$',r'E_i')},
 'E-PREDECESSOR':{'C':exact('C',r'\deleted{\Sigma}E_{\unsure{i|j}}',r'\deleted{\Sigma} beneath E'),
    'H':absent('H','voisinage de $E_i$','No Sigma predecessor represented beneath this E.')},
 'E-COMMA':{'C':exact('C',r'E_{\unsure{i|j}}$, et','Comma after the E index.'),
    'H':absent('H',r'E_i$ et','No comma represented after the E index before et.')},
 'BAR1':both(r'\overline{\Sigma_i^+}'),
 'BAR1-SIGMA-HEAD':{w:absent(w,r'\overline{\Sigma_i^+}',r'Long outer overbar present around ordinary \Sigma_i^+; no separately drawn short-head run represented.') for w in 'CH'},
 'BAR2':both(r'\overline{\deleted{E}\Sigma_i^-}',r'\overline{\Sigma_i^-}'),
 'BAR1-E-PREDECESSOR':{'C':exact('C',r'\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i',r'\deleted{\Sigma} beneath the first intersected E_i'),
    'H':absent('H',r'\overline{\Sigma_i^+}\cap E_i','No Sigma predecessor represented beneath the first intersected E_i.')},
 'BAR2-SIGMA-PREDECESSOR':{'C':exact('C',r'\overline{\deleted{E}\Sigma_i^-}',r'\deleted{E} beneath the second barred Sigma'),
    'H':absent('H',r'\overline{\Sigma_i^-}','No E predecessor represented beneath the second barred Sigma.')},
 'BAR2-E-PREDECESSOR':{'C':exact('C',r'\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i',r'\deleted{\Sigma} beneath the second intersected E_i'),
    'H':absent('H',r'\overline{\Sigma_i^-}\cap E_i','No Sigma predecessor represented beneath the second intersected E_i.')},
 'NONEMPTY-ENDPOINTS':both(r'\ne\varnothing,\quad'+'\n'+r'\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.',
    r'\neq\emptyset$,'+'\n'+r'$\overline{\Sigma_i^-}\cap E_i\neq\emptyset$.'),
 'VOIT':{'C':exact('C',r'\unsure{voit|sait}'),'H':exact('H','On voit donc','voit')},
 'EN':{'C':exact('C','est en','en'),'H':absent('H','classes est '+r'\struck{\ill{}}','No live en represented between est and the cancelled-word placeholder.')},
 'COUNT-WORD':{'C':exact('C',r'\deleted{\unsure{tout|est}}'),'H':exact('H',r'\struck{\ill{}}',occurrence=1)},
 'COUNT':both(r'$(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève',
    r'$(n-1)+2 = n+1 = \operatorname{card}I+1$ (ce qui achève'),
 'ACHEVE':both('ce qui achève'),
 'AUSSI':{'C':exact('C',r'\unsure{aussi|ainsi}'),'H':exact('H','achève aussi la','aussi')},
 'LA-POINT':{'C':absent('C',r'la \unsure{dém.|dem.}','No separate point represented at la.'),
    'H':absent('H',r'la dém.\ par','No separate point represented at la.')},
 'DEM':both(r'\unsure{dém.|dem.}','dém.'),
 'PAR':{'C':exact('C','par récurrence','par'),'H':exact('H','par\nrécurrence','par')},
 'RECURRENCE':both('récurrence'),
 'NB1':{'C':exact('C','le nb des classes est','nb'),'H':exact('H','le nb des\nclasses est','nb')},
 'NB2':{w:exact(w,'sur le nb des classes','nb') for w in 'CH'},
 'CARD':both(r'\operatorname{card} I+1',r'\operatorname{card}I+1'),
 'LEMMA-HEADING':both(r'\uline{Lemme}',r'\emph{Lemme}'),
 'RING3':{'C':exact('C',r'\Pi_I^\circ'),'H':exact('H',r'\Pi_I^0',occurrence=1)},
 'UNION':{'C':exact('C',r'\bigcup_{\alpha\in\deleted{\unsure{I}}K}',r'Generic \bigcup with qualified cancelled-I/K index; no literal union paths.'),
    'H':exact('H',r'\bigcup_{\alpha\in K}',r'Generic \bigcup with alpha-in-K index; no literal union paths.')},
 'UNION-INDEX':both(r'\alpha\in\deleted{\unsure{I}}K',r'\alpha\in K'),
 'BRACE':{'C':exact('C',r'\overbrace{\Sigma_\alpha^+\cup E_\alpha}^{\inserted{\widehat{\Sigma}_\alpha^+}}',r'Generic overbrace under the inserted hatted Sigma label; no literal brace runs.'),
    'H':absent('H',r'\note{au-dessus de $\Sigma_\alpha^+\cup E_\alpha$, il écrit'+'\n'+r'$\widehat{\Sigma}_\alpha^+$}','No brace drawing represented; the apparatus records the upper hatted Sigma label.')},
 'HAT-LABEL':{'C':exact('C',r'\inserted{\widehat{\Sigma}_\alpha^+}'),
    'H':exact('H',r'\note{au-dessus de $\Sigma_\alpha^+\cup E_\alpha$, il écrit'+'\n'+r'$\widehat{\Sigma}_\alpha^+$}',r'Apparatus describes one \widehat{\Sigma}_\alpha^+ above the union term.')},
 'NONVIDE':both(r'\inserted{\deleted{non vide}}',r'\add{\uncertain{non vide}}'),
 'GUIDE':{'C':absent('C',r'partie \inserted{\deleted{non vide}} de $I$, et','No separate curved insertion-guide path represented.'),
    'H':absent('H',r'partie \add{\uncertain{non vide}} de $I$, et','No separate curved insertion-guide path represented; the uncertainty marker covers the words non vide, not a guide path.')},
 'LEMMA-PROSE':both('où $K$ est une partie'),
 'MARGIN':both(r'\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{19}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar',
    r'\marginal{$K$ est $\neq\emptyset$ si $I\neq\emptyset$}'),
 'ONA':{'C':exact('C',r'\deleted{on a}'),'H':exact('H',r'\struck{\ill{}}',occurrence=2)},
 'MEMBERSHIP':{'C':exact('C',r'\deleted{\unsure{\Rightarrow}}\in'),'H':exact('H',r'\Sigma_\alpha^+\in\pi_0',r'\in; no arrow predecessor or local literal path represented.')},
 'MEMBERSHIP-E':both(r'X\setminus E_\alpha'),
 'FINAL-CLAUSES':both(r'tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.',
    'tels que\n'+r'$\forall\alpha,\beta\in K$, $\alpha\neq\beta$, on ait'+'\n'+r'$\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\emptyset$'+'\n'+r'($\Longleftrightarrow \Sigma_\alpha^+\cap\Sigma_\beta^+=\emptyset$).'),
 'ARCHIVE':{'C':exact('C','% archive sheet number: 19'),
    'H':absent('H',r'\page{19}','No separate archive-numeral comment; H carries the editorial page label 19.')},
}
W['S-AUDIT']={}
for w in 'CH':
    W['S-AUDIT'][w]=dict(reading='The two local nonemptiness Sigma expressions carry overbars in this exact witness source.',
        source=span(f'packets/020/{w}.tex',T[w]),complete_inspected_source=span(f'packets/020/{w}.tex',T[w]),
        local_bar_sources=[W['BAR1'][w]['source'],W['BAR2'][w]['source']],marked_in_H=False,
        marked_scope='The two local overbar commands carry no H uncertainty/ill qualifier; other H qualifiers lie outside those components.')
result={f'SRC020-{k}':v for k,v in W.items()}
x=json.loads((OUT/'scan020_source_crosswalk.json').read_text())
assert set(result)=={l['source_locus_id'] for l in x['loci']}
out=dict(scan=20,scope='Exact witness-source readings and bounded source absences; no root choice or count.',
    witnesses=result,main_adjudicated=False)
path=OUT/'scan020_witness_sources.json'
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(path=path.relative_to(BASE).as_posix(),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),source_loci=len(result)),ensure_ascii=False))
