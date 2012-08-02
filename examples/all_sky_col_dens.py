from yt.mods import *
import yt.visualization.volume_rendering.camera as camera

pf = load("JHK-DD0030/galaxy0030")
image = camera.allsky_projection(pf, [0.5,0.5,0.5], 100.0/pf['kpc'],
                                 64, "Density")
camera.plot_allsky_healpix(image, 64, "allsky.png", "Column Density [g/cm^2]")
