from assistant import Assistant
from BuckAD.ClassInfoModule import ClassInfoModule
from watson_developer_cloud import DiscoveryV1
import re
from user import User
from BuckAD.EmailModule import EmailModule
import intentProcessor
assistant=Assistant()
brain = DiscoveryV1(
    version='2018-01-01',
    username='c7721aaf-1c20-4325-bb11-6cfe0cdb8967',
    password='2UOJ7kgQHbXH',
    url='https://gateway.watsonplatform.net/discovery/api'
)
discovery=ClassInfoModule(brain)
current_user=User()
user_input=''
from modules import db_search
db1=db_search.Db_Search(False)
# query=assistant.get_intent_and_entity('who teaches CSE5526',to_string=True)
# queryr=assistant.get_intent_and_entity('who teaches CSE5526',to_string=False)
print('Thanks! How can I help you today?')
while user_input!='exit':
    user_input=input('>')
    if (user_input=='e'):
        print('Bye!')
        break
    queryr=assistant.process_input(user_input)
    print(db1.process([],queryr))