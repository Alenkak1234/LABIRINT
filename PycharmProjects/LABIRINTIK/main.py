#когда пишу эл, не хочет показывать игрока, но переносит его в другую дырку.


from labirint import *
from bomb import *
from bullet import *
from draw import *
from support import *
from player import Player

window = Tk()
window.title('ЛАБИРИНТ')
window.geometry(str(WIDTH) + 'x' + str(HEIGHT))
canvas=Canvas
player_dict={'masha': [1, 5], 'fedya': [3, 1]}
iter_names=iter(player_dict)
iter_pos=iter(player_dict.values())
def main_game(name_pos):
    def takes_a_step(event):
        s = 1
        step = 2
        player.player_drawn
        # !!!!!           помни, что сначала y-строки матрицы, x-столбцы матрицы
        if event.keysym == 'Right':
            for_stenka = [player.pos[0], player.pos[1] + s]
            for_step = [player.pos[0], player.pos[1] + step]
        elif event.keysym == 'Down':
            for_stenka = [player.pos[0] + s, player.pos[1]]
            for_step = [player.pos[0] + step, player.pos[1]]
        elif event.keysym == 'Up':
            for_stenka = [player.pos[0] - s, player.pos[1]]
            for_step = [player.pos[0] - step, player.pos[1]]
        elif event.keysym == 'Left':
            for_stenka = [player.pos[0], player.pos[1] - s]
            for_step = [player.pos[0], player.pos[1] - step]
        canvas.delete(player.player_drawn)
        player.player_drawn = draw_player(player, canvas)
        player.pos = labirintik.what_is_there(player, for_stenka, for_step, canvas)
        canvas.delete(player.player_drawn)
        player.player_drawn = draw_player(player, canvas)
        global bomb_nmb, bul_nmb
        if labirintik.sklad:
            bomb.bomb_nmb += 3
            bullet.bul_nmb += 3
            labirintik.sklad = False
        bomb.update(player, labirintik, canvas)
        bullet.update(player, labirintik)
        labirintik.zona_robot(player)
        print(f'Here is robot {labirintik.robots}')
        print(f'Here is player {player.pos}')
        return player.pos

    player = Player()
    player.pos = name_pos
    action_lbl = Label(window, text='Ваше действие?', font='Times 30')
    action_lbl.pack()

    canvas = Canvas()
    labirintik = LABIRINT(window)
    labirintik.what_is_there(player.pos, player.pos, player.pos, canvas)
    draw_labik(mtx_3, canvas)
    player.player_drawn = draw_player(player, canvas)

    bomb = Bomb(window, labirintik)
    bullet = Bullet(window, labirintik)
    if labirintik.sklad:
        bomb.bomb_nmb += 3
        bullet.bul_nmb += 3
        labirintik.sklad = False
    bomb.update(player, labirintik, canvas)
    bullet.update(player, labirintik)

    window.bind("<Right>", takes_a_step)
    window.bind("<Down>", takes_a_step)
    window.bind("<Up>", takes_a_step)
    window.bind("<Left>", takes_a_step)


def player_change(iter_names):
    global iter_pos
    try:
        new_pos=next(iter_pos)
        new_player = next(iter_names)
    except:
        iter_pos = iter(player_dict.values())
        new_pos = next(iter_pos)
        iter_names = iter(player_dict)
        new_player = next(iter_names)
    print(new_pos)
    print(f'This is new player: {new_pos}, {new_player}')
    player_dict[new_player] = main_game(new_pos)
player_change(iter_names)
window.mainloop()