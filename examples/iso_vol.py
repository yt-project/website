from yt.mods import *

pf = load("JHK-DD0030/galaxy0030")

sphere = pf.h.sphere('max', (125, 'kpc'))
limits = sphere.quantities["Extrema"]("Density")[0]
tf = ColorTransferFunction(na.log10(limits))
# five layers, with the kamae colormap, 0.001 dex wide each
tf.add_layers(8, colormap="kamae", w=0.001)
cam = pf.h.camera([0.5, 0.5, 0.5], # center
                  [0.2, 0.3, 0.4], # view-angle
                  125.0/pf['kpc'],   # FOV
                  (512, 512),      # resolution
                  tf)              # transfer function
cam.snapshot("image.png", 4.0) # clip by 4.0 * std()
