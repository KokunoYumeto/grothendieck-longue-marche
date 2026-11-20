from pathlib import Path
import json,copy,datetime
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan028/R{i}/return.json').read_text()) for i in (1,2,3)]
# Alignment manually checked against all three complete readings and finding lists.
mp2=[1,2,3,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,27,28,29,31,32,33,4,13,21,22,23,24,25,26,30]
mp3=list(range(1,29))+[30,29,31,32,33]
d={'scan':28,'folder':'J81-04','their_page':27,'hua_has':'text','filename':'J81-04_81_scan028.tex','status':'decided','findings':copy.deepcopy(rs[0]['findings'])}
newcrops={2:'F02_ens',12:'F12_comp',25:'F25_ens',26:'F26_X_end',27:'F27_Xprime_end',28:'F28_Xdouble_end',29:'F29_note_gap',30:'F30_avec',31:'F31_intersection_end',32:'F32_cette'}
for i,f in enumerate(d['findings'],1):
 source=[rs[0]['findings'][i-1],rs[1]['findings'][mp2[i-1]-1],rs[2]['findings'][mp3[i-1]-1]]
 f['id']=f'SP41-028-{i:03d}'
 f['readers']={f'R{r}':s['reading'] for r,s in enumerate(source,1)}
 f['reader_source_ids']={f'R{r}':s['id'] for r,s in enumerate(source,1)}
 co=f['confidence'];f['confidence']='high' if co>=.8 else 'medium' if co>=.65 else 'low'
 f['marked_in_H']='yes' if f['marked_in_H'] else 'no'
 f['crop']=f['crop'].replace(str(w)+'/','') if f.get('crop') else ''
 if i in newcrops:f['crop']='crops/scan028/main_'+newcrops[i]+'.png'
 if i==8:f['crop']='readers/scan028/R3/06_maps.png'
 if i==10:f['crop']='readers/scan028/R3/07_isom.png'
 if i==33:f['crop']='readers/scan028/R3/15_second_sss_a.png'
 if i==13:f['crop']='crops/scan028/main_F12_comp.png'
 f['main_adjudication']='All three returns and their full texts compared; main reader viewed the cited crop.'
 if f['c_doubt_status']=='resolved':f['against_C']=True
 # The retained primary-reading uncertainties do not themselves create H differences.
 if i in (22,23,24):f['against_H']=False
 f['evidence']='Main crop inspection confirms: '+f['evidence']
# Every changed or disputed decision follows the observed strokes, with alternatives retained.
d['findings'][10]['reading']=r'Soi\deleted{t}ent'
d['findings'][10]['against_C']=True
d['findings'][10]['evidence']='Main inspection of R1 crop 07: Soi remains singly written and live; the tall old t and crossbar are concentrated at the rewritten ending, followed by ent. Adopt R2’s local Soi\\deleted{t}ent representation. R1 and R3 duplicate the common prefix by giving the whole old Soit as deleted; their readings are preserved in the comparison.'
d['findings'][7]['against_H']=True
d['findings'][7]['evidence']='Main inspection of R3 crop 06: both handwritten P forms have a descending straight stem, a broad right loop, and a leftward return. Use \\mathcal{P} consistently for this written shape; H renders it with \\mathfrak{P}. The subscript 2 is present only on the first occurrence. This records the alphabet-rendering choice without asserting a change of mathematical object.'
d['findings'][7]['mathematical_note']='The same powerset notation is represented in each witness; the final alphabet choice follows the observed looped form.'
d['findings'][8]['evidence']='Main inspection of R1 crop 06 and R3 crop 06: the right point is clear; at left a dark bent stem continues below the shaft while two branches project upward/right. The returning bend favours hookrightarrow, but overtracing leaves leftrightarrow and mapsto open. R3 places leftrightarrow first; the final retains all three, with hook first on the visible lower continuation.'
d['findings'][3]['evidence']='Main inspection of R1 crop 03: the rising stroke attaches to the low letter body and the following tall stroke bends at its top; no detached two-sided circumflex separates cleanly. Retain aretes|arêtes, with the unaccented form first. R2 places arêtes first; R1/R3 place aretes first.'
d['findings'][4]['evidence']='Main inspection of R1 crop 04: a short detached dark mark over the first low letter is broad at left and terminates slightly lower on the right. Retain rèlation|rélation|relation, with the descending accent shape first. R2/R3 prefer rélation; the thick mark does not settle its direction.'
d['findings'][14]['evidence']='Main inspection of R1 crop 09: the crossed initial knot has a small loop and a low return; live on continues to its right. Retain c|con inside deletion, with the short surviving c-like trace first. R2 keeps only uncertain c; R1/R3 also retain con.'
d['findings'][15]['evidence']='Main inspection of R1 crop 10: a sharply bounded dark point occupies the gap after binaire; no second point accompanies it. Adopt the single literal point, resolving C’s and R3’s uncertainty; R1/R2 also read a point.'
d['findings'][19]['evidence']='Main inspection of R1 crop 13: beneath the diagonal cancellation a slanted left stem and three rightward levels survive, with a curved lower foot. The adjacent live E has the same slanted three-arm construction. Resolve the cancelled glyph as E, as R1/R2; R3 retains E|membership-sign.'
d['findings'][22]['evidence']='Main inspection of R1 crop 15: the compressed ending has a crossed high loop, a short lower stroke and a down-right terminal sweep. These favour suivante but do not isolate a final e from the t flourish. Retain suivante|suivant, as R1/R3; R2 resolves suivante.'
d['findings'][23]['evidence']='Main inspection of R1 crop 16: a central dark knot has short spurs and a rising diagonal that meets the curved right boundary. Retain star|A, with the radiating knot favouring star. R2 resolves star; R1/R3 keep the alternative.'
# Main crops confirm all additional H punctuation/connective differences.
for i,obs in {
2:'The linked ens ends with a falling stroke and blank space follows; no separate period is visible.',
12:'The p descender ends before a blank gap; conn. has a distinct separate point, while comp does not.',
13:'A detached black point follows the final n stroke of conn.',
25:'The three low linked strokes of ens end before the separate d, with no period between them.',
26:'The last E subscript ends in a descending tail; the space to its right has no terminal point.',
27:'The first display row ends with the a subscript; no comma follows it.',
28:'The second display row ends with the thick low a subscript; no comma follows it.',
29:'The interval between the display and avec contains paper texture and no authorial words. H explicitly places this explanation in its editorial note macro.',
30:'The word starts with a small low loop, then a v-shaped dip and a final open curve; adopt avec.',
31:'The final zero is a closed loop in the nested index, followed by blank paper with no full stop.',
32:'The initial c is small and low beside the two tall t strokes; adopt lowercase cette.',
33:'Three connected s-shaped turns end with a down-and-back curl and no detached i dot; adopt sss.'
}.items():d['findings'][i-1]['evidence']='Main inspection of the cited crop: '+obs
for i,txt in {9:'The second incidence map carries a visible left-end decoration; its shape remains uncertain, while H prints a plain arrow.',18:'The final coproduct index is retained as c|a, with c first from its open curve; its summand remains E_a.',21:'The lowest index in the first properness inequality is retained as b|0, with b first from its short stem; other a_0 occurrences stay as written.'}.items():d['findings'][i-1]['consequential']=txt
# Complete text, changing only the adjudicated overwrite representation.
t=(w/'readers/scan028/R1/reading.tex').read_text().replace(r'\deleted{Soit}Soient',r'Soi\deleted{t}ent')
(w/'pages'/d['filename']).write_text(t)
d['inventory']=copy.deepcopy(rs[1]['inventory'])
d['inventory'][-2]['first_words_or_objects']='(star|A) Si s in S est un sommet-bout'
d['notes']=[
 {'id':'scan028-note-01','text':'The opening introduces the tree Gamma=(S,A,R), with S as vertices, A as edges, and R as the incidence relation. It writes the maps A to P_2(S) and S to P(A), then asserts injectivity for the latter with the two-vertex one-edge graph as exception. That graph is transcribed with two filled vertices and one unheaded segment. This is an account of the manuscript claim, without a proof check.'},
 {'id':'scan028-note-02','text':'The author introduces the families (U_s) and (E_a) and defines X by their displayed coproducts. The paragraph beginning Pour tout names the components of the tree “coupé en a_0” and writes the binary decomposition X=X′ union X″, its two displayed parts, and their intersection E_{a_0}.'},
 {'id':'scan028-note-03','text':'The lower paragraph calls the decomposition “propre”, gives two inequalities and then a criterion expressed through the terminal vertices and U_s nonempty. Both equivalence abbreviations are visibly sss. The parenthesized condition label remains star|A. These are source statements; their truth was not independently checked in this transcription run.'},
 {'id':'scan028-note-04','text':'The mathematical cues leading back to the ink were the following application/injectivity words at the decorated second arrow, the E_a summand beside the open c-shaped coproduct index, and neighbouring a_0 forms beside the b-shaped nested index. The final arrow retains three candidates; c|a and b|0 retain the ink-led first readings. No index has been repaired from the expected parallel formulas.'},
 {'id':'scan028-note-05','text':'H supplies an editorial note asking about a_0 membership in A′ and A″. The manuscript interval contains no corresponding words. The note is identified as H’s editorial addition in the apparatus and supplies no authorial doubt annotation.'},
 {'id':'scan028-note-06','text':'Five overwritten or cancelled elements are retained: the t revised in Soit, the E candidate beneath Gamma′, the short c|con trace at considérons, the E candidate beneath the last coproduct, and the cancelled E before the inequalities. At Soit the shared Soi remains live and is written once.'},
 {'id':'scan028-note-07','text':'This is a handwritten working sheet with no visible title, date, authorial question mark, or instruction to verify a step. The light pencil 27 at lower left is recorded as an archive sheet-number comment. The reading uncertainties are editorial and are marked in place.'}
]
d['check_events']=[{'statement_id':n['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan028','type':'carried as background without fault found','outcome':'Source-account event only: inspected the page through three independent returns and the cited crops; no independent proof or re-proof of the described mathematical claims.'} for n in d['notes']]
d['notation']=copy.deepcopy(rs[0]['notation'])
d['notation'].append({'scan':28,'form':r'(\unsure{\ast|A})','evidence':'Central knot and short spurs partly merge with the rising stroke of the right boundary.','reading':r'\ast|A'})
d['abbreviations']=copy.deepcopy(rs[2]['abbreviations'])
d['unresolved']=copy.deepcopy(rs[0]['unresolved'])
for u in d['unresolved']:
 c=u.get('confidence',.5)
 if isinstance(c,(float,int)):u['confidence']='high' if c>=.8 else 'medium' if c>=.65 else 'low'
d['main_crop_views']={'R1':list(range(1,17)),'R3':[6,7,15],'main_new':10,'total':29}
d['crop_counts']={'R1':16,'R2':15,'R3':17,'main':10,'total':58}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(w/'decisions/scan028.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print('Decided scan028:',len(d['findings']),'loci;',len(d['unresolved']),'unresolved;',len({x for f in d['findings'] for x in f['c_doubt_ids']}),'C doubt IDs')
