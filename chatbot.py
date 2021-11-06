from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


michael = ChatBot('michael', read_only=True, database_uri='sqlite:///michael.db')
dwight = ChatBot('dwight', read_only=True, database_uri='sqlite:///dwight.db')

michaelTrainer = ListTrainer(michael)
dwightTrainer = ListTrainer(dwight)

fp = open('clean_dwight.txt')
dwightTrainer.train(fp.readlines())
fp.close()

print(dwight.get_response('hallo'))


