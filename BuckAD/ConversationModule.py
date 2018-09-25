
from watson_developer_cloud import AssistantV1
bot = AssistantV1(
    version='2018-01-01',
    username='a49fe062-4a18-4131-8843-f668502ae0de',
    password='JH1donieWOYc',
    url='https://gateway.watsonplatform.net/assistant/api')
#print (bot.list_workspaces()['workspaces'][1])
class ConversationModule:
    def __init__(self,kernel:AssistantV1):
        self.kernel = kernel
        self.current_workspace_id = kernel.list_workspaces()['workspaces'][1]['workspace_id']
        self.response = None

    def run_conversation(self,msg):
        self.response = self.kernel.message(workspace_id=self.current_workspace_id,input = {'text':msg})

    def get_the_best_entity_and_intent(self):
        return (self.response['intents'][0]["intent"],self.response["entities"][0]["value"])

cm = ConversationModule(bot)
cm.run_conversation("Who is teaching CSE 5526")
print (cm.get_the_best_entity_and_intent())

