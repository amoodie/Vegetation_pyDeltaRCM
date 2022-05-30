import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

import deltametrics as dm

_path_root = 'vegetation_output'

"""
A simple animation
  
Built using the template from DeltaMetrics docs:
  https://deltarcm.org/DeltaMetrics/guides/examples/plot/simple_movie.html
"""

def update_field(i):
    im.set_data(data['eta'][i, :, :]+0.01)
    vegi = data['veg_frac'][i, :, :]
    veg_alpha = 0.6 * (vegi > 0.01).astype(float)
    vegim.set_data(vegi)
    vegim.set_alpha(veg_alpha)

data = dm.cube.DataCube(os.path.join(_path_root, 'pyDeltaRCM_output.nc'))

time_idxs = np.arange(0, data.shape[0]-1)

cmap, norm = dm.plot.cartographic_colormap(H_SL=0.0, h=4.5, n=1.0)

fig, ax = plt.subplots(
    gridspec_kw=dict(
        left=0.1, right=0.9))
im = ax.imshow(
    data['eta'][0, :, :],
    extent=data.extent,
    cmap=cmap, norm=norm
    )
veg0 = data['veg_frac'][0, :, :]
veg_alpha = (veg0 > 0.01).astype(float)
vegim = ax.imshow(
    veg0,
    extent=data.extent,
    cmap='Oranges', vmin=0, vmax=0.2,  # hardcoded max for colorbar at veg_frac = 0.2
    alpha=veg_alpha
    )

cb0 = plt.colorbar(im, shrink=0.45, label='elevation [m]')
cb1 = plt.colorbar(vegim, shrink=0.45, label='vegetation frac [-]')

plt.savefig(os.path.join(_path_root, 'initial_frame.png'))

anim = animation.FuncAnimation(
    fig, update_field,
    frames=data.shape[0]-1)
anim.save(os.path.join(_path_root, 'simple_movie.gif'), fps=20)

plt.close()



