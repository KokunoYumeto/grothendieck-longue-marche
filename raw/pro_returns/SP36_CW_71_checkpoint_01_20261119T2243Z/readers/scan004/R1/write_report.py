import json
from pathlib import Path
out=Path('/workspace/scratch/17347c1714f0/out/readers/scan004/R1')
base='/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/'
items=[
('004-R1-01','typewriter','text','upper left, letterhead','U N I V E R S I T E / DES SCIENCES ET TECHNIQUES / DU LANGUEDOC'),
('004-R1-02','typewriter','drawing','upper left, below DU LANGUEDOC','Twelve small upward arches, represented by twelve \\frown signs'),
('004-R1-03','typewriter','text','upper right, dateline','MONTPELLIER, le 19 AVRIL 1977'),
('004-R1-04','typewriter','text','upper left, office name','Service de la Scolarité'),
('004-R1-05','typewriter','text','upper left, below office name','JP/GJ'),
('004-R1-06','typewriter','text','upper left, distribution','Diffusion : Liste A; Diffusion underlined'),
('004-R1-07','typewriter','text','upper left, notice number','N°: 2418'),
('004-R1-08','typewriter','text','centered heading, first line','AVIS DE SOUTENANCE D\'UNE THESE DE DOCTORAT DE; whole line underlined'),
('004-R1-09','typewriter','text','centered heading, second line','SPECIALITE : SCIENCES DE LA TERRE mention GEOLOGIE APPLIQUEE; whole line underlined'),
('004-R1-10','typewriter','text','first field','Nom et prénom du candidat : BAYER Michel; field label underlined'),
('004-R1-11','typewriter','text','second field','Titre de la thèse : Etude gravimétrique de la Corse.; field label underlined'),
('004-R1-12','typewriter','text','third field','Date, heure et lieu de soutenance prévus : 25 AVRIL 1977 à 14 h. 30; field label underlined'),
('004-R1-13','typewriter','text','indented below third field','Salle de cours n° 10 - U.S.T.L.'),
('004-R1-14','typewriter','text','fourth field','Nom du Directeur de thèse : M. LOUIS Pierre; field label underlined'),
('004-R1-15','typewriter','text','fifth field','Désignation du laboratoire où la thèse est préparée :; field label underlined'),
('004-R1-16','typewriter','text','indented below fifth field','Laboratoire de Géophysique'),
('004-R1-17','typewriter','text','six-line abstract','Analyse de l\'ouvrage : Afin de terminer le levé gravimétrique de la Corse, 270 mesures ont été effectuées.; field label underlined; entire abstract transcribed'),
('004-R1-18','typewriter','text','duration field','Durée approximative des recherches ayant abouti à la thèse : Deux ans; field label underlined'),
('004-R1-19','typewriter','text','jury heading','Composition du jury proposé :; field label underlined'),
('004-R1-20','typewriter','text','jury row 1','MM. : P. LOUIS'),
('004-R1-21','typewriter','text','jury row 2','M. MATTAUER'),
('004-R1-22','typewriter','text','jury row 3','R. NEUMANN'),
('004-R1-23','typewriter','text','jury row 4','Mlle F. RIMBERT'),
('004-R1-24','typewriter','text','jury row 5','M. J. ORSINI'),
('004-R1-25','typewriter','text','lower right, signatory office','Le Secrétaire Général,'),
('004-R1-26','another unnamed hand','text','lower right, autograph above typed name','E S, with possible faint continuation E Siau; uncertainty retained'),
('004-R1-27','another unnamed hand','drawing','lower right, through and below autograph','Long thin returning flourish, extending far down-left and to the right'),
('004-R1-28','typewriter','text','lower right, below autograph','E. SIAU; underlined'),
('004-R1-29','another unnamed hand','text','bottom left','Archive pencil number 3; recorded in TeX comment only'),
]
inventory=[dict(scan=4,sheet_kind='reused_typed',hand=hand,element=el,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes') for el,hand,kind,pos,words in items]
report={
'scan':4,'reader':'R1','model':'inherited parent model','effort':'inherited; value not independently exposed',
'started_utc':'2026-11-19T22:12:34Z','finished_utc':'2026-11-19T22:15:32Z',
'images_viewed':[base+'J71-01_71_scan004.jpg',base+'J71-01_71_scan004_a.jpg',base+'J71-01_71_scan004_b.jpg'],
'crops':[{'file':str(out/'autograph.png'),'source':base+'J71-01_71_scan004_b.jpg','box':[900,735,1440,925],'rotation':0,'output_width':2800,'scale':2800/540,'processing':'PIL crop, autocontrast, LANCZOS enlargement; no sharpening or rotation','place':'Autograph and its returning flourish, with typed E. SIAU below','observed':'Two large letter forms support E S. The first has an upper loop and lower curl; the second has a tall curved stroke and lower hook. Very faint short strokes after the second character cannot securely be separated into letters. The flourish extends diagonally far down-left, returns to the far right, and bends back toward the signature. E S remains the preferred abbreviated reading; a fuller E Siau remains uncertain.'}],
'findings':[{
'id':'R1-004-01','place':'Autograph below Le Secrétaire Général,',
'c':r'\handwritten{\unsure{E S|E Siau}}','h':None,'reading':r'\handwritten{\unsure{E S|E Siau}}',
'diff_c':False,'diff_h':False,'c_doubt':True,'s_id':None,'kind':'other','marked_in_H':False,
'evidence':'Half b gives two large signature letters. The one permitted autograph crop confirms the looped first letter and tall curved second letter, but does not resolve the faint continuation. The typed name below is clear E. SIAU; it does not by itself settle the handwritten continuation.',
'crop':str(out/'autograph.png'),'confidence':'low','unresolved':True,'consequential':False}],
'inventory':inventory,
'doubts':[{'place':'Autograph below Le Secrétaire Général,','reading':r'\handwritten{\unsure{E S|E Siau}}','alternatives':'E Siau; only E S is legible with any confidence, and the tiny following traces remain unresolved','confidence':'low','reason':'The enlarged ink shows faint small continuation strokes merging into the long flourish; no secure individual i, a or u can be isolated.'}],
'notes':[
'The sheet is a typed notice of a thesis defense, headed AVIS DE SOUTENANCE D\'UNE THESE DE DOCTORAT DE / SPECIALITE : SCIENCES DE LA TERRE mention GEOLOGIE APPLIQUEE.',
'The dateline is MONTPELLIER, le 19 AVRIL 1977. The notice number is N°: 2418. The distribution field says Liste A.',
'The candidate is BAYER Michel and the thesis title is Etude gravimétrique de la Corse. The announced defense is 25 AVRIL 1977 à 14 h. 30, Salle de cours n° 10 - U.S.T.L.',
'The director field names M. LOUIS Pierre; the laboratory field names Laboratoire de Géophysique.',
'The abstract reports 270 measurements, a combined set of 720 stations, treatment as Bouguer-anomaly maps, derivatives, regional and residual maps, and interpretation using geology and aeromagnetism. These are claims reported by the notice, not independently verified here.',
'The abstract explicitly presents proposed hypotheses for the deep structure of Corsica and adjoining regions, including the bassin Algéro-provençal.',
'The stated duration is Deux ans. The proposed jury lists P. LOUIS, M. MATTAUER, R. NEUMANN, F. RIMBERT and J. ORSINI.',
'The signatory office is Le Secrétaire Général, and the typed name is E. SIAU. A faint autograph and long returning flourish stand above the typed name.',
'There are no mathematical formulas, proofs, calculations, marginal mathematical notes, deletions or insertions on this page. The bottom-left 3 is an archive pencil number.'
],
'checks':[],
'notation':[
{'sign':'Number abbreviation','tex':'N°, n°','place':'Notice number and room number','ink':'Uppercase N or lowercase n followed by a small raised circle; the numeral in the room field is 10.','alternatives':''},
{'sign':'Letterhead ornament','tex':r'\frown\frown\frown\frown\frown\frown\frown\frown\frown\frown\frown\frown','place':'Below DU LANGUEDOC','ink':'Twelve small upward arches.','alternatives':''},
{'sign':'Plain typewriter capitals and initials','tex':r'\ttfamily; \uline{...}','place':'Letterhead, two title lines, names and jury','ink':'Single typewriter outlines; no double-struck alphabets or bold emphasis. Title lines and field labels have single underlines.','alternatives':''},
{'sign':'Autograph','tex':r'\handwritten{\unsure{E S|E Siau}}','place':'Above E. SIAU','ink':'Two large looped or curved letter forms, faint following strokes and long returning flourish.','alternatives':'E Siau remains unresolved; E S is the first candidate.'}
],
'abbreviations':[
{'written':'JP/GJ','expansion':'Two sets of initials; full names are not supplied on this page.'},
{'written':'N°, n°','expansion':'numéro'},
{'written':'h.','expansion':'heure(s)'},
{'written':'U.S.T.L.','expansion':'Université des Sciences et Techniques du Languedoc'},
{'written':'M.','expansion':'Monsieur before LOUIS Pierre and J. ORSINI; M. in M. MATTAUER is the given-name initial.'},
{'written':'MM.','expansion':'Messieurs'},
{'written':'Mlle','expansion':'Mademoiselle'}
],
'brief_feedback':[],
'comparison_status':{'C':'Complete word-by-word and mark-by-mark visual comparison; no substantive changes to C. Its single autograph doubt is retained.','H':'No transcription is supplied; no H omission or collation rows have been manufactured.','S':'No S rows supplied.'}
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
