class User:
    def __init__(self):
        pass
    def assign_email_address(self,email):
        self.__email=email
    def assign_email_password(self,password):
        self.__password=password
    def authorize_email_module(self,email_module):
        email_module.login(self.__email,self.__password)