# Title Screen
import os
import main
import sys


def title_screen_selections():
    option = input("> ")

    if option.lower().find("play") != -1:
        main.start_game()
    elif option.lower().find("help") != -1:
        help_menu()
    elif option.lower().find("quit") != -1:
        sys.exit()

    while option.lower().find("play") and option.lower().find("help") and option.lower().find("quit") == -1:

        print("Please enter a valid command.")
        option = input("> ")

        if option.lower().find("play") != -1:
            main.start_game()
        elif option.lower().find("help") != -1 :
            help_menu()
        elif option.lower().find("quit") != -1:
            sys.exit()

def title_screen():
    os.system("cls")
    print("-------------------------")
    print("- Welcome to the Survey -")
    print("-------------------------")
    print("        -  Play  -       ")
    print("        -  Help  -       ")
    print("        -  Quit  -       ")
    title_screen_selections()


def help_menu():
    print("--------------------------------")
    print("- Are you dumb? Just type dawg -")
    print("--------------------------------")
    title_screen_selections()

title_screen()