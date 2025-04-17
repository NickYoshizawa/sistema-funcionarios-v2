from ui.LoginWindow import LoginScreen
import customtkinter as ctk
from config.theme import WINDOW_ICON
from utils.layout import center_window

class App(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("Sistema Funcionários")
        self.minsize(400,300)

        self.iconbitmap(WINDOW_ICON)

        self.after(10, lambda: center_window(self, 600, 500))
        
        self.login_screen = LoginScreen(self)
        self.login_screen.packFrame()
        

if __name__ == "__main__":
    App().mainloop()    
