#!puzlet

import numpy as np
import mc_plot

A=np.array([[0,-0.25*np.sqrt(3),0.5*np.sqrt(3)],[1,-0.25,-0.5]])
ax = mc_plot.summary(A,0,2)
#fig.set_size_inches(6 ,4)
mc_plot.arc(ax, A, 0, 2)

#!end (16)

