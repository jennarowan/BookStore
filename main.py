# This program builds a desktop program to hold book data for a fictional book store using Tkinter

from tkinter import *

# Tkinter boilerplate to create gui
window = Tk()

# Housekeeping variable creation
title_entry_value = StringVar()
year_entry_value = StringVar()
author_entry_value = StringVar()
isbn_entry_value = StringVar()

def create_labels():

    # This function creates the labels for the user interface
    title_label = Label(window, text = "Title")
    title_label.grid(row = 0, column = 0)

    year_label = Label(window, text = "Year")
    year_label.grid(row = 1, column = 0)

    author_label = Label(window, text = "Author")
    author_label.grid(row = 0, column = 2)

    isbn_label = Label(window, text = "ISBN")
    isbn_label.grid(row = 1, column = 2)

def create_entry_fields():

    # This function creates the text entry fields where users can enter data
    title_entry = Entry(window, textvariable = title_entry_value)
    title_entry.grid(row = 0, column = 1)

    year_entry = Entry(window, textvariable = year_entry_value)
    year_entry.grid(row = 1, column = 1)

    author_entry = Entry(window, textvariable = author_entry_value)
    author_entry.grid(row = 0, column = 3)

    isbn_entry = Entry(window, textvariable = isbn_entry_value)
    isbn_entry.grid(row = 1, column = 3)

def create_buttons():

    # This function creates all the buttons
    view_all_button = Button(window, text = "View All")
    view_all_button.grid(row = 2, column = 3)

    search_entry_button = Button(window, text = "Search Entry")
    search_entry_button.grid(row = 3, column = 3)

    add_entry_button = Button(window, text = "Add Entry")
    add_entry_button.grid(row = 4, column = 3)

    update_selected_button = Button(window, text = "Update Selected")
    update_selected_button.grid(row = 5, column = 3)

    delete_selected_button = Button(window, text = "Delete Selected")
    delete_selected_button.grid(row = 6, column = 3)

    close_button = Button(window, text = "Close")
    close_button.grid(row = 7, column = 3)


# Sets window size
window.geometry("500x500")

# Runs GUI creation functions
create_labels()
create_entry_fields()
create_buttons()

# Gives label columns a bit of padding for the sake of a cleaner UI
window.columnconfigure(0, weight = 1)
window.columnconfigure(2, weight = 1)

# Tkinter boilerplate to create gui
window.mainloop()