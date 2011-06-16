from yt.mods import *
pf = load("RD0005/RedshiftOutput0005")
# Let's center at the center of the box
pc = PlotCollection(pf, [0.5,0.5,0.5])
# Project Density along the x axis...
p = pc.add_projection("Density", 'x')
pc.save()
