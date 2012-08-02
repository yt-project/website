from yt.mods import *
pf = load("RD0005/RedshiftOutput0005")
# Project Density along the x axis...
ProjectionPlot(pf, "x", "Density").save()
