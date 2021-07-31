"""
This program builds a desktop program to hold book data for a fictional book store using Tkinter

Each book will have its Title, Author, Year of Publication, and ISBN stored

A user can view the records, search for an entry, add/update/delete entries, and close the program
"""

from tkinter import *

# Tkinter boilerplate to create gui
window = Tk()

# Variables to be used later in creating text entry fields; created here to prevent scope errors
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

    # Creates listbox to display info on all books
    book_info_listbox = create_listbox(8, 40, 3, 5, 0, 2)

    # Creates scrollbar for listbox and assigns it
    book_info_scrollbar = create_scrollbar(3, 2)
    assign_y_scrollbar(book_info_listbox, book_info_scrollbar)

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

def create_listbox(height_num, width_num, row_num, row_span_num, col_num, col_span_num):

    # This function creates a listbox to display information
    created_listbox = Listbox(window, height = height_num, width = width_num)
    created_listbox.grid(row = row_num, rowspan = row_span_num, column = col_num, columnspan = col_span_num)
    return created_listbox

def create_scrollbar(row_num, col_num):

    # This functions creates scrollbars
    created_scrollbar = Scrollbar(window)
    created_scrollbar.grid(row = row_num, column = col_num)
    return created_scrollbar

def assign_y_scrollbar(component_to_assign_to, scrollbar_to_assign):

    # This function attaches a scrollbar to another component (such as a listbox or textbox) so that the scrollbar operates the vertical axis of the component
    component_to_assign_to.configure(yscrollcommand = scrollbar_to_assign.set)
    scrollbar_to_assign.configure(command = component_to_assign_to.yview)

# Displays title at the top of the window and taskbar, book icon in taskbar
window.title("Book Store App")
window_photo = PhotoImage(file = "book.png")
window.iconphoto(False, window_photo)

# Creates all window components
gui_component_creation()

# Tkinter boilerplate to run gui
window.mainloop()