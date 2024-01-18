import tkinter as tk
from tkinter import ttk, PhotoImage
import serial
import sys
import glob

# This file was generated by the Tkinter Designer
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent

ICON_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\icon")
COVER_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\cover")
MANUAL_PANEL_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\manual\panel")
MANUAL_TEST_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\manual\test")
AUTOMATIC_PANEL_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\automatic\panel")
AUTOMATIC_TEST_PATH = OUTPUT_PATH / Path(r"C:\Users\ITDOSPA\Desktop\NumatoMgr\images\automatic\test")

    
def clear_current_window(current_window):    
    for widget in current_window.winfo_children():
        widget.destroy()

    
def create_debug_window(current_window, msg):
    pass


def get_icon_path(path: str) -> Path:
    return ICON_PATH / Path(path)


def get_cover_path(path: str) -> Path:
    return COVER_PATH / Path(path)


def get_panel_path(type, path: str) -> Path:
    if type == 'manual':
        return MANUAL_PANEL_PATH / Path(path)
    else:
        return AUTOMATIC_PANEL_PATH / Path(path)


def get_test_path(type, path: str) -> Path:
    if type == 'manual':
        return MANUAL_TEST_PATH / Path(path)
    else:
        return AUTOMATIC_TEST_PATH / Path(path)


# SERIAL COM
def beautify_result(list_in):
    list_out = []
    match len(max(list_in, key = len)):
        case 4:
            for elem in list_in:
                list_out.append("       " + elem + "        ")            
        case 5:
            for elem in list_in:
                list_out.append("     " + elem + "        ")            
        case 6:
            for elem in list_in:
                list_out.append("    " + elem + "       ")            
        
    return list_out
        

    
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
        
    beauty_res = beautify_result(result)
    return beauty_res


def on_com_select(com_var, *args):
    selected_value = com_var.get()
    print(f"Selected COM: {selected_value}")


# Baudrate
def get_baudrate_list():
    return ["   2400 bps  ", "   4800 bps  ", "   9600 bps  ", "   19200 bps  ", "   38400 bps  ", "   57600 bps  ", "   115200 bps  ", "   230400 bps  ", "   460800 bps  ", "   500000 bps  ", "   576000 bps  ", "   921600 bps  ", "  1000000 bps  "]


def on_baudrate_select(baudrate_var, *args):
    selected_value = baudrate_var.get()
    print(f"Selected baudrate: {selected_value}")


'''            
def get_serial_tout(entry):
    user_input = entry.get()
    
    
def select_serial_timeout(current_window):
    try:
        tout_text = Label(current_window, text = 'timeout: ')
        tout_text.place(x = 200, y = 150)
    except:
        create_debug_window(current_window, 'get_serial_timeout')
'''    