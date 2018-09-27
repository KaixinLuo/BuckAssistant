import smtplib
from email.mime.text import MIMEText


def construct_email_query(question,student_name):
    email='Dear advisor, \n\nI hope you are doing well. I would like to talk with you about {}, what would be the best time to schedule an appointment with you?\n\nThanks,\n{}'.format(question,student_name)
    return email

def construct_email_appointment(professor_name,question,student_name):
    email='Dear Prof. {},\n\nI hope you are doing well. I would like to make appointment with you for {}, What would be the best time for this appointment?\n\nSincerely,\n{}'.format(professor_name,question,student_name)
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






