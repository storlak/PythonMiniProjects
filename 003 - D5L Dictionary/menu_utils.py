import webbrowser
from tkinter import messagebox


def open_url_in_browser(url):
    webbrowser.open_new(url)


def show_info_message(title, message):
    messagebox.showinfo(title, message)


def open_url_in_browser(url):
    webbrowser.open_new(url)
