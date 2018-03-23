import tkinter
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from image_manager import ImageManager
from color_converter import ColorConverter
import pdb

class GUI:
    def __init__(self, manager = None):
        self.top = tkinter.Tk()
        self.top.title("Image Editor")
        self.manager = manager
        self.image = None
        self.width = 900
        self.height = 900
        self.canvas = tkinter.Canvas(self.top, width=self.width, height=self.height)

    def create_main_loop(self):
        self.top.mainloop()

    def create_file_menu(self, menubar):
        file_menu = tkinter.Menu(menubar)
        file_menu.add_command(label='print')
        file_menu.add_command(label='open', command=self.__open_file_browser)
        return file_menu

    def create_edit_menu(self, menubar):
        edit_menu = tkinter.Menu(menubar)
        edit_menu.add_command(label='grayscale', command=self.make_grayscale)
        edit_menu.add_command(label='RGB', command=self.make_RGB)
        return edit_menu

    def make_grayscale(self):
        self.add_image(self.manager.return_img(), 'to_grayscale')

    def make_RGB(self):
        # Dont need to pass in any argument with current implementation. It will return the managers stored image which is rgb
        self.add_image(self.manager.return_img())

    def create_menu(self):
        menubar = tkinter.Menu(self.top)
        file_menu = self.create_file_menu(menubar)
        edit_menu = self.create_edit_menu(menubar)
        menubar.add_cascade(label='file', menu=file_menu)
        menubar.add_cascade(label='edit', menu=edit_menu)
        self.top.config(menu=menubar)

    def create_menu_button(self):
        w = tkinter.Menubutton(self.top, text='Menu').pack()

    def set_labels(self):
        w = tkinter.Label(self.top, text='Hello!').pack()

    def add_image(self, image, converter='to_RGB'):
        self.canvas.delete("all")
        imgtk = self.__create_valid_image_object_from_cv2(image, converter)
        self.canvas.create_image(self.width / 2, self.height / 2, image=imgtk)
        self.canvas.image = imgtk
        self.canvas.pack()
    # Private

    def __create_valid_image_object_from_cv2(self, image, converter):
        im = Image.fromarray(self.manager.convert(converter))
        return ImageTk.PhotoImage(im)

    def __open_file_browser(self):
        filename = askopenfilename()
        image = self.manager.upload(filename)
        self.add_image(image)
