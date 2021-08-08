"""
This file holds all of the backend SQL functions that drive the actual app functionality
"""

import sqlite3

def connect_to_db():

    # This function either connects to an existing database file or creates one if it doesn't exist, with the relevant fields
    db_connection = sqlite3.connect("books.db")
    db_cursor = db_connection.cursor()

    db_cursor.execute("CREATE TABLE IF NOT EXISTS book_list (id_number PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER")

    db_connection.commit()
    db_connection.close()

def add_entry(title, author, year, isbn):

    db_connection = sqlite3.connect("books.db")
    db_cursor = db_connection.cursor()

    db_cursor.execute("INSERT INTO book_list VALUES (NULL,?,?,?,?)",(title, author, year, isbn))

    db_connection.commit()
    db_connection.close()

def view_all():
    
    db_connection = sqlite3.connect("books.db")
    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM book_list")

    rows = db_cursor.fetchall()

    db_connection.close()
    return rows

# Runs when the main frontend file is open to establish the database connection
connect_to_db()