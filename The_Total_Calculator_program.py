# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:55:23 2023

@author: ethan.drover
"""

price = 0
quantity = 0

def title():
    print("The Total Calculator program")
    print()
 
    

def enter_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")



def enter_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")



def main():
    title()
    price = enter_price()
    quantity = enter_quantity()
    total = price * quantity
    print()
    print(f"PRICE:    {price}")
    print(f"QUANTITY: {quantity}")
    print(f"TOTAL:    {total}")

if __name__ == '__main__':
    main()
        
        
    