# This program builds a desktop program to hold book data for a fictional book store using Tkinter

from tkinter import *

# Tkinter boilerplate to create gui
window = Tk()

# Housekeeping variable creation
title_entry_value = StringVar()
year_entry_value = StringVar()
author_entry_value = StringVar()
isbn_entry_value = StringVar()

def gui_component_creation():

    # This function creates all the components in the GUI

    # Creates all the labels
    title_label = create_label_or_button(Label, "Title", 0, 0)
    year_label = create_label_or_button(Label, "Year", 1, 0)
    author_label = create_label_or_button(Label, "Author", 0, 2)
    isbn_label = create_label_or_button(Label, "ISBN", 1, 2)

    # Creates all the entry fields
    title_entry = create_entry_fields(title_entry_value, 0, 1)
    year_entry = create_entry_fields(year_entry_value, 1, 1)
    author_entry = create_entry_fields(author_entry_value, 0, 3)
    isbn_entry = create_entry_fields(isbn_entry_value, 1, 3)

    # Creates buttons for all the functions
    view_all_button = create_label_or_button(Button, "View All", 2, 3)
    search_entry_button = create_label_or_button(Button, "Search Entry", 3, 3)
    add_entry_button = create_label_or_button(Button, "Add Entry", 4, 3)
    update_selected_button = create_label_or_button(Button, "Update Selected", 5, 3)
    delete_selected_button = create_label_or_button(Button, "Delete Selected", 6, 3)
    close_button = create_label_or_button(Button, "Close", 7, 3)

def create_label_or_button(function, component_text, row_num, col_num):

    # This function creates the labels for the user interface
    created_component = function(window, text = component_text, width = 15)
    created_component.grid(row = row_num, column = col_num)
    return created_component

def create_entry_fields(text_variable, row_num, col_num):

    # This function creates the text entry fields where users can enter data
    created_entry = Entry(window, textvariable = text_variable)
    created_entry.grid(row = row_num, column = col_num)
    return created_entry

# Creates all window components
gui_component_creation()

# Gives label columns a bit of padding for the sake of a cleaner UI
window.columnconfigure(0, weight = 1)
window.columnconfigure(2, weight = 1)

# Tkinter boilerplate to run gui
window.mainloop()