import re, sys
L = open(sys.argv[1]).read().split("\n"); out = []; prev = None
for l in L:
    m = re.match(r"p(\d+) +(\d+), *(\d+) (.*)", l)
    if not m:
        out.append(l); prev = None; continue
    p, x, y, t = int(m[1]), int(m[2]), int(m[3]), m[4]
    if prev and prev[0] == p and 0 < y - prev[2] < 14 and abs(x - prev[1]) < 30 and not re.match(r"\([A-E]\)|[IV]+ ?[-–]", t):
        out[-1] += " " + t
    else:
        out.append(("  " if x > 300 else "") + t)
    prev = (p, x, y)
open(sys.argv[2], "w").write("\n".join(out))
