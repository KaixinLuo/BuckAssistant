from modules.components.discovery_component import Discovery_Component
from modules.components.natural_language_understanding_component import Natural_Language_Understanding_Component
import json
class Discovery_Search:
    acceptable_intents = [
        'Concepts_Course_Is_About',
        'Instructor_Research_Interests',
        'Research_Interest_Instructor',
        'No_Intent'
    ]
    allInterests = ['Natural language processing',
                    'Machine learning',
                    'Grid computing',
                    'Data mining',
                    'Artificial Intelligence',
                    'Computer Graphics',
                    'Computer Network',
                    'Software Engineering',
                    'Algorithm',
                    'Computational Linguistic',
                    'Computer Security',
                    'Cryptography',
                    'Database',
                    'Graph']
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

    def No_Intent(self,assistant_returned_info):
        '''
        Method for handling unknown question. Do natural language query on all collections
        :param assistant_returned_info: [intent(str),flag(bool),context(dict),response(str), input(str)]
        :return: If can find result, return most related paragraph, else return warning message
        '''
        #result=''
        #user_input = assistant_returned_info[4]
        starting_message='I am trying to find some related information.'
        search_result=self.discovery.process_natrual_language_query(assistant_returned_info[2].get('user_input'))
        if search_result=='':
            return starting_message+'It looks like there is no information related to your input.'
        else:
            return starting_message+'\n'+search_result


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
    def Instructor_Research_Interests(self,assistant_returned_info):
        # type 0: given interest, 1: given name
        if 'name' in assistant_returned_info[2]:
            name = assistant_returned_info[2].get('name')
        else:
            print(assistant_returned_info)
            return 'Can you provide the name of the professor?'
        query_w_name = 'extracted_metadata.filename:"' + name + '"'
        query = ''
        type=1
        keyword = name + ".html"
        query_w_name = 'extracted_metadata.filename:"' + keyword + '"'
        return_fields = ['enriched_text.concepts.text']
        query = query_w_name
        my_query = self.discovery.discovery_c.query(environment_id=self.discovery.environment_id, collection_id=self.discovery.collection_id, query=query,
                                   return_fields=return_fields)
        # print(json.dumps(my_query, indent=2))
        result = []
        if my_query.get('matching_results')==0:
            return 'Sorry, I cannot find results related to your query.'

        print(my_query)
        a = my_query["results"][0].get("enriched_text").get("concepts")
        for x in a:
            concept_text=x.get('text');
            if concept_text.isdigit():
                continue
            result.append(concept_text)

        if len(result)==0:
            sentence='Sorry, I cannot find results related to your query.'
        else:
            sentence='Here are the results I found! '+name+' is interested in '
        return sentence+(', '.join(result))
    def Research_Interest_Instructor(self, assistant_returned_info):
        # type 0: given interest, 1: given name
        user_input = assistant_returned_info[4]
        concepts=self.nlu.get_concepts(user_input, 3)  # max number of results returned is 3
        if len(concepts)!=0:
            keyword=concepts[0]
        else:
            return 'Can you rephrase your question and include some details of what concepts or topics you ' \
                   'are looking for?'

        query_w_interest = 'enriched_text.concepts.text:"' + keyword + '"'
        return_fields = ['extracted_metadata.filename']
        query = query_w_interest

        my_query = self.discovery.discovery_c.query(environment_id=self.discovery.environment_id, collection_id=self.discovery.collection_id, query=query,
                                   return_fields=return_fields)
        # print(json.dumps(my_query, indent=2))
        result = []
        # my_query["results"][0].get("extracted_metadata").get("filename").strip(".html")
        a = my_query["results"]
        for x in a:
            result.append(x.get('extracted_metadata').get('filename').strip(".html"))

        if len(result)==0:
            sentence='Sorry, I cannot find results related to your query.'
        else:
            sentence='Here are the results I found! '+keyword+' is interested in '
        return sentence+(', '.join(result))

        # return "I recommend you shooting an email to ask the advisor or the professor directly. I was trying to gather those info when I was created but no professor replyed. Maybe because I am virtual?\n"