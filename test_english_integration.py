#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:33:50 2021

@author: sanvritti
"""
from tkinter import *
from chatterbot import ChatBot
import Chatbot_GUI as gui

translator = Translator()

#dwight = ChatBot('dwight', only_read=True, database_uri='sqlite:///dwight.db')
#bot = dwight

bot= gui.bot

chatbot = gui.ChatApplication()
translateT = False
language = "EN"

def _change_language():                          #False is for english               
        global translateT
        global language                          #True is to change to Dutch
        if translateT == True:
            chatbot.trans_button.config(text="NL")
            translateT = False
            language = "NL"
        else:
            chatbot.trans_button.config(text="EN")
            translateT = True
            language = "EN"
        

def test_change_language():
    global translateT
    global language
    chatbot._change_language(None) 
    assert translateT == True
    assert language == "EN"
    return

def _insert_message(msg, bot):
    global translateT
    if not msg:
        return
    msg2 = ""
    if translateT:
        en_msg = gui.nl_to_en(msg)
        en_response = bot.get_response(en_msg).text
        nl_response = gui.en_to_nl(en_response)
        msg2 = bot.name + ": " + nl_response + "\n\n"
        
    else:
        msg2 = bot.name + ": " + bot.get_response(msg).text + "\n\n"
    return msg2

def test_insert_message():
    msg2= _insert_message(msg, bot)
    if msg2.dest == 'en':
            print("Test: Success")
    else:
        print("Test failed")
