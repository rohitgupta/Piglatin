#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:00:26 2018

@author: rohit
"""

"""
 Pig Latin

A 1947 newspaper question and answer column describes the pig Latin as we understand it today. It describes moving the first letter to the end of a word and then adding "ay".
Word that begin with 'Consonent ' Sound , all letter before the initial vowel are placed at the end of vowel sequence and then 'ay' is added to it.
Eg: latin = atinlay
banana = ananabay

words that begin with vowel sounds one just adds "way" or "yay" to the end (or just "ay")
eat = eatay or eatway or eatyay

Pig Latin Awareness Month is the month of September.
Pig Latin Day is September 15.

"""
pyg = 'ay'
original = input('Enter a Word:')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first == ('a'or 'e'or'i'or'o'or'u'):
        new_word = word + pyg
        print (new_word)
    else:
        new_word = word[1:] + first + pyg
        print (new_word)
else:
    print ('empty')