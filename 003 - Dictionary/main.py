import gui_utils
import menu_utils
import tkinter
from constants import *
from PyMultiDictionary import MultiDictionary
from tkinter import messagebox
from tkinter import ttk

dictionary = MultiDictionary()


# functions for the buttons
def meaning_en():
    word = meaning_entry.get()
    if not word:
        gui_utils.show_warning_message("Warning", "Please enter a word.")
        return
    # Get meaning
    meaning = dictionary.meaning("en", word)
    # Display meaning
    result_text.set(f"Meaning: {meaning}")


def synonyms_en():
    word = synonym_entry.get()
    if not word:
        gui_utils.show_warning_message("Warning", "Please enter a word.")
        return
    # Get synonyms
    synonyms = dictionary.synonym("en", word)
    # Display synonyms
    result_text.set(f"Synonyms: {', '.join(synonyms)}")


def antonyms_en():
    word = antonym_entry.get()
    if not word:
        gui_utils.show_warning_message("Warning", "Please enter a word.")
        return
    # Get antonyms
    antonyms = dictionary.antonym("en", word)
    # Display antonyms
    result_text.set(f"Antonyms: {', '.join(antonyms)}")


def clear():
    meaning_entry.delete(0, "end")
    synonym_entry.delete(0, "end")
    antonym_entry.delete(0, "end")
    result_text.set("")


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


# main window & frame
window = tkinter.Tk()
window.title("English Dictionary")
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
edit_menu.add_command(label="Meaning", command=meaning_en)
edit_menu.add_command(label="Synonym", command=synonyms_en)
edit_menu.add_command(label="Antonym", command=antonyms_en)
edit_menu.add_separator()
edit_menu.add_command(label="Clear", command=clear)

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

# Clear Button
button = tkinter.Button(frame, text="Clear", bg="red", fg="white", command=clear)
button.grid(row=2, sticky="news", column=0, padx=20, pady=10)

window.mainloop()
