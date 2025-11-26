def validate_word(word: str) -> bool:
    return all(
        ("a" <= ch <= "z") or ("A" <= ch <= "Z")
        for ch in word
    )


