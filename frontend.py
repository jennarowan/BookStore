"""
This program builds a desktop program to hold book data for a fictional book store using Tkinter

Each book will have its Title, Author, Year of Publication, and ISBN stored

A user can view the records, search for an entry, add/update/delete entries, and close the program
"""

from tkinter import *
import backend

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
    title_label = create_label("Title", 0, 0)
    year_label = create_label("Year", 1, 0)
    author_label = create_label("Author", 0, 2)
    isbn_label = create_label("ISBN", 1, 2)

    # Creates all the entry fields
    title_entry = create_entry_fields(title_entry_value, 0, 1)
    author_entry = create_entry_fields(author_entry_value, 0, 3)
    year_entry = create_entry_fields(year_entry_value, 1, 1)    
    isbn_entry = create_entry_fields(isbn_entry_value, 1, 3)

    # Creates buttons for all the functions
    view_all_button = create_button("View All", 2, 3, view_all_command)
    search_entry_button = create_button("Search Entry", 3, 3, search_entry_command)
    add_entry_button = create_button("Add Entry", 4, 3, add_entry_command)
    update_selected_button = create_button("Update Selected", 5, 3, backend.update_entry)
    delete_selected_button = create_button("Delete Selected", 6, 3, backend.delete_entry)
    close_button = create_button("Close", 7, 3)

    # Creates listbox to display info on all books; given global scope to be used in the view_all_command() function
    global book_info_listbox 
    book_info_listbox = create_listbox(8, 40, 3, 5, 0, 2)

    # Creates scrollbar for listbox and assigns it
    book_info_scrollbar = create_scrollbar(3, 6, 2)
    assign_y_scrollbar(book_info_listbox, book_info_scrollbar)

def create_label(component_text, row_num, col_num):

    # This function creates the labels for the user interface
    created_component = Label(window, text = component_text, width = 15)
    created_component.grid(row = row_num, column = col_num)
    return created_component

def create_button(component_text, row_num, col_num, button_command = ""):

    # This function creates the buttons for the user interface
    created_component = Button(window, text = component_text, width = 15, command = button_command)
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

def create_scrollbar(row_num, row_span_num, col_num):

    # This functions creates scrollbars
    created_scrollbar = Scrollbar(window)
    created_scrollbar.grid(row = row_num, rowspan = row_span_num, column = col_num)
    return created_scrollbar

def assign_y_scrollbar(component_to_assign_to, scrollbar_to_assign):

    # This function attaches a scrollbar to another component (such as a listbox or textbox) so that the scrollbar operates the vertical axis of the component
    component_to_assign_to.configure(yscrollcommand = scrollbar_to_assign.set)
    scrollbar_to_assign.configure(command = component_to_assign_to.yview)

def view_all_command():

    # This function fetches all existing records from the database and populates the GUI listbox with the data in conjunction with the view_all() function from backend.py

    # Clears any existing information in listbox
    book_info_listbox.delete(0, END)

    # Each row is placed at the end of the listbox
    for row in backend.view_all():

        book_info_listbox.insert(END, row)

def search_entry_command():

    # This function clears the listbox and repopulates it with the information for the book, author, year, and/or isbn entered by the user, in conjunction with the search_entry() function from backend.py

    # Clears any existing information in listbox
    book_info_listbox.delete(0, END)

    # Each row is placed at the end of the listbox
    for row in backend.search_entry(author_entry_value.get(), title_entry_value.get(), year_entry_value.get(), isbn_entry_value.get()):

        book_info_listbox.insert(END, row)

def add_entry_command():

    # This function grabs all the text entry values and adds them to the database in conjunction with the add_entry() function from backend.py

    backend.add_entry(author_entry_value.get(), title_entry_value.get(), year_entry_value.get(), isbn_entry_value.get())

    # Repopulates listbox to include new book
    view_all_command()

# Displays title at the top of the window and taskbar, book icon in taskbar
window.title("Book Store App")
window_photo = PhotoImage(file = "book.png")
window.iconphoto(False, window_photo)

# Creates all window components
gui_component_creation()

# Tkinter boilerplate to run gui
window.mainloop()