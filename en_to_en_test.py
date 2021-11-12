# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 20:03:39 2021

@author: Bilal
"""

from googletrans import Translator

translator = Translator()

def en_to_nl(text_input):
    return translator.translate(text_input, src='en', dest='nl')

def en_to_nl_test():
    en_input = ['In reference to your request for information.', 'You will find the directions attached.', 'We’re looking forward to your reply.', 'I’m looking forward to hearing from you.', 'Thank you in advance.', 'We trust to have provided you with sufficient information.', 'Please refer to the attached general terms & conditions.']
    for i in en_input:
        translation = en_to_nl(i)
        if translation.dest == 'nl':
            print("Test: Succes")
        else:
            print("Test: Failed")
            print("Expected: nl     Got: ", translation.dest)

en_to_nl_test()