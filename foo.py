from watson_developer_cloud import AssistantV1
import json

f = open("key.txt", "r")
f1 = f.read().splitlines()
f.close()
assistant = AssistantV1(
            version=f1[0],
            username=f1[1],
            password=f1[2],
            url=f1[3]
        )

workspace_id = f1[4]
response = assistant.message(
            workspace_id=workspace_id,
            input={
                'text': input("question here: ")
            },
            context={}
        )
print(json.dumps(response,indent=2))
class ShortConversationAssitant:
    def __init__ (self):
        f = open("key.txt", "r")
        f1 = f.read().splitlines()
        f.close()
        self.entity = AssistantV1(
                    version=f1[0],
                    username=f1[1],
                    password=f1[2],
                    url=f1[3]
                )
        self.workspace_id = f1[4]
        self.context = {}
    
    def __call__(input_string):
        self.entity.message()