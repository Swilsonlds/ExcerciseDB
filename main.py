import employee
import datetime
import sqlite3
from employee import show_all
from employee import add_record
from employee import remove_record
from employee import modify_record

from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

print(Fore.YELLOW + "Welcome to my exercise log application!\n")


continue_running = True
acceptable_answer = ["Y","y","N","n"]

while continue_running:
    while True:
        print(Fore.LIGHTBLUE_EX +"Please select an option listed below")
        print("-------------------------------------")
        print("1. View all activities")
        print("2. Add an activity")
        print("3. Update an entry")
        print("4. Remove an entry")
        print("5. Exit the program")

        try:
            selection = int(input("\nSelection: "))
        except ValueError:
            print(Fore.RED + "You've entered a character that isn't a number. Please enter a number.")
            continue

        if selection > 5 or selection < 0 or type(selection) == "String":
            print(Fore.RED + "The number you've entered is not valid. Please try again.")
        else:
            break

    if selection == 1:
        show_all()
        while True:
            again = input(Fore.LIGHTBLUE_EX + "\nWould you like to perform another action?(Y/N): ")
            if again not in acceptable_answer:
                print(Fore.RED + "Input is invalid, please try again.\n")
            else:
                break

        print("\n")
        if again.upper() == "Y":
            continue_running = True
        else:
            continue_running = False
            print(Fore.YELLOW + "Thanks for using the program. Goodbye!")

    elif selection == 2:
        add_record()
        while True:
            again = input(Fore.LIGHTBLUE_EX +"\nWould you like to perform another action?(Y/N): ")
            if again not in acceptable_answer:
                print(Fore.RED + "Input is invalid, please try again.\n")
            else:
                break

        print("\n")
        if again.upper() == "Y":
            continue_running = True
        else:
            continue_running = False
            print(Fore.YELLOW + "Thanks for using the program. Goodbye!")

    elif selection == 3:
        modify_record()
        while True:
            again = input(Fore.LIGHTBLUE_EX +"\nWould you like to perform another action?(Y/N): ")
            if again not in acceptable_answer:
                print(Fore.RED + "Input is invalid, please try again.\n")
            else:
                break

        print("\n")
        if again.upper() == "Y":
            continue_running = True
        else:
            continue_running = False
            print(Fore.YELLOW + "Thanks for using the program. Goodbye!")

    elif selection == 4:
        remove_record()
        while True:
            again = input(Fore.LIGHTBLUE_EX +"\nWould you like to perform another action?(Y/N): ")
            if again not in acceptable_answer:
                print(Fore.RED + "Input is invalid, please try again.\n")
            else:
                break

        print("\n")
        if again.upper() == "Y":
            continue_running = True
        else:
            continue_running = False
            print(Fore.YELLOW + "Thanks for using the program. Goodbye!")

    elif selection == 5:
        continue_running = False

print(Fore.YELLOW + "\nThanks for using the program. Goodbye!")
