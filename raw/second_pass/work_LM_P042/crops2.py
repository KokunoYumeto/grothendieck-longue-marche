import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import crops as C

C.SPECS.clear()
C.SPECS.update({
 "d01": [
  ("412a margin rot x3", "scan412_a", (20, 600, 390, 900), 3.0, -38),
 ],
 "d02": [
  ("412a commune des G_gn ou des", "scan412_a", (820, 840, 1320, 940), 2.5, 0),
  ("412a G_a a une", "scan412_a", (840, 1010, 1320, 1110), 2.5, 0),
  ("412a l1 nb quelc", "scan412_a", (700, 60, 1500, 160), 1.8, 0),
 ],
 "d03": [
  ("412b bottom left", "scan412_b", (300, 770, 1000, 1110), 2.0, 0),
 ],
 "d04": [
  ("412b bottom right", "scan412_b", (980, 760, 1670, 1110), 2.0, 0),
 ],
 "d05": [
  ("412b margin low rot", "scan412_b", (10, 880, 620, 1255), 2.2, -42),
 ],
 "d06": [
  ("413a La condition (n)", "scan413_a", (840, 900, 1660, 1000), 1.9, 0),
  ("a 413a la cat. des (catégorie)", "scan413_a", (330, 300, 640, 380), 2.0, 0),
  ("b 413a inserted ext/cat", "scan413_a", (420, 470, 640, 560), 2.5, 0),
  ("c 414a le gr. cat.", "scan414_a", (900, 1040, 1240, 1110), 2.5, 0),
 ],
 "d07": [
  ("d 414b lie(s) par le groupe cat.", "scan414_b", (300, 395, 900, 470), 2.2, 0),
  ("e 415a cat above l'op.", "scan415_a", (900, 680, 1350, 800), 2.5, 0),
  ("f 416a deux groupes cat", "scan416_a", (1100, 1140, 1600, 1215), 2.2, 0),
 ],
 "d08": [
  ("g 419b admissible ext.", "scan419_b", (380, 505, 720, 575), 2.5, 0),
  ("h 420 cat above profini", "scan420", (1380, 1080, 1620, 1170), 2.5, 0),
  ("i 416a act. ext.", "scan416_a", (860, 70, 1160, 125), 2.5, 0),
  ("j 413b action ext. admissible", "scan413_b", (1000, 330, 1450, 410), 2.0, 0),
 ],
 "d09": [
  ("414b de G')", "scan414_b", (600, 0, 950, 110), 2.5, 0),
  ("414b decrit com.", "scan414_b", (330, 175, 600, 265), 2.5, 0),
  ("414b que si a VP", "scan414_b", (280, 1020, 1100, 1262), 1.8, 0),
 ],
 "d10": [
  ("414 margin low rot", "scan414", (0, 1050, 340, 1460), 2.5, -58),
 ],
 "d11": [
  ("416a top right", "scan416_a", (1150, 15, 1680, 150), 2.5, 0),
  ("416a qui n'est pas la composee", "scan416_a", (310, 800, 900, 910), 2.5, 0),
 ],
 "d12": [
  ("416a qui ... exterieurement", "scan416_a", (1150, 1080, 1680, 1185), 2.5, 0),
  ("416b hom ... pi -> pi' qui", "scan416_b", (600, 130, 1450, 230), 1.9, 0),
 ],
 "d13": [
  ("416b centralisateur L", "scan416_b", (300, 360, 950, 480), 2.4, 0),
  ("416b centralisateur R", "scan416_b", (950, 360, 1600, 480), 2.4, 0),
 ],
 "d14": [
  ("416b pour tout autom", "scan416_b", (600, 470, 1600, 560), 1.6, 0),
  ("416b u de pi associe", "scan416_b", (300, 560, 1600, 650), 1.2, 0),
  ("416b On avait oublie", "scan416_b", (300, 650, 1000, 740), 2.0, 0),
 ],
 "d15": [
  ("416b dans un hom de", "scan416_b", (900, 990, 1500, 1080), 2.5, 0),
  ("417a diagram middle", "scan417_a", (680, 150, 1200, 245), 3.0, 0),
 ],
 "d16": [
  ("419a B subscript", "scan419_a", (850, 610, 1110, 700), 3.0, 0),
  ("419a l'un", "scan419_a", (250, 690, 520, 790), 3.0, 0),
  ("420 groupe a lacets", "scan420", (980, 1090, 1620, 1180), 2.2, 0),
 ],
 "d17": [
  ("420b (G -> N_a(pi))", "scan420_b", (1100, 190, 1620, 275), 2.5, 0),
  ("420b unique de G", "scan420_b", (550, 1040, 950, 1120), 2.5, 0),
  ("420b pi'!", "scan420_b", (300, 1160, 760, 1262), 2.5, 0),
 ],
})

if __name__ == "__main__":
    for n in (sys.argv[1:] or list(C.SPECS)):
        C.build(n)
