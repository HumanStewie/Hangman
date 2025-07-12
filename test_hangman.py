from hangman import Hangman
import hangman
import pytest
import json

def test_get_word_meaning():
    with open("filtered.json", "r") as dic:
        dictionary = json.load(dic)
    assert hangman.get_word_meaning("assert") == dictionary["ASSERT"]["MEANINGS"][0]
    
    with pytest.raises(IndexError):
        assert hangman.get_word_meaning("developments")

def test_get_word_synonym():
    with open("filtered.json", "r") as dic:
        dictionary = json.load(dic)
    assert hangman.get_word_synonym("assert") == dictionary["ASSERT"]["SYNONYMS"]


def test_get_random_word():
    with open("filtered.json", "r") as dic:
        dictionary = json.load(dic)
    fallback = ["python", "hangman", "development", "artificial", "security", "logic", "algorithm", "program", "game", "technology", "intelligence", "data", "collection", "steam", "story", "difficult", "basic"]

    random_word = hangman.get_random_word()

    assert random_word.upper() in dictionary
    
    assert hangman.get_random_word() in fallback

def test_get_letter_position():
    x = [(0, "a"), (1, "s"), (2, "s"), (3, "e"), (4, "r"), (5, "t")]
    y = ["a", "s", "s", "e", "r", "t"]
    assert hangman.get_letter_position("assert") == (x, y)
