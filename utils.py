def is_valid_word(word: str) -> bool:
    return all(
        ("a" <= ch <= "z") or ("A" <= ch <= "Z")
        for ch in word
    )


def normalize_word(word: str) -> str:
    return word.strip().lower()