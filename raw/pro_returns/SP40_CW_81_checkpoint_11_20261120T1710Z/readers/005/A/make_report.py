from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/005/A')
def box(*coords):
    return {'coordinate_system':'original full scan','xyxy':list(coords)}
def row(id,location,C,H,reading,evidence,confidence,kind,diff_C,diff_H,C_doubt_status=None,crop=None,bbox=None,**kw):
    r=dict(id=id,location=location,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=diff_C,diff_H=diff_H,C_doubt_status=C_doubt_status,readers_crop=crop,bbox=bbox)
    r.update(kw)
    return r
D=[
row('005.A.01','Line 1, automorphisme',r'\unsure{automorphisme}','automorphisme','automorphisme','Initial oval a is followed by low connected strokes and a tall t; the latter half has a descender p, a tall h, a separately dotted i, and the shallow isme ending. The complete sequence supports automorphisme; the middle remains compressed rather than absent.','medium','other',True,False,'resolved','crops/01_automorphisme.png',box(680,78,1135,165)),
row('005.A.02','Below the middle of line 1 automorphisme','No isolated point transcribed','No isolated point transcribed',r'\underset{\hspace{-1.3em}\unsure{\cdot}}{\text{automorphisme}}','A tiny, dark, detached point lies below the word, near full-scan (856,171). Its visible shape is point-like; its status as deliberate writing remains unresolved. Conservatively retained as an unsure point for adjudication.','low','omission',True,True,None,'crops/01_automorphisme.png',box(851,166,861,177)),
row('005.A.03','Line 3, after est',r'\unsure{égalmt|également}','également',r'\unsure{égalmt|également}','There is a detached rising accent, a small e, a looped g with long lower return, a tall l, and a very compressed low tail ending in a crossed t-like stroke. The contracted égalmt is the strongest reading; the low connecting strokes do not settle the complete ending.','medium','abbreviation expanded or spelling modernised',False,True,'retained','crops/02_egalmt.png',box(1033,278,1182,361),qualification='The proposed primary reading differs from H; également remains an explicitly doubtful alternative, so this H difference is not a fully resolved exclusion.'),
row('005.A.04','Line 4, first opere',r'\unsure{opere|opère}','opère','opere','The word has an oval o, a long descending p, and low connected remainder. The area above the e contains no detached accent. The second occurrence on line 6 has a separate descending accent and is retained as opère.','high','misread word',True,True,'resolved','crops/03_autc_opere.png',box(920,374,1032,457)),
row('005.A.05','Line 5, l’ens',"l'ens","l'ens.", "l'ens",'The terminal stroke of ens ends near x301, followed by open space before des. No separate point follows the abbreviation. This was settled on half a; no enlargement was needed.','high','other',False,True,None,None,box(147,479,320,550)),
row('005.A.06','Line 5, spèciaux',r'\unsure{spèciaux|spéciaux}','spéciaux','spèciaux','The detached oblique stroke near (615,497) descends to the right. A separate small upper point near (584,481) is also present within the letter group and is retained through the dotted i of the word. The right-descending accent is read as grave, and the final kink plus period are visible.','high','misread word',True,True,'resolved','crops/04_speciaux.png',box(549,474,755,554)),
row('005.A.07','Line 7, Q in Aut',r'\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}}',r'\overline{\mathbb Q}',r'\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}}','A separate bar is above a closed oval Q. The oval is single at its upper portion; the lower left side and the tail have close retraced strokes. Those strokes do not settle ordinary versus deliberately double-stroked Q. Both candidates are retained.','medium','other',False,False,'retained','crops/05_autq.png',box(306,694,350,768),qualification='H’s double-stroked Q is a retained alternative; no confirmed different glyph is asserted against H.'),
row('005.A.08','Below the end of line 8 coeff.','No lower trace transcribed','No lower trace transcribed',r'\underset{\hspace{2.5em}\unsure{-}}{\text{coeff.}}','The abbreviation itself ends with a definite point beside the f crossbar. Farther below and to its right is a short pale horizontal trace near (422,898). It has a dash-like visible shape, but deliberate ink versus a transferred/surface trace remains unresolved. Conservatively retained with an unsure mark.','low','omission',True,True,None,'crops/08_coeff.png',box(406,888,439,906)),
row('005.A.09','Line 9, revient',r'\unsure{revient}','revient','revient','After Il there is a connected r/e/v group, a separately dotted i, a continuing low e/n group, and a final raised crossed t-shaped finish. The word reads revient.','high','other',True,False,'resolved','crops/06_revient.png',box(788,922,935,962)),
row('005.A.10','Line 9, between au and de','au $=$ de','au même de','au $=$ de','Two separate near-horizontal strokes occupy the space after au. There are no letter bodies spelling même at that position.','high','misread symbol or index',False,True,None,'crops/06_revient.png',box(955,925,1187,963),mathematical_consequence='The written equality sign is retained in the running sentence without expanding its verbal meaning.'),
row('005.A.11','First isolated mark below unfinished text',r'\unsure{-|=}','Omitted',r'\unsure{-|=}','The lower short stroke is dark and definite near (374,1427). Above it is a much fainter horizontally distributed trace near y1415. Its pale, uneven appearance leaves unresolved whether the two belong to an equals sign or whether only the dark dash is intentional.','low','omission',False,True,'retained','crops/07_lower_left_mark.png',box(356,1408,393,1433)),
row('005.A.12','Faint isolated trace just right of first lower mark','Omitted','Omitted',r'\unsure{-}','A short, very pale horizontal trace lies to the right of the first lower mark, near (434,1423). It is separated from the dark stroke. Its intention is unresolved; retained as a doubtful dash-like trace.','low','omission',True,True,None,'crops/07_lower_left_mark.png',box(421,1416,452,1430)),
row('005.A.13','Right isolated mark below unfinished text','-','Omitted','-','A single short dark horizontal dash is visible near (920,1426). No accompanying letters or second horizontal stroke was visible on half b.','high','omission',False,True,None,None,box(906,1418,935,1433))
]
report={
 'scan':5,'reader':'A','start_utc':'2026-11-20 10:04:55 UTC','end_utc':'2026-11-20 10:13:11 UTC',
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'differences':D,
 'doubts':[
  {'location':'Line 1, isolated point beneath automorphisme','reading':r'\unsure{\cdot}','alternatives':['intentional detached point','accidental/transferred/surface point'],'confidence':'low','reason':'Shape is visible, intention is not supplied by neighbouring strokes.','crop':'crops/01_automorphisme.png'},
  {'location':'Line 3, contracted égalmt','reading':'égalmt','alternatives':['également'],'confidence':'medium','reason':'The low ending is too compressed to resolve all written letters.','crop':'crops/02_egalmt.png'},
  {'location':'Line 7, barred Q','reading':r'\overline{\mathrm Q}','alternatives':[r'\overline{\mathbb Q}'],'confidence':'medium','reason':'Lower left and tail retracing does not settle whether the Q alphabet is deliberately double-stroked.','crop':'crops/05_autq.png'},
  {'location':'Below line 8 coeff.','reading':r'\unsure{-}','alternatives':['deliberate short stroke','transferred/surface trace'],'confidence':'low','reason':'Pale dash-like trace is visually separated from the abbreviation point.','crop':'crops/08_coeff.png'},
  {'location':'First lower isolated mark','reading':'-','alternatives':['='],'confidence':'low','reason':'The faint upper trace could supply the upper bar, but its status remains unsettled.','crop':'crops/07_lower_left_mark.png'},
  {'location':'Trace just right of first lower isolated mark','reading':r'\unsure{-}','alternatives':['deliberate short stroke','transferred/surface trace'],'confidence':'low','reason':'Trace is pale and isolated; visible shape is retained without assigning intent.','crop':'crops/07_lower_left_mark.png'}
 ],
 'inventory':[
  {'sheet_kind':'text','hand':'his hand','element':'005.A.I01','kind':'text','position':'twelve physical lines from upper heading to lower unfinished sentence','first_words_or_objects':'NB Si σ est un automorphisme','transcribed':'yes'},
  {'sheet_kind':'text','hand':'his hand','element':'005.A.I02','kind':'text','position':'upper left, directly beneath NB','first_words_or_objects':'single short underline beneath NB','transcribed':'yes'},
  {'sheet_kind':'text','hand':'his hand','element':'005.A.I03','kind':'text','position':'line 9, beneath nbs algébriques','first_words_or_objects':'one long underline, slightly sloping, beneath nbs algébriques','transcribed':'yes'},
  {'sheet_kind':'text','hand':'unnamed hand; attribution of trace unresolved','element':'005.A.I04','kind':'text','position':'below middle of first-line automorphisme','first_words_or_objects':'isolated tiny point, uncertain intention','transcribed':'yes'},
  {'sheet_kind':'text','hand':'unnamed hand; attribution of trace unresolved','element':'005.A.I05','kind':'text','position':'below terminal part of coeff. on line 8','first_words_or_objects':'pale short dash-like trace, uncertain intention','transcribed':'yes'},
  {'sheet_kind':'text','hand':'his hand for dark strokes; pale trace attribution unresolved','element':'005.A.I06','kind':'display','position':'below final unfinished line','first_words_or_objects':'doubtful dash/equals, pale dash-like trace nearby, dark dash farther right','transcribed':'yes'},
  {'sheet_kind':'text','hand':'unnamed archive hand','element':'005.A.I07','kind':'text','position':'bottom left near page edge','first_words_or_objects':'archive numeral 4, recorded only in a TeX comment','transcribed':'yes'}
 ],
 'notes':[
  'One handwritten NB paragraph occupies twelve physical lines. It discusses σ, f^σ, Aut(C), Aut(bar Q), coefficients, zeros, and the divisor of f, and ends at est without a completion.',
  'There is no visible manuscript title, date, or authorial page number. The archive numeral is 4 at the lower left and is recorded only in a comment.',
  'No verbal uncertainty by the author was identified in the readable prose. The unsure marks in this return are reader qualifications, not authorial words.',
  'No insertions, deletions, figures, or diagrams were identified. The two underlinings are below NB and nbs algébriques.',
  'H’s final note about where the phrase stops is editorial apparatus. It is not manuscript wording and is excluded from collation.',
  'Per the parent’s convention clarification, H’s emph at NB and nbs algébriques corresponds to the manuscript emphasis. Macro-only emph/uline differences are not counted as H differences.',
  'The coefficient, zero, and divisor wording is retained as written. No mathematical repair, normalization, theorem, or proof check was performed; check_events is empty.',
  'The quotient f=P/Q has plain P and Q, a slash, and an equals sign. The compressed spécial following it was checked in crop 09; its detached rising accent and final comma support the supplied word, so no difference is reported there.',
  'In crop 03 the C has a visible doubled segment on its left; mathbb C is retained without an invented C doubt.',
  'Three additional detached traces are conservatively retained with unsure shapes and exact coordinates. Their presence as visible shapes is distinguished from their unresolved status as deliberate manuscript ink.',
  'The start clock was recorded after reading the brief, preamble, and notation snapshot; packet reads were issued with that clock call. All image reading began afterward.',
  'Dimensions read from the supplied files: whole 1231×1678, half a 1231×919, half b 1231×919. Half a origin is (0,0); half b origin is (0,759), from 1678−919. All boxes in this report use original full-scan coordinates.'
 ],
 'notation':[
  {'location':'Lines 1 and 3','sign':'arched σ, also raised above f','latex':r'\sigma; f^\sigma','evidence':'Small arch-like letter in line 1; corresponding raised arch above the line-3 f.'},
  {'location':'Line 3','sign':'double quotation ticks around spécial','latex':"``spécial''",'evidence':'Two separate short opening ticks and two closing ticks; comma follows.'},
  {'location':'Line 4','sign':'Aut(C)','latex':r'\operatorname{Aut}(\mathbb C)','evidence':'Tall A; capital C with visible doubled portion along its left side; round parentheses.'},
  {'location':'Line 5','sign':'ens','latex':'ens','evidence':'Compressed abbreviation without a detached terminal point.'},
  {'location':'Line 7','sign':'barred Q','latex':r'\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}}','evidence':'Distinct upper bar; lower-left and tail retracing leave the alphabet uncertain.'},
  {'location':'Line 7','sign':'quotient with plain capitals','latex':'f=P/Q','evidence':'Equals sign and slanted fraction stroke between ordinary P and Q.'},
  {'location':'Line 8','sign':'coeff.','latex':'coeff.','evidence':'Two tall f forms and definite separate point at the right of their crossbar.'},
  {'location':'Line 9','sign':'symbol in prose au = de','latex':'au $=$ de','evidence':'Two separate horizontal strokes between au and de.'},
  {'location':'Line 11','sign':'i.e.','latex':'i.e.','evidence':'Dotted i, following punctuation and terminal point after e.'}
 ],
 'check_events':[],
 'crops':json.loads((root/'crop_manifest.json').read_text()),
 'brief_feedback':[
  'The instruction to retain every detached mark provides no separate convention for a visible trace whose intention is unresolved. This return uses positional underset plus unsure for the point and lower abbreviation trace, and an unsure dash in the lower display. Their uncertain status is explicitly recorded for root adjudication.',
  'The source has many very pale paper traces. The three isolated traces specifically flagged here were recorded because they were noticed at the required enlarged loci; no text was reconstructed from the surrounding paper texture.'
 ],
 'view_log':{'whole_image_views':1,'half_a_views':1,'half_b_views':1,'crop_views':{p['path']:1 for p in json.loads((root/'crop_manifest.json').read_text())},'ocr_used':False,'external_research_used':False,'other_pages_or_readers_read':False,'delegation_used':False},
 'visual_read_attestation':'I visually read all twelve physical text lines against C and H from the whole layout view and the supplied halves, then viewed each of the nine listed local enlargements once. The page’s underlining, punctuation, algebraic symbols, lower isolated marks, and archive numeral were included in the pass. Remaining uncertainties are explicit in reading.tex and the doubts list.'
}
for item in report['inventory']:
    h=item['hand']
    if h.startswith('unnamed hand;'):
        item['hand']='unnamed hand'
        item['attribution_note']='Attribution and deliberate manuscript status of this trace remain unresolved.'
    elif h.startswith('his hand for'):
        item['hand']='his hand'
        item['attribution_note']='Attribution of the intervening pale trace remains unresolved.'
    elif h=='unnamed archive hand':
        item['hand']='unnamed hand'
        item['attribution_note']='Archive numeral, recorded only as a TeX comment.'
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
