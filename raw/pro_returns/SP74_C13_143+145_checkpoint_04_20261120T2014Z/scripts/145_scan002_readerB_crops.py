from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
root=Path("/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work")
im=Image.open("/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/145_scan002.jpg").convert("RGB")
items={
"cancelled_header":((262,24,1555,150),3200,0),
"cancelled_diagram":((480,134,1165,407),3200,0),
"triangle_cancel":((390,385,671,493),2600,0),
"h_definition":((742,526,1584,782),3200,0),
"square":((880,797,1250,1013),2800,0),
"nb1":((256,1043,1655,1365),3200,0),
"margin_u":((29,1144,357,1424),2600,-28),
"nb2":((238,1362,1605,1775),3200,0),
"margin_pi":((123,1625,341,1855),2600,0),
"margin_equations":((300,1848,903,2187),3200,0),
"h_paragraph":((690,1691,1642,2079),3200,0),
"hn_definition":((716,2075,1657,2240),3200,0),
"last_line":((362,2221,1658,2345),3200,0),
}
for name,(box,width,angle) in items.items():
    out=ImageOps.autocontrast(im.crop(box))
    if angle:
        out=out.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor="white")
    out=out.resize((width,round(out.height*width/out.width)),Image.Resampling.LANCZOS)
    out=out.filter(ImageFilter.UnsharpMask(radius=1.6,percent=145,threshold=2))
    out.save(root/"crops"/f"145_scan002_readerB_{name}.png")
print(f"Saved {len(items)} uniquely named color-preserving crops.")
