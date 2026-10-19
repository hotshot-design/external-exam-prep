#!/usr/bin/env python3
"""Recomputes every number in maths/worked-examples.md from first principles and compares it with the page.
Run: python3 scripts/verify/maths_examples.py   (exit 1 on any mismatch)"""
import math, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
page = open(f'{ROOT}/maths/worked-examples.md').read().replace('\\,', '').replace('\\$', '$')
bad = 0

def expect(label, value, text, dp=2):
    """value (rounded to dp) must appear in the page text (spaces as thousand separators allowed)."""
    global bad
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(repr(round(value, 9))).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP)  # round half up, as a calculator does
    s = f'{q:,.{dp}f}'.replace(',', ' ')
    plain = s.replace(' ', '')
    ok = s in page or plain in page.replace(' ', '')
    print(('ok   ' if ok else 'FAIL ') + f'{label}: {s}')
    if not ok: bad += 1

# 1 least squares
m = 0.8 * 5 / 2; c = 40 - m * 10; expect('1 slope', m, page, 0); expect('1 intercept', c, page, 0); expect('1 R2 %', 0.8 ** 2 * 100, page, 0)
# 2 moving averages
d = [12, 15, 14, 18, 20, 19, 23]
for i in range(1, 6): expect(f'2 MA{i}', sum(d[i - 1:i + 2]) / 3, page, 1)
# 3 seasonal
y1, y2 = [40, 60, 80, 20], [44, 66, 88, 22]
idx = [(a / 50 + b / 55) / 2 for a, b in zip(y1, y2)]
expect('3 index sum', sum(idx), page, 0); expect('3 deseasonalise', 88 / idx[2], page, 0)
# 4 sequences
expect('4 t20', 12 + 19 * 5, page, 0); expect('4 t6', 3 * 2 ** 5, page, 0); expect('4 depreciation', 10000 * 0.85 ** 3, page, 2)
# 5 earth
expect('5 meridian', 111.2 * 10, page, 0); expect('5 parallel', 111.2 * math.cos(math.radians(30)) * 20, page, 0)
# 6 compound interest
A = 5000 * 1.005 ** 36; expect('6 A', A, page); expect('6 interest', A - 5000, page); expect('6 EAR %', (1.005 ** 12 - 1) * 100, page, 2)
# 7 loan
i = 0.006; dpay = 20000 * i / (1 - (1 + i) ** -60); expect('7 payment', dpay, page); expect('7 repaid', dpay * 60, page); expect('7 interest', dpay * 60 - 20000, page)
# 8 future value annuity
i = 0.004; fv = 200 * ((1 + i) ** 120 - 1) / i; expect('8 FV', fv, page); expect('8 interest', fv - 24000, page)
# 9 perpetuity
expect('9 perpetuity', 500 / 0.01, page, 0)
# 10 Euler
expect('10 faces', 2 + 10 - 6, page, 0)
# 11 critical path
dur = {'A': 3, 'B': 4, 'C': 2, 'D': 5, 'E': 3}
expect('11 path via B', dur['A'] + dur['B'] + dur['D'] + dur['E'], page, 0); expect('11 path via C', dur['A'] + dur['C'] + dur['D'] + dur['E'], page, 0)
# 12 flow: min cut over all S-side sets
cap = {('S', 'A'): 10, ('S', 'B'): 8, ('A', 'B'): 3, ('A', 'T'): 7, ('B', 'T'): 9}
cuts = []
for side in ([], ['A'], ['B'], ['A', 'B']):
    S = {'S', *side}; cuts.append(sum(w for (u, v), w in cap.items() if u in S and v not in S))
expect('12 min cut', min(cuts), page, 0)
# 13 Hungarian (brute force minimum)
M = [[9, 2, 7], [6, 4, 3], [5, 8, 1]]
import itertools
expect('13 min cost', min(sum(M[r][p[r]] for r in range(3)) for p in itertools.permutations(range(3))), page, 0)
# 14 time zones
tz = 10 - (-8); depart = 21 + 50 / 60; arrive = 18 + 50 / 60 + tz  # Sydney clock hours after midnight Tuesday
flight = arrive - depart if arrive > depart else arrive + 24 - depart
expect('14 time difference', tz, page, 0); expect('14 flight hours', flight, page, 0); expect('14 hours flown', 4828 / 12070 * flight, page, 0)
# 15 loan recurrence
a1 = 1.007 * 15000 - 250; a2 = 1.007 * a1 - 250; expect('15 A1', a1, page, 0); expect('15 A2', a2, page); expect('15 interest', 500 - (15000 - a2), page)
# 16 adjacency degrees
deg = {'A': 2, 'B': 2, 'C': 3, 'D': 1}; expect('16 degree sum', sum(deg.values()), page, 0)

print('\nALL OK' if not bad else f'\n{bad} MISMATCH(ES)')
sys.exit(1 if bad else 0)
