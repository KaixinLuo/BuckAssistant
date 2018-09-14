import json

from watson_developer_cloud import DiscoveryV1
from watson_developer_cloud import AssistantV1
 
bot = AssistantV1(
    version='2018-01-01',
    username='c7721aaf-1c20-4325-bb11-6cfe0cdb8967',
    password='2UOJ7kgQHbXH',
    url='https://gateway.watsonplatform.net/discovery/api'
)

brain = DiscoveryV1(
    version='2018-01-01',
    username='c7721aaf-1c20-4325-bb11-6cfe0cdb8967',
    password='2UOJ7kgQHbXH',
    url='https://gateway.watsonplatform.net/discovery/api'
)

 #= '48fca871-ad3b-417e-b222-077b13523ccb'
#collection_id = '66d011eb-a6fe-4cc6-b5e9-1995284d34e3'
def initialize():
    pass

def get_all_environment_ID():
    return [e['environment_id'] for e in brain.list_environments()["environments"]]
    
def get_all_collection_ID(env_id):
    return [c['collection_id'] for c in brain.list_collections(env_id)['collections']]

def get_collection(e_id,c_id):
    return None


class BuckAss:
    def __init__(self):
        self.front = bot
        self.back = brain
        self.__current_env__ =get_all_environment_ID[1]
        self.__current_collection__ = get_all_collection_ID()[0]
    def get_the_most_likely_document(self,q):
         response = brain.query(self.__current_env__,self.__current_collection__,natural_language_query=q)
         return response['result'][0]['id']