import time
from yt.mods import *
pf = load("GalaxyClusterMerger/fiducial_1to3_b0.273d_hdf5_plt_cnt_0175")
pc = PlotCollection(pf, "c")
pc.add_phase_sphere(10.0, 'mpc', ["Density", "Temperature", "CellMassMsun"],
        weight=None)
pc.save()
