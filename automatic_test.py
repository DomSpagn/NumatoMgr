# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, OptionMenu, Button, PhotoImage, Checkbutton, messagebox, BooleanVar, StringVar

import serial
import common as cmn


class AutomaticTestPanel:
    # GUI
    def __init__(self, cover_window):
        self.mainwindow = cover_window
        self.type = 'auto'
        
        self.canvas = Canvas(self.mainwindow, bg="#000000", height=1017, width=480, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Serial COM Settings Section
        self.canvas.create_text(108.0, 11.0, anchor="nw", text="Serial COM Settings", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        # Select COM Dropdown Menu
        self.com_var = StringVar(self.canvas)
        self.com_var.set("Select COM")        
        self.list_of_active_COMs = cmn.list_serial_ports()
        self.select_com_dropdown_menu = OptionMenu(self.canvas, self.com_var, *self.list_of_active_COMs)
        self.select_com_dropdown_menu.config(width=12, height=1, anchor='center', font=('Inter', 14))
        self.com_menu = self.select_com_dropdown_menu.nametowidget(self.select_com_dropdown_menu.menuname)
        self.com_menu.configure(font=('Inter', 14))
        self.select_com_dropdown_menu.place(x=152, y=77)        

        # Select Baudrate Dropdown Menu
        self.baudrate_var = StringVar(self.canvas)
        self.baudrate_var.set("Select Baudrate")        
        self.baudrate_list = cmn.get_baudrate_list()
        self.select_com_dropdown_menu = OptionMenu(self.canvas, self.baudrate_var, *self.baudrate_list)
        self.select_com_dropdown_menu.config(width=12, height=1, anchor='center', font=('Inter', 14))  # Impostazione larghezza e altezza del bottone
        self.com_menu = self.select_com_dropdown_menu.nametowidget(self.select_com_dropdown_menu.menuname)
        self.com_menu.configure(font=('Inter', 14))
        self.select_com_dropdown_menu.place(x=152, y=147)        

        # First Blue Line
        self.canvas.create_rectangle(0, 230.0, 480.0, 230.0, fill="#0000FF", outline="")

        # Relays Section
        self.is_relay_selected = [False] * 16
        self.canvas.create_text(196.0, 241.0, anchor="nw", text="Relays", fill="#FFFFFF", font=("Inter Black", 28 * -1))
        
        self.current_relay_img_idx = [0] * 16
        self.set_relay_1_button()
        self.set_relay_2_button()
        self.set_relay_3_button()
        self.set_relay_4_button()
        self.set_relay_5_button()
        self.set_relay_6_button()
        self.set_relay_7_button()
        self.set_relay_8_button()
        self.set_relay_9_button()
        self.set_relay_10_button()
        self.set_relay_11_button()
        self.set_relay_12_button()
        self.set_relay_13_button()
        self.set_relay_14_button()
        self.set_relay_15_button()
        self.set_relay_16_button()

        self.canvas.create_text(190.0, 494.0, anchor="nw", text="Select All", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.relays_var = BooleanVar()
        self.button_check_relays = Checkbutton(self.canvas, bg='#000000', variable=self.relays_var, onvalue=True, offvalue=False, command=self.manage_all_relays)
        self.button_check_relays.place(x=272, y=493)

        # Second Blue Line
        self.canvas.create_rectangle(0, 550.0, 480.0, 550.0, fill="#0000FF", outline="")

        # GPIOs Section
        self.is_gpio_selected = [False] * 8
        self.canvas.create_text(197.0, 558.0, anchor="nw", text="GPIOs", fill="#FFFFFF", font=("Inter Black", 28 * -1))
        
        self.current_gpio_img_idx = [0] * 8
        self.set_gpio_0_button()
        self.set_gpio_1_button()
        self.set_gpio_2_button()
        self.set_gpio_3_button()
        self.set_gpio_4_button()
        self.set_gpio_5_button()
        self.set_gpio_6_button()
        self.set_gpio_7_button()

        self.canvas.create_text(238.0, 681.0, anchor="n", text="+/-", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.negative_logic_var = BooleanVar()
        self.button_check_relays = Checkbutton(self.canvas, bg='#000000', variable=self.negative_logic_var, onvalue=True, offvalue=False, command=self.set_negative_logic)
        self.button_check_relays.place(x=228, y=702)

        self.canvas.create_text(190.0, 846.0, anchor="nw", text="Select All", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.gpios_var = BooleanVar()
        self.button_check_relays = Checkbutton(self.canvas, bg='#000000', variable=self.gpios_var, onvalue=True, offvalue=False, command=self.manage_all_gpios)
        self.button_check_relays.place(x=272, y=845)

        # Third Blue Line
        self.canvas.create_rectangle(0, 902.0, 480.0, 902.0, fill="#0000FF", outline="")

        # Iterations Section
        self.canvas.create_text(180.0, 912.0, anchor="nw", text="Iterations", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        self.canvas.create_text(190.0, 965.0, anchor="nw", text="#: ", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry.place(x=214.0, y=965.0, width=50.0, height=20.0)
        
    # Manage relays
    def toggle_relay_1_img(self):
        self.current_relay_img_idx[0] = 1 - self.current_relay_img_idx[0]
        self.is_relay_selected[0] = True if self.current_relay_img_idx[0] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_1[self.current_relay_img_idx[0]])
        self.button_relay_1.config(image=new_image)
        self.button_relay_1.image = new_image  # To prevent garbage collection

    def set_relay_1_button(self):
        self.img_paths_relay_1 = [cmn.get_panel_path(self.type, "relay_1_off.png"), cmn.get_panel_path(self.type, "relay_1_on.png")]        
        self.photo_var_relay_1 = PhotoImage(file=self.img_paths_relay_1[self.current_relay_img_idx[0]])
        self.button_relay_1 = Button(image=self.photo_var_relay_1, borderwidth=0, highlightthickness=0, command=self.toggle_relay_1_img, relief="flat")
        self.button_relay_1.place(x=165.0, y=306.0, width=30.0, height=30.0)

    def toggle_relay_2_img(self):
        self.current_relay_img_idx[1] = 1 - self.current_relay_img_idx[1]
        self.is_relay_selected[1] = True if self.current_relay_img_idx[1] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_2[self.current_relay_img_idx[1]])
        self.button_relay_2.config(image=new_image)
        self.button_relay_2.image = new_image  # To prevent garbage collection

    def set_relay_2_button(self):
        self.img_paths_relay_2 = [cmn.get_panel_path(self.type, "relay_2_off.png"), cmn.get_panel_path(self.type, "relay_2_on.png")]        
        self.photo_var_relay_2 = PhotoImage(file=self.img_paths_relay_2[self.current_relay_img_idx[1]])
        self.button_relay_2 = Button(image=self.photo_var_relay_2, borderwidth=0, highlightthickness=0, command=self.toggle_relay_2_img, relief="flat")
        self.button_relay_2.place(x=205.0, y=306.0, width=30.0, height=30.0)

    def toggle_relay_3_img(self):
        self.current_relay_img_idx[2] = 1 - self.current_relay_img_idx[2]
        self.is_relay_selected[2] = True if self.current_relay_img_idx[2] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_3[self.current_relay_img_idx[2]])
        self.button_relay_3.config(image=new_image)
        self.button_relay_3.image = new_image  # To prevent garbage collection

    def set_relay_3_button(self):
        self.img_paths_relay_3 = [cmn.get_panel_path(self.type, "relay_3_off.png"), cmn.get_panel_path(self.type, "relay_3_on.png")]        
        self.photo_var_relay_3 = PhotoImage(file=self.img_paths_relay_3[self.current_relay_img_idx[2]])
        self.button_relay_3 = Button(image=self.photo_var_relay_3, borderwidth=0, highlightthickness=0, command=self.toggle_relay_3_img, relief="flat")
        self.button_relay_3.place(x=245.0, y=306.0, width=30.0, height=30.0)

    def toggle_relay_4_img(self):
        self.current_relay_img_idx[3] = 1 - self.current_relay_img_idx[3]
        self.is_relay_selected[3] = True if self.current_relay_img_idx[3] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_4[self.current_relay_img_idx[3]])
        self.button_relay_4.config(image=new_image)
        self.button_relay_4.image = new_image  # To prevent garbage collection

    def set_relay_4_button(self):
        self.img_paths_relay_4 = [cmn.get_panel_path(self.type, "relay_4_off.png"), cmn.get_panel_path(self.type, "relay_4_on.png")]        
        self.photo_var_relay_4 = PhotoImage(file=self.img_paths_relay_4[self.current_relay_img_idx[3]])
        self.button_relay_4 = Button(image=self.photo_var_relay_4, borderwidth=0, highlightthickness=0, command=self.toggle_relay_4_img, relief="flat")
        self.button_relay_4.place(x=285.0, y=306.0, width=30.0, height=30.0)

    def toggle_relay_5_img(self):
        self.current_relay_img_idx[4] = 1 - self.current_relay_img_idx[4]
        self.is_relay_selected[4] = True if self.current_relay_img_idx[4] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_5[self.current_relay_img_idx[4]])
        self.button_relay_5.config(image=new_image)
        self.button_relay_5.image = new_image  # To prevent garbage collection

    def set_relay_5_button(self):
        self.img_paths_relay_5 = [cmn.get_panel_path(self.type, "relay_5_off.png"), cmn.get_panel_path(self.type, "relay_5_on.png")]        
        self.photo_var_relay_5 = PhotoImage(file=self.img_paths_relay_5[self.current_relay_img_idx[4]])
        self.button_relay_5 = Button(image=self.photo_var_relay_5, borderwidth=0, highlightthickness=0, command=self.toggle_relay_5_img, relief="flat")
        self.button_relay_5.place(x=165.0, y=346.0, width=30.0, height=30.0)

    def toggle_relay_6_img(self):
        self.current_relay_img_idx[5] = 1 - self.current_relay_img_idx[5]
        self.is_relay_selected[5] = True if self.current_relay_img_idx[5] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_6[self.current_relay_img_idx[5]])
        self.button_relay_6.config(image=new_image)
        self.button_relay_6.image = new_image  # To prevent garbage collection

    def set_relay_6_button(self):
        self.img_paths_relay_6 = [cmn.get_panel_path(self.type, "relay_6_off.png"), cmn.get_panel_path(self.type, "relay_6_on.png")]        
        self.photo_var_relay_6 = PhotoImage(file=self.img_paths_relay_6[self.current_relay_img_idx[5]])
        self.button_relay_6 = Button(image=self.photo_var_relay_6, borderwidth=0, highlightthickness=0, command=self.toggle_relay_6_img, relief="flat")
        self.button_relay_6.place(x=205.0, y=346.0, width=30.0, height=30.0)

    def toggle_relay_7_img(self):
        self.current_relay_img_idx[6] = 1 - self.current_relay_img_idx[6]
        self.is_relay_selected[6] = True if self.current_relay_img_idx[6] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_7[self.current_relay_img_idx[6]])
        self.button_relay_7.config(image=new_image)
        self.button_relay_7.image = new_image  # To prevent garbage collection

    def set_relay_7_button(self):
        self.img_paths_relay_7 = [cmn.get_panel_path(self.type, "relay_7_off.png"), cmn.get_panel_path(self.type, "relay_7_on.png")]        
        self.photo_var_relay_7 = PhotoImage(file=self.img_paths_relay_7[self.current_relay_img_idx[6]])
        self.button_relay_7 = Button(image=self.photo_var_relay_7, borderwidth=0, highlightthickness=0, command=self.toggle_relay_7_img, relief="flat")
        self.button_relay_7.place(x=245.0, y=346.0, width=30.0, height=30.0)

    def toggle_relay_8_img(self):
        self.current_relay_img_idx[7] = 1 - self.current_relay_img_idx[7]
        self.is_relay_selected[7] = True if self.current_relay_img_idx[7] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_8[self.current_relay_img_idx[7]])
        self.button_relay_8.config(image=new_image)
        self.button_relay_8.image = new_image  # To prevent garbage collection

    def set_relay_8_button(self):
        self.img_paths_relay_8 = [cmn.get_panel_path(self.type, "relay_8_off.png"), cmn.get_panel_path(self.type, "relay_8_on.png")]        
        self.photo_var_relay_8 = PhotoImage(file=self.img_paths_relay_8[self.current_relay_img_idx[7]])
        self.button_relay_8 = Button(image=self.photo_var_relay_8, borderwidth=0, highlightthickness=0, command=self.toggle_relay_8_img, relief="flat")
        self.button_relay_8.place(x=285.0, y=346.0, width=30.0, height=30.0)

    def toggle_relay_9_img(self):
        self.current_relay_img_idx[8] = 1 - self.current_relay_img_idx[8]
        self.is_relay_selected[8] = True if self.current_relay_img_idx[8] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_9[self.current_relay_img_idx[8]])
        self.button_relay_9.config(image=new_image)
        self.button_relay_9.image = new_image  # To prevent garbage collection

    def set_relay_9_button(self):
        self.img_paths_relay_9 = [cmn.get_panel_path(self.type, "relay_9_off.png"), cmn.get_panel_path(self.type, "relay_9_on.png")]        
        self.photo_var_relay_9 = PhotoImage(file=self.img_paths_relay_9[self.current_relay_img_idx[8]])
        self.button_relay_9 = Button(image=self.photo_var_relay_9, borderwidth=0, highlightthickness=0, command=self.toggle_relay_9_img, relief="flat")
        self.button_relay_9.place(x=165.0, y=386.0, width=30.0, height=30.0)

    def toggle_relay_10_img(self):
        self.current_relay_img_idx[9] = 1 - self.current_relay_img_idx[9]
        self.is_relay_selected[9] = True if self.current_relay_img_idx[9] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_10[self.current_relay_img_idx[9]])
        self.button_relay_10.config(image=new_image)
        self.button_relay_10.image = new_image  # To prevent garbage collection

    def set_relay_10_button(self):
        self.img_paths_relay_10 = [cmn.get_panel_path(self.type, "relay_10_off.png"), cmn.get_panel_path(self.type, "relay_10_on.png")]        
        self.photo_var_relay_10 = PhotoImage(file=self.img_paths_relay_10[self.current_relay_img_idx[9]])
        self.button_relay_10 = Button(image=self.photo_var_relay_10, borderwidth=0, highlightthickness=0, command=self.toggle_relay_10_img, relief="flat")
        self.button_relay_10.place(x=205.0, y=386.0, width=30.0, height=30.0)

    def toggle_relay_11_img(self):
        self.current_relay_img_idx[10] = 1 - self.current_relay_img_idx[10]
        self.is_relay_selected[10] = True if self.current_relay_img_idx[10] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_11[self.current_relay_img_idx[10]])
        self.button_relay_11.config(image=new_image)
        self.button_relay_11.image = new_image  # To prevent garbage collection

    def set_relay_11_button(self):
        self.img_paths_relay_11 = [cmn.get_panel_path(self.type, "relay_11_off.png"), cmn.get_panel_path(self.type, "relay_11_on.png")]        
        self.photo_var_relay_11 = PhotoImage(file=self.img_paths_relay_11[self.current_relay_img_idx[10]])
        self.button_relay_11 = Button(image=self.photo_var_relay_11, borderwidth=0, highlightthickness=0, command=self.toggle_relay_11_img, relief="flat")
        self.button_relay_11.place(x=245.0, y=386.0, width=30.0, height=30.0)

    def toggle_relay_12_img(self):
        self.current_relay_img_idx[11] = 1 - self.current_relay_img_idx[11]
        self.is_relay_selected[11] = True if self.current_relay_img_idx[11] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_12[self.current_relay_img_idx[11]])
        self.button_relay_12.config(image=new_image)
        self.button_relay_12.image = new_image  # To prevent garbage collection

    def set_relay_12_button(self):
        self.img_paths_relay_12 = [cmn.get_panel_path(self.type, "relay_12_off.png"), cmn.get_panel_path(self.type, "relay_12_on.png")]        
        self.photo_var_relay_12 = PhotoImage(file=self.img_paths_relay_12[self.current_relay_img_idx[11]])
        self.button_relay_12 = Button(image=self.photo_var_relay_12, borderwidth=0, highlightthickness=0, command=self.toggle_relay_12_img, relief="flat")
        self.button_relay_12.place(x=285.0, y=386.0, width=30.0, height=30.0)

    def toggle_relay_13_img(self):
        self.current_relay_img_idx[12] = 1 - self.current_relay_img_idx[12]
        self.is_relay_selected[12] = True if self.current_relay_img_idx[12] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_13[self.current_relay_img_idx[12]])
        self.button_relay_13.config(image=new_image)
        self.button_relay_13.image = new_image  # To prevent garbage collection

    def set_relay_13_button(self):
        self.img_paths_relay_13 = [cmn.get_panel_path(self.type, "relay_13_off.png"), cmn.get_panel_path(self.type, "relay_13_on.png")]        
        self.photo_var_relay_13 = PhotoImage(file=self.img_paths_relay_13[self.current_relay_img_idx[12]])
        self.button_relay_13 = Button(image=self.photo_var_relay_13, borderwidth=0, highlightthickness=0, command=self.toggle_relay_13_img, relief="flat")
        self.button_relay_13.place(x=165.0, y=426.0, width=30.0, height=30.0)

    def toggle_relay_14_img(self):
        self.current_relay_img_idx[13] = 1 - self.current_relay_img_idx[13]
        self.is_relay_selected[13] = True if self.current_relay_img_idx[13] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_14[self.current_relay_img_idx[13]])
        self.button_relay_14.config(image=new_image)
        self.button_relay_14.image = new_image  # To prevent garbage collection

    def set_relay_14_button(self):
        self.img_paths_relay_14 = [cmn.get_panel_path(self.type, "relay_14_off.png"), cmn.get_panel_path(self.type, "relay_14_on.png")]        
        self.photo_var_relay_14 = PhotoImage(file=self.img_paths_relay_14[self.current_relay_img_idx[13]])
        self.button_relay_14 = Button(image=self.photo_var_relay_14, borderwidth=0, highlightthickness=0, command=self.toggle_relay_14_img, relief="flat")
        self.button_relay_14.place(x=205.0, y=426.0, width=30.0, height=30.0)

    def toggle_relay_15_img(self):
        self.current_relay_img_idx[14] = 1 - self.current_relay_img_idx[14]
        self.is_relay_selected[14] = True if self.current_relay_img_idx[14] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_15[self.current_relay_img_idx[14]])
        self.button_relay_15.config(image=new_image)
        self.button_relay_15.image = new_image  # To prevent garbage collection

    def set_relay_15_button(self):
        self.img_paths_relay_15 = [cmn.get_panel_path(self.type, "relay_15_off.png"), cmn.get_panel_path(self.type, "relay_15_on.png")]        
        self.photo_var_relay_15 = PhotoImage(file=self.img_paths_relay_15[self.current_relay_img_idx[14]])
        self.button_relay_15 = Button(image=self.photo_var_relay_15, borderwidth=0, highlightthickness=0, command=self.toggle_relay_15_img, relief="flat")
        self.button_relay_15.place(x=245.0, y=426.0, width=30.0, height=30.0)

    def toggle_relay_16_img(self):
        self.current_relay_img_idx[15] = 1 - self.current_relay_img_idx[15]
        self.is_relay_selected[15] = True if self.current_relay_img_idx[15] == 1 else False
        new_image = PhotoImage(file=self.img_paths_relay_16[self.current_relay_img_idx[15]])
        self.button_relay_16.config(image=new_image)
        self.button_relay_16.image = new_image  # To prevent garbage collection

    def set_relay_16_button(self):
        self.img_paths_relay_16 = [cmn.get_panel_path(self.type, "relay_16_off.png"), cmn.get_panel_path(self.type, "relay_16_on.png")]        
        self.photo_var_relay_16 = PhotoImage(file=self.img_paths_relay_16[self.current_relay_img_idx[15]])
        self.button_relay_16 = Button(image=self.photo_var_relay_16, borderwidth=0, highlightthickness=0, command=self.toggle_relay_16_img, relief="flat")
        self.button_relay_16.place(x=285.0, y=426.0, width=30.0, height=30.0)

    def manage_all_relays(self):        
        if not self.relays_var.get():
            self.is_relay_selected = [False] * 16
            self.current_relay_img_idx = [0] * 16
        else:
            self.is_relay_selected = [True] * 16
            self.current_relay_img_idx = [1] * 16
            
        self.set_relay_1_button()
        self.set_relay_2_button()
        self.set_relay_3_button()
        self.set_relay_4_button()
        self.set_relay_5_button()
        self.set_relay_6_button()
        self.set_relay_7_button()
        self.set_relay_8_button()
        self.set_relay_9_button()
        self.set_relay_10_button()
        self.set_relay_11_button()
        self.set_relay_12_button()
        self.set_relay_13_button()
        self.set_relay_14_button()
        self.set_relay_15_button()
        self.set_relay_16_button()

    # Manage GPIOs
    def toggle_gpio_0_img(self):
        self.current_gpio_img_idx[0] = 1 - self.current_gpio_img_idx[0]
        self.is_gpio_selected[0] = True if self.current_gpio_img_idx[0] == 1 else False
        new_image = PhotoImage(file=self.img_paths_gpio_0[self.current_gpio_img_idx[0]])
        self.button_gpio_0.config(image=new_image)
        self.button_gpio_0.image = new_image  # To prevent garbage collection

    def set_gpio_0_button(self):
        self.img_paths_gpio_0 = [cmn.get_panel_path(self.type, "gpio_0_off.png"), cmn.get_panel_path(self.type, "gpio_0_on.png")]        
        self.photo_var_gpio_0 = PhotoImage(file=self.img_paths_gpio_0[self.current_gpio_img_idx[0]])
        self.button_gpio_0 = Button(image=self.photo_var_gpio_0, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_0_img, relief="flat")
        self.button_gpio_0.place(x=147.0, y=698.0, width=36.0, height=36.0)

    def toggle_gpio_1_img(self):
        self.current_gpio_img_idx[1] = 1 - self.current_gpio_img_idx[1]
        self.is_gpio_selected[1] = True if self.current_gpio_img_idx[1] == 1 else False
        new_image = PhotoImage(file=self.img_paths_gpio_1[self.current_gpio_img_idx[1]])
        self.button_gpio_1.config(image=new_image)
        self.button_gpio_1.image = new_image  # To prevent garbage collection

    def set_gpio_1_button(self):
        self.img_paths_gpio_1 = [cmn.get_panel_path(self.type, "gpio_1_off.png"), cmn.get_panel_path(self.type, "gpio_1_on.png")]        
        self.photo_var_gpio_1 = PhotoImage(file=self.img_paths_gpio_1[self.current_gpio_img_idx[1]])
        self.button_gpio_1 = Button(image=self.photo_var_gpio_1, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_1_img, relief="flat")
        self.button_gpio_1.place(x=170.0, y=648.0, width=36.0, height=36.0)

    def toggle_gpio_2_img(self):
        self.current_gpio_img_idx[2] = 1 - self.current_gpio_img_idx[2]
        self.is_gpio_selected[2] = True if self.current_gpio_img_idx[2] == 1 else False
        new_image = PhotoImage(file=self.img_paths_gpio_2[self.current_gpio_img_idx[2]])
        self.button_gpio_2.config(image=new_image)
        self.button_gpio_2.image = new_image  # To prevent garbage collection

    def set_gpio_2_button(self):
        self.img_paths_gpio_2 = [cmn.get_panel_path(self.type, "gpio_2_off.png"), cmn.get_panel_path(self.type, "gpio_2_on.png")]        
        self.photo_var_gpio_2 = PhotoImage(file=self.img_paths_gpio_2[self.current_gpio_img_idx[2]])
        self.button_gpio_2 = Button(image=self.photo_var_gpio_2, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_2_img, relief="flat")
        self.button_gpio_2.place(x=222.0, y=623.0, width=36.0, height=36.0)

    def toggle_gpio_3_img(self):
        self.current_gpio_img_idx[3] = 1 - self.current_gpio_img_idx[3]
        self.is_gpio_selected[3] = True if self.current_gpio_img_idx[3] == 1 else False
        new_image = PhotoImage(file=self.img_paths_gpio_3[self.current_gpio_img_idx[3]])
        self.button_gpio_3.config(image=new_image)
        self.button_gpio_3.image = new_image  # To prevent garbage collection

    def set_gpio_3_button(self):
        self.img_paths_gpio_3 = [cmn.get_panel_path(self.type, "gpio_3_off.png"), cmn.get_panel_path(self.type, "gpio_3_on.png")]        
        self.photo_var_gpio_3 = PhotoImage(file=self.img_paths_gpio_3[self.current_gpio_img_idx[3]])
        self.button_gpio_3 = Button(image=self.photo_var_gpio_3, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_3_img, relief="flat")
        self.button_gpio_3.place(x=271.0, y=648.0, width=36.0, height=36.0)

    def toggle_gpio_4_img(self):
        self.current_gpio_img_idx[4] = 1 - self.current_gpio_img_idx[4]
        self.is_gpio_selected[4] = True if self.current_gpio_img_idx[4] == 1 else False
        new_image = PhotoImage(file=self.img_paths_gpio_4[self.current_gpio_img_idx[4]])
        self.button_gpio_4.config(image=new_image)
        self.button_gpio_4.image = new_image  # To prevent garbage collection

    def set_gpio_4_button(self):
        self.img_paths_gpio_4 = [cmn.get_panel_path(self.type, "gpio_4_off.png"), cmn.get_panel_path(self.type, "gpio_4_on.png")]        
        self.photo_var_gpio_4 = PhotoImage(file=self.img_paths_gpio_4[self.current_gpio_img_idx[4]])
        self.button_gpio_4 = Button(image=self.photo_var_gpio_4, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_4_img, relief="flat")
        self.button_gpio_4.place(x=296.0, y=698.0, width=36.0, height=36.0)

    def toggle_gpio_5_img(self):
        self.current_gpio_img_idx[5] = 1 - self.current_gpio_img_idx[5]
        self.is_gpio_selected[5] = True if self.current_gpio_img_idx[5] == 1 else False
        new_image = PhotoImage(file=self.img_paths_gpio_5[self.current_gpio_img_idx[5]])
        self.button_gpio_5.config(image=new_image)
        self.button_gpio_5.image = new_image  # To prevent garbage collection

    def set_gpio_5_button(self):
        self.img_paths_gpio_5 = [cmn.get_panel_path(self.type, "gpio_5_off.png"), cmn.get_panel_path(self.type, "gpio_5_on.png")]        
        self.photo_var_gpio_5 = PhotoImage(file=self.img_paths_gpio_5[self.current_gpio_img_idx[5]])
        self.button_gpio_5 = Button(image=self.photo_var_gpio_5, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_5_img, relief="flat")
        self.button_gpio_5.place(x=271.0, y=747.0, width=36.0, height=36.0)

    def toggle_gpio_6_img(self):
        self.current_gpio_img_idx[6] = 1 - self.current_gpio_img_idx[6]
        self.is_gpio_selected[6] = True if self.current_gpio_img_idx[6] == 1 else False
        new_image = PhotoImage(file=self.img_paths_gpio_6[self.current_gpio_img_idx[6]])
        self.button_gpio_6.config(image=new_image)
        self.button_gpio_6.image = new_image  # To prevent garbage collection

    def set_gpio_6_button(self):
        self.img_paths_gpio_6 = [cmn.get_panel_path(self.type, "gpio_6_off.png"), cmn.get_panel_path(self.type, "gpio_6_on.png")]        
        self.photo_var_gpio_6 = PhotoImage(file=self.img_paths_gpio_6[self.current_gpio_img_idx[6]])
        self.button_gpio_6 = Button(image=self.photo_var_gpio_6, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_6_img, relief="flat")
        self.button_gpio_6.place(x=222.0, y=773.0, width=36.0, height=36.0)

    def toggle_gpio_7_img(self):
        self.current_gpio_img_idx[7] = 1 - self.current_gpio_img_idx[7]
        self.is_gpio_selected[7] = True if self.current_gpio_img_idx[7] == 1 else False
        new_image = PhotoImage(file=self.img_paths_gpio_7[self.current_gpio_img_idx[7]])
        self.button_gpio_7.config(image=new_image)
        self.button_gpio_7.image = new_image  # To prevent garbage collection

    def set_gpio_7_button(self):
        self.img_paths_gpio_7 = [cmn.get_panel_path(self.type, "gpio_7_off.png"), cmn.get_panel_path(self.type, "gpio_7_on.png")]        
        self.photo_var_gpio_7 = PhotoImage(file=self.img_paths_gpio_7[self.current_gpio_img_idx[7]])
        self.button_gpio_7 = Button(image=self.photo_var_gpio_7, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_7_img, relief="flat")
        self.button_gpio_7.place(x=170.0, y=747.0, width=36.0, height=36.0)

    def set_negative_logic(self):
        pass
    
    def manage_all_gpios(self):        
        if not self.gpios_var.get():
            self.is_gpio_selected = [False] * 8
            self.current_gpio_img_idx = [0] * 8
        else:
            self.is_gpio_selected = [True] * 8
            self.current_gpio_img_idx = [1] * 8
            
        self.set_gpio_0_button()
        self.set_gpio_1_button()
        self.set_gpio_2_button()
        self.set_gpio_3_button()
        self.set_gpio_4_button()
        self.set_gpio_5_button()
        self.set_gpio_6_button()
        self.set_gpio_7_button()
           
    def run(self):
        self.mainwindow.mainloop() 

        
class AutomaticTestSection:
    # GUI
    def __init__(self, cover_window, panel):        
        self.mainwindow = cover_window
        self.panel = panel
        self.type = "auto"
        
        # Horizontal Shift
        self.shift = 480.0
        
        self.canvas = Canvas(self.mainwindow, bg = "#0000FF", height = 1017, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x=0 + self.shift, y=0)

        # Terminal
        self.terminal_img = PhotoImage(file=cmn.get_test_path(self.type, "output_text.png"))
        self.terminal_bg = self.canvas.create_image(721.0, 264.0, image=self.terminal_img)
        self.terminal = Entry(bd=0, bg="#000000", fg="#000716", highlightthickness=0)
        self.terminal.place(x=293.0 + self.shift, y=76.0, width=856.0, height=426.0)
               
        # Gauge        
        self.gauge_img = PhotoImage(file=cmn.get_test_path(self.type, "gauge.png"))
        self.gauge = self.canvas.create_image(720.0, 724.0, image=self.gauge_img)
        self.canvas.create_text(667.0, 695.0, anchor="nw", text="75%", fill="#FFFFFF", font=("Inter Black", 47 * -1))
        
        # Buttons Section
        self.run_img = PhotoImage(file=cmn.get_test_path(self.type, "run.png"))
        self.run_button = Button(image=self.run_img, borderwidth=0, highlightthickness=0, command=self.run_automatic_test, relief="flat")
        self.run_button.place(x=544.0 + self.shift, y=944.0, width=161.0, height=50.0)

        self.quit_img = PhotoImage(file=cmn.get_test_path(self.type, "quit.png"))
        self.quit_button = Button(image=self.quit_img, borderwidth=0, highlightthickness=0, command=lambda: cover_window.destroy(), relief="flat")
        self.quit_button.place(x=735.0 + self.shift, y=944.0, width=161.0, height=50.0)

    # Callbacks
    def get_shrinked_com(self):
        original_str = self.panel.com_var.get()
        return original_str.replace(' ', '')        
    
    def get_shrinked_baudrate(self):        
        original_str = self.panel.baudrate_var.get()
        
        if(original_str == "Select Baudrate"):
            return original_str
        
        baudrate_list = [int(i) for i in original_str.split() if i.isdigit()]
        return str(baudrate_list[0])
    
    def get_timeout(self):
        return 1
       
    def invert_gpios_init_condition(self):
        self.canvas.create_text(365.0, 568.0, anchor="nw", text="0", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_0 = PhotoImage(file=cmn.get_test_path(self.type, "on.png"))
        self.gpio_0 = self.canvas.create_image(372.0, 659.0, image=self.gpio_img_0)

        self.canvas.create_text(597.0, 568.0, anchor="nw", text="1", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_1 = PhotoImage(file=cmn.get_test_path(self.type, "on.png"))
        self.gpio_1 = self.canvas.create_image(604.0, 659.0, image=self.gpio_img_1)

        self.canvas.create_text(828.0, 568.0, anchor="nw", text="2", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_2 = PhotoImage(file=cmn.get_test_path(self.type, "on.png"))
        self.gpio_2 = self.canvas.create_image(836.0, 659.0, image=self.gpio_img_2)

        self.canvas.create_text(1060.0, 568.0, anchor="nw", text="3", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_3 = PhotoImage(file=cmn.get_test_path(self.type, "on.png"))
        self.gpio_3 = self.canvas.create_image(1068.0, 659.0, image=self.gpio_img_3)

        self.canvas.create_text(365.0, 743.0, anchor="nw", text="4", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_4 = PhotoImage(file=cmn.get_test_path(self.type, "on.png"))
        self.gpio_4 = self.canvas.create_image(372.0, 835.0, image=self.gpio_img_4)

        self.canvas.create_text(597.0, 743.0, anchor="nw", text="5", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_5 = PhotoImage(file=cmn.get_test_path(self.type, "on.png"))
        self.gpio_5 = self.canvas.create_image(604.0, 835.0, image=self.gpio_img_5)

        self.canvas.create_text(828.0, 743.0, anchor="nw", text="6", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_6 = PhotoImage(file=cmn.get_test_path(self.type, "on.png"))
        self.gpio_6 = self.canvas.create_image(836.0, 835.0, image=self.gpio_img_6)

        self.canvas.create_text(1060.0, 743.0, anchor="nw", text="7", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_7 = PhotoImage(file=cmn.get_test_path(self.type, "on.png"))
        self.gpio_7 = self.canvas.create_image(1068.0, 835.0, image=self.gpio_img_7)  
    
    def get_iterations_num(self):
        return self.panel.entry.get()
    
    # Test
    def run_automatic_test(self):
        self.com = self.get_shrinked_com()
        self.baudrate = self.get_shrinked_baudrate()
        self.timeout = self.get_timeout()
        self.iterations_num = self.get_iterations_num()
               
        if not any(self.panel.is_relay_selected):
            messagebox.showerror("Error", "No relay has been selected")
            return
        
        if not any(self.panel.is_gpio_selected):
            messagebox.showerror("Error", "No GPIO has been selected")
            return

        print(self.iterations_num)
        if self.iterations_num == '0' or not self.iterations_num.isdigit():
            messagebox.showerror("Error", "Wrong iteration number")
            return           

        try:
            self.serialPort = serial.Serial(self.com, self.baudrate, timeout = self.timeout)
            if not cmn.init_system(self.serialPort):            
                self.serialPort.close()
                return
            
            print("Serial Communication Complete")
            self.serialPort.close()
            
            if self.panel.negative_logic_var.get():
                self.invert_gpios_init_condition()
                           
        except:
            if self.com == "SelectCOM":
                messagebox.showerror("Error", "COM not selected")
            elif self.baudrate == "Select Baudrate":
                messagebox.showerror("Error", "Baudrate not selected")
            else:
                messagebox.showerror("Error", "General Error")        
            
    def run(self):
        self.mainwindow.mainloop()
    
def on_btn_click(cover_window):
    cmn.clear_current_window(cover_window)
    panel = AutomaticTestPanel(cover_window)
    test = AutomaticTestSection(cover_window, panel)
    panel.run()    
    test.run()
