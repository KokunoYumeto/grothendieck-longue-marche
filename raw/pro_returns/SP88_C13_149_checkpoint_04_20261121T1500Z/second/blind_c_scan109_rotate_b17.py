from PIL import Image
from pathlib import Path
root=Path('/workspace/scratch/0cab6a548abb/edition/crops')
im=Image.open(root/'149_scan109_second_b17.png')
im.rotate(-40,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white').save(root/'149_scan109_second_b17_inspect_rotated.png')
