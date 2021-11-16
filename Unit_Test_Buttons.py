# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:34:22 2021

@author: btych
"""

from tkinter import *
from googletrans import Translator
#from chatterbot import ChatBot
#from chat import get_response, bot_name

translator = Translator()

bot = "dwight"

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
translate = False

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:
    
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.UnitTestSend()
        self.UnitTestLang()
        self.UnitTestPers()
        self.window.mainloop()
        

    def _change_language(self, Event):                                       # _change_language and _change_personality have to be declared before declaring the buttons
        global translate                                                    # otherwise it might rise an error or get stuck in a loop
        if translate == True:
            self.trans_button.config(text="NL")
            translate = False
        else:
            self.trans_button.config(text="EN")
            translate = True


    def UnitTestPers(self):
        self.bot_pers.invoke()
        if self.bot_pers['text']!="michael" and bot!="dwight":
            msg = "Personality test 1 successful"
            self._insert_message(msg, "Unit Test", bot)

        self.bot_pers.invoke()
        if self.bot_pers['text']!="dwight" and bot!="michael":
            msg = "Personality test 2 successful"
            self._insert_message(msg, "Unit Test", bot)

    def UnitTestLang(self):
        global translate
        self.trans_button.invoke()
        if translate==True and self.trans_button['text']=="EN":
            msg = "Language test 1 successful"
            self._insert_message(msg, "Unit Test", bot)
        
        self.trans_button.invoke()
        if translate==False and self.trans_button['text']=="NL":
            msg = "Language test 2 successful"
            self._insert_message(msg, "Unit Test", bot)

    def UnitTestSend(self):
        self.msg_entry.insert(1,"abc")
        self.send_button.invoke()
        x=0
        if "You: abc" in self.text_widget.get(0.0,END):
            msg = "Send button text successful"
            self._insert_message(msg, "Unit Test", bot)
        


    def _change_personality(self,Event):
        b = 2
        global bot
        if bot=="dwight":
            self.bot_pers.config(text="Dwight")
            bot = "michael"
        else:
            self.bot_pers.config(text="Michael")
            bot = "dwight"

        
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=950, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
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
        self.send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        self.send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

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
        
        self.text_widget.see(END)
             
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()