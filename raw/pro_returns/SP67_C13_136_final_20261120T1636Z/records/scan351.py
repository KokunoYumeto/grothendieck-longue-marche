{'scan': 351,
 'decisions': [{'id': 'M0867',
                'cote': '136',
                'scan': '351',
                'decision': 'first',
                'reading': '\\uline{y}',
                'what the ink shows': 'A distinct horizontal stroke extends beneath the y, beyond the descender, in '
                                      'the lower matrix.',
                'crop': 'page',
                'confidence': 'high'}],
 'changes': [],
 'inventory': [{'kind': 'text',
                'position': 'heading in upright reading orientation',
                'first_words_or_objects': 'Non-Abelian periods on smooth manifolds',
                'hand': 'typewriter',
                'sheet_kind': 'typescript'},
               {'kind': 'drawing',
                'position': 'under heading',
                'first_words_or_objects': 'five separate underline strokes',
                'hand': 'another unnamed hand',
                'sheet_kind': 'typescript'},
               {'kind': 'text',
                'position': 'first paragraph',
                'first_words_or_objects': 'We can find from the d-formulae',
                'hand': 'typewriter',
                'sheet_kind': 'typescript'},
               {'kind': 'text',
                'position': 'second paragraph',
                'first_words_or_objects': 'For example suppose the model',
                'hand': 'typewriter',
                'sheet_kind': 'typescript'},
               {'kind': 'display',
                'position': 'middle',
                'first_words_or_objects': 'three integrals; footnote 1',
                'hand': 'typewriter',
                'sheet_kind': 'typescript'},
               {'kind': 'text',
                'position': 'third paragraph',
                'first_words_or_objects': 'The first two periods',
                'hand': 'typewriter',
                'sheet_kind': 'typescript'},
               {'kind': 'display',
                'position': 'lower',
                'first_words_or_objects': 'upper triangular matrix',
                'hand': 'typewriter',
                'sheet_kind': 'typescript'},
               {'kind': 'drawing',
                'position': 'matrix',
                'first_words_or_objects': 'two large enclosing parentheses and underline below y',
                'hand': 'another unnamed hand',
                'sheet_kind': 'typescript'},
               {'kind': 'drawing',
                'position': 'above footnote',
                'first_words_or_objects': 'horizontal separator',
                'hand': 'another unnamed hand',
                'sheet_kind': 'typescript'},
               {'kind': 'text',
                'position': 'footnote',
                'first_words_or_objects': '1 These iterated integrals',
                'hand': 'typewriter',
                'sheet_kind': 'typescript'},
               {'kind': 'text',
                'position': 'original-image foot / upright upper right',
                'first_words_or_objects': '352',
                'hand': 'another unnamed hand',
                'sheet_kind': 'typescript'}],
 'note': 'An upside-down English typescript headed ‘Non-Abelian periods on smooth manifolds’, with manuscript '
         'enclosing parentheses, underlines and separator, plus the archive number 352. Authorship is not identified '
         'on this leaf. H has no transcription. Every typed line is retained, including ingegrals and the blank after '
         '‘homology invariants of’; no missing gamma is supplied. The only original doubt, the underline beneath '
         'matrix y, is clear in the native half. The sheet discusses iterated periods for a model with dy=x1 wedge x2 '
         'and a triangular matrix group, and its footnote mentions Chen. No outside source was consulted. A direct '
         'concatenation calculation gives, with A=int omega1, B=int omega2, J=int(int omega1)omega2 and C=int eta-J: '
         'J12=J1+J2+A1 B2, hence C12=C1+C2-A1 B2. The displayed upper-triangular matrices have z12=z1+z2+x1 y2, so the '
         'identification x=A, y=B, z=-C gives that matrix law. The prose does not specify a sign convention for '
         'identifying its third period with z; it has not been silently changed. Homotopy invariance is recorded as a '
         'manuscript assertion, not independently proved here. No date is written.\n'
         '\n'
         'Second reading: Reread both upright views of the originally upside-down typescript. Every sentence, '
         'integral, matrix entry and footnote agrees with the consolidated text. Confirmed the five title underlines, '
         'handwritten matrix parentheses, separate underline beneath y, footnote separator, spelling ingegrals and the '
         'unfilled blank after homology invariants of. No authorship attribution is inferred, and H remains absent. No '
         'further transcription change.',
 'hand': ['On this typescript, a short separate underline lies below the matrix y; it is not just the descender. This '
          'is not evidence for a habit of Grothendieck’s hand.',
          'The scan is upside down relative to its typescript; the handwritten number 352 follows the original scan '
          'orientation.'],
 'notation': [('underlined matrix y', 'Separate underline visible; not normalized away.'),
              ('rho-images', 'Typed Greek rho, distinct from the baseline p used for the base point.')],
 'abbr': [],
 'checks': [{'statement_id': '351.concatenation',
             'date': '2026-11-20 15:21:39 UTC',
             'who': 'GPT-6 Astra Pro; current configured effort; run 2026-11-20',
             'type': 'computation or formal certificate',
             'outcome': 'Splitting the iterated integral over gamma1 followed by gamma2 gives J12=J1+J2+A1B2 and '
                        'C12=C1+C2-A1B2; the matrix law agrees under z=-C, x=A, y=B. This checks the sign convention '
                        'conditionally, not homotopy invariance.'},
            {'statement_id': '351.homotopy-invariance',
             'date': '2026-11-20 15:21:39 UTC',
             'who': 'GPT-6 Astra Pro; current configured effort; run 2026-11-20',
             'type': 'carried as background without fault found',
             'outcome': 'Typescript assertion retained; no independent proof undertaken.'}],
 'unresolved': []}
