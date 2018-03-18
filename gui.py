import tkinter
from PIL import Image, ImageTk

class GUI:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title("Test")

    def create_main_loop(self):
        self.top.mainloop()

    def create_menu(self):
        menubar = tkinter.Menu(self.top)
        file_menu = tkinter.Menu(menubar)
        menubar.add_cascade(label='file', menu=file_menu)
        file_menu.add_command(label='print')
        self.top.config(menu=menubar)

    def create_menu_button(self):
        w = tkinter.Menubutton(self.top, text='Menu').pack()

    def set_labels(self):
        w = tkinter.Label(self.top, text='Hello!').pack()

    def add_image(self, image):
        im = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(im)
        label = tkinter.Label(self.top, image=imgtk)
        label.image = imgtk
        label.pack()
