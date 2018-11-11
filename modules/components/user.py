class User:
    def __init__(self):
        pass
    def set_email_address(self, email):
        self.__email=email
        self.name='Anonymous'
    def get_email_address(self):
        return self.__email
    def set_email_password(self, password):
        self.__password=password
    def authorize_email_account(self,module,function_name):
        result=getattr(module, function_name)(self.__email,self.__password)
        
        if not result:
            print('Authorization failed (user authorize_email_account')
    def set_name(self, name):
        self.name=name