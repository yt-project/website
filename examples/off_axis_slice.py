from yt.mods import *
pf = load("DD0087/DD0087")
sp = pf.h.sphere('max', (100.0,'au'))
L = sp.quantities["AngularMomentumVector"]()
off = OffAxisSlicePlot(pf, L, "Density", center="max", width=(1000, "au"))
off.save()
