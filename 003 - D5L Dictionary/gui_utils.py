import tkinter.messagebox


def show_info_message(title, message):
    tkinter.messagebox.showinfo(title, message)


def show_warning_message(title, message):
    tkinter.messagebox.showwarning(title, message)


def show_error_message(title, message):
    tkinter.messagebox.showerror(title, message)
