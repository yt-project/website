from yt.mods import *
pf = load("DD0053/DD0053")
sp = pf.h.sphere('max', (100.0,'au'))
L = sp.quantities["AngularMomentumVector"]()
pc = PlotCollection(pf)
pc.add_cutting_plane("Density", L)
pc.set_width(1000, 'au')
pc.save()
