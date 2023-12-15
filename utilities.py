import tkinter as tk
from tkinter import ttk
import serial
import sys
import glob

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry("+{}+{}".format(x, y))
    
    
def create_debug_window(current_window, msg):
    debug_window = tk.Toplevel(current_window)
    debug_window.title("Debug")
    debug_window.geometry("300x100")
    
    # Creare uno stile per la finestra di debug
    style = ttk.Style()
    style.configure("Debug.TLabel", font=("Helvetica", 12))

    label = ttk.Label(debug_window, text="Error on func: " + msg, style="Debug.TLabel")
    label.pack(padx=10, pady=10)
    
    # Posiziona la finestra di debug al centro
    center_window(debug_window) 
   
    
def clear_current_window(current_window):    
    for widget in current_window.winfo_children():
        widget.destroy()


def list_serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def on_COM_select():
    selected_value = combobox.get()
    label_result.config(text=f"Selezionato: {selected_value}")


def select_COM(frame):
    try:            
        list_of_active_COMs = list_serial_ports()
               
        # Variabile di controllo per il menu a tendina
        selected_option = tk.StringVar(frame)

        # Creare il menu a tendina
        #COMs_menu = ttk.Combobox(frame, values=list_of_active_COMs)
        #COMs_menu.grid(row=0, column=0, padx=100, pady=100)
        
        # Collegare la funzione on_combobox_change all'evento "<<ComboboxSelected>>"
        #combobox.bind("<<ComboboxSelected>>", on_COM_select)        

    except:
        create_debug_window(frame, 'select_COM')


def on_baudrate_select():
    pass


def select_baudrate(current_window):
    try:            
        allowed_baudrates = [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                            9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
                            576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
                            3000000, 3500000, 4000000]
        
        # Variabile di controllo per il menu a tendina
        selected_option = tk.StringVar(current_window)
        selected_option.set("Select baudrate (bits/s)")

        # Creare il menu a tendina
        baudrates_menu = tk.OptionMenu(current_window, selected_option, *allowed_baudrates, command = on_baudrate_select)
        baudrates_menu.pack(pady = 60)
    except:
        create_debug_window(current_window, 'select_baudrate')
        
        
def get_serial_tout(entry):
    user_input = entry.get()
    
    
def select_serial_timeout(current_window):
    try:
        tout_text = Label(current_window, text = 'timeout: ')
        tout_text.place(x = 200, y = 150)
    except:
        create_debug_window(current_window, 'get_serial_timeout')
    