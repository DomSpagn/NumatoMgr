# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, OptionMenu, Text, Button, Checkbutton, PhotoImage, StringVar, BooleanVar

import common as cmn


class ManualTestPanel:
    def __init__(self, cover_window):        
        self.mainwindow = cover_window
        self.type = 'manual'
        
        self.canvas = Canvas(self.mainwindow, bg = "#000000", height = 1017, width = 480, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x=0, y=0)

        # Serial COM Settings Section
        self.canvas.create_text(108.0, 11.0, anchor="nw", text="Serial COM Settings", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        # Select COM Dropdown Menu
        self.com_var = StringVar(self.canvas)
        self.com_var.set("Select COM")
        self.com_var.trace('w', lambda *args: cmn.on_com_select(self.com_var, *args))
        self.list_of_active_COMs = cmn.list_serial_ports()
        self.select_com_dropdown_menu = OptionMenu(self.canvas, self.com_var, *self.list_of_active_COMs)
        self.select_com_dropdown_menu.config(width=12, height=1, anchor='center', font=('Inter', 14))
        self.com_menu = self.select_com_dropdown_menu.nametowidget(self.select_com_dropdown_menu.menuname)
        self.com_menu.configure(font=('Inter', 14))
        self.select_com_dropdown_menu.place(x=152, y=110)
        
        # Select Baudrate Dropdown Menu
        self.baudrate_var = StringVar(self.canvas)
        self.baudrate_var.set("Select Baudrate")
        self.baudrate_var.trace('w', lambda *args: cmn.on_baudrate_select(self.baudrate_var, *args))
        self.baudrate_list = cmn.get_baudrate_list()
        self.select_com_dropdown_menu = OptionMenu(self.canvas, self.baudrate_var, *self.baudrate_list)
        self.select_com_dropdown_menu.config(width=12, height=1, anchor='center', font=('Inter', 14))
        self.com_menu = self.select_com_dropdown_menu.nametowidget(self.select_com_dropdown_menu.menuname)
        self.com_menu.configure(font=('Inter', 14))
        self.select_com_dropdown_menu.place(x=152, y=210)

        # First Red Line
        self.canvas.create_rectangle(0, 339.0, 480.0, 339.0, fill="#FF0000", outline="")

        # Relays Section
        self.canvas.create_text(196.0, 349.0, anchor="nw", text="Relays", fill="#FFFFFF", font=("Inter Black", 28 * -1))
        
        self.current_relay_img_idx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
        
        self.canvas.create_text(190.0, 630.0, anchor="nw", text="Select All", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.relays_var = BooleanVar()        
        self.button_check_relays = Checkbutton(self.canvas, bg='#000000', variable=self.relays_var, onvalue=True, offvalue=False, command=self.manage_all_relays)
        self.button_check_relays.place(x=272, y=629)

        # Second Red Line
        self.canvas.create_rectangle(0, 678.0, 480.0, 678.0, fill="#FF0000", outline="")

        # GPIOs Section
        self.canvas.create_text(197.0, 686.0, anchor="nw", text="GPIOs", fill="#FFFFFF", font=("Inter Black", 28 * -1))
        
        self.current_gpio_img_idx = [0, 0, 0, 0, 0, 0, 0, 0]
        self.set_gpio_0_button()
        self.set_gpio_1_button()
        self.set_gpio_2_button()
        self.set_gpio_3_button()
        self.set_gpio_4_button()
        self.set_gpio_5_button()
        self.set_gpio_6_button()
        self.set_gpio_7_button()
        
        self.canvas.create_text(190.0, 968.0, anchor="nw", text="Select All", fill="#FFFFFF", font=("Inter Medium", 19 * -1))
        self.gpios_var = BooleanVar()
        self.button_check_relays = Checkbutton(self.canvas, bg='#000000', variable=self.gpios_var, onvalue=True, offvalue=False, command=self.manage_all_gpios)
        self.button_check_relays.place(x=272, y=967)
        
    def toggle_relay_1_img(self):
        self.current_relay_img_idx[0] = 1 - self.current_relay_img_idx[0]
        new_image = PhotoImage(file=self.img_paths_relay_1[self.current_relay_img_idx[0]])
        self.button_relay_1.config(image=new_image)
        self.button_relay_1.image = new_image  # To prevent garbage collection

    def set_relay_1_button(self):
        self.img_paths_relay_1 = [cmn.get_panel_path(self.type, "relay_1_off.png"), cmn.get_panel_path(self.type, "relay_1_on.png")]        
        self.photo_var_relay_1 = PhotoImage(file=self.img_paths_relay_1[self.current_relay_img_idx[0]])
        self.button_relay_1 = Button(image=self.photo_var_relay_1, borderwidth=0, highlightthickness=0, command=self.toggle_relay_1_img, relief="flat")
        self.button_relay_1.place(x=165.0, y=425.0, width=30.0, height=30.0)        

    def toggle_relay_2_img(self):
        self.current_relay_img_idx[1] = 1 - self.current_relay_img_idx[1]
        new_image = PhotoImage(file=self.img_paths_relay_2[self.current_relay_img_idx[1]])
        self.button_relay_2.config(image=new_image)
        self.button_relay_2.image = new_image  # To prevent garbage collection

    def set_relay_2_button(self):
        self.img_paths_relay_2 = [cmn.get_panel_path(self.type, "relay_2_off.png"), cmn.get_panel_path(self.type, "relay_2_on.png")]        
        self.photo_var_relay_2 = PhotoImage(file=self.img_paths_relay_2[self.current_relay_img_idx[1]])
        self.button_relay_2 = Button(image=self.photo_var_relay_2, borderwidth=0, highlightthickness=0, command=self.toggle_relay_2_img, relief="flat")
        self.button_relay_2.place(x=205.0, y=425.0, width=30.0, height=30.0)

    def toggle_relay_3_img(self):
        self.current_relay_img_idx[2] = 1 - self.current_relay_img_idx[2]
        new_image = PhotoImage(file=self.img_paths_relay_3[self.current_relay_img_idx[2]])
        self.button_relay_3.config(image=new_image)
        self.button_relay_3.image = new_image  # To prevent garbage collection

    def set_relay_3_button(self):
        self.img_paths_relay_3 = [cmn.get_panel_path(self.type, "relay_3_off.png"), cmn.get_panel_path(self.type, "relay_3_on.png")]        
        self.photo_var_relay_3 = PhotoImage(file=self.img_paths_relay_3[self.current_relay_img_idx[2]])
        self.button_relay_3 = Button(image=self.photo_var_relay_3, borderwidth=0, highlightthickness=0, command=self.toggle_relay_3_img, relief="flat")
        self.button_relay_3.place(x=245.0, y=425.0, width=30.0, height=30.0)

    def toggle_relay_4_img(self):
        self.current_relay_img_idx[3] = 1 - self.current_relay_img_idx[3]
        new_image = PhotoImage(file=self.img_paths_relay_4[self.current_relay_img_idx[3]])
        self.button_relay_4.config(image=new_image)
        self.button_relay_4.image = new_image  # To prevent garbage collection

    def set_relay_4_button(self):
        self.img_paths_relay_4 = [cmn.get_panel_path(self.type, "relay_4_off.png"), cmn.get_panel_path(self.type, "relay_4_on.png")]        
        self.photo_var_relay_4 = PhotoImage(file=self.img_paths_relay_4[self.current_relay_img_idx[3]])
        self.button_relay_4 = Button(image=self.photo_var_relay_4, borderwidth=0, highlightthickness=0, command=self.toggle_relay_4_img, relief="flat")
        self.button_relay_4.place(x=285.0, y=425.0, width=30.0, height=30.0)

    def toggle_relay_5_img(self):
        self.current_relay_img_idx[4] = 1 - self.current_relay_img_idx[4]
        new_image = PhotoImage(file=self.img_paths_relay_5[self.current_relay_img_idx[4]])
        self.button_relay_5.config(image=new_image)
        self.button_relay_5.image = new_image  # To prevent garbage collection

    def set_relay_5_button(self):
        self.img_paths_relay_5 = [cmn.get_panel_path(self.type, "relay_5_off.png"), cmn.get_panel_path(self.type, "relay_5_on.png")]        
        self.photo_var_relay_5 = PhotoImage(file=self.img_paths_relay_5[self.current_relay_img_idx[4]])
        self.button_relay_5 = Button(image=self.photo_var_relay_5, borderwidth=0, highlightthickness=0, command=self.toggle_relay_5_img, relief="flat")
        self.button_relay_5.place(x=165.0, y=465.0, width=30.0, height=30.0)

    def toggle_relay_6_img(self):
        self.current_relay_img_idx[5] = 1 - self.current_relay_img_idx[5]
        new_image = PhotoImage(file=self.img_paths_relay_6[self.current_relay_img_idx[5]])
        self.button_relay_6.config(image=new_image)
        self.button_relay_6.image = new_image  # To prevent garbage collection

    def set_relay_6_button(self):
        self.img_paths_relay_6 = [cmn.get_panel_path(self.type, "relay_6_off.png"), cmn.get_panel_path(self.type, "relay_6_on.png")]        
        self.photo_var_relay_6 = PhotoImage(file=self.img_paths_relay_6[self.current_relay_img_idx[5]])
        self.button_relay_6 = Button(image=self.photo_var_relay_6, borderwidth=0, highlightthickness=0, command=self.toggle_relay_6_img, relief="flat")
        self.button_relay_6.place(x=205.0, y=465.0, width=30.0, height=30.0)

    def toggle_relay_7_img(self):
        self.current_relay_img_idx[6] = 1 - self.current_relay_img_idx[6]
        new_image = PhotoImage(file=self.img_paths_relay_7[self.current_relay_img_idx[6]])
        self.button_relay_7.config(image=new_image)
        self.button_relay_7.image = new_image  # To prevent garbage collection

    def set_relay_7_button(self):
        self.img_paths_relay_7 = [cmn.get_panel_path(self.type, "relay_7_off.png"), cmn.get_panel_path(self.type, "relay_7_on.png")]        
        self.photo_var_relay_7 = PhotoImage(file=self.img_paths_relay_7[self.current_relay_img_idx[6]])
        self.button_relay_7 = Button(image=self.photo_var_relay_7, borderwidth=0, highlightthickness=0, command=self.toggle_relay_7_img, relief="flat")
        self.button_relay_7.place(x=245.0, y=465.0, width=30.0, height=30.0)

    def toggle_relay_8_img(self):
        self.current_relay_img_idx[7] = 1 - self.current_relay_img_idx[7]
        new_image = PhotoImage(file=self.img_paths_relay_8[self.current_relay_img_idx[7]])
        self.button_relay_8.config(image=new_image)
        self.button_relay_8.image = new_image  # To prevent garbage collection

    def set_relay_8_button(self):
        self.img_paths_relay_8 = [cmn.get_panel_path(self.type, "relay_8_off.png"), cmn.get_panel_path(self.type, "relay_8_on.png")]        
        self.photo_var_relay_8 = PhotoImage(file=self.img_paths_relay_8[self.current_relay_img_idx[7]])
        self.button_relay_8 = Button(image=self.photo_var_relay_8, borderwidth=0, highlightthickness=0, command=self.toggle_relay_8_img, relief="flat")
        self.button_relay_8.place(x=285.0, y=465.0, width=30.0, height=30.0)

    def toggle_relay_9_img(self):
        self.current_relay_img_idx[8] = 1 - self.current_relay_img_idx[8]
        new_image = PhotoImage(file=self.img_paths_relay_9[self.current_relay_img_idx[8]])
        self.button_relay_9.config(image=new_image)
        self.button_relay_9.image = new_image  # To prevent garbage collection

    def set_relay_9_button(self):
        self.img_paths_relay_9 = [cmn.get_panel_path(self.type, "relay_9_off.png"), cmn.get_panel_path(self.type, "relay_9_on.png")]        
        self.photo_var_relay_9 = PhotoImage(file=self.img_paths_relay_9[self.current_relay_img_idx[8]])
        self.button_relay_9 = Button(image=self.photo_var_relay_9, borderwidth=0, highlightthickness=0, command=self.toggle_relay_9_img, relief="flat")
        self.button_relay_9.place(x=165.0, y=505.0, width=30.0, height=30.0)

    def toggle_relay_10_img(self):
        self.current_relay_img_idx[9] = 1 - self.current_relay_img_idx[9]
        new_image = PhotoImage(file=self.img_paths_relay_10[self.current_relay_img_idx[9]])
        self.button_relay_10.config(image=new_image)
        self.button_relay_10.image = new_image  # To prevent garbage collection

    def set_relay_10_button(self):
        self.img_paths_relay_10 = [cmn.get_panel_path(self.type, "relay_10_off.png"), cmn.get_panel_path(self.type, "relay_10_on.png")]        
        self.photo_var_relay_10 = PhotoImage(file=self.img_paths_relay_10[self.current_relay_img_idx[9]])
        self.button_relay_10 = Button(image=self.photo_var_relay_10, borderwidth=0, highlightthickness=0, command=self.toggle_relay_10_img, relief="flat")
        self.button_relay_10.place(x=205.0, y=505.0, width=30.0, height=30.0)

    def toggle_relay_11_img(self):
        self.current_relay_img_idx[10] = 1 - self.current_relay_img_idx[10]
        new_image = PhotoImage(file=self.img_paths_relay_11[self.current_relay_img_idx[10]])
        self.button_relay_11.config(image=new_image)
        self.button_relay_11.image = new_image  # To prevent garbage collection

    def set_relay_11_button(self):
        self.img_paths_relay_11 = [cmn.get_panel_path(self.type, "relay_11_off.png"), cmn.get_panel_path(self.type, "relay_11_on.png")]        
        self.photo_var_relay_11 = PhotoImage(file=self.img_paths_relay_11[self.current_relay_img_idx[10]])
        self.button_relay_11 = Button(image=self.photo_var_relay_11, borderwidth=0, highlightthickness=0, command=self.toggle_relay_11_img, relief="flat")
        self.button_relay_11.place(x=245.0, y=505.0, width=30.0, height=30.0)

    def toggle_relay_12_img(self):
        self.current_relay_img_idx[11] = 1 - self.current_relay_img_idx[11]
        new_image = PhotoImage(file=self.img_paths_relay_12[self.current_relay_img_idx[11]])
        self.button_relay_12.config(image=new_image)
        self.button_relay_12.image = new_image  # To prevent garbage collection

    def set_relay_12_button(self):
        self.img_paths_relay_12 = [cmn.get_panel_path(self.type, "relay_12_off.png"), cmn.get_panel_path(self.type, "relay_12_on.png")]        
        self.photo_var_relay_12 = PhotoImage(file=self.img_paths_relay_12[self.current_relay_img_idx[11]])
        self.button_relay_12 = Button(image=self.photo_var_relay_12, borderwidth=0, highlightthickness=0, command=self.toggle_relay_12_img, relief="flat")
        self.button_relay_12.place(x=285.0, y=505.0, width=30.0, height=30.0)

    def toggle_relay_13_img(self):
        self.current_relay_img_idx[12] = 1 - self.current_relay_img_idx[12]
        new_image = PhotoImage(file=self.img_paths_relay_13[self.current_relay_img_idx[12]])
        self.button_relay_13.config(image=new_image)
        self.button_relay_13.image = new_image  # To prevent garbage collection

    def set_relay_13_button(self):
        self.img_paths_relay_13 = [cmn.get_panel_path(self.type, "relay_13_off.png"), cmn.get_panel_path(self.type, "relay_13_on.png")]        
        self.photo_var_relay_13 = PhotoImage(file=self.img_paths_relay_13[self.current_relay_img_idx[12]])
        self.button_relay_13 = Button(image=self.photo_var_relay_13, borderwidth=0, highlightthickness=0, command=self.toggle_relay_13_img, relief="flat")
        self.button_relay_13.place(x=165.0, y=545.0, width=30.0, height=30.0)

    def toggle_relay_14_img(self):
        self.current_relay_img_idx[13] = 1 - self.current_relay_img_idx[13]
        new_image = PhotoImage(file=self.img_paths_relay_14[self.current_relay_img_idx[13]])
        self.button_relay_14.config(image=new_image)
        self.button_relay_14.image = new_image  # To prevent garbage collection

    def set_relay_14_button(self):
        self.img_paths_relay_14 = [cmn.get_panel_path(self.type, "relay_14_off.png"), cmn.get_panel_path(self.type, "relay_14_on.png")]        
        self.photo_var_relay_14 = PhotoImage(file=self.img_paths_relay_14[self.current_relay_img_idx[13]])
        self.button_relay_14 = Button(image=self.photo_var_relay_14, borderwidth=0, highlightthickness=0, command=self.toggle_relay_14_img, relief="flat")
        self.button_relay_14.place(x=205.0, y=545.0, width=30.0, height=30.0)

    def toggle_relay_15_img(self):
        self.current_relay_img_idx[14] = 1 - self.current_relay_img_idx[14]
        new_image = PhotoImage(file=self.img_paths_relay_15[self.current_relay_img_idx[14]])
        self.button_relay_15.config(image=new_image)
        self.button_relay_15.image = new_image  # To prevent garbage collection

    def set_relay_15_button(self):
        self.img_paths_relay_15 = [cmn.get_panel_path(self.type, "relay_15_off.png"), cmn.get_panel_path(self.type, "relay_15_on.png")]        
        self.photo_var_relay_15 = PhotoImage(file=self.img_paths_relay_15[self.current_relay_img_idx[14]])
        self.button_relay_15 = Button(image=self.photo_var_relay_15, borderwidth=0, highlightthickness=0, command=self.toggle_relay_15_img, relief="flat")
        self.button_relay_15.place(x=245.0, y=545.0, width=30.0, height=30.0)

    def toggle_relay_16_img(self):
        self.current_relay_img_idx[15] = 1 - self.current_relay_img_idx[15]
        new_image = PhotoImage(file=self.img_paths_relay_16[self.current_relay_img_idx[15]])
        self.button_relay_16.config(image=new_image)
        self.button_relay_16.image = new_image  # To prevent garbage collection

    def set_relay_16_button(self):
        self.img_paths_relay_16 = [cmn.get_panel_path(self.type, "relay_16_off.png"), cmn.get_panel_path(self.type, "relay_16_on.png")]        
        self.photo_var_relay_16 = PhotoImage(file=self.img_paths_relay_16[self.current_relay_img_idx[15]])
        self.button_relay_16 = Button(image=self.photo_var_relay_16, borderwidth=0, highlightthickness=0, command=self.toggle_relay_16_img, relief="flat")
        self.button_relay_16.place(x=285.0, y=545.0, width=30.0, height=30.0)
    
    def manage_all_relays(self):        
        if not self.relays_var.get() :
            self.current_relay_img_idx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            self.current_relay_img_idx = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            
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

    def toggle_gpio_0_img(self):
        self.current_gpio_img_idx[0] = 1 - self.current_gpio_img_idx[0]
        new_image = PhotoImage(file=self.img_paths_gpio_0[self.current_gpio_img_idx[0]])
        self.button_gpio_0.config(image=new_image)
        self.button_gpio_0.image = new_image  # To prevent garbage collection

    def set_gpio_0_button(self):
        self.img_paths_gpio_0 = [cmn.get_panel_path(self.type, "gpio_0_off.png"), cmn.get_panel_path(self.type, "gpio_0_on.png")]        
        self.photo_var_gpio_0 = PhotoImage(file=self.img_paths_gpio_0[self.current_gpio_img_idx[0]])
        self.button_gpio_0 = Button(image=self.photo_var_gpio_0, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_0_img, relief="flat")
        self.button_gpio_0.place(x=147.0, y=824.0, width=36.0, height=36.0)

    def toggle_gpio_1_img(self):
        self.current_gpio_img_idx[1] = 1 - self.current_gpio_img_idx[1]
        new_image = PhotoImage(file=self.img_paths_gpio_1[self.current_gpio_img_idx[1]])
        self.button_gpio_1.config(image=new_image)
        self.button_gpio_1.image = new_image  # To prevent garbage collection

    def set_gpio_1_button(self):
        self.img_paths_gpio_1 = [cmn.get_panel_path(self.type, "gpio_1_off.png"), cmn.get_panel_path(self.type, "gpio_1_on.png")]        
        self.photo_var_gpio_1 = PhotoImage(file=self.img_paths_gpio_1[self.current_gpio_img_idx[1]])
        self.button_gpio_1 = Button(image=self.photo_var_gpio_1, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_1_img, relief="flat")
        self.button_gpio_1.place(x=170.0, y=774.0, width=36.0, height=36.0)

    def toggle_gpio_2_img(self):
        self.current_gpio_img_idx[2] = 1 - self.current_gpio_img_idx[2]
        new_image = PhotoImage(file=self.img_paths_gpio_2[self.current_gpio_img_idx[2]])
        self.button_gpio_2.config(image=new_image)
        self.button_gpio_2.image = new_image  # To prevent garbage collection

    def set_gpio_2_button(self):
        self.img_paths_gpio_2 = [cmn.get_panel_path(self.type, "gpio_2_off.png"), cmn.get_panel_path(self.type, "gpio_2_on.png")]        
        self.photo_var_gpio_2 = PhotoImage(file=self.img_paths_gpio_2[self.current_gpio_img_idx[2]])
        self.button_gpio_2 = Button(image=self.photo_var_gpio_2, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_2_img, relief="flat")
        self.button_gpio_2.place(x=222.0, y=749.0, width=36.0, height=36.0)

    def toggle_gpio_3_img(self):
        self.current_gpio_img_idx[3] = 1 - self.current_gpio_img_idx[3]
        new_image = PhotoImage(file=self.img_paths_gpio_3[self.current_gpio_img_idx[3]])
        self.button_gpio_3.config(image=new_image)
        self.button_gpio_3.image = new_image  # To prevent garbage collection

    def set_gpio_3_button(self):
        self.img_paths_gpio_3 = [cmn.get_panel_path(self.type, "gpio_3_off.png"), cmn.get_panel_path(self.type, "gpio_3_on.png")]        
        self.photo_var_gpio_3 = PhotoImage(file=self.img_paths_gpio_3[self.current_gpio_img_idx[3]])
        self.button_gpio_3 = Button(image=self.photo_var_gpio_3, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_3_img, relief="flat")
        self.button_gpio_3.place(x=271.0, y=774.0, width=36.0, height=36.0)

    def toggle_gpio_4_img(self):
        self.current_gpio_img_idx[4] = 1 - self.current_gpio_img_idx[4]
        new_image = PhotoImage(file=self.img_paths_gpio_4[self.current_gpio_img_idx[4]])
        self.button_gpio_4.config(image=new_image)
        self.button_gpio_4.image = new_image  # To prevent garbage collection

    def set_gpio_4_button(self):
        self.img_paths_gpio_4 = [cmn.get_panel_path(self.type, "gpio_4_off.png"), cmn.get_panel_path(self.type, "gpio_4_on.png")]        
        self.photo_var_gpio_4 = PhotoImage(file=self.img_paths_gpio_4[self.current_gpio_img_idx[4]])
        self.button_gpio_4 = Button(image=self.photo_var_gpio_4, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_4_img, relief="flat")
        self.button_gpio_4.place(x=296.0, y=824.0, width=36.0, height=36.0)

    def toggle_gpio_5_img(self):
        self.current_gpio_img_idx[5] = 1 - self.current_gpio_img_idx[5]
        new_image = PhotoImage(file=self.img_paths_gpio_5[self.current_gpio_img_idx[5]])
        self.button_gpio_5.config(image=new_image)
        self.button_gpio_5.image = new_image  # To prevent garbage collection

    def set_gpio_5_button(self):
        self.img_paths_gpio_5 = [cmn.get_panel_path(self.type, "gpio_5_off.png"), cmn.get_panel_path(self.type, "gpio_5_on.png")]        
        self.photo_var_gpio_5 = PhotoImage(file=self.img_paths_gpio_5[self.current_gpio_img_idx[5]])
        self.button_gpio_5 = Button(image=self.photo_var_gpio_5, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_5_img, relief="flat")
        self.button_gpio_5.place(x=271.0, y=873.0, width=36.0, height=36.0)

    def toggle_gpio_6_img(self):
        self.current_gpio_img_idx[6] = 1 - self.current_gpio_img_idx[6]
        new_image = PhotoImage(file=self.img_paths_gpio_6[self.current_gpio_img_idx[6]])
        self.button_gpio_6.config(image=new_image)
        self.button_gpio_6.image = new_image  # To prevent garbage collection

    def set_gpio_6_button(self):
        self.img_paths_gpio_6 = [cmn.get_panel_path(self.type, "gpio_6_off.png"), cmn.get_panel_path(self.type, "gpio_6_on.png")]        
        self.photo_var_gpio_6 = PhotoImage(file=self.img_paths_gpio_6[self.current_gpio_img_idx[6]])
        self.button_gpio_6 = Button(image=self.photo_var_gpio_6, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_6_img, relief="flat")
        self.button_gpio_6.place(x=222.0, y=899.0, width=36.0, height=36.0)

    def toggle_gpio_7_img(self):
        self.current_gpio_img_idx[7] = 1 - self.current_gpio_img_idx[7]
        new_image = PhotoImage(file=self.img_paths_gpio_7[self.current_gpio_img_idx[7]])
        self.button_gpio_7.config(image=new_image)
        self.button_gpio_7.image = new_image  # To prevent garbage collection

    def set_gpio_7_button(self):
        self.img_paths_gpio_7 = [cmn.get_panel_path(self.type, "gpio_7_off.png"), cmn.get_panel_path(self.type, "gpio_7_on.png")]        
        self.photo_var_gpio_7 = PhotoImage(file=self.img_paths_gpio_7[self.current_gpio_img_idx[7]])
        self.button_gpio_7 = Button(image=self.photo_var_gpio_7, borderwidth=0, highlightthickness=0, command=self.toggle_gpio_7_img, relief="flat")
        self.button_gpio_7.place(x=170.0, y=873.0, width=36.0, height=36.0)

    def manage_all_gpios(self):        
        if not self.gpios_var.get():
            self.current_gpio_img_idx = [0, 0, 0, 0, 0, 0, 0, 0]
        else:
            self.current_gpio_img_idx = [1, 1, 1, 1, 1, 1, 1, 1]
            
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


class ManualTestSection:
    def __init__(self, cover_window):        
        self.mainwindow = cover_window
        self.type = "manual"
        
        # Horizontal Shift
        self.shift = 480.0
        
        self.canvas = Canvas(self.mainwindow, bg = "#FF0000", height = 1017, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x=0 + self.shift, y=0)

        # Relays Section
        self.canvas.create_text(365.0, 25.0, anchor="nw", text="1", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_1 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_1 = self.canvas.create_image(372.0, 88.0, image=self.relay_img_1)

        self.canvas.create_text(597.0, 25.0, anchor="nw", text="2", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_2 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_2 = self.canvas.create_image(604.0, 88.0, image=self.relay_img_2)

        self.canvas.create_text(828.0, 25.0, anchor="nw", text="3", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_3 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_3 = self.canvas.create_image(836.0, 88.0, image=self.relay_img_3)

        self.canvas.create_text(1060.0, 25.0, anchor="nw", text="4", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_4 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_4 = self.canvas.create_image(1068.0, 88.0, image=self.relay_img_4)

        self.canvas.create_text(365.0, 148.0, anchor="nw", text="5", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_5 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_5 = self.canvas.create_image(372.0, 211.0, image=self.relay_img_5)

        self.canvas.create_text(597.0, 148.0, anchor="nw", text="6", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_6 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_6 = self.canvas.create_image(604.0, 211.0, image=self.relay_img_6)

        self.canvas.create_text(828.0, 148.0, anchor="nw", text="7", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_7 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_7 = self.canvas.create_image(836.0, 211.0, image=self.relay_img_7)

        self.canvas.create_text(1060.0, 148.0, anchor="nw", text="8", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_8 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_8 = self.canvas.create_image(1068.0, 211.0, image=self.relay_img_8)

        self.canvas.create_text(365.0, 270.0, anchor="nw", text="9", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_9 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_9 = self.canvas.create_image(372.0, 333.0, image=self.relay_img_9)

        self.canvas.create_text(589.0, 270.0, anchor="nw", text="10", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_10 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_10 = self.canvas.create_image(604.0, 333.0, image=self.relay_img_10)

        self.canvas.create_text(820.0, 270.0, anchor="nw", text="11", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_11 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_11 = self.canvas.create_image(836.0, 333.0, image=self.relay_img_11)

        self.canvas.create_text(1051.0, 270.0, anchor="nw", text="12", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_12 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_12 = self.canvas.create_image(1068.0, 333.0, image=self.relay_img_12)

        self.canvas.create_text(357.0, 392.0, anchor="nw", text="13", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_13 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_13 = self.canvas.create_image(372.0, 455.0, image=self.relay_img_13)

        self.canvas.create_text(589.0, 392.0, anchor="nw", text="14", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_14 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_14 = self.canvas.create_image(604.0, 455.0, image=self.relay_img_14)

        self.canvas.create_text(820.0, 392.0, anchor="nw", text="15", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_15 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_15 = self.canvas.create_image(836.0, 455.0, image=self.relay_img_15)

        self.canvas.create_text(1051.0, 392.0, anchor="nw", text="16", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.relay_img_16 = PhotoImage(file=cmn.get_test_path(self.type, "open.png"))
        self.relay_16 = self.canvas.create_image(1068.0, 455.0, image=self.relay_img_16)

        #GPIOs Section
        self.canvas.create_text(365.0, 568.0, anchor="nw", text="0", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_0 = PhotoImage(file=cmn.get_test_path(self.type, "off.png"))
        self.gpio_0 = self.canvas.create_image(372.0, 659.0, image=self.gpio_img_0)

        self.canvas.create_text(597.0, 568.0, anchor="nw", text="1", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_1 = PhotoImage(file=cmn.get_test_path(self.type, "off.png"))
        self.gpio_1 = self.canvas.create_image(604.0, 659.0, image=self.gpio_img_1)

        self.canvas.create_text(828.0, 568.0, anchor="nw", text="2", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_2 = PhotoImage(file=cmn.get_test_path(self.type, "off.png"))
        self.gpio_2 = self.canvas.create_image(836.0, 659.0, image=self.gpio_img_2)

        self.canvas.create_text(1060.0, 568.0, anchor="nw", text="3", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_3 = PhotoImage(file=cmn.get_test_path(self.type, "off.png"))
        self.gpio_3 = self.canvas.create_image(1068.0, 659.0, image=self.gpio_img_3)

        self.canvas.create_text(365.0, 743.0, anchor="nw", text="4", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_4 = PhotoImage(file=cmn.get_test_path(self.type, "off.png"))
        self.gpio_4 = self.canvas.create_image(372.0, 835.0, image=self.gpio_img_4)

        self.canvas.create_text(597.0, 743.0, anchor="nw", text="5", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_5 = PhotoImage(file=cmn.get_test_path(self.type, "off.png"))
        self.gpio_5 = self.canvas.create_image(604.0, 835.0, image=self.gpio_img_5)

        self.canvas.create_text(828.0, 743.0, anchor="nw", text="6", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_6 = PhotoImage(file=cmn.get_test_path(self.type, "off.png"))
        self.gpio_6 = self.canvas.create_image(836.0, 835.0, image=self.gpio_img_6)

        self.canvas.create_text(1060.0, 743.0, anchor="nw", text="7", fill="#FFFFFF", font=("Inter Medium", 24 * -1))
        self.gpio_img_7 = PhotoImage(file=cmn.get_test_path(self.type, "off.png"))
        self.gpio_7 = self.canvas.create_image(1068.0, 835.0, image=self.gpio_img_7)

        # Buttons Section
        self.run_img = PhotoImage(file=cmn.get_test_path(self.type, "run.png"))
        self.run_button = Button(image=self.run_img, borderwidth=0, highlightthickness=0, command=lambda: print("run button clicked"), relief="flat")
        self.run_button.place(x=450.0 + self.shift, y=944.0, width=161.0, height=50.0)

        self.quit_img = PhotoImage(file=cmn.get_test_path(self.type, "quit.png"))
        self.quit_button = Button(image=self.quit_img, borderwidth=0, highlightthickness=0, command=lambda: cover_window.destroy(), relief="flat")
        self.quit_button.place(x=641.0 + self.shift, y=944.0, width=161.0, height=50.0)

        self.back_img = PhotoImage(file=cmn.get_test_path(self.type, "back.png"))
        self.back_button = Button(image=self.back_img, borderwidth=0, highlightthickness=0, command=lambda: print("back button clicked"), relief="flat")
        self.back_button.place(x=832.0 + self.shift, y=944.0, width=161.0, height=50.0)
        
    def run(self):
        self.mainwindow.mainloop()

def on_btn_click(cover_window):
    cmn.clear_current_window(cover_window)
    panel = ManualTestPanel(cover_window)
    test = ManualTestSection(cover_window)
    panel.run()
    test.run()