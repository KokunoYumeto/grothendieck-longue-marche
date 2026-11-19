from pathlib import Path
import json
out=Path('/workspace/scratch/17347c1714f0/out/readers/scan004/R2')
source=Path('/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans')
base=source/'J71-01_71_scan004.jpg'
a=source/'J71-01_71_scan004_a.jpg'
b=source/'J71-01_71_scan004_b.jpg'
signature=r'\handwritten{\unsure{E S|E Siau}}'
added=r'''\draw[thin,black!55] (-2.22,-.72)
 .. controls (-1.28,-.40) and (.16,.17) .. (.88,.37);'''
report={
  'scan':4,'reader':'R2','model':'inherited parent model','effort':'inherited; value not independently exposed',
  'started_utc':'2026-11-19T22:12:42Z','finished_utc':'2026-11-19T22:16:09Z',
  'images_viewed':[str(base),str(a),str(b)],
  'crops':[{'file':str(out/'signature.png'),'source':str(b),'box':[900,735,1440,925],'rotation':0,'scale':2800/540,'output_width':2800,'place':'Autograph and full long return flourish below Le Secrétaire Général; typed name supplies line context.','observed':'Two tall cursive forms support E S. The tiny dark strokes following the second letter do not settle whether a compressed surname follows. Retained E S|E Siau. The flourish has two separate long edges from the left return: a steeper edge ascending into the signature, and a shallower edge leading to the far-right return. C draws only one long left-to-right edge plus the short right-to-signature return; a second ascending edge is added.'}],
  'findings':[
    {'id':'R2-004-01','place':'Handwritten autograph below Le Secrétaire Général','c':signature,'h':None,'reading':signature,'diff_c':False,'diff_h':False,'c_doubt':True,'s_id':None,'kind':'other','marked_in_H':False,'evidence':'One enlarged autograph crop: first form has upper and lower curls joined by a descending stroke; second has a tall upper turn and lower hooked return. These support E S. A few very short dark strokes continue to the right before the flourish, but no distinct complete i/a/u sequence can be securely separated. E S remains first candidate; the fuller candidate remains unresolved. Typed E. SIAU is not treated as a decisive reading of the autograph.','crop':str(out/'signature.png'),'confidence':'low','unresolved':True,'consequential':False},
    {'id':'R2-004-02','place':'Long autograph flourish: ascending edge from left return into letters','c':'','h':None,'reading':added,'diff_c':True,'diff_h':False,'c_doubt':False,'s_id':None,'kind':'drawing or diagram','marked_in_H':False,'evidence':'Half b and the single autograph crop show both long edges meeting at the small lower-left turn. In C the existing path goes from the left turn to the far-right tip and then back toward the letters, leaving no separate line from the letters down to the left turn. Added that observed second edge. This is an added stroke, not merely a change of curve parameters.','crop':str(out/'signature.png'),'confidence':'high','unresolved':False,'consequential':False}
  ],
  'inventory':[],
  'doubts':[{'place':'Autograph below Le Secrétaire Général','reading':signature,'alternatives':'E S; E Siau','confidence':'low','reason':'The two large letters are recognizable, but the few following small strokes merge into the long flourish. The single enlarged crop did not resolve their lexical status.'}],
  'notes':[
    'The visible side is a typewritten thesis-defence notice headed AVIS DE SOUTENANCE D\'UNE THESE DE DOCTORAT DE / SPECIALITE : SCIENCES DE LA TERRE mention GEOLOGIE APPLIQUEE.',
    'The notice is dated MONTPELLIER, le 19 AVRIL 1977, has number N°: 2418 and distribution Liste A, and names BAYER Michel as candidate.',
    'The title is Etude gravimétrique de la Corse. The planned defence is 25 AVRIL 1977 à 14 h. 30, Salle de cours n° 10 - U.S.T.L.; the director is M. LOUIS Pierre and the laboratory is Laboratoire de Géophysique.',
    'The abstract states that 270 measurements completed the gravimetric survey of Corsica and that the whole data set of 720 stations was processed into Bouguer-anomaly, derivative, regional and residual maps, then interpreted with geology and aeromagnetism. These are claims of the notice, not independently verified scientific results.',
    'The abstract explicitly presents the proposed deep structure of Corsica and nearby regions, including the bassin Algéro-provençal, as hypotheses. The research duration is Deux ans.',
    'The proposed jury is P. LOUIS, M. MATTAUER, R. NEUMANN, F. RIMBERT and J. ORSINI, with the titles MM., Mlle and M. placed as transcribed.',
    'The office at the foot is Le Secrétaire Général, followed by an autograph and the underlined typed name E. SIAU. The lower-left pencil 3 is an archive sheet number.'
  ],
  'checks':[],
  'notation':[
    {'sign':'Number abbreviations with raised ring','tex':'N°: 2418; n° 10','place':'Notice number in upper-left block; room field','ink':'Capital N and lowercase n respectively, each followed by a raised hollow circle.','alternatives':''},
    {'sign':'Repeated letterhead decoration','tex':r'$\frown\frown\frown\frown\frown\frown\frown\frown\frown\frown\frown\frown$','place':'Below DU LANGUEDOC','ink':'Twelve separate small downward-opening arches; counted in half a.','alternatives':''},
    {'sign':'Underlined labels and headings','tex':r'\uline{...}','place':'Diffusion; both title lines; form-field labels; typed E. SIAU','ink':'Single continuous dark underlines, stopping before the field colons; single rather than double letter outlines. No bold or double-struck alphabet is inferred.','alternatives':''},
    {'sign':'Autograph','tex':signature,'place':'Below Le Secrétaire Général','ink':'Two tall cursive forms, several small following strokes, and a long narrow return flourish.','alternatives':'E S|E Siau'},
    {'sign':'Typewritten initials and title','tex':'MM. :; Mlle; M.; M. MATTAUER','place':'Jury list','ink':'MM. is followed by a colon; Mlle has no point. The M. immediately before MATTAUER is aligned with the other given-name initials.','alternatives':''}
  ],
  'abbreviations':[
    {'written':'JP/GJ','expansion':'Two sets of initials; full names not supplied on this page.'},
    {'written':'N°, n°','expansion':'numéro'},
    {'written':'h.','expansion':'heure(s)'},
    {'written':'U.S.T.L.','expansion':'Université des Sciences et Techniques du Languedoc (institution name supplied in the letterhead).'},
    {'written':'M.','expansion':'Monsieur when it precedes LOUIS Pierre or J. ORSINI; the M. before MATTAUER is an initial.'},
    {'written':'MM.','expansion':'Messieurs'},
    {'written':'Mlle','expansion':'Mademoiselle'}
  ],
  'brief_feedback':[]
}
items=[
('text','upper-left letterhead','U N I V E R S I T E / DES SCIENCES ET TECHNIQUES / DU LANGUEDOC','typewriter'),
('drawing','beneath letterhead','Twelve small arch ornaments','typewriter'),
('text','upper-right dateline','MONTPELLIER, le 19 AVRIL 1977','typewriter'),
('text','upper-left office','Service de la Scolarité','typewriter'),
('text','under office name','JP/GJ','typewriter'),
('text','upper-left distribution field','Diffusion : Liste A; Diffusion underlined','typewriter'),
('text','under distribution','N°: 2418','typewriter'),
('text','centred title, first line',"AVIS DE SOUTENANCE D'UNE THESE DE DOCTORAT DE; underlined",'typewriter'),
('text','centred title, second line','SPECIALITE : SCIENCES DE LA TERRE mention GEOLOGIE APPLIQUEE; underlined','typewriter'),
('text','candidate field','Nom et prénom du candidat : BAYER Michel; label underlined','typewriter'),
('text','thesis title field','Titre de la thèse : Etude gravimétrique de la Corse.; label underlined','typewriter'),
('text','date and time field','Date, heure et lieu de soutenance prévus : 25 AVRIL 1977 à 14 h. 30; label underlined','typewriter'),
('text','indented room field','Salle de cours n° 10 - U.S.T.L.','typewriter'),
('text','director field','Nom du Directeur de thèse : M. LOUIS Pierre; label underlined','typewriter'),
('text','laboratory field label','Désignation du laboratoire où la thèse est préparée :; label underlined','typewriter'),
('text','indented laboratory name','Laboratoire de Géophysique','typewriter'),
('text','six-line abstract',"Analyse de l'ouvrage : Afin de terminer le levé gravimétrique de la Corse,; label underlined",'typewriter'),
('text','research duration field','Durée approximative des recherches ayant abouti à la thèse : Deux ans; label underlined','typewriter'),
('text','jury heading','Composition du jury proposé :; label underlined','typewriter'),
('text','jury first row','MM. : P. LOUIS','typewriter'),
('text','jury second row','M. MATTAUER','typewriter'),
('text','jury third row','R. NEUMANN','typewriter'),
('text','jury fourth row','Mlle F. RIMBERT','typewriter'),
('text','jury fifth row','M. J. ORSINI','typewriter'),
('text','lower-right office','Le Secrétaire Général,','typewriter'),
('text','autograph below office','E S / E Siau','another unnamed hand'),
('drawing','across and below autograph','Long narrow return flourish with two long edges and a small lower-left turn','another unnamed hand'),
('text','typed signatory name','E. SIAU; underlined','typewriter'),
('margin note','extreme lower-left margin','3; archive pencil sheet number, represented in a TeX comment only','another unnamed hand')
]
for i,(kind,position,first,hand) in enumerate(items,1):
    report['inventory'].append({'scan':4,'sheet_kind':'typescript','hand':hand,'element':f'004-{i:02}','kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
