#!/usr/bin/env python3

def return_evens(num_list):
    if (num_list):
        num_list = [num for num in num_list if num % 2 == 0]
        return num_list
    else :
        return num_list   

def make_exclamation(sentence_list):
    if sentence_list:
        modified_sentences = []
        for sentence in sentence_list:
            modified_sentence = sentence + "!"
            modified_sentences.append(modified_sentence)
        return modified_sentences
    else:
        return []

