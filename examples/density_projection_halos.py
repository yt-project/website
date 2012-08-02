from yt.mods import *
pf = load("RD0005/RedshiftOutput0005")
# Project Density along the x axis...
p = ProjectionPlot(pf, "x", "Density")
halos = HaloFinder(pf)
p.annotate_hop_circles(halos)
p.annotate_hop_particles(halos, 10) # Max of 10 halos
p.save()
