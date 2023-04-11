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
color0 = 'black' #empty
color1 = 'yellow' #conductor
color2='blue' #head
color3='red' #tail
cmap=colors.ListedColormap([color0,color1,color2,color3])
bounds=[0,1,2,3,4]
norm = colors.BoundaryNorm(bounds, cmap.N)
mat=[np.zeros(N) for i in range(N)]

fig,ax=plt.subplots(1,2,figsize=(12,8))
fig.canvas.manager.set_window_title("Wireworld")

def on_click(event):
    global mat
    global paused
    global N
    global speed
    global color0
    global color1
    global color2
    global color3
    global cmap

    if event.button is MouseButton.LEFT:
        if event.inaxes==ax[1]:
            if paused:
                new_mat=[item[:] for item in mat]
                if new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==1:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=2
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==2:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=3
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==3:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=1
                mat=[item[:] for item in new_mat]
        elif event.inaxes==ax[0]:
            if event.xdata>1 and event.xdata<5.2 and event.ydata>8 and event.ydata<10: #Button run/pause
                paused= not paused
                ax[0].clear()
                update_GUI(paused)
            elif event.xdata>1 and event.xdata<5.2 and event.ydata>5 and event.ydata<7: #Save board
                extent = ax[1].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
                nombres=[]
                for images in listdir():
                    if (images.endswith(".png")):
                            nombres.append(images)
                num=1
                while "Wireworld_"+str(num)+".png" in nombres:
                    num+=1
                fig.savefig("Wireworld_"+str(num)+'.png', bbox_inches=extent)
            elif event.xdata>1 and event.xdata<5.2 and event.ydata>2 and event.ydata<4: #Button new 10
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=10
                mat=[np.zeros(N) for i in range(N)]
            elif event.xdata>1 and event.xdata<5.2 and event.ydata>-1 and event.ydata<1: #Button new 50
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=50
                mat=[np.zeros(N) for i in range(N)]
            elif event.xdata>7 and event.xdata<11.2 and event.ydata>8 and event.ydata<10: #Button random board
                paused=True
                ax[0].clear()
                update_GUI(paused)
                mat=[[np.random.choice([0,1]) for i in range(N)] for j in range(N)]

            elif event.xdata>7 and event.xdata<11.2 and event.ydata>5 and event.ydata<7: #change color
                color0 = list(np.random.choice(range(256), size=3)/255)
                color1 = list(np.random.choice(range(256), size=3)/255)
                color2 = list(np.random.choice(range(256), size=3)/255)
                color3 = list(np.random.choice(range(256), size=3)/255)
                cmap=colors.ListedColormap([color0,color1,color2,color3])
            elif event.xdata>7 and event.xdata<11.2 and event.ydata>2 and event.ydata<4: #Button new 25
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=25
                mat=[np.zeros(N) for i in range(N)]
            elif event.xdata>7 and event.xdata<11.2 and event.ydata>-1 and event.ydata<1: #Button new 100
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=100
                mat=[np.zeros(N) for i in range(N)]
    
    elif event.button is MouseButton.RIGHT:
        if event.inaxes==ax[1]:
            if paused:
                new_mat=[item[:] for item in mat]
                if new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==0:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=1
                else:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=0
                mat=[item[:] for item in new_mat]


plt.connect('button_press_event', on_click)

def init():
    global mat
    ax[1].set_xlim(-0.5,N-0.5)
    ax[1].set_ylim(-0.5,N-0.5)
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    grilla=ax[1].imshow(mat,cmap = cmap,norm=norm)

def update(i,j):
    if mat[i][j]==0:
        return 0
    elif mat[i][j]==1:
        neighbors_head=0
        if mat[(i+1)%N][j]==2:
            neighbors_head+=1
        if mat[(i+1)%N][(j+1)%N]==2:
            neighbors_head+=1
        if mat[i][(j+1)%N]==2:
            neighbors_head+=1
        if mat[(i-1)%N][(j+1)%N]==2:
            neighbors_head+=1
        if mat[(i-1)%N][j]==2:
            neighbors_head+=1
        if mat[(i-1)%N][(j-1)%N]==2:
            neighbors_head+=1
        if mat[i][(j-1)%N]==2:
            neighbors_head+=1
        if mat[(i+1)%N][(j-1)%N]==2:
            neighbors_head+=1
        if neighbors_head==1 or neighbors_head==2:
            return 2
        return 1
    elif mat[i][j]==2:
        return 3
    elif mat[i][j]==3:
        return 1

def initialize(iter):
    global mat
    ax[1].clear()
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    ax[1].set_xlabel("Right click: add/remove cell\nLeft click: change cell's state",fontsize=16)
    new_mat=[[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            new_mat[i][j]=update(i,j)
            pass
    mat=[item[:] for item in new_mat]
    ax[1].imshow(mat,cmap = cmap,norm=norm)

def update_GUI(paused_):
    ax[0].set_xlim(0,12)
    ax[0].set_ylim(-2,12)
    ax[0].set_aspect(1)
    ax[0].axis("off")

    if paused:
        ax[0].add_patch(patches.Rectangle((1, 8), 4.2, 2, edgecolor='Black',facecolor='green', linewidth=2)) #Pause/run
        ax[0].text(2.2,8.6,"Run",fontsize=24)
    else:
        ax[0].add_patch(patches.Rectangle((1, 8), 4.2, 2, edgecolor='Black',facecolor='red', linewidth=2)) #Pause/run
        ax[0].text(1.7,8.6,"Pause",fontsize=24)

    ax[0].add_patch(patches.Rectangle((7, 8), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #random board
    ax[0].text(7.15,8.1,"Random\n  board",fontsize=24)

    ax[0].add_patch(patches.Rectangle((1, 5), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #save frame
    ax[0].text(1.75,5.1,"Save\nboard",fontsize=24)

    ax[0].add_patch(patches.Rectangle((7, 5), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #change color
    ax[0].text(7.3,5.1,"Change\n  color",fontsize=24)

    ax[0].add_patch(patches.Rectangle((1, 2), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #new 10x10
    ax[0].text(1.7,2.1," New\n10x10",fontsize=24)

    ax[0].add_patch(patches.Rectangle((7, 2), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #new 25x25
    ax[0].text(7.7,2.1," New\n25x25",fontsize=24)

    ax[0].add_patch(patches.Rectangle((1, -1), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #new 50x50
    ax[0].text(1.7,-0.9," New\n50x50",fontsize=24)

    ax[0].add_patch(patches.Rectangle((7, -1), 4.2, 2, edgecolor='Black',facecolor='white', linewidth=2)) #new 100x100
    ax[0].text(7.005,-0.9,"   New\n100x100",fontsize=24)

    ax[0].text(1,-3.5,"Simulation must be paused in order\nto interact with the board (change the\nstate of a cell).",fontsize=14)
    ax[0].text(1,11,"Rules (at each step in time):\n1- Electron heads become electron tails.\n2- Electron tails become conductors.\n3- Conductors become electron heads only if they have exactly 1 or 2 electron head neighbors.\n4- Empty cells remain empty.",fontsize=14)

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
        ax[1].set_xlabel("Right click: add/remove cell\nLeft click: change cell's state",fontsize=16)
    ax[1].imshow(mat,cmap = cmap,norm=norm)
    xcenter=(-0.5+(N-0.5))/2
    ycenter=(-0.5+(N-0.5))/2
    ax[1].text(xcenter-N/2,ycenter+N/1.4,'States:',fontsize=16)
    ax[1].text(xcenter-N/10,ycenter+N/1.45,'/',fontsize=16)
    #ax[1].text(xcenter+N/6,ycenter+N/1.45,'/',fontsize=16)
    #ax[1].text(xcenter+N/2,ycenter+N/1.45,'/',fontsize=16)
    ax[1].text(xcenter-N/14,ycenter+N/1.45,'Conductor',weight="bold",color=color1,fontsize=16)
    ax[1].text(xcenter-N/3.3,ycenter+N/1.45,'Empty',weight="bold",color=color0,fontsize=16)
    ax[1].text(xcenter-N/3.3,ycenter+N/1.35,'Electron head',weight="bold",color=color2,fontsize=16)
    ax[1].text(xcenter+N/7.9,ycenter+N/1.35,'/',fontsize=16)
    ax[1].text(xcenter+N/6.5,ycenter+N/1.35,'Electron tail',weight="bold",color=color3,fontsize=16)

    

##############################################
#### Welcome screen ####
aux_welcome=FuncAnimation(fig,initialize,frames=2,interval=1,init_func=init,repeat=False)
anim=FuncAnimation(fig,animate,frames=max_iter,interval=speed,init_func=init,repeat=False)


#### Buttons ####
update_GUI(paused)
plt.show()
