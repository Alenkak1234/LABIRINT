from tkinter import *
from support import *

from PIL import Image, ImageTk
class Bomb():
    def __init__(self,window,labirintik):
        self.window=window
        self.labirintik=labirintik
        bomb_downl = Image.open("C:/Users/79775/PycharmProjects/LABIRINTIK/bomb_im.png")
        bomb_img = bomb_downl.resize((30, 30))
        self.bomb_img = ImageTk.PhotoImage(bomb_img)
        self.bomb_nmb = 3
        self.bul_nmb = 3

    def update(self,player,labirintik,canvas):
        def press_btn():
            if labirintik.player_alive:
                def blow_up(event):
                    print("еСЛИ НЕ ПОЛУЧИЛОСЬ, ПЕРЕВЕДИТЕ НА АНГЛИйСКУЮ КЛАВИАТУРУ")
                    s = 1
                    step = 2
                    def popal(for_stenka_x,for_stenka_y,for_step):
                        if mtx_3[for_stenka_y][for_stenka_x] == '|' or mtx_3[for_stenka_y][for_stenka_x] == '-':
                            mtx_3[for_stenka_y][for_stenka_x] = '+'
                            print(*mtx_3,sep='\n')
                            player.pos = for_step
                            print(player.pos)
                            labirintik.what_is_there(player,player.pos,for_step,canvas)
                            if labirintik.sklad:
                                self.bomb_nmb +=3
                                self.bomb_nmb +=3
                                labirintik.sklad = False
                            labirintik.zona_robot(player)
                    if event.keysym == 'a':
                        for_stenka_x = player.pos[1] - s
                        for_stenka_y = player.pos[0]
                        for_step = [player.pos[0], player.pos[1] - step]
                        if for_stenka_x!=0:
                            popal(for_stenka_x, for_stenka_y,for_step)
                        else:
                            labirintik.write('Капитальная стенка')
                    elif event.keysym == 's':
                        for_stenka_x = player.pos[1] + s
                        for_stenka_y = player.pos[0]
                        for_step = [player.pos[0], player.pos[1]+step]
                        if for_stenka_x != len(mtx_3)-1:
                            popal(for_stenka_x,for_stenka_y,for_step)
                        else:
                            labirintik.write('Капитальная стенка')
                    elif event.keysym == 'w':
                        for_stenka_x = player.pos[1]
                        for_stenka_y = player.pos[0] - s
                        for_step = [player.pos[0] - step, player.pos[1]]
                        if for_stenka_y != 0:
                            popal(for_stenka_x, for_stenka_y,for_step)
                        else:
                            labirintik.write('Капитальная стенка')
                    elif event.keysym == 'z':
                        for_stenka_x = player.pos[1]
                        for_stenka_y = player.pos[0] + s
                        for_step = [player.pos[0] + step, player.pos[1]]
                        if for_stenka_y != len(mtx_3) - 1:
                            popal(for_stenka_x,for_stenka_y,for_step)
                        else:
                            labirintik.write('Капитальная стенка')
                    self.window.unbind("<a>")
                    self.window.unbind("<s>")
                    self.window.unbind("<w>")
                    self.window.unbind("<z>")
                if self.bomb_nmb>=1:
                    self.bomb_nmb -= 1
                    displ_bomb_nmb()
                    labirintik.write('Куда кинуть? a-Лево, s - Право, w - Вверх, z - Вниз')
                    self.window.bind("<a>", blow_up)
                    self.window.bind("<s>", blow_up)
                    self.window.bind("<w>", blow_up)
                    self.window.bind("<z>", blow_up)
                else:
                    displ_bomb_nmb()
                    labirintik.write('Бомбы закончились. Походите')
            else:
                labirintik.write('Вы не можете кидать бомбы. Найдите больницу')

        def displ_bomb_nmb():
            bombs_lbl=Label(self.window,text=self.bomb_nmb)
            bombs_lbl.place(x=20,y=15)
        displ_bomb_nmb()
        b = Button(self.window, image=self.bomb_img, command=press_btn)
        b.place(x=50, y=10)