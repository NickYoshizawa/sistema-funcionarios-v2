from utils.process_image import open_image
from customtkinter import *
from tkinter import *
from PIL import Image


class Notebook(CTkFrame):
    def __init__(self, parent, 
        side_bar_vertical: bool = False, 
        header_color: str = None, 
        display_color: str = 'transparent',

        button_highlight_color: str = '#2b4e80', 
        button_color: str = None,
        button_corner_radius: int = None, 
        button_border_width: int = None,
        button_hover_color: str = None,
        button_border_color: str = None,
        
        **kwargs
    ):
        
        self.side_bar_vertical = side_bar_vertical
        self.button_highlight_color = button_highlight_color
        self.button_color = button_color
        self.button_corner_radius = button_corner_radius
        self.button_border_width = button_border_width
        self.button_hover_color = button_hover_color
        self.button_border_color = button_border_color

        self.notebook_frm = CTkFrame(parent, corner_radius=0, fg_color='transparent')
        super().__init__(self.notebook_frm, fg_color=display_color, corner_radius=0) #display
        self.tabs_frm = CTkFrame(self.notebook_frm, fg_color=header_color, corner_radius=0)

    def add(self, 
            frame: any = None, 
            text: str = 'Tab', 
            image: str = None, 
            compound: str = 'left',
            button_height: int = 140,
            button_width: int = 28,
            image_size: tuple = (32, 32),
            padx: tuple | int = None,
            pady: tuple | int = None,
        ):

        img = image
        if image:
            img = Image.open(image)
            img = CTkImage(img, size=image_size)
        button = CTkButton(self.tabs_frm, 
            text=text, 
            image=img, 
            compound=compound,
            command=lambda: self._change_display(frame),
            fg_color=self.button_color,
            width=button_width,
            height=button_height,
            corner_radius=self.button_corner_radius,
            border_color=self.button_border_color,
            hover_color=self.button_hover_color,
            border_width=self.button_border_width
        )


        button.pack(side=TOP if self.side_bar_vertical else LEFT, padx=padx, pady=pady)
        button.bind('<1>', lambda e: self._color_change(e, button))
        self.winfo_children()[0].pack(fill=BOTH, expand=True)
        self.tabs_frm.winfo_children()[0].configure(fg_color=self.button_highlight_color)
    
    def add_logout_button(self, 
        text: str = 'Logout', 
        image: str = None, 
        compound: str = 'left',
        button_height: int = 140,
        button_width: int = 28,
        image_size: tuple = (32, 32),
        padx: tuple | int = None,
        pady: tuple | int = None,
        command: callable = None
    ):
        
        img = image
        if image:
            img = open_image(image, (24, 24))

        button = CTkButton(self.tabs_frm, 
            text=text, 
            image=img, 
            compound=compound,
            command=command,
            fg_color=self.button_color,
            width=button_width,
            height=button_height,
            corner_radius=self.button_corner_radius,
            border_color=self.button_border_color,
            hover_color=self.button_hover_color,
            border_width=self.button_border_width
        )

        button.pack(side=BOTTOM if self.side_bar_vertical else RIGHT, padx=padx, pady=pady,)


    def _change_display(self, frame):
        for widgets in self.winfo_children():
            widgets.pack_forget()
        frame.pack(fill=BOTH, expand=True)
    
    def _color_change(self, event, button):
        for widget in self.tabs_frm.winfo_children():
            widget.configure(fg_color = self.button_color)
        button.configure(fg_color = self.button_highlight_color)

    def pack(self, **kwargs):
        if self.side_bar_vertical:
            self.tabs_frm.pack(fill=Y, side=LEFT)
        else:
            self.tabs_frm.pack(fill=X, side=TOP)
        super().pack(expand=True, fill=BOTH)
        self.notebook_frm.pack(**kwargs)
