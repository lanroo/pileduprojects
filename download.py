
from tkinter import *
from tkinter import filedialog

screen = Tk()
title = screen.title('Youtube Download')
Canvas = Canvas(screen, width=500, height=500)
Canvas.pack()

# image Logo

logo_img = PhotoImage(file='yt.png')

Canvas.create_image(250, 80, image=logo_img)



screen.mainloop()