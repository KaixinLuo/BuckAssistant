from conversation_processor import Conversation_Processor
from user import User
u=User()
f = open("email.txt", "r")
f1 = f.read().splitlines()
print(f1)
u.set_email_address(f1[0])
u.set_email_password(f1[1])
u.set_name('ASD')
cp=Conversation_Processor(True)
cp.assign_user_object(u)
while True:
    st=input('>')
    print(cp.process_message(st))
#cp.loop()
# from test_cases.test_assistant import test_process_input_single_response, test_process_input_sequential_response
# print(test_process_input_single_response())
# print(test_process_input_sequential_response())
#
# from test_cases.test_pipeline import test_db_search
# print(test_db_search())