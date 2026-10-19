"""Tiny SVG helper used by scripts/diagrams.py. Styles come from CSS classes defined in
.vitepress/theme/custom.css (they use VitePress colour variables, so dark mode works)."""
from xml.sax.saxutils import escape

class SVG:
    def __init__(self, name, w, h):
        self.name, self.w, self.h = name, w, h
        self.parts = []
        self.mid = f'ah-{name}'

    # ---- primitives -------------------------------------------------------
    def raw(self, s): self.parts.append(s)

    def text(self, x, y, s, cls='t', anchor='middle', size=None, weight=None):
        lines = str(s).split('\n')
        attrs = f'x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}"'
        if size: attrs += f' font-size="{size}"'
        if weight: attrs += f' font-weight="{weight}"'
        if len(lines) == 1:
            self.parts.append(f'<text {attrs}>{escape(lines[0])}</text>')
        else:
            lh = (size or 14) * 1.25
            y0 = y - lh * (len(lines) - 1) / 2
            t = ''.join(f'<tspan x="{x}" y="{y0 + i * lh:.1f}">{escape(l)}</tspan>' for i, l in enumerate(lines))
            self.parts.append(f'<text {attrs}>{t}</text>')

    def box(self, x, y, w, h, label='', cls='box', rx=8, size=14, tcls='t', weight=None, sub=None):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>')
        if label:
            ty = y + h / 2 + (-7 if sub else 0)
            self.text(x + w / 2, ty + 5, label, tcls, size=size, weight=weight)
        if sub:
            self.text(x + w / 2, y + h / 2 + 14, sub, 't2', size=max(size - 3, 11))

    def line(self, x1, y1, x2, y2, cls='ln', dash=False):
        d = ' stroke-dasharray="5 4"' if dash else ''
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"{d}/>')

    def arrow(self, x1, y1, x2, y2, cls='ar', dash=False):
        d = ' stroke-dasharray="5 4"' if dash else ''
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" marker-end="url(#{self.mid})"{d}/>')

    def path(self, d, cls='ln', arrow=False, fill=None):
        m = f' marker-end="url(#{self.mid})"' if arrow else ''
        f = f' fill="{fill}"' if fill else ''
        self.parts.append(f'<path d="{d}" class="{cls}"{m}{f}/>')

    def circle(self, x, y, r, cls='node'):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls}"/>')

    def poly(self, pts, cls='ln'):
        p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        self.parts.append(f'<polyline points="{p}" class="{cls}" fill="none"/>')

    def title(self, x, y, s): self.text(x, y, s, 'tt', size=17, weight=700)

    # ---- output -----------------------------------------------------------
    def render(self, alt):
        defs = (f'<defs><marker id="{self.mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="ah"/></marker></defs>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{escape(alt)}" '
                f'class="dg">{defs}{"".join(self.parts)}</svg>\n')
