import customtkinter as ctk

from utils.layout import *

from components.DefaultButton import DefaultButton
from components.LabelEntry import LabelEntry
from components.Notebook import Notebook
from components.SearchField import SearchField

class MainScreen(ctk.CTkFrame):

    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.notebook = Notebook(self, 
            side_bar_vertical=True, 
            button_highlight_color='#3d3751', 
            button_color='gray14',
            button_border_width=0,
            button_border_color='black',
            button_corner_radius=0,
            button_hover_color='#3d3751',
            header_color='gray14')
        
        self.customers_frm = ctk.CTkFrame(self.notebook, corner_radius=0)
        self.schedule_frm = ctk.CTkFrame(self.notebook, corner_radius=0)

        self.notebook.add(self.customers_frm, 
            text='', 
            button_width=56, 
            button_height=56, 
            image_size=(48, 42)
        )

        self.notebook.add(self.schedule_frm, 
            text='', 
            button_width=56, 
            button_height=56, 
            image_size=(42, 42)
        )

        self.notebook.add_logout_button(
            text='', 
            button_width=56, 
            button_height=56, 
            image_size=(25, 25),
            command=self.logout,
            image="assets/imgs/exit.png"
        )
        
        self.notebook.pack(expand=True, fill="both")
        
        
        self.search_field = SearchField(self.customers_frm, self.callback_search, width=300) 
        self.search_field.pack()
        
        butao = DefaultButton(self.customers_frm).pack()
        butao = DefaultButton(self.schedule_frm).pack()
    
    def callback_search(self):
        print(self.search_field.get())
    
    def logout(self):
        from ui.LoginWindow import LoginScreen
        self.destroy()
        LoginScreen(self.master).packFrame()
    
    def packFrame(self):
        self.pack(expand=True, fill="both")