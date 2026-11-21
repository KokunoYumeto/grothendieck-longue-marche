"""Mechanical assembly for scan006. No images are opened and no ink is decided.
Only root-supplied decisions may set root_decided. The committed record is separate.
"""
from pathlib import Path
import copy,json,collections,re,hashlib
OUT=Path(__file__).resolve().parents[1]
READY_READERS=['A','B','C']
REPORTS={role:json.loads((OUT/'readers/006'/role/'report.json').read_text()) for role in READY_READERS}
INDEX={role:{x['id']:x for x in d['differences']} for role,d in REPORTS.items()}
MAP={f'{n:02d}':{'A':[f'006-A-{n:03d}'],'B':[],'C':[]} for n in range(1,57)}
B_ROWS=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[49],[11],[12,15,17],[13],[14],[16],[18],[19],[20],[63],[21],[22],[23],[24],[25],[26],[58],[28],[27],[29],[50],[51],[30],[31],[32],[52],[33],[53],[34],[35],[36],[37],[38],[39],[40],[41],[55],[42],[43],[48],[45],[45],[46],[47],[56],[]]
C_ROWS=[[1],[3],[4],[5],[5],[6],[7],[8],[9],[10],[51],[11],[16],[17],[18],[19],[20],[21],[],[],[22],[23],[22],[25],[26],[27],[28],[31],[29],[30],[32],[33],[34],[35],[36],[37],[38],[39],[41],[42],[43],[44],[46],[47],[48],[49],[50],[52],[53],[59],[56],[56],[57],[58],[55],[2]]
assert len(B_ROWS)==len(C_ROWS)==56
for n in range(1,57):
    MAP[f'{n:02}']['B']=[f'B006-{x:02}' for x in B_ROWS[n-1]]
    MAP[f'{n:02}']['C']=[f'D{x:03}' for x in C_ROWS[n-1]]
def link(a=(),b=(),c=()):
    return {'A':[f'006-A-{n:03}' for n in a],'B':[f'B006-{n:02}' for n in b],'C':[f'D{n:03}' for n in c]}
MAP.update({'05b':link([5],[62],[15]),'38b':link([38],[54],[40]),'49b':link([49],[44],[54]),'55b':link([55],[57],[60]),'56b':link([56],[59],[13]),'56c':link([56],[60],[12]),'56d':link([56],[61],[14]),'57':link([],[],[24]),'58':link([],[],[45]),'59':link([41],[36],[43]),'60':link()})
MAP['61']=link()
MAP=dict(sorted(MAP.items(),key=lambda x:(int(re.match(r'\d+',x[0])[0]),x[0])))
C_DOUBT_KEYS=['02','03','04','06','07','08','09','10','12','14','15','17','18','21','22','24','25','28','29','33','41','42','46','48','51']
assert len(C_DOUBT_KEYS)==25
PACKET=OUT.parent/'packets/006'
WITNESSES={r:(PACKET/(r+'.tex')).read_text().splitlines() for r in 'CH'}
READINGS={r:(OUT/'readers/006'/r/'reading.tex').read_text().splitlines() for r in 'ABC'}
def lines(text,start,end=None):return '\n'.join(text[start-1:(end or start)])
def wit(r,start,end=None):return lines(WITNESSES[r],start,end)
def rd(r,start,end=None):return lines(READINGS[r],start,end)
CONTEXT_RANGES={}
def context(keys,cs,ce,hs=None,he=None):
    for key in keys.split():CONTEXT_RANGES[key]={'C':[cs,ce],'H':[hs,he] if hs else []}
context('01 56d',4,4,29,30)
context('02 03 04 05 05b',5,5,33,33)
context('06',9,9)
context('07 08 09 10 56b',10,10,28,28)
context('11',9,10,18,20)
context('12 56c',13,13,27,27)
context('13 14 15 16 17',16,17)
context('18 19 20',20,20,34,34)
context('21 22 23 60',23,23)
context('24 25 26 27',28,28,23,23)
context('28 32',34,34,8,8)
context('29 31',32,32,7,7)
context('30',32,34,7,8)
context('33 34',39,39,11,11)
context('35',39,41,11,11)
context('36',41,41,11,11)
context('37',46,48,12,16)
context('38',46,46,12,13)
context('38b',48,48,16,16)
context('39',51,51)
context('40 41 42 43 44 45 46 47 58 59',53,53,18,20)
context('48 49 49b 55',57,57,21,21)
context('50',57,59,21,22)
context('51 52 53 54 55b',59,59,22,22)
context('56',2,24,26,35)
context('57',27,61,6,23)
context('61',5,5,33,33)
EXTRA_LOCI={}
READER_FALLBACKS={}
WITNESS_OVERRIDES={
'02':{'H':''},'04':{'H':r'\ill{}'},
'05':{'H':r'+\ill{},'},
'06':{'C':r"\frac{P'}{\deleted{\unsure{Q}}P}-\frac{Q'}{Q}",'H':''},
'11':{'C':'','H':''},'12':{'H':'f'},
'13':{'C':r"\frac{(P''Q+\deleted{P'Q'}-\deleted{P'Q'}\deleted{\unsure{+}}\unsure{-|+}Q''P)\deleted{Q}^{\,2}-(P'Q-Q'P)2\deleted{Q}Q'}{Q^{\unsure{3|4}}}",'H':''},
'14':{'H':''},'15':{'H':''},'16':{'H':''},'17':{'H':''},
'19':{'C':'','H':''},
'20':{'C':r'\frac{P\prime\prime Q^2-Q\prime\prime PQ-\unsure{2}P\prime QQ\prime+2PQ\prime^{\,2}}{Q^3}', 'H':r"\frac{P''Q^2 - Q''PQ - 2P'QQ' + 2PQ'^2}{Q^3} ."},
'21':{'H':''},'22':{'H':''},'23':{'H':''},'24':{'H':'a'},
'26':{'H':''},'27':{'C':'','H':'.'},'29':{'H':''},
'31':{'C':'','H':','},'32':{'C':'','H':','},'34':{'H':r'e_1f_{d-3}'},
'36':{'C':'','H':','},'39':{'H':''},'41':{'H':''},
'45':{'H':r'\ill{}'},'47':{'C':'','H':';'},'48':{'H':''},
'50':{'H':''},'51':{'H':''},'54':{'H':r'\ill{}'},
}
WITNESS_OVERRIDES.update({
 '01':{'C':"P'Q-Q'P",'H':"P'Q-PQ'"},
 '05':{'C':r'P\bigl(','H':r'\ill{}','location':'U2, unfinished live P( continuation','C_doubt_status':None},
 '05b':{'C':'','H':',','location':'U2, H terminal comma after the unfinished continuation','final':'No terminal comma','C_doubt_status':None},
 '06':{'C':wit('C',9),'H':''},
 '07':{'C':r"(xy)^{\unsure{2|''}}",'H':"(xy)''"},
 '08':{'C':r"\unsure{x''|x^2}",'H':"x''"},
 '13':{'C':wit('C',16,17),'H':'','location':'U6, full expanded-fraction context; local sign, factor-state and exponent decisions separately mapped'},
 '16':{'C':r'\deleted{Q}^{\,2}','H':''},
 '20':{'C':'','H':'.','location':'U7, H terminal full stop'},
 '21':{'C':r'2{\unsure{p|P}}^2Q^2','H':''},
 '22':{'C':r'\unsure{-}','H':''},
 '23':{'C':wit('C',23),'H':'','location':'U8, complete unfinished lowest fragment','C_doubt_status':None},
 '28':{'C':r'\unsure{\eta|\gamma}','H':r'\eta'},
 '30':{'C':r'\rotatebox{90}{$=$}','H':''},
 '35':{'C':r'\rotatebox{90}{$=$}','H':'='},
 '37':{'C':r'\rotatebox{90}{$=$}','H':''},
 '38':{'C':'','H':',','location':'R4, H terminal comma after the upper delta row','final':'No terminal comma'},
 '38b':{'C':'','H':';','location':'R4, H terminal semicolon after the lower eta row','final':'No terminal semicolon'},
 '40':{'C':'On','H':'on'},
 '42':{'C':r'\unsure{comb. lin}','H':'combinaisons\nlinéaires'},
 '49':{'C':r'2\leq i\leq{}','H':r'2\leq i','location':'R6, second inequality sign and unfinished range'},
 '49b':{'C':'','H':r'($2\leq i$)','location':'R6, H enclosing parentheses around the range','final':'No enclosing parentheses'},
 '51':{'C':r'\deleted{\unsure{S}}','H':''},
 '52':{'C':r's e_{i+1}','H':r'\alpha e_{i+1}','C_doubt_status':None},
 '53':{'C':r't f_{i+1}','H':r'\beta f_{i+1}'},
 '54':{'C':r's e_i+t f_i','H':r'\ill{}'},
 '55':{'C':'','H':';','location':'R6, H semicolon after the unfinished range','final':'No terminal semicolon'},
 '55b':{'C':'','H':';','location':'R6, H semicolon after the lower equation','final':'No terminal semicolon'},
 '56':{'C':wit('C',2,24),'H':wit('H',26,35),'location':'Upright layer, relative order of calculation groups; endpoint punctuation mapped separately'},
 '56b':{'C':'','H':',','location':'U4, H terminal comma after product expression','final':'No terminal comma'},
 '56c':{'C':'','H':',','location':'U5, H terminal comma after general quotient','final':'No terminal comma'},
 '56d':{'C':'','H':',','location':'U1, H terminal comma after first quotient','final':'No terminal comma'},
 '57':{'C':wit('C',27,29),'H':wit('H',23),'location':'Opposite-direction layer, determinant first versus H after final delta system'},
 '58':{'C':'des','H':'de'},
 '59':{'C':',','H':'','location':'R5, comma after the second listed product','final':r'\unsure{,}','C_doubt_status':None,'new_doubt':True,'diff_C':True,'diff_H':True,'confidence':'low'},
 '60':{'C':'','H':'','location':'U8, hooked return at small quotient rule’s right end','final':'Hooked return at rule end; root classification pending','C_doubt_status':None,'classification_pending':True},
 '61':{'C':r"2\frac{P'Q'}{Q^2}",'H':r"2P'\frac{Q'}{Q^2}",'location':'U2, P-prime and Q-prime together above the same fraction rule'},
})
for key in ['05b','49b','56b','56c','56d']:
    WITNESS_OVERRIDES[key]['kind']='text not on the page'
EXTRA_LOCI['60']={'location':'U8, small quotient rule end','C':'','H':'','final':'Hooked return at rule end','evidence':'Root adjudication pending. Reader C describes this in reading.tex line 29 and brief_feedback; no standalone difference row.','crop':'readers/006/C/crops/u08_fragment.png','confidence':'undetermined','kind':'drawing or diagram','diff_C':None,'diff_H':None,'C_doubt_status':None,'marked_in_H':'no'}
EXTRA_LOCI['61']={'location':'U2, numerator factor placement','C':r"2\frac{P'Q'}{Q^2}",'H':r"2P'\frac{Q'}{Q^2}",'final':r"2\frac{P'Q'}{Q^2}",'evidence':'Root supplied an additional exact placement collation after its B01 crop view.','crop':'readers/006/B/crops/01_second_derivative.png','confidence':'high','kind':'insertion or placement','diff_C':False,'diff_H':True,'C_doubt_status':None,'marked_in_H':'no'}
FALLBACK_RANGES={('19','C'):(21,24),('20','C'):(24,25),('56','B'):(2,32),('57','A'):(34,69),('57','B'):(34,72),('58','A'):(61,61),('58','B'):(64,64),('60','A'):(30,32),('60','B'):(30,32),('60','C'):(27,29)}
SUPPLEMENTAL_RANGES={('59','A'):(61,61),('59','B'):(64,64),('59','C'):(60,60)}
FALLBACK_NOTES={('19','C'):'Repeated rule described in comment, represented with ordinary frac.',('20','C'):'No standalone report row; TeX has no terminal stop.',('56','B'):'No order report row; exact reading.tex sequence supplied.',('57','A'):'Determinant precedes delta systems in reading.tex.',('57','B'):'Determinant precedes delta systems in reading.tex.',('58','A'):'des occurs in prose; no separate report row.',('58','B'):'des occurs in prose; no separate report row.',('60','A'):'No separate hooked-return statement; standard frac.',('60','B'):'No separate hooked-return statement; standard frac.',('60','C'):'Hooked return explicitly described in comment.'}
FALLBACK_CROPS={('19','C'):'crops/u07_coefficient.png',('60','A'):'u08_lowest_fragment.png',('60','B'):'crops/07_final_minus.png',('60','C'):'crops/u08_fragment.png'}
for role,path in [('A','u02_second_derivative.png'),('B','crops/01_second_derivative.png'),('C','crops/u02_corrections.png')]:
    FALLBACK_RANGES[('61',role)]=(5,5)
    FALLBACK_NOTES[('61',role)]='Exact reading.tex places P-prime and Q-prime together above one fraction rule; no separate reader report row.'
    FALLBACK_CROPS[('61',role)]=path
for (key,role),bounds in FALLBACK_RANGES.items():
    READER_FALLBACKS.setdefault(key,{})[role]=f'reading.tex lines {bounds[0]}–{bounds[1]}: '+rd(role,*bounds)+' ['+FALLBACK_NOTES[(key,role)]+']'
SPLIT_NOTES={
 '05':'One H ill placeholder covers cancelled predecessor and live continuation. Its H difference is counted once here; original C doubt ownership stays at 04 and terminal comma at 05b.',
 '13':'A/C report full omitted display; B reports three structure rows. Local uncertainties 14–17 are separate. Root allocates H omission counts.',
 '16':'One cancellation-state locus encompassing base Q and raised 2 alternatives.',
 '23':'Root allocates the entire H-omitted fragment once here. C uncertainty owners are 21 and 22; the rule-end detail is at 60.',
 '38':'Upper comma only; A038 also includes lower semicolon, split to 38b.',
 '38b':'Lower semicolon from grouped A038.',
 '41':'Second product and its cancelled predecessor; new comma doubt is separated at 59.',
 '49':'Second inequality only; A049 parentheses separated at 49b.',
 '49b':'Parentheses from grouped A049.',
 '51':'Cancelled predecessor owns the C doubt; B045/C056 also support live s at 52.',
 '52':'Live coefficient only; no second C doubt from B045/C056.',
 '55':'Upper endpoint from A055; lower endpoint is 55b.',
 '55b':'Lower endpoint from A055.',
 '56':'Order only; punctuation from grouped A056 is separated into 56b–56d.',
 '56b':'Product endpoint from grouped A056.', '56c':'General-quotient endpoint from grouped A056.', '56d':'First-quotient endpoint from grouped A056.',
 '59':'New comma qualification from C D043; A/B exact reading.tex has a firm comma. This is outside the 25 original C uncertainty owners.',
 '60':'Reader-comment feature confirmed by root; the exact final TikZ preserves the hooked rule end.'}
ROOT_DECISIONS={}
def root_choice(key,final,confidence,evidence,crop,**kw):
    ROOT_DECISIONS[key]={'final':final,'confidence':confidence,'evidence':evidence,'crop':crop,'root_decided':True,**kw}
root_choice('01',"P'Q-Q'P",'high',"Root viewed crops/006/01_opening_quotient.png: rounded Q with raised tick precedes the tall P. Written factor order is retained.",'crops/006/01_opening_quotient.png',diff_C=False,diff_H=True,root_bbox=[30,22,650,183],root_rotation=0)
root_choice('56d','No terminal comma','high',"Root viewed the opening quotient crop: no terminal comma follows the Q² denominator.",'crops/006/01_opening_quotient.png',diff_C=False,diff_H=True,root_bbox=[30,22,650,183],root_rotation=0)
root_choice('02',r'\deleted{\unsure{+}}','low','Root viewed the B second-derivative crop: dark overlapping strokes do not securely separate the cancelled plus candidate from the following live sign.','readers/006/B/crops/01_second_derivative.png',C_doubt_status='retained',diff_C=False,diff_H=True,alternatives=['unrecovered predecessor'])
root_choice('03',r'\unsure{-|+}','low','Root viewed the B second-derivative crop: dark overlapping strokes do not securely separate the cancelled predecessor and following live sign; minus remains primary with plus alternative.','readers/006/B/crops/01_second_derivative.png',C_doubt_status='retained',diff_C=False,diff_H=False,alternatives=['+'])
root_choice('04',r'\deleted{\unsure{2}}','low','Root viewed the B second-derivative crop and retained the cancelled 2 candidate before live P.','readers/006/B/crops/01_second_derivative.png',C_doubt_status='retained',diff_C=False,diff_H=True,alternatives=['unrecovered predecessor'])
root_choice('05',r'P\bigl(','high','Root viewed the B second-derivative crop and confirmed the visible plus, cancelled predecessor and live P( open fragment. The expression remains unfinished.','readers/006/B/crops/01_second_derivative.png',diff_C=False,diff_H=True)
root_choice('05b','No terminal comma','high','Root viewed the B second-derivative crop and confirmed the absence of H’s trailing comma.','readers/006/B/crops/01_second_derivative.png',diff_C=False,diff_H=True)
root_choice('06',r"\frac{P'}{\deleted{Q}P}-\frac{Q'}{Q}",'high','Root viewed the B logarithmic-quotient crop: a lower oval with tail remains beneath the tall live P. Root resolved the overwritten denominator Q and confirmed the entire H-omitted expression.','readers/006/B/crops/02_log_derivative.png',C_doubt_status='resolved',diff_C=True,diff_H=True)
root_choice('07',r"(xy)^{\unsure{2|''}}",'low','Root viewed the C product crop: the raised bent connected mark remains qualified between 2 and double prime.','readers/006/C/crops/u04_product.png',C_doubt_status='retained',diff_C=False,diff_H=True,alternatives=["''"])
root_choice('08',r"\unsure{x''|x^2}",'medium','Root viewed the C product crop: two upper strokes remain joined or crowded. Root retains the C witness qualification; reader C’s resolution to x double prime is not adopted.','readers/006/C/crops/u04_product.png',C_doubt_status='retained',diff_C=False,diff_H=False,alternatives=['x^2'])
root_choice('09',r'y^{\unsure{\prime}}','low','Root viewed the C product crop: opposite-direction writing overlaps the middle y prime, which remains qualified.','readers/006/C/crops/u04_product.png',C_doubt_status='retained',diff_C=False,diff_H=False,alternatives=['prime not separately recoverable'])
root_choice('10',r'y^{\unsure{\prime\prime|\prime}}','low','Root viewed the C product crop: opposite-direction writing overlaps the final y exponent, leaving double/single-prime alternatives.','readers/006/C/crops/u04_product.png',C_doubt_status='retained',diff_C=False,diff_H=False,alternatives=[r'\prime'])
root_choice('56b','No separately assignable terminal comma','medium','Root viewed the C product crop: no separately assignable terminal comma is supported in the overlap.','readers/006/C/crops/u04_product.png',diff_C=False,diff_H=True)
root_choice('12',r"\deleted{\unsure{P'}}f",'low','Root viewed the B general-quotient crop: the old tall loop and upper tick are crossed or crowded, so the predecessor P prime remains qualified. The live general quotient formula is confirmed.','readers/006/B/crops/04_general_quotient.png',C_doubt_status='retained',diff_C=False,diff_H=True,alternatives=['unrecovered predecessor'])
root_choice('56c','No terminal comma','high','Root viewed the B general-quotient crop: no separate terminal comma appears at the formula’s right endpoint.','readers/006/B/crops/04_general_quotient.png',diff_C=False,diff_H=True)
root_choice('13',r"\frac{(P''Q+\deleted{P'Q'}-\deleted{P'Q'}\deleted{\unsure{+}}\unsure{-|+}Q''P)Q^{\unsure{\deleted{2}|2}} -(P'Q-Q'P)2\deleted{Q}Q'}{Q^3}",'high','Root viewed B05 whole fraction and the C sign, first-factor and denominator crops. All written terms, both struck P-prime Q-prime products, the last separately slashed Q, and the long fraction rule are confirmed. Local sign, first-factor state and denominator decisions are recorded at 14–17.','readers/006/B/crops/05_expanded_quotient.png',diff_C=False,diff_H=True,kind='omission',qualification='H omission of this complete expanded display is counted once here. Local C changes at 16 and 17 are counted at their own rows, with their local confidence qualifications retained.')
root_choice('14',r'\deleted{\unsure{+}}','low','Root viewed B05 and the C numerator-sign crop: a short vertical protrudes through two thick horizontal overtraces; the layers do not isolate a certain cancelled predecessor.','readers/006/C/crops/u06_numerator_sign.png',C_doubt_status='retained',diff_C=False,diff_H=False,alternatives=['unrecovered predecessor'],qualification='H omits the full display; its omission is covered once at 006-13.')
root_choice('15',r'\unsure{-|+}','low','Root viewed B05 and the C numerator-sign crop: a short vertical protrudes through two thick horizontal overtraces; the layers do not isolate a certain live sign.','readers/006/C/crops/u06_numerator_sign.png',C_doubt_status='retained',diff_C=False,diff_H=False,alternatives=['+'],qualification='H omits the full display; its omission is covered once at 006-13.')
root_choice('16',r'Q^{\unsure{\deleted{2}|2}}','low','Root viewed B05 and the C first-factor crop. The large loop and tail of Q remain left of the long oblique crossing, while the raised 2 is crowded by dark cross-strokes and the oblique. The base Q is retained live and both exponent cancellation states remain; no chronology is inferred.','readers/006/C/crops/u06_first_factor.png',diff_C=True,diff_H=False,new_doubt=True,alternatives=['Q^2'],component_confidence={'live_base_Q':'medium','exponent_cancellation':'low'},qualification='One local cancellation-state locus. H omission is covered once at 006-13.',kind='deletion state (struck given live or live given struck)')
root_choice('17',r'Q^3','high','Root viewed B05 and the C denominator crop: two right-bowing lobes and a left-returning lower foot are visible independently of the diagonal. Root resolves the denominator exponent as 3.','readers/006/C/crops/u06_denominator.png',C_doubt_status='resolved',diff_C=True,diff_H=False,qualification='H omission of the full display is covered once at 006-13.')
root_choice('18',r'\unsure{2}','low','Root viewed the B following-fraction crop: a low curled foot shows before and below heavy P, but the upper outline merges with P. The coefficient remains qualified; B’s resolution is not adopted.','readers/006/B/crops/06_simplified_quotient.png',C_doubt_status='retained',diff_C=False,diff_H=False,alternatives=['coefficient not fully recoverable'])
root_choice('19','Distinct partial second rule beneath the right portion of the fraction rule, drawn separately','high','Root viewed the B following-fraction crop and confirmed a distinct partial second fraction rule. Root requires drawing it, with no algebraic role supplied.','readers/006/B/crops/06_simplified_quotient.png',diff_C=True,diff_H=True,kind='drawing or diagram')
root_choice('20','No terminal full stop','high','Root viewed the B following-fraction crop and confirmed the absence of a terminal full stop.','readers/006/B/crops/06_simplified_quotient.png',diff_C=False,diff_H=True)
root_choice('21',r'2p^2Q^2','high','Root viewed the C lowest-fragment crop: the low bowl and descending stem are visibly smaller than the following Q. The lowercase p is resolved.','readers/006/C/crops/u08_fragment.png',C_doubt_status='resolved',diff_C=True,diff_H=False,qualification='H omission of the whole fragment is covered once at 006-23.')
root_choice('22','-','high','Root viewed the C lowest-fragment crop: a pale gap separates the minus from the small fraction bar. The separate minus is resolved.','readers/006/C/crops/u08_fragment.png',C_doubt_status='resolved',diff_C=True,diff_H=False,qualification='H omission of the whole fragment is covered once at 006-23.')
root_choice('23',r"2p^2Q^2\bigl(-\frac{Q'}{Q}+",'high','Root viewed the C lowest-fragment crop and confirmed the entire unfinished expression, including the final plus and absence of a closing continuation. The small fraction rule’s hooked return is preserved separately at 60.','readers/006/C/crops/u08_fragment.png',diff_C=False,diff_H=True,kind='omission',qualification='H omission of this entire fragment is counted once here; local C changes are counted at 21, 22 and 60.')
root_choice('60','Hooked return at the right end of the small fraction rule, preserved in the drawing','high','Root viewed the C lowest-fragment crop and confirmed the hooked return at the rule’s right end. Root requires preserving it in TikZ without interpreting it as an arrow.','readers/006/C/crops/u08_fragment.png',diff_C=True,diff_H=False,classification_pending=False,kind='drawing or diagram',qualification='H omission of the whole fragment is covered once at 006-23.')
root_choice('24',r'a\deleted{\unsure{d|b}}','low','Root viewed the C determinant crop: narrow upright loops and a middle cross-stroke do not settle the additional cancelled letter. Both d and b remain supported.','readers/006/C/crops/r01_determinant.png',C_doubt_status='retained',diff_C=False,diff_H=True,alternatives=['b'])
root_choice('25','-','high','Root viewed the C determinant crop: one short horizontal has open space beneath it, with no second rule. The single dash is resolved.','readers/006/C/crops/r01_determinant.png',C_doubt_status='resolved',diff_C=True,diff_H=True)
root_choice('26',r'\text{inversible}','medium','Root viewed the C determinant crop and then the root word crop because the reader crop clipped the word’s right extent. A narrow initial i and joined low letter run lead into the tall b/l ending; overlapping opposite-direction ink remains visible. Root confirms inversible.','crops/006/03_inversible.png',diff_C=False,diff_H=True,root_bbox=[220,1505,675,1625],root_rotation=180)
root_choice('27','No terminal full stop','medium','Root viewed the C determinant crop and the root word crop: no separate terminal full stop is supported; nearby opposite-orientation ink limits confidence.','crops/006/03_inversible.png',diff_C=False,diff_H=True,root_bbox=[220,1505,675,1625],root_rotation=180)
ROOT_DECISIONS['57']={'root_decided':False,'evidence':'Root inspected the determinant crop and noted that original y1490–1670 places it first after the half-turn, agreeing with all three layout readings. Root confirmation against subsequent row crops remains pending.'}
root_choice('29',r'\deleted{=e_d}','high','Root viewed C’s first delta-row crop: two bars, e and a lowered d are legible beneath the short cancelling sweep. Root resolves the locally cancelled ending.','readers/006/C/crops/r02_first_row.png',C_doubt_status='resolved',diff_C=True,diff_H=True)
root_choice('31','No terminal comma','high','Root viewed C’s first delta-row crop: the locally cancelled ending occupies the continuation, with no terminal comma.','readers/006/C/crops/r02_first_row.png',diff_C=False,diff_H=True)
root_choice('28',r'\eta','high','Root viewed C’s first eta-row crop: an initial short shoulder and arch lead into a long returning right descender. The eta is resolved.','readers/006/C/crops/r03_eta_row.png',C_doubt_status='resolved',diff_C=True,diff_H=False)
root_choice('30',r'\rotatebox{90}{$=$}','high','Root viewed C’s first delta and eta-row crops and confirmed the vertical equals between the left members. Root uses C’s array arrangement to place the sign below the upper left member.','readers/006/C/crops/r03_eta_row.png',diff_C=False,diff_H=True,kind='insertion or placement')
root_choice('33',r'\deleted{f}e_1','medium','Root viewed C’s second-pair crop: a narrow upper loop protrudes above replacement e and a long looped descender survives below, crossed by local short strokes. Root resolves the cancelled predecessor f.','readers/006/C/crops/r04_second_pair.png',C_doubt_status='resolved',diff_C=True,diff_H=True)
root_choice('34',r'e_1\cdot f_{d-3}','high','Root viewed C’s second-pair crop and confirmed the explicit multiplication dot between e₁ and f with index d−3.','readers/006/C/crops/r04_second_pair.png',diff_C=False,diff_H=True)
root_choice('35',r'\rotatebox{90}{$=$}','high','Root viewed C’s second-pair crop and confirmed the vertical equals beneath the left member, with the coefficient row below. C’s array arrangement preserves this placement.','readers/006/C/crops/r04_second_pair.png',diff_C=False,diff_H=True,kind='insertion or placement')
root_choice('36','No terminal comma','high','Root viewed C’s second-pair crop: ample clear space follows the lowered 2, with no terminal comma.','readers/006/C/crops/r04_second_pair.png',diff_C=False,diff_H=True)
root_choice('37',r'\rotatebox{90}{$=$}','high','Root viewed C’s third delta-row and c-eta-row crops: the two strokes of the vertical equals continue across the adjoining crop bounds. Root confirms the sign beneath the left members.','readers/006/C/crops/r06_ceta_row.png',diff_C=False,diff_H=True,kind='insertion or placement',root_additional_crops=['readers/006/C/crops/r05_third_row.png'])
root_choice('38','No terminal comma','high','Root viewed C’s third delta-row and c-eta-row crops and confirmed the absence of H’s upper-row terminal comma.','readers/006/C/crops/r05_third_row.png',diff_C=False,diff_H=True)
root_choice('38b','No terminal semicolon','high','Root viewed C’s third delta-row and c-eta-row crops and confirmed the absence of H’s lower-row terminal semicolon.','readers/006/C/crops/r06_ceta_row.png',diff_C=False,diff_H=True)
root_choice('39','etc','high','Root viewed C’s c-eta-row crop and confirmed the written etc with no terminal stop.','readers/006/C/crops/r06_ceta_row.png',diff_C=False,diff_H=True)
root_choice('40','On','high','Root viewed C’s first prose crop and confirmed the capital O in On.','readers/006/C/crops/r07_prose_one.png',diff_C=False,diff_H=True)
root_choice('11',r'\underset{\unsure{\text{.}}}{\phantom{\text{On}}}','low','Root viewed C’s first prose crop and confirmed the detached dot at approximately full-scan (969,603), below and left of On after the half-turn. Its hand, layer, role and cancellation state remain unknown. B/C relative placement is retained.','readers/006/C/crops/r07_prose_one.png',diff_C=True,diff_H=True,new_doubt=True,alternatives=['hand, layer, role and cancellation state undetermined'],root_bbox=[965,598,973,607],qualification='A’s standalone margin assignment is not adopted; the visible detached dot remains separately qualified.')
root_choice('32','No terminal comma','high','Root viewed the new eta-endpoint crop: ample space follows the final 2, with no comma. This crop covers the endpoint clipped tightly by the C reader crop.','crops/006/04_eta_endpoint.png',diff_C=False,diff_H=True,root_bbox=[170,1250,430,1380],root_rotation=180)
root_choice('41',r'\deleted{f}e_1f_{d-3}','medium','Root viewed C’s first prose crop and the new predecessor crop, which includes the complete ascender clipped in A/B context. A complete narrow upper loop and long lower loop remain beneath the dark e. Root resolves the cancelled f and preserves the whole second listed product. No chronology is inferred.','crops/006/05_prose_predecessor.png',C_doubt_status='resolved',diff_C=True,diff_H=True,root_bbox=[220,540,455,730],root_rotation=180,qualification='The following comma qualification is separated at 006-59; H omission of the product and its following punctuation is allocated here.')
root_choice('59',r'\unsure{,}','low','Root viewed C’s first prose crop and the new predecessor crop: opposite-direction product ink crosses the subscript and ending. The following comma remains the C witness glyph, now qualified as proposed by reader C.','crops/006/05_prose_predecessor.png',diff_C=True,diff_H=False,new_doubt=True,kind='other',root_bbox=[220,540,455,730],root_rotation=180,alternatives=['comma not separately recoverable'],qualification='New punctuation uncertainty outside the original 25 C doubts. H omission of this punctuation with the second product is covered at 006-41; the raw C-reader D043 H flag is retained in provenance.')
root_choice('42','comb. lin','medium','Root viewed C’s remaining prose crops: abbreviated joined comb is followed by a separate dot, then tall l and low in, with no dot after lin. Root resolves the written abbreviation without expanding it.','readers/006/C/crops/r08_prose_two.png',C_doubt_status='resolved',diff_C=True,diff_H=True)
root_choice('43',r'f_{d-2}','high','Root viewed C’s remaining prose crops and confirmed f with index d−2. The preceding e with index d−1 is retained as written.','readers/006/C/crops/r09_prose_three.png',diff_C=False,diff_H=True,qualification='The two prose basis indices remain e_{d-1} and f_{d-2}; neither is changed to match another formula.')
root_choice('44','coeff','high','Root viewed C’s remaining prose crops and confirmed coeff without a terminal dot.','readers/006/C/crops/r09_prose_three.png',diff_C=False,diff_H=True)
root_choice('45','entiers','medium','Root viewed C’s remaining prose crops: joined initial en, a tall t and the low terminal run are legible. Root confirms entiers at H’s ill marker.','readers/006/C/crops/r09_prose_three.png',diff_C=False,diff_H=True)
root_choice('46','fonctions','medium','Root viewed C’s remaining prose crops: tall f and t and the joined intervening and terminal letters support fonctions. Root resolves the C uncertainty.','readers/006/C/crops/r10_prose_four.png',C_doubt_status='resolved',diff_C=True,diff_H=False)
root_choice('47','No terminal semicolon','high','Root viewed C’s last prose crop: no terminal semicolon follows the final d.','readers/006/C/crops/r10_prose_four.png',diff_C=False,diff_H=True)
root_choice('58','des','medium','Root viewed C’s remaining prose crops: the low final s turn is present. Root confirms des.','readers/006/C/crops/r08_prose_two.png',diff_C=False,diff_H=True)
root_choice('48',r'\deleted{\unsure{\delta}}','low','Root viewed the new final-system crop: the cancelled delta candidate remains beneath overlapping slashes and cannot be securely isolated.','crops/006/02_final_system.png',C_doubt_status='retained',diff_C=False,diff_H=True,alternatives=['unrecovered predecessor'])
root_choice('49',r'2\leq i\leq{}','high','Root viewed the new final-system crop: both bars of the final less-than-or-equal sign are visible, with no bound written after it. The range remains unfinished.','crops/006/02_final_system.png',diff_C=False,diff_H=True)
root_choice('49b','No enclosing parentheses','high','Root viewed the new final-system crop and confirmed the absence of H’s enclosing parentheses around the written range.','crops/006/02_final_system.png',diff_C=False,diff_H=True)
root_choice('50',r'\rotatebox{90}{$=$}','high','Root viewed the new final-system crop and confirmed the vertical equals beneath the left member.','crops/006/02_final_system.png',diff_C=False,diff_H=True,kind='insertion or placement')
root_choice('51',r'\deleted{\unsure{S}}','low','Root viewed the new final-system crop: folded overwritten curves leave the predecessor S candidate qualified.','crops/006/02_final_system.png',C_doubt_status='retained',diff_C=False,diff_H=True,alternatives=['unrecovered predecessor'])
root_choice('52',r's e_{i+1}','medium','Root viewed the new final-system crop: the lower s-turn of the live coefficient matches the visible right-hand-side s.','crops/006/02_final_system.png',diff_C=False,diff_H=True)
root_choice('53',r't f_{i+1}','high','Root viewed the new final-system crop: the t coefficient has a visible crossbar.','crops/006/02_final_system.png',diff_C=False,diff_H=True)
root_choice('54',r's e_i+t f_i','medium','Root viewed the new final-system crop: the individual letters and indices of s e_i+t f_i survive the other-layer crossing.','crops/006/02_final_system.png',diff_C=False,diff_H=True)
root_choice('55','No terminal semicolon','high','Root viewed the new final-system crop and confirmed no semicolon after the unfinished range.','crops/006/02_final_system.png',diff_C=False,diff_H=True)
root_choice('55b','No terminal semicolon','high','Root viewed the new final-system crop and confirmed no semicolon after the lower equation.','crops/006/02_final_system.png',diff_C=False,diff_H=True)
root_choice('56','Opening P/Q pair; middle logarithmic quotient; product; general quotient; long expanded fraction; following fraction; lowest unfinished fragment','high','Root confirmed order from the individually viewed crop coordinates and three independent complete layout returns: the opening P/Q pair is above the product, which is above the general quotient. No entire page image was viewed by root.','crops/006/01_opening_quotient.png',diff_C=False,diff_H=True,kind='insertion or placement',qualification='Separate display blocks for logarithmic quotient and product preserve their reported vertical order; this display grouping creates no separate C text change.')
root_choice('57','After half-turn: determinant; three delta pairs; etc; prose; final delta system','high','Root confirmed order from all individually viewed crop coordinates and three independent complete layout returns: after the half-turn the determinant precedes the delta pairs, then prose and final system. No entire page image was viewed by root.','readers/006/C/crops/r01_determinant.png',diff_C=False,diff_H=True,kind='insertion or placement')
root_choice('61',r"2\frac{P'Q'}{Q^2}",'high','Root’s already-viewed B01 second-derivative crop confirms that P-prime and Q-prime stand together above the same fraction rule. All three exact reading.tex lines agree.','readers/006/B/crops/01_second_derivative.png',diff_C=False,diff_H=True,kind='insertion or placement',qualification='The shared numerator is a literal placement difference from H. Slash-versus-stacked-quotient syntax creates no additional row.')
ROOT_DECISIONS['04'].update(diff_H=False,qualification='H’s one ill placeholder covers this predecessor and the live P( continuation; its difference is counted once at 006-05.')
ROOT_DECISIONS['05'].update(final=r'\deleted{\unsure{2}}P\bigl(',qualification='H’s one ill placeholder is counted once here: P( is high confidence; the cancelled predecessor 2 remains low confidence and its original C doubt is owned at 006-04.',component_confidence={'live_P_open_parenthesis':'high','cancelled_2':'low'})
WITNESS_OVERRIDES['05']['C']=r'\deleted{\unsure{2}}P\bigl('
WITNESS_OVERRIDES['05']['location']='U2, cancelled predecessor and readable unfinished P( covered by one H ill marker'
ROOT_DECISIONS['07']['qualification']='H’s double-prime reading survives as an alternative. The primary 2-like reading differs from H, but this retained uncertainty does not establish a conclusive H error.'
for key in ['03','08','09','10','18']:
    ROOT_DECISIONS[key]['qualification']='H’s reading remains a retained primary candidate or supported alternative; no conclusive H error is charged for this qualified locus.'
ROOT_DECISIONS['42']['crop']='readers/006/C/crops/r09_prose_three.png'
ROOT_DECISIONS['45']['crop']='readers/006/C/crops/r10_prose_four.png'
ROOT_DECISIONS['58']['crop']='readers/006/C/crops/r09_prose_three.png'
FINAL_PAGE_PATH=OUT/'pages/J81-01_81_scan006.tex'
FINAL_PAGE_TEXT=FINAL_PAGE_PATH.read_text()
FINAL_PAGE=FINAL_PAGE_TEXT.splitlines()
FINAL_CONTEXT_RANGES={}
def final_context(keys,start,end=None):
    for key in keys.split():FINAL_CONTEXT_RANGES[key]=[start,end or start]
final_context('01 56d',4)
final_context('02 03 04 05 05b 61',5)
final_context('06',9)
final_context('07 08 09 10 56b',12)
final_context('11',69,71)
final_context('12 56c',15)
final_context('13 14 15 16 17',18,19)
final_context('18 19 20',22,30)
final_context('21 22 23 60',32,40)
final_context('24 25 26 27',44)
final_context('28 32',50)
final_context('29 31',48)
final_context('30',48,50)
final_context('33 34',55)
final_context('35',55,57)
final_context('36',57)
final_context('37',62,64)
final_context('38',62)
final_context('38b',64)
final_context('39',67)
final_context('40 41 42 43 44 45 46 47 58 59',71)
final_context('48 49 49b 55',75)
final_context('50',75,77)
final_context('51 52 53 54 55b',77)
final_context('56',2,40)
final_context('57',43,79)
assert set(FINAL_CONTEXT_RANGES)==set(MAP)
ROOT_DECISIONS['13']['final']=lines(FINAL_PAGE,18,19)
ROOT_DECISIONS['19']['final']=lines(FINAL_PAGE,22,30)
ROOT_DECISIONS['60']['final']=lines(FINAL_PAGE,32,40)
ROOT_CROPS={x['path']:x for x in json.loads((OUT/'crops/006/manifest.json').read_text())}

# These annotations describe literal expressions and the scope of the four
# existing events. They do not run a new check or supply another ink choice.
MATH_CONSEQUENCES={
 '01':"The written Q'P factor order is retained. In the commutative coefficient ring of checks/scan006_algebra.md, P has constant coefficient P0 and Q has first coefficient Q1; Q1P0=P0Q1 by multiplication in that ring. The first-quotient certificate represents both products by the same coefficient expression while the record preserves the pen’s order.",
 '03':"The alternatives precede 2P'Q'/Q². The existing second-quotient certificate contains −2P1Q0Q1/Q0³. That recorded negative term does not remove the live minus/plus qualification.",
 '07':"The proved morphism in checks/scan006_algebra.md sends x and y to their stated second-order epsilon polynomials. Event 006-second-product extracts twice the epsilon² coefficient of their product and obtains x2*y0+2*x1*y1+x0*y2. The written 2/double-prime alternatives remain; the coefficient calculation does not convert the 2-like superscript into certain derivative notation.",
 '08':"With the coefficient labels x, x-prime and x-double-prime represented by x0, x1 and x2, the two first-term readings correspond to x2*y0 and x0²*y0. Event 006-second-product contains x2*y0. The page retains both ink candidates.",
 '09':"The middle y-prime candidate corresponds to y1 in the recorded term 2*x1*y1. Its prime remains qualified because the local stroke overlaps the opposite writing.",
 '10':"The final y-double-prime/y-prime alternatives correspond to y2/y1 in the final term. Event 006-second-product contains x0*y2; the manuscript exponent is kept qualified.",
 '13':"The intermediate numerator is reproduced in full, including both struck P'Q' products and the separately struck final Q. The four existing events verify their stated jet and final quotient/product coefficient expressions; they assign no chronology to these local cancellations.",
 '14':"The qualified cancelled plus records a predecessor before Q-double-prime P. Its writing layer remains explicit; the final quotient certificate supplies no chronology for that predecessor.",
 '15':"The sign alternatives occur before Q-double-prime P in the intermediate numerator. Event 006-second-quotient has the final numerator term −Q2*P0*Q0. That coefficient context does not settle the overlapped intermediate sign.",
 '16':"The base Q is live. The alternatives concern a cancelled or live raised 2, preserving the single-Q and Q² layer states within the same factor locus. The displayed intermediate fraction undergoes no cancellation or power reduction; chronology remains unassigned.",
 '17':"The denominator is Q³. The existing second-quotient certificate uses Q0³ beneath P2*Q0²−Q2*P0*Q0−2*P1*Q0*Q1+2*P0*Q1². The explicit generator map and verified inverse relation are in checks/scan006_algebra.md; the 3 glyph is resolved from the crop.",
 '18':"The qualified numeral is the coefficient of the P'QQ' term. The existing second-quotient certificate records −2*P1*Q0*Q1 in its numerator. The uncertain 2 remains qualified in the page despite that coefficient correspondence.",
 '19':"The extra short rule is drawn without introducing another operator, equation or coefficient.",
 '21':"The fragment begins with lowercase p² followed by Q². The quotient certificate uses P-labelled generators; the fragment supplies no identification p=P, so lowercase p is retained.",
 '22':"The separate minus precedes Q'/Q within the open parenthesis. The fragment still ends with its final plus and no closing continuation.",
 '23':"The written expression remains 2p²Q²(−Q'/Q+ with no supplied next summand or completed identity.",
 '25':"The determinant row retains the single dash before ad−bc and the following inversible. No equals sign is inserted, and none of the four recorded coefficient events verifies a determinant assertion.",
 '29':"The =e_d ending remains locally cancelled within the globally cancelled layer. The index d and local deletion are preserved without appending that expression to the surviving row.",
 '33':"The cancelled f is retained beneath live e₁. The surviving product remains e₁·f_{d−3}, including the explicit multiplication dot.",
 '41':"The second product e₁f_{d−3} is retained among the four written products, together with its cancelled predecessor f. H omits this product. The prose’s linear-combination assertion is transcribed; the four checks do not concern the delta systems.",
 '43':"The prose names e_{d−1} and f_{d−2}; H’s second basis index is d−1. The record preserves the changed second indexed symbol and supplies no identification between those indexed elements. The four coefficient checks concern the upright quotient/product expressions.",
 '48':"The delta candidate remains locally cancelled before x_{i−1}, while the surviving displayed term is −e₁x_{i−1}. Both the deletion state and the index are preserved.",
 '49':"The written condition is the open chain 2≤i≤. H keeps only 2≤i. No upper bound is inserted after the second sign.",
 '50':"The vertical equals retains the connection between the two written rows beneath the left member; no additional horizontal chain is supplied.",
 '51':"The S candidate remains locally cancelled before live s, preserving both local writing states inside the globally cancelled system.",
 '52':"The lower left member reads delta(s e_{i+1}+t f_{i+1}); H writes alpha at the first coefficient. The right member also contains s e_i. No equality s=alpha is supplied.",
 '53':"The lower left member has t before f_{i+1}, and the right member has t f_i. H writes beta at the left. The record does not assign t=beta.",
 '54':"The legible right member s e_i+t f_i replaces H’s ill marker. Both coefficients and indices are preserved. The four recorded checks do not verify this delta-system equation.",
 '56':"Calculation groups retain their physical sequence. The numerator factor placement is separately recorded at 61; no algebraic rearrangement changes the recorded page order.",
 '57':"The determinant remains first after the half-turn, before the delta pairs and prose. Its placement supplies no additional algebraic assertion or chronology.",
 '60':"The rule’s hook is drawn without an arrow operator or extra algebraic symbol.",
 '61':"The literal numerator is P'Q' above one Q² rule. In the existing commutative coefficient ring, 2(P1Q1)Q0^{-2} and (2P1)(Q1Q0^{-2}) have the same generator images and coincide by the ring’s associative multiplication. This explicit correspondence retains the written shared numerator as an H placement difference; no new computation event is added.",
}
EXCLUSIONS={}
ROOT_COMPLETE=True

# Inventory is assembled only after all 67 root choices were supplied. Source
# identifiers preserve the three readers' complete item coverage.
INV_B=[1,2,3,4,5,6,7,33,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34]
INV_C=[1,2,3,4,5,6,7,29,8,9,10,11,12,13,14,15,16,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,None]
FINAL_INVENTORY=[]
for n,item in enumerate(REPORTS['A']['inventory'],1):
    row=copy.deepcopy(item)
    row['source_map']={'A':[item['element']],'B':[f'006.B.{INV_B[n-1]:02}'],'C':[f'006.C.{INV_C[n-1]:02}'] if INV_C[n-1] else ['notes: archive numeral comment']}
    row['element']=f'006.{n:02}'
    FINAL_INVENTORY.append(row)
INV_UPDATES={
 1:{'first_words_or_objects':r"(P/Q)'=P'/Q-PQ'/Q^2=(P'Q-Q'P)/Q^2"},
 2:{'first_words_or_objects':r"(P/Q)''=P''/Q\deleted{\unsure{+}}\unsure{-|+}2P'Q'/Q^2+\deleted{\unsure{2}}P("},
 7:{'first_words_or_objects':r"(xy)^{\unsure{2|''}}=\unsure{x''|x^2}y+2x'y^{\unsure{\prime}}+xy^{\unsure{\prime\prime|\prime}}"},
 8:{'kind':'text','hand':'undetermined hand','position':'approximately full-scan (969,603), below-left of On after the half-turn','first_words_or_objects':'detached dot; hand, layer, role and cancellation state unresolved'},
 11:{'first_words_or_objects':ROOT_DECISIONS['13']['final']},
 15:{'first_words_or_objects':r'live base Q with exponent \unsure{\deleted{2}|2}; no chronology inferred'},
 17:{'first_words_or_objects':r"\frac{P''Q^2-Q''PQ-\unsure{2}P'QQ'+2PQ'^{\,2}}{Q^3}"},
 18:{'first_words_or_objects':'distinct partial second fraction rule, reproduced graphically; no algebraic role supplied'},
 26:{'first_words_or_objects':r'\deleted{f} beneath live e_1'},
 29:{'first_words_or_objects':r'On en tire; four listed products; comb. lin des e_{d-1} et f_{d-2}; coeff entiers fonctions; second-product comma qualified'},
 30:{'first_words_or_objects':r'\deleted{f} beneath live e_1 in second listed product'},
}
for n,change in INV_UPDATES.items():FINAL_INVENTORY[n-1].update(change)
FINAL_INVENTORY.append({'sheet_kind':'text','hand':'his hand','element':'006.35','kind':'drawing','position':'U8, small quotient rule right tip, approximately x614–629 y1626–1642','first_words_or_objects':'hooked return at rule end, drawn without an arrow interpretation','transcribed':'yes','source_map':{'A':['006.A.U8'],'B':['006.B.18'],'C':['006.C.17','reading.tex line 29']}})
# Place the hooked-rule item immediately after the lowest upright display.
FINAL_INVENTORY.insert(19,FINAL_INVENTORY.pop())
for n,row in enumerate(FINAL_INVENTORY,1):row['element']=f'006.{n:02}'
FINAL_NOTES="The sheet combines eight upright quotient/product formula groups with an opposite-direction calculation crossed by two long diagonals. After a half-turn, the determinant precedes three paired delta systems, etc, a four-line prose paragraph and the final paired system. The readers found no title, date or authorial page number. The pencilled archive 5 is retained as a comment.\n\nWritten factor order is preserved: the first quotient has Q'P, and the second derivative places P'Q' together above one fraction rule. The determinant retains its single dash before ad−bc and the word inversible. The prose keeps all four listed products and the unequal basis indices e_{d-1}, f_{d-2}; the final system keeps coefficients s and t. Four vertical equality signs remain below their left members. The abbreviations comb. lin, coeff and etc are not expanded.\n\nThe second derivative stops at P(. The lowest fragment retains its open parenthesis and final plus; the last range remains 2≤i≤ with no upper bound. Two drawing details are preserved: a partial second fraction rule and the hooked return at the small quotient rule’s end. No algebraic or arrow role is assigned to them.\n\nMathematical context prompted scrutiny of the product exponents, coefficient 2, long-fraction denominator and cancellation state. The denominator reads 3, but product exponents/primes, coefficient 2 and several predecessors remain qualified. The first Q base is live while cancellation of its raised 2 remains uncertain. The second prose product’s cancelled f is resolved; its following comma remains qualified. The detached dot’s hand, layer, role and cancellation state remain unassigned.\n\nFour root checks actually ran at 10:27:09 UTC: inverse jet, first quotient, second quotient and second product coefficients. All recorded denominator-cleared residual coefficients are zero. checks/scan006_algebra.md supplies the explicit ring morphism and its verified inverse relation. These computations do not settle the handwriting or cancellation chronology."


def source_rows(key,role):
    return [INDEX[role][sid] for sid in MAP[key].get(role,[]) if role in INDEX]

def rootpath(role,path):
    if not path:return ''
    return str(Path('readers/006')/role/path)

def crop_metadata(role,path):
    for x in REPORTS[role]['crops']:
        if x['path']==path:
            z=copy.deepcopy(x);z['path']=rootpath(role,path);return z
    return None

def build():
    decisions=[]
    for key,links in MAP.items():
        available=[(r,x) for r in READY_READERS for x in source_rows(key,r)]
        if available:
            role,base=available[0]
            rec={'id':'006-'+key,'location':base['location'],'C':base.get('C'),'H':base.get('H'),
                 'final':base['reading'],'readers':{},'evidence':'Root adjudication pending. '+role+' reports: '+base['evidence'],
                 'crop':rootpath(role,base.get('readers_crop')),'confidence':base['confidence'],'kind':base['kind'],
                 'diff_C':base.get('diff_C',False),'diff_H':base.get('diff_H',False),
                 'C_doubt_status':base.get('C_doubt_status'),'marked_in_H':'yes' if r'\ill' in str(base.get('H','')) else 'no',
                 'root_decided':False,'source_map':copy.deepcopy(links),'reader_bbox':{},'reader_crops':{}}
        else:
            rec=copy.deepcopy(EXTRA_LOCI[key]);rec.update(id='006-'+key,readers={},root_decided=False,source_map=copy.deepcopy(links),reader_bbox={},reader_crops={})
        rec.update(reader_reports={},reader_evidence={},reader_confidence={},reader_crop_metadata={},reader_text_fallbacks={},
                   final_is_provisional=True,C_doubt_locus=key in C_DOUBT_KEYS,
                   pending_root_decision='Root crop inspection and explicit local decision required.',
                   witness_context={r:{'path':f'packets/006/{r}.tex','lines':bounds,'text':wit(r,*bounds) if bounds else ''} for r,bounds in CONTEXT_RANGES[key].items()})
        for role in 'ABC':
            rows=source_rows(key,role)
            rec['readers'][role]=' | '.join(x['id']+': '+x['reading'] for x in rows) if rows else READER_FALLBACKS.get(key,{}).get(role,('Reader '+role+' final return not yet opened' if role not in READY_READERS else 'No separate report row; exact reading.tex mapping pending'))
            if rows:
                rec['reader_bbox'][role]=[x.get('bbox') for x in rows]
                rec['reader_crops'][role]=[rootpath(role,x.get('readers_crop')) for x in rows]
            rec['reader_reports'][role]=copy.deepcopy(rows)
            rec['reader_evidence'][role]={x['id']:x['evidence'] for x in rows}
            rec['reader_confidence'][role]={x['id']:x['confidence'] for x in rows}
            rec['reader_crop_metadata'][role]=[crop_metadata(role,x.get('readers_crop')) for x in rows]
            if not rows:
                bounds=FALLBACK_RANGES[(key,role)]
                rec['reader_text_fallbacks'][role]={'path':f'readers/006/{role}/reading.tex','lines':list(bounds),'text':rd(role,*bounds),'note':FALLBACK_NOTES[(key,role)]}
                path=FALLBACK_CROPS.get((key,role))
                if path:
                    meta=crop_metadata(role,path)
                    rec['reader_crops'][role]=[rootpath(role,path)]
                    rec['reader_bbox'][role]=[meta['bbox']]
                    rec['reader_crop_metadata'][role]=[meta]
            if (key,role) in SUPPLEMENTAL_RANGES:
                bounds=SUPPLEMENTAL_RANGES[(key,role)]
                exact=rd(role,*bounds)
                rec['reader_text_fallbacks'][role]={'path':f'readers/006/{role}/reading.tex','lines':list(bounds),'text':exact,'note':'Exact prose-line comma mapping supplements the grouped product/predecessor report row.'}
                rec['readers'][role]+=f' | reading.tex lines {bounds[0]}–{bounds[1]}: '+exact
        rec.update(WITNESS_OVERRIDES.get(key,{}))
        if key not in C_DOUBT_KEYS:rec['C_doubt_status']=None
        if key in SPLIT_NOTES:rec['mapping_note']=SPLIT_NOTES[key]
        rec['marked_in_H']='yes' if r'\ill' in str(rec.get('H','')) else 'no'
        rec.update(ROOT_DECISIONS.get(key,{}))
        rec['final_page_context']={'path':'pages/J81-01_81_scan006.tex','lines':FINAL_CONTEXT_RANGES[key],'text':lines(FINAL_PAGE,*FINAL_CONTEXT_RANGES[key])}
        if key in MATH_CONSEQUENCES:rec['mathematical_consequence']=MATH_CONSEQUENCES[key]
        path=rec.get('crop','')
        if path in ROOT_CROPS:
            rec['root_crop_metadata']=copy.deepcopy(ROOT_CROPS[path])
            rec.setdefault('root_bbox',ROOT_CROPS[path]['bbox'])
            rec.setdefault('root_rotation',ROOT_CROPS[path]['rotation'])
        elif path.startswith('readers/006/'):
            role=path.split('/')[2]
            local='/'.join(path.split('/')[3:])
            rec['root_crop_metadata']=crop_metadata(role,local)
        if rec.get('root_decided'):
            rec.update(final_is_provisional=False,pending_root_decision=None)
        if rec.get('C_doubt_status')=='resolved':rec['diff_C']=True
        if key in EXCLUSIONS:
            rec.update(diff_C=False,diff_H=False,C_doubt_status=None,exclusion=EXCLUSIONS[key])
        decisions.append(rec)
    record={'scan':6,'folder':'J81-01','their_page':5,'hua_has':'text','filename':'J81-01_81_scan006.tex',
        'brief_version':'v05','main_adjudicated':False,'decisions':decisions,'doubts':[],
        'inventory':FINAL_INVENTORY if ROOT_COMPLETE else [],'notes':FINAL_NOTES,
        'abbreviations':[{'form':'det','expansion':'déterminant'},{'form':'etc','expansion':'et cetera'},{'form':'comb. lin','expansion':'combinaisons linéaires'},{'form':'coeff','expansion':'coefficients'}],
        'check_events':json.loads((OUT/'checks/scan006_check_events.json').read_text()),
        'workflow_note':'Three independent readers completed visual readings and returned 56, 63 and 60 difference rows, with 13, 18 and 21 crops respectively. All report rows map to 68 local decisions, including the final numerator-placement collation from exact reading.tex lines. Root supplied all 68 choices after 25 successful crop views: 20 existing reader crops and five new crops. Root viewed neither a whole-page image nor supplied halves; the mechanical clerk opened no images. A failed combined image call displayed no images and is not counted. All three original reports, exact C/H substrings, full contexts, crop boxes, evidence, confidence and original flags remain auditable. Eleven of 25 original C uncertainties are resolved and fourteen retained; three additional qualifications produce seventeen final doubt entries. The thirty-five inventory entries follow page order. H apparatus and macro/emphasis differences are excluded; global cancellation is already described by H. Shared H omissions/placeholders are counted once at 05, 13, 23 and 41, with local C qualification/state rows cross-referenced. Four actual root events are copied unchanged from the existing event file; no script was rerun. The final candidate page is linked by exact excerpts and SHA-256. Structural checks passed; no TeX compilation was performed.',
        'apparatus_exclusions':[
          {'source':'H.tex lines 2–3','text':wit('H',2,3),'reason':'H describes global cancellation of the old layer; no missing global-state difference is charged.'},
          {'source':'H.tex line 5','text':wit('H',5),'reason':'Editorial layer heading and linking prose, excluded under v05.'},
          {'source':'H.tex line 25','text':wit('H',25),'reason':'Editorial layer heading including f=P/Q context, excluded under v05.'},
          {'source':'H macros and typography','reason':'Macro, emphasis and preamble differences excluded. Endpoint punctuation is retained where root found no corresponding manuscript mark.'}],
        'source_reports':{r:{'path':f'readers/006/{r}/report.json','rows':len(INDEX[r]),'end_utc':REPORTS[r]['end_utc'],'reader_check_events':[]} for r in READY_READERS},
        'final_page':{'path':'pages/J81-01_81_scan006.tex','sha256':hashlib.sha256(FINAL_PAGE_TEXT.encode()).hexdigest(),'unsure_markers':FINAL_PAGE_TEXT.count('\\unsure{'),'compiled':False},
        'root_evidence_log':'checks/scan006_main_decisions.md',
        'mathematical_context_source':'checks/scan006_algebra.md'}
    assert len(record['check_events'])==4
    assert all(x['date']=='2026-11-20 10:27:09 UTC' for x in record['check_events'])
    assert all(REPORTS[r]['check_events']==[] for r in READY_READERS)
    assert sum(x['C_doubt_locus'] for x in decisions)==25
    if ROOT_COMPLETE:
        assert all(x.get('root_decided') for x in decisions)
        doubt_order={key:n for n,key in enumerate(['02','03','04','07','08','09','10','12','14','15','16','18','24','11','59','48','51'])}
        for x in sorted(decisions,key=lambda x:doubt_order.get(x['id'][4:],100)):
            if x.get('C_doubt_status')=='retained' or x.get('new_doubt'):
                record['doubts'].append({'location':x['location'],'reading':x['final'],'alternatives':x.get('alternatives',[]),'confidence':x['confidence'],'reason':x['evidence'],'crop':x.get('crop','')})
    coverage={}
    for role in READY_READERS:
        refs=[sid for links in MAP.values() for sid in links.get(role,[])]
        counts=collections.Counter(refs);missing=sorted(set(INDEX[role])-set(counts));duplicate={k:v for k,v in counts.items() if v>1}
        assert not missing,(role,missing)
        coverage[role]={'total_rows':len(INDEX[role]),'unmapped':missing,'multiple_mappings':duplicate}
    record['source_row_coverage']=coverage
    for x in decisions:
        for r in 'CH':
            assert not x[r] or x[r] in '\n'.join(WITNESSES[r]),(x['id'],r,x[r])
        for crops in x['reader_crops'].values():
            for path in crops:
                assert not path or (OUT/path).is_file(),(x['id'],path)
    (OUT/'checks/scan006_record_draft.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    rows=['# Scan006 — mechanical source-row mapping','',
          'All 68 local choices are supplied by root. The clerk opened no images. Full reader proposals, source contexts, exact final-page excerpts and provenance remain separately preserved. main_adjudicated is false.','',
          '| Decision | Local issue | A rows | B rows | C rows | Root decision |','| --- | --- | --- | --- | --- | --- |']
    for x in decisions:
        rows.append('| '+x['id']+' | '+x['location'].replace('|','\\|')+' | '+' | '.join(', '.join(x['source_map'].get(r,[])) or 'reading.tex' for r in 'ABC')+' | '+('supplied' if x.get('root_decided') else 'pending')+' |')
    rows+=['','## Coverage']
    for role in READY_READERS:
        refs=[sid for links in MAP.values() for sid in links.get(role,[])]
        counts=collections.Counter(refs);missing=sorted(set(INDEX[role])-set(counts));duplicate={k:v for k,v in counts.items() if v>1}
        rows.append(f'- {role}: {len(INDEX[role])} report rows; unmapped {missing}; multiply mapped {duplicate}.')
    rows+=['','Grouped source rows may map to several local decisions; original C uncertainty ownership is assigned once. Exact row wording, original flags, evidence, confidence, crop paths and coordinates are preserved in reader_reports and associated fields.','',
           '## Original C uncertainty loci','',
           '| Decision | A status | B status | C status | Root |','| --- | --- | --- | --- | --- |']
    for key in C_DOUBT_KEYS:
        values=['; '.join(x['id']+': '+str(x['C_doubt_status']) for x in source_rows(key,r) if x['C_doubt_status']) for r in 'ABC']
        rows.append('| 006-'+key+' | '+' | '.join(values)+' | '+('supplied' if key in ROOT_DECISIONS else 'pending')+' |')
    rows+=['','## Reader disagreements and additional comparisons','',
           '- 006-16: first Q² factor is one cancellation-state locus. A starts with live Q²; B with cancelled exponent 2 plus cancelled-Q/live alternatives; C keeps base Q live and qualifies cancellation of exponent 2.',
           '- 006-17: A/B resolve denominator 3; C retains 3/4. 006-18: only B resolves following coefficient 2.',
           '- 006-33: B/C resolve cancelled f in the second delta row. 006-41: only C resolves the prose cancelled f; A/B disclose clipped contextual strokes.',
           '- 006-57: determinant order; 006-58: des/de. C has separate rows; A/B exact reading.tex contexts are supplied.',
           '- 006-59: C adds a comma doubt after the second product; A/B have an unqualified comma in reading.tex.',
           '- 006-60: root confirmed the hooked rule end described by C, and the exact final TikZ is included.',
           '- 006-19: A/B draw the extra partial fraction rule, while C describes it in a comment.',
           '- 006-11: all readers retain a detached point with hand, layer and role unresolved; placement macros differ.',
           '- H shared-span allocation: the ill placeholder at 05, expanded display at 13, lowest fragment at 23 and second prose product at 41 are each counted once. Local C decisions retain coverage links and raw reader flags.',
           '- 006-61: all three reading.tex lines place P-prime and Q-prime over one fraction rule; root confirmed the placement on its already-viewed B01 crop. This differs from H’s factor outside the numerator.',
           '', '## Crop coverage','',
           'All coordinates are full-scan pixels (1231 × 1680). C’s prose predecessor crop is [30,555,1060,667], rotation 180°. A/B disclose clipped prose context. C’s final-system crop [395,25,1120,225] does not include the range near x=200; those range observations rely on its prior half-image reading. The clerk opened no images.',
           '', '## Root-supplied counts','',f"- {len(decisions)} loci; {sum(bool(x['diff_C']) for x in decisions)} C differences; {sum(bool(x['diff_H']) for x in decisions)} H differences.",
           f"- {sum(x.get('C_doubt_status')=='resolved' for x in decisions)} C doubts resolved; {sum(x.get('C_doubt_status')=='retained' for x in decisions)} retained.",
           f"- {len(record['doubts'])} final doubt rows; {len(record['inventory'])} final inventory entries; {len(record['check_events'])} actual root events loaded."]
    (OUT/'checks/scan006_mapping.md').write_text('\n'.join(rows)+'\n')
    print(json.dumps({'loci':len(decisions),'opened_readers':READY_READERS,'root_decided':sum(x.get('root_decided',False) for x in decisions),'main_adjudicated':False}))

if __name__=='__main__':build()
