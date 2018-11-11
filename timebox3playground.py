from modules.components.discovery_component import Discovery_Component
from watson_developer_cloud import DiscoveryV1

#assistant=Assistant()
apikey = DiscoveryV1(
    version='2018-01-01',
    username='c7721aaf-1c20-4325-bb11-6cfe0cdb8967',
    password='2UOJ7kgQHbXH',
    url='https://gateway.watsonplatform.net/discovery/api'
)
discovery=Discovery_Component()
print(discovery.process_natrual_language_query('what\'s Jim Davis\' research interests?'))