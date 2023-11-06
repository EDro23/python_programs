# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:55:37 2023

@author: ethan.drover
"""
output_example_handle = open("movies.txt",'w')
def command_menu():
    print("Comand Menu")
    print("List - List All Movies")
    print("Add - Add A Movie")
    print("Del - Delete A Movie")
    print("Exit - Exit The Program\n")

def list_movies(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print("{}.{} ({})".format(i, movie[0], movie[1]))
    print()
def add_movie(movie_list):
    movie = input("Which Movie Would You Like To Add?  ")
    year = input("Year: ")
    movie_list.append([movie,year])
    print("{} was added. \n".format(movie))
def del_movie(movie_list):
    number = int(input("Number:  "))
    if number <1 or number > len(movie_list):
        print("Invalid Selection \n")
    else:
        movie = movie_list.pop(number-1)
        print("{} was deleted.".format(movie[0]))

            
def main():
    movie_list = [["Monty Python & The Holy Grail", 1975],["On The Waterfront", 1954],[ "Cat on a Hot Tin Roof", 1958]]
    command_menu()
    while True:
        command = input("Command:  ")
        if command.lower == 'list':
            list_movies(movie_list)
        elif command.lower == 'add':
            add_movie(movie_list)
            with open("first_file.txt", 'w') as outfile_handle:
                outfile_handle.write("This is the second file operation\n")
        elif command.lower == 'del':
            del_movie(movie_list)
        elif command.lower == 'exit':
            print("Bye!")
        else:
            print("Invalid command. \n")
    print("Bye!")

if __name__ == '__main__':
    main()