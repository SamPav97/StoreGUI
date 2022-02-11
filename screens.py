import tkinter as tk
from StoreGUI.auth_service import register, login
from StoreGUI.products_service import get_all_products


def clear_window(window):
    for child in window.winfo_children():
        child.destroy()


def render_products_screen(window):
    clear_window(window)

    products = get_all_products()


def render_login_screen(window):
    clear_window(window)

    tk.Label(window, text='Enter your username: ').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text='Enter your password: ').grid(row=1, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    def on_login():
        username_value = username.get()
        password_value = password.get()

        result = login(username_value, password_value)
        if result:
            render_products_screen(window)
        else:
            tk.Label(window, text="Invalid credentials!", fg='red').grid(row=2, column=1)

    tk.Button(window, text='Login',
              bg='green',
              fg='white',
              command=lambda: on_login()
              ).grid(row=3, column=1)


def render_main_screen(window):
    tk.Button(window, text='Login',
              bg='green',
              fg='white',
              command=lambda: render_login_screen(window)
              ).grid(row=0, column=0)

    tk.Button(window, text='Register',
              bg='yellow',
              fg='black',
              command=lambda: render_register_screen(window)
              ).grid(row=0, column=1)


def render_register_screen(window):
    clear_window(window)

    tk.Label(window, text='Enter your username: ').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text='Enter your email: ').grid(row=1, column=0)
    email = tk.Entry(window)
    email.grid(row=1, column=1)

    tk.Label(window, text='Enter your password: ').grid(row=2, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=2, column=1)

    tk.Label(window, text='Repeat password: ').grid(row=3, column=0)
    confirm_password = tk.Entry(window, show='*')
    confirm_password.grid(row=3, column=1)

    def on_register():
        username_value = username.get()
        email_value = email.get()
        password_value = password.get()
        confirm_password_value = confirm_password.get()

        if password_value != confirm_password_value:
            tk.Label(window, text='Password must match!', fg='red').grid(row=4, column=1)
        else:
            result = register(username_value, email_value, password_value)
            if result:
                render_login_screen(window)
            else:
                tk.Label(window, text='Username is taken!', fg='red').grid(row=4, column=1)

    tk.Button(window, text='Register',
              bg='green',
              fg='black',
              command=on_register
              ).grid(row=5, column=1)