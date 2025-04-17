import customtkinter as ctk
from utils.process_image import open_image
from PIL import Image

class SearchField(ctk.CTkFrame):
    def __init__(self, master, callback_search ,width = 200, height = 35, corner_radius = 8, border_width = 2, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.pack_propagate(False)
        
        self.callback_search = callback_search
        
        self.img_lupa = open_image("assets/imgs/lupa.png", size=(25, 25))
        
        self.entry = ctk.CTkEntry(self, border_width=0, corner_radius=0, fg_color="transparent", placeholder_text="Buscar...")
        self.entry.pack(side="left", fill="both", expand=True, padx=(5,0), pady=5)
        
        self.icon_label = ctk.CTkLabel(self, image=self.img_lupa, text="", cursor="hand2")
        self.icon_label.pack(side="right", padx=(0,5), pady=5)
        
        self.icon_label.bind("<Button-1>", self.on_click)
    
    def on_click(self, event=None):
        self.callback_search()
    
    def get(self):
        return self.entry.get()
    
