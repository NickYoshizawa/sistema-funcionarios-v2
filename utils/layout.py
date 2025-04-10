def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    tela_width = window.winfo_screenwidth()
    tela_height = window.winfo_screenheight()
    x = int((tela_width / 2) - (width / 2))
    y = int((tela_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")