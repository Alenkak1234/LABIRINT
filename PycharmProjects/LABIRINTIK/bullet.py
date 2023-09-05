from tkinter import *
from support import direction_list
from PIL import Image, ImageTk

class Bullet():
    def __init__(self,window,labirintik):
        self.window=window
        self.labirintik=labirintik
        bullet_downl = Image.open("C:/Users/79775/PycharmProjects/LABIRINTIK/bullet_img.png")
        bullet_img = bullet_downl.resize((30, 30))
        self.bullet_img = ImageTk.PhotoImage(bullet_img)
        self.bul_nmb=3

    def update(self,player,labirintik):
        def press_btn():
            if labirintik.player_alive:
                def blow_up(event):
                    bullet_pos=[player.pos[0],player.pos[1]]
                    def letit(uskorenieX,uskorenieY):
                        bullet_pos[0] += uskorenieY
                        bullet_pos[1] += uskorenieX
                        print(bullet_pos)
                        while labirintik.mtx[bullet_pos[0]][bullet_pos[1]] != '-' or labirintik.mtx[bullet_pos[0]][
                            bullet_pos[1]] != '|':
                            if player.pos == bullet_pos:
                                labirintik.write('You killed a player')
                                #labirintik.player_alive = False
                                break
                            for robot in labirintik.robots.values():
                                print(robot)
                                if robot[1] == bullet_pos:
                                    labirintik.write('You killed a robot')
                                    robot[2] = False
                                    break
                            bullet_pos[0] += uskorenieY
                            bullet_pos[1] += uskorenieX
                            print(f'POSITION OF THE BULLET {bullet_pos}')


                    if event.keysym == 'a':
                        uskorenieX = -1
                        uskorenieY = 0
                        letit(uskorenieX,uskorenieY)
                    elif event.keysym == 's':
                        uskorenieX = 1
                        uskorenieY = 0
                        letit(uskorenieX, uskorenieY)
                    elif event.keysym == 'h':
                        if player.pos == bullet_pos:
                            labirintik.write('You killed a player')
                            labirintik.player_alive = False
                        for robot in labirintik.robots.values():
                            if robot == bullet_pos:
                                labirintik.write('You killed a robot')
                                robot[2] = False
                        else:
                            print('NOONE DIED')

                    elif event.keysym == 'w':
                        uskorenieX = 0
                        uskorenieY = -1
                        letit(uskorenieX, uskorenieY)
                    elif event.keysym == 'z':
                        uskorenieX = 0
                        uskorenieY = 1
                        letit(uskorenieX, uskorenieY)

                    self.window.unbind("<a>")
                    self.window.unbind("<s>")
                    self.window.unbind("<w>")
                    self.window.unbind("<z>")
                    self.window.unbind("<h>")
                if self.bul_nmb>=1:
                    self.bul_nmb -= 1
                    displ_bul_nmb()
                    labirintik.write('Куда стрелять? a-Лево, s - Право, w - Вверх, z - Вниз, h - в свою клетку')
                    map(lambda i: self.window.bind(i, blow_up), direction_list)
                    self.window.bind("<a>", blow_up)
                    self.window.bind("<s>", blow_up)
                    self.window.bind("<w>", blow_up)
                    self.window.bind("<z>", blow_up)
                    self.window.bind("<h>", blow_up)
                else:
                    displ_bul_nmb()
                    labirintik.write('Пули закончились. Походите')
            else:
                labirintik.write('Вы не можете стрелять. Найдите больницу')
        def displ_bul_nmb():
            bul_lbl=Label(self.window,text=self.bul_nmb)
            bul_lbl.place(x=20,y=55)
        displ_bul_nmb()
        b = Button(self.window, image=self.bullet_img, command=press_btn)
        b.place(x=50, y=50)