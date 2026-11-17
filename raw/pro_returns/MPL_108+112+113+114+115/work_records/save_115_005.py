from record import save_page
P=['PPPPPPPPPPP ','PPPPPPPPPPPP']+['PP        PP']*3+['PPPPPPPPPPPP','PPPPPPPPPPP ']+['PP          ']*5
R=['RRRRRRRRRRR ','RRRRRRRRRRRR']+['RR        RR']*3+['RRRRRRRRRRRR','RRRRRRRRRRR ','RR    RR    ','RR     RR   ','RR      RR  ','RR       RR ','RR        RR']
E=['EEEEEEEEEEEE']*2+['EE          ']*3+['EEEEEEEE    ']*2+['EE          ']*3+['EEEEEEEEEEEE']*2
D=['DDDDDDDDD   ','DDDDDDDDDD  ','DD       DD ']+['DD        DD']*6+['DD       DD ','DDDDDDDDDD  ','DDDDDDDDD   ']
O=['OOOOOOOOOOOO']*2+['OO        OO']*8+['OOOOOOOOOOOO']*2
N=['NN        NN','NNN       NN','NNNN      NN','NN NN     NN','NN  NN    NN','NN   NN   NN','NN    NN  NN','NN     NN NN','NN      NNNN','NN       NNN','NN        NN','NN         N']
T=['TTTTTTTTTTTT']*2+['     TT     ']*10
rows=['  '.join(r).rstrip().replace(' ',r'\ ') for r in zip(P,R,E,D,O,N,T)]
tex='\\scanpage{5}\n% archive foliation: 4\n\\diagram{\\begin{array}{l}\n'+(' \\\\\n'.join(r'\texttt{'+r+'}' for r in rows))+'\n\\end{array}}\n\n'
record=r'\texttt{****A END JOB 3 PREDONT - CRAY OUTPUT - ROOM 11.24.23 AM 02 JUN 82 R6.PR1 SYS JES2 JOB 3 END A****}'
tex+='\n\n'.join([record]*6)
save_page(115,5,tex,[('diagram','printed large banner','PREDONT')]+[('text',f'printed record {n}','****A END JOB 3 PREDONT') for n in range(1,7)],'reused_typed',doubts=[('banner','individual letter counts and spacing','slight uncertainty in N diagonal and E middle bars','medium')],notes='Printed-only reverse: twelve-line PREDONT banner and six END JOB records, dated 02 JUN 82. All banner letters and six repeated records transcribed; no mathematical handwriting visible.')
