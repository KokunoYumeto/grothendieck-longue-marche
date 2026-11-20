import json
from pathlib import Path
from datetime import datetime, timezone
out=Path('/workspace/scratch/5a09055d9211/SP45_CW_37_work/readers/scan015/r3')
source='/workspace/scratch/5a09055d9211/source/SP45_CW_37_scans/B37-01_37_scan015'
crops=json.loads((out/'unresolved_loci_before_crops.json').read_text())
by={c['path'].rsplit('/',1)[1]:c for c in crops}
def change(locus,c,h,reading,dc,dh,kind,confidence,evidence,crop=None,bbox=None):
    entry={'locus':locus,'c':c,'h':h,'reading':reading,'diff_c':dc,'diff_h':dh,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':evidence,'crop':by[crop]['path'] if crop else '', 'bbox':by[crop]['bbox'] if crop else bbox,'mathematical_consequence':'none; this is textual collation, not a proof check'}
    return entry
changes=[
 change('paragraph 1 line 2: right edge after aidé',r'\unsure{pour}','pour',r'\unsure{pour}',False,True,'other','medium','Crop 01 shows p, o and the partly clipped u; the r lies beyond the surviving right edge. C caution retained; H supplies the complete word without marking the clipping.','01_pour.jpg'),
 change('paragraph 1 line 6: between Les and as-tu',r'Les\deleted{\unsure{r}}as-tu','Les as-tu',r'Les\deleted{\unsure{r}}as-tu',False,True,'omission','low','Crop 02 shows a full x cancellation in one slot with additional middle shoulder/stem ink. An underlying r remains plausible but is not securely resolved; the cancellation itself is certain. H omits it.','02_les.jpg'),
 change('paragraph 1 line 7: envoyer pourlla frappe','pourlla','pour la','pourlla',False,True,'misread word','high','Half a shows two successive l stems after pour, followed directly by a. The first l is lighter, but occupies its own character slot; no space separates pour and lla.',bbox=[652,548,947,594]),
 change('paragraph 1 line 9: right edge after j\'ai',r'\unsure{entièrement}','entièrement',r'\unsure{entièrement}',False,True,'other','medium','Crop 03 shows entièremen, the n partly clipped, while the final t is beyond the surviving edge. The grave accent on è is visible. H presents the full ending without marking the clipping.','03_entierement.jpg'),
 change('paragraph 1 line 11: il after (!),',r'i\deleted{\unsure{n|o}}l','il',r'i\unsure{\deleted{o}l|\deleted{l}o}',True,True,'deletion state (struck given live or live given struck)','medium','Crop 04 shows a tall serifed l stem superposed with a closed rounded o contour. The rounded left and lower contour does not support a separate n shoulder as well as o. The two component glyphs are readable, but their strike order is not visible.','04_il.jpg'),
 change('paragraph 2 line 2: quotation marks surrounding définitive',"``définitive''",'« définitive »',"``définitive''",False,True,'other','high','Half b shows two short upright typewriter strokes at each quotation boundary, not angled guillemets.',bbox=[281,987,522,1033]),
 change('paragraph 2 line 2: word before blâmer',r"\unsure{t\deleted{e}'en|teen}","t'en",r"t\unsure{\deleted{e}'|\deleted{'}e}en",True,True,'deletion state (struck given live or live given struck)','medium','Crop 05 shows a complete first e bowl and crossbar with a separate dark raised apostrophe at the same slot. Thus bare teen omits a real mark. The image does not settle whether the e or apostrophe was typed later; both orders are retained. The following e is heavier but no different underlying character is established.','05_teen.jpg'),
 change('paragraph 2 line 5: after d\'avoir à',r"d'avoir à \deleted{une} y consacrer","d'avoir à y consacrer",r"d'avoir à \deleted{une} y consacrer",False,True,'omission','high','Crop 06 shows three crossed-out slots; beneath the x strokes the u lower curve, n shoulder and e bowl/crossbar remain legible. H omits the cancelled word.','06_une.jpg')
]
def doubt(locus,c,decision,reading,evidence,crop=None):
 return {'locus':locus,'c':c,'decision':decision,'reading':reading,'evidence':evidence,'crop':by[crop]['path'] if crop else ''}
doubts=[
 doubt('paragraph 1 line 2: after aidé',r'\unsure{pour}','retained',r'\unsure{pour}','The surviving pou is followed by the page edge; final r cannot be observed.','01_pour.jpg'),
 doubt('paragraph 1 line 6: cancelled slot after Les',r'\deleted{\unsure{r}}','retained',r'\deleted{\unsure{r}}','x cancellation certain; underlying r-like middle shoulder/stem remains incompletely recoverable.','02_les.jpg'),
 doubt('paragraph 1 line 9: after j\'ai',r'\unsure{entièrement}','retained',r'\unsure{entièrement}','entièremen survives, with part of n clipped and no surviving terminal t.','03_entierement.jpg'),
 doubt('paragraph 1 line 11: il',r'i\deleted{\unsure{n|o}}l','retained',r'i\unsure{\deleted{o}l|\deleted{l}o}','Components refined to o and l from the closed round contour and tall serifed stem; unresolved strike order is explicitly retained.','04_il.jpg'),
 doubt('paragraph 2 line 2: before blâmer',r"\unsure{t\deleted{e}'en|teen}",'retained',r"t\unsure{\deleted{e}'|\deleted{'}e}en",'Presence of both e and apostrophe is resolved; bare teen rejected because it omits the raised mark. Their strike order remains unknown.','05_teen.jpg'),
 doubt('paragraph 1 line 5: assez, de points','assez, de points','resolved','assez, de points','Half a: a comma has a distinct lower tail immediately after assez.'),
 doubt('paragraph 1 line 7: pourlla','pourlla','resolved','pourlla','Half a: two separate l slots; no separating space.'),
 doubt('paragraph 1 line 10: canulé','canulé','resolved','canulé','Half a: c-a-n-u-l-é, including the final acute accent; no lexical correction made.'),
 doubt('paragraph 2 lines 9–10: footnotes améliorations','footnotes améliorations','resolved','footnotes améliorations','Half b: footnotes reaches the line end with no comma; améliorations begins the next line.'),
 doubt('paragraph 2 line 5: after dégueulasse','plûtôt','resolved','plûtôt','Half b: separate circumflexes appear above u and o; both retained.')
]
def inv(element,kind,pos,first,hand='typewriter'):
 return {'sheet_kind':'letter','hand':hand,'element':element,'kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':'yes'}
inventory=[
 inv('015-r3-01','text','top right','Massy le 18.5.1971'),
 inv('015-r3-02','text','upper left below date','Cher Verdier,'),
 inv('015-r3-03','text','body paragraph 1, thirteen source lines','Je ne trouve pas une minute'),
 inv('015-r3-04','deletion','paragraph 1 line 6, after Les','x over an uncertain r'),
 inv('015-r3-05','deletion','paragraph 1 line 11, after (!),','o/l superposition in il; order uncertain'),
 inv('015-r3-06','text','body paragraph 2, thirteen source lines','Si tu en as marre'),
 inv('015-r3-07','deletion','paragraph 2 line 2, before blâmer','e/apostrophe superposition; order uncertain'),
 inv('015-r3-08','deletion','paragraph 2 line 5, after d\'avoir à','une cancelled with x strokes'),
 inv('015-r3-09','text','lower left corner','14, archive sheet number retained as a TeX comment','another unnamed hand')
]
report={
 'scan':15,'reader':'r3','model':'GPT-6 Astra Pro','effort':'inherited; not independently exposed',
 'started_utc':(out/'started_utc.txt').read_text().strip(),
 'ended_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'views':[{'path':source+s+'.jpg','role':role,'viewed_once':True} for s,role in [('', 'whole'),('_a','a'),('_b','b')]],
 'coverage':'The whole image was emitted once for layout, then half a once and half b once. Read the date, salutation, every word/character/accent/punctuation in both thirteen-line body paragraphs, the four overtyped correction loci, ordinary typed capitals and references, both right-edge clippings, all margins, and the pencilled archive 14. Six unresolved loci received one unique crop each, each emitted once. No source area is unviewed. There is no closing or signature on this sheet, and no display, diagram, drawing or marginal insertion. Pale mirrored top traces appear to be reverse-side show-through, not an addition to this letter.',
 'changes':changes,'c_doubts':doubts,
 'unresolved':[
  {'locus':'paragraph 1 line 2, clipped word after aidé','reading':r'\unsure{pour}','alternatives':['pour, with terminal r unavailable'],'confidence':'medium','reason':'Right edge cuts the word after visible pou; final letter cannot be independently verified.'},
  {'locus':'paragraph 1 line 6, cancelled slot after Les','reading':r'\deleted{\unsure{r}}','alternatives':['r'],'confidence':'low','reason':'The x cancellation obscures the underlying shoulder and stem; r remains tentative.'},
  {'locus':'paragraph 1 line 9, clipped word after j\'ai','reading':r'\unsure{entièrement}','alternatives':['entièrement, with terminal t unavailable'],'confidence':'medium','reason':'Right edge removes terminal t and part of the preceding n.'},
  {'locus':'paragraph 1 line 11, il','reading':r'i\unsure{\deleted{o}l|\deleted{l}o}','alternatives':[r'i\deleted{o}l',r'i\deleted{l}o'],'confidence':'medium','reason':'o and l components visible; chronology cannot be read from their superposition.'},
  {'locus':'paragraph 2 line 2, before blâmer','reading':r"t\unsure{\deleted{e}'|\deleted{'}e}en",'alternatives':[r"t\deleted{e}'en",r"t\deleted{'}een"],'confidence':'medium','reason':'First e and raised apostrophe are both visible; strike order remains uncertain.'}
 ],
 'inventory':inventory,
 'notes':[
  {'id':'s015-note01','text':'Dated Massy le 18.5.1971, addressed Cher Verdier. The writer discusses the reissue of SGA 4, Saavedra\'s index for Chap IV, par.9 à 13, and the two Deligne appendices described as assez, de points and image inverse d\'un plat; he asks whether Verdier can send them for typing.','basis':'Observed date, salutation and paragraph 1 lines 1–7; no external identification or reconstruction.'},
  {'id':'s015-note02','text':'The writer asks for a corrected version of exercice 4.10.6 (médaille chocolat), says he has forgotten what was canulé, and seeks something true to replace the false. No mathematical assertion or repair is supplied or verified on this page.','basis':'Observed paragraph 1 lines 8–13; transcription alone, with no proof check.'},
  {'id':'s015-note03','text':'The second paragraph requests instructions on finishing SGA 4, states a preference for leaving it incomplet et dégueulasse over spending time away from boulot survie, and asks Artin what to do with the exposés after VI and the packet of errata/footnotes/améliorations notes.','basis':'Observed paragraph 2; no inference about the notes on other sheets.'},
  {'id':'s015-note04','text':'Visible irregularities are retained: comma in assez, de points; pourlla; canulé; two circumflexes in plûtôt; no separator between footnotes and améliorations. The dashes in paragraph 2 are single plain source strokes: H\'s -- is treated as a typographical encoding of the same dash, and H\'s \\ldots as the same three dots; neither is counted as a substantive collation difference. H\'s guillemets do differ from the observed double quotation marks.','basis':'Direct reading of halves a and b; collation equivalence decision.'},
  {'id':'s015-note05','text':'Archive pencil 14 is entered only as a comment. Faint mirrored top traces are recorded as apparent show-through, with no text imported from a different page. All four correction sites are represented; no mathematical checking occurred and check_events is empty.','basis':'Observed whole and halves; classification of mirrored traces as show-through is an inference from their reversed orientation and faintness.'}
 ],
 'notation':[
  {'sign':'ordinary typewriter capitals and Roman references','latex':'Massy; Cher Verdier; SGA 4; Chap IV; VI','locus':'date, salutation and both paragraphs','evidence':'Each capital was checked independently in the halves. Ordinary typed stems/serifs; no distinct mathematical alphabet, boldface, underline, or separate overtyped earlier character was established.','alternatives':'none'},
  {'sign':'double quotation marks','latex':"``définitive''",'locus':'paragraph 2 line 2','evidence':'Two short typewriter strokes at each boundary in half b.','alternatives':'none'},
  {'sign':'superposed o/l','latex':r'i\unsure{\deleted{o}l|\deleted{l}o}','locus':'paragraph 1 line 11','evidence':'Crop 04: closed rounded contour plus tall serifed l; order not visible.','alternatives':r'i\deleted{o}l; i\deleted{l}o'},
  {'sign':'superposed e/apostrophe','latex':r"t\unsure{\deleted{e}'|\deleted{'}e}en",'locus':'paragraph 2 line 2','evidence':'Crop 05: complete e bowl/crossbar plus distinct raised apostrophe; order not visible.','alternatives':r"t\deleted{e}'en; t\deleted{'}een"}
 ],
 'abbreviations':[{'form':'Chap','expansion':'chapitre (tentative; report only)'},{'form':'par.','expansion':'paragraphes (tentative; report only)'}],
 'check_events':[], 'crops':crops,'brief_feedback':'none'
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'scan':15,'reader':'r3','changes':len(changes),'diff_c':sum(c['diff_c'] for c in changes),'diff_h':sum(c['diff_h'] for c in changes),'c_doubts':len(doubts),'unresolved':len(report['unresolved']),'inventory':len(inventory),'crops':len(crops),'ended_utc':report['ended_utc']},ensure_ascii=False))
