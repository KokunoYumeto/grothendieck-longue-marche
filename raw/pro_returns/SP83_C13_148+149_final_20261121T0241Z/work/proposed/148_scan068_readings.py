"""Manual first-reading data for 148_scan068; no OCR or pixel recognition.
Crops were inspected by reader_c. Positions are printer-character cells.
Retained as work documentation.
"""
BANNER = {
 'p': ['P'*11,'P'*12,'PP'+' '*8+'PP','PP'+' '*8+'PP','PP'+' '*8+'PP','P'*12,'P'*11,'PP','PP','PP','PP','PP'],
 'r': ['R'*11,'R'*12,'RR'+' '*8+'RR','RR'+' '*8+'RR','RR'+' '*8+'RR','R'*12,'R'*11,'RR'+' '*4+'RR','RR'+' '*5+'RR','RR'+' '*6+'RR','RR'+' '*7+'RR','RR'+' '*8+'RR'],
 'e': ['E'*12,'E'*12,'EE','EE','EE','E'*8,'E'*8,'EE','EE','EE','E'*12,'E'*12],
 'd': ['D'*9,'D'*10,'DD'+' '*7+'DD','DD'+' '*8+'DD','DD'+' '*8+'DD','DD'+' '*8+'DD','DD'+' '*8+'DD','DD'+' '*8+'DD','DD'+' '*8+'DD','DD'+' '*7+'DD','D'*10,'D'*9],
 'o': ['O'*12,'O'*12]+['OO'+' '*8+'OO']*8+['O'*12,'O'*12],
 'n': ['NN'+' '*8+'NN','NNN'+' '*7+'NN','NNNN'+' '*6+'NN','NN NN'+' '*5+'NN','NN  NN'+' '*4+'NN','NN   NN'+' '*3+'NN','NN    NN'+' '*2+'NN','NN     NN NN','NN'+' '*6+'NNNN','NN'+' '*7+'NNN','NN'+' '*8+'NN','NN'+' '*9+'N'],
 't': ['T'*12,'T'*12]+[' '*5+'TT'+' '*5]*10,
 'a': [' '+'A'*10+' ','A'*12]+['AA'+' '*8+'AA']*3+['A'*12,'A'*12]+['AA'+' '*8+'AA']*5,
}
# The four zero patterns were counted separately on the one complete-array crop.
# Their matching row readings are recorded explicitly, with no regularization.
ZERO_OFFSETS = [10,9,7,6,5,4,3,2,1,0,0,0]
ZERO_LOCAL = [
 '00000000', '0000000000', '00      0000', '00     00 00',
 '00    00  00', '00   00   00', '00  00    00', '00 00     00',
 '0000      00', '000       00', '0000000000', '00000000',
]
ZERO_COLUMNS = [list(ZERO_LOCAL),list(ZERO_LOCAL),list(ZERO_LOCAL),list(ZERO_LOCAL)]
JOB = '****A END JOB 653 PREDONTA  ROOM  11.24.04 AM 02 JUN 82 R6.PR1  SYS JES2 JOB 653 END A****'

def tt(s):
    return '\\texttt{'+s.replace(' ','\\ ')+'}'

if __name__ == '__main__':
    import csv,re
    marks=list(csv.DictReader(open('packets/148_scan068/MARKS.tsv'),delimiter='\t'))
    dif=[]
    for i,m in enumerate(marks):
        c=m['the mark as written'][len('\\unsure{\\texttt{'):-2].replace('\\ ',' ')
        if i<96:
            row,col=divmod(i,8); ch='predonta'[col]; s=BANNER[ch][row]
        else:
            row,col=divmod(i-96,4);ch='zero'+str(col+1);s=' '*ZERO_OFFSETS[row]+ZERO_COLUMNS[col][row]
        if c!=s: dif.append((m['id'],ch,row+1,c.replace(' ','.'),s.replace(' ','.')))
    print('Manual pattern differences from C:',len(dif))
    for d in dif:print(*d,sep=' | ')
