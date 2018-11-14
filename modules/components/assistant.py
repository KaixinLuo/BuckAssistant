from watson_developer_cloud import AssistantV1
#from BuckAD.ClassInfoModule import ClassInfoModule
import json
import pprint

class Assistant:
    def __init__(self,debug_mode=False):
        self.debug_mode=debug_mode
        self.user_input = ''
        self.context1 = {}
        self.current_action = ''
        f = open("key.txt", "r")
        f1 = f.read().splitlines()
        f.close()
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
    '''
    process the input using assistant service
    :param message_in: user input in string
    :return: a list contains [intent(str),flag(bool),context(dict),response(str),input(str)]
    '''
    def process_input(self,message_in):
        #returns [intent(str),flag(bool),context(dict),response(str), input(str)]
        #where flag is true when current short conversation has ended
        result=[]
        response = self.assistant.message(
            workspace_id=self.workspace_id,
            input={
                'text': message_in
            },
            context=self.context1
        )
        #Keep context for future conversations
        self.context1 = response['context']
        if self.debug_mode:
            print(json.dumps(response, indent=4, sort_keys=True))
        # Add Intent
        if response.get('intents') != []:
            result.append(response.get('intents')[0].get('intent'))
        else:
            result.append('No_Intent')
        # Add Flag
        systemdic=response.get('context').get('system')
        has_question_ended=True
        if 'dialog_stack' in systemdic:
            dialoglist=systemdic.get('dialog_stack')
            if len(dialoglist) !=0 and 'state' in dialoglist[0] and dialoglist[0].get('state')=='in_progress':
                has_question_ended=False
        if 'dialog_status' in self.context1 and self.context1['dialog_status']=='in_progress':
            has_question_ended=False
        result.append(has_question_ended)
        #Add Context (a dictionary of conversation id, system node, and variables)
        tmpdictionary=self.context1
        #tmpdictionary['response']=response.get('output')
        result.append(self.context1)
        #Add Response
        result.append(' '.join(response.get('output').get('text')))
        if self.debug_mode:
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(result)
        result.append(message_in)
        return result
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
        if self.debug_mode:
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
            strresult=strresult+' '.join(intents)+' '+' '.join(entity_values)
            # for i in result:
            #     strresult+=' '.join(i)
            #     strresult+=' '
            #     print('#',strresult)
            return strresult
        return result
    
    def get_node_name(self, message_in, to_string = False):
        node_name = ""
        response = self.assistant.message(
            workspace_id=self.workspace_id,
            input={
                'text': message_in
            },
            context=self.context1
        )
        node_visited = response["output"]["nodes_visited"]
        current_node = node_visited[-1]
        current_node_info = self.assistant.get_dialog_node(
            workspace_id = self.workspace_id,
            dialog_node= current_node
        )
        current_node_name = current_node_info["title"]
        print("\ncurrent node: " + current_node_name + "\n")
