from pathlib import Path
import csv,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan064'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='dc7cdca14936cec33585fe73c5460eb094685121a2bfd596bc4e470b00618da7'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B05':'The lower cancelled group has a low u/n run and an e-like final turn. The heavy strike hides enough of the interiors that une is now retained with avec as an alternative. The raised en and the long l of liaison are distinct. This is a certainty change, not a newly counted word correction.',
'B07':'After the two tall l loops of celle, the live article has a d ascender, e loop and a final pointed downward turn supporting des. The following low group is under the strike; une remains primary, with des unresolved. No grammatical correction to du is made.',
'B08':'The whole tuple and the raised Pi-one expression were viewed. The middle glyph has a lower horizontal base and angular return, like the recurring Sigma, rather than an independently clear R leg. Its short upper decoration and the bracket overlap, so tilde-Sigma/plain-Sigma remain doubtful. The low article beneath the leader is compatible with the existing des.',
'B09':'The raised condition was also viewed in a boundary extension containing its complete glyph. It has a small oval crossed by a long oblique stem, retained as the manuscript phi-shaped empty-set sign. The abbreviation has a full-height p and small raised ts, followed by a hyphen. A long opening curve before en is visible and is restored as the opening parenthesis. The insertion leader extends to the right above this curve.',
'B11':'The two l loops of nouvelle are followed by one e exit. Operation has its p descender, accent, t stem and compressed ion ending. Neither word has a distinct added final s before the large closing parenthesis, so the singular reading remains.',
'B12':'Two adjacent tall strokes joined by a crossbar and a separate low e give tte, not la/de. The raised representation word is readable. The old lower word is heavily crossed; its reconstitution proposal remains under doubt rather than being replaced by an entirely illegible token.',
'B13':'The main crop shows par with a p descender and low a/r, then the low e/n/s abbreviation, followed by f, two dotted i strokes and the nis ending of finis. These are not pour une fois. A boundary extension shows the opening d loop and low u run; no separate apostrophe is visible. The existing du groupoide par ens finis is retained.',
'B14':'An opening square bracket precedes the raised crowded word. Its tall f-like stroke and dotted continuation admit definissant/definition, and the last short group admits un/du. A second, thinner curved stroke beside the insertion leader precedes the baseline d-apostrophe-un; the opening parenthesis is restored, while no invented closing square bracket is added.',
'B15':'The singular revetement has a short accent stroke above e; the conventional French circumflex is retained rather than adding an accent-shape doubt. X-prime is raised. The d before X has a long terminal exit whose hook may contain s, so de/des is not resolved on this crop.',
'B16':'The opening article has a looped d followed by a low u. Groupoide ends in a d ascender and e exit without an independent s. The cancelled category remains too overworked to resolve. S has the ordinary two curved turns, whereas T has a looped head; the calligraphic-S wrapper is not a different source reading.',
'B17':'The formula shows S with subscript 2, loop-headed T and subscripts 0,3. The S-versus-calligraphic-S distinction is editorial styling only; the established source reading is retained.',
'B18':'The rotated whole margin and existing enlarged middle crop were viewed. After ici are two low joined strokes ne; the next line begins a long j descender followed by oue and then the low aucun group. The following live word has an accent over o and a tall l: role, not vide. A preceding old role-like group is crossed and remains doubtful. Autant is readable, but bien/dire/donc and the short phrase before mettre remain uncertain. The next lines retain mettre dans les and a c-opening cas/corps proposal. The lower preposition before the category has a low s/u/r run without a tall d and now reads sur. The two categories and au lieu de survive; neighbouring large main-line writing is not imported into this margin. The upper Sigma decoration may be a flattened tilde or bar and is not resolved.',
'B19':'The lower isolated folio has a closed-loop 6 and the two lobes of 3. Both readings are 63; mspage and margin differ only in editorial wrapper.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={
'B05':[(r'\deleted{une}',r'\deleted{\unsure{une|avec}}')],
'B09':[(r'} en tant que',r'} (en tant que')],
'B14':[(r'\inserted{[\unsure{définissant un}} d\'un',r'\inserted{[\unsure{définissant|définition} \unsure{un|du}} (d\'un')],
}
repls['B14']=[("\\inserted{[\\unsure{définissant un}} d'un","\\inserted{[\\unsure{définissant|définition} \\unsure{un|du}} (d'un")]
margin=r'\margin{$\unsure{\widetilde{\Sigma}|\overline{\Sigma}|\Sigma}$ ici ne joue aucun \deleted{\unsure{rôle|vide}} rôle, autant \unsure{bien|dire|donc} \unsure{pour les|pour se} mettre dans les \unsure{cas|corps} i.e. travailler sur $S\mathcal T_{\mathrm{top}}^\pm$ au lieu de $S\mathcal TD_{\mathrm{top}}^\pm$}'
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,rs in repls.items():
 v=C[b]['first']
 for a,z in rs:
  assert a in v and a in s,(b,a);v=v.replace(a,z);s=s.replace(a,z)
 D[b].update(choice='reading',reading=v)
assert C['B18']['first'] in s;s=s.replace(C['B18']['first'],margin);D['B18'].update(choice='reading',reading=margin)
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
def update(n,b,**kw):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],**kw)
update(4,'B05',final=r'\deleted{\unsure{une|avec}} \inserted{en} liaison',confidence='medium')
for n,b in ((6,'B07'),(7,'B08'),(8,'B09'),(9,'B09'),(10,'B09'),(14,'B11'),(15,'B12'),(16,'B12'),(17,'B12'),(18,'B13'),(20,'B15'),(21,'B15'),(22,'B15'),(23,'B16'),(24,'B16'),(25,'B16'),(35,'B19')):update(n,b)
update(11,'B09',final=D['B09']['reading'])
update(19,'B14',final=D['B14']['reading'],confidence='low')
update(26,'B18',final=r'$\unsure{\widetilde{\Sigma}|\overline{\Sigma}|\Sigma}$')
update(27,'B18',place='Marginal note, ne joue aucun',final='ne joue aucun',diff_c=True,confidence='high',consequential=True)
update(28,'B18',place='Marginal note, cancelled first rôle',final=r'\deleted{\unsure{rôle|vide}}',diff_c=True,confidence='low')
update(29,'B18',place='Marginal note, live rôle',final='rôle',diff_c=True,confidence='high')
update(30,'B18',final=r'autant \unsure{bien|dire|donc}',confidence='low')
update(31,'B18')
update(32,'B18',final=r'\unsure{cas|corps}')
update(33,'B18',final=r'i.e. travailler sur $S\mathcal T_{\mathrm{top}}^\pm$ au lieu de $S\mathcal TD_{\mathrm{top}}^\pm$',diff_c=True,confidence='medium')
update(34,'B18')
for x in r['decisions']:
 if x['id']=='M0776':x.update(evidence=E['B14'],crop=f'crops/{p}_second_B14.png',box=boxes['B14'])
 if x['id']=='M0777':x.update(reading=r'\unsure{définissant|définition} \unsure{un|du}',evidence=E['B14'],crop=f'crops/{p}_second_B14.png',box=boxes['B14'],confidence='low')
 if x['id']=='M0778':x.update(reading=r'autant \unsure{bien|dire|donc}',evidence=E['B18'],crop=f'crops/{p}_second_B18.png',box=boxes['B18'])
 if x['id']=='M0779':x.update(evidence=E['B18'],crop=f'crops/{p}_second_B18.png',box=boxes['B18'])
 if x['id']=='M0780':x.update(reading=r'\unsure{cas|corps}',evidence=E['B18'],crop=f'crops/{p}_second_B18.png',box=boxes['B18'])
for x in r['doubts']:
 if x['place']=='Raised covering phrase':x.update(reading=r'\inserted{[\unsure{définissant|définition} \unsure{un|du}}',alternatives='définissant/définition; un/du',reason=E['B14'],confidence='low')
 if x['place']=='Marginal opening sign':x.update(reading=r'$\unsure{\widetilde{\Sigma}|\overline{\Sigma}|\Sigma}$',alternatives='tilde Sigma; barred Sigma; plain Sigma',reason=E['B18'])
 if x['place']=='Marginal cancelled first vide':x.update(place='Marginal cancelled first rôle',reading=r'\deleted{\unsure{rôle|vide}}',alternatives='rôle; vide',reason=E['B18'])
 if x['place']=='Margin, word after autant':x.update(reading=r'\unsure{bien|dire|donc}',alternatives='bien; dire; donc',reason=E['B18'])
 if x['place']=='Margin, short phrase before mettre':x.update(reason=E['B18'])
 if x['place']=='Margin, short word before i.e.':x.update(reading=r'\unsure{cas|corps}',alternatives='cas; corps',reason=E['B18'])
r['doubts'].append(dict(place='Cancelled word before liaison',reading=r'\deleted{\unsure{une|avec}}',alternatives='une; avec',confidence='low',reason=E['B05']))
r['notes'].append(dict(id=p+'-N-audit',text='The independent reading exposed a material error in the margin: the ink says that the Sigma datum ne joue aucun role, not that it est formellement vide. The live role is clear; its cancelled predecessor and the compressed following phrase remain doubtful. This affects the interpretation of why the author proposes working in S T-top instead of S T D-top, but it is not a proof of an equivalence. Opening parentheses before en tant que and d\'un are restored after separating their curves from the insertion leaders. The abbreviated tte and par ens finis are confirmed from the strokes, as are the singular nouvelle operation and groupoide. The phi-shaped empty-set glyph remains as written. All thirteen unequal boxes were viewed after the complete independent TSV was frozen.'))
extra=[f'crops/{p}_second_main_nonempty_formula.png',f'crops/{p}_second_main_representation_prefix.png',f'crops/{p}_margin_middle.png']
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json','additional_existing_crops_viewed':extra}
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
