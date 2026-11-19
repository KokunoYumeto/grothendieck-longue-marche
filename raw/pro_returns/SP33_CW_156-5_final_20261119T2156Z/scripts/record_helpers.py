def D(place,c,h,final,evidence,c_changed=False,h_changed=False,kind='other',confidence='high',marked_h='no',consequential=None,id=None):
 r=dict(place=place,c=c,h=h,final=final,evidence=evidence,c_changed=c_changed,h_changed=h_changed,kind=kind,confidence=confidence,marked_h=marked_h)
 if consequential:r['consequential']=consequential
 if id:r['id']=id
 return r
def E(kind,position,text):return dict(kind=kind,position=position,text=text)
def Q(place,reading,alternatives='',confidence='medium',reason=''):return dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason)
