from ui.login_window import LoginScreen


def verify_login(username, password):
    print(username, password)
    return True

if __name__ == "__main__":
    LoginScreen(verify_login).mainloop()    
