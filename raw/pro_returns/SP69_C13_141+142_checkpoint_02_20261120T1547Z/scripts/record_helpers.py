from workflow import *
def change(place,C,H,final,ink,kind='misread symbol or index',confidence='high',against_C=True,against_H=True,crop='page',marked_in_H='no',consequential=''):
 return dict(place=place,C=C,H=H,final=final,ink=ink,kind=kind,confidence=confidence,against_C=against_C,against_H=against_H,crop=crop,marked_in_H=marked_in_H,consequential=consequential)
def decision(id,decision,reading,ink,crop='page',confidence='high'):
 return dict(id=id,decision=decision,reading=reading,**{'what the ink shows':ink},crop=crop,confidence=confidence)
def inv(kind,position,words,hand='his hand'):return [hand,kind,position,words]
def check(id,place,statement,outcome,type='targeted proof check'):
 return dict(statement_id=id,place=place,statement=statement,outcome=outcome,type=type)
def base(key):return (SRC/(STEM+'_texts')/'pages'/(key+'.tex')).read_text()
def replace(tex,a,b):
 if a not in tex:raise ValueError('Missing replacement '+repr(a))
 return tex.replace(a,b)
