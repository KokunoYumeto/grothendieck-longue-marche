from pathlib import Path
import csv,json

base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out=base/'edition/reader_reports'
crops={x['name']:x for x in json.loads((out/'145_scan008_crop_manifest.json').read_text())}
changes=[]
def change(n,place,C,H,final,ink,confidence,kind,cc,hc,marked,crop,errors,consequence=''):
    changes.append({'id':f's008-{n:02d}','place':place,'C':C,'H':H,'final':final,'ink':ink,'confidence':confidence,'kind':kind,'c_changed':cc,'h_changed':hc,'marked_in_H':marked,'crop':crops[crop]['crop'],'box':crops[crop]['box'],'error_category':errors,'math_consequence':consequence})

change(1,'opening line, word before remplace',r'\deleted{multiplie}',r'\textbf{multiplie}',r'\deleted{multiplie}',
 'A continuous horizontal cancellation crosses multiplie. The tall l and t, dotted i, descending p and final l/i/e remain visible. It is a cancelled word, not bold live text.', 'high','deletion state',False,True,'no','opening_words',[7])
change(2,'opening line, object of remplace',r'\unsure{$g$|$u$}',r'$u$',r'$g$',
 'The letter has a small upper loop and a long descending loop/tail below the baseline. The u at the end of int(λ)u in the same crop has no such descender. The ink supports g, even though the surrounding operation suggests u.', 'high','misread symbol or index',False,True,'no','opening_words',[1],'Preserves a probable authorial g/u slip instead of silently changing the object of remplace.')
change(3,'first display, argument of rho',r'\lambda g\rho(\unsure{l_0|\lambda})^{-1}',r'\lambda\, g\, \rho(\lambda)^{-1}',r'\lambda g\rho(l_0)^{-1}',
 'Inside ρ(·), a tall looped l is followed by a separate small round 0 below the baseline. The initial λ of the same display has a forked shape and no separate subscript. The argument is l₀.', 'high','misread symbol or index',False,True,'no','conjugating_factor',[1],'The visible l₀ is retained although the displayed expanded right side suggests that λ may have been intended.')
change(4,'first display, emphasis on expanded right side',r'\uline{l_0^\alpha gl_1^{-\alpha}}',r'\mathbf{l_0^{\alpha}\, g\, l_1^{-\alpha}}',r'\uline{l_0^\alpha gl_1^{-\alpha}}',
 'One continuous underline runs below the whole right-hand expression. It is separate from the letter strokes; C preserves that source marking.', 'high','other',False,True,'no','conjugating_factor',[10])
change(5,'after Ceci posé, immediately before live les relations',r'\deleted{\unsure{les}}',r'',r'\deleted{\unsure{les}}',
 'A dense cancelled word occupies the position before the clear live les. Its initial tall loop resembles l and its lower remnant could be es, but the loops and cancellation obscure every-letter recovery. Keep C’s struck-text uncertainty.', 'low','omission',False,True,'no','deleted_les',[3,7])
change(6,'third row of the system, label beneath u(l-one)',r'\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}',r'\underbrace{u(l_1)}',r'\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}',
 'The brace below u(l₁) has the label int(g)l₁^p directly beneath it. The letters int, both parentheses around g, the subscript 1 and exponent p are recoverable. H records the label in an editorial note rather than in its formula.', 'high','insertion or placement',False,True,'no','system_third_line',[3,6])
change(7,'far-right cancelled result in third system row',r'\deleted{\unsure{\operatorname{int}g\rho(g)l_\infty^p}}',r'\struck{\mathrm{int}(g\rho(g))\ill{}}',r'\deleted{\unsure{\operatorname{int}(g\rho(g))l_\infty^p|\operatorname{int}g\rho(g)l_\infty^p}}',
 'The cancellation crosses int and the gρ(g) portion. A possible opening parenthesis after int and an extra closing curve are visible, but the precise original parentheses remain doubtful. The final l∞ reaches the paper edge, and its p is not separately secure. Preserve the full uncertainty, including both parenthesis readings.', 'low','misread symbol or index',True,True,'yes','system_third_line',[1,7])
change(8,'live replacement above far-right end of third system row',r'\inserted{\operatorname{int}(g\rho(g))l_\infty^p}',r'\marginal{$\mathrm{int}\, g\rho(g))\, l_\infty^{p}$}',r'\inserted{\operatorname{int}g\rho(g))l_\infty^p}',
 'The live text above the cancellation reads int, then gρ(g)), then l∞^p. There is no separate opening parenthesis between int and g. A curved insertion leader attaches this expression to the cancelled end of the row; it is not an independent marginal assertion. Root separately confirmed the absent opening parenthesis.', 'high','insertion or placement',True,True,'yes','system_third_line',[3,6,9],'Preserves the author’s unmatched parenthesis in the replacement expression.')
change(9,'oblique left marginal NB note',r'\uline{NB} On voit que $u$ automatiquement respecte la structure à lacets, avec le multiplicateur $p$',r'NB On sait que \ill{} \uncertain{automorphismes} \ill{} respectant la \uncertain{structure} \ill{} à lacets \ill{} multiplicateur $p$',r'\uline{NB} On voit que \unsure{$u$|$g$} automatiquement respecte la structure à lacets, avec le multiplicateur $p$',
 'Voit has the initial low v/o turns and a clear final t; it is not sait. Automatiquement is one long word with the auto-, -mat-, -ique- and -ment strokes. Respecte ends with t and e, without the -ant of H. Structure, à lacets, avec le and multiplicateur p are legible. The subject has an upper u-like curve but also a lower descender, so u/g remains locally uncertain. NB is underlined.', 'medium','misread word',False,True,'yes','margin_nb',[2,3,5])
change(10,'last live display, first int expression',r'\operatorname{int}(g^{-1})l_0^p',r'\mathrm{int}(g^{-1})\, l_0^{p}',r'\operatorname{int}g^{-1})l_0^p',
 'The strokes of int run directly into g, followed by the inverse exponent and one closing parenthesis. No separate opening curve occurs before g. The initial parentheses supplied by both witnesses are not visible.', 'high','text not on the page',True,True,'no','last_two_displays',[9],'The unmatched closing parenthesis is preserved literally.')
change(11,'last live display, int-rho expression before target l-infinity',r'\operatorname{int}(\rho(g))(l_\infty^p)',r'\mathrm{int}(\rho(g))(l_\infty^{p})',r'\operatorname{int}(\rho(g)(l_\infty^p)',
 'After g, the crop shows only one closing curve before the opening curve of (l∞^p). The balanced nested expression in both witnesses would require two closing curves there. The crossed display above has more clearly separated closing curves and provides a local contrast. Root also saw the single closing curve in the live display.', 'high','text not on the page',True,True,'no','last_two_displays',[9],'No balancing parenthesis is silently supplied.')
change(12,'closing prose, mark immediately after the first (*) reference',r'$(*)\unsure{,}$',r'$(*)$',r'$(*)\unsure{2|,}$',
 'A small dark character follows the closing parenthesis. It has an upper turn, a descending diagonal and a lower rightward foot, resembling 2 more than an ordinary comma. Its function and exact reading remain unresolved; it is not silently omitted or made into a subscript.', 'low','misread symbol or index',True,True,'no','final_references',[1,3])
change(13,'closing parenthetical prose, reference after pour',r'pour $**$,',r'pour $(**)$,',r'pour $**$,',
 'The opening parenthesis belongs before pour. After pour there are two bare asterisks and then a comma; there is no surrounding pair of parentheses around the asterisks themselves.', 'high','text not on the page',False,True,'no','pour_double_star',[9])
change(14,'closing prose, abbreviation after il suffit',r'$\unsure{=|\bar m}$',r'\struck{\ill{}}',r'$\bar m$',
 'The sign consists of a separate upper bar and a lower shallow double-curved m. Neither stroke crosses the other, so the form is live rather than deleted. It matches the established barred-m abbreviation for même.', 'high','abbreviation expanded or spelling modernised',True,True,'yes','suffit_barred_m',[5,7,8])
change(15,'closing prose, phrase after la valeur',r'\unsure{aux|des} deux mb en',r'aux deux arguments',r'aux deux mb en',
 'Aux has a low initial a/u sequence and a final short x-like turn, with no tall d. After deux are a low m and a taller b, followed by the separate low joined en. The ink says mb en, not the longer word arguments.', 'high','misread word',False,True,'no','valeur_aux_deux_mb',[2,8])

decisions=[]
def decision(id,choice,reading,ink,crop,confidence):
    decisions.append({'id':id,'decision':choice,'reading':reading,'ink':ink,'crop':crops[crop]['crop'],'box':crops[crop]['box'],'confidence':confidence})
decision('M0782','first',r'$g$','A looped upper body and long lower descender distinguish this g from the plain u at the end of int(λ)u in the same crop.','opening_words','high')
decision('M0783','first',r'l_0','The argument has a tall looped l plus a separate small subscript 0. Initial λ on the same line is forked and lacks that subscript.','conjugating_factor','high')
decision('M0784','undecided',r'\unsure{2|,}','A 2-like upper turn, diagonal and foot are visible after (*), but the small glyph could be an unusually formed or overwritten comma. Its reading is left open.','final_references','low')
decision('M0785','alternative',r'\bar m','The upper bar is detached from a lower double-curved m. It is live ink and agrees with the established abbreviation même.','suffit_barred_m','high')
decision('M0786','first','aux','Low a/u turns and a short final x-like turn are visible; there is no tall d that would support des.','valeur_aux_deux_mb','high')

doubts=[
 {'place':'word cancelled before live les relations','reading':r'\deleted{\unsure{les}}','alternatives':['les','another cancelled short word'],'confidence':'low','reason':'The initial loop could be l, but overlapping cancellation hides the complete es strokes.'},
 {'place':'third system row, label below the rho-conjugation product','reading':r'\unsure{\operatorname{int}(\rho(g))}','alternatives':[r'\operatorname{int}(\rho(g))',r'\operatorname{int}(\rho(g)'],'confidence':'low','reason':'The small closing curves in the underbrace label are crowded; there may be only one closing parenthesis after g.'},
 {'place':'cancelled end of third system row','reading':r'\deleted{\unsure{\operatorname{int}(g\rho(g))l_\infty^p|\operatorname{int}g\rho(g)l_\infty^p}}','alternatives':[r'\operatorname{int}(g\rho(g))l_\infty^p',r'\operatorname{int}g\rho(g)l_\infty^p'],'confidence':'low','reason':'Cancellation and clipping at the physical right edge prevent certain recovery of parentheses and final exponent.'},
 {'place':'oblique NB note, subject after que','reading':r'\unsure{$u$|$g$}','alternatives':['u','g','a corrected g/u overlap'],'confidence':'low','reason':'The upper letter is u-like, but a separate lower loop/descender remains. No unambiguous cancellation can be assigned to it.'},
 {'place':'closing prose, sign immediately after (*)','reading':r'\unsure{2|,}','alternatives':['2',','],'confidence':'low','reason':'The visible shape is 2-like; neither its reading nor a subscript function is secure.'}
]

inventory=[]
def inv(element,kind,position,words,box):
    inventory.append({'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'box':box,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('T01','text','top opening paragraph, three lines including a display placed in the third line','choisi — si on ... remplace g ... alors g est remplacé par',[232,43,1615,341])
inv('D01','deletion','first line, immediately before remplace','multiplie',[666,62,931,130])
inv('F01','display','third opening line, right of remplacé par','λgρ(l₀)^{-1} = l₀^α g l₁^{-α}.',[717,245,1301,398])
inv('T02','text','right end of opening third line and following two lines','Ceci posé, ... les relations (*) et (**) ... par',[211,274,1647,621])
inv('D02','deletion','before live les relations',r'\deleted{\unsure{les}}',[210,415,286,485])
inv('F02a','display','first row under the large left brace','u(l₀) = l₀^p',[449,627,754,701])
inv('F02b','display','second row under brace and its underbrace label','u(l₁) = uρ(l₀) ... = int(g)l₁^p; l₀^p',[474,700,1271,807])
inv('F02c','display','third row under brace, with three lower brace labels','u(l∞) = uρ(l₁) ...',[479,723,1681,970])
inv('D03','deletion','far right of third system row','int(gρ(g))l∞^p, exact parentheses uncertain',[1502,835,1681,921])
inv('I01','insertion','above cancelled right end of third row, joined by curved leader',r'\operatorname{int}g\rho(g))l_\infty^p',[1405,733,1669,841])
inv('MN01','margin note','left, oblique, five lines','NB On voit que ... automatiquement respecte ...',[21,640,444,1048])
inv('T03','text','two lines below the system','Il faut vérifier ... la relation l₀′l₁′l∞′ = 1 i.e.',[208,991,1647,1164])
inv('F03','display','boxed endomorphism condition','l₀^p · int(g)l₁^p · int(gρ(g))l∞^p = 1',[454,1145,1145,1240])
inv('T04','text','to right of the boxed condition','ou encore',[1271,1166,1534,1217])
inv('F04','display','expanded product below the boxed condition','l₀^p(gl₁^pg^{-1})(gρ(g)l∞^pρ(g)^{-1}g^{-1}) = 1',[477,1239,1394,1360])
inv('T05','text','left before next product display','i.e.',[200,1380,287,1446])
inv('F05','display','product with adjacent g factors cancelled','l₀^pgl₁^pρ(g)l∞^pρ(g)^{-1}g^{-1} = 1',[511,1461,1259,1590])
inv('T06','text','line before the last pair of displays','soit encore, en faisant passer le g^{-1} à gauche',[208,1593,1550,1676])
inv('D04','deletion','entire penultimate display, single horizontal strike','l₀^p · int(g)(l₁^p · int(ρ(g))(l∞^p)) = 1',[434,1689,1390,1811])
inv('F06','display','last live display, below the struck one','int g^{-1})l₀^p · l₁^p · int(ρ(g)(l∞^p) = 1',[502,1801,1390,1907])
inv('T07','text','closing paragraph, three lines','Les relations (*) ... et (**) sont vérifiées ...',[204,1904,1660,2228])
inv('P01','text','lower-left manuscript number','7',[33,2265,88,2323])

second_boxes=[]
def sb(n,kind,coords,reading): second_boxes.append({'box':f'B{n:02d}','kind':kind,'coords':coords,'reading':reading})
sb(1,'opening cancellation and resolved C mark; all numeric inline parameters',[232,43,1615,236],r'choisi --- si on \deleted{multiplie} remplace $g$ par $\operatorname{int}(\lambda)u$ avec $\lambda=l_0^\alpha\in L_0$ ($\alpha\in\hat{\mathbb Z}^{*}$), alors $g$ est')
sb(2,'complete formula containing resolved C mark and numerical indices',[717,245,1301,398],r'\lambda g\rho(l_0)^{-1}=\uline{l_0^\alpha gl_1^{-\alpha}}.')
sb(3,'cancelled doubtful word before live les relations',[204,410,618,504],r'\deleted{\unsure{les}} les relations')
sb(4,'parameter paragraph and relation references',[298,419,1647,621],r'les relations $(*)$ et $(**)$ déterminent $u$ en termes de $p\in\hat{\mathbb Z}^{*}$ et de $g\in\pi$, par')
sb(5,'complete first two system rows, including all numerical indices and underbrace label',[448,627,1271,807],r'\begin{aligned}u(l_0)&=l_0^p\\u(l_1)&=u\rho(l_0)=\operatorname{int}(g)\rho\underbrace{u(l_0)}_{l_0^p}=\operatorname{int}(g)l_1^p\end{aligned}')
sb(6,'complete third system row, correction, cancellation, labels and proposed doubt',[479,723,1681,970],r'u(l_\infty)=u\rho(l_1)=\operatorname{int}(g)\rho\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}=\operatorname{int}(g)\underbrace{\rho\operatorname{int}(g)\rho^{-1}}_{\unsure{\operatorname{int}(\rho(g))}}\underbrace{(\rho l_1^p)}_{l_\infty^p}=\deleted{\unsure{\operatorname{int}(g\rho(g))l_\infty^p|\operatorname{int}g\rho(g)l_\infty^p}}\inserted{\operatorname{int}g\rho(g))l_\infty^p}')
sb(7,'entire marginal note; all lexical disagreements and proposed subject doubt',[21,640,444,1048],r'\uline{NB} On voit que \unsure{$u$|$g$} automatiquement respecte la structure à lacets, avec le multiplicateur $p$')
sb(8,'complete prose condition with all primed numerical generator indices',[208,991,1647,1164],r'Il faut vérifier, pour qu\textquotesingle on ait bien un endom. de $\pi$, la relation $l_0\prime l_1\prime l_\infty\prime=1$ i.e.')
sb(9,'complete boxed display with numerical indices and terminal 1',[454,1145,1145,1240],r'\boxed{l_0^p\cdot\operatorname{int}(g)l_1^p\cdot\operatorname{int}(g\rho(g))l_\infty^p=1}')
sb(10,'complete expanded-product display',[477,1239,1394,1360],r'l_0^p(gl_1^pg^{-1})(g\rho(g)l_\infty^p\rho(g)^{-1}g^{-1})=1')
sb(11,'complete simplified-product display',[511,1461,1259,1590],r'l_0^pgl_1^p\rho(g)l_\infty^p\rho(g)^{-1}g^{-1}=1')
sb(12,'prose with numeric inverse exponent',[208,1593,1550,1676],r'soit encore, en faisant passer le $g^{-1}$ à gauche')
sb(13,'complete struck display and complete live replacement, preserving literal parentheses',[434,1689,1390,1907],r'\deleted{l_0^p\cdot\operatorname{int}(g)\bigl(l_1^p\cdot\operatorname{int}(\rho(g))(l_\infty^p)\bigr)=1}\qquad\operatorname{int}g^{-1})l_0^p\cdot l_1^p\cdot\operatorname{int}(\rho(g)(l_\infty^p)=1')
sb(14,'complete first closing line and doubtful character after (*)',[214,1904,1494,2009],r'Les relations $(*)\unsure{2|,}$ et $(**)$ sont vérifiées par')
sb(15,'complete second closing line, bare double-star reference and barred m',[204,1999,1660,2111],r'construction (pour $**$, il suffit $\bar m$ de la vérifier')
sb(16,'complete last closing line, lexical disagreement and numeric generator indices',[206,2104,1470,2228],r'pour la valeur aux deux mb en $l_0,l_1$).')
sb(17,'handwritten manuscript page number',[33,2265,88,2323],r'\mspage{7}')

substantive={3:2,6:3,8:5,15:6,21:7,22:8,23:8,25:8,26:9,27:9,28:9,53:12,54:13,55:13,56:14,58:15}
special={
 1:'Editorial scan marker; not a source word.',
 2:'Dash encoding differs (TeX em dash versus a typographic dash); the visible single dash is preserved.',
 15:'H moves the brace label to an editorial note; s008-06 retains its actual mathematical placement.',
 21:'The cancelled original result has uncertain parentheses, logged as s008-07.',
 22:'This alignment conflates the struck result and the live insertion; s008-07 covers the cancellation and s008-08 the replacement and its placement.',
 23:'The live insertion is s008-08. H’s ensuing explanatory note is editorial; its observation about the missing opening parenthesis is checked against ink.',
 25:'The insertion is read with its actual missing opening parenthesis (s008-08); H’s prose explanation itself is not transcribed.',
 29:'H’s description of the oblique note is editorial.',
 30:'Placement of the prime before or after the subscript is typographic; all three generator primes are present.',
 31:'Prime/subscript grouping and TeX thin spacing; no source comma.',
 32:'Prime/subscript grouping and TeX thin spacing; no source comma.',
 33:'Prime placement before/after the infinity subscript is typographic.',
 57:'Only C’s alternative des is removed after crop resolution M0786; H already reads aux. The distinct mb en/arguments disagreement is s008-15.',
 59:'C’s manuscript page number 7 is preserved as P01/B17. H’s comment on the overwritten second reference is editorial; the overinked reference was independently read.'
}
rows=list(csv.DictReader((base/'packets/145_scan008/differences.tsv').open(),delimiter='\t'))
diff_coverage=[]
for n,row in enumerate(rows,1):
    if n in substantive:
        d={'row':n,'status':'substantive','change_id':f's008-{substantive[n]:02d}'}
        if n in special:d['explanation']=special[n]
    else:d={'row':n,'status':'macro/editorial','explanation':special.get(n,'TeX spacing, display environment, or token boundary only; no distinct source inscription changes.')}
    diff_coverage.append(d)

report={
 'scan':8,'reader':'/root/reader_a','lines_read':29,
 'layout':'Upright handwritten mathematical sheet, manuscript page 7 at lower left. The opening paragraph occupies three lines with a formula embedded in the third. Two further prose lines lead to a three-row brace system with four underbrace labels, a cancelled right-end result, and a curved leader to its replacement above. A five-line oblique note occupies the left margin. The lower body contains a boxed condition, two expanded product displays, a fully struck display and its live replacement, followed by three concluding prose lines. No independent diagram or drawing is present. The line count includes separate annotation/underbrace baselines, the insertion, the margin lines and the page number.',
 'changes':changes,'decisions':decisions,'doubts':doubts,'inventory':inventory,'second_boxes':second_boxes,
 'notation':[
  {'observation':r'$\bar m$ abbreviates même and is live after il suffit.','observed_places':['T07, second line'],'qualification':'Local upper bar and lower double curve agree with the packet’s established notation.'},
  {'observation':'The page uses int for conjugation, with inconsistent written parentheses.','observed_places':['F02c replacement','F06'],'qualification':'The live upper-right correction omits an opening parenthesis; the last live display also omits parentheses supplied by both witnesses. These are retained literally.'},
  {'observation':'The first display reads ρ(l₀)^{-1}; the first λ has a distinct forked shape.','observed_places':['F01'],'qualification':'A local l₀/λ distinction, not a proposed uniform rule beyond the page.'},
  {'observation':'Underbraces annotate generator images and a conjugation identity.','observed_places':['F02b','F02c'],'qualification':'Four label placements are preserved; the tiny closing curves in one label remain doubtful.'},
  {'observation':'The final prose writes bare ** after pour, but parenthesized (*) and (**) earlier.','observed_places':['T07'],'qualification':'No parentheses are supplied around the bare reference.'}
 ],
 'hand':[
  {'habit':'The g has a small upper loop and a long descending tail; u usually lacks that tail.','affected_places':['T01 after remplace','T01 final int(λ)u','F01 g'],'universal_on_page':'Useful local distinction; the marginal subject remains ambiguous because its strokes overlap.','witness_misreadings':'H reads u where the opening letter is g.'},
  {'habit':'The l has a tall narrow loop; a separate small round subscript 0 can be distinguished from the forked λ.','affected_places':['F01 argument of ρ and initial λ'],'universal_on_page':'Observed locally in the first display and checked against the generator forms in the system.','witness_misreadings':'H reads λ for the visible l₀ in ρ(l₀).'},
  {'habit':'Long lower-case cursive words flatten into connected horizontal waves, while tall consonants and descenders remain diagnostic.','affected_places':['MN01 automatiquement, respecte, structure, multiplicateur','T07 aux deux mb en'],'universal_on_page':'Recurring feature of this page, with variation in ink strength.','witness_misreadings':'H gives automorphismes/respectant and arguments, and leaves substantial marginal prose illegible.'},
  {'habit':'Small m under an overbar has a shallow double-curved baseline and may resemble an equals sign.','affected_places':['T07 after il suffit'],'universal_on_page':'One local occurrence.','witness_misreadings':'C offers equality sign; H treats the live abbreviation as struck illegible text.'},
  {'habit':'Parentheses are sometimes omitted in hurried formulas; cramped or reinforced curves must be counted independently of the expected algebra.','affected_places':['F02c insertion','F06','F02c underbrace label'],'universal_on_page':'Not universal; many other formulas have explicit balanced pairs.','witness_misreadings':'Both witnesses regularize the final live display; C supplies an opening parenthesis in the upper-right replacement.'}
 ],
 'abbreviations':[
  {'form':'int','expansion':'automorphisme intérieur / conjugaison','place':'throughout formulas'},
  {'form':'NB','expansion':'nota bene','place':'oblique left marginal note'},
  {'form':'endom.','expansion':'endomorphisme','place':'prose introducing the boxed condition'},
  {'form':'i.e.','expansion':'id est','place':'after the generator relation and before a product display'},
  {'form':r'$\bar m$','expansion':'même','place':'closing paragraph after il suffit'},
  {'form':'mb','expansion':'membres','place':'closing paragraph, aux deux mb en'}
 ],
 'notes':[
  'The page continues an earlier sentence with choisi. In the opening transformation the manuscript reads g after remplace and l₀ as the argument of ρ in λgρ(l₀)^{-1}. The adjacent int(λ)u and expanded expression l₀^αgl₁^{-α} suggest possible authorial slips, but neither symbol is silently changed. The written hypothesis α ∈ Z-hat-star is likewise preserved.',
  'The author states that relations (*) and (**) determine u from p and g. A three-row system computes the images of l₀, l₁ and l∞, annotating intermediate expressions with underbraces. The final result is crossed at the physical right edge and rewritten above it. The replacement lacks an opening parenthesis immediately after int. The precise parentheses and final exponent of the crossed version remain uncertain.',
  'The marginal note says that the map automatically respects the structure à lacets with multiplier p. Its readable prose is retained, but the subject letter after que remains u/g because an upper u-like curve and a lower descender coexist.',
  'The lower calculations state the condition that the three generator images multiply to 1, expand the inner conjugations, simplify the product, and move g^{-1} to the left. One whole intermediate display is struck out. The following live display has unmatched written parentheses; the transcription preserves those strokes instead of balancing them.',
  'The closing paragraph asserts that (*) and (**) hold by construction and that, for **, it is enough to verify the two members at l₀ and l₁. It uses the live abbreviation barred m and the written abbreviation mb. A 2-like mark after the first (*) remains unresolved against C’s suggested comma; no subscript status is asserted.',
  'All four C deletion/insertion states were individually checked: cancelled multiplie; doubtful cancelled les; cancelled system result and its insertion above; and the fully struck penultimate display. The latter is readable across the strike. No date or independent drawing is present. The handwritten manuscript number is 7. Il faut vérifier is the author’s stated verification obligation, not a report of verification by this reader.',
  'The reading used only this page packet, the established notation supplied in it, and root’s messages about this same page. No OCR, external research, or other page was consulted for this assignment. No mathematical proof check or formal computation was completed; the report records the author’s assertions and literal symbols.'
 ],
 'check_events':[],
 'diff_coverage':diff_coverage
}
def normalize_strings(x):
    if isinstance(x,str): return x.replace(chr(92)+'prime',"'").replace(chr(92)+'textquotesingle on',"'on")
    if isinstance(x,list): return [normalize_strings(z) for z in x]
    if isinstance(x,dict): return {k:normalize_strings(v) for k,v in x.items()}
    return x
report=normalize_strings(report)
(out/'145_scan008.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'decisions':len(decisions),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second_boxes),'diff_rows':len(diff_coverage),'crops':len(crops)},indent=2))
