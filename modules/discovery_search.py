from modules.components.discovery_component import Discovery_Component
from modules.components.natural_language_understanding_component import Natural_Language_Understanding_Component
import json
class Discovery_Search:
    acceptable_intents = [
        'Concepts_Course_Is_About',
        'Instructor_Research_Interests',
        'No_Intent'
    ]
    def __init__(self,debug_mode=False):
        self.debug_mode=debug_mode
        self.discovery=Discovery_Component(debug_mode)
        self.nlu=Natural_Language_Understanding_Component(debug_mode)

    def process(self, potato, assistant_returned_info):
        result=[]
        intent=assistant_returned_info[0]
        if intent in Discovery_Search.acceptable_intents:
            result.append(True) #This is hard coded for now since current requests do not involve more than 1 module
            result.append(getattr(Discovery_Search, intent)(self, assistant_returned_info))
            #result.append(self.discovery_search(assistant_returned_info))
        else:
            result.append(False)
            result.append('No result')
        return result

    def Concepts_Course_Is_About(self,assistant_returned_info):
        '''
        Search courses containing the concepts in user input
        :param assistant_returned_info: [intent(str),flag(bool),context(dict),response(str), input(str)]
        :return: a str of course numbers
        '''
        #Use natural language understanding tool to extract concepts from user input
        #Confidence threshold can be changed via nlu.additional_settings()
        user_input=assistant_returned_info[4]
        concepts=self.nlu.get_concepts(user_input,3) #max number of results returned is 3
        subquery='enriched_text.concepts.text:' #Add " before and after a concept
        query=''
        if len(concepts)!=0:
            for concept in concepts:
                query = query + subquery + '"' + concept+'"|'
        else:
            return 'Can you rephrase your question and include some details of what concepts or topics you ' \
                   'are looking for?'
        query=query[:-1] #remove extra |
        response=self.discovery.process_discovery_query(query)
        #if self.debug_mode:
        #print(json.dumps(response, indent=2))
        filenames=self.get_file_names_of_matching_results(response)
        if len(filenames)==0:
            return 'Sorry. I didn\'t find any related course. Is the course you are looking for a CSE course? Currently ' \
                   'I cannot find courses in other majors.'
        else:
            sentence='Sure! Here are some courses that might interest you: '
            return sentence+(', '.join(filenames))

    def get_file_names_of_matching_results(self,response):
        filenames=[]
        passages=response.get('results')
        if len(passages)!=0:
            for item in passages:
                filename=self.discovery.get_document_details(item.get('id'),True)
                filename=filename.replace('.pdf', '').replace('General_', '').replace('-', ' ')
                if filename not in filenames:
                    filenames.append(filename)
        return filenames

    def discovery_search(self,assistant_returned_info):
        if 'user_input' in assistant_returned_info[2]:
            return '\n'+self.discovery.process_natrual_language_query(assistant_returned_info[2].get('user_input'))
        else:
            return 'Warning in discover_search:No user input.'
    def No_Intent(self,assistant_returned_info):
        return "Please tell me something more or be more specific like: \nI would like to know who is teaching CSE5526\n"
    
    def Instructor_Research_Interests(self,info):
        return "I recommend you shooting an email to ask the advisor or the professor directly. I was trying to gather those info when I was created but no professor replyed. Maybe because I am virtual?\n"