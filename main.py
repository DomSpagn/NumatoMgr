'''
GUI works just for a Full HD (1920x1080) screen resolution
'''

# This file was generated by the Tkinter Designer
from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Button, PhotoImage

import manual_test as mt
import automatic_test as at

OUTPUT_PATH = Path(__file__).parent

# Laptop
ICON_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\icon")
COVER_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\cover")

# Desktop
#ICON_PATH = OUTPUT_PATH / Path(r"C:\Users\domsp\Desktop\numato_manager\images\icon")
#COVER_PATH = OUTPUT_PATH / Path(r"C:\Users\domsp\Desktop\numato_manager\images\cover")

def get_icon_path(path: str) -> Path:
    return ICON_PATH / Path(path)

def get_cover_path(path: str) -> Path:
    return COVER_PATH / Path(path)

class NumatoMgr:
    def __init__(self):
                
        # Main window
        root = Tk()
        self.mainwindow = root        
        self.mainwindow.title("Numato Manager")
        self.mainwindow.iconbitmap(get_icon_path("numato_icon.ico"))        
        self.screen_width = 1920
        self.screen_height = 1080
        self.mainwindow.geometry('{}x{}+{}+{}'.format(self.screen_width, self.screen_height, 0, 0))
        self.mainwindow.configure(bg = "#FFFFFF")
                
        # Manual Test Button
        self.manual_button_img = PhotoImage(file=get_cover_path("manual.png"))
        self.manual_button = Button(image=self.manual_button_img, borderwidth=0, highlightthickness=0, command=lambda: mt.on_btn_click(root), relief="flat", background="#FF0000")
        self.manual_button.place(x=0.0, y=0.0, width=self.screen_width//2, height=self.screen_height)

        # Automatic Test Button
        self.auto_button_img = PhotoImage(file=get_cover_path("auto.png"))
        self.auto_button = Button(image=self.auto_button_img, borderwidth=0, highlightthickness=0, command=lambda: at.on_btn_click(root), relief="flat", background="#0000FF")
        self.auto_button.place(x=self.screen_width//2, y=0.0, width=self.screen_width//2, height=self.screen_height)        

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NumatoMgr()
    app.run()