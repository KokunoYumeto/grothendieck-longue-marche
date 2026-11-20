from pathlib import Path
from records import *
ROOT=OUT.parent

def source(scan):
 return (ROOT/'source/SP59_CW_71_witnesses/codex'/FOLDERS[scan]/'pages'/page_name(scan)).read_text()

def replace(tex, old, new):
 if old not in tex: raise ValueError('Replacement not found: '+old)
 return tex.replace(old,new)

def ch(place,C,H,final,scan_shows,diff_C=False,diff_H=False,kind='other',error_kind='Other',confidence='high',**kw):
 return dict(place=place,C=C,H=H,final=final,scan_shows=scan_shows,diff_C=diff_C,diff_H=diff_H,kind=kind,error_kind=error_kind,confidence=confidence,**kw)

def inv(kind,position,first_words_or_objects,**kw):
 return dict(kind=kind,position=position,first_words_or_objects=first_words_or_objects,**kw)

def doubt(place,reading,alternatives='',confidence='medium',status='remaining'):
 return dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,status=status)
