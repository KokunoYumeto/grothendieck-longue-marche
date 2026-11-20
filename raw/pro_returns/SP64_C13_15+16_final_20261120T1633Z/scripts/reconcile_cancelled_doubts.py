"""Primary reader's complete disposition register for C's struck-text doubts.

The explicit readings below were decided during the two visual readings. Exact
string checks here verify their presence; they do not choose readings.
"""
from workflow import *
from audit_uncertainty import parse_page
from report_helpers import mdcell

chosen={
 '15/183':{3:r'\unsure{point de vue}',4:'dupliquer',10:r'\unsure{divisé|désigné}',12:'F',15:r'\unsure{intérieur|intérieurs}'},
 '15/185':{11:'classes de'},
 '15/187':{1:"u(s')"},
 '15/191':{1:r'\unsure{(réduite, ce qui ne restreint p|réduit, ce qui ne restreint p}',3:'On',5:r'\text{de t.f. sur}',7:r'\mathbb{W}',12:r'\unsure{pts}',13:'On',17:'soit un'},
 '15/193':{9:'aie',15:'il est',16:'sont',25:'est'},
 '16/003':{6:r'\mathrm{gr}',8:'par'},
 '16/004':{1:'algèbre',7:"d'où",8:'la relation',9:r'\unsure{\pi_\nu|\pi_j|\pi_{i+\nu}}',14:'de',15:'voulons',16:'supp'},
 '16/005':{1:r'les $\pi_i$ \unsure{de} degré zéro',3:'Supp',4:"Supposons, établi l'unicité",15:r'\unsure{Considéré|Considé}',16:r'\illegible{1}'},
 '16/006':{3:'qui',5:r'\unsure{\forall\alpha}\ \pi_\alpha u=0\ (\text{\unsure{pour}}\ \alpha\neq i),',7:r'\pi_\alpha u=0\ (\text{\unsure{pour}}\ \alpha\neq2n-i),',8:r'\pi_i(\mathfrak Z\mathcal E^0)',14:'suff'},
 '16/007':{3:'=0'},
 '16/008':{3:'que',10:'donc'},
 '16/009':{4:'Ceci'},
 '16/010':{3:'Une graduation',4:'pour un',6:'tel choix',16:'1',17:'6.7',21:'6.7'},
 '16/011':{1:r'\in',3:r'\pi_{j\alpha}',4:'Car'},
 '16/012':{2:'il',8:'poser',10:'-',15:r'\Lambda\pi_{i,\alpha}'},
 '16/013':{6:r'\pi_{2n-i}',7:r'\pi_{2n-i}'},
 '16/014':{1:'2',5:r'\mathcal E',7:r'\xi',13:r'\xi'},
 '16/015':{3:r'L^j',8:r'L_0^{\beta-\alpha}',9:'2n',13:r'\unsure{\varphi_{i,\alpha}^{j,\beta}\varphi_{i\prime,\alpha\prime}^{j\prime,\beta\prime}}'.replace(r'\prime',"'")},
 '16/016':{7:'représentation',13:'avec',14:'voit donc',15:'0',22:'Pour',23:r'\boldsymbol\Lambda'},
}
special={
 ('16/015',8):'C duplicated the beta-minus-alpha expression. The ink belongs to the exponent of the old L_0 below the replacement definition; retained once in that cancelled formula.',
 ('16/015',13):'The old product remains cancelled. The single surviving equality sign is placed to its right and shared with the replacement product; C supplied a second equality in the old expression.',
 ('16/005',16):'The struck fragment is physically obscured; the final retains one illegible word before the separate live de.',
 ('16/006',5):'The cancelled hypothesis retains its legible core. Additional forall-alpha and pour traces remain doubtful in place.',
 ('16/006',7):'The cancelled hypothesis retains its legible core; the short pour trace remains doubtful in place.',
}
cert=readrows('certainty_only.tsv')
result=[]; source_live=[]
for cote,scan in ORDER:
 key=cote+'/'+scan
 source=parse_page(SRC/'pages'/f'{cote}_scan{scan}.tex')
 final=(WORK/'pages'/f'{cote}_scan{scan}.tex').read_text()
 for o in source.occurrences:
  if not o.inside_deleted:
   source_live.append((cote,scan,o.raw));continue
  reading=chosen.get(key,{}).get(o.ordinal,o.raw)
  assert reading in final,(key,o.ordinal,reading)
  uncertain=r'\unsure{' in reading or r'\illegible{' in reading
  status='retained uncertainty' if reading==o.raw else ('revised uncertainty' if uncertain else 'resolved reading')
  if (key,o.ordinal)==('16/015',8):status='duplicate assigned to its written exponent'
  if (key,o.ordinal)==('16/015',13):status='cancelled product and single shared equality'
  matches=[r for r in cert if r['scan']==key and r['old_mark']==o.raw and r['reading']==reading]
  evidence=matches[0]['evidence'] if matches else special.get((key,o.ordinal),
   ('The final retains the unresolved strokes explicitly. See this scan in the remaining-doubts and crop registers; the second visual reading did not settle them.' if uncertain else
    'The primary reader retained this visible reading after both scan readings. Its cancellation remains in the transcription; see the page change and certainty registers.'))
  confidence=matches[0]['confidence'] if matches else ('low' if uncertain else 'medium')
  line=source.text.count('\n',0,o.start)+1
  result.append(dict(cote=cote,scan=scan,C_occurrence=str(o.ordinal),C_line=str(line),C_mark=o.raw,final_reading=reading,disposition=status,evidence=evidence,confidence=confidence))

# The 151 live macros and the supplied 151 marks have the same page order.
marks=__import__('csv').DictReader((SRC/'MARKS.tsv').open(),delimiter='\t')
marks=list(marks)
assert len(source_live)==len(marks)==151
for (cote,scan,raw),mark in zip(source_live,marks):
 assert cote==mark['cote'] and int(scan)==int(mark['scan'])
 assert raw==mark['the mark as written'].replace('\\\\','\\'),(cote,scan,raw,mark['id'])
assert len(result)==137
name='cancelled_doubt_review.tsv'
HEADERS[name]=['cote','scan','C_occurrence','C_line','C_mark','final_reading','disposition','evidence','confidence']
write_rows(name,result)

p=WORK/(PREFIX+'_doubts.md');existing=p.read_text()
start='<!-- BEGIN CANCELLED DOUBT AUDIT -->';end='<!-- END CANCELLED DOUBT AUDIT -->'
assert start not in existing
lines=[start,'## Complete audit of C uncertainty in struck text','',
 'The primary reader reviewed all 288 uncertainty macros in witness C: the 151 live marks correspond in order to `MARKS.tsv` and `decisions.tsv`; the 137 occurrences inside cancellations are accounted for below and in `cancelled_doubt_review.tsv`. C occurrence numbers count all uncertainty macros on that page. These are reading dispositions, not additional change counts.','',
 '| Scan | C occurrence / line | C uncertainty | Final reading | Disposition | Confidence |',
 '| --- | --- | --- | --- | --- | --- |']
for r in result:
 lines.append('| '+' | '.join(mdcell(v) for v in [r['cote']+'/'+r['scan'],r['C_occurrence']+' / '+r['C_line'],r['C_mark'],r['final_reading'],r['disposition'],r['confidence']])+' |')
lines += [end,'']
p.write_text(existing+'\n\n'+'\n'.join(lines))
log('complete C uncertainty reconciliation '+now()+': 288 macros reviewed by primary reader; 151 live macros matched exactly in supplied MARKS order; 137 struck-text dispositions recorded and checked for literal presence in the final pages')
print('Recorded 137 struck-text dispositions; matched 151 live source marks.')
