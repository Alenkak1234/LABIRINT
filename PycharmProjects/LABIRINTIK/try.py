from tkinter import *
window=Tk()
canvas=Canvas()
PLAYERRAZMER=50
player=canvas.create_rectangle(100+15, 100+15, 100 + PLAYERRAZMER, 100 + PLAYERRAZMER, outline="black", fill="red", width=2)
canvas.pack(fill=BOTH, expand=1)
canvas.delete(player)
window.mainloop()