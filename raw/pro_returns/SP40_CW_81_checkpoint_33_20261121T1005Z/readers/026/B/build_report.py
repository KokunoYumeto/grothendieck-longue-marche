from pathlib import Path
import json,re,hashlib
from datetime import datetime,timezone
P=Path(__file__).resolve().parent; BASE=P.parents[3]
C=(BASE/'packets/026/C.tex').read_text(); H=(BASE/'packets/026/H.tex').read_text(); CD=(BASE/'packets/026/C_doubts.txt').read_text()
G=json.loads((P/'graphic_records.json').read_text()); GM={g['id']:g for g in G}
crops=json.loads((P/'crop_plan.json').read_text()); CP={x['path'].split('/')[1].split('.')[0]:x for x in crops}
start='2026-11-21 07:37:10 UTC'
D=[]
def diff(id,loc,c,h,reading,evidence,kind='other',dc=False,dh=False,status=None,crop=None,bbox=None,confidence='medium',source_row=None,**kw):
 d={'id':id,'location':loc,'C':c,'H':h,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':status,'readers_crop':('crops/'+crop+'.png') if crop else None,'bbox':bbox,'source_row':source_row}
 d.update(kw); D.append(d); return d

# Actual C uncertainty rows, in their original source order. All other source table sections stay separate.
sec=CD.split('## Doubtful readings\n',1)[1].split('\n## Slips kept as written',1)[0]
rawrows=[l for l in sec.splitlines() if l.startswith('| 26 |')]
rows=[]
for i,line in enumerate(rawrows,1):
 fields=[f.strip() for f in line.strip('|').split('|')]
 rows.append({'source_row_id':f'C026-R{i:02d}','source_row_number':i,'source_file':'packets/026/C_doubts.txt','source_section':'Doubtful readings','raw_source_row':line,'original_columns':dict(zip(['scan','location','reading','other_readings','confidence','evidence','contextual_preference'],fields))})
assert len(rows)==15
R={r['source_row_id']:r for r in rows}

def row(n,parts,status='retained'):
 r=R[f'C026-R{n:02d}']; r['local_parts']=parts; r['aggregate_status']=status

def part(id,loc,primary,alts,crop,status='retained',graphic=None,hand='his hand',role='glyph reading',attachment='as written',confidence='low',**kw):
 p={'id':id,'location':loc,'primary':primary,'alternatives':alts,'complete_candidates':[primary]+alts,'crop':'crops/'+crop+'.png','status':status,'graphic_id':graphic,'hand':hand,'role':role,'attachment':attachment,'confidence':confidence};p.update(kw);return p

row(1,[part('R01a','opening family after membership',r'\mathcal E',[r'\mathscr E',r'\varepsilon'],'01_family',graphic='B026-EFAM',confidence='medium')])
row(2,[
 part('R02a','second inserted Sigma lower dark predecessor',r'\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha}',[],'04_interlinear',graphic='B026-S04',role='predecessor glyph qualified; deletion retained'),
 part('R02b','third inserted Sigma upper dark predecessor',r'\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,\circ}',[r'\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,0}',r'\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,o}'],'04_interlinear',graphic='B026-S05',role='upper predecessor qualified independently of the lower predecessor and ring'),
 part('R02c','third inserted Sigma lower dark predecessor',r'\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,\circ}',[r'\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,0}',r'\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,o}'],'04_interlinear',graphic='B026-S05',role='lower predecessor qualified independently of the upper predecessor and ring'),
 part('R02d','following si les Sigma lower dark mark',r'\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha}',[r'\Sigma_{\unsure{\alpha}}^{\alpha}'],'05_si_condition',graphic='B026-S07',role='alpha candidate retained; newly qualified cancelled/live lower-index state')])
row(3,[part('R03a','cancelled group after connexes',r'\deleted{\Sigma_\alpha}',[r'\deleted{les}'],'04_interlinear',graphic='B026-S06',role='complete cancelled group')])
row(4,[part('R04a','cancelled word after on conclut',r'\deleted{aussitôt}',[r'\deleted{aussitot}'],'06_connexe_correction',graphic='B026-GAUSS',role='whole word with accent uncertainty',confidence='medium')])
row(5,[part('R05a','crossed label above marginal connector',r'\deleted{E}',[r'\deleted{B}',r'\deleted{\Sigma}'],'07_margin_diagram',graphic='B026-DIAG',role='complete crossed glyph')])
row(6,[part('R06a','tail at lower marginal E',r'E_\alpha',['E with hooked lower-arm return and no subscript'],'07_margin_diagram',graphic='B026-DIAG',role='shared tail allocation: lower alpha or E return',attachment='one connected lower-right stroke, drawn once')])
row(7,[part('R07a','last Sigma superscript in parenthesis',r'\Sigma^{-,\circ}',[r'\Sigma^{\alpha,\circ}',r'\Sigma^{-\alpha,\circ}',r'\Sigma^{-,0}',r'\Sigma^{\alpha,0}',r'\Sigma^{-\alpha,0}',r'\Sigma^{-,o}',r'\Sigma^{\alpha,o}',r'\Sigma^{-\alpha,o}'],'09_parenthesis_end',graphic='B026-S14',role='complete superscript with independent comma after formula')])
row(8,[part('R08a','deleted word after the two pairs',r'\deleted{distinctes}',[],'10_pairs_correction',status='resolved',graphic='B026-GPAIRS',role='whole cancelled word',confidence='medium')],status='resolved')
row(9,[part('R09a','underlined lower adjective','non panachées',['non penchées','non parallèles','non panachees','non penchees','non paralleles'],'11_adjective',graphic='B026-GADJ',role='complete phrase with word and accent alternatives')])
row(10,[part('R10a','struck signs after first lower Sigma2minus',r'\deleted{\ne\varnothing}',[],'14_first_bottom_row',status='resolved',graphic='B026-GNEDEL',role='complete cancelled sign pair',confidence='medium')],status='resolved')
row(11,[part('R11a','second explanatory equality label','ie',['i.e.','i.e'],'15_second_bottom_row',role='complete label; punctuation unresolved',confidence='medium')])
row(12,[part('R12a','relation in si les Sigma connexes et E ... emptyset',r'\ne',['+'],'05_si_condition',graphic='B026-REL1',role='complete three-run relation',confidence='medium')])
row(13,[part('R13a','second pair left delimiter','[',['('],'10_pairs_correction',graphic='B026-DELIM2',role='complete delimiter',confidence='medium')])
row(14,[part('R14a','first lower inclusion cluster',r'\subset',[r'\deleted{\cap}\subset'],'14_first_bottom_row',graphic='B026-INCL1',role='complete old/live relation states',confidence='medium')])
ringlocs=[('S05','inserted equation third Sigma','04_interlinear'),('S08','cancelled les Sigma connexes','06_connexe_correction'),('S09','main barred conclusion','08_barred_formulas'),('S10','first parenthetical barred term','08_barred_formulas'),('S11','parenthetical right barred term','08_barred_formulas'),('S12','right unbarred difference term','08_barred_formulas'),('S13','et Sigma ne peut','09_parenthesis_end'),('S14','car Sigma est un ouvert','09_parenthesis_end')]
row(15,[part('R15'+str(i+1),loc,r'\circ',['0','o'],crop,graphic='B026-'+sid,role='raised ring, locally inspected recurrence',confidence='medium',first_occurrence_printing=(i==0)) for i,(sid,loc,crop) in enumerate(ringlocs)])

# Source-row resolution/retention records remain separate from additional local geometric records.
for i,r in enumerate(rows,1):
 ps=r['local_parts']; primary='; '.join(p['primary'] for p in ps)
 changed=i in [8,10,11,13,14,15] or i==2
 h_by_row={1:r'\omega (note: \omega or \varepsilon)',2:r'\Sigma^\alpha et \Sigma^\alpha\smallsetminus E=\Sigma^{\alpha,0}; later \Sigma^\alpha',3:r'\ill{}',4:r'\struck{aussitôt}',5:r'\struck{\ill{}} / un signe biffé',6:'E',7:r'\Sigma^{\alpha,0}',8:r'\struck{distinctes}',9:'non parallèles',10:r'note: un « \neq\emptyset » biffé',11:'i.e.',12:r'\neq',13:r'\{',14:r'\subset',15:'0'}
 hd=i in [1,2,3,5,6,7,9,11,13,15]
 diff(f'B026-R{i:02d}',r['original_columns']['location'],r['raw_source_row'],h_by_row[i],primary,'; '.join(p['role'] for p in ps)+'. Source uncertainty retained unless expressly resolved; literal shapes remain in the referenced graphical groups.',dc=changed,dh=hd,status=r['aggregate_status'],crop=ps[0]['crop'].split('/')[1][:-4],bbox=CP[ps[0]['crop'].split('/')[1][:-4]]['bbox'],source_row=r['source_row_id'],confidence='medium' if i in [8,10,11,12,13,14,15] else 'low',local_parts=ps,qualified_difference=hd and i not in [2,3,13],count_scope='one original C row; local scopes retained separately',marked_in_H=(i in [1,3,5]))

# Additional witness comparisons; literal source quotations are kept separate from the selected reading.
diff('B026-L01','opening underlined definition','décomposition binaire','disposition binaire','décomposition binaire','The long compound includes the initial dé-, medial com and the following position strokes; the underlined span is visible on half a.',kind='misread word',dh=True,bbox=[870,115,1400,190],confidence='high')
diff('B026-L02','second ens abbreviation','un ens de deux',r'un ens.\ de deux','un ens de deux','No terminal point follows the second ens on half a; the first ens. retains its visible point.',kind='other',dh=True,bbox=[440,230,760,277],confidence='high')
diff('B026-L03','opening family first Sigma',r'\Sigma_\alpha^\alpha',r'\Sigma^\alpha',r'\Sigma_\alpha^\alpha','A separate upper alpha and a lower looped alpha both survive beside the first Sigma.',kind='omission',dh=True,crop='01_family',bbox=[600,288,677,346],confidence='high')
diff('B026-L04','topological phrase',"on s'intéresse au cas où les",r'on \uncertain{suppose} \ill{} \ill{} que',"on s'intéresse au cas où les",'The s apostrophe, tall t, reduced intéresse, au cas and the accented où are visible in the complete narrow phrase crop; les stands above the following line.',kind='readable ink left as \\ill{}',dh=True,crop='02_interest',bbox=[620,705,1560,801],confidence='high',count_scope='one contiguous H misread/placeholder phrase',marked_in_H=True)
diff('B026-L05','word hémisphères and preceding les','les hémisphères',r'\struck{hémisphères} les','les hémisphères primary; les deleted hémisphères alternative','A short transverse run crosses the initial looped h; no full-word crossing is established. The live primary and full-word cancellation alternative are retained, with les before the word.',kind='deletion state (struck given live or live given struck)',dc=True,dh=True,crop='03_hemispheres',bbox=[280,851,655,937],confidence='low',qualified_difference=True,complete_candidates=['les hémisphères',r'les \deleted{hémisphères}'],graphic_id='B026-HSTART')
diff('B026-L06','first Sigma in raised inserted equation',r'\Sigma_\alpha^\alpha',r'\Sigma^\alpha',r'\Sigma_\alpha^\alpha','The first inserted Sigma has independently visible upper and lower alphas; this is outside the dark-predecessor scope of original row R02.',kind='omission',dh=True,crop='04_interlinear',bbox=[671,890,752,942],confidence='high')
diff('B026-L07','et où after cancelled trailing group','et où',r'et \uncertain{si}','et où','The low rounded body and separate upper mark support où at this physical word.',kind='misread word',dh=True,crop='04_interlinear',bbox=[1165,927,1357,974],confidence='high')
diff('B026-L08','X connexe replacement and second si correction',r'si \deleted{les $\Sigma_\alpha^{\alpha,0}$ connexes}, \inserted{$X$ connexe, \deleted{et}}',r'\struck{\ill{}} si \struck{les $\Sigma^{\alpha,0}$ connexes}',r'si \deleted{les $\Sigma_\alpha^{\alpha,\circ}$ connexes}, \inserted{$X$ connexe, \deleted{et}}','Raised X connexe, is legible above the crossed lower clause; et has its own crossing. The lower alpha in the old Sigma is visible. The long curved upper guide and lower strike are separately represented.',kind='insertion or placement',dh=True,crop='06_connexe_correction',bbox=[548,1057,1125,1194],confidence='high',count_scope='one full correction cluster; original ring qualification recorded under R15',marked_in_H=True,graphic_id='B026-GCONN')
diff('B026-L09','complete parenthetical ending',r'et $\Sigma^{\alpha,0}$ ne peut être à la fois ouvert et fermé car $\Sigma^{\unsure{-,0|\alpha,0|-\alpha,0}}$, est un ouvert $\ne\varnothing$ et $\ne X$',r'et \uncertain{si} $\Sigma^{\alpha,0}$ une partie à la fois ouverte et fermée $\neq\emptyset$ et $\neq X$) / \uncertain{car} $\Sigma^{\alpha,0}$ est un \uncertain{ouvert} \ill{}',r'et $\Sigma^{\alpha,\circ}$ ne peut être [à|:] la fois ouvert et fermé car $\Sigma^{-,\circ|\alpha,\circ|-\alpha,\circ}$, est un ouvert $\ne\varnothing$ et $\ne X$)','The continuous two-line ink reads ne peut être, the two-mark à/colon locus, and singular ouvert/fermé; the final car clause, its low comma, both inequalities and closing parenthesis belong together. The report retains all superscript and ring alternatives separately.',kind='misread word',dc=True,dh=True,crop='09_parenthesis_end',bbox=[270,1285,1600,1550],confidence='medium',count_scope='one compound H parenthetical reconstruction; independent local source-row details retained',marked_in_H=True)
diff('B026-L10','two marks before la fois','à','à','à primary; colon alternative','Two vertically separated narrow marks are visible; the body of a letter is reduced to those marks. B026-ATWO preserves their positions and both readings.',kind='other',dc=True,dh=False,crop='09_parenthesis_end',bbox=[905,1349,930,1383],confidence='low',graphic_id='B026-ATWO')
diff('B026-L11','lower paragraph opening','deux décompositions binaires','deux dispositions binaires','deux décompositions binaires','The long word includes the décom- sequence in the lower opening line, independently of the opening definition.',kind='misread word',dh=True,bbox=[969,1533,1359,1620],confidence='high')
diff('B026-L12','de X after crossed distinctes',r'\inserted{de $X$,}','de $X$,',r'\inserted{de $X$,}','The words stand below the pairs and crossed word, with a long bent guide rising towards the corrected position.',kind='insertion or placement',dh=True,crop='10_pairs_correction',bbox=[225,1682,595,1755],confidence='high',graphic_id='B026-GPAIRS')
diff('B026-L13','lower raised distinctes clause',r'si \inserted{elles sont \uline{distinctes}, et si} on peut trouver',r'\add{si elles sont \emph{distinctes}, et} si on peut trouver',r'si \inserted{elles sont \uline{distinctes}, et si} on peut trouver','The first si is on the base line to the left; the raised clause begins elles and ends et si. Its curved guide and the separate underline under distinctes are preserved.',kind='insertion or placement',dh=True,crop='12_distinctes_insertion',bbox=[275,1685,1015,1886],confidence='high',graphic_id='B026-GDIST')
diff('B026-L14','introduction of final rows','on a alors','on a donc','on [a-shaped point] alors','The final word has the tall looped l and low following ors strokes, supporting alors. The intervening a-shaped point is qualified independently.',kind='misread word',dh=True,crop='14_first_bottom_row',bbox=[305,2078,587,2133],confidence='high')
diff('B026-L15','reduced a in on a alors','a','a','a primary; an uninterpreted point alternative','A small filled lozenge stands between on and alors. The source preserves its shape rather than supplying a normal printed a.',kind='other',dc=True,crop='14_first_bottom_row',bbox=[408,2098,429,2121],confidence='low',graphic_id='B026-ARED',complete_candidates=['on a alors','on [uninterpreted point] alors'])
diff('B026-L16','definition label over equals','def','déf','déf primary; def with a separate upper trace alternative','A small short upper slant is visible beside the e and before the tall f. Its attachment remains qualified; the complete def body and trace are drawn once.',kind='other',dc=True,dh=False,crop='16_final_row',bbox=[607,2244,648,2290],confidence='low',graphic_id='B026-DEF',complete_candidates=['déf','def plus detached upper trace'])

# One H parent count for the actual description of the marginal drawing.
diff('B026-HDIA','entire oblique marginal diagram',C[C.index('% margin note'):C.index('(car ')],H[H.index('\\marginal'):H.index('Considérons')],GM['B026-DIAG']['reading'],'The once-rotated crop supplies both filled vertices, the shallow connector, the crossed upper label, all lower formula strokes and a separate small dot below the connector.',kind='drawing or diagram',dc=True,dh=True,crop='07_margin_diagram',bbox=[38,950,265,1375],confidence='medium',graphic_id='B026-DIAG',count_scope='one H drawing-description replacement; variable local labels and point below are children')
for n in [5,6]:
 d=next(d for d in D if d['id']==f'B026-R{n:02d}');d['raw_diff_H_before_parent_count']=d['diff_H'];d['diff_H']=False;d['H_count_parent']='B026-HDIA'
# R07 is local to the complete parenthetical H cluster, whose precise source quotation is L09.
d=next(d for d in D if d['id']=='B026-R07'); d['raw_diff_H_before_parent_count']=d['diff_H'];d['diff_H']=False;d['H_count_parent']='B026-L09'

# Geometric omissions/additions and their exact ownership. Ordinary glyph-font substitutions are not counted.
for g in G:
 if g['id'].startswith('B026-S') and 'upper-run role retained' in g['role']:
  sid=g['id']; num=int(sid[-2:]); crop=g['crop']; crop=None if crop=='half_b' else crop
  diff(sid+'-HEAD',g['reading'],'ordinary Sigma body in local C expression','ordinary Sigma body in local H expression',g['reading']+' with its separate short head retained literally','The local crop/half shows a short upper run separated from the bent body. Its presence is firm; head/retrace versus independent-run role remains qualified locally. Each occurrence is mapped independently.',kind='drawing or diagram',dc=True,dh=True,crop=crop,bbox=g['bbox'],confidence='medium',graphic_id=sid,recurring_first_occurrence=(sid=='B026-S01'),candidate_specific_hand={'head/retrace':'his hand','independent upper run':'undetermined hand for that run; body and decorations his hand'})

for id,loc,why,dh in [
 ('GDE','above et plus','A curved diagonal insertion guide survives separately from the inserted de.',True),
 ('GEQ','raised equation and connexes','A long bent guide descends at the left of connexes; the corrected trailing group has two crossing paths.',True),
 ('GCONN','X connexe replacement','A curved upper guide and separate lower cancellation span the old clause; both endpoints remain.',True),
 ('GAUSS','cancelled aussitôt','The crossing follows a bent low path through the word.',False),
 ('GPAIRS','pairs and deleted distinctes','The two cancellation runs and the curved de X guide preserve their separate paths.',True),
 ('GADJ','non adjective','The observed underline begins under the latter part of non; the p descender crosses it and returns upward. The long p is drawn once before the six suffix candidates.',True),
 ('GDIST','distinctes insertion','The long bent guide and the short distinctes underline are separate strokes.',True),
 ('GQDESC',"qu'elles",'The long q descender is attached to qu’elles and reaches the raised insertion neighbourhood; it is not a second insertion guide.',True),
 ('CAP1','first display intersection','The angular arch and detached lower-right point are preserved as one relation group.',True),
 ('E1','first E in d’où expression','The detached upper curve remains beside the E body and index.',True),
 ('E2','second E in d’où expression','The second detached upper curve is recorded locally under the first printing qualifier.',True),
 ('REL1','E relation before emptyset','The short upper-right run, long middle run and slanted upright are drawn literally under the original relation doubt.',True),
 ('INCL1','first lower inclusion','The fuller relation contains the main C-shaped run, lower-left return and short internal stroke once.',False),
 ('GNEDEL','cancelled inequality pair','All visible crossing runs and the slashed oval remain in the one cancelled group.',False),
 ('NEFINAL','last inequality','The tiny detached point at the right of the lower run is preserved with its unresolved endpoint attachment.',True)
]:
 g=GM['B026-'+id]
 diff('B026-G-'+id,loc,'No separate literal component for this geometry','Description or ordinary mathematical/text form',g['reading'],why,kind='drawing or diagram',dc=True,dh=dh,crop=g['crop'],bbox=g['bbox'],confidence='medium',graphic_id=g['id'],physical_cluster='B026-'+id)

for id,loc in [('M02','under first parenthetical closure roof'),('M03','left of main barred conclusion'),('M04','below peut'),('M06','below first final-row intersection')]:
 g=GM['B026-'+id]
 diff('B026-OM-'+id,loc,'absent','absent',g['reading'],'The supported local graphical shape is retained; character, role, attachment, hand and surface origin remain unestablished.',kind='omission',dc=True,dh=True,crop=g['crop'],bbox=g['bbox'],confidence='low',graphic_id=g['id'],qualified_difference=True)
diff('B026-OM-M01','below marginal connector','absent','absent','one detached dark point','A compact round point stands below the connector, between its left endpoint and the crossed label; it remains separate from the connector.',kind='omission',dc=True,dh=False,crop='07_margin_diagram',bbox=[123,1247,132,1257],confidence='medium',graphic_id='B026-DIAG',H_count_parent='B026-HDIA',hand='undetermined hand',role='unestablished',attachment='unestablished')
diff('B026-OM-M05','below right end of adjective underline','absent','absent','two detached dark points','Two small points lie below the right end of the underline, separate from the adjective. No punctuation function is assigned.',kind='omission',dc=True,dh=True,crop='11_adjective',bbox=[1579,1677,1593,1693],confidence='medium',graphic_id='B026-GADJ',hand='undetermined hand',role='unestablished',attachment='unestablished')

# Literal witness anchors for geometric records, so prose descriptions never replace an original quoted form.
sanchor={1:(r'\Sigma_{\alpha}^{\alpha}',r'\Sigma^{\alpha}'),2:(r'\Sigma_{\alpha}',r'\Sigma_{\alpha}'),3:(r'\Sigma_{\alpha}^{\alpha}',r'\Sigma^{\alpha}'),4:(r'\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha}',r'\Sigma^{\alpha}'),5:(r'\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,\unsure{0|\circ|o}}',r'\Sigma^{\alpha,0}'),6:(r'\deleted{\unsure{$\Sigma_{\alpha}$|les}}',r'\ill{}'),7:(r'\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha}',r'\Sigma^{\alpha}'),8:(r'\deleted{les $\Sigma_{\alpha}^{\alpha,0}$ connexes}',r'\struck{les $\Sigma^{\alpha,0}$ connexes}'),9:(r'\overline{\Sigma^{\alpha,0}}',r'\overline{\Sigma^{\alpha,0}}'),10:(r'\overline{\Sigma^{\alpha,0}}',r'\overline{\Sigma^{\alpha,0}}'),11:(r'\overline{\Sigma^{\alpha,0}}',r'\overline{\Sigma^{\alpha,0}}'),12:(r'\Sigma^{\alpha,0}',r'\Sigma^{\alpha,0}'),13:(r'\Sigma^{\alpha,0}',r'\Sigma^{\alpha,0}'),14:(r'\Sigma^{\unsure{-,0|\alpha,0|-\alpha,0}}',r'\Sigma^{\alpha,0}')}
for num,index,sign in [(15,'1','+'),(16,'1','-'),(17,'2','+'),(18,'2','-'),(19,'1','+'),(20,'2','+'),(21,'1','+'),(22,'2','+'),(23,'1','+'),(24,'2','-'),(25,'1','+'),(26,'2','-'),(27,'1','+'),(28,'2','+'),(29,'1','-'),(30,'2','+'),(31,'1','-'),(32,'2','+'),(34,'1','-'),(35,'2','-'),(36,'1','-'),(37,'2','-')]:
 sanchor[num]=(r'\Sigma_'+index+'^{'+sign+'}',r'\Sigma_{'+index+'}^{'+sign+'}')
sanchor[33]=(r'\Sigma_{12}',r'\Sigma_{12}')
for d in D:
 if d['id'].endswith('-HEAD'):
  n=int(d['graphic_id'][-2:]);d['C'],d['H']=sanchor[n];d['C_anchor']=d['C'];d['H_anchor']=d['H']
  if n in [6]:d['raw_diff_H_before_parent_count']=d['diff_H'];d['diff_H']=False;d['H_count_parent']='B026-R03'
  if n in [14]:d['raw_diff_H_before_parent_count']=d['diff_H'];d['diff_H']=False;d['H_count_parent']='B026-L09'

anchors={
 'GDE':(r'\inserted{de}',r'\add{de}'),
 'GEQ':(r'\inserted{$\Sigma_{\alpha}^{\alpha}$ et',H[H.index('\\note{interligne'):H.index('\\uncertain{car}')]),
 'GCONN':(r'\inserted{$X$ connexe, \deleted{et}}',r'\struck{\ill{}} si \struck{les $\Sigma^{\alpha,0}$ connexes}'),
 'GAUSS':(r'\deleted{\unsure{aussitôt}}',r'\struck{aussitôt}'),
 'GPAIRS':(r'\deleted{\unsure{distinctes}} \inserted{de $X$,}',r'\struck{distinctes} de $X$,'),
 'GADJ':(r'\uline{non \unsure{panachées|penchées|parallèles}}',r'\emph{non parallèles}'),
 'GDIST':(r'\inserted{elles sont \uline{distinctes}, et si}',r'\add{si elles sont \emph{distinctes}, et}'),
 'GQDESC':("qu'elles","qu'elles"),'CAP1':(r'\cap',r'\cap'),'E1':('E_1','E_{1}'),'E2':('E_2','E_{2}'),
 'REL1':(r'\mathrel{\unsure{\ne|+}}',r'\neq'),
 'INCL1':(r'\mathrel{\unsure{\deleted{\cap}\subset|\subset}}',r'\subset'),
 'GNEDEL':(r'\deleted{\unsure{\ne\varnothing}}',r'un « $\neq\emptyset$ » biffé'),
 'NEFINAL':(r'\ne\varnothing',r'\neq\emptyset')}
for d in D:
 if d['id'].startswith('B026-G-'):
  key=d['id'][7:]; d['C'],d['H']=anchors[key]; d['C_anchor']=d['C'];d['H_anchor']=d['H']

# Explicit complete reader candidates, with the hand and role scope attached to each candidate.
candidate_records=[]
for g in G:
 id=g['id'];cs=list(g.get('candidates',[]))
 if id.startswith('B026-S'):
  n=int(id[-2:])
  semantic=g['reading']
  # The full actual local state receives each recurring role candidate; no candidate's local decorations are dropped.
  if n in [8,9,10,11,12,13]:
   cs=[]
   for ring in [r'\circ','0','o']:
    s=semantic.replace(r'\circ',ring)
    cs.append(s+' with detached head/retrace');cs.append(s+' with independent upper run')
  elif n==14:
   cs=[]
   for sign in ['-',r'\alpha',r'-\alpha']:
    for ring in [r'\circ','0','o']:
     for role in ['detached head/retrace','independent upper run']:
      cs.append(r'\Sigma^{'+sign+','+ring+'} with '+role)
  elif n==5:
   cs=[]
   for ring in [r'\circ','0','o']:
    for role in ['detached head/retrace','independent upper run']:
     cs.append(r'\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,'+ring+'} with '+role)
  elif n==4:
   cs=[r'\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha} with detached head/retrace',r'\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha} with independent upper run']
  elif n==6:
   cs=[r'\deleted{\Sigma_\alpha} with head/retrace',r'\deleted{\Sigma_\alpha} with independent upper run',r'\deleted{les}']
  elif n==7:
   cs=[r'\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha}',r'\Sigma_{\unsure{\alpha}}^{\alpha}']
 states=[]
 for c in cs:
  hand={'main':'his hand'}
  role=g.get('role','')
  attachment='within the complete source group at its fixed origin'
  if 'independent upper run' in c or 'independent upper curve' in c:
   hand['independent_upper_component']='undetermined hand';attachment='upper component preserved at observed position; semantic attachment unestablished'
  if id in ['B026-M02','B026-M03','B026-M04','B026-M06']:
   hand={'all':'undetermined hand'};attachment='unestablished; no character supplied'
  if id=='B026-ARED' and 'uninterpreted' in c:
   hand={'point':'undetermined hand'};role='point role unestablished';attachment='unestablished'
  if id=='B026-DEF' and c.startswith('def plus'):
   hand['upper_trace']='undetermined hand';attachment='word body firm; separate upper-trace attachment unresolved'
  states.append({'reading':c,'hand':hand,'role':role,'attachment':attachment,'insertion_state':'inserted' if id in ['B026-S03','B026-S04','B026-S05','B026-GDE','B026-GEQ','B026-GDIST'] else 'as described in complete source','cancellation_state':'contained in complete candidate; no chronology inferred'})
 candidate_records.append({'graphic_id':id,'selected_source_reading':g['reading'],'source_comment_candidates':g.get('candidates',[]),'complete_candidate_states':states,'printed_qualifier':g.get('qualifier_printed'), 'retained_later_qualification':id.startswith('B026-S') and id!='B026-S01' and 'upper-run role retained' in g['role']})
# Explicit special component scopes that coexist with main-writing hand in a single source group.
special_components=[
 {'id':'B026-M01','source_group':'B026-DIAG','reading':'one dark point below connector','hand':'undetermined hand','role':'unestablished','attachment':'unestablished','surface_origin':'unestablished'},
 {'id':'B026-M05','source_group':'B026-GADJ','reading':'two detached points below underline','hand':'undetermined hand','role':'unestablished','attachment':'unestablished','surface_origin':'unestablished'},
 {'id':'B026-CAP1-point','source_group':'B026-CAP1','states':[{'reading':'detached terminal point of cap','hand':'his hand','role':'terminal component','attachment':'cap'},{'reading':'independent point','hand':'undetermined hand','role':'unestablished','attachment':'unestablished'}]},
 {'id':'B026-NEFINAL-point','source_group':'B026-NEFINAL','states':[{'reading':'detached endpoint of lower relation run','hand':'his hand','role':'endpoint','attachment':'lower relation run'},{'reading':'independent adjacent point','hand':'undetermined hand','role':'unestablished','attachment':'unestablished'}]}
]

# Qualifier overlap and recurring-ring accounting are explicit.
for id,txt in {
 'B026-R01':"H's noted epsilon candidate remains a supported alternative; its omega primary is not selected. This is a qualified change of primary reading.",
 'B026-R07':"H's alpha,0 survives among the complete candidates. The circle/zero change is shared with original row R15 and creates no extra physical mark.",
 'B026-R09':"H's parallèles remains an explicit supported whole-word alternative; this row does not claim a conclusive H error.",
 'B026-R11':"H's i.e. remains an alternative; its endpoint punctuation is not conclusively rejected."
}.items():
 next(d for d in D if d['id']==id)['evidence']+=' '+txt
next(d for d in D if d['id']=='B026-R07')['diff_C']=True
next(d for d in D if d['id']=='B026-R07')['shared_ring_change_parent']='B026-R15'

inventory=[]
def inv(el,kind,pos,first,hand='his hand',bbox=None,**kw):
 z={'sheet_kind':'text','hand':hand,'element':el,'kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':'yes'}
 if bbox:z['bbox']=bbox
 z.update(kw);inventory.append(z)
inv('B026-T01','text','top, lines 1–2','Soit X un ens. Une décomposition binaire',[ ][0] if False else 'his hand',bbox=[275,115,1560,280])
inv('B026-U01','text','opening definition underline','single underline under décomposition binaire',bbox=[915,172,1395,183])
inv('B026-F01','display','family on its own line','(Sigma_alpha^alpha)_{alpha in script E}; (les hémisphères)',bbox=[580,278,1445,350])
inv('B026-T02','text','upper paragraph, réunion through topological clause','dont la réunion est X, et dont ...',bbox=[278,344,1638,810])
inv('B026-DEL01','deletion','first sentence, after et dont',"l'intersection",bbox=[1063,341,1342,380])
inv('B026-T03','text','middle upper, hemispheres and connexity clauses','les hémisphères ... le plus souvent ... si les Sigma connexes',bbox=[275,778,1640,1195])
inv('B026-DEL02','deletion','inserted equation, lower second Sigma','qualified lower alpha predecessor',bbox=[849,913,883,939],source_row='C026-R02',graphic_id='B026-S04')
inv('B026-DEL03','deletion','inserted equation, upper third Sigma','qualified upper alpha predecessor',bbox=[973,873,991,889],source_row='C026-R02',graphic_id='B026-S05')
inv('B026-DEL04','deletion','inserted equation, lower third Sigma','qualified lower alpha predecessor',bbox=[989,905,1022,928],source_row='C026-R02',graphic_id='B026-S05')
inv('B026-DEL05','deletion','after connexes','deleted Sigma_alpha / deleted les',bbox=[1050,935,1122,991],source_row='C026-R03',graphic_id='B026-S06')
inv('B026-DEL06','deletion','following si les Sigma','deleted/live qualified lower alpha',bbox=[846,1041,884,1074],source_row='C026-R02',graphic_id='B026-S07')
inv('B026-DEL07','deletion','old lower middle clause','les Sigma_alpha^(alpha,circle) connexes',bbox=[635,1095,1115,1174],graphic_id='B026-GCONN')
inv('B026-INS01','insertion','above cancelled middle clause','X connexe, deleted et',bbox=[595,1071,911,1113],graphic_id='B026-GCONN')
inv('B026-DEL08','deletion','end of raised middle replacement','et',bbox=[853,1070,910,1101],graphic_id='B026-GCONN')
inv('B026-T04','text','closure conclusion and parenthesis','que barred Sigma ... (car ... et ... car ...)',bbox=[278,1150,1647,1550])
inv('B026-T05','text','lower paragraph','Considérons deux décompositions binaires ...',bbox=[98,1530,1650,1943])
inv('B026-DEL09','deletion','after binary pairs','distinctes',bbox=[508,1627,699,1693],graphic_id='B026-GPAIRS')
inv('B026-INS02','insertion','below binary pairs','de X,',bbox=[276,1682,470,1747],graphic_id='B026-GPAIRS')
inv('B026-INS03','insertion','above on peut trouver','elles sont distinctes, et si',bbox=[370,1710,929,1789],graphic_id='B026-GDIST')
inv('B026-U02','text','lower insertion','single underline under distinctes',bbox=[562,1750,753,1775],graphic_id='B026-GDIST')
inv('B026-F02','display','first lower display','Sigma1+ cap Sigma2+ = emptyset (d’où E1 cap E2 = emptyset)',bbox=[646,1897,1635,2010])
inv('B026-T06','text','before final three rows','on a/point alors',bbox=[309,2083,586,2132])
inv('B026-F03','display','bottom, first row','Sigma1+ subset Sigma2-; i.e. equality',bbox=[648,2058,1492,2158])
inv('B026-F04','display','bottom, second row','Sigma2+ subset Sigma1-; ie/i.e./i.e equality',bbox=[641,2155,1483,2246])
inv('B026-F05','display','bottom, final row','Sigma12 definition, superset E1 cup E2, final nonemptiness',bbox=[528,2244,1440,2338])
for g in G:
 kind='drawing'; hand=g['hand']
 if g['id'] in ['B026-GDE','B026-GEQ','B026-GDIST']:kind='insertion'
 if g['id'] in ['B026-GAUSS','B026-GNEDEL']:kind='deletion'
 if g['id']=='B026-DIAG':kind='diagram'
 if g['id'] in ['B026-HSTART','B026-GADJ','B026-GQDESC']:kind='text'
 if g['id'].startswith('B026-M'):hand='undetermined hand'
 inv(g['id'],kind,'local group at full scan box '+str(g['bbox']),g['reading'],hand=hand,bbox=g['bbox'],source_group=g['id'],components=g.get('components',[]))
inv('B026-M01','drawing','below marginal connector','one detached point',hand='undetermined hand',bbox=[123,1247,132,1257],source_group='B026-DIAG')
inv('B026-M05','drawing','under lower adjective underline','two detached points',hand='undetermined hand',bbox=[1579,1677,1593,1693],source_group='B026-GADJ')
inv('B026-ARCHIVE','text','bottom left archive numeral','25, recorded only as archive-number comment',hand='undetermined hand',bbox=[35,2300,89,2343])
inventory.sort(key=lambda x:(x.get('bbox',[0,0])[1],x.get('bbox',[0,0])[0]))

notes={
 'page_content':'The sheet introduces a décomposition binaire and calls its parts hémisphères and their intersection équateur. It records closure/intersection expressions in the topological discussion. The lower paragraph names a relation between two decompositions with the qualified adjective panachées/penchées/parallèles and records the disjointness display, two inclusions, their explanatory equalities, and the final Sigma12 definition. These are descriptions of this manuscript’s written assertions.',
 'author_own_uncertainty':{'exact_words':[],'note':'No explicit verbal proof-reservation or authorial question mark was identified. Reader qualifications and crossed corrections are not attributed to the author as proof reservations.'},
 'title_date_page_counts':{'title':'none','date':'none','manuscript_page_number':'none','archive_number':'25','H_page':'25','our_scan':'26'},
 'mathematics_led_reading_decisions':'No mathematical proof check was performed. The repeated formulas guided attention to individual signs and indices, while each proposed reading comes from its local ink. The nonmatching second pair delimiter, the comma before est, the reduced two-mark à/colon candidate and every retained correction remain in the source.'}
notation=[{'location':g['bbox'],'id':g['id'],'proposed_LaTeX_or_graphic':g['reading'],'source_group':g['id'],'locally_retained_candidates':next(x['complete_candidate_states'] for x in candidate_records if x['graphic_id']==g['id']),'evidence_source':g['crop']} for g in G]
notation += [
 {'location':'opening first and second ens','proposed_LaTeX':'ens.; ens','evidence':'first stop visible, second absent on half a'},
 {'location':'first bottom equality','proposed_LaTeX':'i.e.','evidence':'upright i, its point, intervening separator and terminal point visible in crop14'},
 {'location':'second bottom equality','proposed_LaTeX':r'\unsure{ie|i.e.|i.e}','evidence':'reduced connected label; retained punctuation alternatives in crop15'},
 {'location':'quotation marks and clause dash','proposed_LaTeX':"``hémisphères''; ``équateur''; --",'evidence':'paired ticks and single long clause stroke on half a'}]
doubts=[]
for r in rows:
 for p in r['local_parts']:
  if p['status']=='retained':doubts.append({'location':p['location'],'reading':p['primary'],'alternatives':p['alternatives'],'confidence':p['confidence'],'reason':p['role'],'crop':p['crop'],'source_row':r['source_row_id'],'local_part':p['id']})
for cr in candidate_records:
 if len(cr['complete_candidate_states'])>1 or GM[cr['graphic_id']].get('qualifier_printed'):
  g=GM[cr['graphic_id']]
  doubts.append({'location':g['bbox'],'reading':cr['complete_candidate_states'][0]['reading'] if cr['complete_candidate_states'] else g['reading'],'alternatives':[s['reading'] for s in cr['complete_candidate_states'][1:]],'confidence':'low' if g['id'].startswith('B026-M') else 'medium','reason':g['role'],'crop':('crops/'+g['crop']+'.png') if g['crop']!='half_b' else None,'graphic_id':g['id'],'candidate_states':cr['complete_candidate_states']})

tex=(P/'reading.tex').read_text()
source_groups=[]
for g in G:
 fragment=g['literal_source']; count=tex.count(fragment)
 if count!=1:raise RuntimeError((g['id'],'literal count',count))
 pos=tex.index(fragment);end=pos+len(fragment)
 source_groups.append({**g,'start_char':pos,'end_char':end,'start_byte':len(tex[:pos].encode()),'end_byte':len(tex[:end].encode()),'source_sha256':hashlib.sha256(fragment.encode()).hexdigest(),'occurrences':count})
source_groups.sort(key=lambda x:x['start_char'])
bounds=sorted({0,len(tex)}|{z for g in source_groups for z in [g['start_char'],g['end_char']]})
partition=[]
for lo,hi in zip(bounds,bounds[1:]):
 partition.append({'start_char':lo,'end_char':hi,'source':tex[lo:hi],'owners':[g['id'] for g in source_groups if g['start_char']<=lo and hi<=g['end_char']]})
assert ''.join(x['source'] for x in partition)==tex
source_map={
 'scan':26,'reader':'B','reading_sha256':hashlib.sha256(tex.encode()).hexdigest(),'offset_convention':'zero-based, half-open character and UTF-8 byte offsets; source includes comments and qualifiers','source_groups':source_groups,'ordered_source_partition':partition,'exact_reconstruction_from_partition':True,
 'witness_sources':{'C':{'path':'packets/026/C.tex','sha256':hashlib.sha256(C.encode()).hexdigest(),'exact_source':C},'H':{'path':'packets/026/H.tex','sha256':hashlib.sha256(H.encode()).hexdigest(),'exact_source':H},'C_doubts':{'path':'packets/026/C_doubts.txt','sha256':hashlib.sha256(CD.encode()).hexdigest(),'exact_source':CD}},
 'original_C_rows':rows,'complete_candidate_records':candidate_records,'special_component_candidates':special_components,
 'literal_p_suffix_correspondence':{'literal_prefix':'p','suffixes':['anachées','enchées','arallèles','anachees','enchees','aralleles'],'complete_words':['panachées','penchées','parallèles','panachees','penchees','paralleles'],'map':'For each list position, concatenate the one drawn p with that suffix; the resulting complete word is recorded at the same position. No second printed p is present.'},
 'native_coordinate_note':'Each local drawing maps (u,v) to full-scan (x0+u,y0+v). Ordinary groups use x=.085 mm and y=-.085 mm. Diagram overlay preserves its separately declared rotated-crop units, x=.10 mm and y=-.10 mm, then +52-degree outer page orientation. Paths and fixed rectangles are manual approximations; their declarations do not claim metric or render verification.'}
(P/'source_map.json').write_text(json.dumps(source_map,ensure_ascii=False,indent=2)+'\n')
end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report={
 'scan':26,'reader':'B','start_utc':start,'end_utc':end,'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,'differences':D,'doubts':doubts,'inventory':inventory,'notes':notes,'notation':notation,'check_events':[],'crops':crops,'brief_feedback':'No missing convention required a pause. Complete reader candidate states, native source maps and inherited C compound scope are provided explicitly. Long ordinary-letter descenders that meet graphical guides retain their word ownership.',
 'C_uncertainty_source_rows':rows,'candidate_records':candidate_records,'special_component_candidates':special_components,
 'view_audit':json.loads((P/'view_audit.json').read_text()),'view_counts':{'whole_successful':1,'half_a_successful':1,'half_b_successful':1,'deep_crop_successful':17,'failed_image_deliveries':0,'total_successful':20,'reopened_decided_targets':0},
 'provenance':{'packet_metadata':json.loads((BASE/'packets/026/metadata.json').read_text()),'C_inventory_original':json.loads((BASE/'packets/026/C_inventory.json').read_text()),'C_doubt_actual_rows':15,'C_notation_rows_excluded_from_doubt_count':6,'C_spelling_rows_excluded_from_doubt_count':4,'H_status':'text','independence':'No other reader directories, root decisions or other-page images were opened. No delegation. No external text, OCR, text recognition, PDF extraction, compilation, rendering or installation.','administrative_geometry_checks':[{'input_full_size':[1694,2370],'input_half_size':[1694,1265],'map':'lower-half origin y=2370-1265','result':1105,'scope':'coordinate bookkeeping only'},{'map':'original crop -> optional PIL BICUBIC rotation -> LANCZOS resize -> autocontrast -> UnsharpMask','fixed_inputs_and_results':'crop_plan.json records each box, rotation, input and output size and filter values','scope':'image display preparation; no pixel-difference or image-alignment calculation'}],'source_reconstruction':{'partition_exact':True,'groups_exact_once':True,'reading_sha256':hashlib.sha256(tex.encode()).hexdigest()},'text_output_truncation':'Initial bulk source read was truncated; all required brief, packet, notation and convention text was subsequently read through bounded outputs. No image delivery was truncated or failed.','overlap_note':'Some tight crops include neighbouring previously viewed writing as context. Each named unresolved target has one planned enlargement; no decided target was reopened. Crop17 is a newly noticed pale-arc target clipped at crop08’s context boundary.','mathematical_check_scope':'Empty check_events is intentional: no theorem, proof or mathematical correspondence was checked.'}}
(P/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(D),'doubts':len(doubts),'inventory':len(inventory),'source_groups':len(source_groups),'C_rows':len(rows),'end_utc':end},indent=2))
