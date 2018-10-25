from modules.discovery_component import Discovery_Component
class Discovery_Search:
    acceptable_intents = [
        'Instructor_Research_Interests',
        'No_Intent'
    ]
    def __init__(self,debug_mode=False):
        self.dc=Discovery_Component()

    def process(self, potato, assistant_returned_info):
        result=[]
        intent=assistant_returned_info[0]
        if intent in Discovery_Search.acceptable_intents:
            result.append(True) #This is hard coded for now since current requests do not involve more than 1 module
            result.append(self.discovery_search(assistant_returned_info))
        else:
            result.append(False)
            result.append('No result')
        return result
    def discovery_search(self,assistant_returned_info):
        if 'user_input' in assistant_returned_info[2]:
            return '\n'+self.dc.process_natrual_language_query(assistant_returned_info[2].get('user_input'))
        else:
            return 'Warning in discover_search:No user input.'