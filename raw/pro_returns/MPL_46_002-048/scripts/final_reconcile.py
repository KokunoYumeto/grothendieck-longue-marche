"""Pre-context reconciliation from the final visual comparisons; run once."""
import json
from record_page import ROOT, amend, rebuild, utc

amend(12, r'\mathbf Z/p\mathbf Z', r'\mathbb Z/p\mathbb Z',
      'Final visual notation comparison: doubled Z strokes agree with scan 017.')
amend(18, r'\mathcal O_T', r'\underline O_T',
      'Final enlarged view of cancelled proof: separate lower stroke beneath O is visible.')
amend(20, r'f\in\mathcal O_X', r'f\in\unsure{O_X|\underline O_X}',
      'Final enlarged notation comparison: round O; a separate lower stroke is unresolved.')
amend(21, r'\mathcal O', 'O',
      'Final notation comparison: the two local-ring O glyphs are round and have no separate underline.')
amend(22, r'_{\mathcal O_X}', r'_{\underline O_X}',
      'Final notation comparison: lower stroke of cancelled symmetric-power subscript retained.')
amend(22, r'_{\mathcal O_S}', r'_{\underline O_S}',
      'Final notation comparison: lower stroke in both bottom coefficient-ring symbols retained.')
amend(13, '\\end{tikzcd}}}\n\nDéfinitions',
      '\\end{tikzcd}}\\figure{\\begin{tikzpicture}\\draw (0,0)--(1.8,0)..controls(2.5,0)and(2.2,.9)..(2.2,1.5)..controls(2.2,1.8)and(2.6,1.8)..(3.0,1.8)--(6.0,1.9);\\end{tikzpicture}}}\n\nDéfinitions',
      'Final full-page comparison: added the bent outline separating the marginal diagram from the body.')
amend(13, r"\node[draw,ellipse] {C'est};",
      r"\node[draw,ellipse] {C'est};\draw (-.45,.1)..controls(-1,1.0)and(-.6,1.8)..(.5,2.1);",
      'Final full-page comparison: retained the curved pointer from the circled insertion.')

def get(n):
    p=ROOT/'records'/f'scan{n:03d}.json'
    return p,json.loads(p.read_text())

def move_row(n, match, before):
    p,r=get(n)
    row=next(x for x in r['inventory'] if match in x[2])
    r['inventory'].remove(row)
    idx=next(i for i,x in enumerate(r['inventory']) if before in x[2])
    r['inventory'].insert(idx,row)
    p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')

for n,match,before in [
    (7,'vertical emphasis','Théorème'),
    (13,'small outline','C’est un foncteur'),
    (34,'oval and short tail','b) implique que'),
    (41,'outline around et dualité','et dualité des projectifs'),
    (47,'curved enclosure','on sait par construction')]:
    move_row(n,match,before)

p,r=get(13)
i=next(i for i,x in enumerate(r['inventory']) if x[0]=='diagram')
r['inventory'].insert(i+1,['drawing','lower/right boundary of upper-left diagram','bent outline separating diagram from body'])
for row in r['inventory']:
    if row[2]=='small outline around C’est':
        row[2]='small outline around C’est and upward curved pointer'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')

# Update explanatory metadata to describe the final readings, not superseded readings.
for n in (29,36,45,47):
    p,r=get(n)
    if n==29:
        for row in r['inventory']:
            row[1]=row[1].replace('boxed heading','heading between horizontal rules')
        for row in r['doubts']:
            row[0]=row[0].replace('boxed heading','heading between horizontal rules')
    elif n==36:
        r['doubts'][-1]=['top diagram, right upper object',"X′ followed by ! or another prime",'The separate stroke lacks a securely resolved dot; both readings are marked inline.','medium']
    elif n==45:
        r['inventory'][-2][2]='à vérifier ; Montrons/Montrer X→S est projectif'
        r['doubts'][-1][1]='Montrons/Montrer; géoréd!; q(Pic(X/S)); noéthérien'
    else:
        for row in r['inventory']:
            row[2]=row[2].replace('construction L de ξ','construction C/L de ξ')
        r['doubts']=[
            ['proof insertion','on sait par construction C/L de ξ','Compressed parenthesis joins the sufficiency clause; the symbol resembles C, with script L retained as alternative.','low'],
            ['proof, last words','Ce est par descente, tjs/tjrs avec le = principe','Short abbreviation between the comma and avec is compressed; wording is not regularized.','low'],
            ['lower left margin',"car on sait qu'il/car alors qu'il devient trivial sur X",'Several words remain weak after rotation and enlargement; the earlier diviseur guess was rejected on the second visual reading.','low'],
            ['bottom remark',"au =/avec la relation d’incidence can.",'Small second line touches the lower paper edge; the connective and initial article remain especially tentative.','low']]
    p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')

for p in sorted((ROOT/'records').glob('scan*.json')):
    r=json.loads(p.read_text()); rows=[]
    for row in r.get('notation',[]):
        title,tex,policy=row
        if title=='Finite-field symbol with doubled vertical stem':
            tex=r'\mathbb F_q'; policy='Doubled upright is represented by blackboard bold; visually reconciled with scans 008–009 and 030–032.'
        elif title=='Structure sheaf, looped capital O':
            tex=r'\mathcal O_S, \mathcal O_X'; policy='Use only for the ununderlined looped glyphs, as in 015 margin and 022 opening; a separate underbar is represented explicitly elsewhere.'
        elif title=='Finite field and prime field':
            tex=r'\mathbb F_q,\mathbb Z/p\mathbb Z'; policy='Doubled strokes checked across 007–009, 012 and 017; not substituted for ordinary sheaf F.'
        elif title=='Underlined structure sheaf in blue ink':
            tex=r'\underline O_X'; policy='Distinct lower stroke retained; ununderlined local-ring O in 021 is O, while the last O in 020 remains uncertain.'
        elif title=='Typed relation arguments':
            tex=r'R\{x,y\unsure{\{|\}}'; policy='The terminal typewritten brace resembles an opening brace; the visual ambiguity is retained, not normalized.'
        rows.append([title,tex,policy])
    r['notation']=rows
    p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')

rebuild()
with (ROOT/'progress.log').open('a') as f:
    f.write(f'notation and inventory reconciled {utc()} from the scans only; no context opened\n')
