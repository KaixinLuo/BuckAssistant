from watson_developer_cloud import AssistantV1
from BuckAD.ClassInfoModule import ClassInfoModule
import json


class Assistant:
    def __init__(self):
        self.user_input = ''
        self.context1 = {}
        self.current_action = ''
        f = open("D:\key.txt", "r")
        f1 = f.read().splitlines()
        self.assistant = AssistantV1(
            version=f1[0],
            username=f1[1],
            password=f1[2],
            url=f1[3]
        )
        self.workspace_id = f1[4]
        response = self.assistant.message(
            workspace_id=self.workspace_id,
            input={
                'text': self.user_input
            },
            context=self.context1
        )
        print(response['output']['text'][0])

    def get_response(self,messagein):
        # Returns a list of length 2, where 1st item is intend, and 2nd item is a list of entities
        result = ''
        response = self.assistant.message(
            workspace_id=self.workspace_id,
            input={
                'text': messagein
            },
            context=self.context1
        )
        self.context1 = response['context']
        # print(response['output']['text'][0])
        # print(json.dumps(response, indent=4, sort_keys=True))
        if response['output']['text']:
            result=response['output']['text'][0]



    def get_intent_and_entity(self,message_in,to_string=False):
        result=[]
        response = self.assistant.message(
            workspace_id=self.workspace_id,
            input={
                'text': message_in
            },
            context=self.context1
        )
        self.context1 = response['context']
        # print(response['output']['text'][0])
        print(json.dumps(response, indent=4, sort_keys=True))
        # Add Intend
        intents=[]
        for intent in response.get('intents'):
            intents.append(intent.get('intent'))
        result.append(intents)
        #Add Entity
        entities = {}
        entity_values=[]
        for entity in response.get('entities'):
            entity_name=entity.get('entity')
            location_of_entity=entity.get('location')
            entity_value=message_in[location_of_entity[0]:(location_of_entity[1]+1)]
            if entity_name not in entities:
                entities[entity_name]=(entity_value)
                entity_values.append(entity_value)
        result.append(entities)
        if (to_string):
            strresult=''
            print('in if')
            strresult=strresult+' '.join(intents)+' '+' '.join(entity_values)
            # for i in result:
            #     strresult+=' '.join(i)
            #     strresult+=' '
            #     print('#',strresult)
            return strresult
        return result

    def get_intent_and_variable(self,messagein,variable_name, toString=False):
        result=[]
        response = self.assistant.message(
            workspace_id=self.workspace_id,
            input={
                'text': messagein
            },
            context=self.context1
        )
        self.context1 = response['context']
        # print(response['output']['text'][0])
        print(json.dumps(response, indent=4, sort_keys=True))
        # Add Intend
        intents=[]
        for intent in response.get('intents'):
            intents.append(intent.get('intent'))
        result.append(intents)
        #Add Entity
        variables = []
        variables.append(response["context"][variable_name])
        result.append(" ")
        result.append(variables)
        if (toString):
            strresult=''
            for i in result:
                strresult+=' '.join(i)
            print(strresult)
            return strresult
        
        return result


        
#    def modify_answer_node(self, intent, result):

#
 #       return {
  #          "#Course_Instructor_of": "The instructors who recently provided this course: \n" + 

   #     }(intent, "I don't understand")



