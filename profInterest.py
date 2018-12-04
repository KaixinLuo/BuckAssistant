from watson_developer_cloud import DiscoveryV1
import json
#Discovery Info
collection_id='ecb955ce-2f8a-470a-b575-883d6ae3b23e'
configuration_id='32c941f8-00f0-4818-a1a2-313863fbabf2'
environment_id='d5fd4c04-ff01-43ee-80fd-97c790115f9e'
discovery = DiscoveryV1(
    version='2018-08-01',
    username='ca79b3a2-16f4-47ce-91aa-9a6ca5f3c844',
    password = '5ZED45njognu',
    url='https://gateway.watsonplatform.net/discovery/api'
)
allInterests=['Natural language processing',
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
'Database']
def discoveryQuery(keyword,type):
    #type 0: given interest, 1: given name
    queryWInterest = 'enriched_text.concepts.text:"' + keyword + '"'
    queryWName = 'extracted_metadata.filename:"' + keyword + '"'
    query=''
    if (type==0):
        return_fields = ['extracted_metadata.filename']
        query=queryWInterest
    else:
        keyword=keyword+".html"
        queryWName = 'extracted_metadata.filename:"' + keyword + '"'
        return_fields = ['enriched_text.concepts.text']
        query = queryWName
    my_query = discovery.query(environment_id=environment_id, collection_id=collection_id, query=query,
                               return_fields=return_fields)
    #print(json.dumps(my_query, indent=2))
    result=[]
    if (type==0):
        #my_query["results"][0].get("extracted_metadata").get("filename").strip(".html")
        a=my_query["results"]
        for x in a:
            result.append(x.get('extracted_metadata').get('filename').strip(".html"))
    else:
        print(my_query)
        a=my_query["results"][0].get("enriched_text").get("concepts")
        for x in a:
            result.append(x.get('text'))
    return result

print(discoveryQuery('Wei Xu', 1))