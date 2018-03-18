import tkinter
from PIL import Image, ImageTk

class GUI:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title("Test")

    def create_main_loop(self):
        self.top.mainloop()

    def set_labels(self):
        w = tkinter.Label(self.top, text='Hello!')
        w.pack()

    def create_canvas(self, image):
        im = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(im)
        label = tkinter.Label(self.top, image=imgtk)
        label.image = imgtk
        label.pack()
        # FigureCanvasTkAgg(figure, master=self.top).draw()
