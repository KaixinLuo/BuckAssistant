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

class Brain:
    def __init__(self,kernel:DiscoveryV1):
        self.kernel = kernel
        self.currentEnvironment = kernel.list_environments(name = 'byod')['environments'][0]['environment_id']
        self.collectionIndex = {e["name"]:e["collection_id"] for e in kernel.list_collections(environment_id=self.currentEnvironment)["collections"]}


    def retrieve_first_doc_text(self,nl_query):
        return {
        name: self.kernel.query(self.currentEnvironment, col_id, natural_language_query=nl_query)["results"][0]["text"]
        for (name, col_id) in self.collectionIndex.items()}

    def retrieve_docs_by_confidence(self,query,key = "text"):
        r = {name:self.kernel.query(self.currentEnvironment, col_id, natural_language_query=query)for (name,col_id) in self.collectionIndex.items()}
        return {k:[(e["text"],e["result_metadata"]["score"]) for e in elem["results"]] for (k,elem) in r.items()}


b = Brain(brain)

print(b.retrieve_docs_by_confidence("deliang wang")["CourseInfo"])
