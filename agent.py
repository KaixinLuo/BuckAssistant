import os 
from BuckAD.EmailModule import EmailModule
import IntentProcessor
from assistant import Assistant


class Agent:
    def __init__(self):
        self.user_input = ""
        self.user_name_dot_num = ""
        self.user_password = ""
        self.email_module = EmailModule()
        self.assistant = Assistant()
    
    def get_credential(self):
        self.user_name_dot_num = input("\nPlease enter your name.#:")
        self.user_password = input("\nPlease enter your password:")
    
    def get_ready_for_email(self):
        username_email = self.user_name_dot_num + "@osu.edu"
        self.email_module.login(username_email, self.user_password)
    def get_response(self):
        while self.user_input!='exit':
            self.user_input=input('>')
            queryr=self.assistant.get_intent_and_entity(self.user_input,to_string=False)
            if ('course_num' in queryr[1]):
                search_parameters = queryr[1].get('course_num')
            elif ('semesters' in queryr[1]):
                search_parameters = queryr[1].get('semesters')
            elif ('sys-number' in queryr[1]):
                search_parameters = queryr[1].get('sys-number')
            elif ('sys-person' in queryr[1]):
                search_parameters = queryr[1].get('sys-person')
            result = getattr(IntentProcessor, queryr[0][0])(search_parameters)
            # discovery.run_query(query)
            # result = discovery.retrieve_first_doc_text()
            print(result)



