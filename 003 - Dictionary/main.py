from PyMultiDictionary import MultiDictionary
import tkinter
from tkinter import ttk
import menu_utils
from constants import *

dictionary = MultiDictionary()


# Function to search for the meaning of a word in English
def search_en():
    word = word_entry.get()
    if word:
        # Get meaning
        meaning = dictionary.meaning("en", word)
        # Get synonyms
        synonyms = dictionary.synonym("en", word)
        # Display meaning and synonyms
        result_text.set(f"Meaning: {meaning}\nSynonyms: {', '.join(synonyms)}")


# Functions and menu utils
# Opens the README in Github
def open_readme():
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/PythonMiniProjects/blob/main/003%20-%20Dictionary/README.md"
    )


# Opens the License file in Github
def open_license():
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/PythonMiniProjects/blob/main/LICENSE"
    )


def about():
    current_date = "26.03.2024"
    menu_utils.show_info_message(
        "About",
        f"{APP_NAME}\nVersion: {APP_VERSION}\nAuthor: {AUTHOR}\nLast Update: {current_date}",
    )


# GUI
root = tkinter.Tk()
root.title("Dictionary")
root.geometry("400x350")
root.configure(bg="gray16")

# Menu bar
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
help_menu.add_command(label="Welcome", command=about)
help_menu.add_command(label="Documentation", command=open_readme)
help_menu.add_separator()
help_menu.add_command(label="View Licence", command=open_license)
help_menu.add_separator()
help_menu.add_command(label="About", command=about)

# Labels, entries, widgets
word_label = tkinter.Label(
    root, text="English to English Dictionary", fg="#FFFFFF", bg="gray16"
)
word_entry = tkinter.Entry(root, width=30)
meaning_button = tkinter.Button(
    root, text="Meaning", fg="black", bg="Turquoise", command=search_en
)
separator = ttk.Separator(root, orient="horizontal")  # Separator widget
bot_label = tkinter.Label(
    root, text=f"Version: {APP_VERSION} - {AUTHOR}", fg="black", bg="Turquoise"
)

# Frame to display search results
result_frame = tkinter.Frame(root, bg="gray16")
result_text = tkinter.StringVar()
result_label = tkinter.Label(
    result_frame, textvariable=result_text, fg="#FFFFFF", bg="gray16", wraplength=280
)
result_text1 = tkinter.Label(
    result_frame, text="Search Results", fg="white", bg="gray16"
)

# Placing widgets, labels, entries
word_label.pack(pady=5)
word_entry.pack()
meaning_button.pack(pady=5)
separator.pack(fill="x", pady=5)  # Packing separator after search button
result_frame.pack(pady=5, expand=True, anchor="n")
result_text1.pack()
result_label.pack()
bot_label.pack(side="bottom", fill="x")

root.mainloop()
