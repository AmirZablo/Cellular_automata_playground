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
speed=1
paused=True
color0 = 'black' #tile 0
color1 = 'grey' #tile 1
color2 = 'blue' #ant on tile 0 facing up
color3 = 'red' #ant on tile 0 facing right
color4 = 'green' #ant on tile 0 facing down
color5 = 'yellow' #ant on tile 0 facing left
color6 = 'orange' #ant on tile 1 facing up
color7 = 'purple' #ant on tile 1 facing right
color8 = 'brown' #ant on tile 1 facing down
color9 = 'pink' #ant on tile 1 facing left
cmap=colors.ListedColormap([color0,color1,color2,color3,color4,color5,color6,color7,color8,color9])
bounds=[0,1,2,3,4,5,6,7,8,9,10]
norm = colors.BoundaryNorm(bounds, cmap.N)
mat=[[0 for j in range(N)] for i in range(N)]

fig,ax=plt.subplots(1,2,figsize=(12,8))
fig.canvas.manager.set_window_title("Langton's Ant")

def on_click(event):
    global mat
    global paused
    global N
    global speed
    global color0
    global color1
    global color2
    global color3
    global color4
    global color5
    global color6
    global color7
    global color8
    global color9
    global cmap

    if event.button is MouseButton.LEFT:
        if event.inaxes==ax[1]:
            if paused:
                new_mat=[item[:] for item in mat]
                if new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==0:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=2
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==2:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=3
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==3:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=4
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==4:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=5
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==5:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=0

                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==1:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=6
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==6:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=7
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==7:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=8
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==8:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=9
                elif new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==9:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=1

                mat=np.copy(new_mat)
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
                while "Ant_"+str(num)+".png" in nombres:
                    num+=1
                fig.savefig("Ant_"+str(num)+'.png', bbox_inches=extent)
            elif event.xdata>1 and event.xdata<5.2 and event.ydata>2 and event.ydata<4: #Button new 10
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=10
                mat=[[0 for j in range(N)] for i in range(N)]
            elif event.xdata>1 and event.xdata<5.2 and event.ydata>-1 and event.ydata<1: #Button new 50
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=50
                mat=[[0 for j in range(N)] for i in range(N)]
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
                color4 = list(np.random.choice(range(256), size=3)/255)
                color5 = list(np.random.choice(range(256), size=3)/255)
                color6 = list(np.random.choice(range(256), size=3)/255)
                color7 = list(np.random.choice(range(256), size=3)/255)
                color8 = list(np.random.choice(range(256), size=3)/255)
                color9 = list(np.random.choice(range(256), size=3)/255)
                cmap=colors.ListedColormap([color0,color1,color2,color3,color4,color5,color6,color7,color8,color9])
            elif event.xdata>7 and event.xdata<11.2 and event.ydata>2 and event.ydata<4: #Button new 25
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=25
                mat=[[0 for j in range(N)] for i in range(N)]
            elif event.xdata>7 and event.xdata<11.2 and event.ydata>-1 and event.ydata<1: #Button new 100
                paused=True
                ax[0].clear()
                update_GUI(paused)
                N=100
                mat=[[0 for j in range(N)] for i in range(N)]
    
    elif event.button is MouseButton.RIGHT:
        if event.inaxes==ax[1]:
            if paused:
                new_mat=[item[:] for item in mat]
                if new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==0 or new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==2 or new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==3 or new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==4 or new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]==5:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=1 
                else:
                    new_mat[int(event.ydata+0.5)][int(event.xdata+0.5)]=0
                mat=np.copy(new_mat)


plt.connect('button_press_event', on_click)

def init():
    global mat
    ax[1].set_xlim(-0.5,N-0.5)
    ax[1].set_ylim(-0.5,N-0.5)
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    grilla=ax[1].imshow(mat,cmap = cmap,norm=norm)

def update():
    global mat
    new_mat=np.copy(mat)

    for i in range(N):
        for j in range(N): 
            if mat[i][j]!=0 and mat[i][j]!=1: #There is an ant
                if mat[i][j]==2: #Ant is facing up on a tile 0
                    new_mat[i][j]=1
                    if new_mat[i][(j+1)%N]==0 or new_mat[i][(j+1)%N]==1:
                        if mat[i][(j+1)%N]==0:
                            new_mat[i][(j+1)%N]=3
                        elif mat[i][(j+1)%N]==1:
                            new_mat[i][(j+1)%N]=7
                    else:
                        new_mat[i][(j+1)%N]=0

                elif mat[i][j]==3: #Ant is facing right on a tile 0
                    new_mat[i][j]=1
                    if new_mat[(i+1)%N][j]==0 or new_mat[(i+1)%N][j]==1:
                        if mat[(i+1)%N][j]==0:
                            new_mat[(i+1)%N][j]=4
                        elif mat[(i+1)%N][j]==1:
                            new_mat[(i+1)%N][j]=8
                    else:
                        new_mat[(i+1)%N][j]=0
                elif mat[i][j]==4: #Ant is facing down on a tile 0 ERROR
                    new_mat[i][j]=1
                    if new_mat[i][(j-1)%N]==0 or new_mat[i][(j-1)%N]==1:
                        if mat[i][(j-1)%N]==0:
                            new_mat[i][(j-1)%N]=5
                        elif mat[i][(j-1)%N]==1:
                            new_mat[i][(j-1)%N]=9
                    else:
                        new_mat[i][(j-1)%N]=0
                elif mat[i][j]==5: #Ant is facing left on a tile 0
                    new_mat[i][j]=1
                    if new_mat[(i-1)%N][j]==0 or new_mat[(i-1)%N][j]==1:
                        if mat[(i-1)%N][j]==0:
                            new_mat[(i-1)%N][j]=2
                        elif mat[(i-1)%N][j]==1:
                            new_mat[(i-1)%N][j]=6
                    else:
                        new_mat[(i-1)%N][j]=0
                elif mat[i][j]==6: #Ant is facing up on a tile 1
                    new_mat[i][j]=0
                    if new_mat[i][(j-1)%N]==0 or new_mat[i][(j-1)%N]==1:
                        if mat[i][(j-1)%N]==0:
                            new_mat[i][(j-1)%N]=5
                        elif mat[i][(j-1)%N]==1:
                            new_mat[i][(j-1)%N]=9
                    else:
                        new_mat[i][(j-1)%N]=0
                elif mat[i][j]==7: #Ant is facing right on a tile 1
                    new_mat[i][j]=0
                    if new_mat[(i-1)%N][j]==0 or new_mat[(i-1)%N][j]==1:
                        if mat[(i-1)%N][j]==0:
                            new_mat[(i-1)%N][j]=2
                        elif mat[(i-1)%N][j]==1:
                            new_mat[(i-1)%N][j]=6
                    else:
                        new_mat[(i-1)%N][j]=0
                elif mat[i][j]==8: #Ant is facing down on a tile 1
                    new_mat[i][j]=0
                    if new_mat[i][(j+1)%N]==0 or new_mat[i][(j+1)%N]==1:
                        if mat[i][(j+1)%N]==0:
                            new_mat[i][(j+1)%N]=3
                        elif mat[i][(j+1)%N]==1:
                            new_mat[i][(j+1)%N]=7
                    else:
                        new_mat[i][(j+1)%N]=0
                else: #Ant is facing left on a tile 1
                    new_mat[i][j]=0
                    if new_mat[(i+1)%N][j]==0 or new_mat[(i+1)%N][j]==1:
                        if mat[(i+1)%N][j]==0:
                            new_mat[(i+1)%N][j]=4
                        elif mat[(i+1)%N][j]==1:
                            new_mat[(i+1)%N][j]=8
                    else:
                        new_mat[(i+1)%N][j]=0
    
    return new_mat

def initialize(iter):
    global mat
    ax[1].clear()
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    ax[1].set_xlabel("Right click: add/remove cell\nLeft click: change cell's state",fontsize=16)
    new_mat=update()
    mat=np.copy(new_mat)
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
    ax[0].text(0,11.5,"Rules (at each step in time, for each ant):\n1- If it is at a tile of type 1, turn 90° clockwise, flip the type of the tile, move forward one cell.\n2- If it is at a tile of type 2, turn 90° counter-clockwise, flip the type of the tile, move forward one cell. \n3- If two or more ants moev to the same tile, they die.",fontsize=14)

def animate(iter):
    global mat
    ax[1].clear()
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    if not paused:
        ax[1].set_xlabel("Simulation running",fontsize=16)
        new_mat=update()
        mat=np.copy(new_mat)
    else:
        ax[1].set_xlabel("Right click: change tile type\nLeft click: add/rotate/remove ant from tile",fontsize=16)
    ax[1].imshow(mat,cmap = cmap,norm=norm) #ACA ESTA EL PROBLEMA
    xcenter=(-0.5+(N-0.5))/2
    ycenter=(-0.5+(N-0.5))/2
    ax[1].text(xcenter-N/1.7,ycenter+N/1.45,'Tile 1:',fontsize=16)
    ax[1].text(xcenter-N/2.5,ycenter+N/1.45,'Empty',weight="bold",color=color0,fontsize=16)
    ax[1].text(xcenter-N/5,ycenter+N/1.45,'/',fontsize=16)
    ax[1].text(xcenter-N/5.8,ycenter+N/1.45,'Ant facing',fontsize=16)
    ax[1].text(xcenter+N/8.8,ycenter+N/1.45,'up',weight="bold",color=color2,fontsize=16)
    ax[1].text(xcenter+N/5,ycenter+N/1.45,'/',fontsize=16)
    ax[1].text(xcenter+N/4.4,ycenter+N/1.45,'right',weight="bold",color=color3,fontsize=16)
    ax[1].text(xcenter+N/2.55,ycenter+N/1.45,'/',fontsize=16)
    ax[1].text(xcenter+N/2.37,ycenter+N/1.45,'down',weight="bold",color=color4,fontsize=16)
    ax[1].text(xcenter+N/1.68,ycenter+N/1.45,'/',fontsize=16)
    ax[1].text(xcenter+N/1.59,ycenter+N/1.45,'left',weight="bold",color=color5,fontsize=16)
    
    ax[1].text(xcenter-N/1.7,ycenter+N/1.33,'Tile 2:',fontsize=16)
    ax[1].text(xcenter-N/2.5,ycenter+N/1.33,'Empty',weight="bold",color=color1,fontsize=16)
    ax[1].text(xcenter-N/5,ycenter+N/1.33,'/',fontsize=16)
    ax[1].text(xcenter-N/5.8,ycenter+N/1.33,'Ant facing',fontsize=16)
    ax[1].text(xcenter+N/8.8,ycenter+N/1.33,'up',weight="bold",color=color6,fontsize=16)
    ax[1].text(xcenter+N/5,ycenter+N/1.33,'/',fontsize=16)
    ax[1].text(xcenter+N/4.4,ycenter+N/1.33,'right',weight="bold",color=color7,fontsize=16)
    ax[1].text(xcenter+N/2.55,ycenter+N/1.33,'/',fontsize=16)
    ax[1].text(xcenter+N/2.37,ycenter+N/1.33,'down',weight="bold",color=color8,fontsize=16)
    ax[1].text(xcenter+N/1.68,ycenter+N/1.33,'/',fontsize=16)
    ax[1].text(xcenter+N/1.59,ycenter+N/1.33,'left',weight="bold",color=color9,fontsize=16)

    

##############################################
#### Welcome screen ####
aux_welcome=FuncAnimation(fig,initialize,frames=2,interval=1,init_func=init,repeat=False)
anim=FuncAnimation(fig,animate,frames=max_iter,interval=speed,init_func=init,repeat=False)


#### Buttons ####
update_GUI(paused)
plt.show()
