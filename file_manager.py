DICT_FILE = "data/dictionary.txt"
LOG_FILE = "data/log.txt"


class DictionaryManager:

    def add_to_dictionary(self, eng, es):
        with open(DICT_FILE, "a", encoding="utf-8") as f:
            f.write(f"{eng}:{es}\n")

    def read_dictionary(self):
        try:
            with open(DICT_FILE, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Dictionary empty."

    def clear_dictionary(self):

        open(DICT_FILE, "w", encoding="utf-8").close()

    def get_translation(self, eng: str):
        try:
            target = eng.strip().lower()
            with open(DICT_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or ":" not in line:
                        continue
                    e, s = line.split(":", 1)
                    if e.strip().lower() == target:
                        return s.strip()
        except FileNotFoundError:
            return None

    def read_log(self):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Log empty."

    def clear_log(self):
        open(LOG_FILE, "w", encoding="utf-8").close()


def log_action(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
