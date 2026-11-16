# Grothendieck's five-point diagram (cote 148, scan 31), drawn

Pictures and an interactive model of the finite diagram that Grothendieck sketched for the fundamental groupoid of
the moduli space of five points on the sphere (Montpellier archive, cote 148, scan 31). Our research run EXIT_TOWER
(GPT-6 Astra, ChatGPT Pro mode), checkpoint 28, made the diagram explicit: 542 objects in nine orbits of the
relabelling group S5, and 1,620 arrows in fourteen families (statements B.12, B.16, B.17 and B.25 of the run).
These are the run's claims and have not been refereed yet.

Open `page/index.html` in a browser: seven plates, with the images and the loop beside it in `page/img` and
`page/video`. The interactive model (Plate IV) loads three.js from cdnjs.

## The plates

| Plate | What it shows |
|---|---|
| I | The whole diagram in 3D, laid out from its own symmetry and seen down its five-fold axis; an oblique view; a loop that turns it by 72 degrees, which maps it onto itself. |
| II | The three most symmetric ways to put five labelled points on a sphere: regular pentagon (I10, 12 labellings), triangular bipyramid (I6, 20), square pyramid (I4, 30). |
| III | The pattern: the nine kinds of object and the fourteen arrow families, with their counts. The manuscript's "14 orbites" counts the families; there are 16 orbits (B.12). |
| IV | A model you can turn: tap an object to see its five-point structure and its arrows; switch families and kinds on and off. |
| V | The same graph laid out by Graphviz (sfdp), which knows nothing of the symmetry. |
| VI | The exact connectivity of the rank-k pieces of the tower (D.45), with the bound proposed in our prompt and refuted by the run (D.6). |
| VII | Drinfeld's three relations defining the Grothendieck-Teichmüller group, as bracketed trees with coloured strands; the pentagon is one of the twelve real pentagons whose centres are the I10 objects. |

Every picture uses one colour per labelled point: 0 rose, 1 amber, 2 green, 3 blue, 4 violet.

## How the layout is made

1. `tools/s5_action.py`, `tools/s5_action2.py`: the run's data file `b_diagram.json` (EXIT_TOWER checkpoint 28,
   `code/b_diagram.json`, in `raw/`) gives each object as a coset representative. These scripts find, for each kind,
   the stabilizer and the coset convention under which the representatives are canonical; the arrows pin them down
   uniquely. Every one of the 120 relabellings then maps the 1,620 arrows, family by family, onto themselves.
   Result: `data/stabilizers.json` (D5, S3 acting on the poles by its sign, C4, and a double transposition for the
   four C2 kinds, as in the run's table B.16).
2. `tools/spectral.py`, `tools/layout_c5.py`: the eigenvectors of the graph Laplacian come in representations of S5.
   The first four-dimensional one sends the twelve pentagons to the origin (their stabilizer D5 fixes no vector
   there); the first five-dimensional one keeps every kind apart. Its projection onto the fixed line and the
   72-degree plane of the five-cycle 0 -> 1 -> 2 -> 3 -> 4 -> 0 has exact D5 symmetry. Result: `data/layout_c5.json`.
3. `tools/blender_graph.py` (Blender 4.5, Cycles on the GPU): the renders in `renders/` and the loop.
   `tools/blender_fivepoint.py`: Plate II. `tools/make_dot.py`: the Graphviz file `renders/cote148_hairball.dot`.
   `tools/relax_d5.py`: a force relaxation that keeps the D5 symmetry (not used for the plates).

## Credits and licence

Computed and drawn by Claude (Claude Opus 5.5 at effort max), 16-17 November 2026, from the data of the run
EXIT_TOWER (GPT-6 Astra, ChatGPT Pro mode). Tools: Python (numpy), Blender 4.5, Graphviz 16.1.1, three.js r128.
Our pictures, scripts and data files are dedicated to the public domain under CC0 1.0.
