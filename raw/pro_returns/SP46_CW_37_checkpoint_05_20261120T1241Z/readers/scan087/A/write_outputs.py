from pathlib import Path
import json
out=Path('/workspace/scratch/006c0e32b2af/out/readers/scan087/A')
packet=Path('/workspace/scratch/006c0e32b2af/packets/scan087')
meta=json.loads((packet/'meta.json').read_text())
graphic=r'''\margin{\vspace*{0.7ex}\figure{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm]
\fill (-0.12,-0.05)
 .. controls (-0.18,0.04) and (-0.07,0.19) .. (0.01,0.18)
 .. controls (0.11,0.18) and (0.15,0.03) .. (0.09,-0.07)
 .. controls (0.02,-0.12) and (-0.07,-0.10) .. (-0.12,-0.05) -- cycle;
\fill (0.42,0.57)
 .. controls (0.38,0.62) and (0.41,0.82) .. (0.50,0.91)
 .. controls (0.58,0.96) and (0.70,0.81) .. (0.62,0.74)
 .. controls (0.58,0.67) and (0.50,0.60) .. (0.42,0.57) -- cycle;
\end{tikzpicture}%
}}}'''
tex=(packet/'C.tex').read_text()
tex=tex.replace(r'\deleted{\S\ \unsure{7.}}',r'\deleted{\S\ 7\unsure{.|{}}}')
tex=tex.replace(r'\deleted{7\unsure{.}}',r'\deleted{7\unsure{.|{}}}')
target=r'\noindent\qquad 6.5. Anneaux normaux et ferm\deleted{t}e\deleted{e}ture intégrale\dotfill'
assert target in tex
tex=tex.replace(target,target+'\n'+graphic)
(out/'reading.tex').write_text(tex)
proc=json.loads((out/'crop_processing.json').read_text())
for item in proc:
 item['requested_deliveries']=1
 item['actual_visual_views']=1
(out/'crop_processing.json').write_text(json.dumps(proc,ensure_ascii=False,indent=2)+'\n')

def D(id,place,c,reading,diff,c_doubt,unresolved,alts,conf,kind,shows,crop,bbox):
 return {'id':id,'place':place,'c_reading':c,'h_reading':None,'reading':reading,'diff_c':diff,'diff_h':False,'c_doubt':c_doubt,'unresolved':unresolved,'alternatives':alts,'confidence':conf,'kind':kind,'scan_shows':shows,'crop':crop,'bbox':bbox}
decisions=[
D('A087-D01','6.2: cancelled word between limite and the continuation inductive',r'\deleted{\unsure{project|projecti}}',r'\deleted{\unsure{project|projecti}}',False,True,True,['project','projecti'],'low','other','The overprinting X row crosses lower letter shapes p-r-o-j-e-c-t; the first p and the j have lower extensions, and the last clear upright has a hooked low return. The extra terminal X cell does not yield a securely separable final i. Both incomplete strings in C remain possible. No longer contextual word is supplied.','A087_01_cancelled_project.jpg',[1250,1297,1422,1341]),
D('A087-D02','Right margin, below and to the right of the 6.5 leaders','',graphic,True,False,True,['unassigned dark pair; possible punctuation','incidental ink or marks of unresolved origin'],'medium','drawing or diagram','A small compact triangular/rounded lower-left point and a slightly longer upper-right oblique teardrop stand well apart from the larger regular hollow-centred leader dots. No paper-coloured cut, crease or scratch is established. Their shapes are retained; punctuation value and material origin are not assigned.','A087_03_right_point_pair.jpg',[1549,1531,1566,1551]),
D('A087-D03','6.7: cancelled extra glyph immediately after sur',r'\deleted{\unsure{l|1}}',r'\deleted{\unsure{l|1}}',False,True,True,['l','1'],'medium','other','The cancelled typewriter character has an upper leftward serif, tall upright and broad foot. A rising slash crosses it and extends beyond the top and bottom. Its surviving head and foot closely resemble the following l, but the serifed typewriter 1 alternative is not excluded by this overprinted shape.','A087_04_sur_crossed_glyph.jpg',[724,1596,753,1637]),
D('A087-D04','Cancelled section-start row immediately above the live section 7 heading',r'\deleted{\S\ \unsure{7.}}',r'\deleted{\S\ 7\unsure{.|{}}}',True,True,True,[r'\deleted{\S\ 7.}',r'\deleted{\S\ 7}'],'medium','misread symbol or index','The section sign retains opposed loops. In the numeral cell an upper horizontal with a short left downward hook joins a descending right-to-left stroke, extending below the X baseline; this determines 7. The last X has a rounded low dark trace that could be the point or part of cancellation ink, so only the numeral is now unmarked. The explicit absence alternative changes the recorded reading.','A087_05_cancelled_section.jpg',[273,1671,363,1709]),
D('A087-D05','Cancelled numeric stub before the live 7.5',r'\deleted{7\unsure{.}}',r'\deleted{7\unsure{.|{}}}',True,True,True,[r'\deleted{7.}',r'\deleted{7}'],'low','other','The left glyph has the upper horizontal, short left hook and descending stem of 7, with cancellation strokes across it. The following cell is filled by an X and merged curved and low traces; an independent period cannot be separated securely from the cancellation. C’s doubt is retained, with the no-point alternative made explicit.','A087_06_cancelled_number.jpg',[315,1973,361,2011])]

inventory=[]
def I(element,kind,pos,words,hand='typewriter'):
 inventory.append({'sheet_kind':'typescript','hand':hand,'element':element,'kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'})
I('Typed page number','text','Top centre','- 539 -')
I('Contents entry 3.8','text','Top; two typed lines','3.8. Quasi-homéomorphismes et images réciproques de faisceaux')
I('Contents entry 3.9','text','Below 3.8','3.9. Faisceaux d’espaces pseudo-discrets')
I('Section 4 heading','text','Upper quarter','§ 4. Espaces annelés')
for n,title in [
 ('4.1','Espaces annelés , A-Modules , A-Algèbres'),
 ('4.2',"Image directe d’un A-Module"),
 ('4.3',"Image réciproque d’un B-Module"),
 ('4.4','Relations entre images directes et images réciproques'),
 ('4.5','Immersions ouvertes et morphismes représentables par des immersions ouvertes')]:
 I('Contents entry '+n,'text','Upper section 4 block',n+'. '+title)
I('Section 5 heading','text','Upper-middle page','§ 5. Faisceaux quasi-cohérents et faisceaux cohérents')
for n,title in [
 ('5.1','Faisceaux quasi-cohérents'),('5.2','Faisceaux de type fini'),('5.3','Faisceaux cohérents'),('5.4','Faisceaux localement libres'),('5.5','Modules localement libres sur un espace localement annelé'),('5.6','Groupe de Picard'),('5.7',"Morphismes plats d’espaces annelés")]:
 I('Contents entry '+n,'text','Middle section 5 block',n+'. '+title)
I('Section 6 heading','text','Below section 5 block','§ 6. Compléments d’algèbre commutative .')
I('Contents entry 6.1','text','First line of section 6 block','6.1. Limites inductives d’anneaux')
I('Contents entry 6.2','text','Section 6; two typed lines','6.2. Identification du module M_f à une limite … inductive')
I('Cancelled incomplete word','deletion','6.2, end of first line','project / projecti, cancelled by an X row')
I('Contents entry 6.3','text','Middle of section 6 block','6.3. Propriétés de finitude')
I('Contents entry 6.4','text','Middle of section 6 block','6.4. Critères pour qu’un anneau soit noethérien')
I('Contents entry 6.5','text','Middle of section 6 block','6.5. Anneaux normaux et fermeture intégrale')
I('First overtyped letter in fermeture','deletion','6.5, immediately after ferm','t underneath live e')
I('Second overtyped letter in fermeture','deletion','6.5, immediately after the corrected e','e underneath live t')
I('Detached dark point pair','drawing','Right margin below the 6.5 leader baseline','Lower-left compact point and upper-right oblique teardrop','unnamed hand')
I('Contents entry 6.6','text','Lower part of section 6 block','6.6. Compléments sur la platitude')
I('Contents entry 6.7','text','Lower part of section 6 block','6.7. Compléments sur … les modules projectifs')
I('Cancelled surplus character','deletion','6.7, immediately after sur','l / 1 crossed with a rising slash')
I('Contents entry 6.8','text','End of section 6 block','6.8. Existence d’extensions plates d’anneaux locaux')
I('Cancelled section-start row','deletion','Between entry 6.8 and the live section 7 heading','§ 7 with uncertain point, cancelled by Xs')
I('Section 7 heading','text','Lower page','§ 7. Compléments d’algèbre topologique')
for n,title in [('7.1','Anneaux admissibles'),('7.2','Anneaux adiques et limites projectives'),('7.3','Anneaux préadiques noethériens'),('7.4','Modules quasi-finis sur les anneaux locaux')]:
 I('Contents entry '+n,'text','Lower section 7 block',n+'. '+title)
I('Cancelled numeric stub','deletion','Immediately left of the live 7.5 number','7 with uncertain point, cancelled by Xs')
I('Contents entry 7.5','text','Penultimate line','7.5. Anneaux de séries formelles restreintes')
I('Contents entry 7.6','text','Final line','7.6. Anneaux complets de fractions')
I('Archive sheet number','text','Lower left corner; recorded only as a TeX comment','86','unnamed hand')
report={
 'scan':87,'reader':'A','image_views':meta['images'],'reading_path':str(out/'reading.tex'),
 'crops':[{k:p[k] for k in ['file','bbox','rotation','reason']} for p in proc],
 'decisions':decisions,'inventory':inventory,
 'notes':"Continuation of a typewritten contents list, carrying typed page number - 539 - and archive number 86 at lower left. It contains entries 3.8–3.9; section 4 and 4.1–4.5; section 5 and 5.1–5.7; section 6 and 6.1–6.8; a cancelled section-start stub; section 7 and 7.1–7.6, with a cancelled stub immediately before 7.5. No independent page title, date, signature, authorial question mark or authorial doubt is present. The four explicit C doubts were all inspected and reported. The numeral 7 in the cancelled section row is resolved while its point remains doubtful; the other deleted readings retain uncertainty. A small previously omitted point pair at right is preserved graphically with unresolved origin. All substantive typewriting is machine text; the archive numeral is an unnamed hand. The graphic inventory’s unnamed-hand label records the absence of an identified writer, not a determination that the dark pair was deliberately penned. H is description only and unavailable as a transcription. No H differences are counted. Crops and their processing and actual view counts are documented in crop_processing.json and processing.md.",
 'math_reading_decisions':[
  'The two A letters in 4.1, A in 4.2, and B in 4.3 each have one ordinary typewriter outline: no separate doubled stem or script construction. C’s ordinary A/B reading is confirmed independently at each occurrence.',
  'In 6.2 the M has the ordinary typewriter stems and central diagonals. The following f has an ascender, crossbar and lower foot on a distinctly lowered baseline: M_f, not a same-baseline Mf or an exponent. Both components are typewritten.',
  'The unmarked C-context target in 6.5 is confirmed: two adjacent overtyped e/t positions. The first has a visible t ascender and bar beneath the rounded e body, while the second has an e-like lower contour under the live t stem and return. This is retained as ferm\\deleted{t}e\\deleted{e}ture.',
  'Each live section sign has the two opposed loops of §; each decimal entry number and point was checked. The two cancelled starts were separately cropped and are reported in decisions.',
  'Regular hollow-centred low leader impressions extend rightward from every live contents entry and sections 4, 5 and 7. Section 6 ends in one isolated period, without a leader row. These agree with C.'
 ],
 'check_events':[],
 'notation':[
  {'sign':'Ordinary typed letter prefixes','latex':'A; B','evidence':'Single ordinary typewriter outlines, separately inspected at all four occurrences; no independent doubled stems.','place':'4.1 twice, 4.2 and 4.3'},
  {'sign':'Module letter and subscript','latex':r'M_f','evidence':'Ordinary typewritten M followed by a distinct lowered f with crossbar and foot.','place':'6.2'},
  {'sign':'Section and decimal references','latex':r'\S\ 4.; \S\ 5.; \S\ 6.; \S\ 7.; 3.8.; 7.6.','evidence':'Opposed loops in the section signs; independently read typewriter digits and low points.','place':'Four live section headings and contents entries'},
  {'sign':'Unassigned point pair','latex':graphic,'evidence':'Small lower-left compact point and upper-right slanting teardrop; punctuation value and material origin unresolved.','place':'Far right, slightly below entry 6.5 leaders'}
 ],
 'abbreviations':[],
 'slips':[
  '6.2 has a cancelled incomplete project/projecti before the live continuation inductive; no longer deleted word has been supplied.',
  '6.5 contains two adjacent overtyped letters, retained as deleted t then live e, deleted e then live t.',
  '6.7 has a surplus cancelled l/1 immediately after sur.',
  'A cancelled section-start row remains above the live section 7 heading, and a cancelled numeric stub remains before the live 7.5.'
 ],
 'completion':'Complete diplomatic reading of scan 087: the whole image was viewed once, half a once, and half b once, in that order; every text line, number, accent, punctuation mark, leader group, overtyping/cancellation and marginal element was checked. Each of six remaining open loci received one retained enlarged crop and one actual visual inspection. Four explicit C doubts and every substantive difference are recorded. No OCR, external source, other page, other reader, delegation or TeX compilation was used.'
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(out/'processing.md').write_text('''# Scan 087 — reader A processing record\n\n## Inputs and viewing order\n\nRead only the assigned brief v09, conventions, PREAMBLE.tex, scan087 packet files, and the three named images. The packet notation table was read in full; a middle range omitted by tool-output truncation was retrieved as text. No other page or reader file was accessed.\n\n1. Whole-page source B37-04_37_scan087.jpg, 1687 × 2149: one actual view for layout.\n2. Half a, 1687 × 1154: one actual line-by-line view, top offset 0.\n3. Half b, 1687 × 1155: one actual line-by-line view, top offset 994.\n\nThe halves overlap by 160 pixels. No half was reopened or enlarged.\n\n## Open loci after the half readings\n\n- Cancelled project/projecti in 6.2.\n- Two overtyped adjacent letters in fermeture in 6.5.\n- Small dark pair to the far right of 6.5.\n- Cancelled l/1 after sur in 6.7.\n- Cancelled section-start row above section 7.\n- Cancelled numeric stub before 7.5.\n\nEach was cropped once from the original whole-page JPEG. Each crop was resized once to 2600 px across with LANCZOS, RGB autocontrast with cutoff 0, then UnsharpMask radius 1.2 / percent 110 / threshold 3; JPEG quality 95, no rotation. Exact bboxes, resulting dimensions, source path and processing are in crop_processing.json. Crops 01–03 and 04–06 were delivered in two batches of three. All six images reached the reader and were each actually inspected once; none was recropped or reopened.\n\n## Results\n\nThe ordinary contents text agrees with C. The unmarked e/t correction target in 6.5 is confirmed. The 7 in the cancelled section start is resolved, while the terminal point is retained as uncertain. Both cancelled number/point contexts explicitly allow an absent point. The cancelled word and surplus l/1 remain uncertain. The omitted dark point pair is typeset as an uncertain graphic; its origin is not assigned, and it is not diagnosed as a scratch or crease.\n\nNo OCR, recognition tool, PDF text, web source, mathematical proof check or TeX engine was used. Report validation and simple source-balance checks are recorded below after writing the reading.\n''')
print(json.dumps({'reading':str(out/'reading.tex'),'report':str(out/'report.json'),'decision_count':len(decisions),'c_doubt_rows':sum(d['c_doubt'] for d in decisions),'inventory_count':len(inventory),'crops':len(proc)},indent=2))
