import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

# Default settings
DARK_BG = '#4B5267'
TEXT_COLOUR = '#FFFFFF'
BUTTON_COLOUR = '#2E294E'

# Functions
def enter_data():
    # Getting information from form
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    gender = gender_combobox.get()
    registration_status = registration_status_var.get()
    courses_number = courses_number_spinbox.get()
    semesters_number = semesters_number_spinbox.get()

    if first_name and last_name: # Checking if fields are empty
        if not terms_check_var.get(): # Checking if terms were agreed
            messagebox.showerror(title='Error', message='You have not accepted the terms!')
            print('Unsuccessful submit attempt')
        else:
            # Creating SQL table
            connection = sql.connect('data.db')

            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data (first_name TEXT, last_name TEXT, title TEXT, age INT, 
            gender TEXT, registration_status TEXT, courses_number INT, semesters_number INT)'''
            connection.execute(table_create_query)

            # Inserting data to table
            data_insert_query = '''INSERT INTO Student_Data (first_name, last_name, title, age, gender, registration_status, 
            courses_number, semesters_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (first_name, last_name, title, age, gender, registration_status, courses_number, semesters_number)

            cursor = connection.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            connection.commit()

            # Closing connection
            connection.close()

            # Confirmation message box
            messagebox.showinfo(title='Success!', message='The information has been successfully submitted!')
            print('Successful submit attempt')
    else:
        messagebox.showerror(title='Error!', message='First and Last name are required.')
        print('Unsuccessful submit attempt')

# Button cursor changes
def on_enter(event):
    button.config(cursor="hand2")

def on_leave(event):
    button.config(cursor="")

# Window settings
window = tk.Tk()
window.title('SQL Entry Form')
window.iconbitmap('./icon.ico')
window.config(bg=DARK_BG)

# Window arrangement
frame = tk.Frame(window, padx=15, pady=15, bg=DARK_BG)
frame.grid(row=0, column=0)

# Widgets

# Saving user information
user_info = tk.LabelFrame(frame, text='User Information', bg=DARK_BG, fg=TEXT_COLOUR)
user_info.grid(row=0, column=0, padx=10, pady=10, sticky="w")

first_name_label = tk.Label(user_info, text='First Name', bg=DARK_BG, fg=TEXT_COLOUR)
first_name_label.grid(row=0, column=0, padx=5, pady=5)

last_name_label = tk.Label(user_info, text='Last Name', bg=DARK_BG, fg=TEXT_COLOUR)
last_name_label.grid(row=0, column=1, padx=5, pady=5)

first_name_entry = tk.Entry(user_info)
first_name_entry.grid(row=1, column=0, padx=5, pady=5)

last_name_entry = tk.Entry(user_info)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

title_label = tk.Label(user_info, text='Title', bg=DARK_BG, fg=TEXT_COLOUR)
title_label.grid(row=0, column=2, padx=5, pady=5)

title_combobox = ttk.Combobox(user_info, values=['', 'Mr.', 'Ms.', 'Dr.'])
title_combobox.grid(row=1, column=2, padx=5, pady=5)

age_label = tk.Label(user_info, text='Age', bg=DARK_BG, fg=TEXT_COLOUR)
age_label.grid(row=2, column=0, padx=5, pady=5)

age_spinbox = tk.Spinbox(user_info, from_=18, to=120)
age_spinbox.grid(row=3, column=0, padx=5, pady=5)

gender_label = tk.Label(user_info, text='Gender', bg=DARK_BG, fg=TEXT_COLOUR)
gender_label.grid(row=2, column=1, padx=5, pady=5)

gender_combobox = ttk.Combobox(user_info, values=['Male', 'Female', "I'd rather not say"])
gender_combobox.grid(row=3, column=1, padx=5, pady=5)

# Saving courses info
courses_frame = tk.LabelFrame(frame, text='Courses information', bg=DARK_BG, fg=TEXT_COLOUR)
courses_frame.grid(row=1, column=0, padx=10, pady=10, sticky="we")

registered_label = tk.Label(courses_frame, text='Registration Status', bg=DARK_BG, fg=TEXT_COLOUR)
registered_label.grid(row=0, column=0, padx=5, pady=5)

registration_status_var = tk.StringVar()
registered_check = tk.Checkbutton(courses_frame, text='Currently Registered', variable=registration_status_var,
                                  onvalue='Registered', offvalue='Not registered', bg=DARK_BG, fg=TEXT_COLOUR, 
                                  selectcolor=DARK_BG, activeforeground=TEXT_COLOUR)
registered_check.grid(row=1, column=0, padx=5, pady=5)

courses_number_label = tk.Label(courses_frame, text='Completed courses', bg=DARK_BG, fg=TEXT_COLOUR)
courses_number_label.grid(row=0, column=1, padx=5, pady=5)

courses_number_spinbox = tk.Spinbox(courses_frame, from_=0, to=float('inf'))
courses_number_spinbox.grid(row=1, column=1, padx=5, pady=5)

semesters_number_label = tk.Label(courses_frame, text='Semesters', bg=DARK_BG, fg=TEXT_COLOUR)
semesters_number_label.grid(row=0, column=2, padx=5, pady=5)

semesters_number_spinbox = tk.Spinbox(courses_frame, from_=0, to=float('inf'))
semesters_number_spinbox.grid(row=1, column=2, padx=5, pady=5)

# Accept terms
terms_frame = tk.LabelFrame(frame, text='Terms and Conditions', bg=DARK_BG, fg=TEXT_COLOUR)
terms_frame.grid(row=2, column=0, padx=10, pady=10, sticky="we")

terms_check_var = tk.BooleanVar(value=False)
terms_check = tk.Checkbutton(terms_frame, text='I accept all the terms and conditions', variable=terms_check_var,
                             onvalue=True, offvalue=False, bg=DARK_BG, fg=TEXT_COLOUR, selectcolor=DARK_BG, 
                             activeforeground=TEXT_COLOUR)
terms_check.grid(row=0, column=0, padx=5, pady=5)

# Button
button = tk.Button(frame, text='Enter data', command=enter_data, bg= BUTTON_COLOUR, fg= TEXT_COLOUR)
button.grid(row=3, column=0, padx=10, pady=10, sticky="we")

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# App control
window.mainloop()
print('Window closed by user')
