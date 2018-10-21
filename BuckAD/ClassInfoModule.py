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

class ClassInfoModule:
    def __inClassInfoModuleit__(self,kernel:DiscoveryV1):
        self.kernel = kernel
        self.currentEnvironment = kernel.list_environments(name = 'byod')['environments'][0]['environment_id']
        self.collectionIndex = {e["name"]:e["collection_id"] for e in kernel.list_collections(environment_id=self.currentEnvironment)["collections"]}
        self.query_response = None

    def run_query(self,nlq):
        self.query_response = {name:self.kernel.query(self.currentEnvironment, col_id, natural_language_query=nlq) for (name, col_id) in self.collectionIndex.items()}

        print(self.query_response)
    def num_of_result(self):
        return {name:elem["matching_results"] for (name,elem) in self.query_response.items()}

    def retrieve_first_doc_text(self):
        return {name: r["results"][0]["text"] for (name, r) in self.query_response}

    def retrieve_docs_with_score(self,query,key = "text"):
        return {k:[(e[key],e["result_metadata"]["score"]) for e in elem["results"]] for (k,elem) in self.query_response.items()}




