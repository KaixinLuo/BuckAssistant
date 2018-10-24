# from modules import db_search
# # db1=db_search.Db_Search(False)
# # db1.process([],['Course_Average_Size_Of'])
from user import User
from test33 import Testu
user1=User()
user1.set_email_address('aaa')
user1.set_email_password('qqq')
t=Testu()
user1.authorize_email_account(t,'testfunc')



