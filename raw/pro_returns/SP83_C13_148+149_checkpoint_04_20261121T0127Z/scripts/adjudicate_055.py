from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan055'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B01':'The upper number is 11 and the item is 3). The cancelled Gommage is followed by a raised Bouchage de trous, ou and raised quotation ticks around gommage. In both de groups the low e finishes before the next word, without a separate s hook; the final preposition has the same de form, not a closed du. The terminal point after recollement is present.',
'B03':'The two lower looped l indices, prime on the first A, pi-zero, boundary sign and isomorphism agree. The l/ell spelling is a typographical choice for the same cursive letter. The parenthetical extends beyond the exact rectangle and is not reconstructed from that missing area.',
'B04':'The singular du graphe agrees. After consiste the compact sign consists of separated upper and lower marks, so à/colon is made explicit. The group after correspondantes has a low a, narrow v, e and open terminal c, rather than sans. Bien follows unchanged.',
'B05':'The little preposition has a low a with a u turn; dessous would require an additional o before the u in the following word, which is not present. Dessus is retained without hyphen. Mais is crossed. After the t in restent there is a low open e, then n and final t, not an a bowl. A small terminal point is visible at the extreme right edge.',
'B06':'A long horizontal stroke runs from left of the isolated sign across its central form and upper right curve. The old identification as cancelled 4) remains plausible but uncertain; the curve is not omitted, and the sign is not silently made a secure live item number.',
'B07':'The three heading words have no separate final s hooks; the singular Gommage simultané mixte is retained. The small crossed ou remains doubtful. The continuation has the p/d/t pattern of correspondant; its following compact à/colon is now explicit. The raised old A-prime union R-prime is separately crossed, beside its live R-prime union Sigma-prime replacement. The upper horizontal of each Sigma belongs to that capital, not an additional overbar. The lower struck word beneath the raised ambient set has the d/e/s ending. Physical revision scopes are retained.',
'B08':'The upper replacement et telle sits above a crossed q-like group; puis lacks a secure i-dot and is not preferred. The overwritten initial group before A union R could be the first de or a Sigma-plus-union unit, so that alternative is added without resolving it. In the containment formula the connector has a sharply pointed apex and two descending legs: wedge is now the literal leading reading, with intersection retained as an alternative. The expected set-intersection meaning is not used to erase the pointed form. The lower cancelled phrase begins a separate short word then ens. with no secure accented réun. sequence. The insertion covers que and the formula.',
'B09':'The upper Sigma again has its own detached top bar, without a second accent. The mark after au consists of two horizontal strokes, so the literal equality sign is retained instead of spelling même. Both primes in the raised R-prime union A-prime and the later vertical restriction bar are visible. The comma joined to the old cancellation remains doubtful.',
'B10':'The upper phrase has the plural des graphes pondérés endings. Enlever has the looped l and subsequent v/e/r run, without the x/c group required by exclure. The single overworked article-like group remains cancelled les versus live/overwritten la; no separate la is supplied on the next line. Above it de vector R has an arrow shaft and pointed right end, not a separate prime; the later vector R-prime does carry a distinct prime. The insertion placement is retained.',
'B11':'The clear A has a separate prime. Its small lower group is overworked, with two descending parts and a thick crossing/retracing through the middle. Neither a complete prop/reg abbreviation nor a secure live ell can be established. The first doubtful cancelled pq remains; aussi bien libres que liées and the following weights sentence agree.',
'B12':'The annotation has the upper bar and lower bowl of 5, then the open angled 4 with descending right leg. The mspage wrapper records the same folio 54.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={
'B04':[('consiste à gommer',r'consiste \unsure{à|:} gommer')],
'B07':[('correspondant à une',r'correspondant \unsure{à|:} une')],
'B08':[(r'\unsure{de} $A\amalg R$',r'\unsure{de|$\Sigma\amalg$} $A\amalg R$'),(r'R\cap\Sigma',r'R\unsure{\wedge|\cap}\Sigma')]}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,rs in repls.items():
 v=C[b]['first']
 for a,z in rs: assert a in v and a in s,(b,a);v=v.replace(a,z);s=s.replace(a,z)
 D[b].update(choice='reading',reading=v)
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
for x in r['changes']:
 if x['id']==p+'-18':x.update(final=r'\unsure{de|$\Sigma\amalg$}',evidence=E['B08'],crop=f'crops/{p}_second_B08.png',box=boxes['B08'])
 if x['id']==p+'-20':x.update(final=r"\inserted{que $R'\supset R\unsure{\wedge|\cap}\Sigma'$}",diff_c=True,diff_h=True,kind='misread symbol or index',error_kind='Symbols and indices',evidence=E['B08'],crop=f'crops/{p}_second_B08.png',box=boxes['B08'],confidence='medium',consequential=True)
for x in r['doubts']:
 if x['place']=='Cancelled preposition and A union R':x.update(reading=r'\deleted{\unsure{de|$\Sigma\amalg$} $A\amalg R$}',alternatives='de; Sigma union; overwritten group unresolved',reason=E['B08'])
for place,reading,alts,b in [('After consiste in first graph paragraph',r'\unsure{à|:}','à; colon','B04'),('After correspondant in mixed operation',r'\unsure{à|:}','à; colon','B07'),('Connector in inserted containment formula',r"R'\supset R\unsure{\wedge|\cap}\Sigma'",'wedge; angular intersection','B08')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=E[b]))
r['notes'].append(dict(id=p+'-N-audit',text='The independent audit retains the singular mixed-operation heading, literal equality shorthand, unbarred capital Sigma forms, the insertion of de vector R without a prime, and the uncertain cancelled A-prime subscript. In the containment condition the connector is sharply pointed: wedge is the leading literal reading with cap as an alternative; the intersection interpretation recorded in N02 remains a mathematical reading of that source condition, not permission to round the written sign. The heavily overwritten group before A union R also admits Sigma union besides de. Two compact à/colon forms remain open.'))
r.setdefault('hand',[])
# Existing per-page hand entries are a list under handwriting; add through the established key below if present.
hkey=next((k for k in ('hand_log','handwriting','hand') if isinstance(r.get(k),list) and (r.get(k) or k=='hand')), 'hand')
# Store the local observation separately for the consolidated consistency review.
r['audit_notation_observation']={'symbol':r'\unsure{\wedge|\cap}','place':'inserted R-prime containment formula','observation':'Sharp apex with two straight descending legs; cap is the contextual interpretation, retained as an alternative rather than imposed on the literal shape.','scope':'single connector on scan055','witnesses':'C and H both use cap.'}
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json'}
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
