import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np

def summary(A,u,v):

    # plot
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')

    # ticks
    majorLocator   = MultipleLocator(1)
    majorFormatter = FormatStrFormatter('%d')

    # vectors
    o=np.array([0,0,0])
    ax.quiver(o,o,A[0,0],A[1,0],angles='xy',scale_units='xy',
        scale=1,color='red')
    ax.quiver(o,o,A[0,1],A[1,1],angles='xy',scale_units='xy',
        scale=1,color='blue')
    ax.quiver(o,o,A[0,2],A[1,2],angles='xy',scale_units='xy',
        scale=1,color='green')

    # plotting
    ax.set_xlim([np.min(np.c_[o,A[0,:]])-1,np.max(np.c_[o,A[0,:]])+1])
    ax.set_ylim([np.min(np.c_[o,A[1,:]])-1,np.max(np.c_[o,A[1,:]])+1])
    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_major_formatter(majorFormatter)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_major_formatter(majorFormatter)
    
    return fig, ax
    
def arc(ax, A, u,v):
    
    # process columns of A as 2D vectors
    mags=np.apply_along_axis(np.linalg.norm, 0, A) # columns lengths
    angs=np.arctan2(A[1,:],A[0,:]) # column angles
    diff_ang=(angs[v]-angs[u])*180/np.pi # angular diff of selected columns
    diff_cos=np.cos(diff_ang*np.pi/180)
    
    # annotation
    txt_ang=0.5*(angs[v]+angs[u]) # angle of annotating text
    txt_mag=1.3*np.min(mags[np.ix_([u,v])]) # radius of text center
    txt_x=txt_mag*np.cos(txt_ang) # convert to x
    txt_y=txt_mag*np.sin(txt_ang) # convert to y
    
    # angle "arc"
    w1 = Wedge((0,0), 0.5*np.min(mags[np.ix_([u,v])]), angs[v]*180/np.pi,
        angs[u]*180/np.pi, 
        color='k', fill=False, zorder=0)
    ax.text(txt_x, txt_y, r"$\mu=|\cos (%.2f)|=%.4f$"%(np.abs(diff_ang),
        np.abs(diff_cos)),
        rotation=txt_ang*180/np.pi, va='center', ha='center')
    ax.add_artist(w1)

if __name__=="__main__":
    
    A=np.array([[1,-1,1],[1,2,4]])
    fig, ax = summary(A,2,0)
    fig.savefig("mc_plot_1.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)
    arc(ax, A,2,0)
    fig.savefig("mc_plot_2.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)
