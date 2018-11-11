from conversation_processor import Conversation_Processor
from modules.components.user import User
from modules.components.natural_language_understanding_component import Natural_Language_Understanding_Component
u=User()
f = open("email.txt", "r")
f1 = f.read().splitlines()
u.set_email_address(f1[0])

u.set_email_password(f1[1])
u.set_name('ASD')
cp=Conversation_Processor(False)
cp.assign_user_object(u)
nlu=Natural_Language_Understanding_Component()
while True:
    st=input('>')
    #print(nlu.get_concepts(st))
    print(cp.process_message(st))




# s='qwe'
# print(s[:-1])
# from modules.components.discovery_component import Discovery_Component
# dc=Discovery_Component()
# #dc.process_discovery_query('enriched_text.concepts.text:"Artificial intelligence"|enriched_text.concepts.text:"Database"')
# #print(dc.get_document_details('0749c8c4f95fe22ac5f099b7360cadfs',True))



#
# print('General_CSE-6193.pdf'.replace('.pdf','').replace('General_','').replace('-',' '))
# print('General_CSE-6193.pdf'.strip('.pdf').strip('General_').strip('-'))
#cp.loop()
# from test_cases.test_assistant import test_process_input_single_response, test_process_input_sequential_response
# print(test_process_input_single_response())
# print(test_process_input_sequential_response())
#
# from test_cases.test_pipeline import test_db_search
# print(test_db_search())