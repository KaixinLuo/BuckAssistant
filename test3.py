from assistant import Assistant
from BuckAD.ClassInfoModule import ClassInfoModule
from watson_developer_cloud import DiscoveryV1
import json
assistant=Assistant()
brain = DiscoveryV1(
    version='2018-01-01',
    username='863d2ed8-3581-4c7f-bc7a-1d846e591384',
    password='5x6t2XkF5mZ4',
    url='https://gateway.watsonplatform.net/discovery/api'
)
discovery = ClassInfoModule(brain)
user_input = ""
while user_input != "exit":
    user_input = input(">")
    query=assistant.get_intent_and_variable(user_input,toString=True)
    discovery.run_query(query)
    course_info = assistant.search_instructor_by_course_num(query, discovery)
    print(json.dumps(course_info))
    print("----------------------------")
    names = course_info["professors"]
    print(names)


