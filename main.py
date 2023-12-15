import tkinter as tk
from PIL import Image, ImageTk

import manual_test as mt
import automatic_test as at

absolute_path = "C:/Users/domsp/Desktop/numato_manager/"
images_path = absolute_path + 'images/'

class NumatoMgr:
    def __init__(self):
        
        # Main window
        root = tk.Tk()
        root.title("Numato Manager")                                                        # Title
        root.iconbitmap(images_path + "numato_icon.ico")                                    # Main window icon        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        screen = {'w' : screen_width, 'h' : screen_height}
        window_width = root.winfo_width()
        window_height = root.winfo_height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2        
        root.geometry('{}x{}+{}+{}'.format(screen_width, screen_height, x, y))        

        # Size of both buttons
        button_width = screen_width // 2
        button_height = screen_height

        # Manual Test Button
        self.btn_manual = tk.Button(root, command=lambda: mt.on_btn_click(root, screen))
        self.img_uomo = tk.PhotoImage(file=images_path + "uomo.png")
        self.btn_manual.configure(background="red", compound="center", image=self.img_uomo, justify="left", takefocus=False)
        self.btn_manual.place(height=button_height, width=button_width, x=0, y=0)
       
        # Automatic Test Button
        self.btn_auto = tk.Button(root, command=lambda: at.on_btn_click(root, screen))
        self.img_robot = tk.PhotoImage(file=images_path + "robot.png")
        self.btn_auto.configure(background="blue", compound="center", default="normal", image=self.img_robot, justify="left")
        self.btn_auto.place(height=button_height, width=button_width, x=button_width, y=0)

        # Main widget
        self.mainwindow = root

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NumatoMgr()
    app.run()