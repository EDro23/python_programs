# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:41:27 2023

@author: ethan.drover
"""



def menu():
    print("COMMAND MENU")
    print()
    
def menu_options():
    print("show -    Show book info\nadd -  Add book\
          \nedit -   Edit book\ndel -  Delete book\
              \nexit - \t  Exit program")
             
              

def show(books):
    book = input("Title: ").capitalize()
    if book in books:
        print(f"Title: {book}")
        print(f"Author name: {books[book]['author']}")
        print(f"Publication year: {books[book]['year']}")
    else:
        print(f"Sorry, {book} doesn't exist in the catalog")

def edit_book(books):
    title = input('Title: ').capitalize()
    if title in books:
        books[title]['author'] = input('Author name: ')
        books[title]['year'] = input('Publication year: ')
        print(f"{title} has been modified.")
    else:
        print(f"Sorry, {title} doesn't exist in the catelog.")
def add_book(books):
    title = input("Title: ").capitalize()
    author = input("Author name: ").capitalize()
    year = int(input("Publication year: "))
    books[title] = {'author':author, 'year':year}

def delete_book(books):
    title = input('Title: ').capitalize()
    if title in books:
        books.pop(title)
        print(f"{books} has been deleted.\n")
    else:
        print(f"Sorry, {books} doesn't exist in the catalog.\n")
        
def main():
    books = {'Heart of darkness':{'author':'Joseph conrad','year':1899}}
    
    menu()
    menu_options()
    while True:
        print()
        command = input('Command: ').lower()
        if command == 'show':
            show(books)
        elif command == 'edit':
            edit_book(books)
        elif command == 'add':
            add_book(books)
        elif command == 'del':
            delete_book(books)
        elif command == 'exit':
            print("Bye!")
            break

if __name__ == '__main__':
    main()
        
        
    