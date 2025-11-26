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
from utils import validate_word


def decorate_menu(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        print("💠       SIMPLE TRANSLATOR MENU       💠")
        print("=" * 40)

        result = func(*args, **kwargs)

        print("=" * 40)
        print("💠              END OF MENU             💠")
        print("=" * 40 + "\n")

        return result
    return wrapper


@decorate_menu
def menu_iteration():
    print(Fore.BLUE + "1. Translate a word")
    print(Fore.BLUE + "2. Add a word to the dictionary")
    print(Fore.BLUE + "3. Show dictionary")
    print(Fore.BLUE + "4. Show log")
    print(Fore.BLUE + "5. Clear dictionary")
    print(Fore.BLUE + "6. Clear log")
    print(Fore.BLUE + "7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        word = input("Type word (ENG): ").strip()
        if not validate_word(word):
            print(Fore.RED + "Invalid input. Only letters allowed.")
            return True
        original, translated = translate_word(word)
        print(Fore.GREEN + f"{original} -> {translated}")
        log_action(f"Translation: {original} -> {translated}")

    elif choice == "2":
        eng = input("ENG: ").strip()
        es = input("ES: ").strip()
        if not (validate_word(eng) and validate_word(es)):
            print(Fore.RED + "Invalid input. Only letters allowed.")
            return True
        add_to_dictionary(eng, es)
        print(Fore.GREEN + "Saved to dictionary.")
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
        log_action("Application exited by user.")
        return False

    else:
        print(Fore.RED + "Something wrong, try again :)")

    return True


def show_menu():
    while menu_iteration():
        pass
