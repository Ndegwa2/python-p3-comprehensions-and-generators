#!/usr/bin/env python3

def return_evens(num_list):
    """
    Returns a list of all even elements from the given list of integers.
    """
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    """
    Takes a list of sentence strings and returns a list of sentence strings
    with exclamation marks added to the end.
    """
    return [sentence + '!' for sentence in sentence_list]
