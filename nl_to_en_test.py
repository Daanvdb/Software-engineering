# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:04:02 2021

@author: Bilal
"""

from googletrans import Translator

translator = Translator()

def nl_to_en(text_input):
    return translator.translate(text_input, src='nl', dest='en')

def test_nl_to_en():
    nl_input = ['Een andere taal leren kost veel tijd.', 'Ik hou van sport.', 'Hartelijk bedankt voor uw belangstelling om met ons samen te werken.', 'Vriendelijk bedankt voor uw aanvraag.', 'Een routebeschrijving is bijgevoegd.', 'Wij zien uw reactie met belangstelling tegemoet.', 'Je m\'appelle']
    for i in nl_input:
        translation = nl_to_en(1)
        if translation.dest == 'en':
            print("Test: Succes")
        else:
            print("Test: Failed")
            print("Expected: en      Got: ", translation.dest)
            
test_nl_to_en()