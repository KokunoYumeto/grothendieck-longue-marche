from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json
here=Path(__file__).resolve().parent
for item in json.loads((here/'crop_log.json').read_text()):
    im=ImageOps.autocontrast(Image.open(item['source']).crop(item['box']))
    w=item['output_width']; im=im.resize((w,round(im.height*w/im.width)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.5,percent=130,threshold=3))
    im.save(here/Path(item['file']).name)
