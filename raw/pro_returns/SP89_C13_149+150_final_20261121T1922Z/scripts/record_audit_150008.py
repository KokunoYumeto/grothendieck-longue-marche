from audit_record import AuditRecord
A=AuditRecord('150_scan008')
e='The compressed word after the three Sigma objects favors espaces, but its small low joins do not fully exclude esp. The following top. remains abbreviated. The literal first inclusion repeats Sigma_01; the neighboring products do not authorize replacing its right member.'
n=A.c['B01']['first'].replace('espaces top.',r'\unsure{espaces|esp.} top.')
A.decide('B01',e,n,'Preferred espaces retained with an abbreviation alternative; no new primary C correction for uncertainty alone.')
A.replace('espaces top.',r'\unsure{espaces|esp.} top.')
A.doubt('Opening espaces / esp.',r'\unsure{espaces|esp.}','espaces | esp.',e)
A.inventory('E01',first_words_or_objects=r'Sigma_0, Sigma_1, Sigma_2 \unsure{espaces|esp.} top.')
A.decide('B02','The crossed initial a)-like label, Posons, product inclusion and vertical two-bar identity are all present. The lower expression is the intersection of the two parenthesized products. The second array changes alignment encoding only.')
A.decide('B03','The live wording is On veut que and de sorte qu’on a un diagramme commutatif. Sigma_012 maps to Sigma_0 times Sigma_2, with image contained in Sigma_02. Arrow-command length and apostrophe encoding account for the differences.')
old=r'\draw[dash pattern=on 2.6pt off 2pt] (2.5,-0.04) .. controls (2.3,-0.35) and (2.75,-0.42) .. (3.1,-0.36);'
new=old+'\n'+r'\draw (3.00,-0.25)--(3.12,-0.36)--(3.00,-0.47);'
n=A.c['B04']['first'].replace(old,new)
e='The seven object labels and ten solid arrows remain supported. Upper cart is crossed; lower cart is live. The right lower label uses rounded delimiters (ell), while three other labels use square brackets. The broken curved stroke below the middle rightward arrow ends in a distinct right-facing two-arm chevron, omitted from the first geometric transcription; restore those two short strokes literally.'
A.decide('B04',e,n);A.replace(old,new);A.change('P04_a',final=n,evidence=e)
A.inventory('E07',first_words_or_objects='Seven objects, ten solid arrows, five broken curved/hook strokes including a right-facing terminal chevron below the middle arrow, four ell labels and two cart labels')
A.decide('B05','The low star-like mark after Sigma has several short branches and remains the preferred star; the disjoint-union signs and bracketed [0,1,2] are clear. The rotated prose reads signifie que / sur / on a une relation d’ordre / au dessus de. No source revision is required for the second reader’s star uncertainty.')
mapold=r'\Sigma_{12}\longrightarrow\Sigma_2'
mapnew=r'\Sigma_{12}\mathrel{\unsure{-|\longrightarrow}}\Sigma_2'
n=A.c['B06']['first'].replace(mapold,mapnew)
e='The third upper connector is a short horizontal shaft whose end lacks the separate paired head strokes present in the clear arrows elsewhere on the leaf. Prefer a bare connector while retaining an arrow interpretation locally. The underlined bordants and both parenthetical groups remain; donc aussi below belongs to the following insertion.'
A.decide('B06',e,n);A.replace(mapold,mapnew)
A.new_change('A01','B06','Third b) connector head',mapold,mapold,mapnew,e,'drawing or diagram',True,True,'low',consequential=True,error_category='4')
A.doubt('Third b) connector',r'\unsure{-|\longrightarrow}','bare shaft | arrow',e)
upold=r'\overset{\deleted{\unsure{}}}'
upnew=r'\overset{\deleted{\unsure{}}\,\unsure{b)|\deleted{b)}|c)}}'
n=A.c['B07']['first'].replace(upold,upnew)
e='The raised replacement has the distinct et, a, tall f and successive ortiori strokes; it reads et a fortiori, not est fermé. Donc aussi remains attached by its bent leader. The overworked target 0 and cancelled equivalence remain uncertain. Above that sign a cancelled illegible prefix is followed by a legible b)-like tail; b), cancelled b), and c) remain alternatives for the tail and its state.'
A.decide('B07',e,n);A.replace(upold,upnew)
raised=r'\deleted{\unsure{}}\,\unsure{b)|\deleted{b)}|c)}'
A.change('P07_e',final=raised,evidence=e)
A.update('doubts','place','P07 raised obliterated item',reading=raised,alternatives='cancelled illegible prefix; b)-like tail, possibly cancelled b) or c)',reason=e)
A.update('deletion_insertion_review','text','raised obliterated item',scope_attachment='Cancelled illegible prefix and uncertain b)-like tail above the separate equivalence sign.',evidence=e)
A.inventory('E16',first_words_or_objects='Cancelled illegible prefix with b)-like tail and separate doubtful cancelled equivalence beneath')
old=r'\unsure{sous que}';new=r'\unsure{sous|suit|suffit} que'
n=A.c['B09']['first'].replace(old,new)
e='The end of the first line gives p.r. à and the next line begins un morphisme bordant; the source is not changed to au morphisme. After Cela, a separate s-like opening and low joined body precede a raised loop with a long return. Sous remains provisional; suit and suff it contracted as suffit remain alternatives. No complete signifie is visible. Preserve the written final closing parenthesis without inventing an opening one.'
A.decide('B09',e,n,'Preferred sous retained and alternatives added; no new primary C correction for the new doubt alone.')
A.replace(old,new);A.change('P09_d',final=new,evidence=e)
A.update('decisions','id','M0303',reading=new,evidence=e)
A.update('doubts','place','P09 phrase after Cela',reading=new,alternatives='sous | suit | suffit, followed by que',reason=e)
A.inventory('E20',first_words_or_objects='Sigma_12 to Sigma_1 est transversal p.r. à un morphisme bordant; Cela unsure sous/suit/suffit que ... bordant)')
first=A.c['B11']['first']
oldmap=r'\Sigma_{012}\xrightarrow{[\mathrm{liss}]}\Sigma_{02}'
newmap=r'\Sigma_{012}\overset{[\mathrm{liss}]}{\mathrel{\unsure{-|\longrightarrow}}}\Sigma_{02}'
n=first.replace(r'\Sigma_{12}\xrightarrow{(\mathrm{liss}]}',r'\Sigma_{1,2}\xrightarrow{(\mathrm{liss}]}').replace(oldmap,newmap).replace(r'\deleted{\unsure{donc}}',r'\deleted{\unsure{donc|et}}')
e='The third upper source index has a separate descending comma between 1 and 2. The liss labels end before a separate e, and the third upper label retains its mixed (liss] delimiters. The first lower labelled connector has a horizontal shaft with no secure head, so its bare-shaft reading is preferred locally. The crossed small word after lower fibrant remains unresolved between inherited donc and the second reader’s et; no preceding comma is visible. The final source retains its written 0,12 comma.'
A.decide('B11',e,n)
A.replace(r'\Sigma_{12}\xrightarrow{(\mathrm{liss}]}',r'\Sigma_{1,2}\xrightarrow{(\mathrm{liss}]}')
A.replace(oldmap,newmap);A.replace(r'\deleted{\unsure{donc}}',r'\deleted{\unsure{donc|et}}')
A.change('P11_b',final=r'\Sigma_{1,2}\xrightarrow{(\mathrm{liss}]}\Sigma_1',evidence=e)
A.change('P11_d',final=newmap,evidence=e,against_c=True,against_h=True,confidence='low')
A.change('P11_e',final=r'fibrant \deleted{\unsure{donc|et}} et',evidence=e)
A.new_change('A02','B11','Third upper f) source-index comma',r'\Sigma_{12}',r'\Sigma_{12}',r'\Sigma_{1,2}',e,'omission',True,True,'high',consequential=True,error_category='3')
A.update('doubts','place','P11 cancelled donc',reading=r'\deleted{\unsure{donc|et}}',alternatives='donc | et',reason=e)
A.doubt('First lower f) connector',newmap,'bare shaft | arrow, with liss label',e)
A.inventory('E24',first_words_or_objects='doubtful cancelled donc|et after lower fibrant')
A.update('deletion_insertion_review','text','donc after lower fibrant',text='donc|et after lower fibrant',evidence=e)
verb=r'\unsure{renforcer|remplacer}'
n=A.c['B12']['first'].replace('remplacer',verb)
e='In the rotated note the disputed verb has one dominant looped descender and tall crossing, consistent with f in renforcer. The separate p followed by l required by remplacer is not securely visible. Prefer renforcer with remplacer retained. The reference (f), comma after the verb, par la condition que le diagramme, the two outward arrows, au dessus, loc raised t and final period remain visible.'
A.decide('B12',e,n);A.replace('remplacer',verb)
for id in ['P12_a','P12_b']:
 A.change(id,final=A.get('changes','id',id)['final'].replace('remplacer',verb),evidence=e,confidence='low')
A.update('decisions','id','M0304',decision='undecided',reading='devrait se '+verb,evidence=e,confidence='low')
A.doubt('Lower marginal verb',verb,'renforcer | remplacer',e)
A.inventory('E25',first_words_or_objects='(f) devrait se unsure renforcer|remplacer, par la condition ... est loc raised t trivial sur Sigma_0.')
A.update('notes','id','N01',text=A.get('notes','id','N01')['text'].replace('as a replacement for f)','as the proposed strengthening/replacement of f), with renforcer preferred and remplacer still possible'))
A.append('notes',id='N10',text='Main reader inspected all ten nonidentical independent targets. The lower marginal verb now favors renforcer; the short phrase after Cela remains unresolved. The third upper f) source has a comma in 1,2. Locally incomplete arrowheads and the chevron on the broken central-diagram stroke are recorded from the ink, without changing the conditional mathematical checks in N07–N09.')
A.append('check_events',statement_id='150008-independent-audit',type='independent image comparison',outcome='All ten differing targets personally inspected; targeted crops used for Cela, cancelled small word, and raised label tail.')
A.save()
