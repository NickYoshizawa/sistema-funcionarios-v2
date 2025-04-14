from ui.login_window import LoginScreen


def verify_login(username, password):
    print(username, password)
    return True

LoginScreen(verify_login).mainloop()