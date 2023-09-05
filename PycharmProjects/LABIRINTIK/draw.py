from tkinter import *
from support import *
#from PIL import Image, ImageTk


def draw_labik(mtx,canvas):
    otstupx=100
    otstupy=80
    for row, i in enumerate(mtx):
        for col, j in enumerate(i):
            if j == '-' or j == 'V-':
                if row == 0 or col == 0 or row == len(mtx) - 1 or col == len(i) - 1:
                    x = (col // 2) * (CELLRAZMER + WALLRAZMER) + otstupx+ WALLRAZMER
                    y = (row // 2) * (CELLRAZMER + WALLRAZMER) + otstupy
                    canvas.create_rectangle(
                        x, y, x + CELLRAZMER, y + WALLRAZMER,outline="black", fill="brown", width=2)

            elif j == '|' or j == 'V|':
                if row==0 or col==0 or row==len(mtx)-1 or col==len(i)-1:
                    x = (col // 2) * (CELLRAZMER + WALLRAZMER) + otstupx
                    y = (row // 2) * (CELLRAZMER + WALLRAZMER) + otstupy+ WALLRAZMER
                    canvas.create_rectangle(
                        x, y, x + WALLRAZMER, y + CELLRAZMER, outline="black", fill="brown", width=2)

            elif j == ' ' or j == 'H' or j == 'A' or j == 'K' or j[:-1]=='Dira':
                x = (col // 2) * (CELLRAZMER + WALLRAZMER)+otstupx+ WALLRAZMER
                y = (row // 2) * (CELLRAZMER + WALLRAZMER)+otstupy+ WALLRAZMER
                canvas.create_rectangle(x,y,x+CELLRAZMER,y+CELLRAZMER, outline="black", fill="green", width=2)
    canvas.pack(fill=BOTH, expand=1)

def draw_player(player,canvas):
    playery=player.pos[0]
    playerx=player.pos[1]
    x = (playerx // 2) * (CELLRAZMER + WALLRAZMER) + 100 + WALLRAZMER
    y = (playery // 2) * (CELLRAZMER + WALLRAZMER) + 80 + WALLRAZMER
    player.player_drawn=canvas.create_rectangle(x+15, y+15, x + PLAYERRAZMER, y + PLAYERRAZMER, outline="black", fill="red", width=2)
    canvas.pack(fill=BOTH, expand=1)
    return player.player_drawn



'''def add_map_3():
    pass
def add_map_5():
    labirint_painted.add_map_5()
    labirintik.add_map_5()
    labirintik.what_is_there(player_pos, player_pos, player_pos)
    labirint_painted.draw_player(player_pos)

menubar = Menu()
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="3x3", command=add_map_3)
fileMenu.add_command(label="5x5", command=add_map_5)
menubar.add_cascade(label="Клетки", menu=fileMenu)'''