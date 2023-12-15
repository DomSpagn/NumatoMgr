import tkinter as tk
from tkinter import ttk
import utilities as ut

def set_frames(curr_window, screen):
    # Pulire la finestra corrente
    ut.clear_current_window(curr_window)
    
    # Creare uno stile per i frame
    style = ttk.Style()
    style.configure("Black.TFrame", background="black")
    style.configure("Red.TFrame", background="red")
    
    # Creare un frame nero sulla sinistra
    black_frame = ttk.Frame(curr_window, style="Black.TFrame", width=screen['w'] // 4, height=screen['h'])
    black_label = ttk.Label(black_frame, text="Serial COM Settings", foreground='white')
    black_label.pack(side='top')
    
    # Creare un frame rosso sulla destra
    red_frame = ttk.Frame(curr_window, style="Red.TFrame", width=(screen['w'] // 4) * 3, height=screen['h'])

    # Posizionare i frame
    black_frame.pack(side=tk.LEFT)
    red_frame.pack(side=tk.RIGHT)        
    
    return black_frame


def on_btn_click(curr_window, screen):    
    frame = set_frames(curr_window, screen)
    
    ut.select_COM(frame)
    #ut.select_baudrate(curr_window)
    #ut.select_serial_timeout(curr_window)
