import tkinter
from tkinter import ttk
from tkinter import messagebox


def enter_data():
    pass


# main window & frame
window = tkinter.Tk()
window.title("English Dictionary")
frame = tkinter.Frame(window)
frame.pack()

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

synonym_entry = tkinter.Entry(search_frame)
synonym_entry.grid(row=1, column=1)

antonym_entry = tkinter.Entry(search_frame)
antonym_entry.grid(row=1, column=2)

meaning_search_button = tkinter.Button(search_frame, text="Search")
meaning_search_button.grid(row=2, column=0)

synonym_search_buttnon = tkinter.Button(search_frame, text="Search")
synonym_search_buttnon.grid(row=2, column=1)

antonym_search_button = tkinter.Button(search_frame, text="Search")
antonym_search_button.grid(row=2, column=2)


# adjusting grid for all grids
for widget in search_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# results frame
courses_frame = tkinter.LabelFrame(frame, text="Your results:")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registred_label = tkinter.Label(courses_frame, text="Registration Status")
# checkbutton value storing
reg_status_var = tkinter.StringVar(value="Not Registered")  # to store checkbutton value
registred_check = tkinter.Checkbutton(
    courses_frame,
    text="Currently Registred",
    variable=reg_status_var,
    onvalue="Registered",
    offvalue="Not Registered",
)

registred_label.grid(row=0, column=0)
registred_check.grid(row=1, column=0)

num_courses_label = tkinter.Label(courses_frame, text="Completed courses")
num_courses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")

num_courses_label.grid(row=0, column=1)
num_courses_spinbox.grid(row=1, column=1)

num_semestres_label = tkinter.Label(courses_frame, text="# Semesters")
num_semestres_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")

num_semestres_label.grid(row=0, column=2)
num_semestres_spinbox.grid(row=1, column=2)

# adjusting grid for all grids
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(
    terms_frame,
    text="I accept the terms and conditions",
    variable=accept_var,
    onvalue="Accepted",
    offvalue="Not Accepted",
)
terms_check.grid(row=0, column=0)

# Add Button
button = tkinter.Button(
    frame, text="Enter data", bg="red", fg="white", command=enter_data
)
button.grid(row=3, sticky="news", column=0, padx=20, pady=10)

window.mainloop()
