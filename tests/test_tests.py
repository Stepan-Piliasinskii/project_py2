from utils import validate_word

def test_validate_word_true():
    assert validate_word("Hello") == True
    assert validate_word("abc") == True
    assert validate_word("hello1") == False
    assert validate_word("hi!") == False