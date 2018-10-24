from modules.db_search import Db_Search
from modules.send_email import Send_Email
class Module_Pipeline:
    def __init__(self,debug_mode=False):
        self.debug_mode=debug_mode
        self.modules={}
        self.modules['db_search']=Db_Search(debug_mode)
        self.modules['send_email']=Send_Email(debug_mode)

    def assign_user_object(self,user_object):
        self.modules.get('send_email').log_in(user_object)

    def process(self,assistant_returned_info):
        potato=[False,'No result']
        for i in self.modules:
            potato=self.modules[i].process(potato,assistant_returned_info)
            if potato[0]:
                if self.debug_mode:
                    print('Intent Processed: ',assistant_returned_info[0],' using ', i)
                break
        return potato[1]
