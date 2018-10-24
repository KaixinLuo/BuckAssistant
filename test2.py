from assistant import Assistant
from BuckAD.DocumentModule import ClassInfoModule
from watson_developer_cloud import DiscoveryV1
assistant=Assistant()
brain = DiscoveryV1(
    version='2018-01-01',
    username='c7721aaf-1c20-4325-bb11-6cfe0cdb8967',
    password='2UOJ7kgQHbXH',
    url='https://gateway.watsonplatform.net/discovery/api'
)
discovery=ClassInfoModule(brain)
user_input=''

while user_input!='exit':
    user_input=input('>')
    query=assistant.get_intent_and_entity(user_input,toString=True)
    result=discovery.retrieve_first_doc_text(query)
    print(result)