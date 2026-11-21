from pathlib import Path
import json

ROOT=Path('/workspace/scratch/d7279cb02214')
WORK=ROOT/'SP92_C13_150+151_work'
PAGE='151_scan004'
p=json.loads((ROOT/'reading_packets'/PAGE/'packet.json').read_text())
cm=json.loads((WORK/'records'/(PAGE+'_cropmap.json')).read_text())
C=p['witness_C']
assert p['witness_H'] is None and not p['differences']

candidate=r'''\scanpage{4}
% The letter is upside down in the source scan. Its typed reading order is restored here.
\hrule
\begin{tabular}{p{.47\linewidth}p{.47\linewidth}}
\textbf{ACADEMIE D'AIX-MARSEILLE} & AVIGNON le 6 décembre 1990\\
\rule{3cm}{.4pt}&\\
\textbf{INSPECTION ACADEMIQUE} & Jacques ROUX, responsable\\
\textbf{DE VAUCLUSE}&départemental de l'Action\\
\rule{1cm}{.4pt}&Culturelle,\\[1em]
C.D.A.C.N°16&à\\[1em]
&M
\end{tabular}

\uline{OBJET} : Projets d'Action Educative Collège.\\
Année scolaire 1990/1991

L'attribution des aides aux P.A.E. se déroulera cette année en deux temps :

\begin{tabular}{l p{.72\linewidth}}
DECEMBRE & - instruction des dossiers\\
&par l'Inspection Académique\\[1em]
&propositions à la M.I.A.D.A.C.\\[1em]
JANVIER & - Monsieur le Recteur attribue\\
&une aide globalisée à Monsieur\\
&l'Inspecteur d'Académie.
\end{tabular}

Une commission se réunit vers le 15 janvier 1991, afin d'assurer la ventilation des aides au niveau du département. Je vous demanderai alors de participer à cette Commission.

P/L'Inspecteur d'Académie

% Unreadable autograph with a long looped flourish; it is not a cancellation of the typed text.
\handwritten{\illegible{1}}

% A separate lower line is clipped to a few stroke tops at the scan edge. No complete word is reconstructed.
\illegible{1}
\margin{3}
'''

changes=[{
 'id':'C01','place':'separate line beneath the autograph, clipped at the original upper image edge',
 'C':r'\unsure{ROUX}','H':None,'final':r'\illegible{1}',
 'evidence':'At the edge there is a low rounded ink nub followed by four short upright/rounded tips. The bodies of the presumed letters lie outside the image. No complete R, O, U, or X can be identified; the typed ROUX in the sender block is not evidence for supplying this clipped word. A separate illegible fragment is retained instead.',
 'crop':cm['clipped_name']['crop'],'box':cm['clipped_name']['box'],
 'confidence':'high','kind':'text not on the page','error_kind':'9 not on page',
 'against_C':True,'against_H':False,'consequential':False,'marked_in_H':False
}]

decisions=[
 {'id':'M0744','cote':'151','scan':'4','decision':'undecided','reading':r'\illegible{1}',
  'ink':'The autograph has a tall curved stem with a lower loop, a detached small upper loop, a round middle loop, several narrow turns and a long crossing flourish. These components do not separate into a secure letter-by-letter name; no name is inferred from the typed sender.',
  'crop':cm['signature_detail']['crop'],'box':cm['signature_detail']['box'],'confidence':'low'},
 {'id':'M0745','cote':'151','scan':'4','decision':'undecided','reading':r'\illegible{1}',
  'ink':'The image edge removes nearly the entire separate lower line. Only about five stroke tops survive, which cannot establish ROUX or any other complete word. The reading remains unresolved because of physical clipping, while the unsupported complete conjecture is removed.',
  'crop':cm['clipped_name']['crop'],'box':cm['clipped_name']['box'],'confidence':'low'}
]

inventory=[]
def inv(element,kind,position,words,hand='typed letter',sheet_kind='letter'):
 inventory.append({'sheet_kind':sheet_kind,'hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'transcribed':'yes'})
inv('top horizontal rule','text','above letterhead in upright reading orientation','horizontal rule',hand='printed or copied letterhead rule')
inv('academy letterhead','text','upright upper left','ACADEMIE D\'AIX-MARSEILLE; INSPECTION ACADEMIQUE; DE VAUCLUSE, with two short separator rules',hand='printed letterhead')
inv('place and date','text','upright upper right','AVIGNON le 6 décembre 1990')
inv('sender block','text','upright upper right, below date','Jacques ROUX, responsable / départemental de l\'Action / Culturelle,')
inv('reference number','text','upright left, below letterhead','C.D.A.C.N°16')
inv('recipient placeholders','text','upright right, below sender','à / M; remainder blank')
inv('subject and school year','text','upright upper middle','OBJET : Projets d\'Action Educative Collège. / Année scolaire 1990/1991')
inv('introductory paragraph','text','upright middle','L\'attribution des aides aux P.A.E. se déroulera cette année en deux temps :')
inv('December schedule','text','upright middle','DECEMBRE — instruction des dossiers / par l\'Inspection Académique / propositions à la M.I.A.D.A.C.')
inv('January schedule','text','upright lower middle','JANVIER — Monsieur le Recteur attribue / une aide globalisée à Monsieur / l\'Inspecteur d\'Académie.')
inv('closing paragraph','text','upright lower body','Une commission se réunit vers le 15 janvier 1991 ... de participer à cette Commission.')
inv('signature authority line','text','upright lower right','P/L\'Inspecteur d\'Académie')
inv('autograph','text','upright bottom, clipped flourish at the image edge','unreadable signature; long oval flourish',hand='signatory hand, not securely identified from the autograph')
inv('separate clipped lower line','text','upright extreme bottom; original upper image edge','only a few letter tops survive',hand='cannot securely classify the clipped fragments as typed or handwritten')
inv('other-hand foliation','margin note','original bottom left; upside down relative to the letter','3',hand='other hand: thin light foliation')

second_boxes=[]
def blind(kind,name,reading,rotation=None):
 v=cm[name]; b=v['box']
 second_boxes.append({'box':f'B{len(second_boxes)+1:02d}','kind':kind,'x0':b[0],'y0':b[1],'x1':b[2],'y1':b[3],
                      'reading':reading,'rotation':v['rotation'] if rotation is None else rotation})
blind('printed heading and excluded colon-like copy specks','letterhead',r"\textbf{ACADEMIE D'AIX-MARSEILLE}\par\rule{3cm}{.4pt}\par\textbf{INSPECTION ACADEMIQUE}\par\textbf{DE VAUCLUSE}\par\rule{1cm}{.4pt}")
blind('typed word and excluded irregular copy marks','inspection_accent',r"par l'Inspection Académique")
blind('complete edge word','edge_alors','alors')
blind('whole autograph and separate clipped lower fragment; both C marks','signature_detail',r'\handwritten{\illegible{1}}\par\illegible{1}')
blind('separate clipped lower fragment','clipped_name',r'\illegible{1}')
blind('handwritten foliation','folio3',r'\margin{3}')

notes=r'''# 151_scan004 — reader A

This is an administrative letter with printed letterhead and a typed body, not a mathematical manuscript page. The source photograph presents it upside down. I restored its reading orientation by rotating the supplied native halves by 180 degrees, then read the entire letter. Original coordinates are retained in every evidence box. The light foliation 3 is upright in the original scan and therefore upside down relative to the letter; it is another hand and remains a margin item. No authorial manuscript page number or handwritten date is present.

The letter is headed ACADEMIE D'AIX-MARSEILLE / INSPECTION ACADEMIQUE / DE VAUCLUSE. It is dated AVIGNON le 6 décembre 1990 and names Jacques ROUX, responsable départemental de l'Action Culturelle. The recipient area has only the typed à and M, with no supplied recipient name. Its subject is Projets d'Action Educative Collège, for the school year 1990/1991. It describes December dossier examination and proposals, followed in January by a global allocation through the Recteur and Inspecteur d'Académie. A commission is to meet around 15 janvier 1991 to distribute the aid, and the letter says the recipient will then be asked to participate. This summarizes the typed text; no external facts or institutional expansions have been researched.

## Full ink review

Every typed word, capital, accent, punctuation mark and numeral was read on the native halves, including the reference C.D.A.C.N°16, P.A.E., M.I.A.D.A.C., both year forms, and the unstopped placeholder M. The heading ACADEMIE/ACADEMIQUE and the month DECEMBRE have no added accents; Educative is likewise retained without a supplied acute. The actual accents in décembre, départemental, Année, Académique, globalisée, Académie, réunit and département are retained. The final Commission is capitalized, unlike commission at the paragraph’s beginning. The subject OBJET is underlined. A long top rule and two shorter letterhead separator rules are kept as rules, not treated as strikes.

The tightly framed then-enlarged right-edge word alors includes the complete final s before the dark border and is retained without truncation. Two black points beside the printed ACADEMIQUE are diagonal and off the character alignment, resembling other copy specks; no colon is added. The irregular dot over the body c and broken small upright over a in Académique do not form a secure typed diacritic and differ from the intact acute over é; no extra accent is invented. These are excluded uncertain copy marks, not confidently transcribed text. The large fold and scattered stains are likewise not text.

## Signature and clipping

The autograph below P/L'Inspecteur d'Académie is a tall looped stem, a detached upper loop, a rounded middle loop and narrow turns joined to a long oval flourish. Its letters cannot be securely separated at the available resolution, so M0744 remains illegible. The flourish does not cancel any typed wording and is not reproduced as a diagram or a guessed name.

A separate lower line is almost entirely outside the scan: only about five small stroke tops remain at the original upper image boundary. No complete R, O, U or X survives, so C's tentative ROUX cannot be maintained as a transcription of visible letters. This is represented as a separate illegible fragment, with the image loss documented. M0745 remains undecided; removing the unsupported full-word conjecture is not claimed as recovery of another word. The clearly typed ROUX in the sender block is not used to reconstruct either lower item.

No insertion, deletion or securely recoverable typed overstrike was found. No mathematical formula, diagram, mathematical doubt, or proof check occurs on this page. Witness H is absent for the entire page, and no C/H difference rows were supplied.
'''

record={
 'page':PAGE,'cote':'151','scan':4,'reader':'reader_a / GPT-6 Astra Pro / effort not exposed / run SP92',
 'line_count':28,
 'line_count_note':'28 written line units: left letterhead3, right date1, sender3, reference1, recipient placeholders2, subject/year2, introductory paragraph2, December schedule3, January schedule3, closing paragraph4, authority line1, autograph1, clipped lower fragment1, foliation1. Separate column lines are counted separately; horizontal rules are not text lines.',
 'half_review':'The original was viewed once for layout. The two supplied native halves were each rotated 180 degrees without resizing and each viewed once in upright reading order (half2 then half1). All printed, typed and handwritten ink was read against C; H is absent. Eight tight evidence crops were saved and viewed, with the unresolved signature detail reframed once to include its detached upper loop and viewed again. Native upright half previews were moved into reading_packets/151_scan004 and are not deliverable crops. No OCR, research or compilation was used.',
 'deletion_insertion_review':[
  {'place':'entire printed/typed letter','state':'no deletion/insertion found','bounds':'C contains no deletion or insertion macros; all letterhead, body and closing lines were inspected. No reliably separable typed overstrike was found.','attachment':'Not applicable. The long and short printed rules are separators, not cancellations.','reading':'All typed prose retained as visible.','confidence':'high','crop':None,'box':None},
  {'place':'autograph flourish','state':'signature stroke, not deletion','bounds':'The looped horizontal sweep belongs to the autograph and does not strike the authority line above.','attachment':'Below P/L\'Inspecteur d\'Académie, separate from the clipped lower fragment.','reading':r'\handwritten{\illegible{1}}','confidence':'high','crop':cm['signature_detail']['crop'],'box':cm['signature_detail']['box']}
 ],
 'changes':changes,'diff_coverage':[],'decisions':decisions,'inventory':inventory,'notes':notes,'check_events':[],
 'notation':[
  {'sign':'3 in the original lower-left corner','reading':r'\margin{3}, other-hand foliation','evidence':'Thin light stroke forming two rightward lobes; orientation opposes the typed letter.'},
  {'sign':'P/L','reading':'literal typed short form P/L','evidence':'Capital P, oblique slash, capital L before the apostrophe of Inspecteur; no expansion in text.'},
  {'sign':'signature and clipped lower fragment','reading':'two separate illegible items','evidence':'An autograph survives above a second line reduced to a few stroke tops by the image edge.'}
 ],
 'hand_log':[
  {'habit':'This leaf is a letter in different hands and printing, not evidence for the mathematical manuscript hand','places':['entire page'],'scope':'151_scan004 only','witness_errors':'Do not transfer manuscript glyph habits or infer the signature from the typed sender.'},
  {'habit':'Thin foliation is oriented independently of the letter','places':['original bottom-left 3'],'scope':'this page','witness_errors':'C correctly uses margin rather than mspage.'},
  {'habit':'Copy specks can imitate colon points or extra accents','places':['right of printed ACADEMIQUE','above body c/a in Académique'],'scope':'this copied letter only','witness_errors':'No extra punctuation or accented spelling is added.'},
  {'habit':'Signature has large intersecting flourishes that do not indicate cancellation','places':['autograph under authority line'],'scope':'signatory hand on this letter only','witness_errors':'C’s unreadable-signature status is retained; the nearby clipped ROUX conjecture is not supported by complete visible letters.'}
 ],
 'abbreviations':[
  {'form':'M','expansion':'Monsieur; blank recipient placeholder, not expanded in the transcription'},
  {'form':'P/L','expansion':'Pour l’ — retained literally'},
  {'form':'P.A.E.','expansion':'Projets d’Action Educative, as the subject line supplies'},
  {'form':'C.D.A.C.','expansion':'Not expanded on this leaf; retained literally'},
  {'form':'M.I.A.D.A.C.','expansion':'Not expanded on this leaf; retained literally'},
  {'form':'N°','expansion':'Numéro; retained literally'}
 ],
 'doubts':[
  {'place':'autograph, M0744','reading':r'\illegible{1}','alternatives':'Roux or another signature cannot be established letter by letter.','confidence':'low','reason':'The tall loop, rounded middle and narrow turns are merged with an extended flourish; a familiar surname from the letterhead would be a conjecture.'},
  {'place':'separate clipped lower line, M0745','reading':r'\illegible{1}','alternatives':'No complete word is recoverable; C conjectures ROUX.','confidence':'low','reason':'Only stroke tops survive; the character bodies are beyond the image edge. No missing letters are supplied.'}
 ],
 'second_boxes':second_boxes,
 'crops':[{'place':name,**v,'viewed':True,'method':'Pillow crop from assigned original; 180-degree rotation for typed reading orientation except foliation; LANCZOS enlargement, autocontrast, sharpness1.15.'} for name,v in cm.items()]
}

assert changes[0]['C'] in C
assert [d['id'] for d in decisions]==[m['id'] for m in p['marks']]
assert len(cm)==8 and all((WORK/v['crop']).exists() for v in cm.values())
assert all(c['H'] is None for c in changes)
(WORK/'records'/(PAGE+'.tex')).write_text(candidate)
(WORK/'records'/(PAGE+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(f'Saved {PAGE}: {len(changes)} change, no supplied differences, {len(decisions)} unresolved marks, {len(inventory)} inventory entries, {len(second_boxes)} blind boxes, {len(cm)} crops.')
