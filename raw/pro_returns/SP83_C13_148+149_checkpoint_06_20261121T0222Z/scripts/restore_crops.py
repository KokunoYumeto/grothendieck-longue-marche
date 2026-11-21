#!/usr/bin/env python3
from pathlib import Path
import sys
from compact_archive_v2 import restore
restore(Path(__file__).resolve().parents[1], sys.argv[1:])
