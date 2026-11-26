# SR10_156-4-46 — seconde lecture achevée

Les trente pages fournies sont closes. La dernière clôture est datée du 25 novembre 2026 à 19:22:19 UTC ; l'examen codicologique du lot avait été intégré à 19:21:13 UTC.

## Résultats consignés

| Élément | Total final |
|---|---:|
| Pages éditées | 30 |
| Boîtes avec deux lectures et recadrages étroits | 885 |
| Différences courantes entre les lectures | 583 |
| Décisions dans placements.tsv | 606 |
| Remplacements exacts, décision a | 288 |
| Événements CHECK_EVENTS.tsv | 888 |
| Lignes H/C obligatoires couvertes | 636 |
| Marqueurs de doute ou d'illisibilité de C couverts | 484 |
| Recadrages enregistrés dans CROPS.tsv | 1 840 |
| Images du dépôt final de crops | 986 |

Les décisions comprennent les différences ainsi que des constatations supplémentaires faites sur les crops. Les 888 événements couvrent les 885 boîtes et trois identifiants supplémentaires. Ils enregistrent l'usage du contenu comme arrière-plan ; aucune lecture visuelle n'est présentée comme une preuve mathématique vérifiée.

Le journal conserve 42 lignes historiques de clôture concernant 30 pages distinctes. Le dernier décompte historique par page donne 588 différences ; cinq correspondances de présentation, chacune démontrée par ses transformations exactes et conservant sa décision, donnent 583 au décompte courant. Le détail se trouve dans `review/final_difference_counts.tsv` et `review/final_audit_refresh_report.md`. Le journal historique est conservé.

## Fichiers à consulter

- `edited_pages/` : les trente textes, dans l'ordre des scans. Chaque modification est reproduisible depuis le texte fourni par sa ligne exacte de `placements.tsv`.
- `placements.tsv` : décisions, deux lectures, remplacements, observations de l'encre, noms et coordonnées des crops, degré de confiance.
- `second/` : listes de boîtes, premières lectures, lectures aveugles, comparaisons et manifestes ; les lectures complémentaires sont conservées dans leurs sous-dossiers.
- `SR10_156-4-46_notes.md` : table de notation, lectures incertaines, particularités conservées et examen codicologique de l'ensemble.
- `SR10_156-4-46_hand_log.md` : observations de main, de frappe et de notation, avec leurs limites locales.
- `review/codicology_leaves.tsv` : trente feuillets, numérotations, couches visibles, lacunes et 84 comparaisons avec les trois feuillets disponibles suivants ; le raccord 45/080→45/063 est enregistré en plus.
- `review/codicology_sources.tsv` : références, adresses, empreintes SHA-256, pages consultées et limites des sources extérieures.
- `review/46_scan024_arrow_counts_blind.tsv`, `review/46_scan025_arrow_counts_blind.tsv` et `review/46_scan026_b15_fresh_blind.tsv` : contrôles aveugles supplémentaires des tirets et surfrappes.
- `crops/CROPS.tsv` : inventaire permettant de recouper les images depuis les scans fournis.
- `review/final_prepackage_verification.json`, `review/final_progress_events_check.json` et les tableaux de clôture : contrôles de reconstruction, de couverture et de traçabilité.
- `scripts/` et les scripts de `review/` : procédures exécutées. Les rapports intermédiaires datés et les états historiques demeurent présents ; les rapports portant `final` décrivent l'état achevé.

## Dépôt des images

`SR10_156-4-46_crops.zip` contient 986 JPEG en niveaux de gris, qualité 85, et leurs manifestes. Il pèse 135 084 233 octets, sans réduction de dimensions. La sélection conserve tous les composants et crops cités des changements, ainsi que les crops des lectures laissées douteuses. Les autres crops sont reconstructibles à partir de leurs rectangles enregistrés.

Les scans fournis, les témoins inchangés, le préambule fourni et les sources extérieures téléchargées ne sont pas recopiés dans les archives livrées. La lecture des scans n'a utilisé aucun OCR ni couche de texte ; aucun TeX n'a été compilé.

## Vérification reproductible

Le vérificateur `scripts/verify_final.py` accepte `--root` pour désigner le dossier extrait, ainsi que `--main-zip`, `--crop-zip`, `--strict` et `--expect-pages 30`. Il vérifie les substitutions contre les textes originaux disponibles dans le dossier de travail et les empreintes des membres des archives. Les entrées fournies doivent être remises dans le dossier `sources/` pour rejouer la vérification depuis une extraction indépendante.

La preuve de couverture détaillée reste dans `review/final_target_closure_status.tsv`, `review/finished_mandatory_closure_check.tsv` et leurs rapports associés. Les limites documentaires conservées comprennent l'identification externe du tapuscrit bleu n° 371, les paires recto/verso et les mains non attribuées, ainsi que la page 62 française de Serre : le lemme et sa preuve ont été lus dans la traduction anglaise aux pages imprimées 53–54.
