import customtkinter as ctk
import tkinter.messagebox as mb

from  utils.layout import *
from ui.MainWindow import MainScreen
from models.login_verify import login_verify

from components.DefaultButton import DefaultButton
from components.LabelEntry import LabelEntry



class LoginScreen(ctk.CTkFrame):

    def __init__(self, master, _callback_login: callable = login_verify, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.master = master
        self._callback_login = _callback_login
        
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(expand=True)

        self.user_entry = LabelEntry(self.frame, label_text="User")
        self.user_entry.pack(padx=20, pady=(20, 0))

        self.pw_entry =LabelEntry(self.frame, label_text="Password", show="*")
        self.pw_entry.pack(padx=20)

        button = DefaultButton(self.frame, text="Entrar", command=self.try_login)
        button.pack(pady=20)

    def try_login(self):
        user = self.user_entry.get()
        pw = self.pw_entry.get()

        if self._callback_login(user, pw):
            self.destroy()
            MainScreen(self.master).packFrame()
        else:
            mb.showerror("Erro", "Usuário ou senha inválidos")
    
    def packFrame(self):
        self.pack(expand=True, fill="both")