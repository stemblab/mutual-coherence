import numpy as np
import mc_plot

A=np.array([[0,-0.25*np.sqrt(3),0.5*np.sqrt(3)],[1,-0.25,-0.5]])
fig, ax = mc_plot.summary(A,0,2)
mc_plot.arc(ax, A, 0, 2)
fig.savefig("bound_plot.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)
