import time
from yt.mods import *
pf = load("JHK-DD0030/galaxy0030")
pc = PlotCollection(pf, [0.5, 0.5, 0.5])
pc.add_phase_sphere(1.0, '1', ["Density", "Temperature", "CellMassMsun"],
        weight=None)
pc.save()
