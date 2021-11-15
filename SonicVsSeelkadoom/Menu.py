
from tkinter import *;

root = Tk();

label_title = Label(root, text="Sonic vs Seelkadoom");
label_title.pack();

def game():
    import sonicVSseelkadoom

button = Button(root, text="Begin", command=game)
button.pack();




root.mainloop();
