from watson_developer_cloud import DiscoveryV1
class Discovery_Component:
    def __init__(self):
        f = open("key.txt", "r")
        f1 = f.read().splitlines()
        self.discovery = DiscoveryV1(
            version=f1[5],
            username=f1[6],
            password=f1[7],
            url=f1[8]
        )
        self.currentEnvironment = self.discovery.list_environments(name ='byod')['environments'][0]['environment_id']
        self.collectionIndex = {e["name"]:e["collection_id"] for e in self.discovery.list_collections(environment_id=self.currentEnvironment)["collections"]}
        self.query_response = None

    def process_natrual_language_query(self, natrual_language_query):
        result=''
        for i in self.collectionIndex:
            col_id=self.collectionIndex.get(i)
            self.query_response=self.discovery.query(self.currentEnvironment, col_id, natural_language_query=natrual_language_query)
            #pp.pprint(''.join())
            #print(self.query_response.get('results'))
            if self.query_response.get('results')==[]:
                result=result+''
            else:
                stripped=self.query_response.get('results')[0].get('text').replace('\n','. ')
                result=result+stripped
        return result