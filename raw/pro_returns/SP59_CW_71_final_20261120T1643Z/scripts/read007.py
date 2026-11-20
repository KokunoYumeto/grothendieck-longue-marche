from read_support import *
t=source(7)
for a,b in [
 (r'\unsure{\varphi|\phi}',r'\varphi'),(r'\unsure{ordonné}','ordonné'),
 (r'\unsure{\Sigma|\mathbb{\Sigma}}',r'\Sigma'),(r'\unsure{\mathcal X|\mathscr X}',r'\mathcal X'),
 (r'\unsure{\partial|\delta}',r'\partial'),
 (r'\unsure{i_{k_{i-1}}|i_{ki-1}|i_{k-1}}',r'\unsure{i_{k_{i-1}}|i_{ki-1}}'),
 (r'\unsure{\mathord{-}|\supset|\longrightarrow}',r'\supset'),
 (r'\partial X_{\unsure{i_k|k}}',r'\partial X_{i_k}'),
 (r'i_{\unsure{\alpha|2}}',r'i_\alpha'),
 (r'\unsure{\pi_0|\Pi_0}',r'\pi_0'),(r'\unsure{D|\mathcal D}',r'D'),
 (r'\deleted{\updownarrow}',r'\deleted{\unsure{\downarrow|\updownarrow}}')]: t=replace(t,a,b)
# The long lower link has no triangular arrowhead; preserve its hooked, unheaded form.
t=replace(t,r'X_{i_{k-1}}\arrow[d,hook]',r'X_{i_{k-1}}\arrow[d,hook,dash]')
changes=[
 ch('Flag line',r'i_0>-->i_k',r'i_0>\cdots>i_k',r'i_0>-->i_k','Top half: two short horizontal dashes between the greater signs; H substitutes an ellipsis.',diff_H=True,kind='other'),
 ch('Main diagram, first upper subscript',r'\unsure{i_{k_{i-1}}|i_{ki-1}|i_{k-1}}',r'i_{k-1}',r'\unsure{i_{k_{i-1}}|i_{ki-1}}','Scan 007 crop (440,855,900,1000): a second dotted i is visibly present after k and before -1; its exact nesting remains uncertain.',diff_H=True,kind='misread symbol or index',error_kind='Symbols and indices',confidence='medium',consequential='An extra dotted i in the first upper index is retained; the neighbouring expected k-1 does not erase it.'),
 ch('Main diagram, upper third object',r'\deleted{\unsure{\partial}}\Delta',r'\Delta',r'\deleted{\unsure{\partial}}\Delta','Scan 007 crop (1300,845,1540,985): a hooked vertical loop survives inside the retraced triangle; probable overwritten boundary sign is retained as doubtful.',diff_H=True,kind='omission',error_kind='Struck text',confidence='low'),
 ch('Main diagram, intermediate object after (X)',r'\deleted{\unsure{i_k}}',r'_{\ill{}}',r'\deleted{\unsure{i_k}}','Scan 007 crop (490,1040,785,1185): dense overwritten strokes after the parenthesis, with a descending stem and k-like turn; they are cancellation ink, not a confidently live subscript.',diff_H=True,kind='deletion state (struck given live or live given struck)',error_kind='Struck text',marked_H='yes',confidence='low'),
 ch('Main diagram, second vertical link','unheaded vertical stroke',r'\downarrow','unheaded vertical stroke','Top and bottom halves: the thin vertical stroke below the boundary-Sigma ends in a blunt stroke at the fold; no arrowhead is visible.',diff_H=True,kind='drawing or diagram',error_kind='Drawings and diagrams'),
 ch('Main diagram, lower middle relation',r'\unsure{-|\supset|\longrightarrow}',r'\longleftarrow',r'\supset','Scan 007 crop (1015,1215,1385,1340): long lower arm turns upward and back left at its right end, like the elongated containment sign to its left; there is no left-pointing arrowhead.',diff_C=True,diff_H=True,kind='misread symbol or index',error_kind='Symbols and indices',confidence='medium',marked_H='yes',consequential='The lower middle link is read as containment, not a leftward map.'),
 ch('Main diagram and following Sigma formula, interval separators','short dashes',r'\dots','short dashes','Both halves: a single horizontal dash separates the terminal indices; H regularises the shorthand to ellipsis in the boundary-Sigma, the two Delta labels, and the following Sigma formula.',diff_H=True,kind='other'),
 ch('Below Sigma formula, before d-prime condition','no prose','pour','no prose','Bottom half: the condition d-prime proper-subset d stands by itself to the left of the arrow; no word pour is written.',diff_H=True,kind='text not on the page',error_kind='Text that is not on the page'),
 ch('Lower central column, first index',r'\unsure{i_{j_k}|j_{i_k}|i_k}',r'i_k',r'\unsure{i_{j_k}|j_{i_k}|i_k}','Scan 007 crop (835,1505,1035,2100): the X stroke joins a hooked lower stroke before the small dotted stem and k; nesting is not secure. H removes this ambiguity.',diff_H=True,kind='misread symbol or index',error_kind='Symbols and indices',confidence='low'),
 ch('Lower central column, second index',r'\unsure{j_k|i_k}',r'i_k',r'\unsure{j_k|i_k}','Scan 007 crop (835,1505,1035,2100): hooked descending stroke touches X; a j-form is the literal first candidate, but an i joined to X remains possible.',diff_H=True,kind='misread symbol or index',error_kind='Symbols and indices',confidence='low'),
 ch('Lower central column, unheaded links','upper plain stroke; lower hooked arrow','two arrows','upper plain stroke; lower hooked unheaded stroke','Bottom half and scan 007 crop (835,1505,1035,2100): upper link is blunt-ended; lower link has a curved top and blunt lower end, without a triangular arrowhead.',diff_C=True,diff_H=True,kind='drawing or diagram',error_kind='Drawings and diagrams',confidence='medium'),
 ch('Lower square, erased continuation of subscript',r'\deleted{\unsure{\cap d\prime}}','editorial note only',r'\deleted{\unsure{\cap d\prime}}','Scan 007 crop (375,1975,705,2290): an intersection-shaped first stroke and final prime survive the scribble; tentative d in between.',diff_H=True,kind='omission',error_kind='Struck text',marked_H='yes',confidence='low'),
 ch('Lower square, struck arrow and Sigma',r'\deleted{\updownarrow};\deleted{\Sigma_{d\prime}}','editorial note only',r'\deleted{\unsure{\downarrow|\updownarrow}};\deleted{\Sigma_{d\prime}}','Scan 007 crop (375,1975,705,2290): long shaft, lower pointed strokes, overwritten loops, and crossed Sigma-d-prime. Upward point is not securely recoverable.',diff_C=True,diff_H=True,kind='drawing or diagram',error_kind='Struck text',marked_H='yes',confidence='low'),
 ch('Between the isolated Sigma and singleton formula','no semicolon','semicolon','no semicolon','Top half: the two expressions occupy separate positions; no semicolon is drawn between them.',diff_H=True,kind='text not on the page',error_kind='Text that is not on the page'),
]
doubts=[
 doubt('Upper map label',r'\varphi',r'\phi','high','C doubt resolved: the repeated small loop and long stem agree.'),
 doubt('After I','ordonné','','high','C doubt resolved from top half.'),
 doubt('First Sigma',r'\Sigma',r'\mathbb{\Sigma}','high','C doubt resolved: retracing, not a distinct double-struck alphabet.'),
 doubt('Script X',r'\mathcal X',r'\mathscr X','high','C doubt resolved to a calligraphic X with curved arms and a middle bar.'),
 doubt('Boundary symbols',r'\partial',r'\delta','high','C doubt resolved: hooked upper stem, lower oval; uniform boundary notation.'),
 doubt('Main diagram first subscript',r'i_{k_{i-1}}',r'i_{ki-1}','low'),
 doubt('Overwritten sign inside Delta',r'\deleted{\partial}','','low'),
 doubt('Overwritten after (X)',r'\deleted{i_k}','','low'),
 doubt('Bottom-right boundary index',r'i_k','k','high','C doubt resolved from bottom half.'),
 doubt('Lower column first index',r'i_{j_k}',r'j_{i_k}; i_k','low'),
 doubt('Lower column second index',r'j_k',r'i_k','low'),
 doubt('Erased continuation',r'\cap d\prime','','low'),
 doubt('Lowest struck arrow',r'\downarrow',r'\updownarrow','low'),
 doubt('Lower right subscript',r'\alpha','2','high','C doubt resolved: loop with crossing exit, scan 007 crop (835,1505,1035,2100).'),
 doubt('Final equality',r'\pi_0(\Sigma_d)=D(d)',r'\Pi_0;\mathcal D','high','C doubts resolved: curved pi top, low oval 0, plain bowed D; crop (1160,1720,1595,1875).'),
]
inventory=[inv('diagram','upper left','e in E; M(e); M(E_e); E_0=M(E); varphi; I ordonné'),inv('display','upper centre','|E|=X; X_i union'),inv('display','upper right','E_e={x in E | x<=e}'),inv('diagram','upper right below separator','e_0 maps to X_e0'),inv('display','upper middle','(i_0>-->i_k)=d in Drap(I); d subset I'),inv('display','middle left','Sigma_d(calligraphic X)'),inv('display','middle right','Sigma_{i}(X)=Sigma(X_i,partial X_i)'),inv('drawing','above singleton boundary','faint three-armed trace'),inv('diagram','middle','four-column Sigma/Delta and X boundary diagram'),inv('deletion','main diagram upper Delta','overwritten partial'),inv('deletion','main diagram intermediate (X)','overwritten i_k'),inv('display','below main diagram','Sigma_{i0,-ik}(calligraphic X)=Sigma(Delta,partial Delta)'),inv('diagram','below formula left','arrow to Sigma_dprime; dprime proper subset d'),inv('diagram','lower left','Sigma_d to Sigma_tilde_dprime to Sigma_dprime'),inv('diagram','lower centre','boundary-X column and two-row square'),inv('deletion','lower square second subscript','cap dprime'),inv('deletion','bottom of square','arrow and Sigma_dprime'),inv('display','lower right','pi_0(Sigma_d)=D(d)'),inv('deletion','across page','long oblique cancellation and crossing lower stroke')]
for i in inventory:i['sheet_kind']='cancelled_draft'
# SP59 mechanical repair: separate partial from X.
t = t.replace(r"\partialX_i", r"\partial X_i")
record_page(7,t,changes,inventory,
'''The sheet assembles a filtration from an ordered set E, its M(E), and a map to an ordered I, then sketches flag-indexed Sigma spaces and boundary/Delta diagrams. It ends with pi_0(Sigma_d)=D(d). No proof or dated heading is present. The long diagonal and shorter counterstroke mark a cancelled working sheet; their geometry is retained in TikZ.

The first upper Sigma subscript contains an extra dotted i, unlike its neighbour: it is retained, with doubt over nesting. The adjacent simpler k-1 suggests an authorial indexing slip but is not substituted. In the lower column the X strokes run into the indices, so j/i remains open. The lower middle horizontal sign resembles the other elongated containment signs; it is not silently converted into a map. These are reading decisions, not a verification of the proposed construction.

No verbal check request or manuscript title/date/page count occurs. Archival corner number: 6.''',doubts=doubts,
 hand=[dict(habit='Elongated containment signs can look like one-sided arrows.',occurrences='007 main diagram bottom row',scope='Three horizontal containment forms; middle one has a particularly short upper arm.',misreadings='H gave a leftward arrow; C left the middle link unresolved.'),dict(habit='The right stroke of X can join a lowered index and make i look like j.',occurrences='007 lower central column',scope='Only the two crowded top indices remain ambiguous; other i_k occurrences are clear.',misreadings='C records nested alternatives; H gives uncomplicated i_k at both places.'),dict(habit='Retraced Sigma and overwritten Delta have extra interior strokes.',occurrences='007 isolated Sigma and main upper Delta',scope='Not evidence of a distinct alphabet; Delta contains a possible overwritten boundary symbol.',misreadings='C offered a blackboard Sigma; H omitted the overwritten sign.')],
 notation=[dict(sign=r'\varphi',form='Small loop above a long descending stem.',remarks='Upper-left map and upper-centre union condition.'),dict(sign=r'\partial',form='Tall hooked stroke with a small lower oval.',remarks='Boundary sign; distinguish from delta.'),dict(sign=r'\mathcal X / X',form='Curved, middle-barred calligraphic X / plain crossed X.',remarks='Calligraphic X is not silently replaced by the space X.'),dict(sign=r'\pi_0',form='Curved top over two stems, low loop 0.',remarks='Connected-component expression at lower right.'),dict(sign='dash separators',form='One or two short horizontal strokes between end indices.',remarks='Do not expand to a printed ellipsis.')],
 abbreviations=[dict(abbreviation='Drap',expansion='drapeaux',remarks='Notation only; no expansion in transcription.')],
 unresolved=['Main diagram: the extra dotted i is certain, but its nested level is not.','Overwritten partial, overwritten i_k, lower-column indices, erased cap d-prime, and struck arrow remain marked in place.'])
