import tkinter as tk
from tkinter import ttk
import utilities as ut

def set_frames(curr_window, screen):
    # Pulire la finestra corrente
    ut.clear_current_window(curr_window)
    
    # Creare uno stile per i frame
    style = ttk.Style()
    style.configure("Black.TFrame", background="black")
    style.configure("Blue.TFrame", background="blue")
    
    # Creare un frame nero sulla sinistra
    black_frame = ttk.Frame(curr_window, style="Black.TFrame", width=screen['w'] // 4, height=screen['h'])
    
    # Creare un frame rosso sulla destra
    blue_frame = ttk.Frame(curr_window, style="Blue.TFrame", width=(screen['w'] // 4) * 3, height=screen['h'])

    # Posizionare i frame
    black_frame.pack(side=tk.LEFT)
    blue_frame.pack(side=tk.RIGHT)
    
    
def on_btn_click(curr_window, screen):    
    set_frames(curr_window, screen)
