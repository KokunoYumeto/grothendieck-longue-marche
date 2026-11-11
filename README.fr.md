# Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981) : transcription

Une transcription diplomatique en LaTeX du manuscrit de Grothendieck *La Longue Marche à travers la théorie de
Galois*, faite à partir des scans des archives de l'Université de Montpellier (cotes 140-1 à 140-4, 1 588 pages
numérisées), avec des notes de recherche sur les mathématiques. C'est une édition initiale : tout le manuscrit est
transcrit en premier jet, et la transcription est en cours de vérification page par page sur les scans.

[English version](README.md)

## Contenu

- **Lecteurs provisoires**, un PDF par fichier d'archive, dans les [Releases](../../releases) : cote 140-2 (pages
  1–292 du manuscrit), 140-3 (pages 293–650), 140-4 (pages 650bis–787) et 140-1 (un brouillon). Chaque partie
  utilise le meilleur texte disponible ; [reader/READER_SOURCES.md](reader/READER_SOURCES.md) indique lequel.
- `transcription/` : le LaTeX de chaque paquet de scans (10, 19 ou 20 scans), par cote.
  - `*_first_pass.tex` : le premier jet tel que rendu.
  - `*_first_pass_fixed.tex` : le premier jet après des réparations ciblées (diagrammes et marques illisibles
    refaits, ou balisage LaTeX réparé pour qu'il compile).
  - `*_checked.tex` et `*_changes.md` : le texte après la seconde passe, et le tableau de chaque changement avec ses
    preuves et un degré de confiance.
- `notes/` : pour chaque paquet, l'apparat du premier jet (doutes, abréviations, lisibilité) et ses notes de
  recherche : conjectures et questions de Grothendieck, affirmations qu'il laisse sans preuve, implications qu'il ne
  poursuit pas, et idées propres des modèles, signalées comme telles. `*_notes_checked.md` : les mêmes notes
  vérifiées sur le texte corrigé (gardées, corrigées ou retirées, avec leurs raisons).
- [notes/RESEARCH_TOPICS.md](notes/RESEARCH_TOPICS.md) : une première carte des thèmes du manuscrit et des questions
  que Grothendieck laisse ouvertes, avec les numéros de scan (en anglais).
- `methodology/` : comment la transcription est faite, les prompts utilisés, la liste des paquets et la couverture
  (en anglais).
- [`raw/`](raw/README.md) : résultats de recherche bruts, non revus pour publication (en anglais) : réponses de
  GPT-6 Astra (ChatGPT, mode Pro) à des prompts de recherche sur *La Longue Marche* (schémas en groupes, équation
  des lacets, tour de Teichmüller), premières passes de
  transcription des cotes 146, 147 et 149 des archives, leurs relectures, les prompts avec tout ce qui y était joint,
  et les scripts.

La transcription est diplomatique : le français de Grothendieck, son orthographe, ses abréviations, sa numérotation,
ses ratures, ajouts et notes marginales tels qu'écrits, avec le doute marqué (`\unsure{a|b}`, `\illegible{n}`). Les
mathématiques gardent ses lettres, indices et flèches ; les diagrammes sont composés avec tikz-cd.

## État (9 novembre 2026)

- Premier jet : les 1 588 scans.
- Seconde passe, où chaque ligne est vérifiée sur les images d'archive en pleine résolution et collationnée avec les
  transcriptions antérieures citées plus bas là où elles couvrent le texte : cote 140-2, scans 21–30 et 101–575 ;
  cote 140-3, scans 1–130. Les autres scans (cote 140-2, scans 1–20 et 31–100 ; cote 140-3, scans 131–696 ; cotes
  140-4 et 140-1) n'ont que le premier jet.
- Les transcriptions antérieures couvrent la première partie du manuscrit (§§ 1–37, cote 140-2). Pour la cote 140-3,
  elles n'offrent que les titres de sections de la table des matières : les images décident donc seules de la lecture.
- Dans les paquets vérifiés, la seconde passe a changé la lecture du premier jet à environ 2 endroits sur 100 mots
  (en comptant les changements faits avec une confiance haute ou moyenne), et environ la moitié de ces endroits ne
  portaient pas de marque de doute. Il faut s'attendre à des erreurs de ce genre dans les paquets pas encore vérifiés.
  Les endroits que les images ne tranchent pas restent marqués.

## Comment elle a été faite

La transcription, les corrections, la composition et les notes sont produites par IA.

- Premier jet : ChatGPT Pro (OpenAI), un paquet de scans à la fois, à partir d'images contrastées, sans accès à
  aucune autre transcription. Le paquet 57 (cote 140-2, scans 561–570) a été transcrit par l'API OpenAI (GPT-6
  Astra), à titre d'essai.
- Seconde passe : Claude Opus 5.5 (Anthropic), sur les images d'archive et les transcriptions antérieures.

Détails, taux d'erreur mesurés et coûts : [methodology/METHODOLOGY.md](methodology/METHODOLOGY.md) (en anglais).

## Sources et travaux antérieurs

- Les scans : Université de Montpellier, Institut Montpelliérain Alexander Grothendieck,
  [archives Grothendieck](https://grothendieck.umontpellier.fr/archives-grothendieck/), cotes 140-1 (37 scans),
  140-2 (575), 140-3 (696) et 140-4 (280).
- Transcriptions antérieures, consultées comme témoins lors de la seconde passe et non reproduites ici :
  - l'édition de la première partie par Mateo Carmona, transcrite d'après le tapuscrit, et le texte composé déchiffré
    et transcrit par Mateo Carmona avec la collaboration de Matthias Künzer
    ([agrothendieck.github.io](https://agrothendieck.github.io/)) ;
  - l'édition provisoire du Centre for Grothendieckian Studies (Grothendieck Institute, Mondovì), février 2026 ;
  - la table des matières établie par Grothendieck lui-même, publiée par le Grothendieck Circle.

  Ces textes lisent certains passages autrement que l'encre, et nous aussi ; chaque désaccord est tranché sur le scan.
  Les tableaux `*_changes.md` indiquent où un témoin s'accorde ou diffère.

## Erreurs

Merci de signaler les erreurs par une [issue](../../issues), avec la cote et le numéro de scan.

## Droits

Les droits sur l'œuvre originale appartiennent à son auteur ou à ses représentants ou ayants droit. Pour autant que
nous détenions des droits sur la transcription, la traduction, les corrections et la composition produites par IA,
ils sont placés dans le domaine public sous CC0 1.0. Cette édition est publiée à des fins éducatives et non
lucratives, et nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre
et vous opposez à sa publication ici, ouvrez une issue GitHub et nous la retirerons.

---

[Sponsor this work](https://github.com/sponsors/KokunoYumeto)
