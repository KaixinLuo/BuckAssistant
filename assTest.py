from watson_developer_cloud import AssistantV1
import json
f= open("D:\key.txt","r")
f1 = f.read().splitlines()
ass = AssistantV1(
    version=f1[0],
    username=f1[1],
    password=f1[2],
    url=f1[3]
)
workspace_id=f1[4]

user_input = ''
context = {}
current_action = ''

while True:
    user_input=input('>')
    response = ass.message(
      workspace_id = workspace_id,
        input={
            'text': user_input
        },
    )
    print(response['output']['text'][0])
    #print(TempText.dumps(response, indent=4, sort_keys=True))
    # print (response['intents'][0].get('intent'))
    if response['intents'][0].get('intent')=='General_Ending':
        break