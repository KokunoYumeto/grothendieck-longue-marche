#!/usr/bin/env python3
"""Synthetic-only regression tests for the conservative TeX context checker.

This suite never reads manuscript pages, records, witnesses, scans, or context.
It loads the checker code and AST-selected pure helpers from review.py, then
passes invented strings directly to analyze_text. No diagnostic runner is used.

Optional overrides: MATH_CONTEXT_CHECKER_PATH and MATH_CONTEXT_REVIEW_PATH.
Run with PYTHONDONTWRITEBYTECODE=1 to avoid creating bytecode caches.
"""

from pathlib import Path
import os
import runpy
import unittest
from unittest import mock


CHECKER_PATH = Path(os.environ.get(
    "MATH_CONTEXT_CHECKER_PATH",
    str(Path(__file__).with_name("check_tex_math_context.py")),
))
REVIEW_PATH = Path(os.environ.get(
    "MATH_CONTEXT_REVIEW_PATH",
    str(Path(__file__).with_name("review.py")),
))


class MathContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        checker = runpy.run_path(str(CHECKER_PATH))
        cls.analyze = staticmethod(checker["analyze_text"])
        cls.helpers = checker["load_helpers"](REVIEW_PATH)

    def check(self, source):
        result = self.analyze(source, self.helpers)
        self.assertIsInstance(result, dict)
        for key in ("targets", "findings", "notes"):
            self.assertIsInstance(result[key], list)
        return result

    @staticmethod
    def tokens(result):
        return [item["token"] for item in result["findings"]]

    def assertUncertain(self, source):
        result = self.check(source)
        self.assertEqual(result["findings"], [], result)
        self.assertTrue(result["notes"], "Unclassified coverage needs an explicit note")
        return result

    def test_commands_outside_editorial_targets_are_not_reported(self):
        result = self.check(r"plain \Lambda_a and \to; \unsure{ordinary words}")
        self.assertEqual(result["findings"], [])
        self.assertEqual(len(result["targets"]), 1)

    def test_text_targets_warn_for_obvious_math_commands(self):
        result = self.check(r"\unsure{\Lambda} and \deleted{\to}")
        self.assertEqual(self.tokens(result), [r"\Lambda", r"\to"])
        self.assertEqual([f["target"] for f in result["findings"]], ["unsure", "deleted"])

    def test_unicode_coordinates_are_character_positions(self):
        result = self.check("π\né \\unsure{\\Lambda}\n")
        self.assertEqual(len(result["findings"]), 1)
        finding = result["findings"][0]
        self.assertEqual(
            {k: finding[k] for k in ("line", "column", "target_line", "target_column")},
            {"line": 2, "column": 11, "target_line": 2, "target_column": 3},
        )

    def test_explicit_math_delimiters_protect_targets(self):
        for opening, closing in (("$", "$"), ("$$", "$$"), (r"\(", r"\)"), (r"\[", r"\]")):
            with self.subTest(opening=opening):
                result = self.check(opening + r"\unsure{\Lambda_a}" + closing)
                self.assertEqual(result["findings"], [])
                self.assertEqual(len(result["targets"]), 1)
                self.assertIs(result["targets"][0]["math_at_entry"], True)

    def test_ensuremath_works_around_and_inside_targets(self):
        for source in (
            r"\ensuremath{\unsure{\Lambda_a}}",
            r"\unsure{\ensuremath{\Lambda_a}}",
            r"\deleted{\ensuremath\Lambda}",
        ):
            with self.subTest(source=source):
                self.assertEqual(self.check(source)["findings"], [])

    def test_math_alphabet_does_not_establish_math_mode(self):
        result = self.check(r"\unsure{\mathrm{A}\alpha}")
        self.assertEqual(self.tokens(result), [r"\mathrm", r"\alpha"])

    def test_known_text_wrappers_override_math(self):
        for command in (
            "text", "mbox", "hbox", "textbf", "textit", "emph",
            "margin", "diagram", "figure", "illegible",
        ):
            with self.subTest(command=command):
                result = self.check(r"\(" + "\\" + command + r"{\unsure{\Lambda}}\)")
                self.assertEqual(self.tokens(result), [r"\Lambda"])
                self.assertIs(result["targets"][0]["math_at_entry"], False)

    def test_text_wrappers_with_dimensions_and_optional_arguments(self):
        for wrapper in (
            r"\parbox[t][2em][s]{3em}",
            r"\raisebox{1em}[2em][3em]",
            r"\rotatebox[origin=c]{10}",
            r"\scalebox{1}[2]",
            r"\resizebox{3em}{2em}",
            r"\makebox[3em][l]",
            r"\shortstack[l]",
        ):
            with self.subTest(wrapper=wrapper):
                result = self.check("$" + wrapper + r"{\deleted{\Lambda}}$")
                self.assertEqual(self.tokens(result), [r"\Lambda"])

    def test_nested_text_and_math_overrides_are_scoped(self):
        result = self.check(r"\ensuremath{\text{\unsure{\Lambda \ensuremath{\alpha}}}}")
        self.assertEqual(self.tokens(result), [r"\Lambda"])
        result = self.check(r"\unsure{{\ensuremath{\Lambda}}\beta}")
        self.assertEqual(self.tokens(result), [r"\beta"])

    def test_custom_inherited_wrappers_preserve_caller_mode(self):
        for command in ("handwritten", "inserted", "underline", "phantom"):
            body = r"\unsure{" + "\\" + command + r"{\Lambda}}"
            with self.subTest(command=command, mode="text"):
                self.assertEqual(self.tokens(self.check(body)), [r"\Lambda"])
            with self.subTest(command=command, mode="math"):
                self.assertEqual(self.check("$" + body + "$")["findings"], [])

    def test_alternatives_can_have_different_local_modes(self):
        result = self.check(r"\unsure{$\alpha$|\beta}")
        self.assertEqual(self.tokens(result), [r"\beta"])

    def test_outer_math_environments_establish_math(self):
        for environment in ("math", "displaymath", "equation", "align*", "gather", "multline"):
            with self.subTest(environment=environment):
                source = "\\begin{" + environment + r"}\unsure{\Lambda_a}\end{" + environment + "}"
                self.assertEqual(self.check(source)["findings"], [])

    def test_text_environment_inside_math_is_classified_as_text(self):
        source = r"\begin{equation}\begin{minipage}{3em}\unsure{\Lambda}\end{minipage}\end{equation}"
        self.assertEqual(self.tokens(self.check(source)), [r"\Lambda"])

    def test_math_required_environment_does_not_silently_fix_text_mode(self):
        in_math = r"$\unsure{\begin{matrix}\alpha\end{matrix}}$"
        in_text = r"\unsure{\begin{matrix}\alpha\end{matrix}}"
        self.assertEqual(self.check(in_math)["findings"], [])
        self.assertIn(r"\begin{matrix}", self.tokens(self.check(in_text)))

    def test_nested_targets_do_not_duplicate_a_token_finding(self):
        result = self.check(r"\unsure{a\deleted{\Lambda}}")
        self.assertEqual(len(result["targets"]), 2)
        self.assertEqual(self.tokens(result), [r"\Lambda"])
        finding = result["findings"][0]
        self.assertEqual(finding["target"], "deleted")
        self.assertEqual((finding["target_line"], finding["target_column"]), (1, 10))

    def test_unknown_macro_arguments_around_targets_are_unclassified(self):
        result = self.assertUncertain(r"\mystery{\unsure{\Lambda_a}}")
        self.assertEqual(len(result["targets"]), 1)
        self.assertIsNone(result["targets"][0]["math_at_entry"])

    def test_unknown_macro_arguments_inside_targets_have_coverage_notes(self):
        self.assertUncertain(r"\unsure{\mystery{\Lambda_a}}")

    def test_unknown_optional_and_required_arguments_are_unclassified(self):
        result = self.assertUncertain(r"\mystery[\unsure{\Lambda_a}]{\deleted{\beta_b}}")
        self.assertEqual(len(result["targets"]), 2)

    def test_unknown_group_does_not_hide_later_known_text(self):
        result = self.check(r"\unsure{\mystery{\alpha_a}\beta}")
        self.assertEqual(self.tokens(result), [r"\beta"])
        self.assertTrue(result["notes"])

    def test_tikz_environments_around_targets_are_unclassified(self):
        for environment in ("tikzpicture", "tikzcd"):
            with self.subTest(environment=environment):
                source = "\\begin{" + environment + r"}\unsure{\Lambda_a}\end{" + environment + "}"
                self.assertUncertain(source)

    def test_tikz_environments_inside_targets_have_coverage_notes(self):
        for environment in ("tikzpicture", "tikzcd"):
            with self.subTest(environment=environment):
                source = r"\unsure{\begin{" + environment + r"}\Lambda_a\end{" + environment + "}}"
                self.assertUncertain(source)

    def test_raw_script_characters_only_warn_in_known_text(self):
        result = self.check(r"\unsure{a_b^c}")
        self.assertEqual(self.tokens(result), ["_", "^"])
        self.assertTrue(all(f["kind"] == "math script character" for f in result["findings"]))
        self.assertEqual(self.check(r"$\unsure{a_b^c}$")["findings"], [])
        self.assertUncertain(r"\mystery{\unsure{a_b^c}}")

    def test_escaped_delimiters_scripts_and_braces_keep_their_meaning(self):
        result = self.check(r"\unsure{a\_b\^c \$ \{\Lambda\}}")
        self.assertEqual(self.tokens(result), [r"\Lambda"])
        self.assertEqual(len(result["targets"]), 1)
        # Two backslashes make a control symbol, leaving the following '_' live.
        self.assertEqual(self.tokens(self.check(r"\unsure{a\\_b}")), ["_"])

    def test_comments_verbatim_and_definitions_are_not_active_targets(self):
        source = (
            "% \\unsure{\\Lambda}\n"
            r"\verb|\unsure{\Lambda}|" + "\n"
            r"\verb*+\deleted{\beta}+" + "\n"
            r"\begin{verbatim}\unsure{\Lambda}\end{verbatim}" + "\n"
            r"\newcommand{\example}{\unsure{\Lambda}}" + "\n"
            r"\def\sample{\deleted{\beta}}" + "\n"
            r"\deleted{ordinary text}"
        )
        result = self.check(source)
        self.assertEqual(result["findings"], [])
        self.assertEqual(len(result["targets"]), 1)
        self.assertEqual(result["targets"][0]["line"], 7)

    def test_comment_with_a_delimiter_does_not_change_mode(self):
        source = "\\unsure{% $ \\Lambda\n\\beta}"
        result = self.check(source)
        self.assertEqual(self.tokens(result), [r"\beta"])
        self.assertEqual((result["findings"][0]["line"], result["findings"][0]["column"]), (2, 1))

    def test_unmatched_closing_delimiters_do_not_cascade_flags(self):
        for source in (r"\unsure{\)\Lambda_a}", r"\unsure{\]\Lambda_a}"):
            with self.subTest(source=source):
                self.assertUncertain(source)

    def test_conflicting_dollar_delimiters_do_not_cascade_flags(self):
        self.assertUncertain(r"\unsure{$a$$\Lambda_a}")

    def test_nested_conflicting_delimiters_do_not_restore_false_certainty(self):
        for source in (
            r"\unsure{$a\(\alpha\)$\Lambda_a}",
            r"\unsure{$a\[\alpha\]$\Lambda_a}",
        ):
            with self.subTest(source=source):
                self.assertUncertain(source)

    def test_unmatched_environment_close_does_not_cascade_flags(self):
        self.assertUncertain(r"\unsure{\end{equation}\Lambda_a}")

    def test_unbalanced_target_is_not_guessed(self):
        result = self.assertUncertain(r"\unsure{\Lambda")
        self.assertEqual(result["targets"], [])

    def test_analysis_performs_no_file_access(self):
        with mock.patch("builtins.open", side_effect=AssertionError("unexpected file access")), \
             mock.patch.object(Path, "read_text", side_effect=AssertionError("unexpected file access")), \
             mock.patch.object(Path, "read_bytes", side_effect=AssertionError("unexpected file access")):
            result = self.analyze(r"\unsure{\Lambda}", self.helpers)
        self.assertEqual(self.tokens(result), [r"\Lambda"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
