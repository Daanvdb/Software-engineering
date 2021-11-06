from googletrans import Translator
from chatterbot import ChatBot

translator = Translator()

michael = ChatBot('michael', only_read=True, database_uri='')
dwight = ChatBot('dwight', only_read=True, database_uri='sqlite:///dwight.db')



