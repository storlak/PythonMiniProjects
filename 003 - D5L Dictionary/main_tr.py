import tkinter
import gui_utils
import menu_utils
from PyMultiDictionary import MultiDictionary
from tkinter import messagebox
from tkinter import ttk
from constants import *

dictionary = MultiDictionary()
selected_language = None  # Initialize selected_language to None initially


# functions for the buttons
def meaning_en():
    search_word(meaning_entry.get(), "meaning")


def synonyms_en():
    search_word(synonym_entry.get(), "synonyms")


def antonyms_en():
    search_word(antonym_entry.get(), "antonyms")


def search_word(word, search_type):
    if not word:
        gui_utils.show_warning_message("Warning", "Please enter a word.")
        return

    global selected_language
    if search_type == "meaning":
        result = dictionary.meaning(selected_language, word)
    elif search_type == "synonyms":
        result = dictionary.synonym(selected_language, word)
    elif search_type == "antonyms":
        result = dictionary.antonym(selected_language, word)

    if result:
        if isinstance(result, list):
            result_text.set(f"{search_type.capitalize()}: {', '.join(result)}")
        else:
            result_text.set(f"{search_type.capitalize()}: {result}")
    else:
        result_text.set(f"No {search_type} found for '{word}'")


def clear():
    meaning_entry.delete(0, "end")
    synonym_entry.delete(0, "end")
    antonym_entry.delete(0, "end")
    result_text.set("")


def language_selection(language):
    global selected_language
    selected_language = language


# functions and menu utils
# opens the README file in github
def open_readme():
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/PythonMiniProjects/blob/main/003%20-%20Dictionary/README.md"
    )


# opens the project in github
def welcome():
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/PythonMiniProjects/tree/main/003%20-%20Dictionary"
    )


# opens the license file in github
def open_license():
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/PythonMiniProjects/blob/main/LICENSE"
    )


# pops up about message
def about():
    current_date = "09.05.2024"
    menu_utils.show_info_message(
        "About",
        f"{APP_NAME}\nVersion: {APP_VERSION}\nAuthor: {AUTHOR}\nLast Update: {current_date}",
    )


def shortcuts():
    menu_utils.show_info_message(
        "Keyboard Shortcuts",
        f"{KEYBOARD_SHORTCUTS}:\nSearch Meaning:  {MEANING}\nSearch Synonym: {SYNONYM}\nSearch Antonym: {ANTONYM}\nCopy Search: {COPY}\nClear: {CLEAR}\nHelp: {HELP}",
    )


def help():
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/PythonMiniProjects/discussions"
    )


# copy the result text to clipboard
def copy_result():
    result = result_text.get()
    window.clipboard_clear()  # Clear the clipboard
    window.clipboard_append(result)  # Append the result text to clipboard


# main window & frame
window = tkinter.Tk()
window.title("D5L Dictionary")
frame = tkinter.Frame(window)
frame.pack()

# Menu bar
menubar = tkinter.Menu(window)
window.config(menu=menubar)

# File menu
file_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=window.quit)

# Edit menu
edit_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Search Meaning", command=meaning_en, accelerator="Alt+M")
edit_menu.add_command(label="Search Synonym", command=synonyms_en, accelerator="Alt+S")
edit_menu.add_command(label="Search Antonym", command=antonyms_en, accelerator="Alt+A")
edit_menu.add_separator()
edit_menu.add_command(label="Copy Search", command=copy_result, accelerator="Alt+C")
edit_menu.add_command(label="Clear", command=clear, accelerator="Alt+L")

# Bind keyboard shortcuts to menu items
window.bind_all("<Alt-m>", lambda event: meaning_en())
window.bind_all("<Alt-s>", lambda event: synonyms_en())
window.bind_all("<Alt-a>", lambda event: antonyms_en())
window.bind_all("<Alt-c>", lambda event: copy_result())
window.bind_all("<Alt-l>", lambda event: clear())

# Tools menu
tools_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Quick Commands", command=shortcuts)
tools_menu.add_separator()
tools_menu.add_command(label="Switch to English")
tools_menu.add_command(label="Türkçe Arayüz")
tools_menu.add_command(label="Interface française")
tools_menu.add_command(label="中文界面")
tools_menu.add_command(label="Русский интерфейс")

# Help menu
help_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Welcome", command=welcome)
help_menu.add_command(label="Documentation", command=open_readme)
help_menu.add_separator()
help_menu.add_command(label="Help", command=help, accelerator="F1")
help_menu.add_command(label="View Licence", command=open_license)
help_menu.add_separator()
help_menu.add_command(label="About D5L", command=about)

window.bind_all("<F1>", lambda event: help())


# search frame
search_frame = tkinter.LabelFrame(frame, text="Search any word for:")
search_frame.grid(row=0, column=0, padx=20, pady=10)

meaning_title_label = tkinter.Label(search_frame, text="Meaning")
meaning_title_label.grid(row=0, column=0)

synonym_title_label = tkinter.Label(search_frame, text="Synonym")
synonym_title_label.grid(row=0, column=1)

antonym_title_label = tkinter.Label(search_frame, text="Antonym")
antonym_title_label.grid(row=0, column=2)

meaning_entry = tkinter.Entry(search_frame)
meaning_entry.grid(row=1, column=0)
meaning_entry.bind(
    "<Return>", lambda event: meaning_en()
)  # Bind Return key to meaning_en

synonym_entry = tkinter.Entry(search_frame)
synonym_entry.grid(row=1, column=1)
synonym_entry.bind(
    "<Return>", lambda event: synonyms_en()
)  # Bind Return key to synonyms_en

antonym_entry = tkinter.Entry(search_frame)
antonym_entry.grid(row=1, column=2)
antonym_entry.bind(
    "<Return>", lambda event: antonyms_en()
)  # Bind Return key to antonyms_en

meaning_search_button = tkinter.Button(search_frame, text="Search", command=meaning_en)
meaning_search_button.grid(row=2, column=0)

synonym_search_button = tkinter.Button(search_frame, text="Search", command=synonyms_en)
synonym_search_button.grid(row=2, column=1)

antonym_search_button = tkinter.Button(search_frame, text="Search", command=antonyms_en)
antonym_search_button.grid(row=2, column=2)

# adjusting grid for all grids
for widget in search_frame.winfo_children():
    widget.grid_configure(
        padx=10, pady=5, sticky="nsew"
    )  # Make widgets sticky to all sides

# frame to display search results
result_frame = tkinter.Frame(
    frame, bg=search_frame["bg"], highlightbackground="white", highlightthickness=1
)  # Use the same background color
result_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

result_text = tkinter.StringVar()
result_label = tkinter.Label(
    result_frame, textvariable=result_text, fg="#FFFFFF", bg="gray16", wraplength=280
)
result_label.pack(expand=True, fill="both")  # Expand to fill the available space

# clear button & copy result button
button = tkinter.Button(frame, text="Clear", bg="red", fg="white", command=clear)
button.grid(row=2, sticky="news", column=0, padx=20, pady=5)

copy_button = tkinter.Button(
    frame, text="Copy Search Result", bg="gray16", fg="white", command=copy_result
)
copy_button.grid(row=3, column=0, sticky="news", padx=20, pady=5)

# radio buttons for language selection
language_frame = tkinter.LabelFrame(
    frame,
    text="Select a language:",
)
language_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

# radio buttons for language selection
language_button = tkinter.Radiobutton(
    language_frame, text="English", value="en", command=lambda: language_selection("en")
)
language_button.grid(row=4, column=0)

language_button1 = tkinter.Radiobutton(
    language_frame, text="Türkçe", value="tr", command=lambda: language_selection("tr")
)
language_button1.grid(row=4, column=1)

language_button2 = tkinter.Radiobutton(
    language_frame,
    text="Français",
    value="fr",
    command=lambda: language_selection("fr"),
)
language_button2.grid(row=4, column=2)

language_button3 = tkinter.Radiobutton(
    language_frame, text="中国人", value="zh", command=lambda: language_selection("zh")
)
language_button3.grid(row=4, column=3)

language_button4 = tkinter.Radiobutton(
    language_frame, text="Русский", value="ru", command=lambda: language_selection("ru")
)
language_button4.grid(row=4, column=4)

# set English radio button as default
language_button.select()
selected_language = "en"

# adjusting grid for all grids
for widget in language_frame.winfo_children():
    widget.grid_configure(
        padx=10, pady=5, sticky="nsew"
    )  # Make widgets sticky to all sides

window.mainloop()
