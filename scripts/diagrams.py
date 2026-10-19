#!/usr/bin/env python3
"""Generate every concept diagram into .vitepress/theme/diagrams/*.svg (run: python3 scripts/diagrams.py)."""
import os, sys, importlib
sys.path.insert(0, os.path.dirname(__file__))
OUT = os.path.join(os.path.dirname(__file__), '..', '.vitepress', 'theme', 'diagrams')
os.makedirs(OUT, exist_ok=True)
n = 0
for mod in ['diagrams_business', 'diagrams_film', 'diagrams_english', 'diagrams_spanish', 'diagrams_digital', 'diagrams_maths', 'diagrams_solutions', 'diagrams_solutions2', 'diagrams_examples', 'diagrams_solutions3']:
    try:
        m = importlib.import_module(mod)
    except ModuleNotFoundError as e:
        if e.name == mod: continue
        raise
    for name, fn in m.ALL.items():
        svg, alt = fn()
        open(os.path.join(OUT, name + '.svg'), 'w').write(svg)
        n += 1
print('wrote', n, 'diagrams to', os.path.normpath(OUT))
