#!/usr/bin/env python3
"""Validate derived membership of every chosen source word, then replay fully.

The comparison uses the actual main-word descriptions passed by the replay,
including its independently reconstructed N generators.  A chosen word must
be a main-generator commutator, or an iterated conjugate of such a word by
main generators.  No chosen generator is admitted merely because its saved
finite permutation belongs to the expected base derived group.
"""
from pathlib import Path
import json
import de_ferrari_sl2_5_derived_replay as replay

records = []
original_stage = replay.replay_stage


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def checked_stage(model, main, perms, kernel, expected_base_order, stem,
                  descriptions, kernel_description, expected_dir, output_dir):
    expected = json.loads((expected_dir/(stem+'.json')).read_text())
    main_words = {canonical(d) for d in descriptions}

    def is_derived_word(description):
        if set(description) == {'commutator'}:
            args = description['commutator']
            return len(args) == 2 and all(canonical(a) in main_words for a in args)
        if set(description) == {'conjugate'}:
            args = description['conjugate']
            return (len(args) == 2 and canonical(args[0]) in main_words and
                    is_derived_word(args[1]))
        return False

    chosen = expected['chosen_base_derived_generator_descriptions']
    assert all(is_derived_word(d) for d in chosen), stem
    records.append({'stage': stem, 'actual_main_word_count': len(descriptions),
                    'chosen_word_count': len(chosen),
                    'all_chosen_words_are_actual_derived_words': True})
    return original_stage(model, main, perms, kernel, expected_base_order, stem,
                          descriptions, kernel_description, expected_dir, output_dir)


if __name__ == '__main__':
    replay.replay_stage = checked_stage
    replay.main()
    assert len(records) == 3
    Path(__file__).with_suffix('.json').write_text(json.dumps(records, indent=2)+'\n')
    print('PASS_ALL_CHOSEN_GENERATORS_HAVE_ACTUAL_DERIVED_SOURCE_EXPRESSIONS', flush=True)
