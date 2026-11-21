#!/usr/bin/env python3
"""Read-only geometric recovery of two retained PNG crop transforms. No OCR.
All crop/source image transformations are in memory. No evidence image is written.
"""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import numpy as np
from scipy.signal import fftconvolve
import json,hashlib,time
ROOT=Path('/workspace/scratch/f28c4f52d3ec')
PAGES={'148_scan051_r_arrow.png':'148_scan051','148_scan053_cela.png':'148_scan053'}
def window_sums(a,h,w):
 s=np.pad(a,((1,0),(1,0))).cumsum(0).cumsum(1)
 return s[h:,w:]-s[:-h,w:]-s[h:,:-w]+s[:-h,:-w]
def ncc(src,t):
 h,w=t.shape
 z=t-t.mean()
 numerator=fftconvolve(src,z[::-1,::-1],mode='valid')
 den=np.sqrt(np.maximum(window_sums(src*src,h,w)-window_sums(src,h,w)**2/(h*w),1e-10)*np.sum(z*z))
 return numerator/den

def coarse():
 out={}
 for crop,page in PAGES.items():
  sim=Image.open(ROOT/'source/SP83_C13_148+149_scans'/(page+'.jpg')).convert('L')
  cim=Image.open(ROOT/'result/crops'/crop).convert('L')
  src=np.asarray(sim.resize((sim.width//4,sim.height//4),Image.Resampling.LANCZOS),dtype=np.float64)
  candidates=[]
  for w in range(30,min(src.shape[1],400),2):
   h=round(w*cim.height/cim.width)
   if h<5 or h>src.shape[0]:continue
   t=np.asarray(cim.resize((w,h),Image.Resampling.LANCZOS),dtype=np.float64)
   a=ncc(src,t);y,x=np.unravel_index(a.argmax(),a.shape)
   candidates.append({'score':float(a[y,x]),'box_coarse':[int(x),int(y),int(x+w),int(y+h)],'size_coarse':[w,h]})
  candidates.sort(key=lambda r:r['score'],reverse=True)
  out[crop]=candidates[:10]
  print(crop,json.dumps(candidates[:5]),flush=True)
 return out

def refine():
 out={}
 settings={'148_scan051_r_arrow.png':([590,1570,1060,1785],range(375,411)), '148_scan053_cela.png':([320,1590,1075,1750],range(650,697))}
 for crop,(roi,ws) in settings.items():
  page=PAGES[crop]
  sim=Image.open(ROOT/'source/SP83_C13_148+149_scans'/(page+'.jpg')).convert('L')
  cim=Image.open(ROOT/'result/crops'/crop).convert('L')
  src=np.asarray(sim.crop(roi),dtype=np.float64)
  cand=[]
  for w in ws:
   hh=round(w*cim.height/cim.width)
   for h in range(hh-2,hh+3):
    t=np.asarray(cim.resize((w,h),Image.Resampling.LANCZOS),dtype=np.float64)
    a=ncc(src,t); y,x=np.unravel_index(a.argmax(),a.shape)
    cand.append({'score':float(a[y,x]),'box':[int(x+roi[0]),int(y+roi[1]),int(x+roi[0]+w),int(y+roi[1]+h)]})
  cand.sort(key=lambda x:x['score'],reverse=True)
  out[crop]=cand[:20]
  print('REFINE',crop,json.dumps(cand[:5]),flush=True)
 return out

def exact_tests():
 out={}
 boxes={'148_scan051_r_arrow.png':[631,1612,1023,1745], '148_scan053_cela.png':[356,1627,1032,1714]}
 for crop,box in boxes.items():
  cim=Image.open(ROOT/'result/crops'/crop).convert('RGB');target=np.array(cim).astype(np.int16)
  sim=Image.open(ROOT/'source/SP83_C13_148+149_scans'/(PAGES[crop]+'.jpg')).convert('RGB')
  options={'plain':sim.crop(box),'autocontrast':ImageOps.autocontrast(sim.crop(box)),'global_autocontrast':ImageOps.autocontrast(sim).crop(box)}
  cand=[]
  for label,im in options.items():
   for resname,res in [('LANCZOS',Image.Resampling.LANCZOS),('BICUBIC',Image.Resampling.BICUBIC)]:
    enlarged=im.resize(cim.size,res)
    filters=[('none',None),('sharp_1.2_105_3',ImageFilter.UnsharpMask(1.2,105,3)),('sharp_1_120_3',ImageFilter.UnsharpMask(1,120,3)),('sharp_default',ImageFilter.UnsharpMask()),('sharp_1.5_120_3',ImageFilter.UnsharpMask(1.5,120,3)),('sharp_1_100_3',ImageFilter.UnsharpMask(1,100,3)),('sharp_1.2_120_3',ImageFilter.UnsharpMask(1.2,120,3))]
    for fn,filt in filters:
     o=enlarged if filt is None else enlarged.filter(filt)
     ar=np.asarray(o,dtype=np.int16);delta=ar-target
     row={'contrast':label,'resampling':resname,'filter':fn,'rmse':float(np.sqrt(np.mean(delta.astype(np.float64)**2))),'max_error':int(abs(delta).max()),'pixel_channels_equal':int(np.count_nonzero(delta==0)),'total_pixel_channels':int(delta.size),'exact':bool(np.array_equal(ar,target))}
     cand.append(row)
  cand.sort(key=lambda x:x['rmse']);out[crop]={'box':box,'candidates':cand[:7]}
  print('EXACT',crop,json.dumps(cand[:3]),flush=True)
 return out

def verify_recovered():
 from io import BytesIO
 from datetime import datetime,timezone
 settings={
  '148_scan051_r_arrow.png':{'box':[631,1612,1023,1745],'size':[2300,780],'unsharp_percent':115,'expected_sha256':'8e2b293dd11a0885753829af6c173972011316585b729c01d4ba254f3bbcb4f8'},
  '148_scan053_cela.png':{'box':[356,1627,1032,1714],'size':[3000,386],'unsharp_percent':105,'expected_sha256':'48b4b965daa68af816ff1f7ec3c9530cc3c8ef14f86605ae2f2ba78e3ad3caa5'}
 }
 report={'method':'Grayscale normalized cross-correlation for location/scale; integer-box refinement; exact in-memory RGB recreation against every retained target channel. No OCR. No crop image written.','rectangle_convention':'Pillow original-pixel (left,top,right,bottom), right and bottom exclusive','generated_utc':datetime.now(timezone.utc).isoformat(),'geometry_status':'exactly recovered for both files','files':[]}
 for crop,setting in settings.items():
  source=Path('source/SP83_C13_148+149_scans')/(PAGES[crop]+'.jpg')
  target=Path('result/crops')/crop
  original_bytes=(ROOT/target).read_bytes();sha=hashlib.sha256(original_bytes).hexdigest()
  assert sha==setting['expected_sha256'],(crop,'retained file changed')
  sim=Image.open(ROOT/source).convert('RGB')
  cropped=sim.crop(setting['box'])
  local_auto=ImageOps.autocontrast(cropped)
  global_auto=ImageOps.autocontrast(sim).crop(setting['box'])
  assert np.array_equal(cropped,local_auto)
  assert np.array_equal(cropped,global_auto)
  enlarged=cropped.resize(tuple(setting['size']),Image.Resampling.LANCZOS)
  recreated=enlarged.filter(ImageFilter.UnsharpMask(radius=1.2,percent=setting['unsharp_percent'],threshold=3))
  existing=Image.open(ROOT/target).convert('RGB')
  a=np.asarray(recreated);b=np.asarray(existing)
  assert np.array_equal(a,b),(crop,'pixel mismatch')
  memory=BytesIO();recreated.save(memory,format='PNG')
  assert hashlib.sha256((ROOT/target).read_bytes()).hexdigest()==sha
  report['files'].append({'crop':str(target),'source':str(source),'source_sha256':hashlib.sha256((ROOT/source).read_bytes()).hexdigest(),'crop_sha256_before':sha,'crop_sha256_after':sha,'box':setting['box'],'native_crop_size':list(cropped.size),'output_size':list(existing.size),'rotation_degrees':0,'resampling':'Pillow Image.Resampling.LANCZOS','sharpen':{'type':'Pillow ImageFilter.UnsharpMask','radius':1.2,'percent':setting['unsharp_percent'],'threshold':3},'contrast_note':'Local-crop and full-source ImageOps.autocontrast both act as identity on this crop. Their historical use cannot be distinguished from no autocontrast; all reproduce the same pixels.','verification':{'mode':'RGB','all_channels_compared':int(a.size),'pixel_mismatches':0,'maximum_absolute_channel_error':0,'raw_rgb_sha256':hashlib.sha256(a.tobytes()).hexdigest(),'in_memory_png_bytes_equal_to_retained_file':memory.getvalue()==original_bytes},'geometry_status':'exact: zero pixel error with recovered integer source box','historical_generator_status':'not found; transform recovered from pixels rather than asserted as surviving history'})
 return report

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--search',action='store_true',help='Repeat the coarse/refined geometry searches before verifying. Never writes images.')
 args=ap.parse_args()
 if args.search:
  for label,fun in [('coarse',coarse),('refine',refine),('exact_tests',exact_tests)]:
   (ROOT/'result/qa'/('early_small_crop_recovery_'+label+'.json')).write_text(json.dumps(fun(),indent=2)+'\n')
 report=verify_recovered()
 (ROOT/'result/qa/early_small_crop_recovery.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report,indent=2))
