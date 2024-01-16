from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, OptionMenu, Button, PhotoImage, Checkbutton, BooleanVar, StringVar

import utilities as ut

OUTPUT_PATH = Path(__file__).parent

# Laptop
PANEL_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\automatic\panel")
TEST_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\automatic\test")

# Desktop
#PANEL_PATH = OUTPUT_PATH / Path(r"C:\Users\domsp\Desktop\numato_manager\images\automatic\panel")
#TEST_PATH = OUTPUT_PATH / Path(r"C:\Users\domsp\Desktop\numato_manager\images\automatic\test")


class AutomaticTestPanel:
    def __init__(self, cover_window):
        self.mainwindow = cover_window

        self.canvas = Canvas(self.mainwindow, bg="#000000", height=1017, width=480, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Serial COM Settings Section
        self.canvas.create_text(108.0, 11.0, anchor="nw", text="Serial COM Settings", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        # Select COM Dropdown Menu
        self.com_var = StringVar(self.canvas)
        self.com_var.set("Select COM")
        self.select_com_dropdown_menu = OptionMenu(self.canvas, self.com_var, "      COM1      ", 
                                                                              "      COM2      ", 
                                                                              "      COM3      ", 
                                                                              "      COM4      ", 
                                                                              "      COM14      ", 
                                                                              "      COM255      ")
        self.select_com_dropdown_menu.config(width=12, height=1, anchor='center', font=('Inter', 14))
        self.com_menu = self.select_com_dropdown_menu.nametowidget(self.select_com_dropdown_menu.menuname)
        self.com_menu.configure(font=('Inter', 14))
        self.select_com_dropdown_menu.place(x=152, y=77)
        self.select_com_dropdown_menu.bind("<Configure>", self.on_com_select)

        # Select Baudrate Dropdown Menu
        self.baudrate_var = StringVar(self.canvas)
        self.baudrate_var.set("Select Baudrate")
        self.select_com_dropdown_menu = OptionMenu(self.canvas, self.baudrate_var, "   2400 bps  ", 
                                                                                   "   4800 bps  ", 
                                                                                   "   9600 bps  ", 
                                                                                   "   19200 bps  ", 
                                                                                   "   38400 bps  ", 
                                                                                   "   57600 bps  ", 
                                                                                   "   115200 bps  ",
                                                                                   "   230400 bps  ", 
                                                                                   "   460800 bps  ",
                                                                                   "   500000 bps  ",
                                                                                   "   576000 bps  ",
                                                                                   "   921600 bps  ",
                                                                                   "   1000000 bps  ")

        self.select_com_dropdown_menu.config(width=12, height=1, anchor='center', font=('Inter', 14))  # Impostazione larghezza e altezza del bottone
        self.com_menu = self.select_com_dropdown_menu.nametowidget(self.select_com_dropdown_menu.menuname)
        self.com_menu.configure(font=('Inter', 14))
        self.select_com_dropdown_menu.place(x=152, y=147)
        self.select_com_dropdown_menu.bind("<Configure>", self.on_baudrate_select)

        # First Blue Line
        self.canvas.create_rectangle(0, 230.0, 480.0, 230.0, fill="#0000FF", outline="")

        # Relays Section
        self.canvas.create_text(196.0, 241.0, anchor="nw", text="Relays", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        self.button_img_relay_1 = PhotoImage(file=self.get_panel_path("relay_1_off.png"))
        self.button_relay_1 = Button(image=self.button_img_relay_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_1 clicked"), relief="flat")
        self.button_relay_1.place(x=165.0, y=306.0, width=30.0, height=30.0)

        self.button_img_relay_2 = PhotoImage(file=self.get_panel_path("relay_2_off.png"))
        self.button_relay_2 = Button(image=self.button_img_relay_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_2 clicked"), relief="flat")
        self.button_relay_2.place(x=205.0, y=306.0, width=30.0, height=30.0)

        self.button_img_relay_3 = PhotoImage(file=self.get_panel_path("relay_3_off.png"))
        self.button_relay_3 = Button(image=self.button_img_relay_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_3 clicked"), relief="flat")
        self.button_relay_3.place(x=245.0, y=306.0, width=30.0, height=30.0)

        self.button_img_relay_4 = PhotoImage(file=self.get_panel_path("relay_4_off.png"))
        self.button_relay_4 = Button(image=self.button_img_relay_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_4 clicked"), relief="flat")
        self.button_relay_4.place(x=285.0, y=306.0, width=30.0, height=30.0)

        self.button_img_relay_5 = PhotoImage(file=self.get_panel_path("relay_5_off.png"))
        self.button_relay_5 = Button(image=self.button_img_relay_5, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_5 clicked"), relief="flat")
        self.button_relay_5.place(x=165.0, y=346.0, width=30.0, height=30.0)

        self.button_img_relay_6 = PhotoImage(file=self.get_panel_path("relay_6_off.png"))
        self.button_relay_6 = Button(image=self.button_img_relay_6, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_6 clicked"), relief="flat")
        self.button_relay_6.place(x=205.0, y=346.0, width=30.0, height=30.0)

        self.button_img_relay_7 = PhotoImage(file=self.get_panel_path("relay_7_off.png"))
        self.button_relay_7 = Button(image=self.button_img_relay_7, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_7 clicked"), relief="flat")
        self.button_relay_7.place(x=245.0, y=346.0, width=30.0, height=30.0)

        self.button_img_relay_8 = PhotoImage(file=self.get_panel_path("relay_8_off.png"))
        self.button_relay_8 = Button(image=self.button_img_relay_8, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_8 clicked"), relief="flat")
        self.button_relay_8.place(x=285.0, y=346.0, width=30.0, height=30.0)

        self.button_img_relay_9 = PhotoImage(file=self.get_panel_path("relay_9_off.png"))
        self.button_relay_9 = Button(image=self.button_img_relay_9, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_9 clicked"), relief="flat")
        self.button_relay_9.place(x=165.0, y=386.0, width=30.0, height=30.0)

        self.button_img_relay_10 = PhotoImage(file=self.get_panel_path("relay_10_off.png"))
        self.button_relay_10 = Button(image=self.button_img_relay_10, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_10 clicked"), relief="flat")
        self.button_relay_10.place(x=205.0, y=386.0, width=30.0, height=30.0)

        self.button_img_relay_11 = PhotoImage(file=self.get_panel_path("relay_11_off.png"))
        self.button_relay_11 = Button(image=self.button_img_relay_11, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_11 clicked"), relief="flat")
        self.button_relay_11.place(x=245.0, y=386.0, width=30.0, height=30.0)

        self.button_img_relay_12 = PhotoImage(file=self.get_panel_path("relay_12_off.png"))
        self.button_relay_12 = Button(image=self.button_img_relay_12, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_12 clicked"), relief="flat")
        self.button_relay_12.place(x=285.0, y=386.0, width=30.0, height=30.0)

        self.button_img_relay_13 = PhotoImage(file=self.get_panel_path("relay_13_off.png"))
        self.button_relay_13 = Button(image=self.button_img_relay_13, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_13 clicked"), relief="flat")
        self.button_relay_13.place(x=165.0, y=426.0, width=30.0, height=30.0)

        self.button_img_relay_14 = PhotoImage(file=self.get_panel_path("relay_14_off.png"))
        self.button_relay_14 = Button(image=self.button_img_relay_14, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_14 clicked"), relief="flat")
        self.button_relay_14.place(x=205.0, y=426.0, width=30.0, height=30.0)

        self.button_img_relay_15 = PhotoImage(file=self.get_panel_path("relay_15_off.png"))
        self.button_relay_15 = Button(image=self.button_img_relay_15, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_15 clicked"), relief="flat")
        self.button_relay_15.place(x=245.0, y=426.0, width=30.0, height=30.0)

        self.button_img_relay_16 = PhotoImage(file=self.get_panel_path("relay_16_off.png"))
        self.button_relay_16 = Button(image=self.button_img_relay_16, borderwidth=0, highlightthickness=0, command=lambda: print("button_relay_16 clicked"), relief="flat")
        self.button_relay_16.place(x=285.0, y=426.0, width=30.0, height=30.0)

        self.canvas.create_text(190.0, 494.0, anchor="nw", text="Select All", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.relays_var = BooleanVar()
        self.button_check_relays = Checkbutton(self.canvas, bg='#000000', variable=self.relays_var, onvalue=True, offvalue=False, command=lambda: print("relay check box clicked"))
        self.button_check_relays.place(x=272, y=493)

        # Second Blue Line
        self.canvas.create_rectangle(0, 550.0, 480.0, 550.0, fill="#0000FF", outline="")

        # GPIOs Section
        self.canvas.create_text(197.0, 558.0, anchor="nw", text="GPIOs", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        self.button_img_gpio_0 = PhotoImage(file=self.get_panel_path("gpio_0_off.png"))
        self.button_gpio_0 = Button(image=self.button_img_gpio_0, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_0 clicked"), relief="flat")
        self.button_gpio_0.place(x=147.0, y=698.0, width=36.0, height=36.0)

        self.button_img_gpio_1 = PhotoImage(file=self.get_panel_path("gpio_1_off.png"))
        self.button_gpio_1 = Button(image=self.button_img_gpio_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_1 clicked"), relief="flat")
        self.button_gpio_1.place(x=170.0, y=648.0, width=36.0, height=36.0)

        self.button_img_gpio_2 = PhotoImage(file=self.get_panel_path("gpio_2_off.png"))
        self.button_gpio_2 = Button(image=self.button_img_gpio_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_2 clicked"),relief="flat")
        self.button_gpio_2.place(x=222.0, y=623.0, width=36.0, height=36.0)

        self.button_img_gpio_3 = PhotoImage(file=self.get_panel_path("gpio_3_off.png"))
        self.button_gpio_3 = Button(image=self.button_img_gpio_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_3 clicked"), relief="flat")
        self.button_gpio_3.place(x=271.0, y=648.0, width=36.0, height=36.0)

        self.button_img_gpio_4 = PhotoImage(file=self.get_panel_path("gpio_4_off.png"))
        self.button_gpio_4 = Button(image=self.button_img_gpio_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_4 clicked"), relief="flat")
        self.button_gpio_4.place(x=296.0, y=698.0, width=36.0, height=36.0)

        self.button_img_gpio_5 = PhotoImage(file=self.get_panel_path("gpio_5_off.png"))
        self.button_gpio_5 = Button(image=self.button_img_gpio_5, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_5 clicked"), relief="flat")
        self.button_gpio_5.place(x=271.0, y=747.0, width=36.0, height=36.0)

        self.button_img_gpio_6 = PhotoImage(file=self.get_panel_path("gpio_6_off.png"))
        self.button_gpio_6 = Button(image=self.button_img_gpio_6, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_6 clicked"), relief="flat")
        self.button_gpio_6.place(x=222.0, y=773.0, width=36.0, height=36.0)

        self.button_img_gpio_7 = PhotoImage(file=self.get_panel_path("gpio_7_off.png"))
        self.button_gpio_7 = Button(image=self.button_img_gpio_7, borderwidth=0, highlightthickness=0, command=lambda: print("button_gpio_7 clicked"), relief="flat")
        self.button_gpio_7.place(x=170.0, y=747.0, width=36.0, height=36.0)

        self.canvas.create_text(190.0, 846.0, anchor="nw", text="Select All", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.gpios_var = BooleanVar()
        self.button_check_relays = Checkbutton(self.canvas, bg='#000000', variable=self.gpios_var, onvalue=True, offvalue=False, command=lambda: print("gpio check box clicked"))
        self.button_check_relays.place(x=272, y=845)

        # Third Blue Line
        self.canvas.create_rectangle(0, 902.0, 480.0, 902.0, fill="#0000FF", outline="")

        # Iterations Section
        self.canvas.create_text(182.0, 912.0, anchor="nw", text="Iterations", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        self.canvas.create_text(171.0, 965.0, anchor="nw", text="Number: ", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry.place(x=256.0, y=965.0, width=50.0, height=20.0)
        
    def get_panel_path(self, path: str) -> Path:
        return PANEL_PATH / Path(path)

    def get_test_path(self, path: str) -> Path:
        return TEST_PATH / Path(path)

    def on_com_select(self, event):
        selected_value = self.com_var.get()
        print(f"Selected COM: {selected_value}")
        
    def on_baudrate_select(self, event):
        selected_value = self.baudrate_var.get()
        print(f"Selected Baudrate: {selected_value}")
    
    def run(self):
        self.mainwindow.mainloop() 
        
class AutomaticTestSection:
    def __init__(self, cover_window):        
        self.mainwindow = cover_window

        # Horizontal Shift
        self.shift = 480.0
        
        self.canvas = Canvas(self.mainwindow, bg = "#0000FF", height = 1017, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x=0 + self.shift, y=0)

        # Terminal
        self.terminal_img = PhotoImage(file=self.get_test_path("output_text.png"))
        self.terminal_bg = self.canvas.create_image(721.0, 264.0, image=self.terminal_img)
        self.terminal = Entry(bd=0, bg="#000000", fg="#000716", highlightthickness=0)
        self.terminal.place(x=293.0 + self.shift, y=76.0, width=856.0, height=426.0)
               
        # Gauge        
        self.gauge_img = PhotoImage(file=self.get_test_path("gauge.png"))
        self.gauge = self.canvas.create_image(720.0, 724.0, image=self.gauge_img)
        self.canvas.create_text(667.0, 695.0, anchor="nw", text="75%", fill="#FFFFFF", font=("Inter Black", 47 * -1))
        
        # Buttons Section
        self.run_img = PhotoImage(file=self.get_test_path("run.png"))
        self.run_button = Button(image=self.run_img, borderwidth=0, highlightthickness=0, command=lambda: print("run button clicked"), relief="flat")
        self.run_button.place(x=450.0 + self.shift, y=944.0, width=161.0, height=50.0)

        self.quit_img = PhotoImage(file=self.get_test_path("quit.png"))
        self.quit_button = Button(image=self.quit_img, borderwidth=0, highlightthickness=0, command=lambda: print("quit button clicked"), relief="flat")
        self.quit_button.place(x=641.0 + self.shift, y=944.0, width=161.0, height=50.0)

        self.back_img = PhotoImage(file=self.get_test_path("back.png"))
        self.back_button = Button(image=self.back_img, borderwidth=0, highlightthickness=0, command=lambda: print("back button clicked"), relief="flat")
        self.back_button.place(x=832.0 + self.shift, y=944.0, width=161.0, height=50.0)

    def get_test_path(self, path: str) -> Path:
        return TEST_PATH / Path(path)

    def run(self):
        self.mainwindow.mainloop()
    
def on_btn_click(cover_window):
    ut.clear_current_window(cover_window)
    panel = AutomaticTestPanel(cover_window)
    test = AutomaticTestSection(cover_window)
    panel.run()    
    test.run()
