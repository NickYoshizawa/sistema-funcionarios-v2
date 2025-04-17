import customtkinter as ctk
from  utils.layout import *
from components.DefaultButton import DefaultButton
from components.LabelEntry import LabelEntry
from components.SearchField import SearchField

class MainScreen(ctk.CTkFrame):

    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.search_field = SearchField(self, self.callback_search, width=200) 
        self.search_field.pack()
    
    def callback_search(self):
        print(self.search_field.get())
    
    def packFrame(self):
        self.pack(expand=True, fill="both")