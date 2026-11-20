#!/usr/bin/env python3
"""Replay all 67 root-authored crop recipes for cote 12, scan 070.

Default/--metadata-only validates the embedded recipe snapshot without image
imports, source-file reads, output-directory creation, or rendering. Actual
rendering requires --render and --destination outside the deliverable folder.
The two original recipe JSON byte streams are embedded with SHA-256 provenance,
so replay does not depend on the unbundled work/ files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from crop_metadata import TRANSFORM_ORDER, validate_crop_metadata

PAGE_KEY = 'B12-01_12_scan070'
OUTPUT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCAN_ROOT = OUTPUT_ROOT.parent / 'source' / 'SP02_CW_10+12_scans'
SOURCE_DOCUMENTS = [{'path': 'work/crops12_070.json', 'bytes': 9489, 'sha256': '83e730d17db96890df74e4c0813ad56e81b7f0cfc8b646de75c9ef88521aa752', 'raw_json': '[\n  {\n    "id": "heading",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      235,\n      138,\n      1087,\n      232\n    ],\n    "scale": 6,\n    "rotation": 0\n  },\n  {\n    "id": "Les",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      592,\n      176,\n      681,\n      226\n    ],\n    "scale": 18,\n    "rotation": 0\n  },\n  {\n    "id": "Rinsert",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      866,\n      144,\n      918,\n      197\n    ],\n    "scale": 22,\n    "rotation": 0\n  },\n  {\n    "id": "condition",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      1400,\n      171,\n      1665,\n      224\n    ],\n    "scale": 12,\n    "rotation": 0\n  },\n  {\n    "id": "pourvucancel",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      608,\n      239,\n      1035,\n      297\n    ],\n    "scale": 13,\n    "rotation": 0\n  },\n  {\n    "id": "coprof",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      521,\n      384,\n      784,\n      438\n    ],\n    "scale": 16,\n    "rotation": 0\n  },\n  {\n    "id": "Sn",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      537,\n      458,\n      601,\n      521\n    ],\n    "scale": 20,\n    "rotation": 0\n  },\n  {\n    "id": "CohMac",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      539,\n      523,\n      704,\n      578\n    ],\n    "scale": 16,\n    "rotation": 0\n  },\n  {\n    "id": "regulier",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      514,\n      592,\n      714,\n      647\n    ],\n    "scale": 15,\n    "rotation": 0\n  },\n  {\n    "id": "normalRn",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      520,\n      663,\n      743,\n      729\n    ],\n    "scale": 17,\n    "rotation": 0\n  },\n  {\n    "id": "normal",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      519,\n      741,\n      666,\n      793\n    ],\n    "scale": 16,\n    "rotation": 0\n  },\n  {\n    "id": "integre",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      520,\n      810,\n      690,\n      861\n    ],\n    "scale": 17,\n    "rotation": 0\n  },\n  {\n    "id": "reduit",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      522,\n      881,\n      689,\n      931\n    ],\n    "scale": 16,\n    "rotation": 0\n  },\n  {\n    "id": "vii_viii",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      599,\n      961,\n      919,\n      1021\n    ],\n    "scale": 13,\n    "rotation": 0\n  },\n  {\n    "id": "condinsert",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      964,\n      1,\n      1629,\n      58\n    ],\n    "scale": 8,\n    "rotation": 0\n  },\n  {\n    "id": "bquice",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1425,\n      40,\n      1665,\n      96\n    ],\n    "scale": 17,\n    "rotation": 0\n  },\n  {\n    "id": "quiinsert",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      243,\n      82,\n      329,\n      117\n    ],\n    "scale": 22,\n    "rotation": 0\n  },\n  {\n    "id": "verifiee",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      325,\n      110,\n      500,\n      158\n    ],\n    "scale": 20,\n    "rotation": 0\n  },\n  {\n    "id": "toutcancel",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      598,\n      109,\n      781,\n      159\n    ],\n    "scale": 24,\n    "rotation": 0\n  },\n  {\n    "id": "unregulier",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1071,\n      107,\n      1336,\n      153\n    ],\n    "scale": 14,\n    "rotation": 0\n  },\n  {\n    "id": "casinsert",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      811,\n      143,\n      1522,\n      190\n    ],\n    "scale": 10,\n    "rotation": 0\n  },\n  {\n    "id": "Nagata",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      570,\n      181,\n      708,\n      228\n    ],\n    "scale": 17,\n    "rotation": 0\n  },\n  {\n    "id": "gata",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      81,\n      198,\n      186,\n      243\n    ],\n    "scale": 22,\n    "rotation": 0\n  },\n  {\n    "id": "egale",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1448,\n      181,\n      1666,\n      224\n    ],\n    "scale": 14,\n    "rotation": 0\n  },\n  {\n    "id": "ivvvi",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      929,\n      249,\n      1201,\n      304\n    ],\n    "scale": 17,\n    "rotation": 0\n  },\n  {\n    "id": "dansv",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1435,\n      250,\n      1658,\n      300\n    ],\n    "scale": 15,\n    "rotation": 0\n  },\n  {\n    "id": "viB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      276,\n      321,\n      392,\n      373\n    ],\n    "scale": 17,\n    "rotation": 0\n  },\n  {\n    "id": "catenaire",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1130,\n      322,\n      1326,\n      370\n    ],\n    "scale": 22,\n    "rotation": 0\n  },\n  {\n    "id": "faiedge",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1565,\n      318,\n      1683,\n      371\n    ],\n    "scale": 20,\n    "rotation": 0\n  },\n  {\n    "id": "marchervi",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      467,\n      389,\n      563,\n      443\n    ],\n    "scale": 17,\n    "rotation": 0\n  },\n  {\n    "id": "japonais",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1256,\n      390,\n      1683,\n      446\n    ],\n    "scale": 12,\n    "rotation": 0\n  },\n  {\n    "id": "univcat",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      249,\n      459,\n      529,\n      515\n    ],\n    "scale": 15,\n    "rotation": 0\n  },\n  {\n    "id": "remheading",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      245,\n      552,\n      1081,\n      606\n    ],\n    "scale": 9,\n    "rotation": 0\n  },\n  {\n    "id": "remii",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      309,\n      622,\n      855,\n      674\n    ],\n    "scale": 10,\n    "rotation": 0\n  },\n  {\n    "id": "remrefs",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      244,\n      687,\n      922,\n      746\n    ],\n    "scale": 10,\n    "rotation": 0\n  },\n  {\n    "id": "remiicancel",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      320,\n      682,\n      431,\n      745\n    ],\n    "scale": 22,\n    "rotation": 0\n  },\n  {\n    "id": "remiii",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      315,\n      755,\n      1009,\n      817\n    ],\n    "scale": 10,\n    "rotation": 0\n  },\n  {\n    "id": "suppR",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      901,\n      837,\n      951,\n      893\n    ],\n    "scale": 24,\n    "rotation": 0\n  },\n  {\n    "id": "ABcancel",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1396,\n      835,\n      1540,\n      888\n    ],\n    "scale": 24,\n    "rotation": 0\n  },\n  {\n    "id": "RA",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      243,\n      905,\n      333,\n      962\n    ],\n    "scale": 22,\n    "rotation": 0\n  },\n  {\n    "id": "SpecBSpecA",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      868,\n      902,\n      1203,\n      963\n    ],\n    "scale": 16,\n    "rotation": 0\n  },\n  {\n    "id": "Rgeo",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      242,\n      981,\n      526,\n      1033\n    ],\n    "scale": 17,\n    "rotation": 0\n  },\n  {\n    "id": "ilenest",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      542,\n      975,\n      885,\n      1030\n    ],\n    "scale": 18,\n    "rotation": 0\n  },\n  {\n    "id": "Specdeleted",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1027,\n      976,\n      1329,\n      1032\n    ],\n    "scale": 18,\n    "rotation": 0\n  },\n  {\n    "id": "Betant",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1331,\n      977,\n      1683,\n      1034\n    ],\n    "scale": 15,\n    "rotation": 0\n  },\n  {\n    "id": "Arappelons",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      246,\n      1035,\n      579,\n      1086\n    ],\n    "scale": 13,\n    "rotation": 0\n  },\n  {\n    "id": "RB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      601,\n      1036,\n      698,\n      1091\n    ],\n    "scale": 22,\n    "rotation": 0\n  },\n  {\n    "id": "tirer",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1206,\n      1033,\n      1335,\n      1086\n    ],\n    "scale": 24,\n    "rotation": 0\n  },\n  {\n    "id": "lastref",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1330,\n      1034,\n      1588,\n      1088\n    ],\n    "scale": 14,\n    "rotation": 0\n  },\n  {\n    "id": "archive",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      27,\n      1062,\n      114,\n      1129\n    ],\n    "scale": 20,\n    "rotation": 0\n  }\n]\n'}, {'path': 'work/fine12_070.json', 'bytes': 3240, 'sha256': 'd735341f273910a78ddcbf7a6b4d0fcf6d04e4d5cee5a049550eab16b1a0ca0e', 'raw_json': '[\n  {\n    "id": "catcellB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1203,\n      315,\n      1253,\n      377\n    ],\n    "scale": 28,\n    "rotation": 0\n  },\n  {\n    "id": "hcontrolA",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      586,\n      522,\n      632,\n      579\n    ],\n    "scale": 28,\n    "rotation": 0\n  },\n  {\n    "id": "ncontrolA",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      523,\n      735,\n      563,\n      797\n    ],\n    "scale": 28,\n    "rotation": 0\n  },\n  {\n    "id": "tircellB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      1247,\n      1030,\n      1281,\n      1090\n    ],\n    "scale": 30,\n    "rotation": 0\n  },\n  {\n    "id": "toutcellsB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      611,\n      104,\n      701,\n      166\n    ],\n    "scale": 26,\n    "rotation": 0\n  },\n  {\n    "id": "queB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      692,\n      104,\n      781,\n      169\n    ],\n    "scale": 26,\n    "rotation": 0\n  },\n  {\n    "id": "NagatafullB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      487,\n      177,\n      646,\n      233\n    ],\n    "scale": 22,\n    "rotation": 0\n  },\n  {\n    "id": "gatalastB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      144,\n      193,\n      181,\n      247\n    ],\n    "scale": 30,\n    "rotation": 0\n  },\n  {\n    "id": "insertplaceB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      712,\n      5,\n      1655,\n      246\n    ],\n    "scale": 5,\n    "rotation": 0\n  },\n  {\n    "id": "quiplaceB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      238,\n      78,\n      544,\n      163\n    ],\n    "scale": 10,\n    "rotation": 0\n  },\n  {\n    "id": "firstrefA",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      246,\n      240,\n      606,\n      297\n    ],\n    "scale": 12,\n    "rotation": 0\n  },\n  {\n    "id": "parrefsB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      245,\n      36,\n      950,\n      91\n    ],\n    "scale": 9,\n    "rotation": 0\n  },\n  {\n    "id": "list1A",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      385,\n      380,\n      512,\n      578\n    ],\n    "scale": 8,\n    "rotation": 0\n  },\n  {\n    "id": "list2A",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      385,\n      592,\n      512,\n      797\n    ],\n    "scale": 8,\n    "rotation": 0\n  },\n  {\n    "id": "list3A",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      385,\n      806,\n      520,\n      938\n    ],\n    "scale": 9,\n    "rotation": 0\n  },\n  {\n    "id": "brownmarkA",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_a.jpg",\n    "box": [\n      1441,\n      151,\n      1486,\n      193\n    ],\n    "scale": 22,\n    "rotation": 0\n  },\n  {\n    "id": "gataextraB",\n    "source": "SP02_CW_10+12_scans/B12-01_12_scan070_b.jpg",\n    "box": [\n      139,\n      187,\n      218,\n      258\n    ],\n    "scale": 28,\n    "rotation": 0\n  }\n]\n'}]


def recipe_snapshot() -> list[dict]:
    recipes = []
    ids, filenames = set(), set()
    for document in SOURCE_DOCUMENTS:
        raw = document['raw_json'].encode('utf-8')
        if len(raw) != document['bytes'] or hashlib.sha256(raw).hexdigest() != document['sha256']:
            raise ValueError('Embedded source JSON differs from its captured provenance.')
        values = json.loads(document['raw_json'])
        if not isinstance(values, list):
            raise ValueError('Embedded source recipes must be lists.')
        for crop in values:
            validate_crop_metadata(crop)
            normalized = re.sub(r'[^A-Za-z0-9_.+-]+', '_', crop['id'])
            if crop['id'] in ids or normalized in filenames:
                raise ValueError('Duplicate crop ID or normalized output filename.')
            if '..' in Path(crop['source']).parts:
                raise ValueError('Parent traversal is prohibited in crop sources.')
            ids.add(crop['id']); filenames.add(normalized)
            recipes.append(crop)
    if len(recipes) != 67:
        raise ValueError('The captured page-070 snapshot must contain exactly 67 crops.')
    return recipes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--metadata-only', action='store_true', help='Validate embedded geometry only; this is the default.')
    mode.add_argument('--render', action='store_true', help='Explicitly read attached source images and render every captured recipe.')
    parser.add_argument('--scan-root', type=Path, default=DEFAULT_SCAN_ROOT,
                        help='Known scan directory; used only for rendering.')
    parser.add_argument('--destination', type=Path,
                        help='Required with --render; must be outside the deliverable folder.')
    args = parser.parse_args(argv)
    if args.render and args.destination is None:
        parser.error('--render requires --destination')
    if not args.render and args.destination is not None:
        parser.error('--destination is used only with --render')
    recipes = recipe_snapshot()
    encoded = json.dumps(recipes, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    result = {
        'page': PAGE_KEY, 'recipe_count': len(recipes),
        'recipe_counts_by_source': [len(json.loads(d['raw_json'])) for d in SOURCE_DOCUMENTS],
        'recipe_snapshot_sha256': hashlib.sha256(encoded).hexdigest(),
        'source_documents': [{k: d[k] for k in ('path', 'bytes', 'sha256')} for d in SOURCE_DOCUMENTS],
        'transform_order': list(TRANSFORM_ORDER),
        'mode': 'render' if args.render else 'metadata-only',
        'geometry_metadata_valid': True,
        'pixel_extent_bounds_checked': False,
        'images_opened': False,
    }
    if args.render:
        destination = args.destination.expanduser().resolve()
        output_root = OUTPUT_ROOT.resolve()
        if destination == output_root or output_root in destination.parents:
            parser.error('--destination must be outside the deliverable folder')
        # Import the image renderer only after the explicit render gate.
        from render_crops import render_crop
        result['crops'] = [render_crop(crop, args.scan_root, destination, PAGE_KEY) for crop in recipes]
        result['images_opened'] = True
        result['pixel_extent_bounds_checked'] = True
        result['rendered_count'] = len(result['crops'])
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
