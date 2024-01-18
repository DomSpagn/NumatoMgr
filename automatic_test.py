# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, OptionMenu, Button, PhotoImage, Checkbutton, BooleanVar, StringVar

import common as cmn


class AutomaticTestPanel:
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
        self.com_var.trace('w', lambda *args: cmn.on_com_select(self.com_var, *args))
        self.list_of_active_COMs = cmn.list_serial_ports()
        self.select_com_dropdown_menu = OptionMenu(self.canvas, self.com_var, *self.list_of_active_COMs)
        self.select_com_dropdown_menu.config(width=12, height=1, anchor='center', font=('Inter', 14))
        self.com_menu = self.select_com_dropdown_menu.nametowidget(self.select_com_dropdown_menu.menuname)
        self.com_menu.configure(font=('Inter', 14))
        self.select_com_dropdown_menu.place(x=152, y=77)        

        # Select Baudrate Dropdown Menu
        self.baudrate_var = StringVar(self.canvas)
        self.baudrate_var.set("Select Baudrate")
        self.baudrate_var.trace('w', lambda *args: cmn.on_baudrate_select(self.baudrate_var, *args))
        self.baudrate_list = cmn.get_baudrate_list()
        self.select_com_dropdown_menu = OptionMenu(self.canvas, self.baudrate_var, *self.baudrate_list)
        self.select_com_dropdown_menu.config(width=12, height=1, anchor='center', font=('Inter', 14))  # Impostazione larghezza e altezza del bottone
        self.com_menu = self.select_com_dropdown_menu.nametowidget(self.select_com_dropdown_menu.menuname)
        self.com_menu.configure(font=('Inter', 14))
        self.select_com_dropdown_menu.place(x=152, y=147)        

        # First Blue Line
        self.canvas.create_rectangle(0, 230.0, 480.0, 230.0, fill="#0000FF", outline="")

        # Relays Section
        self.canvas.create_text(196.0, 241.0, anchor="nw", text="Relays", fill="#FFFFFF", font=("Inter Black", 28 * -1))
        self.current_image_index = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

        '''
        # GPIOs Section
        self.canvas.create_text(197.0, 558.0, anchor="nw", text="GPIOs", fill="#FFFFFF", font=("Inter Black", 28 * -1))

        self.button_img_gpio_0 = PhotoImage(file=cmn.get_panel_path("gpio_0_off.png"))
        self.button_gpio_0 = Button(image=self.button_img_gpio_0, borderwidth=0, highlightthickness=0, command=lambda: cmn.set_gpio_config(self, 0, 'off'), relief="flat")
        self.button_gpio_0.place(x=147.0, y=698.0, width=36.0, height=36.0)

        self.button_img_gpio_1 = PhotoImage(file=cmn.get_panel_path("gpio_1_off.png"))
        self.button_gpio_1 = Button(image=self.button_img_gpio_1, borderwidth=0, highlightthickness=0, command=lambda: cmn.set_gpio_config(self, 1, 'off'), relief="flat")
        self.button_gpio_1.place(x=170.0, y=648.0, width=36.0, height=36.0)

        self.button_img_gpio_2 = PhotoImage(file=cmn.get_panel_path("gpio_2_off.png"))
        self.button_gpio_2 = Button(image=self.button_img_gpio_2, borderwidth=0, highlightthickness=0, command=lambda: cmn.set_gpio_config(self, 2, 'off'), relief="flat")
        self.button_gpio_2.place(x=222.0, y=623.0, width=36.0, height=36.0)

        self.button_img_gpio_3 = PhotoImage(file=cmn.get_panel_path("gpio_3_off.png"))
        self.button_gpio_3 = Button(image=self.button_img_gpio_3, borderwidth=0, highlightthickness=0, command=lambda: cmn.set_gpio_config(self, 3, 'off'), relief="flat")
        self.button_gpio_3.place(x=271.0, y=648.0, width=36.0, height=36.0)

        self.button_img_gpio_4 = PhotoImage(file=cmn.get_panel_path("gpio_4_off.png"))
        self.button_gpio_4 = Button(image=self.button_img_gpio_4, borderwidth=0, highlightthickness=0, command=lambda: cmn.set_gpio_config(self, 4, 'off'), relief="flat")
        self.button_gpio_4.place(x=296.0, y=698.0, width=36.0, height=36.0)

        self.button_img_gpio_5 = PhotoImage(file=cmn.get_panel_path("gpio_5_off.png"))
        self.button_gpio_5 = Button(image=self.button_img_gpio_5, borderwidth=0, highlightthickness=0, command=lambda: cmn.set_gpio_config(self, 5, 'off'), relief="flat")
        self.button_gpio_5.place(x=271.0, y=747.0, width=36.0, height=36.0)

        self.button_img_gpio_6 = PhotoImage(file=cmn.get_panel_path("gpio_6_off.png"))
        self.button_gpio_6 = Button(image=self.button_img_gpio_6, borderwidth=0, highlightthickness=0, command=lambda: cmn.set_gpio_config(self, 6, 'off'), relief="flat")
        self.button_gpio_6.place(x=222.0, y=773.0, width=36.0, height=36.0)

        self.button_img_gpio_7 = PhotoImage(file=cmn.get_panel_path("gpio_7_off.png"))
        self.button_gpio_7 = Button(image=self.button_img_gpio_7, borderwidth=0, highlightthickness=0, command=lambda: cmn.set_gpio_config(self, 7, 'off'), relief="flat")
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
        '''
        
    def toggle_relay_1_img(self):
        self.current_image_index[0] = 1 - self.current_image_index[0]
        new_image = PhotoImage(file=self.image_paths_1[self.current_image_index[0]])
        self.button_relay_1.config(image=new_image)
        self.button_relay_1.image = new_image  # To prevent garbage collection

    def set_relay_1_button(self):
        self.image_paths_1 = [cmn.get_panel_path(self.type, "relay_1_off.png"), cmn.get_panel_path(self.type, "relay_1_on.png")]        
        self.photo_var_1 = PhotoImage(file=self.image_paths_1[self.current_image_index[0]])
        self.button_relay_1 = Button(image=self.photo_var_1, borderwidth=0, highlightthickness=0, command=self.toggle_relay_1_img, relief="flat")
        self.button_relay_1.place(x=165.0, y=306.0, width=30.0, height=30.0)

    def toggle_relay_2_img(self):
        self.current_image_index[1] = 1 - self.current_image_index[1]
        new_image = PhotoImage(file=self.image_paths_2[self.current_image_index[1]])
        self.button_relay_2.config(image=new_image)
        self.button_relay_2.image = new_image  # To prevent garbage collection

    def set_relay_2_button(self):
        self.image_paths_2 = [cmn.get_panel_path(self.type, "relay_2_off.png"), cmn.get_panel_path(self.type, "relay_2_on.png")]        
        self.photo_var_2 = PhotoImage(file=self.image_paths_2[self.current_image_index[1]])
        self.button_relay_2 = Button(image=self.photo_var_2, borderwidth=0, highlightthickness=0, command=self.toggle_relay_2_img, relief="flat")
        self.button_relay_2.place(x=205.0, y=306.0, width=30.0, height=30.0)

    def toggle_relay_3_img(self):
        self.current_image_index[2] = 1 - self.current_image_index[2]
        new_image = PhotoImage(file=self.image_paths_3[self.current_image_index[2]])
        self.button_relay_3.config(image=new_image)
        self.button_relay_3.image = new_image  # To prevent garbage collection

    def set_relay_3_button(self):
        self.image_paths_3 = [cmn.get_panel_path(self.type, "relay_3_off.png"), cmn.get_panel_path(self.type, "relay_3_on.png")]        
        self.photo_var_3 = PhotoImage(file=self.image_paths_3[self.current_image_index[2]])
        self.button_relay_3 = Button(image=self.photo_var_3, borderwidth=0, highlightthickness=0, command=self.toggle_relay_3_img, relief="flat")
        self.button_relay_3.place(x=245.0, y=306.0, width=30.0, height=30.0)

    def toggle_relay_4_img(self):
        self.current_image_index[3] = 1 - self.current_image_index[3]
        new_image = PhotoImage(file=self.image_paths_4[self.current_image_index[3]])
        self.button_relay_4.config(image=new_image)
        self.button_relay_4.image = new_image  # To prevent garbage collection

    def set_relay_4_button(self):
        self.image_paths_4 = [cmn.get_panel_path(self.type, "relay_4_off.png"), cmn.get_panel_path(self.type, "relay_4_on.png")]        
        self.photo_var_4 = PhotoImage(file=self.image_paths_4[self.current_image_index[3]])
        self.button_relay_4 = Button(image=self.photo_var_4, borderwidth=0, highlightthickness=0, command=self.toggle_relay_4_img, relief="flat")
        self.button_relay_4.place(x=285.0, y=306.0, width=30.0, height=30.0)

    def toggle_relay_5_img(self):
        self.current_image_index[4] = 1 - self.current_image_index[4]
        new_image = PhotoImage(file=self.image_paths_5[self.current_image_index[4]])
        self.button_relay_5.config(image=new_image)
        self.button_relay_5.image = new_image  # To prevent garbage collection

    def set_relay_5_button(self):
        self.image_paths_5 = [cmn.get_panel_path(self.type, "relay_5_off.png"), cmn.get_panel_path(self.type, "relay_5_on.png")]        
        self.photo_var_5 = PhotoImage(file=self.image_paths_5[self.current_image_index[4]])
        self.button_relay_5 = Button(image=self.photo_var_5, borderwidth=0, highlightthickness=0, command=self.toggle_relay_5_img, relief="flat")
        self.button_relay_5.place(x=165.0, y=346.0, width=30.0, height=30.0)

    def toggle_relay_6_img(self):
        self.current_image_index[5] = 1 - self.current_image_index[5]
        new_image = PhotoImage(file=self.image_paths_6[self.current_image_index[5]])
        self.button_relay_6.config(image=new_image)
        self.button_relay_6.image = new_image  # To prevent garbage collection

    def set_relay_6_button(self):
        self.image_paths_6 = [cmn.get_panel_path(self.type, "relay_6_off.png"), cmn.get_panel_path(self.type, "relay_6_on.png")]        
        self.photo_var_6 = PhotoImage(file=self.image_paths_6[self.current_image_index[5]])
        self.button_relay_6 = Button(image=self.photo_var_6, borderwidth=0, highlightthickness=0, command=self.toggle_relay_6_img, relief="flat")
        self.button_relay_6.place(x=205.0, y=346.0, width=30.0, height=30.0)

    def toggle_relay_7_img(self):
        self.current_image_index[6] = 1 - self.current_image_index[6]
        new_image = PhotoImage(file=self.image_paths_7[self.current_image_index[6]])
        self.button_relay_7.config(image=new_image)
        self.button_relay_7.image = new_image  # To prevent garbage collection

    def set_relay_7_button(self):
        self.image_paths_7 = [cmn.get_panel_path(self.type, "relay_7_off.png"), cmn.get_panel_path(self.type, "relay_7_on.png")]        
        self.photo_var_7 = PhotoImage(file=self.image_paths_7[self.current_image_index[6]])
        self.button_relay_7 = Button(image=self.photo_var_7, borderwidth=0, highlightthickness=0, command=self.toggle_relay_7_img, relief="flat")
        self.button_relay_7.place(x=245.0, y=346.0, width=30.0, height=30.0)

    def toggle_relay_8_img(self):
        self.current_image_index[7] = 1 - self.current_image_index[7]
        new_image = PhotoImage(file=self.image_paths_8[self.current_image_index[7]])
        self.button_relay_8.config(image=new_image)
        self.button_relay_8.image = new_image  # To prevent garbage collection

    def set_relay_8_button(self):
        self.image_paths_8 = [cmn.get_panel_path(self.type, "relay_8_off.png"), cmn.get_panel_path(self.type, "relay_8_on.png")]        
        self.photo_var_8 = PhotoImage(file=self.image_paths_8[self.current_image_index[7]])
        self.button_relay_8 = Button(image=self.photo_var_8, borderwidth=0, highlightthickness=0, command=self.toggle_relay_8_img, relief="flat")
        self.button_relay_8.place(x=285.0, y=346.0, width=30.0, height=30.0)

    def toggle_relay_9_img(self):
        self.current_image_index[8] = 1 - self.current_image_index[8]
        new_image = PhotoImage(file=self.image_paths_9[self.current_image_index[8]])
        self.button_relay_9.config(image=new_image)
        self.button_relay_9.image = new_image  # To prevent garbage collection

    def set_relay_9_button(self):
        self.image_paths_9 = [cmn.get_panel_path(self.type, "relay_9_off.png"), cmn.get_panel_path(self.type, "relay_9_on.png")]        
        self.photo_var_9 = PhotoImage(file=self.image_paths_9[self.current_image_index[8]])
        self.button_relay_9 = Button(image=self.photo_var_9, borderwidth=0, highlightthickness=0, command=self.toggle_relay_9_img, relief="flat")
        self.button_relay_9.place(x=165.0, y=386.0, width=30.0, height=30.0)

    def toggle_relay_10_img(self):
        self.current_image_index[9] = 1 - self.current_image_index[9]
        new_image = PhotoImage(file=self.image_paths_10[self.current_image_index[9]])
        self.button_relay_10.config(image=new_image)
        self.button_relay_10.image = new_image  # To prevent garbage collection

    def set_relay_10_button(self):
        self.image_paths_10 = [cmn.get_panel_path(self.type, "relay_10_off.png"), cmn.get_panel_path(self.type, "relay_10_on.png")]        
        self.photo_var_10 = PhotoImage(file=self.image_paths_10[self.current_image_index[9]])
        self.button_relay_10 = Button(image=self.photo_var_10, borderwidth=0, highlightthickness=0, command=self.toggle_relay_10_img, relief="flat")
        self.button_relay_10.place(x=205.0, y=386.0, width=30.0, height=30.0)

    def toggle_relay_11_img(self):
        self.current_image_index[10] = 1 - self.current_image_index[10]
        new_image = PhotoImage(file=self.image_paths_11[self.current_image_index[10]])
        self.button_relay_11.config(image=new_image)
        self.button_relay_11.image = new_image  # To prevent garbage collection

    def set_relay_11_button(self):
        self.image_paths_11 = [cmn.get_panel_path(self.type, "relay_11_off.png"), cmn.get_panel_path(self.type, "relay_11_on.png")]        
        self.photo_var_11 = PhotoImage(file=self.image_paths_11[self.current_image_index[10]])
        self.button_relay_11 = Button(image=self.photo_var_11, borderwidth=0, highlightthickness=0, command=self.toggle_relay_11_img, relief="flat")
        self.button_relay_11.place(x=245.0, y=386.0, width=30.0, height=30.0)

    def toggle_relay_12_img(self):
        self.current_image_index[11] = 1 - self.current_image_index[11]
        new_image = PhotoImage(file=self.image_paths_12[self.current_image_index[11]])
        self.button_relay_12.config(image=new_image)
        self.button_relay_12.image = new_image  # To prevent garbage collection

    def set_relay_12_button(self):
        self.image_paths_12 = [cmn.get_panel_path(self.type, "relay_12_off.png"), cmn.get_panel_path(self.type, "relay_12_on.png")]        
        self.photo_var_12 = PhotoImage(file=self.image_paths_12[self.current_image_index[11]])
        self.button_relay_12 = Button(image=self.photo_var_12, borderwidth=0, highlightthickness=0, command=self.toggle_relay_12_img, relief="flat")
        self.button_relay_12.place(x=285.0, y=386.0, width=30.0, height=30.0)

    def toggle_relay_13_img(self):
        self.current_image_index[12] = 1 - self.current_image_index[12]
        new_image = PhotoImage(file=self.image_paths_13[self.current_image_index[12]])
        self.button_relay_13.config(image=new_image)
        self.button_relay_13.image = new_image  # To prevent garbage collection

    def set_relay_13_button(self):
        self.image_paths_13 = [cmn.get_panel_path(self.type, "relay_13_off.png"), cmn.get_panel_path(self.type, "relay_13_on.png")]        
        self.photo_var_13 = PhotoImage(file=self.image_paths_13[self.current_image_index[12]])
        self.button_relay_13 = Button(image=self.photo_var_13, borderwidth=0, highlightthickness=0, command=self.toggle_relay_13_img, relief="flat")
        self.button_relay_13.place(x=165.0, y=426.0, width=30.0, height=30.0)

    def toggle_relay_14_img(self):
        self.current_image_index[13] = 1 - self.current_image_index[13]
        new_image = PhotoImage(file=self.image_paths_14[self.current_image_index[13]])
        self.button_relay_14.config(image=new_image)
        self.button_relay_14.image = new_image  # To prevent garbage collection

    def set_relay_14_button(self):
        self.image_paths_14 = [cmn.get_panel_path(self.type, "relay_14_off.png"), cmn.get_panel_path(self.type, "relay_14_on.png")]        
        self.photo_var_14 = PhotoImage(file=self.image_paths_14[self.current_image_index[13]])
        self.button_relay_14 = Button(image=self.photo_var_14, borderwidth=0, highlightthickness=0, command=self.toggle_relay_14_img, relief="flat")
        self.button_relay_14.place(x=205.0, y=426.0, width=30.0, height=30.0)

    def toggle_relay_15_img(self):
        self.current_image_index[14] = 1 - self.current_image_index[14]
        new_image = PhotoImage(file=self.image_paths_15[self.current_image_index[14]])
        self.button_relay_15.config(image=new_image)
        self.button_relay_15.image = new_image  # To prevent garbage collection

    def set_relay_15_button(self):
        self.image_paths_15 = [cmn.get_panel_path(self.type, "relay_15_off.png"), cmn.get_panel_path(self.type, "relay_15_on.png")]        
        self.photo_var_15 = PhotoImage(file=self.image_paths_15[self.current_image_index[14]])
        self.button_relay_15 = Button(image=self.photo_var_15, borderwidth=0, highlightthickness=0, command=self.toggle_relay_15_img, relief="flat")
        self.button_relay_15.place(x=245.0, y=426.0, width=30.0, height=30.0)

    def toggle_relay_16_img(self):
        self.current_image_index[15] = 1 - self.current_image_index[15]
        new_image = PhotoImage(file=self.image_paths_16[self.current_image_index[15]])
        self.button_relay_16.config(image=new_image)
        self.button_relay_16.image = new_image  # To prevent garbage collection

    def set_relay_16_button(self):
        self.image_paths_16 = [cmn.get_panel_path(self.type, "relay_16_off.png"), cmn.get_panel_path(self.type, "relay_16_on.png")]        
        self.photo_var_16 = PhotoImage(file=self.image_paths_16[self.current_image_index[15]])
        self.button_relay_16 = Button(image=self.photo_var_16, borderwidth=0, highlightthickness=0, command=self.toggle_relay_16_img, relief="flat")
        self.button_relay_16.place(x=285.0, y=426.0, width=30.0, height=30.0)

    def manage_all_relays(self):        
        if(not self.relays_var.get()):
            self.current_image_index = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            self.current_image_index = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            
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
        self.terminal_img = PhotoImage(file=cmn.get_test_path("output_text.png"))
        self.terminal_bg = self.canvas.create_image(721.0, 264.0, image=self.terminal_img)
        self.terminal = Entry(bd=0, bg="#000000", fg="#000716", highlightthickness=0)
        self.terminal.place(x=293.0 + self.shift, y=76.0, width=856.0, height=426.0)
               
        # Gauge        
        self.gauge_img = PhotoImage(file=cmn.get_test_path("gauge.png"))
        self.gauge = self.canvas.create_image(720.0, 724.0, image=self.gauge_img)
        self.canvas.create_text(667.0, 695.0, anchor="nw", text="75%", fill="#FFFFFF", font=("Inter Black", 47 * -1))
        
        # Buttons Section
        self.run_img = PhotoImage(file=cmn.get_test_path("run.png"))
        self.run_button = Button(image=self.run_img, borderwidth=0, highlightthickness=0, command=lambda: print("run button clicked"), relief="flat")
        self.run_button.place(x=450.0 + self.shift, y=944.0, width=161.0, height=50.0)

        self.quit_img = PhotoImage(file=cmn.get_test_path("quit.png"))
        self.quit_button = Button(image=self.quit_img, borderwidth=0, highlightthickness=0, command=lambda: print("quit button clicked"), relief="flat")
        self.quit_button.place(x=641.0 + self.shift, y=944.0, width=161.0, height=50.0)

        self.back_img = PhotoImage(file=cmn.get_test_path("back.png"))
        self.back_button = Button(image=self.back_img, borderwidth=0, highlightthickness=0, command=lambda: print("back button clicked"), relief="flat")
        self.back_button.place(x=832.0 + self.shift, y=944.0, width=161.0, height=50.0)

    def run(self):
        self.mainwindow.mainloop()
    
def on_btn_click(cover_window):
    cmn.clear_current_window(cover_window)
    panel = AutomaticTestPanel(cover_window)
    #test = AutomaticTestSection(cover_window)
    panel.run()    
    #test.run()
