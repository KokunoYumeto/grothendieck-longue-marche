from pathlib import Path
import json

ROOT=Path('/workspace/scratch/d7279cb02214')
WORK=ROOT/'SP92_C13_150+151_work'
PAGE='151_scan006'
p=json.loads((ROOT/'reading_packets'/PAGE/'packet.json').read_text())
cm=json.loads((WORK/'records'/(PAGE+'_cropmap.json')).read_text())
C=p['witness_C']
assert p['witness_H'] is None and p['differences']==[]

candidate=C.replace(r'\scanpage{6}',r'\scanpage{6}'+'\n% The source letter is upside down; typed reading order is restored.')
candidate=candidate.replace(r'\illegible{1}'+'\n'+r'\unsure{ROUX}',
 r'% Unreadable autograph; its looped flourish is not a cancellation.'+'\n'+
 r'\handwritten{\illegible{1}}'+'\n\n'+
 r'% A separate line below the autograph is clipped to character tops. No missing lower letter parts are reconstructed.'+'\n'+
 r'\illegible{1}')

change={
 'id':'C01','place':'lower name line at the original upper image edge, below the autograph in upright orientation',
 'C':r'\unsure{ROUX}','H':None,'final':r'\illegible{1}',
 'evidence':'Four separated character-top groups survive: a squared upper bowl, a rounded upper bowl, two upright strokes, then two sloping strokes. ROUX is compatible with these tops, but the first character’s distinguishing lower leg, the third character’s base and the final crossing are outside the image. No complete four-letter reading can be certified from this scan. The fragment is kept separately without completing its missing letter bodies.',
 'crop':cm['clipped_name']['crop'],'box':cm['clipped_name']['box'],
 'confidence':'high','kind':'text not on the page','error_kind':'9 not on page',
 'against_C':True,'against_H':False,'consequential':False,'marked_in_H':False
}
decisions=[
 {'id':'M0752','cote':'151','scan':'6','decision':'undecided','reading':r'\illegible{1}',
  'ink':'A tall curved stem with a lower loop, a detached small upper loop, a rounded middle loop and narrow turns merge with a long crossing flourish. Their letter divisions are not securely recoverable. The typed sender name is not used to reconstruct the autograph.',
  'crop':cm['signature_detail']['crop'],'box':cm['signature_detail']['box'],'confidence':'low'},
 {'id':'M0753','cote':'151','scan':'6','decision':'undecided','reading':r'\illegible{1}',
  'ink':'Four upper character groups are visible, compatible with ROUX but not diagnostic: the first group lacks a visible lower leg, the two upright strokes lack their base, and the final sloping pair lacks its crossing. Most of the line lies beyond the image edge. The complete word remains undecided.',
  'crop':cm['clipped_name']['crop'],'box':cm['clipped_name']['box'],'confidence':'low'}
]

inventory=[]
def inv(element,kind,position,words,hand='typed letter'):
 inventory.append({'sheet_kind':'letter','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'transcribed':'yes'})
inv('upper rule','text','upright top, above letterhead','long horizontal rule','printed/copied rule')
inv('letterhead with separator rules','text','upright upper left',"ACADEMIE D'AIX-MARSEILLE / INSPECTION ACADEMIQUE / DE VAUCLUSE",'printed letterhead')
inv('place and date','text','upright upper right','AVIGNON le 6 décembre 1990')
inv('sender block','text','upright right beneath date',"Jacques ROUX, responsable / départemental de l'Action / Culturelle,")
inv('administrative reference','text','upright left below letterhead','C.D.A.C.N°16')
inv('recipient placeholders','text','upright right below sender','à / M; no recipient name written')
inv('subject and school year','text','upright middle above fold',"OBJET : Projets d'Action Educative Collège. / Année scolaire 1990/1991")
inv('introductory paragraph','text','upright middle below fold',"L'attribution des aides aux P.A.E. se déroulera cette année en deux temps :")
inv('December schedule','text','upright middle',"DECEMBRE - instruction des dossiers / par l'Inspection Académique / propositions à la M.I.A.D.A.C.")
inv('January schedule','text','upright lower middle',"JANVIER - Monsieur le Recteur attribue / une aide globalisée à Monsieur / l'Inspecteur d'Académie.")
inv('closing paragraph','text','upright lower body','Une commission se réunit vers le 15 janvier 1991 ... de participer à cette Commission.')
inv('authority line','text','upright lower right',"P/L'Inspecteur d'Académie")
inv('autograph with flourish','text','upright bottom, above clipped line','unreadable signature','signatory hand as reproduced; not identified letter by letter')
inv('clipped lower line','text','upright extreme bottom; original upper image edge','four character-top groups, remaining bodies lost','lettering too clipped to classify securely')
inv('other-hand foliation','margin note','original bottom left; opposed to letter orientation','5','other hand: thin light foliation')

second_boxes=[]
def blind(kind,name,reading):
 v=cm[name]; b=v['box']
 second_boxes.append({'box':f'B{len(second_boxes)+1:02d}','kind':kind,'x0':b[0],'y0':b[1],'x1':b[2],'y1':b[3],'reading':reading,'rotation':v['rotation']})
blind('typed accented word and excluded irregular copy marks','inspection_accent',r"par l'Inspection Académique")
blind('complete word at the paper edge','edge_alors','alors')
blind('whole autograph plus separate clipped lower line, both supplied C marks','signature_detail',r'\handwritten{\illegible{1}}\par\illegible{1}')
blind('separate clipped lower line','clipped_name',r'\illegible{1}')
blind('handwritten foliation','folio5',r'\margin{5}')

notes=r'''# 151_scan006 — reader A

This leaf is a typed administrative letter on a printed letterhead. Its text is upside down in the source photograph. I read this assigned original for layout, then its two supplied native halves after 180-degree rotation, without consulting another page. The foliation 5 is in a thin light hand upright in the source scan, thus opposed to the letter’s reading direction; it is a margin item, not an authorial manuscript page number. There is no mathematical text or authorial handwritten date.

The printed letterhead reads ACADEMIE D'AIX-MARSEILLE / INSPECTION ACADEMIQUE / DE VAUCLUSE. The typed date is AVIGNON le 6 décembre 1990. The sender block names Jacques ROUX, responsable départemental de l'Action Culturelle. The recipient area contains only à and M, with the name left blank. The subject is Projets d'Action Educative Collège, for the school year 1990/1991. The December rows concern dossier examination by the Inspection Académique and proposals to the M.I.A.D.A.C.; the January rows concern an allocation by the Recteur to the Inspecteur d'Académie. The closing paragraph places a commission around 15 janvier 1991 and says the recipient will then be asked to participate. These statements describe this letter’s ink, without external verification or institutional reconstruction.

## Complete typed-text review

All wording was checked directly against the native images, including the letterhead, reference C.D.A.C.N°16, the date, capitalizations, the two year forms, the blank recipient placeholders, each stop in P.A.E. and M.I.A.D.A.C., and P/L. The printed ACADEMIE/ACADEMIQUE and typed DECEMBRE/Educative remain unaccented where printed that way. The accents in the body and date are retained. The first commission is lower case and the closing Commission has a capital C. OBJET is underlined. The long top rule and two short letterhead rules remain separators; there is no evidence that they cancel wording.

The body word Académique has a clear acute over é. Small irregular ink marks above c and a are not recognizable typewriter diacritics; they are excluded as uncertain copy artifacts. No extra accent or typographical correction is supplied. The right-edge word alors was enlarged: its last s is visible in full before the border, so the word is not truncated. Scattered dots, stains and the fold are not transcribed.

## Signature and image-edge loss

The autograph below P/L'Inspecteur d'Académie has a tall curved stem, lower loop, detached upper loop, rounded middle loop, narrow turns and long oval/crossing flourishes. These cannot be divided into secure letters, so M0752 remains an illegible signature. Its horizontal flourish is not a cancellation of the authority line and is not drawn as a substitute for text.

A separate lower line is clipped by the image edge. Four upper groups survive: a squared bowl, rounded bowl, paired upright strokes and paired sloping strokes. Those tops are compatible with C's conjectural ROUX, but do not expose the diagnostic lower parts needed to distinguish the letters. In particular, no lower R leg, U base or X crossing survives within the image. M0753 therefore remains undecided, and the clipped fragment is represented separately as illegible rather than completing the word. This decision rests on this scan’s exposed strokes; the typed sender name is not used to fill the missing parts.

No deletion, insertion or securely separable typed overstrike was found. The autograph and foliation are the handwritten items requiring blind rereading. H is absent for the whole page and there are no supplied C/H difference rows. No mathematical check, computation, external research or TeX compilation was performed.
'''

record={
 'page':PAGE,'cote':'151','scan':6,'reader':'reader_a / GPT-6 Astra Pro / effort not exposed / run SP92',
 'line_count':28,
 'line_count_note':'28 written line units: letterhead3, date1, sender3, reference1, recipient placeholders2, subject/year2, introductory paragraph2, December schedule3, January schedule3, final paragraph4, authority line1, autograph1, clipped lower line1, foliation1. Separate columns count separately; horizontal rules are excluded.',
 'half_review':'Whole original viewed once. Each supplied native half was rotated180 degrees without resizing and viewed once in upright reading order, half2 then half1. Every typed word, numeral, punctuation mark, accent, rule, placeholder and handwritten item was inspected against this page’s C. H is absent. All six saved tight evidence crops were viewed. Upright native previews are in reading_packets/151_scan006, outside deliverable crops. No OCR, external research or compilation.',
 'deletion_insertion_review':[
  {'place':'entire letter','state':'no deletion or insertion found','bounds':'C has no deletion/insertion macros. The letterhead, body, date, references and closing were checked; no securely separable typed overstrike was identified.','attachment':'The three horizontal printed/copied rules are separators, not strikes.','reading':'Visible typed wording retained.','confidence':'high','crop':None,'box':None},
  {'place':'signature flourish','state':'autograph stroke, not deletion','bounds':'The long oval and crossing sweep belong to the signature below the authority line, and do not cancel that typed line.','attachment':'Autograph above a separate edge-clipped line.','reading':r'\handwritten{\illegible{1}}','confidence':'high','crop':cm['signature_detail']['crop'],'box':cm['signature_detail']['box']}
 ],
 'changes':[change],'diff_coverage':[],'decisions':decisions,'inventory':inventory,'notes':notes,'check_events':[],
 'notation':[
  {'sign':'thin 5','reading':r'\margin{5}','evidence':'Upper bar, short downward/curved middle and lower rounded turn in another hand, upright only in the original scan orientation.'},
  {'sign':'P/L','reading':'literal typed short form P/L','evidence':'Capital P, slash and capital L before the apostrophe; not expanded in the text.'},
  {'sign':'lower clipped four-character group','reading':r'\illegible{1}','evidence':'Only upper bowls/uprights/oblique strokes survive; missing letter bodies are not reconstructed.'}
 ],
 'hand_log':[
  {'habit':'This copied letter’s printing and signature are distinct from the mathematical manuscript hand','places':['entire page'],'scope':'151_scan006 only','witness_errors':'No mathematical glyph habit is used to identify the autograph.'},
  {'habit':'Signature flourishes cross without indicating deletion','places':['autograph below authority line'],'scope':'the signatory hand as reproduced on this page','witness_errors':'C’s illegibility is retained; no complete signature word is recovered.'},
  {'habit':'Physical clipping can leave non-diagnostic upper letter groups','places':['lower separate line, M0753'],'scope':'this image edge','witness_errors':'C’s full-word ROUX conjecture is not asserted from only upper bowls and strokes.'},
  {'habit':'Light foliation has its own orientation','places':['original bottom-left5'],'scope':'this leaf','witness_errors':'C’s margin convention is retained.'},
  {'habit':'Irregular copy marks above typed letters can imitate accents','places':['c/a in body Académique'],'scope':'this photocopied line','witness_errors':'No additional accent is introduced.'}
 ],
 'abbreviations':[
  {'form':'M','expansion':'Monsieur; typed recipient placeholder, left unexpanded'},
  {'form':'P/L','expansion':'Pour l’ — retained literally'},
  {'form':'P.A.E.','expansion':'Projets d’Action Educative, supplied by the subject line'},
  {'form':'C.D.A.C.','expansion':'Not expanded on the page'},
  {'form':'M.I.A.D.A.C.','expansion':'Not expanded on the page'},
  {'form':'N°','expansion':'Numéro; retained literally'}
 ],
 'doubts':[
  {'place':'autograph, M0752','reading':r'\illegible{1}','alternatives':'No name is secure letter by letter.','confidence':'low','reason':'Tall loops and compressed turns overlap an extended flourish; the typed sender name cannot establish the signature’s letters.'},
  {'place':'edge-clipped lower line, M0753','reading':r'\illegible{1}','alternatives':'ROUX is compatible with the upper groups but remains unconfirmed.','confidence':'low','reason':'The character bodies needed to distinguish the first, third and fourth letters lie beyond the image edge.'}
 ],
 'second_boxes':second_boxes,
 'crops':[{'place':name,**v,'viewed':True,'method':'Pillow crop of assigned original; 180-degree rotation except foliation; LANCZOS enlargement, autocontrast, sharpness1.15.'} for name,v in cm.items()]
}

assert change['C'] in C and change['H'] is None
assert [d['id'] for d in decisions]==[m['id'] for m in p['marks']]
assert len(cm)==6 and all((WORK/v['crop']).exists() for v in cm.values())
(WORK/'records'/(PAGE+'.tex')).write_text(candidate)
(WORK/'records'/(PAGE+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(f'Saved {PAGE}: 1 change, 2 unresolved marks, 15 inventory entries, 5 blind boxes, 6 viewed crops.')
