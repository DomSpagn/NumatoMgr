from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, BooleanVar

import utilities as ut

OUTPUT_PATH = Path(__file__).parent

# Laptop
#PANEL_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\automatic\panel")
#TEST_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\automatic\test")

# Desktop
PANEL_PATH = OUTPUT_PATH / Path(r"C:\Users\domsp\Desktop\numato_manager\images\automatic\panel")
TEST_PATH = OUTPUT_PATH / Path(r"C:\Users\domsp\Desktop\numato_manager\images\automatic\test")

def get_panel_path(path: str) -> Path:
    return PANEL_PATH / Path(path)

def get_test_path(path: str) -> Path:
    return TEST_PATH / Path(path)

class AutomaticTestPanel:
    def __init__(self, cover_window):
        self.canvas = Canvas(cover_window, bg="#000000", height=1017, width=480, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Serial COM Settings Section
        self.canvas.create_text(99.0, 11.0, anchor="nw", text="Serial COM Settings", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        self.button_img_select_com = PhotoImage(file=get_panel_path("select_com.png"))
        self.button_select_com = Button(image=self.button_img_select_com, borderwidth=0, highlightthickness=0, command=lambda: print("button_select_com clicked"), relief="flat")
        self.button_select_com.place(x=163.0, y=77.0, width=153.0, height=39.0)

        self.button_img_select_baudrate = PhotoImage(file=get_panel_path("select_baudrate.png"))
        self.button_select_baudrate = Button(image=self.button_img_select_baudrate, borderwidth=0, highlightthickness=0, command=lambda: print("button_select_baudrate clicked"), relief="flat")
        self.button_select_baudrate.place(x=163.0, y=147.0, width=153.0, height=39.0)

        # First Blue Line
        self.canvas.create_rectangle(0, 230.0, 480.0015869140625, 230.0, fill="#0000FF", outline="")

        # Relays Section
        self.canvas.create_text(193.0, 241.0, anchor="nw", text="Relays", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        self.button_img_relay_1 = PhotoImage(file=get_panel_path("relay_1.png"))
        self.button_relay_1 = Button(image=self.button_img_relay_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_1 clicked"), relief="flat")
        self.button_relay_1.place(x=165.0, y=306.0, width=30.0, height=30.0)

        self.button_img_relay_2 = PhotoImage(file=get_panel_path("relay_2.png"))
        self.button_relay_2 = Button(image=self.button_img_relay_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_2 clicked"), relief="flat")
        self.button_relay_2.place(x=205.0, y=306.0, width=30.0, height=30.0)

        self.button_img_relay_3 = PhotoImage(file=get_panel_path("relay_3.png"))
        self.button_relay_3 = Button(image=self.button_img_relay_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_3 clicked"), relief="flat")
        self.button_relay_3.place(x=245.0, y=306.0, width=30.0, height=30.0)

        self.button_img_relay_4 = PhotoImage(file=get_panel_path("relay_4.png"))
        self.button_relay_4 = Button(image=self.button_img_relay_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_4 clicked"), relief="flat")
        self.button_relay_4.place(x=285.0, y=306.0, width=30.0, height=30.0)

        self.button_img_relay_5 = PhotoImage(file=get_panel_path("relay_5.png"))
        self.button_relay_5 = Button(image=self.button_img_relay_5, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_5 clicked"), relief="flat")
        self.button_relay_5.place(x=165.0, y=346.0, width=30.0, height=30.0)

        self.button_img_relay_6 = PhotoImage(file=get_panel_path("relay_6.png"))
        self.button_relay_6 = Button(image=self.button_img_relay_6, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_6 clicked"), relief="flat")
        self.button_relay_6.place(x=205.0, y=346.0, width=30.0, height=30.0)

        self.button_img_relay_7 = PhotoImage(file=get_panel_path("relay_7.png"))
        self.button_relay_7 = Button(image=self.button_img_relay_7, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_7 clicked"), relief="flat")
        self.button_relay_7.place(x=245.0, y=346.0, width=30.0, height=30.0)

        self.button_img_relay_8 = PhotoImage(file=get_panel_path("relay_8.png"))
        self.button_relay_8 = Button(image=self.button_img_relay_8, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_8 clicked"), relief="flat")
        self.button_relay_8.place(x=285.0, y=346.0, width=30.0, height=30.0)

        self.button_img_relay_9 = PhotoImage(file=get_panel_path("relay_9.png"))
        self.button_relay_9 = Button(image=self.button_img_relay_9, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_9 clicked"), relief="flat")
        self.button_relay_9.place(x=165.0, y=386.0, width=30.0, height=30.0)

        self.button_img_relay_10 = PhotoImage(file=get_panel_path("relay_10.png"))
        self.button_relay_10 = Button(image=self.button_img_relay_10, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_10 clicked"), relief="flat")
        self.button_relay_10.place(x=205.0, y=386.0, width=30.0, height=30.0)

        self.button_img_relay_11 = PhotoImage(file=get_panel_path("relay_11.png"))
        self.button_relay_11 = Button(image=self.button_img_relay_11, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_11 clicked"), relief="flat")
        self.button_relay_11.place(x=245.0, y=386.0, width=30.0, height=30.0)

        self.button_img_relay_12 = PhotoImage(file=get_panel_path("relay_12.png"))
        self.button_relay_12 = Button(image=self.button_img_relay_12, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_12 clicked"), relief="flat")
        self.button_relay_12.place(x=285.0, y=386.0, width=30.0, height=30.0)

        self.button_img_relay_13 = PhotoImage(file=get_panel_path("relay_13.png"))
        self.button_relay_13 = Button(image=self.button_img_relay_13, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_13 clicked"), relief="flat")
        self.button_relay_13.place(x=165.0, y=426.0, width=30.0, height=30.0)

        self.button_img_relay_14 = PhotoImage(file=get_panel_path("relay_14.png"))
        self.button_relay_14 = Button(image=self.button_img_relay_14, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_14 clicked"), relief="flat")
        self.button_relay_14.place(x=205.0, y=426.0, width=30.0, height=30.0)

        self.button_img_relay_15 = PhotoImage(file=get_panel_path("relay_15.png"))
        self.button_relay_15 = Button(image=self.button_img_relay_15, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_15 clicked"), relief="flat")
        self.button_relay_15.place(x=245.0, y=426.0, width=30.0, height=30.0)

        self.button_img_relay_16 = PhotoImage(file=get_panel_path("relay_16.png"))
        self.button_relay_16 = Button(image=self.button_img_relay_16, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_16 clicked"), relief="flat")
        self.button_relay_16.place(x=285.0, y=426.0, width=30.0, height=30.0)

        self.canvas.create_text(190.0, 494.0, anchor="nw", text="Select All", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.relays_var = BooleanVar()
        self.button_check_relays = Checkbutton(self.canvas, bg='#000000', variable=self.relays_var, onvalue=True, offvalue=False, command=lambda: print("relay check box clicked"))
        self.button_check_relays.place(x=272, y=493)

        # Second Blue Line
        self.canvas.create_rectangle(0, 550.0, 480.0015869140625, 550.0, fill="#0000FF", outline="")

        # GPIOs Section
        self.canvas.create_text(196.0, 558.0, anchor="nw", text="GPIOs", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        self.button_img_gpio_0 = PhotoImage(file=get_panel_path("gpio_0.png"))
        self.button_gpio_0 = Button(image=self.button_img_gpio_0, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_0 clicked"), relief="flat")
        self.button_gpio_0.place(x=147.0, y=698.0, width=36.0, height=36.0)

        self.button_img_gpio_1 = PhotoImage(file=get_panel_path("gpio_1.png"))
        self.button_gpio_1 = Button(image=self.button_img_gpio_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_1 clicked"), relief="flat")
        self.button_gpio_1.place(x=170.0, y=648.0, width=36.0, height=36.0)

        self.button_img_gpio_2 = PhotoImage(file=get_panel_path("gpio_2.png"))
        self.button_gpio_2 = Button(image=self.button_img_gpio_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_2 clicked"),relief="flat")
        self.button_gpio_2.place(x=222.0, y=623.0, width=36.0, height=36.0)

        self.button_img_gpio_3 = PhotoImage(file=get_panel_path("gpio_3.png"))
        self.button_gpio_3 = Button(image=self.button_img_gpio_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_3 clicked"), relief="flat")
        self.button_gpio_3.place(x=271.0, y=648.0, width=36.0, height=36.0)

        self.button_img_gpio_4 = PhotoImage(file=get_panel_path("gpio_4.png"))
        self.button_gpio_4 = Button(image=self.button_img_gpio_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_4 clicked"), relief="flat")
        self.button_gpio_4.place(x=296.0, y=698.0, width=36.0, height=36.0)

        self.button_img_gpio_5 = PhotoImage(file=get_panel_path("gpio_5.png"))
        self.button_gpio_5 = Button(image=self.button_img_gpio_5, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_5 clicked"), relief="flat")
        self.button_gpio_5.place(x=271.0, y=747.0, width=36.0, height=36.0)

        self.button_img_gpio_6 = PhotoImage(file=get_panel_path("gpio_6.png"))
        self.button_gpio_6 = Button(image=self.button_img_gpio_6, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_6 clicked"), relief="flat")
        self.button_gpio_6.place(x=222.0, y=773.0, width=36.0, height=36.0)

        self.button_img_gpio_7 = PhotoImage(file=get_panel_path("gpio_7.png"))
        self.button_gpio_7 = Button(image=self.button_img_gpio_7, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_7 clicked"), relief="flat")
        self.button_gpio_7.place(x=170.0, y=747.0, width=36.0, height=36.0)

        self.canvas.create_text(190.0, 846.0, anchor="nw", text="Select All", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.gpios_var = BooleanVar()
        self.button_check_relays = Checkbutton(self.canvas, bg='#000000', variable=self.gpios_var, onvalue=True, offvalue=False, command=lambda: print("gpio check box clicked"))
        self.button_check_relays.place(x=272, y=845)

        # Third Blue Line
        self.canvas.create_rectangle(0, 902.0, 480.0015869140625, 902.0, fill="#0000FF", outline="")

        # Iterations Section
        self.canvas.create_text(168.0, 912.0, anchor="nw", text="Iterations", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        self.canvas.create_text(159.0, 965.0, anchor="nw", text="Number: ", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry.place(x=244.0, y=965.0, width=50.0, height=20.0)
        

    def on_com_select(self, event):
        selected_value = self.com_var.get()
        print(f"Selected COM: {selected_value}")
        
    def on_baudrate_select(self, event):
        selected_value = self.baudrate_var.get()
        print(f"Selected Baudrate: {selected_value}")
    
    def run(self):
        self.mainwindow.mainloop() 
        
    
def on_btn_click(cover_window):
    ut.clear_current_window(cover_window)
    panel = AutomaticTestPanel(cover_window)
    panel.run()    
