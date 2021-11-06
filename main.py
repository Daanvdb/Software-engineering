from googletrans import Translator
from chatterbot import ChatBot

translator = Translator()

michael = ChatBot('michael', only_read=True, database_uri='')
dwight = ChatBot('dwight', only_read=True, database_uri='sqlite:///dwight.db')


def nl_to_en(text_input):
    return translator.translate(text_input, src='nl', dest='en').text

def en_to_nl(text_input):
    return translator.translate(text_input, src='en', dest='nl').text