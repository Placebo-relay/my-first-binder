# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 03:37:11 2023

@author: Placebo

Code: grabs text input and counts words on the fly
"""

from ipywidgets import interact, Text


def wid():
    """
    making a nice widget
    """
    interact(process_input, user_input=Text(description="type here"))


def process_input(user_input):
    """
    self-explanatory
    """
    words = []
    longest_words = []
    shortest_words = []
    longest_word_len = 0
    shortest_word_len = float("inf")

    word = ""
    for i, char in enumerate(user_input):
        #isalpha() method: True if a-Z or A-Z
        if char.isalpha():
            word += char
        #not alpha: if ',' - check for indent (ispace() ~ " ")
        #important note: ',' while inside a word appends symbol count
        elif char == ",":
            if i < len(user_input) - 1 and (
                user_input[i + 1].isspace() or user_input[i + 1] == "\t"
            ):
                continue
            word += char
        elif word:
            words.append(word)
            # is new longest?
            if len(word) > longest_word_len:
                longest_words = [word]
                longest_word_len = len(word)
            # is same as longest?
            elif len(word) == longest_word_len:
                longest_words.append(word)
            # is new shortest?
            if len(word) < shortest_word_len:
                shortest_words = [word]
                shortest_word_len = len(word)
            # is same as shortest?
            elif len(word) == shortest_word_len:
                shortest_words.append(word)
            word = ""
    # on-the-fly check block
    if word:
        words.append(word)
        # is new longest?
        if len(word) > longest_word_len:
            longest_words = [word]
            longest_word_len = len(word)
        # is same as longest?
        elif len(word) == longest_word_len:
            longest_words.append(word)
        # is new shortest?
        if len(word) < shortest_word_len:
            shortest_words = [word]
            shortest_word_len = len(word)
        # is same as shortest?
        elif len(word) == shortest_word_len:
            shortest_words.append(word)
    # print block
    print("Words:")
    for word in words:
        print(word)
    print("Total count:", len(words))
    print("Longest words:", longest_words)
    print("Longest word length:", longest_word_len)
    print("Shortest words:", shortest_words)
    print("Shortest word length:", shortest_word_len)
