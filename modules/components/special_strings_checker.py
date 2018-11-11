import re
class Special_Strings_Checker:
    #list of functions that will be called in checking (Must be in this class, but no need to include all functions)
    function_checklist=[
        'check_if_contains_symbols_only'
    ]
    def __init__(self, debug_mode=False):
        self.debug_mode=debug_mode

    '''
    Check if the given string is a special string or not. Should be called before assistant.process()
    :param user_input: user input in string
    :returns: a list [skip_assistant(bool), processed_input(string),output(string)]
    '''
    def process(self, user_input):
        input_info=[False,user_input,'']
        for function_name in Special_Strings_Checker.function_checklist:
            if not getattr(Special_Strings_Checker, function_name)(self, input_info):
                return input_info

        return input_info

    '''
    Check if the input contains strange symbols only
    :param user_input: user input in string
    :param input_info: a list [skip_assistant(bool), processed_input(string),output(string)]
    :returns: passed(bool). If passed, input_info will not be modified.
    '''
    def check_if_contains_symbols_only(self, input_info):
        if re.search('[a-zA-Z0-9]',input_info[1])!=None:
            return True
        else:
            input_info[0]=True
            input_info[2]='Stephen Detected!'
            return False