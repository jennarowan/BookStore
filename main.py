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

    # Creates textbox to display info on all books
    book_info_textbox = create_textbox(8, 40, 3, 5, 0, 3)

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

def create_textbox(height_num, width_num, row_num, row_span_num, col_num, col_span_num):

    # This function creates a textbox to display information
    created_textbox = Text(window, height = height_num, width = width_num)
    created_textbox.grid(row = row_num, rowspan = row_span_num, column = col_num, columnspan = col_span_num)
    return created_textbox

# Displays title at the top of the window and taskbar, book icon in taskbar
window.title("Book Store App")
window_photo = PhotoImage(file = "book.png")
window.iconphoto(False, window_photo)

# Creates all window components
gui_component_creation()

# Tkinter boilerplate to run gui
window.mainloop()