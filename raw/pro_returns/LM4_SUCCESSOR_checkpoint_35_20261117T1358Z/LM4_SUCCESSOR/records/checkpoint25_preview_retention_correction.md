# Authored component-preview retention correction

The final packaging audit found an inherited exclusion for authored
component PDFs ending in _check.pdf and several named review PDFs.
It also found two new authored failed-layout PDFs that the generic DE
third-party-copy heuristic would misclassify because their matching
TeX snapshots use different names. These files document the research.

The checkpoint25 packager now retains all authored check/review PDFs,
including the explicit B118_initial_spacing.pdf and
B122_initial_layout.pdf exceptions. Third-party full source copies,
user-provided attachment duplicates and regenerable runtime caches
remain excluded with their separately stated reasons. The previous
packager and estimator text are preserved in this directory; all earlier
archives remain unchanged. Earlier excluded authored previews still
present locally are included at their exact original paths for the
first time in checkpoint25. This change preserves additional bytes;
it does not omit or alter any previously archived logical entry.

The size estimate is rerun under exactly the revised inclusion rules
before the one scheduled capture. No extra ZIP is created.
