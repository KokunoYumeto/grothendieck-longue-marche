from page_work import save_page
text=r'''\scanpage{134}
\deleted{$\overline{\underline{\mathrm V}}$}
\deleted{\uline{Fidèle platitude}\par
\uline{Descente} fid. plate\par
Applications}
\mspage{133}
'''
elements=[('text','top, left of title','V with upper and lower bars'),('deletion','top','V crossed by oblique line'),('text','top right','Fidèle platitude; Descente fid. plate; Applications'),('deletion','across title','three oblique cancellation strokes'),('text','bottom left','133')]
save_page(134,text,elements,sheet_kind='cover',observations='Whole, top half and bottom half inspected. Title and V are crossed; underline on Fidèle platitude and Descente, no added page count.')
