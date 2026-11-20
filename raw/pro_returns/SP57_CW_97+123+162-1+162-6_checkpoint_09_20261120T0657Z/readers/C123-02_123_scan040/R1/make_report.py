from pathlib import Path
import json,re
base=Path('out/readers/C123-02_123_scan040/R1')
c=Path('packets/C123-02_123_scan040/C.tex').read_text()
h=Path('packets/C123-02_123_scan040/H.tex').read_text()
r=(base/'reading.tex').read_text()
source='source/SP57_CW_97+123+162-1+162-6_scans/C123-02_123_scan040.jpg'
manifest=[json.loads(x) for x in (base/'crops/crop_manifest.jsonl').read_text().splitlines()]
crops={int(x['dest'].split('_')[0]):x for x in manifest}
def crop(n): return None if n is None else 'readers/C123-02_123_scan040/R1/crops/'+crops[n]['dest']
def pic(text,marker):
 pos=text.index(marker); start=text.rfind(r'\begin{tikzpicture}',0,pos)
 assert start>=0, marker
 dep=0
 for m in re.finditer(r'\\(begin|end)\{tikzpicture\}',text[start:]):
  dep+=1 if m.group(1)=='begin' else -1
  if dep==0:return text[start:start+m.end()]
 raise ValueError(marker)
def span(text,a,b):
 start=text.index(a); end=text.index(b,start)+len(b); return text[start:end]
def command(text,a):
 start=text.index(a); b=text.index('{',start); depth=0
 for i in range(b,len(text)):
  if text[i]=='{':depth+=1
  elif text[i]=='}':
   depth-=1
   if depth==0:return text[start:i+1]
 raise ValueError(a)
D=[]
def add(place,C,H,reading,evidence,confidence='high',kind='omission',n=None,bbox=None,c_changed=False,h_changed=True,marked=False):
 assert reading
 if C: assert C in c, ('C string absent',place,C)
 if H: assert H in h, ('H string absent',place,H)
 if bbox is None: bbox=crops[n]['box']
 D.append(dict(id='R1-D%02d'%(len(D)+1),place=place,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=marked,c_changed=c_changed,h_changed=h_changed,crop=crop(n),bbox=bbox,bbox_source='whole image: '+source))
add('Upper-right manuscript page number and arch',r'\mspage{\handwritten{23}}','',command(r,r'\mspage{'),'The crop shows 2 then 3 beneath a separate rising curved stroke; C preserves the numeral but omits that stroke. H supplies an archive page marker, not this manuscript number.',kind='drawing or diagram',n=22,c_changed=True)
add('Opening typed continuation',span(c,'sent en termes','inductives)'),'','sent en termes de limites projectives finies exclusivement, tandis que les autres notions impliquent implicitement des constructions faisant appel également à des limites inductives)','The half shows the opening fragment sent and three typed lines. H does not transcribe this passage, although its later note quotes the endpoint limites inductives).',n=None,bbox=[270,140,1663,315])
add('Top note: adjective after opérations','fonctorielles','fonctionnelles','fonctorielles','The handwritten succession has c-t-o-r-i before elles; there is no n-n sequence for fonctionnelles.',kind='misread word',n=1)
add('Top note: position of the obliterated word',r'fonctorielles \deleted{\illegible{1}} habituelles',r"les opérations qui \struck{\ill{}}" ,r'fonctorielles \deleted{\illegible{1}} habituelles','A dense cancellation lies immediately after fonctorielles and before habituelles. The surviving marks do not yield a complete word. H places its explicit ill at the later qui locus.',confidence='high',kind='insertion or placement',n=1,marked=True)
add('Top note: retouched ending of s’exprime',r"s'exprime\deleted{nt}\unsure{r}","s'exprimer",r"s'exprime\deleted{nt}\unsure{r}",'The base exprime is readable; two following forms are heavily retouched, with a possible r laid over the first and a dark terminal t-shaped remnant. C’s local doubt is retained. H prints only the final infinitive.',confidence='low',kind='deletion state (struck given live or live given struck)',n=2)
add('Top note: peuvent insertion leader',r'\inserted{peuvent}',"peuvent s'exprimer",pic(r,'(v)'),'Peuvent sits above the verb and has an under-running line bending down before s’. C marks the insertion but does not draw its leader; H linearizes it.',kind='drawing or diagram',n=2,c_changed=True)
add('Top note: enclosure and matching lower-loop sign',command(c,r'\figure{'),span(h,r'\note{en tête du feuillet','suivante}'),command(r,r'\figure{'),'The half shows a left-and-bottom open enclosure with a step in the bottom edge and a stem ending in a low loop. H describes an enclosure/link in prose but supplies neither actual drawing nor call sign.',kind='drawing or diagram',bbox=[241,16,1670,147])
add('After inductives: additional close-shaped pen trace',r'inductives)\handwritten{)}.','',span(r,'inductives)', '\\end{tikzpicture}}}.'),'A thin close-shaped pen stroke lies between the typed close and the heavy bracket. Its upper relationship to the insertion boundary is not secure. The shape is drawn with uncertainty rather than asserted to be a second punctuation parenthesis.',confidence='medium',kind='other',n=4,c_changed=True)
add('De plus note: quotation strokes and underline',r"``\uline{commute}''",'« commute »',r"``\uline{commute}''",'Two short quotation strokes on each side and a separate underline beneath commute are visible. H uses guillemets and omits the underline.',kind='misread symbol or index',n=4)
add('De plus note: long lower enclosing curve',span(c,'De plus, le foncteur',r'\tikz[baseline=-0.3ex,scale=.18]{\draw (0,1.3)--(0,.15) .. controls (-.4,-.2) and (.4,-.2) .. (0,.15);}'),r'\marginal{De plus, le foncteur $u^*$ « commute » à toutes}',pic(r,'(plus)'),'A continuous pen line begins beside De plus, runs under the note, and bends below the right call sign. The call sign itself has a low loop. C has the sign but not the long line; H gives the words only.',kind='drawing or diagram',n=4,c_changed=True)
add('Left-margin instruction: après',r'à la ligne après : Quant au...',r'à la ligne, puis : Quant au …',r'à la ligne après : Quant au...','The second slanted row begins a-p-r-è-s, then a colon. No comma follows ligne; three separate dots follow au.',kind='misread word',n=5)
add('Left-margin instruction: two slanted rows and enclosure',span(c,r'\margin{\handwritten{\figure{',r'\end{tikzpicture}}}}'),r'à la ligne, puis : Quant au …',command(r,r'\margin{'),'The first row à la ligne sits above the second row, which begins farther left; both rise to the right inside an enclosure open on the left. C’s single upright text node loses this geometry.',kind='insertion or placement',n=5,c_changed=True)
add('Opposing brackets at Quant au',span(c,r'\handwritten{\tikz[baseline=-.6ex',r'Quant au'),"""Quant au foncteur image
directe $u_*$""",pic(r,'(q)'),'The heavy opposing brackets bound the break before Quant au; the right opening bracket runs above and below Quant au. The saved drawing now anchors those words inside the bracket rather than placing two unattached signs before them.',kind='drawing or diagram',n=4,c_changed=True)
add('Direct-image map: insertion leader',r"$\mathrm{u}_{\handwritten{*}}$\inserted{$:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$},",r"$u_*$ » reçoit « $: E \to E'$ »,",pic(r,'(d)'),'The raised map has ordinary typed E, E-prime, a pen right arrow, and a curved leader descending immediately before the baseline comma after u-star. The comma remains in the drawing’s baseline text.',kind='drawing or diagram',n=6,c_changed=True)
add('Par suite: curved leader to toute',r'\inserted{par suite} toute',r'« respecte » reçoit « par suite »',pic(r,'(b) {toute}'),'The raised typed par suite has a curve running under it and dropping before toute. C has the words as an insertion but omits the curve; H mentions the addition editorially.',kind='drawing or diagram',n=7,c_changed=True,bbox=[1424,313,1624,397])
add('Exclusivement: curved leader before parenthesis',r'\inserted{exclusivement} (telles',r'« définissable en termes de limites projectives » reçoit « exclusivement »',pic(r,'(b) {(telles}'),'The curved leader drops before the typed opening parenthesis; the raised word is typescript. The drawing keeps (telles in its baseline node.',kind='drawing or diagram',n=7,c_changed=True,bbox=[1091,453,1392,540])
add('Cancelled dans beneath parmi',r'\deleted{dans}\inserted{parmi}',r'« parmi » remplace un mot biffé',r'\deleted{dans}\inserted{parmi}','The lower cells retain d-a-n-s beneath cancellation; parmi is typed above. H mentions a crossed word without transcribing its readable letters.',n=7,bbox=[1209,541,1325,594])
add('Par contre: overlapping f/c without secure chronology',r'Par \deleted{f}contre,','',span(r,'Par \\unsure{',r'\end{tikzpicture}}ontre,'),'An ascender and hook of f coexist with the open bowl of c. Both are typescript; their impression order is not established by the surviving contours. C assigns f to a deleted predecessor; the reading preserves the overlay with local uncertainty.',confidence='medium',kind='other',n=8,c_changed=True,bbox=[629,631,663,666])
add('Cancelled e in n[e]’est',r"n\deleted{e}'est",'',r"n\deleted{e}'est",'The e cell between n and apostrophe is crossed by a typewriter x. C retains it; H’s synopsis does not transcribe this correction.',n=8,bbox=[1076,633,1160,668])
add('First typed paragraph: full source wording beyond quoted additions',span(c,'Quant au foncteur image directe',r"dans l'exposé suivant\handwritten{)}."),span(h,'$u_*$\nrespecte toute structure',"dans l'exposé suivant"),span(r,r'\begin{tikzpicture}[baseline=(q.base)]',r"dans l'exposé suivant\handwritten{)}."),'The complete typed body is visible in half a, including the structure examples, failure of right exactness and epimorphism preservation, and cohomological parenthesis. H’s corresponding passage is explicitly an editorial synopsis, not a literal transcription; its paraphrases are not treated as assertions about deletion state.',bbox=[273,276,1671,1098])
add('Punctuation after second épimorphisme',r'\handwritten{\unsure{;|,}}','',r'\handwritten{\unsure{;|,}}','The punctuation has a short upper mark, a darker lower loop/tail, and retouching before the separate opening parenthesis. Semicolon remains first candidate, comma second; neither is resolved by grammar.',confidence='low',kind='other',n=9)
add('Separate cancellation x and small pen trace before comme','', '',pic(r,'(x) {\\texttt{x}}'),'A separate typewriter x occupies the cell immediately after d’ailleurs; a short oblique pen trace rises at its upper right. C and H omit this separate mark. The x is definite; the function of the small pen trace is uncertain and is drawn under its own unsure wrapper.',confidence='medium',kind='drawing or diagram',n=10,c_changed=True,bbox=[672,846,708,884])
add('Cancelled clause after c’est d’ailleurs',r'\deleted{\unsure{comme} nous le verrons au}','',r'\deleted{\unsure{comme} nous le verrons au}','Nous le verrons au is recoverable through the x run. The first word has visible c/o and merged central strokes but remains doubtful comme; the pen and x cancellation are real. H’s synopsis does not transcribe the deleted clause.',confidence='medium',n=10,bbox=[705,840,1185,885])
add('Second pen note: cancelled transforme pas',r'\deleted{transforme pas}\inserted{s\'étend pas}' if False else r"\deleted{transforme pas}\inserted{s'étend pas}",r'« s’étend pas »' if '« s’étend pas »' in h else "« s'étend pas » au-dessus d'un mot\nbiffé",r"\deleted{transforme pas}\inserted{s'étend pas}",'The baseline trace retains transforme pas under a heavy crossing run; s’étend pas is raised above it. H acknowledges a crossed word in a note but omits its readable wording.',n=11,bbox=[1127,1024,1394,1089])
add('H attaches en présence d’ to the wrong note',r"\deleted{se donne}\inserted{est \inserted{\handwritten{en}} présenced'}un",r"\marginal{Par suite, il ne s'étend pas, en général, en présence d'}",pic(r,"(b) {un}"),'The pen note ends en général, followed by its upper-loop call sign. Est présenced’ is a separate typed replacement below, belonging to the next paragraph, with en written above the gap. H appends that lower replacement to its handwritten note. C’s lexical placement is retained.',kind='insertion or placement',n=11,bbox=[813,1023,1661,1138])
add('Second note and footer: matching upper-loop calls and separator',command(c,r'\inserted{\handwritten{Par suite'),r"appel d'une note de bas de page, de sa main :",command(r,r'\inserted{\handwritten{Par suite'),'The half shows a call sign with its loop at the top after en général and the matching sign at the footer, below a long separator with a short left step. H describes a footnote call but supplies no graphic transcription.',kind='drawing or diagram',bbox=[22,2003,1667,2127])
add('Footer begins en un, not ou un','en un foncteur','ou un foncteur','en un foncteur','The first small word has an e-like entry connected to one n-shaped hump, before a distinct un. It is en; H reads ou.',kind='misread word',n=19,bbox=[113,2041,386,2088])
add('Footer: comma after groupe','groupe,','groupe et',r'groupe\unsure{,} et','A terminal downward-curving stroke follows groupe, but it is not securely separable from the last letter’s flourish. The comma is retained with doubt; H supplies none.',confidence='low',kind='other',n=20,c_changed=True,bbox=[1488,2046,1601,2092])
add('Footer: cancelled small word before module libre',r'\deleted{\unsure{le|de}}','',r'\deleted{\unsure{le|de}}','The dense small cancellation leaves a loop and a short upright trace; le and de remain possible. H omits this crossed word in its literal marginal transcription.',confidence='low',n=20,bbox=[1100,2074,1143,2114])
add('Footer: quotation strokes around module libre engendré',r"``module libre engendré''",'« module libre engendré »',r"``module libre engendré''",'Two upright opening strokes appear just after the cancellation and a pair of short closing strokes appears after engendré. They are quotation strokes, not angled guillemets.',kind='misread symbol or index',n=20)
add('Section numeral corrected from 2 to 3',r'\deleted{2}\handwritten{3}.1.3.','',r'\deleted{2}\handwritten{3}.1.3.','The initial cell contains the underlying typed 2 and a handwritten 3. H’s editorial synopsis labels section 3.1.3 but does not transcribe the correction.',n=12,bbox=[279,1125,403,1169])
add('Replacement est présenced’: leader and source spacing',r"\deleted{se donne}\inserted{est \inserted{\handwritten{en}} présenced'}un",'',r'\deleted{se donne}'+pic(r,'(b) {un}'),'The raised typescript joins présence directly to d’, with no intervening machine space; en is a smaller pen insertion above. A long lower curve descends before baseline un. C records the wording but not this leader.',kind='drawing or diagram',n=12,c_changed=True,bbox=[882,1082,1227,1168])
add('Second typed paragraph: literal body omitted by H',span(c,r'\deleted{2}\handwritten{3}.1.3.',"il y a lieu d'écrire $\\mathrm{f}$ sous la forme"),span(h,'3.1.3 : devant un',"l'écrire $f = u^*$"),span(r,r'\deleted{2}\handwritten{3}.1.3.',"il y a lieu d'écrire $\\mathrm{f}$ sous la forme"),'Half b supplies the full wording on exactness, adjoints, geometric nature and intuition. H gives a synopsis; it does not literally transcribe these sentences. In particular, its synopsis’s mathcal U is not treated as a direct source reading of the underlined typed U on this page.',bbox=[281,1082,1666,1794])
add('Explicit cancellation of se donne',r'\deleted{se donne}','',r'\deleted{se donne}','The seven typed letters se donne remain visible under x cancellation before un. H does not quote that deletion.',n=12,bbox=[907,1124,1075,1167])
add('Toutes: leader before baseline les',r'\inserted{\handwritten{toutes}} les','',pic(r,'(b) {les}'),'Toutes is penned above les; its line passes beneath the added word and curves down immediately before the baseline les. The drawing anchors the actual word les.',kind='drawing or diagram',n=13,c_changed=True,bbox=[1255,1159,1389,1236])
add('Propriétés: two é/t overlaps with uncertain order',r'propri\deleted{t}é\deleted{é}tés','',span(r,'propri\\unsure{',r'\end{tikzpicture}}és'),'Both cells retain the round e body, acute accent, and t stem/crossbar in different positions. The physical superpositions are definite but do not establish which impression came first. C’s deleted/live order is replaced by two locally doubtful literal overlays.',confidence='medium',kind='other',n=13,c_changed=True,bbox=[1468,1193,1527,1239])
add('Cancelled first formulation about an exact adjoint',r'\deleted{y compris et de déterminer s\'il admet un foncteur exact}' if False else r"\deleted{y compris et de déterminer s'il admet un foncteur exact}",'',r"\deleted{y compris et de déterminer s'il admet un foncteur exact}",'All words survive below the typewriter x run, including exact at the right. H’s synopsis omits this cancelled formulation.',n=14)
add('Cancelled qui before compréhension',r'\deleted{qui}','',r'\deleted{qui}','The q descender, u bowl and i dot survive the three crossed cells. H does not transcribe this cancellation.',n=15,bbox=[1201,1473,1269,1522])
add('Une replacement: cancelled l’ and insertion curve',r"\deleted{l'}\inserted{une}intuition",'',pic(r,"(b) {\\deleted{l'}intuition}"),'Une is typed above the cancelled l-apostrophe cells; a pen line beneath une bends down before them. Intuition begins immediately after the cancelled cells. C omits the curved leader.',kind='drawing or diagram',n=15,c_changed=True,bbox=[1144,1510,1330,1591])
add('Two stepped enclosures around f=u-star and u:F→E',pic(c,r'(n) {$\mathrm{f}=')+'\noù\n'+pic(c,r'(n) {$\mathrm{u}:'),'',pic(r,r'(n) {$\mathrm{f}=')+'\noù\n'+pic(r,r'(n) {$\mathrm{u}:'),'The first enclosure includes the comma after u-star; the second contains the complete u:F→E map. Both have short outward bottom tails. H’s synopsis gives the equations but does not draw the enclosures.',kind='drawing or diagram',n=16,bbox=[906,1741,1397,1826])
add('Curved left enclosure/underline at est un',pic(c,'(n) {est un}'),'',pic(r,'(n) {est un}'),'A curved upper branch meets the left end of the lower stroke under est un. The saved path preserves that curve and the words in the baseline node; C’s upper branch was straight.',kind='drawing or diagram',n=16,c_changed=True,bbox=[1368,1729,1507,1804])
add('Repeated opening quotation pair before application continue',r"````application continue''",'',r"````application continue''",'The crop has four opening vertical strokes, the first pair lighter than the second, and two closing strokes. C’s doubled opening pair is retained; H does not transcribe this phrase.',n=17)
add('Final typed sentence',span(c,'Lorsque $\\mathrm{f}$ commute',r'gauche,\deleted{$\mathrm{g}$}'),'',span(r,'Lorsque $\\mathrm{f}$ commute',r'gauche,\deleted{$\mathrm{g}$}'),'The bottom typescript reads the assertion about commuting with arbitrary projective limits and admitting a left adjoint, then ends after a cancelled g. H omits this sentence; no continuation is supplied.',bbox=[289,1895,1657,2017])
add('Cancelled g at end of final typed line',r'\deleted{$\mathrm{g}$}','',r'\deleted{$\mathrm{g}$}','The lower closed descender and upper body identify typed g beneath cancellation. C retains it; H supplies no direct transcription of the final line.',n=18,bbox=[1574,1980,1607,2017])
add('Separate terminal cancellation x following g','', '',r'\deleted{$\mathrm{g}$}'+pic(r[r.index('gauche,\\deleted{$\\mathrm{g}$}'):],'(x) {\\texttt{x}}'),'The cell after g contains a separate full typewriter x. It extends the cancellation into the following cell and is not another live mathematical variable. C drops this separate impression; H omits the final line.',kind='drawing or diagram',n=18,c_changed=True,bbox=[1605,1983,1631,2017])
CD=[]
def doubt(place,C,decision,evidence,n,bbox=None,confidence='medium'):
 assert C in c
 CD.append(dict(place=place,C=C,decision=decision,evidence=evidence,confidence=confidence,crop=crop(n),bbox=bbox or crops[n]['box'],bbox_source='whole image: '+source))
doubt('Deleted top-note word after fonctorielles',r'\deleted{\illegible{1}}',r'\deleted{\illegible{1}} retained','The heavy crossing run leaves disconnected contours but no secure sequence; trials expresses/explicites cannot be promoted to a word.',1,confidence='low')
doubt('End of s’exprime in top note',r"s'exprime\deleted{nt}\unsure{r}",r"s'exprime\deleted{nt}\unsure{r} retained",'The terminal retouch is consistent with cancellation of nt and a replacement r, but does not make r certain. The syntactic effect of peuvent was not used to resolve it.',2,confidence='low')
doubt('After inductives, before Quant au',r')\handwritten{)}.','Typed close retained; pen trace drawn with unsure rather than assigned a second parenthesis','The thin curve lies beside a heavy bracket and may belong to the insertion boundary.',4,confidence='medium')
doubt('After second épimorphisme',r'\handwritten{\unsure{;|,}}',r'\handwritten{\unsure{;|,}} retained','The distinct upper trace and looping lower form support semicolon, with comma still possible under retouching.',9,confidence='low')
doubt('Cancelled words after c’est d’ailleurs',r'\deleted{\unsure{comme} nous le verrons au}',r'\deleted{\unsure{comme} nous le verrons au} retained','Nous le verrons au is read cell by cell; comme has merged central contours and stays unsure. An additional preceding cancellation x is separately retained.',10,confidence='medium')
doubt('Footer before module libre',r'\deleted{\unsure{le|de}}',r'\deleted{\unsure{le|de}} retained','The surviving loop/short upright does not distinguish the two candidates.',20,[1100,2074,1143,2114],confidence='low')
doubt('Opening fragment','sent','sent retained without supplied prefix','The beginning of the visible typescript is s-e-n-t. No letters from another sheet were consulted or supplied.',None,[271,142,353,175],confidence='high')
doubt('Raised replacement above 3.1.3',r"est \inserted{\handwritten{en}} présenced'",r"est \inserted{\handwritten{en}} présenced' retained in raised drawing",'Présenced’ has no machine space before d’; en is small pen writing above the gap after est. The leader reaches the following paragraph’s un.',12,confidence='high')
doubt('Epimorphism sentence lacks articles','ne transforme pas en général épimorphisme en épimorphisme','No articles supplied','The typed sequence has en général immediately followed by épimorphisme and then en épimorphisme.',None,[488,773,1674,885],confidence='high')
doubt('f/c overprint in contre',r'\deleted{f}contre','Both f and c drawn as overlapping forms, with order doubtful','The f ascender and c bowl survive; neither an x cancellation nor a securely ordered correction is visible.',8,[629,631,663,666],confidence='medium')
doubt('Cancelled e in n[e]’est',r"n\deleted{e}'est",r"n\deleted{e}'est retained",'The e is present below an x impression; the following apostrophe is separate and live.',8,[1076,633,1160,668],confidence='high')
doubt('Mixed t/é impressions in propriétés',r'propri\deleted{t}é\deleted{é}tés','Both mixed cells drawn as overlays, without assigning their order','Round e forms, accents and t stems all survive; chronological deletion/live assignments remain uncertain.',13,[1468,1193,1527,1239],confidence='medium')
doubt('Two opening quotation pairs',r"````application continue''",r"````application continue'' retained",'Four separate opening strokes are visible, then two closing strokes.',17,confidence='high')
doubt('Final cancelled g',r'\deleted{$\mathrm{g}$}',r'\deleted{$\mathrm{g}$} retained, followed by drawn cancellation x','The g descender is definite; another x occupies the following cell. No continuation is supplied.',18,confidence='high')
I=[]
def inv(element,kind,bbox,words,hand='typescript with pen additions'):
 I.append(dict(sheet_kind='typescript',hand=hand,element=element,kind=kind,position={'bbox':bbox,'bbox_source':'whole image'},first_words_or_objects=words,transcribed='yes'))
inv('Manuscript number and arch','text',[1604,80,1668,132],'23','handwritten')
inv('Opening continuation','text',[270,142,1667,315],'sent en termes de limites projectives','typewritten')
inv('Top marginal continuation','margin note',[269,16,1669,140],'les opérations fonctorielles','handwritten')
inv('Top-note open enclosure and low-loop call','drawing',[240,16,1670,149],'left/bottom enclosure with stepped bottom; stem ending in low loop','handwritten')
inv('Top-note deleted word','deletion',[621,23,717,50],'unreadable word after fonctorielles','handwritten')
inv('Peuvent with insertion curve','insertion',[638,44,780,88],'peuvent','handwritten')
inv('Retouched nt/r ending','deletion',[813,57,867,86],"s'exprime[nt]r",'handwritten')
inv('De plus insertion','insertion',[1060,232,1671,284],'De plus, le foncteur u-star','handwritten')
inv('De plus underline, boundary curve and low-loop call','drawing',[1057,232,1671,295],'underline under commute; long lower line; low-loop call','handwritten')
inv('Extra close-shaped pen trace','drawing',[1061,266,1085,327],'close-shaped curve beside typed close','handwritten')
inv('Slanted margin instruction','margin note',[20,254,282,439],'à la ligne / après : Quant au...','handwritten')
inv('Slanted instruction enclosure','drawing',[20,254,284,439],'open-left slanted enclosure','handwritten')
inv('Opposing paragraph brackets','drawing',[1067,265,1282,339],'opposing brackets before/around Quant au','handwritten')
inv('Direct-image typed paragraph','text',[274,278,1674,1097],'Quant au foncteur image directe','typewritten with pen symbols')
inv('Raised direct-image map','insertion',[473,315,633,357],': E → E-prime','typewritten E/colon/prime; pen arrow')
inv('Direct-image map leader','drawing',[467,327,660,398],'curve descending before baseline comma','handwritten')
inv('Par suite addition','insertion',[1427,313,1622,350],'par suite','typewritten')
inv('Par suite leader','drawing',[1493,327,1624,398],'curve before toute','handwritten')
inv('Exclusivement addition','insertion',[1093,451,1360,486],'exclusivement','typewritten')
inv('Exclusivement leader','drawing',[1147,468,1392,541],'curve before (telles','handwritten')
inv('Dans cancellation and raised parmi','deletion',[1210,541,1324,594],'dans / parmi','typewritten')
inv('f/c overprint','text',[629,631,663,666],'f and c in contre','typewritten')
inv('e cancellation','deletion',[1086,633,1124,667],"n[e]'est",'typewritten')
inv('Uncertain punctuation','text',[322,826,354,895],'semicolon/comma after épimorphisme','handwritten')
inv('Separate x before comme and small pen trace','drawing',[672,846,708,884],'cancellation x and short upper-right oblique trace','typewritten x; pen trace')
inv('Cancelled comme nous le verrons au','deletion',[705,840,1185,885],'comme nous le verrons au','typewritten with x/pen cancellation')
inv('Added à in cohomological clause','insertion',[723,906,759,955],'à','handwritten')
inv('Added parenthesis after suivant','insertion',[764,1035,792,1107],')','handwritten')
inv('Second pen insertion','insertion',[810,1024,1660,1095],'Par suite, il ne...','handwritten')
inv('Transforme pas cancellation','deletion',[1127,1050,1394,1089],'transforme pas','handwritten')
inv('S’étend pas replacement','insertion',[1154,1023,1342,1058],"s'étend pas",'handwritten')
inv('Second note’s upper-loop call','drawing',[1640,1030,1659,1097],'upper-loop stem sign','handwritten')
inv('Section number correction','deletion',[279,1125,403,1169],'2 replaced by 3 in 3.1.3','typed 2; pen 3')
inv('Section 3.1.3 full typed paragraph','text',[280,1123,1671,2017],'En pratique, lorsqu’on...','typewritten with pen additions')
inv('Se donne cancellation','deletion',[907,1124,1075,1167],'se donne','typewritten')
inv('Est présenced’ replacement and nested en','insertion',[882,1082,1172,1134],"est / en / présenced'",'typewritten phrase; pen en')
inv('Replacement leader to un','drawing',[1060,1093,1227,1168],'curve descending before un','handwritten')
inv('Inline map f:E→F','text',[1330,1121,1509,1168],'f: E → F','typed Latin letters; pen arrow')
inv('Underlined U','text',[283,1200,313,1238],'U-topos','typewritten with separate underline')
inv('Toutes addition','insertion',[1255,1159,1369,1206],'toutes','handwritten')
inv('Toutes leader','drawing',[1265,1180,1389,1236],'curve before les','handwritten')
inv('First mixed é/t cell','text',[1468,1193,1496,1239],'first é/t overlap in propriétés','typewritten')
inv('Second mixed t/é cell','text',[1494,1193,1527,1239],'second t/é overlap in propriétés','typewritten')
inv('Cancelled exact-adjoint formulation','deletion',[549,1255,1647,1315],"y compris et de déterminer s'il admet un foncteur exact",'typewritten')
inv('Cancelled qui','deletion',[1201,1473,1269,1522],'qui','typewritten')
inv('Cancelled l-apostrophe','deletion',[1182,1550,1229,1587],"l'",'typewritten with cancellation')
inv('Une replacement','insertion',[1144,1510,1220,1549],'une','typewritten')
inv('Une leader','drawing',[1163,1531,1255,1594],'curve before cancelled l-apostrophe','handwritten')
inv('f=u-star enclosure','drawing',[906,1741,1163,1825],'f = u-star,','typed letters; pen star and enclosure')
inv('u:F→E enclosure','drawing',[1182,1741,1397,1826],'u: F → E','typed letters; pen arrow and enclosure')
inv('Est un curved enclosure/underline','drawing',[1368,1729,1507,1804],'est un','typewritten words; pen curve')
inv('Doubled opening quotation pair','text',[447,1904,490,1936],'four opening strokes before application','typewritten')
inv('Final cancelled g','deletion',[1574,1980,1607,2017],'g','typewritten')
inv('Separate following x mark','drawing',[1605,1983,1631,2017],'x cancellation impression','typewritten')
inv('Footer separator','drawing',[22,2003,1667,2038],'long horizontal rule with short left step','handwritten')
inv('Footer upper-loop call','drawing',[75,2035,100,2114],'upper-loop stem sign','handwritten')
inv('Footer continuation','margin note',[111,2035,1640,2127],'en un foncteur sur des objets du type comodule','handwritten')
inv('Footer cancelled le/de','deletion',[1100,2074,1143,2114],'le/de','handwritten')
report=dict(page='C123-02_123_scan040',reader='R1',viewed={'whole':source,'a':source.replace('.jpg','_a.jpg'),'b':source.replace('.jpg','_b.jpg')},reading_file='readers/C123-02_123_scan040/R1/reading.tex',differences=D,c_doubts=CD,inventory=I,
remaining_doubts=[
 {'place':'Top-note cancelled word','reading':r'\deleted{\illegible{1}}','alternatives':['expresses (trial only)','explicites (trial only)','unrecovered word'],'confidence':'low'},
 {'place':'Top-note verb ending','reading':r"s'exprime\deleted{nt}\unsure{r}",'alternatives':['replacement r','retouched nt with replacement not securely separable'],'confidence':'low'},
 {'place':'After inductives','reading':'drawn close-shaped pen trace under unsure','alternatives':['second close parenthesis','part of insertion boundary'],'confidence':'medium'},
 {'place':'Contre f/c cell','reading':'locally unsure literal f/c overlay','alternatives':['c over f','f over c','relative impression order not established'],'confidence':'medium'},
 {'place':'After second épimorphisme','reading':r'\unsure{;|,}','alternatives':['semicolon','comma'],'confidence':'low'},
 {'place':'Small pen trace at preceding cancellation x','reading':'definite typed x and separately unsure drawn oblique stroke','alternatives':['cancellation-related pen stroke','punctuation-related pen stroke'],'confidence':'low'},
 {'place':'Cancelled comme','reading':r'\unsure{comme}','alternatives':['comme','unrecovered central letter sequence'],'confidence':'medium'},
 {'place':'Propriétés two mixed cells','reading':'é/t and t/é literal overlays','alternatives':['C’s proposed deleted/live order','opposite or unrecoverable impression order'],'confidence':'medium'},
 {'place':'Footer after groupe','reading':r'groupe\unsure{,}','alternatives':['comma','terminal flourish with no separate punctuation'],'confidence':'low'},
 {'place':'Footer crossed small word','reading':r'\deleted{\unsure{le|de}}','alternatives':['le','de'],'confidence':'low'}],
notes=[
 'The source is a typescript with handwritten mathematical signs, substitutions, extensive marginal continuations and graphic insertion instructions. Its visible manuscript page number is 23; an inverted archive number 39 appears at upper left and is recorded only as a comment. No date, title or total page count is visible.',
 'The opening sent is a continuation fragment. This reader consulted no other source page and supplied no preceding letters.',
 'The text discusses the direct-image functor preserving structures expressed with projective limits, its general failure of right exactness and epimorphism preservation, and the relation of that failure to cohomological properties. The added top note describes operations expressed with inductive limits and finite projective limits, with free objects and tensor products as examples.',
 'The added lower note says the direct-image functor generally does not extend to the listed coalgebra/comodule/torsor-type constructions or commute with free-module and tensor operations. Its footer begins en un foncteur.',
 'Section 3.1.3, with initial 2 corrected to 3, asks that exactness and existence of adjoints be made explicit in understanding a functor geometrically. It gives the inverse-image notation f=u-star under the stated preservation conditions and begins a further sentence on arbitrary projective limits.',
 'There is no explicit assertion that a proof is unverified. The phrases en général and s’il s’avère que express generality/conditionality, not an authorial declaration of an unproved step.',
 'H’s opening note is an editorial synopsis. Only its marginal transcriptions and quoted insertion wording are compared as literal readings. Synopsis omissions are reported as omissions, not as claims that crossed text is live or that a synopsis alphabet directly transcribes a source occurrence.',
 'All actual source drawings represented in the saved reading use TikZ; insertion leaders have their baseline words or punctuation inside their anchor nodes. Archival numbering is not promoted to manuscript text.'
],
notation=[
 {'place':'Typed maps and functor letters','reading':r'\mathrm{u},\mathrm{f},\mathrm{E},\mathrm{E}\prime,\mathrm{F}','evidence':'Ordinary serifed typewriter contours; no secure paired same-letter impressions. The added map and lower formula crops were inspected separately.'},
 {'place':'U-topos','reading':r'\underline{\mathrm{U}}','evidence':'The half shows a separate low rule beneath the ordinary typed U. H’s mathcal U belongs to its synopsis and is not taken as a literal competing alphabet at this locus.'},
 {'place':'Handwritten arrows and stars','reading':'Right arrows in the three typed maps; lower stars in direct-image u; upper stars in inverse-image u','evidence':'Arrow shafts have right heads. Star placement was read locally rather than inferred from adjunction.'},
 {'place':'Top-note limit signs','reading':r'\varinjlim and \varprojlim','evidence':'The first lim has a rightward arrow underneath, the second a leftward arrow. Their order is preserved.'},
 {'place':'Two call-sign pairs','reading':'Literal TikZ stems with low loop for the top continuation and upper loop for the footer continuation','evidence':'These are graphic matching marks, not letters or mathematical operators.'},
 {'place':'Mixed typewriter impressions','reading':'Literal f/c and é/t overlays with local uncertainty','evidence':'Different surviving letter contours do not establish double-struck notation or a chronological correction order.'},
 {'place':'Quotation marks','reading':'Two-stroke quotation marks; two opening pairs before application continue','evidence':'No source guillemets are present at the quoted handwritten expressions; the repeated opening pair is visible in its crop.'}
],abbreviations=[
 {'form':'p.ex.','expansion':'Editorial expansion: par exemple.'},
 {'form':'cf.','expansion':'Editorial expansion: confer / compare.'},
 {'form':'i.e.','expansion':'Editorial expansion: id est / that is.'},
 {'form':'etc.','expansion':'Editorial expansion: et cetera.'}
],math_checks=[
 {'type':'Targeted type-direction check actually performed','result':'For the lower paragraph, f:E→F and u:F→E make the displayed f=u-star directionally consistent: an inverse-image functor of u has the direction E→F. This check was performed only after reading the arrowheads and did not decide their transcription.'},
 {'type':'Local notation check actually performed','result':'Compared the two arrows under lim and the upper/lower positions of the stars. The source has rightward inductive-limit then leftward projective-limit notation in the top note, and distinct u-star placements in the two discussions.'},
 {'type':'Statement read, not proved','result':'No proof or counterexample calculation was performed for preservation of algebraic structures, lack of right exactness, failure to preserve epimorphisms, or existence of adjoints. These claims are transcribed as source statements.'},
 {'type':'Scope check','result':'The earlier added u-star map uses E→E-prime, while the later independent example uses u:F→E. No identification across these contexts or missing prior-page definition was inferred.'}
],crop_count=len(manifest),workflow_feedback={
 'image_sizes':{'whole':[1684,2141],'a':[1684,1150],'b':[1684,1151]},
 'views':'Whole, a and b each viewed once. Twenty-two distinct crops generated with crop.py and each viewed once; no locus was recropped.',
 'source_constraints':'No OCR, automatic text recognition, web, external research, other-page images, other-reader files or root reading decisions were consulted.',
 'serialization':'The complete reading was saved before assembling this report. A parent text-only audit identified a comment-line serialization defect; that defect and one similar f/c-comment defect were repaired without new ink evidence or image views.',
 'limits':'No TeX compilation was performed. Final checks are text-only brace/environment balance and report-to-drawing coverage, not a visual rendering claim.'
})
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Saved',base/'report.json')
print('Differences:',len(D),'C doubts:',len(CD),'Inventory:',len(I),'Crops:',len(manifest))
