# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:47:32 2023

@author: ethan.drover
"""
countries = {'CA':'Canada',
             'US':'United States',
             'MX':'Mexico'}

def menu_title():
    print("COMMAND MENU")
    print()

def menu_list():
    print("view - View country name\nadd - Add a country")
    print("del - Delete a country\nexit - Exit program\n")

# Viewing

def view_country(countries):
    codes = list(countries.keys())
    codes.sort()
    print_string = "Country codes: "
    for code in codes:
        print_string += code + " "
    print(print_string)

def view_name(countries_dict):
    # view_country(countries_dict)
    code = input("Enter country code: ").upper()
    if code in countries_dict:
        country_name = countries_dict[code]
        print(f"Country name: {country_name}. \n")
    else:
        print("No country with this code exists.\n")


  
# Adding

def adding_country(countries):
    code = input("Enter country code: ")
    if code in countries:
        country_name = countries[code]
        print(f"{country_name} is already using this code.")
    else:
        country_name = input("Enter country_name: ").capitalize()
        countries[code] = country_name
        print(f'{country_name} was added.\n')



# Delete
def deleting_country(countries):
    code = input("Enter country code: ").upper()
    if code in countries:
        country_name = countries.pop(code)
        print(f'{country_name} was deleted.\n')
    else:
        print("There is no country with this code.\n")

def main():
    menu_title()
    menu_list()
    while True:
        command = input("Command: ")
    
        if command == 'view':
            view_country(countries)
            view_name(countries)
        elif command == 'add':
            adding_country(countries)
        elif command == 'del':
            deleting_country(countries)
        elif command == 'exit':
            print("Bye!")
            break
    
if __name__ == '__main__':
    main()
        
        
    
    
