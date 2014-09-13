#!puzlet

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()

ax.quiver(np.cos(np.pi/6),np.sin(np.pi/6),angles='xy',
    scale_units='xy', scale=1,color='blue', width=.04)
ax.quiver(np.sin(np.pi/6),np.cos(np.pi/6),angles='xy',
    scale_units='xy', scale=1,color='green', width=.04)
ax.text(0.5, 0.52, r'$\cos(\theta)$', rotation=38, va='center', 
    ha='center', size=100)

ax.set_frame_on(False)
ax.axes.get_yaxis().set_visible(False)
ax.axes.get_xaxis().set_visible(False)
ax.set_xlim([0,1])
ax.set_ylim([0,1])

#!end (38)

