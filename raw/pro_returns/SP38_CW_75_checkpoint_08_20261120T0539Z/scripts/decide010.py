from pathlib import Path
import json, copy, hashlib

root=Path(__file__).resolve().parents[1]
rep={r:json.loads((root/'readings/scan010'/r/'report.json').read_text()) for r in ('R1','R2','R3')}
obs=json.loads((root/'decisions/scan010_main_observations.json').read_text())
ob={x['place']:x for x in obs['observations']}
def get(r,k):
    return next(f for f in rep[r]['findings'] if f['id']==k)
def rp(r,k):return f'readings/scan010/{r}/crops/{k}.png'
def mp(k):return f'crops/scan010/{k}.png'
paths={
 'heading':rp('R1','01_title'), 'central':rp('R3','02_diagram_centre'),
 'tau':rp('R3','03_tau'), 'equiv':rp('R1','04_vertical_connector'),
 'aff':rp('R3','04_aff_cancellation'), 'product':rp('R3','05_product_words'),
 'adjective':rp('R3','06_subgroup_word'), 'old_aut':rp('R1','08_cancelled_aut'),
 'hom':rp('R2','10_hom_heading'), 'pair':rp('R3','10_pair'),
 'pour':rp('R2','11_car_pour'), 'vector':rp('R2','12_vector_insertion'),
 'law':rp('R3','14_law'), 'quadratic':rp('R2','14_quadratic_end'),
 'transf':rp('R2','15_displacements'), 'verb':rp('R3','17_final_verb'),
 'depl':rp('R3','18_last_formula'), 'nb_end':rp('R2','18_nb_final_punctuation'),
 'right':mp('01_diagram_right'), 'stack':mp('02_left_identities_gap_dot'),
 'bracket':mp('03_left_bracket_connector'), 'nb':mp('04_cancelled_NB'),
 'torsor':mp('05_torsor_insertion'), 'phrase':mp('06_NB_explanatory_phrase'),
 'formula1':mp('07_first_vector_formula'), 'formula2':rp('R3','13_aff_v'),
 'inline':mp('08_subgroup_inline_formula')}
r1=['D01','D02','D03','N01','N01','N02',None,'D04','N03','N04','D05','N20','D06','D07','D08','N05','D09','D10','D11','N06','D12','N07','N07','D13','N08','D14','N09','D15','N10','N12','D16','D17','N13','N14','N16','N17','D18','D19','N18','N19','D20','N11','N02']
r3=['C01','C02','C03','N01','N01','N02','N03','C04','N04','N05','C05','N24','C06','C07','C08','N06','C09','C10','C11','N07','C12','N08','N08','C13','N25','C14','N10','C15','N11','N13','C16','C17','N14','N16','N18','N19','C18','C19','N21','N22','C20','N12',None]
keys=['heading','heading','central','central','central','central','central','tau','tau','tau','equiv','stack','aff','aff','product','aff','adjective','old_aut','old_aut','old_aut','hom','hom','hom','pair','pair','nb','torsor','pour','phrase','bracket','vector','vector','vector','law','quadratic','quadratic','transf','verb','verb','depl','depl','nb_end','right']
obskeys=['heading','heading','upper central diagram','upper central diagram','upper central diagram','upper central diagram','upper central diagram','tau and lower point','tau and lower point','tau and lower point','right equivariance','upper identities and gap point','canceled Aff and product','canceled Aff and product','product annotation','canceled Aff and product','subgroup adjective','old Aut, sign and savoir','old Aut, sign and savoir','old Aut, sign and savoir','Hom introduction','Hom introduction','Hom introduction','ordered-pair map','ordered-pair map','canceled NB','target torsor and nonempty insertion','car ... si','NB explanatory phrase','left bracket and return','vector insertion and baseline','vector insertion and baseline','vector insertion and baseline','lower law','quadratic condition','quadratic condition','transf and following a','distance verb','distance verb','final operator','final operator','NB end','upper right sequence']
fs=copy.deepcopy(rep['R2']['findings'])
assert len(fs)==len(r1)==len(r3)==len(keys)==len(obskeys)==43
for i,f in enumerate(fs):
    f['readers']={'R1':get('R1',r1[i])['final'] if r1[i] else 'Vertical equal connector in the reading.tex diagram.',
                  'R2':f['final'], 'R3':get('R3','R3-'+r3[i])['final'] if r3[i] else 'Downward inclusion from central Aut and curved q below p in reading.tex.'}
    f['crop']=paths[keys[i]]
    f['evidence']=ob[obskeys[i]]['evidence']
    f['decision']='Main compared all three returns and inspected the named crop; the stated consolidated reading follows the ink.'
    for k in ['c','h','final']:
        f[k]=f[k].replace(r'd\prime op',"d'op").replace(r'd\textquotesingle op',"d'op")
by={i+1:f for i,f in enumerate(fs)}
def upd(n,**kw):by[n].update(kw)
upd(1,decision='Retain C and all readers: associated-word middle remains compressed; it is live, unlike H’s canceled illegibility.',kind=r'readable ink left as \ill{}')
upd(2,final=r'\unsure{\mathbb{Z}|Z}',decision='R1/R2 retain doubled/plain uncertainty; R3 resolves doubled. Main retains the two Z alphabets, excluding both G forms from C.',diff_c=True,confidence='medium')
upd(4,c=r'\text{ens. à}',h=r'\text{ens. à}',final=r'\text{ens à}',diff_c=True)
upd(5,c=r"\text{gr d'op}",h=r"\text{gpe d'op.}",final=r"\text{gr d'op}",diff_c=False)
upd(7,final='Slanted equals sign below-left of the upper Aff expression.',decision='Choose R2/R3 slanted equality over the vertical equal connector in C/R1; reproduce its below-left position with R3.',diff_c=True,diff_h=False)
upd(8,final=r'\tau_{g^{\unsure{\prime|.}}}^{\unsure{s|\deleted{s}|\delta}}',decision='Retain an s-like raised sign and unresolved cancellation, with delta as an alternative. Exclude g because no separate descender survives. The adjacent index mark is logged separately.',diff_c=True,consequential=True,math_note='The translation superscript and its deletion state remain unresolved. A usual inverse right-translation convention checks the sequence, but is not supplied to the text.')
upd(9,final=r'\tau_{g^{\unsure{\prime|.}}}',decision='Retain the detached raised mark as prime/point, following R3 geometry. Do not silently identify it with an unprimed g from the expected construction.')
upd(10,readers={'R1':'Lower detached point drawn without doubt (and a separate upper point).','R2':r'Lower detached \unsure{\cdot}', 'R3':r'Lower detached \unsure{.}'},final='Lower detached point, with uncertainty about its status as writing.',decision='Keep the point and its low position; its softer edge does not establish whether it is punctuation or incidental ink/surface trace.')
upd(12,final='Three stacked identities with no joining commas; separate underbraced right-hand criterion.',evidence=ob['upper identities and gap point']['evidence']+' The right criterion and its brace are also visible in '+paths['equiv']+'.')
upd(13,final=r"\deleted{\unsure{\substack{\text{ens à}\\\text{gr d'op}}}}",diff_c=True,decision='Retain the crossed wording but omit the unsupported ens stop, with R2. R1/R3 retained the stop under a broad doubt.')
upd(14,final=r'\deleted{\unsure{(\mathbb{Z}_{d})|(G_d)}}',diff_c=True,decision='Keep R3’s explicit G alternative: the crossed capital cannot be securely separated from the diagonal strikes.')
upd(15,final=r'\unsure{(produit|produit|(produits|produits} 1/2 direct)',decision='Both opening-parenthesis status and terminal s remain open; include all four combinations with C’s singular opening-parenthesis reading first.')
upd(16,final='A short oblique stroke drawn in TikZ below the first product factor.',confidence='high',decision='The stroke is definite ink. Follow R1’s purely graphical representation; its unidentified purpose is not a doubtful minus sign.')
upd(17,final='naturel',doubt_action='resolve',confidence='high',diff_c=True,decision='Choose R1/R3 naturel; the compressed strokes support this word and not R2/C structural or H évident.')
upd(18,final=r"de \deleted{\unsure{\operatorname{Aut}_{\substack{\text{ens}\\\text{gr d'op}}}(G,G_d)}}\operatorname{Aff}(\mathbb{Z})",diff_c=True,decision='The crossed operator follows de. Retain its uncertain letters, with no point after ens, as R2/R3 read.')
upd(19,final=r'\deleted{\unsure{=|-}}',diff_c=True,decision='Retain the equals/dash uncertainty of R1/R3; the blot does not warrant R2’s single candidate.')
upd(20,evidence=ob['old Aut, sign and savoir']['evidence']+' Same-line continuation is independently shown in '+paths['inline']+'.',decision='All three readers have savoir. Keep the following formula on the prose line, confirmed by its original y position.')
upd(22,decision='Choose R1/R2 singular primary, retain a possible s; do not infer number from the generic meaning.')
upd(23,decision='Choose R1/R2 singular primary, retain a possible s independently of the preceding word.')
upd(24,final=r'(E,\unsure{\mathbb{G}|G})',doubt_action='retain',confidence='medium',diff_h=True,decision='Source capital is rounded G, excluding C’s Z alternative. Choose R1’s doubled/plain doubt between R2 plain G and R3 doubled G.')
upd(27,consequential=True,math_note='Both primes are in the ink: the target E′ is a G′-torsor. H loses the primes and thereby changes the uniqueness hypothesis; M010-UNIQ verifies the written statement and M010-SOURCE refutes H’s altered version.')
upd(28,final=r'\deleted{\unsure{pour}} si',doubt_action='retain',diff_c=False,confidence='medium',decision='With R1/R3, retain the canceled word’s doubt; the strike hides its interior. The cancellation traverses pour, while si is live.')
upd(31,decision='Resolve the contraction grpe with R2: g, r shoulder, p return and e are visible, with no ou sequence.')
upd(32,final=r'\unsure{ss-jacent à|s-jacent à|sous-jacent à}',diff_c=True,confidence='low',decision='Retain R1/R3’s extra single-s alternative. The prefix before the long j descender is too compressed to settle; no following un is present.')
upd(35,final=r'non dég\unsure{,|.}, with inserted Q above the ending',decision='Only one punctuation mark is present. Its curved tail favors comma, with period retained. Place Q above that ending, avoiding a second stop or comma.',confidence='medium')
upd(36,final=r'\unsure{on|$\to$}',decision='Keep on/arrow uncertainty with R2/R3. The bent right end disfavors R1’s bare-dash alternative. The next-line a is logged separately.')
upd(39,confidence='high',decision='The short detached stroke is definite ink; draw it without asserting that it underlines the whole word.')
upd(43,evidence=ob['upper right sequence']['evidence']+' Central inclusion and left arrowhead are in '+paths['central']+'.')

def extra(r,id,key,others,**kw):
    f=copy.deepcopy(get(r,id));f['readers']={**others,r:f['final']};f['crop']=paths[key]
    f['decision']='Main inspected the named crop and adopts the stated reading.'
    f.update(kw);fs.append(f);return f
extra('R1','N22','heading',{'R2':'à un groupe','R3':'à un groupe'},evidence='A separate accented à follows the compressed associated-word; no colon is present.')
extra('R1','N04','stack',{'R2':'No upper detached point represented.','R3':'No upper detached point represented.'},place='Upper gap, far right of q(gamma) line',c='No upper point',h='No upper point',final='A separate black point in the upper gap, drawn in TikZ.',evidence=ob['upper identities and gap point']['evidence'],confidence='high',decision='Retain R1’s additional upper point. It is far from the closing parenthesis and is not treated as a joining comma.')
extra('R3','R3-N09','pair',{'R1':r"G'",'R2':r"G'"},final=r"\unsure{G'|C'}",decision='Keep R3’s new local G/C doubt. The open target outline lacks a secure inward bar; its later primary G is unmarked under the recurring-sign convention.')
extra('R3','R3-N15','formula1',{'R1':'Two separately centered displays.','R2':'Relation signs aligned.'},evidence=ob['lower display alignment']['evidence']+' Second formula: '+paths['formula2']+'.',decision='Choose R3 left-start alignment, supported by both original-coordinate crops.')
extra('R3','R3-N17','law',{'R1':'Aut_R(V) as one subscripted label.','R2':'Aut_R(V) as one subscripted label.'},evidence=ob['lower law']['evidence'],decision='Choose R3: R occupies its own lower line below the entire Aut(V) label.')
extra('R1','N21','transf',{'R2':'a le groupe','R3':'a le groupe'},evidence=ob['transf and following a']['evidence'])
extra('R3','R3-N23','right',{'R1':'No comma after final 1.','R2':'No comma after final 1.'},evidence='The rightmost 1 is followed by blank paper; no comma occurs there.')

text=(root/'readings/scan010/R2/reading.tex').read_text()
def replace(old,new):
    global text
    assert text.count(old)==1,(old,text.count(old))
    text=text.replace(old,new)
replace(r'\arrow[d,phantom,"\rotatebox{20}{$=$}" description]',r'\arrow[d,phantom,"{\rotatebox{18}{$=$}}"{description,xshift=-4.5em}]')
replace(r'&q(\gamma)=(\gamma,\gamma)\\',r'&\tikz[remember picture,baseline=(s010qline.base)]{\node[inner sep=0pt] (s010qline) {$q(\gamma)=(\gamma,\gamma)$};}\\')
replace(r"\tau_{g\unsure{'}}^{\unsure{s|\delta|g|\deleted{s}}}",r'\tau_{g^{\unsure{\prime|.}}}^{\unsure{s|\deleted{s}|\delta}}')
replace(r'\node[inner sep=0pt] at ([xshift=-.15em,yshift=-.65em]idefend) {$\unsure{\cdot}$};',r'\fill ([xshift=5.1em,yshift=.3ex]s010qline.east) circle (.45pt);'+'\n'+r'\node[inner sep=0pt] at ([xshift=-.15em,yshift=-.65em]idefend) {$\unsure{.}$};')
replace(r'(\mathbb{Z})\deleted{\unsure{(\mathbb{Z}_{d})}}',r'(\mathbb{Z})\deleted{\unsure{(\mathbb{Z}_{d})|(G_d)}}')
replace(r'\underset{\unsure{\rotatebox{-25}{$-$}}}{\mathbb{Z}}',r'\underset{\text{\tikz[baseline=-.4ex]{\draw (0,.04)--(.13,0);}}}{\mathbb{Z}}')
replace(r'\unsure{structural|naturel}','naturel')
replace(r'\deleted{\unsure{=}}',r'\deleted{\unsure{=|-}}')
replace(r"(E,G)\arrow[r,\"{(\rho,\gamma)}\"']\&(E',G')".replace('\\"','"'),r"(E,\unsure{\mathbb{G}|G})\arrow[r,\"{(\rho,\gamma)}\"']\&(E',\unsure{G'|C'})".replace('\\"','"'))
replace(r'\deleted{pour} si',r'\deleted{\unsure{pour}} si')
replace(r'\inserted{grpe \unsure{ss-jacent à|sous-jacent à}}',r'\inserted{grpe \unsure{ss-jacent à|s-jacent à|sous-jacent à}}')
replace(r'\Gamma&=\operatorname{Aut}_{R}(V)\subset\operatorname{Aut}_{\mathrm{gr}}(V)\\'+'\n'+r'\operatorname{Aff}_{R}(V)&\simeq V\mathbin{.}\operatorname{Aut}_{R}(V)',r'&\Gamma=\operatorname{Aut}_{R}(V)\subset\operatorname{Aut}_{\mathrm{gr}}(V)\\[.8em]'+'\n'+r'&\operatorname{Aff}_{R}(V)\simeq V\mathbin{.}\operatorname{Aut}_{R}(V)')
replace(r'\underset{\substack{\rotatebox{90}{$\ni$}\\\operatorname{Aut}_{R}(V)}}{\gamma}',r'\underset{\substack{\rotatebox{90}{$\ni$}\\\underset{R}{\operatorname{Aut}(V)}}}{\gamma}')
replace(r'non dég \inserted{$Q$}\unsure{,|.}',r'non \tikz[baseline=(s010deg.base)]{\node[inner sep=0pt] (s010deg) {dég\unsure{,|.}};\node[anchor=south,inner sep=0pt] at ([yshift=1ex]s010deg.north east) {\inserted{$Q$}};}')
# The two raised clauses and their callout curves are retained as actual shapes.
replace(r"sous $G'$\inserted{et $E\ne\varnothing$}",r"sous \tikz[baseline=(s010target.base)]{\node[inner sep=0pt] (s010target) {$G'$};\node[anchor=south west,inner sep=0pt] (s010nonempty) at ([xshift=.6em,yshift=1.5ex]s010target.north east) {\inserted{et $E\ne\varnothing$}};\draw ([xshift=.1em,yshift=-.2ex]s010target.south east) .. controls +(.2em,2ex) and +(1em,0) .. ([xshift=.2em]s010nonempty.south east);}")
replace(r'\inserted{grpe \unsure{ss-jacent à|s-jacent à|sous-jacent à}} vectoriel',r'\tikz[baseline=(s010vectoriel.base)]{\node[inner sep=0pt] (s010vectoriel) {vectoriel};\node[anchor=south west,inner sep=0pt] (s010underlying) at ([xshift=.3em,yshift=1.5ex]s010vectoriel.north west) {\inserted{grpe \unsure{ss-jacent à|s-jacent à|sous-jacent à}}};\draw ([xshift=-.2em,yshift=-.2ex]s010vectoriel.south west) .. controls +(-.1em,2ex) and +(1em,0) .. ([xshift=.2em]s010underlying.south east);}')
# Overlay the raised labels so they do not displace the following baseline words.
text=text.replace("(s010target) {$G'$}","(s010target) {$G'\\vphantom{\\rule{0pt}{3.8ex}}$}")
text=text.replace('(s010vectoriel) {vectoriel}',r'(s010vectoriel) {vectoriel\vphantom{\rule{0pt}{3.8ex}}}')
text=text.replace(r'\node[anchor=south west,inner sep=0pt] (s010nonempty)',r'\node[overlay,anchor=base west,inner sep=0pt] (s010nonempty)')
text=text.replace(r'\node[anchor=south west,inner sep=0pt] (s010underlying)',r'\node[overlay,anchor=base west,inner sep=0pt] (s010underlying)')
text=text.replace(r'[xshift=.6em,yshift=1.5ex]s010target.north east',r'[xshift=.6em,yshift=2.6ex]s010target.base east')
text=text.replace(r'[xshift=.3em,yshift=1.5ex]s010vectoriel.north west',r'[xshift=.3em,yshift=2.6ex]s010vectoriel.base west')
text=text.replace(r'\draw ([xshift=.1em,yshift=-.2ex]s010target.south east)',r'\draw[overlay] ([xshift=.1em,yshift=-.2ex]s010target.base east)')
text=text.replace(r'\draw ([xshift=-.2em,yshift=-.2ex]s010vectoriel.south west)',r'\draw[overlay] ([xshift=-.2em,yshift=-.2ex]s010vectoriel.base west)')
for place,key,wording in [('Raised nonemptiness insertion and its callout','torsor',r'et $E\ne\varnothing$'),('Raised underlying-group insertion and its callout','vector',r'grpe ss-jacent à')]:
    fs.append(dict(id='MAIN-callout',place=place,c='Insertion macro; connector not drawn.',h='Insertion described in a note; connector not drawn.',final='Raised insertion with curved connector reproduced in TikZ: '+wording,evidence='The raised clause has a continuous curved callout to its insertion site, visible in the named crop.',confidence='high',kind='drawing or diagram',marked_in_H=False,diff_c=True,diff_h=True,bbox=[500,1228,1330,1380] if key=='torsor' else [382,1534,1383,1657],crop=paths[key],doubt_action='',s_id='',math_note='',readers={r:'Insertion text represented with the inserted macro; no explicit callout curve.' for r in rep},decision='Main retains the insertion wording and adds its observed raised placement and curved callout.'))
text=text.replace('% A detached point is below the right end of the i(g) line; punctuation versus stray ink is unresolved.','% Detached upper-gap point and lower i(g) point; only the lower point has uncertain status as writing.')
(root/'decisions/scan010_final.tex').write_text(text)

inventory=copy.deepcopy(rep['R3']['inventory'])
inventory.insert(4,dict(sheet_kind='text',hand='his hand',element='Upper-gap detached point',kind='drawing',position='x767 y426, far right of q(gamma) line',first_words_or_objects='small isolated black point, function unassigned',transcribed='yes'))
for x in inventory:
    if x['element']=='Example heading':x['first_words_or_objects']='Ex; Groupe affine associé? à un groupe doubled/plain Z'
    if x['element']=='Hom introduction':x['first_words_or_objects']='Hom d’ens à op. avec groupe(s) variable(s), singular primary'
    if x['element']=='Ordered-pair map':x['first_words_or_objects']='(E,doubled/plain G) to (E-prime,G-prime/C-prime), label below'
    if x['element']=='Underlying-group wording':x['first_words_or_objects']='grpe; ss-jacent à/s-jacent à/sous-jacent à; raised with callout curve'
    if x['element']=='Nonemptiness insertion':x['first_words_or_objects']='et E ≠ empty, raised with callout curve after G-prime'
    if x['element']=='Quadratic form label':x['first_words_or_objects']='Q raised above ending of non dég and its single doubtful punctuation mark'
events=json.loads((root/'pending_events/scan010.json').read_text())
for e in events:
    e['who']=e['who'].replace(' preliminary check','')
    e['outcome']=e['outcome'].replace('The superscript and translation convention in the manuscript remain to be read; no formula is silently repaired.','The ink leaves the superscript/state unresolved and adds a doubtful prime-like index mark; the convention is not supplied and no formula is repaired.').replace('Which primes are in the ink still awaits adjudication; this is not yet a claim of manuscript error.','The crops confirm E-prime and G-prime in the manuscript. The refutation concerns H’s altered hypothesis, not the manuscript.').replace('the written nondegeneracy phrase and verb still await ink adjudication.','the ink retains the abbreviated nondegeneracy phrase and the doubtful invarient/invariant verb; no positive-definiteness hypothesis is supplied.')
for r in rep:
    for sid,c in zip(['M010-UNIQ','M010-VEC'],rep[r]['checks']):
        events.append(dict(statement_id=sid,date='2026-11-20',who=f'GPT-6 Astra Pro; effort inherited/not exposed; scan010 {r}',type='targeted proof check',outcome=c['statement']+' '+c['reasoning']+' '+c['outcome']))
unresolved=[('Heading word','associé','compressed interior; no secure competing word','medium'),('Recurring angular group alphabet',r'\mathbb Z','Z','medium'),('Permutation alphabet',r'\mathfrak S',r'\mathcal S','medium'),('Tau superscript/state','live s','canceled s; delta','low'),('Tau index raised trace','prime-like mark','point or incidental trace; role unassigned','low'),('Point below i(g)','lower detached point','writing versus incidental ink/surface trace','low'),('Canceled Aff subscript',"ens à / gr d'op",'letters partly covered by cancellation','low'),('Canceled Aff argument',r'(\mathbb Z_d)',r'(G_d)','low'),('Product annotation','(produit','produit; (produits; produits','low'),('Canceled Aut expression',"Aut with ens / gr d'op and (G,G_d)",'letters partly crossed; alphabet not secure','low'),('Canceled sign after Aff','=','dash','low'),('Hom group-word ending','groupe','groupes','medium'),('Hom variable-word ending','variable','variables','medium'),('Source pair group alphabet',r'\mathbb G','G','medium'),('Target group capital',"G'","C'; later primary G unmarked",'medium'),('Canceled NB word','pour','interior obscured by strike; no competing word secured','medium'),('Underlying-group insertion','ss-jacent à','s-jacent à; sous-jacent à','low'),('Nondegeneracy punctuation','comma','period; only one mark exists','medium'),('Final connector','on','rightward arrow','low'),('Distance verb','invarient','invariant','low'),('Canceled Depl subscript','aff','Aff; orth','low')]
notes="""The handwritten page, headed underlined Ex, gives the affine-group split sequence, its diagonal section and translation inclusion, a boxed conjugation identity, the equivariance criterion, subgroups induced by Gamma, a note on maps with variable acting groups, and vector-space and quadratic-form examples. It has no date or author page number; archive foliation 9 is comment-only. S has no row on this scan.

The ink has the live associated-word, the adjective naturel, savoir, the target-torsor primes E′ and G′, the inserted unprimed E≠∅, and en termes de rho. The p-initial word after car is canceled and si is live; pour remains doubtful beneath the strike. No authorial question or explicit doubt phrase is securely written. The angular group alphabet remains doubled/plain Z; the source pair instead has rounded doubled/plain G. A local G′/C′ outline doubt is retained at the target pair. The tau superscript/state and a small raised index mark remain unresolved; the expected translation notation does not replace them. All 20 C doubts have explicit dispositions: six resolved, fourteen retained, with changed alternatives recorded separately from errors.

The slanted equality, stacked identities, vertical equivariance, lower membership signs, left-start alignment, R beneath the entire Aut(V) label, and long arrow back to this page’s heading are reproduced. Both raised clauses retain their curved callouts. The upper gap point, softer low point after i(g), and two short detached strokes are retained without assigning functions; the low point’s status as writing remains doubtful. The final paragraph has one punctuation mark after the abbreviated nondegeneracy phrase, with Q raised above that ending, and a doubtful on/arrow trace. No extra NB terminal period is supplied.

The actual checks, recorded in CHECK_EVENTS.tsv, establish the split affine pair construction under the left-regular interpretation. Writing rho(x)=gamma(x)a identifies the kernel with right translations; composition reverses their positive parameters, so an inverse right-translation parametrization makes the inclusion a homomorphism and yields the boxed conjugation formula. This is conditional on the translation convention, which the doubtful tau notation does not settle. Projection to rho embeds the group as the normalizer of left translations, and inverse images of Gamma give the stated semidirect subgroups.

For the NB, choosing x in the nonempty source and using freeness of the target action proves uniqueness of gamma. H’s source-torsor version is false: a constant map from a regular C2-set to a trivial singleton C2-set is compatible with both the trivial and identity homomorphisms. Omitting nonemptiness also destroys uniqueness for the empty source. These are checks of an altered witness statement and a counterfactual variant, not corrections of the manuscript. Composition of equivariant pairs also checks directly.

Composing x↦z+gamma(x) gives the written vector affine law, identity and inverse; R1 additionally checked associativity directly. For affine maps, preservation of Q(x−y) is equivalent to membership of the linear part in Orth(V,Q), giving the final semidirect expression under that interpretation. If distance means the real metric sqrt(Q(x−y)), positive definiteness is needed: the nondegenerate form x²−y² is negative at (0,1). This qualification does not change the written nondegeneracy phrase or doubtful verb. No external material was used."""
dec=dict(base='R2',text_file='decisions/scan010_final.tex',findings=fs,inventory=inventory,notes=notes,events=events,unresolved=[dict(place=p,reading=x,alternatives=a,confidence=c) for p,x,a,c in unresolved],abbreviations=rep['R2']['abbreviations'],main_crop_count=8,main_crop_views=obs['main_crop_views'])
(root/'decisions/scan010.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
coverage=json.loads((root/'decisions/scan010_C_doubt_coverage.json').read_text())
nums=[1,2,3,8,11,13,14,15,17,18,19,21,24,26,28,31,32,37,38,41]
for d,n in zip(coverage['doubts'],nums):
    d['disposition']=by[n]['doubt_action'];d['findings']=[f'S010-{n:03d}'];d['final']=by[n]['final'];d['crop']=by[n]['crop']
assert all(d['disposition'] in ('retain','resolve') for d in coverage['doubts'])
(root/'decisions/scan010_C_doubt_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((root/'readings/scan010').glob('R*/*')) if p.name in ('reading.tex','report.json')}
(root/'decisions/scan010_reader_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(dict(findings=len(fs),inventory=len(inventory),events=len(events),doubts=len(unresolved),views=len(obs['main_crop_views'])))
