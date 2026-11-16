#!/usr/bin/env python3
"""Retain the literal A186 candidate data for independent GP clients."""
from pathlib import Path
import hashlib

p=Path(__file__).resolve().parent
source=p/'point3_fermat8_genus2_rank_certificate.gp'
lines=[line for line in source.read_text().splitlines() if line.startswith('cases=')]
assert len(lines)==1
out=p/'point3_fermat8_genus2_candidate_data.gp'
out.write_text('\\\\ Literal data from the complete A186 certificate.\n'
               +'\\\\ Source SHA256 '+hashlib.sha256(source.read_bytes()).hexdigest()+'\n'
               +lines[0]+'\n')
print('PASS: exact candidate-data assignment copied; source SHA256 '+hashlib.sha256(source.read_bytes()).hexdigest())
