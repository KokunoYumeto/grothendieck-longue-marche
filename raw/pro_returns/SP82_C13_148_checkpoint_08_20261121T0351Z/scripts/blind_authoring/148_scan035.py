"""Independent blind visual reading of scan035, authored from fixed crops.

No recognition software, external research, comparison or TeX compilation.
"""
import csv
import json
import os
import tempfile
from pathlib import Path

BASE=Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
INPUT=Path('/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan035/boxes.tsv')
DISPLAY=Path('/workspace/scratch/8132fe1cca43/work/blind_display/148_scan035')

R={}
R['035_heading_case']=r'''\mspage{(4)} $\nu=2$.
\deleted{Il y a \unsure{deux} cas}
\inserted{\unsure{Dans les}}'''

R['035_first_kg']=r'''$K^g=\{P\}$, et $K\setminus K^g$ \inserted{$=I$} est réunion'''

R['035_autom_universel']=r'''Ainsi, $g$ est un autom. \deleted{\unsure{de}} ``universel'' de'''

R['035_di_fixed']=r'''$\Sigma\setminus I$ $(g\in V(\unsure{D_I|\mathcal D_I}))$ et $P$ est \inserted{\unsure{un aut.}} un p\textsuperscript{t} fixe. \deleted{\unsure{De|Ce}} Cette fois,'''

R['035_modules_orbit']=r'''la situation \unsure{a} des ``modules'', p.ex. en choisissant une'''

# The local corrections below sit within a broad canceled passage. Nested
# deleted macros retain separately visible local cancellations.
mu=r'''\unsure{p.ex.} pour l'opération de $\langle g\rangle$ sur
\deleted{celle-ci est celle de} $\mu_2$\inserted{$=\{\pm1\}$} sur $\mu_2$\inserted{$=(\pm1)$}, et $P=0$, l'autre orbite'''
orbit=r'''est \deleted{donnée par} une $\{t,-t\}$, avec $\lambda=t^2\ne1$, $\lambda\in k^\times$ ---'''
jline=r'''donc $\unsure{\lambda=}\quad J=(0,\pm1,\pm\unsure{\sqrt\lambda|t})\deleted{\unsure{\sqrt\lambda,-\sqrt\lambda)}}$, avec $\lambda\in\Sigma(k)\setminus\{0,1,\infty\}$,'''
change=r'''Si on \deleted{change} change le choix de l'orbite, \unsure{on trouve}'''
parameter=r'''$(0,\pm1,\pm\sqrt{1/\lambda})$. Prenons le paramètre $\rho=\lambda+\frac1\lambda$\inserted{$\ne2$}, donc $\lambda^2-\rho\lambda+1=0$;
\deleted{$\lambda=\frac12(\rho\pm\sqrt{\rho^2-4})$}'''
triple=r'''on trouve $(0,\pm1,\pm\sqrt{\frac12(\rho\pm\sqrt{\rho^2\unsure{-4}})})$.'''
eliminer=r'''Eliminer $0,\infty$, et \unsure{les}'''
comme=r'''comme $\unsure{f^{\circ}|\rho}\quad\lambda$, et'''
discriminant=r'''\unsure{discriminant} $\lambda\longrightarrow1$, ou $-$'''
gline=r'''$g(z)=\frac{\unsure{\lambda|1}}{z}$, p\textsuperscript{ts} fixes'''

R['035_canceled_mu']='des deux orbites, \\deleted{'+mu+'}'
R['035_canceled_orbit']='\\deleted{'+orbit+'}'
R['035_canceled_J']='\\deleted{'+jline+'}'
R['035_canceled_change']='\\deleted{'+change+'}'
R['035_canceled_parameter']='\\deleted{'+parameter+'}'
R['035_canceled_triple']='\\deleted{'+triple+'}'
R['035_canceled_eliminer']='\\deleted{'+eliminer+'\n'+r'''$\unsure{f^{\circ}|\rho}\quad\lambda$, et'''+ '}'
R['035_canceled_discriminant']='\\deleted{'+discriminant+'}'
R['035_canceled_g']='\\deleted{'+gline+'}'
R['035_canceled_comme']='\\deleted{'+comme+'}'

R['035_pointdevue']='\\deleted{'+gline+r'''}
Cas moins intéressant que les
précédents, de notre point de vue, car il y a des'''

R['035_des_sommets']=r'''cas \inserted{des sommets} d'un \deleted{\unsure{cube}} carré'''

question=r'''\inserted{Est-ce le cas $1^{\circ}$ ?}'''
R['035_equilateral_edge']=r'''sphériques équilatéraux et des milieux de
une des arêtes. '''+question+r'''
Quand c'est une structure'''
R['035_question_tetra']=question+r'''
Quand c'est une structure
$P$ est un des \inserted{6} sommets de l'
'''

R['035_figure_upper']=r'''\figure{\begin{tikzpicture}[x=.0045cm,y=-.0045cm,line cap=round,line join=round]
\draw[line width=.7pt] (534,335) .. controls (507,242) and (567,121) .. (662,72) .. controls (767,12) and (916,12) .. (967,104) .. controls (1000,161) and (1004,225) .. (987,297);
\draw[line width=.55pt] (980,318) .. controls (966,430) and (887,490) .. (789,502) .. controls (678,527) and (557,441) .. (534,335);
\draw[line width=.7pt] (534,335) .. controls (648,366) and (860,321) .. (970,267);
\draw[line width=.55pt,dash pattern=on 6pt off 7pt] (534,308) .. controls (666,249) and (883,194) .. (972,229);
\fill (602,342) circle (9);\fill (682,340) circle (8);\fill (780,330) circle (10);
\fill (672,255) circle (10);\fill (860,222) circle (8);
\node[below,font=\small,inner sep=1pt] at (685,354) {$P$};
\draw[line width=.65pt] (124,358) .. controls (87,371) and (62,405) .. (54,449);
\draw[line width=.55pt] (49,447) .. controls (51,457) and (58,450) .. (59,443);
\end{tikzpicture}}'''

R['035_figure_lower']=r'''\figure{\begin{tikzpicture}[x=.0045cm,y=-.0045cm,line cap=round,line join=round]
\draw[line width=.7pt] (177,292) .. controls (269,171) and (500,68) .. (594,86) .. controls (696,80) and (753,208) .. (783,322) .. controls (811,422) and (767,578) .. (725,650);
\draw[line width=.8pt] (177,292) .. controls (90,389) and (120,647) .. (202,733) .. controls (298,816) and (502,836) .. (619,745);
\draw[line width=.5pt] (176,292) .. controls (112,329) and (57,553) .. (173,732);
\draw[line width=.55pt] (180,288) .. controls (263,200) and (470,92) .. (559,117);
\draw[line width=.65pt] (445,225) .. controls (426,257) and (401,293) .. (374,320);
\draw[line width=.6pt] (488,246) .. controls (467,286) and (451,328) .. (439,365);
\draw[line width=.65pt] (548,246) .. controls (551,304) and (568,326) .. (581,356) .. controls (619,416) and (655,492) .. (682,537);
\draw[line width=.55pt] (405,398) .. controls (367,452) and (287,492) .. (200,550);
\draw[line width=.65pt] (453,414) .. controls (500,447) and (548,451) .. (567,478);
\draw[line width=.55pt,dash pattern=on 4pt off 6pt] (609,500)--(635,536);
\draw[line width=.65pt] (444,579) .. controls (520,583) and (602,578) .. (682,563);
\draw[line width=.55pt,dash pattern=on 6pt off 7pt] (188,563) .. controls (280,568) and (371,591) .. (444,579);
\draw[line width=.5pt,dash pattern=on 1pt off 6pt] (432,395)--(188,563);
\draw[line width=.5pt,dash pattern=on 1pt off 8pt] (432,395)--(581,356);
\draw[line width=.55pt] (654,322)--(671,318);
\draw[line width=.45pt] (523,184)--(527,203);
\foreach \p in {(515,154),(430,395),(188,563),(682,563),(715,300)} {\fill \p circle (10);}
\fill (568,351)--(581,344)--(590,358)--(578,368)--cycle;
\fill (302,479)--(321,469)--(333,480)--(325,496)--cycle;
\draw[line width=.6pt] (248,468)--(200,532)--(210,539);
\draw[line width=.6pt] (201,548)--(225,505)--(268,487);
\node[right,font=\small,inner sep=2pt] at (741,287) {$P$};
\end{tikzpicture}}'''

R['035_antiauto_heading']=r'''\uline{Cas des antiautomorphismes \inserted{$\sigma$} de} $\Sigma$ laissant
\uline{stables} $K$. \inserted{(cas $k=\mathbb C$)} Comme $\sigma$ est d'ordre pair, on voit qu'il
dans $K$, donc dans $\Sigma$,'''

R['035_antiauto_body']=r'''\deleted{\unsure{et}}. un p\textsuperscript{t} fixe au moins
et étant d'ordre fini, on sait qu'il est d'ordre $2$,
il correspond à une structure réelle sur $\Sigma$, \deleted{et}
On distingue suivant le cardinal de $K^\sigma$, qui est $1,3$,
ou $6$.'''

R['035_page_two']=r'''\mspage{2}'''
R['035_folio']=r'''\margin{\mspage{34}}'''

R['035_square_case_number']=r'''précédents, de notre point de vue,
modules. Quand la structure $(\Sigma,I)$ est une
structure carrée, on retrouve soit le cas $2^{\circ}$ (si $g$ laisse
deux diagonales), soit le cas \inserted{des sommets} d'un \deleted{\unsure{cube}} carré'''

R['035_large_canceled_scope']='des deux orbites, \\deleted{'+ '\n'.join((mu,orbit,jline,change,parameter,triple,eliminer,comme,discriminant,gline))+r'''}
Cas moins intéressant que les'''

EXTRA_VIEWS=('heading_case','di_fixed','canceled_J','canceled_triple','canceled_discriminant','antiauto_body','question_tetra','canceled_comme')

def atomic(path, callback):
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix=path.name+'.',suffix='.tmp',dir=path.parent)
    try:
        with os.fdopen(fd,'w',encoding='utf-8',newline='') as f:
            callback(f)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp,path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

def main():
    with INPUT.open(newline='') as f:
        rows=list(csv.DictReader(f,delimiter='\t'))
    assert len(rows)==27
    assert set(R)=={r['box'] for r in rows}
    journal={
        'page':'148_scan035',
        'protocol':'Independent blind visual reading using only the assigned scan/box list and derivatives of each saved full fixed crop. No OCR, external research, comparison, other page or TeX compilation.',
        'fixed_crop_run':'scripts/blind_io.py crop 35, once',
        'views':[],
        'failed_display_note':'The first attempted native3 question_tetra display was discarded at the code-mode output limit after antiauto_body. It was retried alone and successfully inspected; the failed attempt did not count as a viewing.',
        'observations':[
            'All27 fixed enhanced crops were successfully viewed before authoring the complete file.',
            'Eight complete saved crops were additionally viewed as native-color3x enlargements. No detail rectangles or rotations were created.',
            'The large canceled scope retains the uncanceled initial words and the uncanceled new paragraph at the end; nested deleted macros preserve smaller local cancellations within it.',
            'The inserted restriction appears as neq2, without an added plus/minus sign. The final numeral in antiauto_body reads6, retained despite the preceding1,3.',
            'The question annotation reads1-degree, and the square-case paragraph reads2-degree; neither was normalized to another case number.',
            'Uncertainties remain in the heading replacement words, the interlinear correction in di_fixed, some crossed-out words, the locally canceled radical terms in canceled_J, and the marked radicand in canceled_triple.',
            'The partly obscured numerator in canceled_g is retained as1/lambda uncertainty. The surviving arrow in canceled_discriminant is transcribed as lambda right-arrow1; no inferred missing term is supplied.',
            'The small drawings use literal strokes and patches. Ambiguous tapered patches were not assigned an inferred arrow direction.',
            'Perforations and paper specks were not treated as writing.'
        ]
    }
    for row in rows:
        name=row['box']
        entry={'box':name,'fixed_crop':f'crops/second/148_scan035/{name}.png','successful_displays':[str(DISPLAY/(name+'.jpg'))],'rotation_degrees':0,'successfully_inspected':True}
        if name.removeprefix('035_') in EXTRA_VIEWS:
            entry['successful_displays'].append(str(DISPLAY/(name+'_native3.png')))
        journal['views'].append(entry)
    def tsv(f):
        writer=csv.writer(f,delimiter='\t',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        writer.writerow(['box','reading'])
        for row in rows:
            writer.writerow([row['box'],R[row['box']].strip()])
    atomic(BASE/'second/148_scan035_second.tsv',tsv)
    atomic(BASE/'second/148_scan035_blind_journal.json',lambda f:json.dump(journal,f,ensure_ascii=False,indent=2))
    print('Atomically wrote27 scan035 readings and27 successful-inspection journal entries.')

if __name__=='__main__':
    main()
