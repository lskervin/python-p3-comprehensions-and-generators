#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [item for item in num_list if item % 2 == 0]
    return even_list

def make_exclamation(sentence_list):
    exclamation_list = [f'{item}!' for item in sentence_list if len(item) > 0]
    return exclamation_list