# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 08:50:04 2023

@author: ethan.drover
"""

items = ['wooden staff','wizard hat','cloth shoes']

def title():
    print("The Wizard Inventory Program")

def menu_options():
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop item")
    print ("exit - Exit program")


def show(items):
    for num,item in enumerate(items, start=1):

        print(f"{num}. {item}")


def grab_item(items):
    if len(items) >= 4:
        print("You can't carry anymore items. Drop something first.\n")
    else:
        item = input("Name: ")
        items.append(item)
        print(f"{item} Was added.")

def edit_item(items):
    number = int(input("Number: "))
    if number < 1 or number > len(items):
        print("Invalid item number")
    else:
        item = input("Updated name: ")
        items[number-1] = item
        print(f"Item number {number} was updated.\n")

def drop_item(items):
    number = int(input("Number: "))
    if number < 1 or number > len(items):
        print("Invalid item number")
        
    else:
        item = items.pop(number-1)
        print(f"{item} Was added")
def main():
    title()
    menu_options()
    
    wizard_inv = ['wooden staff','wizard hat','cloth shoes']
    
    while True:
        task = input("Command: ")
        if task == 'show'.lower():
            show(wizard_inv)
        elif task == 'grab'.lower():
            grab_item(wizard_inv)
        elif task == 'edit'.lower():
            edit_item(wizard_inv)
        elif task == 'drop'.lower():
            drop_item(wizard_inv)
        elif task == 'exit'.lower():
            break
        else:
            print("Not a valid command. Please try again.\n")
        print("Bye!")
    
if __name__ == '__main__':
    main()

