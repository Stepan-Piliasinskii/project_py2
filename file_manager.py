DICT_FILE = "data/dictionary.txt"
LOG_FILE = "data/log.txt"

def add_to_dictionary(eng, es):

    with open(DICT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{eng}:{es}\n")


def read_dictionary():
    try:
        with open(DICT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Dictionary empty."


def clear_dictionary():
    open(DICT_FILE, "w", encoding="utf-8").close()


def read_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Log empty."

def clear_log():
    open(LOG_FILE, "w", encoding="utf-8").close()

def log_action(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")