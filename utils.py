import re


def validate_word(word: str) -> bool:
    return re.fullmatch(r"[A-Za-z]+", word) is not None


