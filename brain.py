import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib import patches
from matplotlib.backend_bases import MouseButton
from matplotlib import colors
import matplotlib as mpl
from os import listdir

N=10 #Grid size (NxN)
max_iter=99999999999
speed=50
paused=True
color0 = 'black' #dead
color1 = 'green' #alive
color2 = 'blue' #dying
cmap=colors.ListedColormap([color0,color1,color2])
bounds=[0,1,2,3]
norm = colors.BoundaryNorm(bounds, cmap.N)
mat=[np.zeros(N) for i in range(N)]

fig,ax=plt.subplots(1,2,figsize=(12,8))
fig.canvas.manager.set_window_title("Brian's brain")

def on_click(event):
    global mat
    global paused
    global N
    global speed
    global color0
    global color1
    global color2
    global cmap
    if event.button is MouseButton.LEFT:
        if event.inaxes==ax[1]:
            if paused:
                new_mat=[item[:] for item in mat]
                new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=(mat[int(event.ydata+0.5)][int(event.xdata+0.5)]+1)%3
                mat=[item[:] for item in new_mat]
        elif event.inaxes==ax[0]:
            if event.xdata>1 and event.xdata<5.2 and event.ydata>9 and event.ydata<11: #Button run/pause
                paused= not paused
                ax[0].clear()
                update_GUI(paused)
            elif event.xdata>1 and event.xdata<5.2 and event.ydata>6 and event.ydata<8: #Save board
                extent = ax[1].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
                nombres=[]
                for images in listdir():
                    if (images.endswith(".png")):
                            nombres.append(images)
                num=1
                while "Brian_"+str(num)+".png" in nombres:
                    num+=1
                fig.savefig("Brian_"+str(num)+'.png', bbox_inches=extent)
            elif event.xdata>1 and event.xdata<5.2 and event.ydata>3 and event.ydata<5: #Button new 10
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=10
                mat=[np.zeros(N) for i in range(N)]
            elif event.xdata>1 and event.xdata<5.2 and event.ydata>0 and event.ydata<2: #Button new 50
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=50
                mat=[np.zeros(N) for i in range(N)]
            elif event.xdata>7 and event.xdata<11.2 and event.ydata>9 and event.ydata<11: #Button random board
                paused=True
                ax[0].clear()
                update_GUI(paused)
                mat=[[np.random.choice([0,1,2]) for i in range(N)] for j in range(N)]
            elif event.xdata>7 and event.xdata<11.2 and event.ydata>6 and event.ydata<8: #change color
                color0 = list(np.random.choice(range(256), size=3)/255)
                color1 = list(np.random.choice(range(256), size=3)/255)
                color2 = list(np.random.choice(range(256), size=3)/255)
                cmap=colors.ListedColormap([color0,color1,color2])
            elif event.xdata>7 and event.xdata<11.2 and event.ydata>3 and event.ydata<5: #Button new 25
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=25
                mat=[np.zeros(N) for i in range(N)]
            elif event.xdata>7 and event.xdata<11.2 and event.ydata>0 and event.ydata<2: #Button new 100
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=100
                mat=[np.zeros(N) for i in range(N)]

plt.connect('button_press_event', on_click)

def init():
    global mat
    ax[1].set_xlim(-0.5,N-0.5)
    ax[1].set_ylim(-0.5,N-0.5)
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    grilla=ax[1].imshow(mat,cmap = cmap, norm= norm)

def update(i,j):
    if mat[i][j]==0:
        alive_neighbours=0
        for k in range(-1,2):
            for l in range(-1,2):
                if (k!=0 or l!=0):
                    if mat[(i+k)%N][(j+l)%N] == 1:
                        alive_neighbours+=1
        if alive_neighbours==2:
            return 1
    elif mat[i][j]==1:
        return 2
    
    return 0

def initialize(iter):
    global mat
    ax[1].clear()
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    ax[1].set_xlabel("Click a cell to change its state!",fontsize=16)
    new_mat=[[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            new_mat[i][j]=update(i,j)
            pass
    mat=[item[:] for item in new_mat]
    ax[1].imshow(mat,cmap = cmap, norm= norm)

def update_GUI(paused_):
    ax[0].set_xlim(0,12)
    ax[0].set_ylim(-2,12)
    ax[0].set_aspect(1)
    ax[0].axis("off")

    if paused:
        ax[0].add_patch(patches.Rectangle((1, 9), 4.2, 2, edgecolor='Black',facecolor='green', linewidth=2)) #Pause/run
        ax[0].text(2.2,9.6,"Run",fontsize=24)
    else:
        ax[0].add_patch(patches.Rectangle((1, 9), 4.2, 2, edgecolor='Black',facecolor='red', linewidth=2)) #Pause/run
        ax[0].text(1.7,9.6,"Pause",fontsize=24)

    ax[0].add_patch(patches.Rectangle((7, 9), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #random board
    ax[0].text(7.15,9.1,"Random\n  board",fontsize=24)

    ax[0].add_patch(patches.Rectangle((1, 6), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #save frame
    ax[0].text(1.75,6.1,"Save\nboard",fontsize=24)

    ax[0].add_patch(patches.Rectangle((7, 6), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #change color
    ax[0].text(7.3,6.1,"Change\n  color",fontsize=24)

    ax[0].add_patch(patches.Rectangle((1, 3), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #new 10x10
    ax[0].text(1.7,3.1," New\n10x10",fontsize=24)

    ax[0].add_patch(patches.Rectangle((7, 3), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #new 25x25
    ax[0].text(7.7,3.1," New\n25x25",fontsize=24)

    ax[0].add_patch(patches.Rectangle((1, 0), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #new 50x50
    ax[0].text(1.7,0.1," New\n50x50",fontsize=24)

    ax[0].add_patch(patches.Rectangle((7, 0), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #new 100x100
    ax[0].text(7.005,0.1,"   New\n100x100",fontsize=24)

    ax[0].text(1,-2.5,"Simulation must be paused in order\nto interact with the board (change the\nstate of a cell).",fontsize=14)
    ax[0].text(1,12,"Rules (at each step in time):\n1- Any dead cell with exactly two live neighbours becomes alive.\n2- Every live cell becomes a dying cell.\n3- Every dying cell becomes a dead cell.",fontsize=14)

def animate(iter):
    global mat
    ax[1].clear()
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    if not paused:
        ax[1].set_xlabel("Simulation running",fontsize=16)
        new_mat=[[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                new_mat[i][j]=update(i,j)
        mat=[item[:] for item in new_mat]
    else:
        ax[1].set_xlabel("Click a cell to change its state!",fontsize=16)
    ax[1].imshow(mat,cmap = cmap, norm= norm)
    xcenter=(-0.5+(N-0.5))/2
    ycenter=(-0.5+(N-0.5))/2
    ax[1].text(xcenter-N/2.8,ycenter+N/1.55,'States:',fontsize=16)
    ax[1].text(xcenter-N/6.3,ycenter+N/1.55,'Dead',weight="bold",color=color0,fontsize=16)
    ax[1].text(xcenter+N/90,ycenter+N/1.55,'/',fontsize=16)
    ax[1].text(xcenter+N/25,ycenter+N/1.55,'Alive',weight="bold",color=color1,fontsize=16)
    ax[1].text(xcenter+N/5,ycenter+N/1.55,'/',fontsize=16)
    ax[1].text(xcenter+N/4.4,ycenter+N/1.55,'Dying',weight="bold",color=color2,fontsize=16)
    

##############################################
#### Welcome screen ####
aux_welcome=FuncAnimation(fig,initialize,frames=2,interval=1,init_func=init,repeat=False)
anim=FuncAnimation(fig,animate,frames=max_iter,interval=speed,init_func=init,repeat=False)


#### Buttons ####
update_GUI(paused)
plt.show()
