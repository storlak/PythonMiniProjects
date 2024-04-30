from PyMultiDictionary import MultiDictionary
import tkinter
import menu_utils

dictionary = MultiDictionary()


# enter a word in english for meaning
def search_en(word):
    input("Enter a word: ")
    print(dictionary.meaning("en", word))


# gui
root = tkinter.Tk()
root.title("Dictionary")
root.geometry("300x275")
root.configure(bg="gray16")

# menu bar
menubar = tkinter.Menu(root)
root.config(menu=menubar)

# File menu
file_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

# Tools menu
tools_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=tools_menu)

# Help menu
help_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)

# Labels, entries, widgets
word_label = tkinter.Label(root, text="Word in English", fg="#FFFFFF", bg="gray16")
word_entry = tkinter.Entry(root, width=30)
search_button = tkinter.Button(
    root, text="Search", fg="black", bg="Turquoise", command=search_en
)

# Placing widgets, labels, entries
word_label.pack(pady=5)
word_entry.pack()
search_button.pack(pady=5)

root.mainloop()
