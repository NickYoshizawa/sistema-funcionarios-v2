import customtkinter as ctk
import tkinter.messagebox as mb
from  utils.layout import *
from components.DefaultButton import DefaultButton
from components.LabelEntry import LabelEntry
from components.SearchField import SearchField
from config.theme import COLOR_BACKGROUND, WINDOW_ICON

class MainScreen(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master=master, fg_color=COLOR_BACKGROUND)
        
        self.search_field = SearchField(self, self.callback_search, width=200) 
        self.search_field.pack()
    
    def callback_search(self):
        print(self.search_field.get())