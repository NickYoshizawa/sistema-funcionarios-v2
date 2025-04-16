import customtkinter as ctk
import tkinter.messagebox as mb
from  utils.layout import *
from components.DefaultButton import DefaultButton
from components.LabelEntry import LabelEntry
from config.theme import COLOR_BACKGROUND, WINDOW_ICON
from ui.main_window import MainScreen


class LoginScreen(ctk.CTk):

    def __init__(self, callback_login):
        super().__init__(fg_color=COLOR_BACKGROUND)

        self.callback_login = callback_login

        self.title("Login")
        self.geometry("500x400")
        self.minsize(400,300)
        
        self.iconbitmap(WINDOW_ICON)
        
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(expand=True)

        self.user_entry = LabelEntry(self.frame, label_text="User")
        self.user_entry.pack(padx=20, pady=(20, 0))

        self.pw_entry =LabelEntry(self.frame, label_text="Password", show="*")
        self.pw_entry.pack(padx=20)

        button = DefaultButton(self.frame, text="Entrar", command=self.tentar_login)
        button.pack(pady=20)

        self.after(10, lambda: center_window(self))

    def tentar_login(self):
        user = self.user_entry.get()
        pw = self.pw_entry.get()

        if self.callback_login(user, pw):
            self.after(100, self.destroy)
            MainScreen().mainloop()
            
        else:
            mb.showerror("Erro", "Usuário ou senha inválidos")