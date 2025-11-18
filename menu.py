from translator import translate_word
from colorama import Fore, Style, init
from file_manager import (
    add_to_dictionary,
    read_dictionary,
    clear_dictionary,
    read_log,
    clear_log,
    log_action
)


def show_menu():
    while True:
        print(Fore.YELLOW + "\n======== SIMPLE TRANSLATOR ========")
        print(Fore.BLUE + "1. Translate a word")
        print(Fore.BLUE + "2. Add a word to the dictionary")
        print(Fore.BLUE + "3. Show dictionary")
        print(Fore.BLUE + "4. Show log")
        print(Fore.BLUE + "5. Clear dictionary")
        print(Fore.BLUE + "6. Clear log")
        print(Fore.BLUE + "7. Exit")
        print(Fore.YELLOW + "===================================\n")

        choice = input("Choose an option: ")

        if choice == "1":
            word = input("Type word (ENG): \n")
            original, translated = translate_word(word)
            print(Fore.GREEN + f"{original} -> {translated}")
            log_action(f"Translation: {original} -> {translated}")

        elif choice == "2":
            eng = input("ENG: ")
            es = input("ES: ")
            add_to_dictionary(eng, es)
            log_action(f"Added word: {eng}:{es}")

        elif choice == "3":
            print(Fore.YELLOW + "--- Dictionary ---")
            print(read_dictionary())

        elif choice == "4":
            print(Fore.MAGENTA + "--- LOG ---")
            print(read_log())

        elif choice == "5":
            clear_dictionary()
            print("Dictionary cleared")
            log_action("Dictionary cleared")

        elif choice == "6":
            clear_log()
            print("Log cleared")
            log_action("Log cleared")

        elif choice == "7":
            print(Fore.RED + "Exiting...")
            break

        else:
            print(Fore.RED + "Something wrong, try again :)")
