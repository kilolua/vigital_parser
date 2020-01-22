from tkinter import *

root = Tk()


platform = Label(root, text='Площадки:')
platform.grid(row=0, column=0, sticky=N)

vk_ch = Checkbutton(root)
vk_ch.grid(row=1, column=1, sticky=N)
yt_ch = Checkbutton(root)
yt_ch.grid(row=2, column=1, sticky=N)
vk_lb = Label(root, text='VK:')
vk_lb.grid(row=1, column=0, sticky=N)
yt_lb = Label(root, text='YOUTUBE:')
yt_lb.grid(row=2, column=0, sticky=N)

inp_lb = Label(root, text='Входные данные:', font=('arial', 20))
inp_lb.grid(row=0, column=2)
inp = Text(root, width=100, height=20)
inp.grid(row=1, column=2, rowspan=3)

btn = Button(root, text='Сгенерировать')
btn.grid(row=3, column=0, sticky=N)

root.mainloop()