import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions, ConceptsOptions

# response = natural_language_understanding.analyze(
#     text='show me some courses about neural network',
#     features=Features(categories=CategoriesOptions()))
#Features(concepts=ConceptsOptions(limit=3))).get_result()

class Natural_Language_Understanding_Component:
    def __init__(self,debug_mode=False):
        f = open("key.txt", "r")
        f1 = f.read().splitlines()
        self.debug_mode=debug_mode
        self.nlu = NaturalLanguageUnderstandingV1(
            version=f1[9],
            username=f1[10],
            password=f1[11],
            url=f1[12]
        )
    def additional_settings(self,min_relevance=0.0):
        self.min_relevance=min_relevance

    def get_concepts(self,user_input,max_number_of_concepts=3):
        '''
        Extract concepts from a given string
        :param str user_input:
        :param int max_number_of_concepts:
        :return: a list of concepts(str)
        '''
        result=[]
        response=self.nlu.analyze(
            text=user_input,
            features=Features(concepts=ConceptsOptions(limit=max_number_of_concepts)),
            language = 'en'
        )
        if self.debug_mode:
            print(json.dumps(response, indent=2))

        concepts=response.get('concepts')
        if len(concepts)!=0:
            for concept in concepts:
                result.append(concept.get('text'))
        return result