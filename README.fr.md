# Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981) : transcription

Une transcription diplomatique en LaTeX du manuscrit de Grothendieck *La Longue Marche à travers la théorie de
Galois*, faite à partir des scans des archives de l'Université de Montpellier (cotes 140-1 à 140-4, 1 588 pages
numérisées), avec des notes de recherche sur les mathématiques. C'est une édition initiale : tout le manuscrit est
transcrit en premier jet, et la transcription est en cours de vérification page par page sur les scans.

[English version](README.md)

Une traduction anglaise de tout le manuscrit (245 unités, 1 588 scans ; traduite par IA) se trouve dans `translation/en/` et, en un seul PDF, dans les [Releases](../../releases) : voir la section [English translation](README.md#english-translation) du README anglais.

## Contenu

- **Lecteurs composés, version de travail (14 novembre 2026)** : cinq lecteurs et deux maîtres annotés, en français et
  en anglais (diplomatique, corrigé avec apparat, texte de lecture), dans les
  [Releases](../../releases/tag/lm-readers-working-draft-2026-11-14). Le texte est établi ; la composition est en cours
  d'achèvement, et une édition achevée les remplacera.
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

## Comment cette transcription est faite : les défaillances de l'IA, et ce que nous faisons contre elles

Tout ce qui se trouve ici a été produit par IA. La transcription par IA de mathématiques manuscrites échoue de façons
connues : elle lit ce que l'argument demande au lieu de ce qui est écrit, laisse tomber de petits signes, fait
disparaître les mots barrés et les abréviations, confond les lettres qui se ressemblent et lit le même signe de façons
différentes d'une page à l'autre. La méthode est construite contre ces défaillances, et nous mesurons ce qui reste.

- **Source.** Les scans des cotes 140-1 à 140-4 (1 588 pages), à la résolution des archives, contraste renforcé et
  bandeau d'en-tête retiré.
- **Premier passage, à l'aveugle :** GPT-6 Astra (ChatGPT, mode Pro), un lot à la fois, sans accès à aucune autre
  transcription. Les lectures douteuses sont marquées `\unsure{…}`, les mots barrés `\deleted{…}`, les insertions et
  les notes marginales comme telles ; les corrections des mathématiques vont dans les notes de recherche, jamais dans le
  texte. Le prompt a été révisé chaque fois qu'un nouveau type d'erreur est apparu.
- **Second passage, contre l'encre :** Claude Opus 5.5 (effort max), lot par lot, chaque ligne contre les scans en
  pleine résolution et contre les transcriptions antérieures comme témoins (Carmona avec Künzer ; l'édition provisoire
  du Centre d'études grothendieckiennes ; la table des matières de Grothendieck lui-même). Chaque modification est
  consignée avec sa justification et un degré de confiance, et les endroits qui restent ouverts restent marqués. La
  section « État » dit où en est ce passage.
- **Ce que trouve le second passage.** Sur cinq lots mesurés, il a fait 286 modifications sur 4 926 mots, dont 64 de
  confiance élevée (1,3 pour 100 mots), et dans chaque lot 7 à 10 corrections qui changent les mathématiques (une
  hypothèse rétablie, Γ lu pour T, « épi » pour « iso »), le plus souvent non marquées au premier passage. C'est
  pourquoi aucun lot ne s'en passe.
- **Vérifications par échantillon.** Des vérifications indépendantes, mot à mot, d'échantillons de huit pages contre
  les scans comptent les erreurs pour 100 mots et fixent des règles pour les lots suivants, par exemple une table de
  notations commune quand des pages sont lues en flux parallèles.
- **Anglais :** GPT-6.1 Sol (effort de raisonnement max, API OpenAI, niveau Flex), à partir de notre transcription
  française.
- Détails, taux mesurés et coûts : [methodology/METHODOLOGY.md](methodology/METHODOLOGY.md).

## État (12 novembre 2026)

- Premier jet : les 1 588 scans.
- Seconde passe, où chaque ligne est vérifiée sur les images d'archive en pleine résolution et collationnée avec les
  transcriptions antérieures citées plus bas là où elles couvrent le texte : les 1 588 scans (116 paquets, cotes
  140-1 à 140-4), avec 4 890 changements au premier jet et 3 636 endroits non résolus, qui restent marqués. Les
  dossiers `transcription/` et `notes/` de l'édition et les lecteurs provisoires la contiennent pour la cote 140-2,
  scans 21–30 et 101–575, et la cote 140-3, scans 1–130 ; le reste est sous [`raw/`](raw/README.md) (section
  « Second passes ») jusqu'à la prochaine version.
- Les transcriptions antérieures couvrent la première partie du manuscrit (§§ 1–37, cote 140-2). Pour la cote 140-3,
  elles n'offrent que les titres de sections de la table des matières : les images décident donc seules de la lecture.
- Dans les paquets vérifiés, la seconde passe a changé la lecture du premier jet à environ 2 endroits sur 100 mots
  (en comptant les changements faits avec une confiance haute ou moyenne), et environ la moitié de ces endroits ne
  portaient pas de marque de doute. Il faut s'attendre à des erreurs de ce genre dans les paquets pas encore vérifiés.
  Les endroits que les images ne tranchent pas restent marqués.

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

## Considérations sur les droits

**Les textes de Grothendieck.** Les droits appartiennent à ses ayants droit ; ses textes sont protégés jusqu'à la fin
de 2084. L'Université de Montpellier publie les scans de ses papiers mathématiques (https://grothendieck.umontpellier.fr/archives-grothendieck/) avec l'accord de ses
ayants droit. Nous ne détenons aucune licence de ses ayants droit et ne revendiquons aucun droit sur ses textes.

**Éditions et transcriptions antérieures.** D'autres ont édité ou transcrit avant nous des parties de ces papiers :
- *Les Dérivateurs* : l'édition électronique de M. Künzer, J. Malgoire et G. Maltsiniotis (https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html) ;
- *La Longue Marche à travers la théorie de Galois* : le tome 1, édité par J. Malgoire (Université Montpellier II,
  1995), et les transcriptions de M. Carmona avec M. Künzer (https://agrothendieck.github.io/) ;
- *Pursuing Stacks* : la transcription de M. Carmona (https://arxiv.org/abs/2111.01000), qu'il a versée au domaine public sous CC0, et
  l'édition de G. Maltsiniotis, *À la poursuite des champs*, vol. I (SMF, 2022) ;
- les transcriptions du Centre d'études grothendieckiennes (https://csg.igrothendieck.org/), qui déclare les publier avec le consentement des
  ayants droit.

À part cette déclaration, aucune de ces éditions n'indique détenir une licence des ayants droit, et une transcription ne
donne à son auteur aucun droit sur le texte transcrit. Nous faisons le même travail avec l'IA pour l'ensemble des
archives : pour rendre le tout disponible en LaTeX modifiable, avec des traductions, et comme une seconde lecture à côté
de celles qui existent. Ce n'est ni une revendication d'antériorité ou de supériorité, ni une revendication de droits
que nous ne détenons pas. Si les éditeurs d'une édition antérieure préfèrent que nous retirions ce que nous avons fondé
sur leur travail, pour que le leur reste seul, nous le ferons par courtoisie.

**Œuvres ayant une édition autorisée.** Lorsqu'une œuvre a une édition publiée avec l'autorisation des ayants droit,
comme *Récoltes et Semailles* (Gallimard, 2022), nous ne la reproduisons ni ne la traduisons ; tout au plus écrivons-nous
notre propre commentaire sur ses mathématiques.

**Textes d'autres auteurs.** Nous ne transcrivons ou ne traduisons les textes d'autres auteurs que lorsque les ayants
droit, ou l'institution qui détient ces textes, les ont rendus publiquement accessibles pour l'étude. Par exemple les
carnets de Daniel Quillen, que le Clay Mathematics Institute a numérisés et mis à la disposition de la communauté
mathématique (https://www.claymath.org/online-resources/quillen-notebooks/), et les exposés du Séminaire Bourbaki et les rédactions de Bourbaki que Grothendieck a
réutilisés ou gardés parmi ses propres notes, que l'Université publie avec ses papiers. C'est notre lecture de bonne
foi, non une revendication de droits. Si vous détenez des droits sur l'un de ces textes et vous y opposez, ouvrez une
issue GitHub et nous le retirerons.

---

[Sponsor this work](https://github.com/sponsors/KokunoYumeto)
