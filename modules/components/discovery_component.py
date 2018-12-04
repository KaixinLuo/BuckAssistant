from watson_developer_cloud import DiscoveryV1
import json
class Discovery_Component:
    def __init__(self,debug_mode=False,query_word_limit=150):
        f = open("key.txt", "r")
        f1 = f.read().splitlines()
        self.debug_mode=debug_mode
        self.discovery = DiscoveryV1(
            version=f1[5],
            username=f1[6],
            password=f1[7],
            url=f1[8]
        )
        self.discovery_c = DiscoveryV1(
            version=f1[20],
            username=f1[21],
            password=f1[22],
            url=f1[23]
        )
        self.collection_id = f1[24]
        self.configuration_id = f1[25]
        self.environment_id = f1[26]
        f.close()
        self.query_word_limit=query_word_limit
        self.currentEnvironment = self.discovery.list_environments(name ='byod')['environments'][0]['environment_id']
        self.collectionIndex = {e["name"]:e["collection_id"] for e in self.discovery.list_collections(environment_id=self.currentEnvironment)["collections"]}
    def process_discovery_query(self,discovery_query):
        collection_id=self.collectionIndex.get("general_syllabus")
        response=self.discovery.query(environment_id=self.currentEnvironment, collection_id=collection_id, query=discovery_query)
        if self.debug_mode:
            print(json.dumps(response, indent=2))
        return response

    def get_document_details(self,document_id,title_only):
        collection_id=self.collectionIndex.get("general_syllabus")
        doc_info = self.discovery.get_document_status(self.currentEnvironment, collection_id, document_id)
        #print(json.dumps(doc_info, indent=2))
        if title_only:
            return doc_info.get('filename')
        return doc_info

    def process_natrual_language_query(self, natrual_language_query):
        result=''
        #for i in self.collectionIndex:
        col_id=self.collectionIndex.get("general_syllabus")
        query_response=self.discovery.query(self.currentEnvironment, col_id, natural_language_query=natrual_language_query)
        #pp.pprint(''.join())
        #print(self.query_response.get('results'))
        #passages_characters
        if query_response.get('results')==[]:
            result=result+''
        else:
            stripped=query_response.get('results')[0].get('text').replace('\n','.')
            if len(stripped)>self.query_word_limit:
                stripped=stripped[:self.query_word_limit]
            result=result+stripped
        return result