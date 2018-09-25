

class Agent:
    def __init__(self,interface,pipeline):
        self.interface = interface
        self.pipline = pipeline

    def init(self,usr_info):
        self.info = usr_info

    def repl(self):
        command = ''
        while (command != "quit"):
            command = input(">")
            (intent,entity)=self.interface.run_conversation(command)
            self.pipline(intent,entity)




