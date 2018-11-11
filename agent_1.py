from BuckAD.EmailModule import EmailModule
from BuckAD.ClassInfoModule import ClassInfoModule
from modules.components.assistant import Assistant

intent_module_map={
    "Course_Credits_Of" : {"intentProcessor", "self.ClassInfoModule"},
    "Course_Opentime_Of" : {"intentProcessor", "self.ClassInfoModule"},
    "Course_Desription_Of" : {"intentProcessor", "self.ClassInfoModule"},
    "Course_Instructor_Of" : {"intentProcessor", "self.ClassInfoModule"},
    "Course_Average_Size_Of" : {"intentProcessor", "self.ClassInfoModule"},
    "Course_Prerequisite_Of" : {"intentProcessor", "self.ClassInfoModule"},
    "Course_Title_Of" : {"intentProcessor", "self.ClassInfoModule"},
    "Credit_Course_Is" : {"intentProcessor", "self.ClassInfoModule"},
    "Semester_Has_Courses" : {"intentProcessor", "self.ClassInfoModule"},
    "Instructor_Teaches" : {"intentProcessor", "self.ClassInfoModule"},
    "Instructor_Rsearch_Interest" : {"intentProcessor", "self.ClassInfoModule"},
    "Concept_Courses" : {"self.ClassInfoModule"},
    "Email_Send_Appointment" :{"self.email_module"},
    "anything_else" : {}

}
intent_entity_map={

}
class Agent_1:
    def __init__(self):
        self.user_input = ""
        self.user_name_dot_num = ""
        self.user_password = ""
        self.email_module = EmailModule()
        self.assistant = Assistant()
        self.classInfo_module = ClassInfoModule()
    
    def get_credential(self):
        self.user_name_dot_num = input("\nPlease enter your name.#:")
        self.user_password = input("\nPlease enter your password:")
    
    def get_ready_for_email(self):
        username_email = self.user_name_dot_num + "@osu.edu"
        self.email_module.login(username_email, self.user_password)

    def get_response_from_module(self, query, times_of_process):
        ##assume query is a list : query[0] is header ; query[1]
        module = intent_module_map[query[0]][times_of_process]
        entity = query[1][intent_entity_map[query[0]]]
        query = query[0:]
        result = module.get_response(query)
        return result 
    
