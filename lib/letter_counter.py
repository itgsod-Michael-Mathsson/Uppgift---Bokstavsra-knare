__author__ = 'michael.mathsson'

import string

def count_letters(text):
    letters = {}

    for letter in text.lower():
        if letter in string.letters:
            letters[letter] = 0
    for letter in text.lower():
        if letter in string.letters:
            letters[letter] +=1

    print letters
    return letters


count_letters("hello")