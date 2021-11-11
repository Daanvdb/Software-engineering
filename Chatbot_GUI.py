# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:34:22 2021

@author: btych
"""

from tkinter import *
from googletrans import Translator
from chatterbot import ChatBot
from chat import get_response, bot_name

translator = Translator()

michael = ChatBot('michael', only_read=True, database_uri='sqlite:///michael.db')
dwight = ChatBot('dwight', only_read=True, database_uri='sqlite:///dwight.db')
bot = dwight

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
translateT = False

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


def nl_to_en(text_input):
    return translator.translate(text_input, src='nl', dest='en').text

def en_to_nl(text_input):
    return translator.translate(text_input, src='en', dest='nl').text

class ChatApplication:
    
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()

    def _change_language(self, Event):                                       # _change_language and _change_personality have to be declared before declaring the buttons
        global translateT                                                    # otherwise it might rise an error or get stuck in a loop
        if translateT == True:
            self.trans_button.config(text="NL")
            translateT = False
        else:
            self.trans_button.config(text="EN")
            translateT = True

    def _change_personality(self,Event):
        b = 2
        global bot
        if bot==dwight:
            self.bot_pers.config(text="Dwight")
            bot = michael
        else:
            self.bot_pers.config(text="Michael")
            bot = dwight

        
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=950, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    

        # translate button
        self.trans_button = Button(head_label, text="NL", font=FONT_BOLD, width=4, bg=BG_GRAY,
                             command= lambda: self._change_language(None))
        self.trans_button.place(x=890,y=0)

        #Bot personality
        self.bot_pers = Button(head_label, text="Michael", font=FONT_BOLD, width=6, bg=BG_GRAY,
                             command= lambda: self._change_personality(None))
        self.bot_pers.place(x=800,y=0)
     
    def _on_enter_pressed(self, event):
        global bot
        msg = self.msg_entry.get()
        self._insert_message(msg, "You", bot)
        
    def _insert_message(self, msg, sender, bot):
        if not msg:
            return

    
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        if translate:
            en_msg = nl_to_en(msg)
            en_response = bot.get_response(en_msg).text
            nl_response = en_to_nl(en_response)
            msg2 = bot.name + ": " + nl_response + "\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(state=DISABLED)
        
        else:
            msg2 = bot.name + ": " + bot.get_response(msg).text + "\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
             
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()