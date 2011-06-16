from yt.mods import *
pf = load("plt01200")

pf.h.print_stats()
print pf.h.grids[0]["Density"]

for g in pf.h.grids:
    print g.LeftEdge, g.RightEdge, g.dds, g["Density"].max()
