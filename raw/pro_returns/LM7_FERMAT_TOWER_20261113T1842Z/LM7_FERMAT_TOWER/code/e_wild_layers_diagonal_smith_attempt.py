#!/usr/bin/env python3
"""Materialized source of the recorded inline diagonal-only Smith attempt.

The original inline execution was session54058. It set a20-second SIGALRM
before the degree-two smith_normal_form call and exited142 without a Smith
result. This retained source is not rerun by the completed certificate.
"""
import importlib.util
import signal
import time
from pathlib import Path

import numpy as np
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_form

path = Path(__file__).with_name("e_wild_layers.py")
spec = importlib.util.spec_from_file_location("wild_layers", path)
wild_layers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wild_layers)
h = wild_layers.hall.Hall(2)
inputs = wild_layers.hall.arithmetic_inputs()
T = wild_layers.dense(h.action(inputs["tau"], 2)[0])
J = wild_layers.dense(h.action(inputs["c"], 2)[0])
I = np.eye(len(T), dtype=np.int64)
A = np.hstack([T - 7 * I, J + I])
start = time.monotonic()
signal.alarm(20)
D = smith_normal_form(
    DomainMatrix.from_Matrix(s.Matrix(A.tolist())).convert_to(s.ZZ)
).to_Matrix()
print(time.monotonic() - start)
print([D[i, i] for i in range(D.rows)])
