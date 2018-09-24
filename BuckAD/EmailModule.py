import smtplib
from email.mime.text import MIMEText


def construct_email_advisor(question,student_name):
    email='Dear advisor, \n\nI hope you are doing well. I want to make appointment with you for {}, what is your best time or could you tell me about it via email?\n\nBest,\n{}'.format(question,student_name)
    return email

def construct_email_professor(professor_name,question,student_name):
    email='Dear Prof. {},\n\nI hope you are doing well. I want to make appointment with you for {}, what is your best time to hold this appointment?\n\nBest,\n{}'.format(professor_name,question,student_name)
    return email

class EmailModule:
    def __init__(self,mail_host='smtp-mail.outlook.com',port = 587):
        self.mail_host = mail_host
        self.port = port
        self.server = smtplib.SMTP()

    def login(self,uname,pswd):
        self.username = uname
        self.password = pswd
        try:
            self.server.connect(self.mail_host,port=self.port)
            self.server.starttls()
            self.server.login(self.username,self.password)
        except smtplib.SMTPException:
            print("Error: Unable to log in")

    def send(self,receiver,subject,text):
        message = MIMEText(text, 'plain', 'utf-8')
        message['Subject'] = subject
        message['From'] = self.username
        message['To'] = receiver
        try:
            #smtpObj.sendmail(sender, receivers, message.as_string())
            self.server.sendmail(self.username,[receiver],message.as_string())
        except smtplib.SMTPException:
            print ("Error: Unable to send this message")
    def log_out(self):
        try:
            #smtpObj.sendmail(sender, receivers, message.as_string())
            self.server.quit()
        except smtplib.SMTPException:
            print ("Error: Unable to log out")






