import customtkinter as ctk
import tkinter.messagebox as mb
from  utils.layout import *
from components.DefaultButton import DefaultButton
from components.LabelEntry import LabelEntry
from config.theme import COLOR_BACKGROUND, WINDOW_ICON

class MainScreen(ctk.CTk):

    def __init__(self):
        super().__init__(fg_color=COLOR_BACKGROUND)

        self.title("Aplicação")
        self.geometry("500x400")
        self.iconbitmap(WINDOW_ICON)
        
        
        
        self.after(10, lambda: center_window(self)) 