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
email_module=EmailModule()


user_input=input('Can I start by asking your email address?')
while not re.match(r".*@.*\..*", user_input):
    user_input = input('Sorry that may not be the correct email. Please type again.')
current_user.assign_email_address(user_input)
user_input=input('Can I have your password as well?')
current_user.assign_email_password(user_input)
current_user.authorize_email_module(email_module)
user_input=input('What is your name?')
current_user.assign_name(user_input)
# query=assistant.get_intent_and_entity('who teaches CSE5526',to_string=True)
# queryr=assistant.get_intent_and_entity('who teaches CSE5526',to_string=False)
print('Thanks! How can I help you today?')
while user_input!='exit':
    user_input=input('>')
    queryr=assistant.get_intent_and_entity(user_input,to_string=False)
    if ('course_num' in queryr[1]):
        search_parameters = queryr[1].get('course_num')
    elif ('semesters' in queryr[1]):
        search_parameters = queryr[1].get('semesters')
    elif ('sys-number' in queryr[1]):
        search_parameters = queryr[1].get('sys-number')
    elif ('sys-person' in queryr[1]):
        search_parameters = queryr[1].get('sys-person')
<<<<<<< HEAD
    result = getattr(intentProcessor, queryr[0][0])(search_parameters)
=======
    if queryr[0]==[]:
        print('Unknown Question')
    elif (queryr[0][0]=='General_Ending'):
        print('Bye!')
        break
    if queryr[0][0]=='Email_Send_Appointment':
        if ('sys-person' not in queryr[1]):
            professor=input('What is the name of professor?')
        else:
            professor= queryr[1].get('sys-person')
        question=input('What is the topic of this appointment? Or what is your question?')
        email=input('What about his/her email?')
        result = getattr(intentProcessor, queryr[0][0])(email_module,current_user,question,professor,email)
    else:
        result = getattr(intentProcessor, queryr[0][0])(search_parameters)
>>>>>>> c65ed0cb771195151b198a473ea63cdf55c4a326
    # discovery.run_query(query)
    # result = discovery.retrieve_first_doc_text()
    print(result)