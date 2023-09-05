from tkinter import *
import time
from support import *
from PIL import Image, ImageTk
class LABIRINT():

    def __init__(self,window):
        self.window=window
        self.lbl = Label(self.window, text='')
        self.lbl.place(x=WIDTH // 2 - 10, y=HEIGHT - 200)
        self.player_alive=True
        self.player_klad=False
        self.VIHOD=False
        self.count=1
        self.sklad=False
        self.mtx = mtx_3
        self.Dira1 = mtx_3_Dira1
        self.robots = mtx_3_robots

    def write(self,text):
        self.lbl.place_forget()
        self.lbl = Label(self.window, text=text, font='Times 18')
        self.lbl.place(x=50, y=HEIGHT -300)

    def zona_robot(self,player):
        print(self.robots)
        for robot in self.robots.values():
            if robot[2]:    #robot[2]- alive  or not
                if player.pos[0] == robot[0] and player.pos[1] == robot[1] and self.player_alive:
                    self.write('Вас съел робот. Ищите больницу. \nПока вы не можете стрелять, взрывать стенки и забирать клад.')
                    self.player_alive = False
                elif (player.pos[1] - robot[1] <= 3 or player.pos[0] - robot[0] <= 3) and self.player_alive:
                    self.robot_lbl = Label(self.window, text='Вы в ЗОНЕ действия РОБОТА', font='Times 18')
                    self.robot_lbl.place(x=50, y=HEIGHT -100)


                    #robot movement
                    print(f'Here I am. Robot: {robot}')
                    if player.pos[1] - robot[1] < 0 and self.mtx[robot[0]][robot[1]-1] == '+':
                        robot[1] -= 2
                        print('robot moves left')
                    elif player.pos[1] - robot[1] > 0 and self.mtx[robot[0]][robot[1]+1] == '+':
                        robot[1] += 2
                        print('robot moves right')
                    elif player.pos[0] - robot[0] < 0 and  self.mtx[robot[0] - 1][robot[0]] == '+':
                        robot[0] -= 2
                        print('robot moves up')
                    elif player.pos[0] - robot[0] < 0 and self.mtx[robot[0] + 1][robot[0]] == '+':
                        robot[0] += 2
                        print('moves down')
                    print(f'Now I am here. Robot: {robot}')
                else:
                    self.robot_lbl = Label(self.window, text='Вы вне ЗОНЫ действия РОБОТА', font='Times 18')
                    self.robot_lbl.place(x=50, y=HEIGHT -100)
            else:
                self.robot_lbl.place_forget()
    def what_is_there(self,player,for_stenka,for_step,canvas):
        stenka_or_not_stenka=self.mtx[for_stenka[0]][for_stenka[1]]
        try:
            if stenka_or_not_stenka == '-':
                x = (for_stenka[1] // 2) * (CELLRAZMER + WALLRAZMER) + 100  + WALLRAZMER
                y = (for_stenka[0] // 2) * (CELLRAZMER + WALLRAZMER) + 80
                canvas.create_rectangle(x, y, x + CELLRAZMER, y + WALLRAZMER, outline="black", fill="brown", width=2)
                canvas.pack(fill=BOTH, expand=1)
                self.write('Стенка. Походите снова.')
                player=player.pos
                return player
            elif stenka_or_not_stenka == '|':
                x = (for_stenka[1] // 2) * (CELLRAZMER + WALLRAZMER) + 100
                y = (for_stenka[0] // 2) * (CELLRAZMER + WALLRAZMER) + 80  + WALLRAZMER
                canvas.create_rectangle(x, y, x + WALLRAZMER, y + CELLRAZMER, outline="black", fill="brown", width=2)
                canvas.pack(fill=BOTH, expand=1)
                self.write('Стенка. Походите снова.')
                player = player.pos
                return player


            elif stenka_or_not_stenka[0] == 'V' and self.player_klad:
                self.write('ПОЗДРАВЛЯЮ, ВЫ ВЫИГРАЛИ!!')
                time.sleep(3)
                self.window.destroy()
                return for_step
            else:
                if stenka_or_not_stenka[0] == 'V' and self.count % 2 != 0:
                    self.write('Выход из лабиринта')
                    self.VIHOD = True
                    self.count += 1
                else:
                    self.VIHOD = False

                if self.mtx[for_step[0]][for_step[1]] == 'H':
                    self.write('Больница')
                    x = (for_step[1] // 2) * (CELLRAZMER + WALLRAZMER) + 100 + WALLRAZMER
                    y = (for_step[0] // 2) * (CELLRAZMER + WALLRAZMER) + 80 + WALLRAZMER
                    canvas.create_rectangle(x + 15, y + 15, x + PLAYERRAZMER, y + PLAYERRAZMER, outline="black",
                                            fill="purple", width=2)
                    canvas.pack(fill=BOTH, expand=1)
                    if not self.player_alive:
                        self.write('Больница. Вы ожили. Отправляйтесь за кладом!')
                        self.player_alive = True
                    return for_step
                elif self.mtx[for_step[0]][for_step[1]] == 'A':
                    self.write('Склад')
                    self.sklad = True
                    x = (for_step[1] // 2) * (CELLRAZMER + WALLRAZMER) + 100 + WALLRAZMER
                    y = (for_step[0] // 2) * (CELLRAZMER + WALLRAZMER) + 80 + WALLRAZMER
                    canvas.create_rectangle(x + 15, y + 15, x + PLAYERRAZMER, y + PLAYERRAZMER, outline="black",
                                            fill="blue", width=2)
                    canvas.pack(fill=BOTH, expand=1)
                    return for_step
                elif self.mtx[for_step[0]][for_step[1]] == 'K':
                    self.write('Клад')
                    self.player_klad = True
                    x = (for_step[1] // 2) * (CELLRAZMER + WALLRAZMER) + 100 + WALLRAZMER
                    y = (for_step[0] // 2) * (CELLRAZMER + WALLRAZMER) + 80 + WALLRAZMER
                    canvas.create_rectangle(x + 15, y + 15, x + PLAYERRAZMER, y + PLAYERRAZMER, outline="black",
                                            fill="black", width=2)
                    canvas.pack(fill=BOTH, expand=1)
                    return for_step
                if self.mtx[for_step[1]][for_step[0]] == 'Dira1':
                    def fly(event):
                        player.pos = self.Dira1[str(player.pos[0]) + str(player.pos[1])]
                        print('IN THE HOLE. HERE I AM', player.pos)
                        self.write('Дыра. Летите снова? Нажмите L. не летите?')
                        return player.pos
                    self.write('Дыра. Летите снова? Нажмите L. не летите?')
                    player.pos=self.Dira1[str(for_step[0]) + str(for_step[1])]
                    canvas.pack(fill=BOTH, expand=1)
                    self.window.bind("<l>", fly)
                    print('IN THE HOLE. HERE I AM',player.pos)
                    return player.pos
                else:
                    self.write('Прошли')
                    return for_step
                self.zona_robot(player)
        except IndexError:
            self.write('Здесь предел лабиринта. Дальше нет прохода. Походите обратно')