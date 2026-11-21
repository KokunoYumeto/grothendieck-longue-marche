"""Generate the page-068 first-reader proposal and its audit metadata.
Inputs are the assigned packet plus retained, manually read page-068 data.
No OCR, outside page text, web source, or TeX compilation is used.
"""
from pathlib import Path
import csv,json,re,runpy
BASE=Path('/workspace/scratch/f28c4f52d3ec')
PAGE='148_scan068'
P=BASE/'packets'/PAGE
R=runpy.run_path(str(BASE/'proposed'/f'{PAGE}_readings.py'))
F=runpy.run_path(str(BASE/'proposed'/f'{PAGE}_figures.py'))
BANNER=R['BANNER']; ZERO=R['ZERO_COLUMNS']; OFFSET=R['ZERO_OFFSETS']; tt=R['tt']; FIG=F['FIGURES']
C=(P/'C.tex').read_text(); H=(P/'H.tex').read_text()
marks=list(csv.DictReader((P/'MARKS.tsv').open(),delimiter='\t'))
boxes=json.loads((BASE/'proposed'/f'{PAGE}_crop_boxes.json').read_text())
viewpaths=json.loads((BASE/'proposed'/f'{PAGE}_view_paths.json').read_text())

def macro_blocks(s, macro):
    out=[]; token='\\'+macro+'{'; at=0
    while True:
        i=s.find(token,at)
        if i<0:break
        j=i+len(token); depth=1
        while depth:
            if s[j]=='{':depth+=1
            elif s[j]=='}':depth-=1
            j+=1
        out.append(s[i:j]);at=j
    return out

cfig=macro_blocks(C,'figure'); cdiag=macro_blocks(C,'diagram')
cells=[]
for m in marks:
    v=m['the mark as written']
    assert v.startswith(r'\unsure{\texttt{') and v.endswith('}}')
    cells.append(v[len(r'\unsure{\texttt{'):-2].replace(r'\ ',' '))

def column_tex(values, uncertain_rows=()):
    rows=[('\\unsure{'+tt(s)+'}') if i in uncertain_rows else tt(s) for i,s in enumerate(values)]
    return '\\diagram{\\(\\begin{array}{l}\n'+'\\\\\n'.join(rows)+'\n\\end{array}\\)}'

banner_rows=[' & '.join(tt(BANNER[ch][r]) for ch in 'predonta') for r in range(12)]
banner_tex='\\diagram{\\begingroup\\tiny\\setlength{\\arraycolsep}{2pt}\\(\\begin{array}{llllllll}\n'+'\\\\\n'.join(banner_rows)+'\n\\end{array}\\)\\endgroup}'
zero_values=[]
zero_nodes=[]
for r in range(12):
    row=[]
    for col in range(4):
        s=' '*OFFSET[r]+ZERO[col][r]
        reading=tt(s)
        if r==0:reading='\\unsure{'+reading+'}'
        row.append(reading)
        zero_nodes.append('\\node[anchor=base west,inner sep=0] at ('+str(14*col)+','+str(r)+') {'+reading+'};')
    zero_values.append(row)
zero_tex='\\diagram{\\begingroup\\ttfamily\\scriptsize\n\\settowidth{\\unitlength}{0}\n\\begin{tikzpicture}[x=\\unitlength,y=-.30cm]\n'+'\n'.join(zero_nodes)+'\n\\end{tikzpicture}\\endgroup}'
jobs=[x for x in macro_blocks(C,'texttt') if x.startswith(r'\texttt{****A END JOB')]
assert len(jobs)==6
job_tex='\n\n'.join(jobs)
folio_tex=r'\mspage{67}'
order=['loop','small_edges','chord_circle','long_edge','short_edge','holes']
tex='\\scanpage{68}\n'+ '\n\n'.join(FIG[x] for x in order)+'\n\n% The reused computer listing is upside down relative to the pencil drawings.\n'+job_tex+'\n\n'+banner_tex+'\n\n'+zero_tex+'\n'+folio_tex+'\n'
(BASE/'proposed'/f'{PAGE}.tex').write_text(tex)

changes=[]
def change(place,c,h,final,diff_c,diff_h,kind,error,evidence,crop,confidence='high',consequential=False):
    changes.append({'id':f'{PAGE}-{len(changes)+1:02d}','place':place,'c':c,'h':h,'final':final,'diff_c':diff_c,'diff_h':diff_h,'kind':kind,'error_kind':error,'evidence':evidence,'crop':f'crops/{PAGE}_{crop}.png','box':boxes[crop],'confidence':confidence,'marked_in_h':False,'consequential':consequential})

scope=cfig[0][cfig[0].find(r'\begin{scope}'):cfig[0].find(r'\end{scope}')+len(r'\end{scope}')]
cloop=cfig[0].replace(scope,'')
change('upper pencil drawing: sole vertex and loops',cloop,'une boucle attachée à un sommet',FIG['loop'],True,True,'drawing or diagram','Drawings and diagrams','Four pencil runs leave the sole dark vertex. One outline rises leftward and returns diagonally; another rises almost vertically, crosses the first away from the vertex, and returns from the lower right. These are two overlapping closed loops, not C\'s three-branch outer loop with one interior arc. No additional crossing vertex is marked.','loop',consequential=True)
change('top row of miniature point/edge figures',scope,'absent',FIG['small_edges'],False,True,'omission','Omissions','Three pairs have a visible short joining stroke; the next two pairs have no joining stroke. Ten substantial dark endpoint marks are visible. Nearby tiny isolated specks do not share their size or form and are not graph vertices or labels.','small_edges',consequential=True)
change('six-vertex oval and its internal pencil strokes',cfig[1],'un cercle portant six sommets',FIG['chord_circle'],True,True,'drawing or diagram','Drawings and diagrams','Six dark vertices are certain. The clearest interior strokes run from the upper-left-side vertex toward the lower-right vertex, and from the bottom vertex toward the lower-right vertex; the lower inner arc and perimeter retracings are also visible. Faint upper-to-lower portions disappear beneath the printed hatching. Their visible fragments are retained, with an in-place doubt about their joins, instead of C\'s completed five-chord graph.','chord_circle','medium',True)
change('long dark two-vertex edge and thin surroundings',cfig[2],"deux arêtes à deux sommets, chaque sommet entouré de petits cercles et l'arête entourée de courbes ovales",FIG['long_edge'],True,True,'drawing or diagram','Drawings and diagrams','The dark edge has two marked endpoints, thin continuations beyond both ends, endpoint enclosures, a long surrounding contour, and two thin rays at the right endpoint. The surrounding outline and right endpoint enclosure have pen gaps. The paths are traced with those gaps; C\'s forced closed surrounding contour and exact circles conceal them. H does not record the extensions or rays.','long_edge')
change('short dark/retraced two-vertex edge in a broad enclosure',cfig[3],"deux arêtes à deux sommets, chaque sommet entouré de petits cercles et l'arête entourée de courbes ovales",FIG['short_edge'],True,True,'drawing or diagram','Drawings and diagrams','Two dark endpoint marks have small thin enclosures. Two closely spaced traced runs make the joining edge, with a narrow pale interval between them in the middle. The broad surrounding curve has a visible upper pen gap and the left endpoint enclosure has a small gap; these are not replaced by exact closed ellipses.','short_edge')
change('two-hole oval with connecting and radial strokes',cfig[4],'un disque à deux trous reliés par une bande, avec des segments radiaux.',FIG['holes'],True,True,'drawing or diagram','Drawings and diagrams','The two inner closed outlines, the outer oval with its upper pen gap, two principal connecting strokes, and the source-visible radial runs are reproduced. Additional faint connecting/upper radial fragments and the upper-left run from the lower hole cannot all be joined securely through the hatching. They remain visibly doubtful; no missing run is supplied by symmetry and the ten evenly regular spokes in C are not imposed.','holes','medium',True)
change('six repeated job-record lines, read with listing upright',job_tex,'absent',job_tex,False,True,'omission','Omissions','Each of the six lines was read separately. All have four initial asterisks, A, END JOB 653, PREDONTA, ROOM, 11.24.04 AM 02 JUN 82, R6.PR1, SYS JES2 JOB 653 END, A and four final asterisks. The periods in the timestamp and R6.PR1 and both job numbers are visible on every line. H mentions the date editorially but does not transcribe the printed lines.','job_records')

bevidence={
'p':'The first and seventh bars each contain eleven P forms (eleven stems and upper bowls), not ten; rows two and six contain twelve. Rows three to five have PP at each end with eight empty character cells; rows eight to twelve contain only the initial PP.',
'r':'The first and seventh bars each have eleven R forms, not ten. Rows eight through twelve have the right RR pair after respectively four, five, six, seven and eight blank cells following the initial RR. C places the right pair one column too far left in rows eight through eleven. The second and sixth bars contain twelve R forms, and the upper side rows have eight internal blanks.',
'e':'Both middle horizontal bars (rows six and seven) contain eight E forms, with their three short horizontal strokes visible, not seven. The top two and bottom two bars contain twelve; the other rows contain the left EE only.',
'd':'The top and bottom bars each contain nine D forms, not eight. Rows two and eleven contain ten. The right DD pair is one column inward on rows three and ten: seven blank cells separate the left and right pairs there, versus eight on rows four through nine. C flattens those side-row offsets.',
'o':'The top two and bottom two bars each contain twelve closed O forms. Every middle row has two O forms at each side and eight empty cells between them. This agrees with C after resolving its twelve separate doubts.',
'n':'The diagonal advances one printer column per row; each N has the diagonal between two uprights. The final row visibly has NN at the left and only one N at the far-right cell, with the preceding right-stem cell blank. That irregularity agrees with C and is preserved.',
 't':'The two upper bars each contain twelve T forms. Each of the following ten rows has TT in the two central cells, with five blank cells on each side. The clear crossbars and vertical stems settle the twelve C marks.',
 'a':'The first row has ten A forms inset one cell at each end; rows two, six and seven have twelve. All other rows have AA at each side separated by eight blank cells. The two sloping legs and middle bars distinguish the A forms.'}
for col,ch in enumerate('predonta'):
    cvalues=[cells[r*8+col] for r in range(12)]
    ctex=column_tex(cvalues,range(12))
    final=column_tex(BANNER[ch])
    differs=cvalues!=BANNER[ch]
    change('printed PREDONTA banner: '+ch.upper()+' block, all twelve rows',ctex,'absent',final,differs,True,'drawing or diagram' if differs else 'omission','Drawings and diagrams' if differs else 'Omissions',bevidence[ch]+' H omits this printed block.','banner_'+ch)
change('four large printed zero patterns, all twelve rows and fixed-pitch positions',cdiag[1],'absent',zero_tex,True,True,'drawing or diagram','Drawings and diagrams','All four patterns were read individually. Their glyph bases are fourteen printer columns apart. Relative row starts are ten, nine, seven, six, five, four, three, two, one, zero, zero and zero cells from each base: the zero shapes lean strongly. The middle row gaps and the merged four-zero row differ from C\'s upright array. Rows two through twelve are countable at each glyph; in row one the hatching obscures portions of the eight candidate zero outlines, so all four supplied marks remain undecided. The apparently small labels above/below at half scale are simply the faint first and last zero rows; no words are added.','zero_fields','medium')
change('pale handwritten lower folio',folio_tex,'absent',folio_tex,False,True,'omission','Omissions','The first digit has the upper entry and lower closed loop of 6; the second has the long upper stroke, descending stroke and crossbar of 7. The folio is 67.','folio')

# Every supplied MARKS row has its own evidence record.
decisions=[]
letter_shape={'p':'upright stem and upper bowl','r':'upright, upper bowl and descending leg','e':'upright and three horizontal strokes','d':'upright left side and rounded right side','o':'closed rounded outline','n':'two uprights joined by a diagonal','t':'top crossbar and descending upright','a':'two sloping legs and middle crossbar'}
for i,m in enumerate(marks):
    if i<96:
        row,col=divmod(i,8);ch='predonta'[col];s=BANNER[ch][row]
        positions=[j+1 for j,c in enumerate(s) if c!=' ']
        ev=f'PREDONTA block {ch.upper()}, upright row {row+1}: {len(positions)} {ch.upper()} forms at local printer cells '+', '.join(map(str,positions))+f'. The {letter_shape[ch]} is visible; blank cells are measured against the fixed pitch, not filled from a regular glyph template.'
        crop='banner_'+ch; reading=tt(s); dec='first' if s==cells[i] else 'other'; conf='high'
    else:
        row,col=divmod(i-96,4);s=' '*OFFSET[row]+ZERO[col][row]
        crop='zero_fields';reading=zero_values[row][col]
        if row==0:
            dec='undecided';conf='low'
            ev=f'Zero pattern {col+1}, first upright row: the candidate eight zero outlines fall after ten leading fixed-pitch cells, but printed hatching and faint impression obscure individual loops. The eight-zero reading is retained as a doubt, independently for this pattern. The shifted row position is clear; it does not settle the count.'
        else:
            positions=[j+1 for j,c in enumerate(s) if c!=' ']
            ev=f'Zero pattern {col+1}, upright row {row+1}: {len(positions)} narrow zero outlines occupy local printer cells '+', '.join(map(str,positions))+f'. This occurrence was counted in the complete-array crop. Its row start is {OFFSET[row]} cells to the right of the bottom-row base; internal empty cells and the diagonal are retained as seen.'
            dec='first' if s==cells[i] else 'other';conf='high'
    decisions.append({'id':m['id'],'decision':dec,'reading':reading,'evidence':ev,'crop':f'crops/{PAGE}_{crop}.png','box':boxes[crop],'confidence':conf})

implicit=[]
for num,(name,dec,conf,ev) in enumerate([
('loop','other','high','The sole vertex has four incident visible runs and two returning loop outlines.'),
('small_edges','first','high','Three joined pairs and two unjoined pairs, ten endpoint marks in total.'),
('chord_circle','undecided','medium','Six vertices and the strongest diagonals are readable; faint upper-to-lower joins beneath the hatching remain open.'),
('long_edge','other','high','Visible pen gaps, extensions and both right-end rays are retained rather than closed geometrically.'),
('short_edge','other','high','The doubled/retraced dark edge and visible gaps in thin enclosing paths are retained.'),
('holes','undecided','medium','The holes and visible run fragments are retained; some faint radial/band connections cannot be completed securely.'),
('folio','first','high','Visible closed lower loop of 6 and crossbar/descending stroke of 7.')],1):
    implicit.append({'id':f'I{num:02d}','decision':dec,'reading':folio_tex if name=='folio' else FIG[name],'evidence':ev,'crop':f'crops/{PAGE}_{name}.png','box':boxes[name],'confidence':conf})

doubts=[
 {'place':'six-vertex oval: faint interior joins','reading':FIG['chord_circle'],'alternatives':'The visible upper-to-lower fragments may join different lower vertices or be parts of retraced outlines; the complete five-chord incidence supplied by C is not secure.','confidence':'medium','reason':'Pencil strokes disappear beneath the printed hatching. The proposed figure follows visible fragments and does not complete the hidden joins.'},
 {'place':'two-hole oval: faint connecting and radial joins','reading':FIG['holes'],'alternatives':'Some faint band/radial fragments may join the adjacent outline or continue differently under the hatching; their precise incidence and independent stroke count remain open.','confidence':'medium','reason':'The faint strokes are partially lost against the printer bands. No symmetric missing spoke is supplied.'}
]
for col in range(4):
    doubts.append({'place':f'large zero pattern {col+1}, first upright row (M{896+col:04d})','reading':zero_values[0][col],'alternatives':'Eight zero characters remain the leading reading; the obscured individual outlines prevent a secure count.','confidence':'low','reason':'The printed first row is faint within the hatched band; its row offset is visible but not every candidate zero is independently complete.'})

inventory=[]
def inv(hand,kind,pos,objects):
    inventory.append({'element':f'E{len(inventory)+1:02d}','sheet_kind':'reused_typed','hand':hand,'kind':kind,'position':pos,'first_words_or_objects':objects,'transcribed':'yes'})
inv('his hand','drawing','upper drawing group, left','sole dark vertex with two overlapping loops')
inv('his hand','drawing','upper drawing group, small top row','three joined endpoint pairs followed by two unjoined pairs')
inv('his hand','drawing','upper drawing group, right','oval with six dark vertices and internal strokes')
inv('his hand','drawing','middle of pencil group, left','long dark edge with two vertices, endpoint enclosures, outer curve and rays')
inv('his hand','drawing','lower pencil group, left','short dark/retraced edge with two vertices and thin enclosing paths')
inv('his hand','drawing','lower pencil group, right','two-hole oval with connecting and radial strokes')
inv('print','text','six rows across sheet below the upper sketches; upside down relative to them','****A END JOB 653 PREDONTA; six complete repeated records')
inv('print','display','large middle printer banner, upside down relative to sketches','PREDONTA formed by twelve rows of repeated letters')
inv('print','display','lower printer block, upside down relative to sketches','four large slanted zero patterns formed by twelve rows of zero characters')
inv('unnamed hand (folio annotation; attribution uncertain)','margin note','lower left edge in sketch orientation','67')
notes=[
 {'id':f'{PAGE}-N01','text':'The mathematical content is pictorial: a one-vertex two-loop figure, miniature edge/point pairs, an oval with six vertices and internal strokes, two two-vertex edge neighborhoods, and a two-hole region with radial/connecting strokes. There is no accompanying handwritten theorem, argument or formula on this leaf. The six-vertex and two-hole figures retain explicit doubts about faint joins. This is a transcription of the drawings, not a proof of any topological assertion.'},
 {'id':f'{PAGE}-N02','text':'The reused listing is upside down relative to the pencil sketches. All six printed records give job 653, PREDONTA, 11.24.04 AM 02 JUN 82 and R6.PR1, with SYS JES2 JOB 653 END. The large letter banner and all four zero patterns are part of the source and are transcribed in full. The first four zero-row counts remain uncertain. Leading positions and internal blank printer cells are retained, including the last row of N with only one right-hand N.'},
 {'id':f'{PAGE}-N03','text':'H\'s prose synopsis, quotation of the printer date and reference to figures of page 66 are editorial material, not handwritten prose on this leaf. They are not added to the transcription. Its qualitative drawing descriptions do not substitute for the source paths. No separate small labels occur around the zero block: the suspected runs are its first and last rows of zeros.'},
 {'id':f'{PAGE}-N04','text':'The broad colored/hatched printer bands and scattered tiny specks are background, not deletion strokes or extra graph vertices. No insertion or struck text is identified on this leaf. The visible pencil pen gaps are preserved; no exact ellipse or symmetric set of spokes is silently imposed. The pale folio is 67, attributed only to an unnamed hand because appearance alone does not identify its writer.'},
 {'id':f'{PAGE}-N05','text':'Physical line count: six job-record lines, twelve rows of the PREDONTA banner, twelve rows of the four-zero block, and the one folio numeral line = 31. Six drawing units were also read completely. Some evidence/audit rectangles contain neighboring drawing fragments because complete extended paths overlap their rectangular bounds; the named complete target units cover those neighboring figures separately.'}
]
check_events=[{'statement_id':f'{PAGE}-N01','type':'carried as background without fault found','outcome':'The visible sketch objects, marked vertices, open paths and doubtful joins were read and transcribed. No mathematical proposition is asserted in words here, and no proof or independent re-proof is claimed.'}]
notation=[
 {'sign':'dark filled marks in the pencil figures','meaning_or_form':'Marked vertices/endpoints; distinguish them from isolated small paper specks. No vertex is marked at the crossing of the two loops.','places':'148_scan068 upper loops, miniature pairs, six-vertex oval and both dark edges','universality':'Consistent within the six inspected drawing units of this leaf; not asserted as a universal hand rule.','witness_errors':'C gives only three runs at the sole loop vertex; H omits the miniature point/edge row.'},
 {'sign':'printed 0 and O','meaning_or_form':'The four large slanted numeric zero patterns consist of narrow zero outlines; the O of PREDONTA consists of letter O forms. Fixed-pitch blanks carry the printed geometry.','places':'148_scan068 PREDONTA O block and four-zero block','universality':'Limited to this printer sheet.','witness_errors':'C distorts several letter counts and the zero-pattern row offsets/internal gaps; the final single N in the right stem is genuine and retained.'}
]
second=[]
def audit(name,kind,reading,target):
    x0,y0,x1,y1=boxes[name]
    second.append({'box':f'B{len(second)+1:02d}','kind':kind,'x0':x0,'y0':y0,'x1':x1,'y1':y1,'reading':reading,'target':target})
for name in order:
    audit(name,'handwritten on typescript',FIG[name],name.replace('_',' '))
audit('job_records','different words',job_tex,'all six complete printed job records')
for ch in 'predonta':audit('banner_'+ch,'different words',column_tex(BANNER[ch]),'complete twelve-row '+ch.upper()+' block of printed banner')
audit('zero_fields','low-confidence departure',zero_tex,'all four complete twelve-row zero patterns, including four doubtful first rows')
audit('folio','handwritten number',folio_tex,'complete lower folio numeral')

out={'page':PAGE,'reader':'reader_c','lines_read':31,'changes':changes,'decisions':decisions,'implicit_decisions':implicit,'doubts':doubts,'inventory':inventory,'notes':notes,'check_events':check_events,'notation':notation,'abbreviations':[{'form':'AM','expansion':'ante meridiem (printed timestamp)'},{'form':'JUN','expansion':'June (printed date)'}],'second_boxes':second,
 'agreed_ink_checks':[
  'All six repeated job-record strings checked separately against the image; agreement with C is recorded, not assumed.',
  'All 96 letter-banner rows/cells and all 48 zero-pattern rows/cells inspected in their own whole-glyph/whole-array evidence crops.',
  'O, N, T and A agree with C after examination, including the anomalous final single N.',
  'No handwritten words, formula labels, numeral labels, insertions or cancellations are visible among the drawings; the only handwritten numeral is folio 67.'
 ],
 'supporting_evidence':[{'name':n,'crop':f'crops/{PAGE}_{n}.png','box':boxes[n],'viewed':True,'transport_view':viewpaths[n] if n=='zero_fields' else None} for n in boxes],
 'reading_protocol':{'original_views':1,'prepared_half_views':[1,1],'evidence_crops_viewed':17,'second_reading_started':False,'ocr_used':False,'web_used':False,'tex_compiled':False,'transport_note':'The two oversized prepared PNG halves and the zero-fields evidence crop were viewed through lossless WebP copies at identical dimensions, with decoded pixel equality verified. Failed image-transport calls delivered no image and are not counted as views. Canonical PNG files remain unchanged.'}}
(BASE/'proposed'/f'{PAGE}.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
# Retain the troubleshooting handoff, but make its superseded status explicit.
handoff=BASE/'proposed'/f'{PAGE}_reader_handoff.md'
if handoff.exists():
    status='## Current status (supersedes the troubleshooting handoff below)\n\nThe same reader_c continued successfully. The original and both prepared halves have each been read once; lossless WebP transport solved the oversized image delivery issue. All seventeen evidence crops have been read. The complete first-reading proposal and metadata are now in proposed/148_scan068.tex and proposed/148_scan068.json. No replacement reader or blind second reading was used.\n\n'
    prior=handoff.read_text()
    if not prior.startswith('## Current status'):handoff.write_text(status+prior)
print(json.dumps({'tex':str(BASE/'proposed'/f'{PAGE}.tex'),'json':str(BASE/'proposed'/f'{PAGE}.json'),'changes':len(changes),'marks':len(decisions),'decisions':{k:sum(x['decision']==k for x in decisions) for k in ['first','other','undecided']},'implicit':len(implicit),'doubts':len(doubts),'inventory':len(inventory),'audit_boxes':len(second)},ensure_ascii=False))
