"""Plot G-code tool-centre paths (XY) for checking. Usage: backplot.py out.png file1.nc file2.nc ..."""
import re, sys, math
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
out = sys.argv[1]; files = sys.argv[2:]
n = len(files); cols = min(3, n); rows = math.ceil(n / cols)
fig, axs = plt.subplots(rows, cols, figsize=(5 * cols, 5 * rows), squeeze=False)
for ax, fn in zip(axs.flat, files):
    x = y = 0.0; z = 25.0; mode = 0; canned = False
    for line in open(fn):
        line = line.split('(')[0].strip()
        if not line: continue
        g = [int(v) for v in re.findall(r'G(\d+)', line)]
        for gg in g:
            if gg in (0, 1, 2, 3): mode = gg; canned = False
            if gg in (81, 83): canned = True
            if gg == 80: canned = False
        w = dict((k, float(v)) for k, v in re.findall(r'([XYZIJ])(-?[\d.]+)', line))
        nx, ny = w.get('X', x), w.get('Y', y)
        if canned and ('X' in w or 'Y' in w):
            ax.plot(nx, ny, 'o', ms=4, mfc='none', color='tab:red'); x, y = nx, ny; continue
        if 'Z' in w: z = w['Z']
        if mode in (2, 3) and ('I' in w or 'J' in w):
            cx, cy = x + w.get('I', 0), y + w.get('J', 0)
            a0 = math.atan2(y - cy, x - cx); a1 = math.atan2(ny - cy, nx - cx); r = math.hypot(x - cx, y - cy)
            if mode == 3:
                while a1 <= a0 + 1e-9: a1 += 2 * math.pi
            else:
                while a1 >= a0 - 1e-9: a1 -= 2 * math.pi
            ts = [a0 + (a1 - a0) * k / 40 for k in range(41)]
            ax.plot([cx + r * math.cos(t) for t in ts], [cy + r * math.sin(t) for t in ts], color='tab:blue', lw=0.8)
        elif ('X' in w or 'Y' in w):
            ax.plot([x, nx], [y, ny], color='tab:blue' if mode else '0.8', lw=0.8 if mode else 0.4, ls='-' if mode else ':')
        x, y = nx, ny
    ax.set_aspect('equal'); ax.set_title(fn.split('/')[-1], fontsize=8); ax.grid(alpha=0.3)
for ax in list(axs.flat)[n:]: ax.axis('off')
fig.tight_layout(); fig.savefig(out, dpi=80)
