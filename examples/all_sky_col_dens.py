from yt.mods import *
import yt.visualization.volume_rendering.camera as camera

pf = load("RedshiftOutput0010.dir/RedshiftOutput0010")
cam = camera.HEALpixCamera([0.5, 0.5, 0.5], 50./pf['mpc'], 
                           nside = 64, pf = pf,
                           log_fields = [False])
bitmap = cam.snapshot("allsky.png")
