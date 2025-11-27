from translator import Translator
from file_manager import DictionaryManager, log_action
from utils import validate_word
from colorama import Fore
import time


def decorate_menu(func):
    def wrapper(*args, **kwargs):
        banner = (
            "\n" 
            "================ SIMPLE TRANSLATOR ================\n"
            "|  EN -> ES  |  type words, save, and view logs  |\n"
            "==================================================\n"
        )
        print(Fore.YELLOW + banner)
        result = func(*args, **kwargs)
        print(Fore.YELLOW + ("=" * 50) + "\n")
        return result
    return wrapper

@decorate_menu
def menu_iteration(translator: Translator, dictionary_manager: DictionaryManager):
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
        print(Fore.CYAN + "Translating", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.4)
        print()
        saved = dictionary_manager.get_translation(word)
        if saved is not None:
            original, translated = word, saved
        else:
            original, translated = translator.translate(word)
        print(Fore.GREEN + f"{original} -> {translated}")
        log_action(f"Translation: {original} -> {translated}")

    elif choice == "2":
        eng = input("ENG: ").strip()
        es = input("ES: ").strip()
        if not (validate_word(eng) and validate_word(es)):
            print(Fore.RED + "Invalid input. Only letters allowed.")
            return True
        dictionary_manager.add_to_dictionary(eng, es)
        print(Fore.GREEN + "Saved to dictionary.")
        log_action(f"Added word: {eng}:{es}")

    elif choice == "3":
        print(Fore.YELLOW + "--- Dictionary ---")
        print(dictionary_manager.read_dictionary())

    elif choice == "4":
        print(Fore.MAGENTA + "--- LOG ---")
        print(dictionary_manager.read_log())

    elif choice == "5":
        dictionary_manager.clear_dictionary()
        print("Dictionary cleared")
        log_action("Dictionary cleared")

    elif choice == "6":
        dictionary_manager.clear_log()
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
    translator = Translator()
    dictionary_manager = DictionaryManager()
    while menu_iteration(translator, dictionary_manager):
        pass
