import sys, os
from PIL import Image, ImageOps, ImageDraw

IMG = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\img"
OUT = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\work_LM_P042"

# composite name -> list of (label, file, box, scale, rotate)
SPECS = {
 "c01": [
  ("411a margin", "scan411_a", (20, 300, 280, 490), 3.0, 0),
  ("411a margin rot", "scan411_a", (20, 300, 280, 490), 3.0, -32),
  ("411a sous Gamma", "scan411_a", (300, 640, 900, 760), 2.0, 0),
 ],
 "c02": [
  ("411b psi line", "scan411_b", (840, 720, 1640, 885), 2.0, 0),
  ("411b induisant + display", "scan411_b", (300, 860, 1150, 1010), 1.8, 0),
 ],
 "c03": [
  ("411b N subset", "scan411_b", (880, 560, 1640, 745), 2.0, 0),
  ("412a l1", "scan412_a", (300, 60, 1100, 170), 2.0, 0),
 ],
 "c04": [
  ("412a margin rot", "scan412_a", (10, 560, 420, 1000), 2.2, -38),
 ],
 "c05": [
  ("412a lines 9-12", "scan412_a", (300, 760, 1660, 1215), 1.15, 0),
 ],
 "c06": [
  ("412b cond1", "scan412_b", (300, 280, 1670, 460), 1.15, 0),
  ("412b bottom", "scan412_b", (300, 760, 1670, 1110), 1.15, 0),
 ],
 "c07": [
  ("412b margin rot", "scan412_b", (10, 600, 620, 1255), 1.8, -42),
 ],
 "c08": [
  ("413a l4-5", "scan413_a", (300, 400, 1660, 575), 1.15, 0),
  ("413a revision", "scan413_a", (300, 860, 1680, 1262), 1.15, 0),
 ],
 "c09": [
  ("413b donnee", "scan413_b", (300, 540, 1600, 660), 1.15, 0),
  ("413b Pts", "scan413_b", (300, 1040, 1650, 1240), 1.15, 0),
 ],
 "c10": [
  ("414a l1", "scan414_a", (300, 55, 1050, 135), 2.0, 0),
  ("414a l4", "scan414_a", (300, 360, 1100, 435), 2.0, 0),
  ("414a display", "scan414_a", (440, 570, 1360, 760), 1.6, 0),
 ],
 "c11": [
  ("414 margin rot", "scan414", (0, 520, 450, 1520), 1.5, -58),
 ],
 "c12": [
  ("414a bottom", "scan414_a", (300, 740, 1670, 1262), 1.15, 0),
 ],
 "c13": [
  ("414b top", "scan414_b", (280, 0, 1680, 330), 1.12, 0),
  ("414b mid", "scan414_b", (280, 320, 1680, 700), 1.12, 0),
 ],
 "c14": [
  ("414b bottom", "scan414_b", (300, 680, 1680, 1262), 1.12, 0),
 ],
 "c15": [
  ("415a cond4", "scan415_a", (300, 540, 1680, 900), 1.12, 0),
  ("415a del top", "scan415_a", (300, 990, 1680, 1262), 1.12, 0),
 ],
 "c16": [
  ("415b del", "scan415_b", (300, 0, 1680, 880), 1.0, 0),
 ],
 "c17": [
  ("415b bottom", "scan415_b", (300, 860, 1680, 1262), 1.15, 0),
 ],
 "c18": [
  ("416a top", "scan416_a", (300, 15, 1680, 240), 1.15, 0),
  ("416a top left x2", "scan416_a", (300, 15, 1050, 140), 2.0, 0),
 ],
 "c19": [
  ("416a diagram", "scan416_a", (300, 400, 1500, 760), 1.3, 0),
 ],
 "c20": [
  ("416a bottom", "scan416_a", (300, 760, 1680, 1262), 1.15, 0),
 ],
 "c21": [
  ("416b top", "scan416_b", (300, 0, 1680, 700), 1.15, 0),
 ],
 "c22": [
  ("416b bottom", "scan416_b", (300, 700, 1680, 1262), 1.15, 0),
 ],
 "c23": [
  ("417a diagram", "scan417_a", (200, 100, 1500, 330), 1.25, 0),
  ("417a text", "scan417_a", (300, 380, 1680, 760), 1.15, 0),
 ],
 "c24": [
  ("417a text2", "scan417_a", (300, 700, 1680, 1262), 1.15, 0),
 ],
 "c25": [
  ("418a (a)", "scan418_a", (300, 1030, 1680, 1262), 1.15, 0),
  ("418b (a)", "scan418_b", (250, 0, 1680, 450), 1.12, 0),
 ],
 "c26": [
  ("418b (b)", "scan418_b", (250, 500, 1680, 900), 1.12, 0),
 ],
 "c27": [
  ("419a sys", "scan419_a", (250, 170, 1680, 480), 1.12, 0),
  ("419a pts", "scan419_a", (250, 580, 1680, 830), 1.12, 0),
 ],
 "c28": [
  ("419b left", "scan419_b", (0, 300, 1000, 760), 1.6, 0),
 ],
 "c29": [
  ("419b right", "scan419_b", (1100, 280, 1680, 980), 2.0, 0),
 ],
 "c30": [
  ("420a top", "scan420_a", (300, 150, 1680, 470), 1.15, 0),
  ("420a mid", "scan420_a", (300, 480, 1680, 820), 1.15, 0),
 ],
 "c31": [
  ("420b top", "scan420_b", (250, 0, 1680, 330), 1.12, 0),
  ("420b bottom", "scan420_b", (250, 780, 1680, 1262), 1.12, 0),
 ],
}

def prep(f, box, scale, rot):
    im = Image.open(os.path.join(IMG, f + ".jpg")).convert("L")
    c = im.crop(box)
    c = ImageOps.autocontrast(c, cutoff=1)
    if scale != 1.0:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255, resample=Image.BICUBIC)
    return c

def build(name):
    parts = []
    for (lab, f, box, scale, rot) in SPECS[name]:
        c = prep(f, box, scale, rot)
        strip = Image.new("L", (c.width, 24), 200)
        ImageDraw.Draw(strip).text((4, 5), lab, fill=0)
        parts.append(strip)
        parts.append(c)
    W = max(p.width for p in parts)
    H = sum(p.height for p in parts)
    comp = Image.new("L", (W, H), 255)
    y = 0
    for p in parts:
        comp.paste(p, (0, y))
        y += p.height
    comp.save(os.path.join(OUT, name + ".png"))
    print(name, comp.size)

if __name__ == "__main__":
    names = sys.argv[1:] or list(SPECS)
    for n in names:
        build(n)
