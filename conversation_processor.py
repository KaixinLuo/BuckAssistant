from modules.module_pipeline import Module_Pipeline
from modules.components.assistant import Assistant
from modules.components.special_strings_checker import Special_Strings_Checker
class Conversation_Processor:
    def __init__(self,debug_mode=False):
        self.debug_mode=debug_mode
        self.module_pipeline=Module_Pipeline(debug_mode)
        self.assistant=Assistant(debug_mode)
        self.saved_intent = ''
        self.has_intent_saved = False
        self.long_conversation = False
        self.special_string_checker=Special_Strings_Checker()

    def assign_user_object(self,user_object):
        self.module_pipeline.assign_user_object(user_object)

    def process_message(self,message):
        result=''
        check_info=self.special_string_checker.process(message)
        if check_info[0]: #if skip assistant processing
            result=check_info[2] #directly assing output message to result
            result=result+'\nInvalid input. Please re-enter your message.'
        else:
            message=check_info[1] #user input might be changed, need to re assign it to message
            assistant_returned_info = self.assistant.process_input(message)
            # print output from assistant
            result=result+assistant_returned_info[3]
            #print(assistant_returned_info[3])
            if assistant_returned_info[1]:
                if self.long_conversation:
                    if assistant_returned_info[0]!='General_Wrong_Question_Or_Stop':
                        assistant_returned_info[0] = self.saved_intent
                        result = result + self.module_pipeline.process(assistant_returned_info)
                        self.long_conversation = False
                        self.has_intent_saved = False
                else:
                    returned_string=self.module_pipeline.process(assistant_returned_info)
                    if result=='' or returned_string!='No result':
                        result = result + returned_string
                    #print(self.module_pipeline.process(assistant_returned_info))
            else:
                self.long_conversation = True
                if not self.has_intent_saved:
                    self.saved_intent = assistant_returned_info[0]
                    self.has_intent_saved = True
        return result

    '''
    For test purpose only. Use process_message instead.
    '''
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

