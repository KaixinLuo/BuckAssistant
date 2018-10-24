from modules.module_pipeline import Module_Pipeline
from assistant import Assistant
class Conversation_Processor:
    def __init__(self,debug_mode=False):
        self.debug_mode=debug_mode
        self.module_pipeline=Module_Pipeline(debug_mode)
        self.assistant=Assistant(debug_mode)
        self.saved_intent = ''
        self.has_intent_saved = False
        self.long_conversation = False

    def assign_user_object(self,user_object):
        self.module_pipeline.assign_user_object(user_object)

    def process_message(self,message):
        result=''
        user_input = message
        assistant_returned_info = self.assistant.process_input(user_input)
        # print output from assistant
        result=result+assistant_returned_info[3]
        #print(assistant_returned_info[3])
        if assistant_returned_info[1]:
            if self.long_conversation:
                assistant_returned_info[0] = self.saved_intent
                result = result + self.module_pipeline.process(assistant_returned_info)
                long_conversation = False
                has_intent_saved = False
            else:
                print(ass)
                result = result + self.module_pipeline.process(assistant_returned_info)
                #print(self.module_pipeline.process(assistant_returned_info))
        else:
            long_conversation = True
            if not self.has_intent_saved:
                saved_intent = assistant_returned_info[0]
                has_intent_saved = True
        return result

    def loop(self):
        saved_intent=''
        has_intent_saved=False
        long_conversation=False
        while True:
            user_input=input('>')
            assistant_returned_info=self.assistant.process_input(user_input)
            #print output from assistant
            print(assistant_returned_info[3])
            if assistant_returned_info[1]:
                if long_conversation:
                    assistant_returned_info[0]=saved_intent
                    print(self.module_pipeline.process(assistant_returned_info))
                    long_conversation=False
                    has_intent_saved=False
                else:
                    print(self.module_pipeline.process(assistant_returned_info))
            else:
                long_conversation=True
                if not has_intent_saved:
                    saved_intent=assistant_returned_info[0]
                    has_intent_saved=True

