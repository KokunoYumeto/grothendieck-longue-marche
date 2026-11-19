#!/usr/bin/env python3
"""Synthetic-only tests for explicit occurrence-confidence bookkeeping.

No manuscript, witness, context, or committed page/decision data is read here.
Only function definitions from the selected mechanical review.py are loaded;
its module-level source-map initialization is never executed. Integration
fixtures are created beneath TemporaryDirectory and contain invented strings.

Set AUDIT_REVIEW_PATH when testing a staged candidate. Installed beside
review.py, this file can be run directly with ``python3 test_audit_confidence.py``.
"""

import ast
import copy
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import tempfile
import unittest


PAGE = "pages/SYNTHETIC.tex"
DECISION_FILE = "decisions/SYNTHETIC.json"
MACRO = r"\unsure{A|B}"


def load_functions():
    path = Path(os.environ.get("AUDIT_REVIEW_PATH", Path(__file__).with_name("review.py")))
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    namespace = {
        "Path": Path,
        "csv": csv,
        "hashlib": hashlib,
        "json": json,
        "re": re,
    }
    # Literal constants are safe to recover without evaluating imports, paths,
    # source-map loads, calls, or any other module-level expression.
    for node in tree.body:
        if isinstance(node, ast.Assign):
            try:
                value = ast.literal_eval(node.value)
            except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
                continue
            for target in node.targets:
                if isinstance(target, ast.Name):
                    namespace[target.id] = value
    definitions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    exec(compile(ast.Module(body=definitions, type_ignores=[]), str(path), "exec"), namespace)
    for name in (
        "_audit_source_text",
        "_validate_audit_confidence",
        "_unsure_entries",
        "_unsure_confidence_detail",
        "rebuild_doubts",
    ):
        if name not in namespace:
            raise RuntimeError(f"The candidate review.py does not define {name}")
    return namespace


def load_diagnostic_module():
    """Load only the stdlib-only diagnostic module, never review.py itself."""
    path = Path(os.environ.get(
        "AUDIT_DIAGNOSE_PATH", Path(__file__).with_name("diagnose_committed.py")
    ))
    return runpy.run_path(str(path))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def context_for(page_bytes, record=None, decision_file=DECISION_FILE):
    if record is None:
        record = {"decisions": [{"final": MACRO, "confidence": "high"}]}
    return {
        "page_bytes": page_bytes,
        "decision_file": decision_file,
        "record": record,
    }


def occurrence(line=2, column=3, macro=MACRO, confidence="medium", number=1,
               decision_file=DECISION_FILE):
    return {
        "line": line,
        "column": column,
        "macro": macro,
        "confidence": confidence,
        "decision_ref": {"file": decision_file, "number": number},
    }


def document(page_bytes, entries=None, page_file=PAGE):
    if entries is None:
        entries = [occurrence()]
    return {
        "version": 1,
        "pages": {
            page_file: {
                "page_sha256": digest(page_bytes),
                "occurrences": entries,
            }
        },
    }


class AuditConfidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.helpers = load_functions()

    def setUp(self):
        self.page_bytes = ("header\nx " + MACRO + "\n").encode("utf-8")
        self.record = {"decisions": [{"final": MACRO, "confidence": "high"}]}
        self.contexts = {PAGE: context_for(self.page_bytes, copy.deepcopy(self.record))}

    def validate(self, payload=None, contexts=None):
        if payload is None:
            payload = document(self.page_bytes)
        if not isinstance(payload, str):
            payload = json.dumps(payload, ensure_ascii=False)
        return self.helpers["_validate_audit_confidence"](
            payload, self.contexts if contexts is None else contexts
        )

    def entries(self, page_bytes=None):
        text = self.helpers["_audit_source_text"](
            self.page_bytes if page_bytes is None else page_bytes
        )
        entries, notes = self.helpers["_unsure_entries"](text)
        self.assertEqual(notes, [])
        return entries

    def test_exact_override_uses_supplied_confidence_and_reference(self):
        original_contexts = copy.deepcopy(self.contexts)
        index = self.validate()
        self.assertEqual(self.contexts, original_contexts)
        key = (PAGE, 2, 3, MACRO)
        self.assertEqual(set(index), {key})
        self.assertEqual(index[key]["confidence"], "medium")
        self.assertEqual(index[key]["decision_ref"], {"file": DECISION_FILE, "number": 1})
        entries = self.entries()
        baseline = self.helpers["_unsure_confidence_detail"](entries[0], self.record, entries)
        self.assertEqual((baseline["basis"], baseline["confidence"]), ("direct_final", "high"))
        supplied = self.helpers["_unsure_confidence_detail"](
            entries[0], self.record, entries, audit_entries=index, page_file=PAGE
        )
        self.assertEqual(supplied["basis"], "primary_occurrence")
        self.assertEqual(supplied["confidence"], "medium")
        self.assertEqual(supplied["decision_numbers_1_based"], [1])
        self.assertIsNone(supplied["pending_reason"])

    def test_unicode_columns_tabs_and_universal_newlines(self):
        macro = "\\unsure{ A |\n B }"
        raw = "header\r\nα\t \\unsure{ A |\r\n B }\r\n".encode("utf-8")
        ctx = {PAGE: context_for(raw)}
        entry = occurrence(line=2, column=4, macro=macro)
        index = self.validate(document(raw, [entry]), ctx)
        self.assertIn((PAGE, 2, 4, macro), index)
        self.assertEqual(
            self.helpers["_audit_source_text"]("α\r\nβ\rγ\n".encode()), "α\nβ\nγ\n"
        )
        wrong_byte_column = copy.deepcopy(entry)
        wrong_byte_column["column"] = 5
        with self.assertRaises(ValueError):
            self.validate(document(raw, [wrong_byte_column]), ctx)

    def test_absent_and_empty_audit_leave_first_pass_unchanged(self):
        validator = self.helpers["_validate_audit_confidence"]
        self.assertEqual(validator(None, self.contexts), {})
        self.assertEqual(self.validate({"version": 1, "pages": {}}), {})
        entry = self.entries()[0]
        record = {"decisions": [{"final": "C retained", "c": MACRO, "confidence": "low"}]}
        original = self.helpers["_unsure_confidence_detail"](entry, record, [entry])
        self.assertEqual((original["basis"], original["confidence"]), ("c_retained_exact", "low"))
        for index in (None, {}):
            with self.subTest(index=index):
                self.assertEqual(
                    self.helpers["_unsure_confidence_detail"](
                        entry, record, [entry], audit_entries=index, page_file=PAGE
                    ),
                    original,
                )
        with self.assertRaises(ValueError):
            validator("", self.contexts)

    def test_identical_repeated_macro_does_not_receive_another_occurrences_value(self):
        raw = (MACRO + "\n" + MACRO + "\n").encode()
        record = {"decisions": [{"final": "C retained", "c": MACRO, "confidence": "high"}]}
        contexts = {PAGE: context_for(raw, record)}
        index = self.validate(document(raw, [occurrence(line=1, column=1)]), contexts)
        entries = self.entries(raw)
        first, second = [
            self.helpers["_unsure_confidence_detail"](
                entry, record, entries, audit_entries=index, page_file=PAGE
            ) for entry in entries
        ]
        self.assertEqual((first["basis"], first["confidence"]), ("primary_occurrence", "medium"))
        self.assertEqual(second["confidence"], "not assessed")
        self.assertEqual(second["pending_reason"], "ambiguous_retained_c_occurrences")

    def test_distinct_locations_can_hold_distinct_explicit_values(self):
        raw = (MACRO + "\n" + MACRO + "\n").encode()
        entries = [
            occurrence(line=1, column=1, confidence="high"),
            occurrence(line=2, column=1, confidence="low"),
        ]
        index = self.validate(document(raw, entries), {PAGE: context_for(raw)})
        self.assertEqual(index[(PAGE, 1, 1, MACRO)]["confidence"], "high")
        self.assertEqual(index[(PAGE, 2, 1, MACRO)]["confidence"], "low")

    def test_same_text_on_another_page_is_not_an_override_key(self):
        index = self.validate()
        entry = self.entries()[0]
        unresolved_record = {"decisions": [{}]}
        result = self.helpers["_unsure_confidence_detail"](
            entry, unresolved_record, [entry], audit_entries=index, page_file="pages/OTHER.tex"
        )
        self.assertEqual(result["confidence"], "not assessed")
        self.assertNotEqual(result["basis"], "primary_occurrence")

    def test_duplicate_json_keys_are_rejected_at_multiple_depths(self):
        base = json.dumps(document(self.page_bytes))
        block = json.dumps(document(self.page_bytes)["pages"][PAGE])
        duplicate_pages = '{"version":1,"pages":{' + json.dumps(PAGE) + ':' + block + ',' + json.dumps(PAGE) + ':' + block + '}}'
        cases = {
            "root": '{"version":1,"version":1,"pages":{}}',
            "page": duplicate_pages,
            "occurrence": base.replace('"confidence": "medium"', '"confidence": "medium", "confidence": "low"', 1),
            "reference": base.replace('"number": 1', '"number": 1, "number": 1', 1),
        }
        for name, text in cases.items():
            with self.subTest(level=name), self.assertRaises(ValueError):
                self.validate(text)

    def test_duplicate_locations_are_rejected_even_if_values_agree(self):
        for confidence in ("medium", "low"):
            first = occurrence()
            second = occurrence(confidence=confidence)
            with self.subTest(confidence=confidence), self.assertRaises(ValueError):
                self.validate(document(self.page_bytes, [first, second]))

    def test_stale_hash_rejects_unrelated_edit_even_with_same_occurrence(self):
        # Appending text preserves the exact occurrence, line and column. Only
        # the page-version guard distinguishes this from a valid assignment.
        changed = self.page_bytes + b"unrelated synthetic footer\n"
        contexts = {PAGE: context_for(changed)}
        with self.assertRaises(ValueError):
            self.validate(document(self.page_bytes), contexts)

    def test_changed_coordinates_are_not_relocated(self):
        for field in ("line", "column"):
            entry = occurrence()
            entry[field] += 1
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.validate(document(self.page_bytes, [entry]))

    def test_macro_matching_has_no_whitespace_or_reading_fallback(self):
        for macro in (r"\unsure{A |B}", r"\unsure{B|A}", " " + MACRO, MACRO + " ", "A"):
            with self.subTest(macro=macro), self.assertRaises(ValueError):
                self.validate(document(self.page_bytes, [occurrence(macro=macro)]))
        changed_raw = self.page_bytes.replace(b"{A|B}", b"{A |B}")
        # A refreshed page hash must not make a stale macro string acceptable.
        with self.assertRaises(ValueError):
            self.validate(document(changed_raw), {PAGE: context_for(changed_raw)})

    def test_integer_coordinates_reject_booleans_nonintegers_and_nonpositive_values(self):
        for field in ("line", "column"):
            for value in (True, False, 0, -1, 1.0, "2", None):
                item = occurrence()
                item[field] = value
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    self.validate(document(self.page_bytes, [item]))

    def test_reference_number_must_name_an_existing_decision(self):
        for number in (0, -1, True, False, 1.0, "1", None, 2):
            with self.subTest(number=number), self.assertRaises(ValueError):
                self.validate(document(self.page_bytes, [occurrence(number=number)]))
        contexts = {PAGE: context_for(self.page_bytes, {"decisions": [None]})}
        with self.assertRaises(ValueError):
            self.validate(contexts=contexts)

    def test_reference_is_same_page_and_canonical_even_if_other_record_exists(self):
        contexts = copy.deepcopy(self.contexts)
        contexts["pages/OTHER.tex"] = context_for(self.page_bytes, decision_file="decisions/OTHER.json")
        for path in ("decisions/OTHER.json", "decisions/MISSING.json", "../decisions/SYNTHETIC.json", "/tmp/SYNTHETIC.json", "decisions/./SYNTHETIC.json"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.validate(document(self.page_bytes, [occurrence(decision_file=path)]), contexts)

    def test_unknown_or_noncanonical_page_keys_are_rejected(self):
        for page in ("pages/MISSING.tex", "pages/./SYNTHETIC.tex", "pages/../pages/SYNTHETIC.tex", "/tmp/SYNTHETIC.tex", "sources/SYNTHETIC.tex"):
            with self.subTest(page=page), self.assertRaises(ValueError):
                self.validate(document(self.page_bytes, page_file=page))

    def test_forbidden_confidence_values_are_not_coerced(self):
        for value in ("not assessed", "High", "medium ", "certain", "", None, True, 3):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.validate(document(self.page_bytes, [occurrence(confidence=value)]))

    def test_schema_missing_unknown_or_wrongly_typed_fields_are_rejected(self):
        cases = []
        for key in ("version", "pages"):
            item = document(self.page_bytes)
            del item[key]
            cases.append(("missing root " + key, item))
        for version in (True, 0, 2, "1", None):
            item = document(self.page_bytes)
            item["version"] = version
            cases.append(("invalid version " + repr(version), item))
        item = document(self.page_bytes)
        item["unapproved_extra"] = 1
        cases.append(("unknown root key", item))
        item = document(self.page_bytes)
        item["pages"] = []
        cases.append(("pages not object", item))
        for key in ("page_sha256", "occurrences"):
            item = document(self.page_bytes)
            del item["pages"][PAGE][key]
            cases.append(("missing page " + key, item))
        item = document(self.page_bytes)
        item["pages"][PAGE]["unknown"] = 1
        cases.append(("unknown page key", item))
        item = document(self.page_bytes)
        item["pages"][PAGE]["occurrences"] = {}
        cases.append(("occurrences not array", item))
        for key in ("line", "column", "macro", "confidence", "decision_ref"):
            item = document(self.page_bytes)
            del item["pages"][PAGE]["occurrences"][0][key]
            cases.append(("missing occurrence " + key, item))
        item = document(self.page_bytes)
        item["pages"][PAGE]["occurrences"][0]["guess"] = True
        cases.append(("unknown occurrence key", item))
        for reference in ({"file": DECISION_FILE}, {"number": 1}, {"file": DECISION_FILE, "number": 1, "extra": 0}, None, []):
            item = document(self.page_bytes)
            item["pages"][PAGE]["occurrences"][0]["decision_ref"] = reference
            cases.append(("invalid reference shape " + repr(reference), item))
        for name, item in cases:
            with self.subTest(case=name), self.assertRaises(ValueError):
                self.validate(item)

    def test_hash_has_strict_lowercase_hex_shape(self):
        for value in (digest(self.page_bytes).upper(), "0" * 63, "g" * 64, "0" * 64, None, 0):
            item = document(self.page_bytes)
            item["pages"][PAGE]["page_sha256"] = value
            with self.subTest(hash=value), self.assertRaises(ValueError):
                self.validate(item)

    def test_comments_and_verbatim_do_not_create_auditable_occurrences(self):
        raw = ("% " + MACRO + "\n\\begin{verbatim}\n" + MACRO + "\n\\end{verbatim}\n" + MACRO + "\n").encode()
        contexts = {PAGE: context_for(raw)}
        for line, column in ((1, 3), (3, 1)):
            with self.subTest(line=line), self.assertRaises(ValueError):
                self.validate(document(raw, [occurrence(line=line, column=column)]), contexts)
        valid = self.validate(document(raw, [occurrence(line=5, column=1)]), contexts)
        self.assertIn((PAGE, 5, 1, MACRO), valid)

    def test_parser_warning_elsewhere_on_audited_page_blocks_application(self):
        raw = (MACRO + "\n\\unsure{unfinished\n").encode()
        contexts = {PAGE: context_for(raw)}
        with self.assertRaises(ValueError):
            self.validate(document(raw, [occurrence(line=1, column=1)]), contexts)

    def make_rebuild_fixture(self, directory):
        root = Path(directory)
        (root / "pages").mkdir()
        (root / "decisions").mkdir()
        page_bytes = ("header\nx " + MACRO + "\ny \\unsure{C|D}\n").encode()
        (root / PAGE).write_bytes(page_bytes)
        record = {
            "cote": "SYNTHETIC",
            "scan": 1,
            "decisions": [{"final": "C retained", "c": MACRO, "confidence": "low"}],
            "inventory": [],
            "unresolved": "Synthetic fixture only.",
        }
        (root / DECISION_FILE).write_text(json.dumps(record), encoding="utf-8")
        (root / "notation.md").write_text("# Synthetic notation\n\nFixture only.\n", encoding="utf-8")
        namespace = load_functions()
        namespace.update({
            "ROOT": root,
            "PREFIX": "SYNTHETIC",
            "ROWS": [{"cote": "SYNTHETIC", "our_scan": "1", "codex_file": "SYNTHETIC.tex"}],
        })
        return root, namespace, page_bytes, root / "SYNTHETIC_doubts.md"

    @staticmethod
    def rendered_data_rows(text):
        rows = []
        for line in text.splitlines():
            if line.startswith("| SYNTHETIC/1 |"):
                rows.append([cell.strip() for cell in line.strip("|").split("|")])
        return rows

    def test_rebuild_absent_and_empty_file_are_byte_identical(self):
        with tempfile.TemporaryDirectory(prefix="audit-confidence-synthetic-") as directory:
            root, ns, raw, output = self.make_rebuild_fixture(directory)
            protected = {path: path.read_bytes() for path in (root / PAGE, root / DECISION_FILE)}
            first = ns["rebuild_doubts"]()
            baseline = output.read_bytes()
            (root / "audit_confidence.json").write_text('{"version":1,"pages":{}}\n', encoding="utf-8")
            second = ns["rebuild_doubts"]()
            self.assertEqual(output.read_bytes(), baseline)
            self.assertEqual(first["rows"], second["rows"])
            self.assertEqual([x["confidence"] for x in first["rows"]], ["low", "not assessed"])
            for path, data in protected.items():
                self.assertEqual(path.read_bytes(), data)

    def test_rebuild_valid_override_keeps_five_columns_and_uncovered_row_pending(self):
        with tempfile.TemporaryDirectory(prefix="audit-confidence-synthetic-") as directory:
            root, ns, raw, output = self.make_rebuild_fixture(directory)
            (root / "audit_confidence.json").write_text(json.dumps(document(raw)), encoding="utf-8")
            result = ns["rebuild_doubts"]()
            rows = self.rendered_data_rows(output.read_text(encoding="utf-8"))
            self.assertEqual(len(rows), 2)
            self.assertTrue(all(len(row) == 5 for row in rows))
            self.assertEqual([row[-1] for row in rows], ["medium", "not assessed"])
            self.assertEqual(result["rows"][0]["basis"], "primary_occurrence")
            self.assertEqual(result["rows"][1]["confidence"], "not assessed")

    def test_invalid_audit_does_not_overwrite_last_good_doubts(self):
        with tempfile.TemporaryDirectory(prefix="audit-confidence-synthetic-") as directory:
            root, ns, raw, output = self.make_rebuild_fixture(directory)
            saved = b"A previous generated document must survive validation failure.\n"
            output.write_bytes(saved)
            bad = document(raw)
            bad["pages"][PAGE]["page_sha256"] = "0" * 64
            (root / "audit_confidence.json").write_text(json.dumps(bad), encoding="utf-8")
            protected = {path: path.read_bytes() for path in (root / PAGE, root / DECISION_FILE)}
            with self.assertRaises(ValueError):
                ns["rebuild_doubts"]()
            self.assertEqual(output.read_bytes(), saved)
            for path, data in protected.items():
                self.assertEqual(path.read_bytes(), data)

    def make_diagnostic_fixture(self, directory):
        """Create a complete, internally consistent, wholly invented package."""
        root, ns, _, _ = self.make_rebuild_fixture(directory)
        ns["PREFIX"] = root.name
        row = {
            "folder": "SYNTHETIC",
            "cote": "SYNTHETIC",
            "our_scan": "1",
            "their_page": "1",
            "codex_file": "SYNTHETIC.tex",
            "hua_has": "text",
        }
        ns["ROWS"] = [row]
        raw = ("\\scanpage{1}\nx " + MACRO + "\ny \\unsure{C|D}\n").encode()
        (root / PAGE).write_bytes(raw)
        record_path = root / DECISION_FILE
        record = json.loads(record_path.read_text(encoding="utf-8"))
        record.update({
            "sheet_kind": "text",
            "hand": "synthetic",
            "inventory": [["text", "body", "invented fixture"]],
        })
        record["decisions"][0].update({
            "kind": "other",
            "c_changed": False,
            "h_changed": False,
            "place": "synthetic first occurrence",
        })
        record_path.write_text(json.dumps(record), encoding="utf-8")
        (root / "scripts").mkdir()
        review_path = Path(os.environ.get(
            "AUDIT_REVIEW_PATH", Path(__file__).with_name("review.py")
        ))
        (root / "scripts/review.py").write_bytes(review_path.read_bytes())
        (root / "PREAMBLE.tex").write_text(
            "\\newcommand{\\scanpage}[1]{}\n\\newcommand{\\unsure}[1]{#1}\n",
            encoding="utf-8",
        )
        (root / (root.name + "_transcription.tex")).write_text(
            raw.decode().rstrip() + "\n", encoding="utf-8"
        )
        (root / (root.name + "_changes.md")).write_text("Synthetic changes.\n", encoding="utf-8")
        (root / (root.name + "_notes.md")).write_text("Synthetic notes.\n", encoding="utf-8")
        (root / "progress.log").write_text("Synthetic progress fixture.\n", encoding="utf-8")
        (root / "CHECK_EVENTS.tsv").write_text(
            "statement_id\tdate\twho\ttype\toutcome\n", encoding="utf-8"
        )
        page_map = root / "synthetic_page_map.tsv"
        with page_map.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(row), delimiter="\t")
            writer.writeheader()
            writer.writerow(row)
        ns["rebuild_tables"]()
        ns["rebuild_doubts"]()
        return root, ns, raw, page_map

    @staticmethod
    def synthetic_tree_bytes(root):
        return {
            path.relative_to(root).as_posix(): path.read_bytes()
            for path in root.rglob("*") if path.is_file()
        }

    def test_diagnostic_adapter_reports_exact_primary_provenance(self):
        diagnostic = load_diagnostic_module()
        with tempfile.TemporaryDirectory(prefix="audit-adapter-synthetic-") as directory:
            root, ns, raw, page_map = self.make_diagnostic_fixture(directory)
            (root / "audit_confidence.json").write_text(
                json.dumps(document(raw)), encoding="utf-8"
            )
            ns["rebuild_doubts"]()
            before = self.synthetic_tree_bytes(root)
            snapshot = diagnostic["capture"](root, page_map)
            self.assertTrue(snapshot["stable"])
            self.assertEqual(snapshot["raw_content"][PAGE], raw)
            result = diagnostic["audit"](root, snapshot)
            self.assertEqual(result["structural_issues"], [])
            self.assertTrue(result["audit_confidence_file_present"])
            self.assertEqual(result["audit_confidence_entries"], 1)
            self.assertEqual(result["audit_confidence_pages"], 1)
            self.assertEqual(result["confidence_mapping_counts"], {
                "primary_occurrence": 1, "no_matching_record": 1,
            })
            self.assertEqual(result["pending_confidence_rows"], 1)
            self.assertEqual(len(result["primary_confidence_rows"]), 1)
            primary = result["primary_confidence_rows"][0]
            self.assertEqual(primary["scan"], "SYNTHETIC/1")
            self.assertEqual(primary["page_file"], PAGE)
            self.assertEqual((primary["tex_line"], primary["tex_column"]), (2, 3))
            self.assertEqual(primary["macro_sha256"], digest(MACRO.encode()))
            self.assertEqual(primary["confidence"], "medium")
            self.assertEqual(primary["basis"], "primary_occurrence")
            self.assertEqual(primary["decision_ref"], {"file": DECISION_FILE, "number": 1})
            pending = result["pending_confidence"][0]
            self.assertEqual((pending["tex_line"], pending["tex_column"]), (3, 3))
            self.assertEqual(pending["match_status"], "no_matching_record")
            self.assertEqual(self.synthetic_tree_bytes(root), before)

    def test_diagnostic_adapter_absent_and_empty_audit_keep_first_pass(self):
        diagnostic = load_diagnostic_module()
        with tempfile.TemporaryDirectory(prefix="audit-adapter-synthetic-") as directory:
            root, ns, raw, page_map = self.make_diagnostic_fixture(directory)
            output = root / (root.name + "_doubts.md")
            previous_output = output.read_bytes()
            absent = diagnostic["audit"](root, diagnostic["capture"](root, page_map))
            self.assertEqual(absent["structural_issues"], [])
            self.assertFalse(absent["audit_confidence_file_present"])
            self.assertEqual(absent["confidence_mapping_counts"], {
                "c_retained_exact": 1, "no_matching_record": 1,
            })
            (root / "audit_confidence.json").write_text(
                '{"version":1,"pages":{}}\n', encoding="utf-8"
            )
            ns["rebuild_doubts"]()
            empty = diagnostic["audit"](root, diagnostic["capture"](root, page_map))
            self.assertEqual(output.read_bytes(), previous_output)
            self.assertEqual(empty["structural_issues"], [])
            self.assertTrue(empty["audit_confidence_file_present"])
            for result in (absent, empty):
                self.assertEqual(result["audit_confidence_entries"], 0)
                self.assertEqual(result["audit_confidence_pages"], 0)
                self.assertEqual(result["primary_confidence_rows"], [])
            for field in ("confidence_mapping_counts", "pending_confidence", "pending_confidence_rows"):
                self.assertEqual(empty[field], absent[field])

    def test_diagnostic_adapter_invalid_audit_raises_without_report_writes(self):
        diagnostic = load_diagnostic_module()
        with tempfile.TemporaryDirectory(prefix="audit-adapter-synthetic-") as directory:
            root, _, raw, page_map = self.make_diagnostic_fixture(directory)
            stale = document(raw)
            stale["pages"][PAGE]["page_sha256"] = "0" * 64
            cases = {
                "malformed JSON": '{"version":',
                "duplicate JSON key": '{"version":1,"version":1,"pages":{}}',
                "stale hash": json.dumps(stale),
            }
            for case, text in cases.items():
                with self.subTest(case=case):
                    (root / "audit_confidence.json").write_text(text, encoding="utf-8")
                    before = self.synthetic_tree_bytes(root)
                    snapshot = diagnostic["capture"](root, page_map)
                    with self.assertRaises(ValueError):
                        diagnostic["audit"](root, snapshot)
                    self.assertEqual(self.synthetic_tree_bytes(root), before)
                    self.assertFalse((root / "diagnostics").exists())

    def test_referenced_decision_duplicate_keys_block_both_adapters_without_writes(self):
        diagnostic = load_diagnostic_module()
        with tempfile.TemporaryDirectory(prefix="audit-adapter-synthetic-") as directory:
            root, ns, raw, page_map = self.make_diagnostic_fixture(directory)
            output = root / (root.name + "_doubts.md")
            prior_doubts = output.read_bytes()
            (root / "diagnostics").mkdir()
            prior_report = root / "diagnostics/previous_synthetic_report.md"
            report_bytes = b"A previous synthetic diagnostic must remain unchanged.\n"
            prior_report.write_bytes(report_bytes)
            (root / "audit_confidence.json").write_text(
                json.dumps(document(raw)), encoding="utf-8"
            )
            record_path = root / DECISION_FILE
            text = record_path.read_text(encoding="utf-8")
            needle = '"confidence": "low"'
            self.assertEqual(text.count(needle), 1)
            # Conflicting duplicate keys are not resolved by selecting whichever
            # value happens to occur last in the referenced record.
            malformed = text.replace(
                needle, '"confidence": "low", "confidence": "high"', 1
            )
            record_path.write_text(malformed, encoding="utf-8")
            before = self.synthetic_tree_bytes(root)
            with self.assertRaises(ValueError):
                ns["rebuild_doubts"]()
            self.assertEqual(output.read_bytes(), prior_doubts)
            self.assertEqual(self.synthetic_tree_bytes(root), before)
            snapshot = diagnostic["capture"](root, page_map)
            with self.assertRaises(ValueError):
                diagnostic["audit"](root, snapshot)
            self.assertEqual(output.read_bytes(), prior_doubts)
            self.assertEqual(prior_report.read_bytes(), report_bytes)
            self.assertEqual(self.synthetic_tree_bytes(root), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
