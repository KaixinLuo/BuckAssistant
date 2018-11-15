from modules.components.email_component import Email_Component
import modules.components.email_component as email
class Send_Email:
    acceptable_intents=[
        'Email_Send_Appointment'
    ]
    def __init__(self, debug_mode):
        self.debug_mode=debug_mode

    def log_in(self,user_object):
        self.user_object=user_object
        self.email_component=Email_Component()
        self.email_component.log_in(user_object)

    def process(self, potato, assistant_returned_info):
        '''
        Check if the passed in intent can be processed in this model and process it.
        :param potato: a list of the same format as the return list which is passed in to this module.
        :param assistant_returned_info: a list contains processed returned info from assistant in the format of
            [intent(str),flag(bool),context(dict),response(str), input(str)]
        :returns: a list [is_successfully_processed (bool), result (str)], where result can also be a string contains
            necessary info about processing a request which involves more than 1 modules if is_successfully_processed is. It will be passed to other
            modules.
        '''
        result=[]
        intent=assistant_returned_info[0]
        if intent in Send_Email.acceptable_intents:
            result.append(True) #This is hard coded for now since current requests do not involve more than 1 module
            paramlist=[]
            if self.debug_mode:
                print('send_email passed in intent: ',intent)
            result.append(getattr(Send_Email, intent)(self, assistant_returned_info))
        else:
            result.append(False)
            result.append('No result')
        return result
    def Email_Send_Appointment(self,assistant_returned_info):
        if 'person' in assistant_returned_info[2]:
            professor_name=assistant_returned_info[2].get('person')
        else:
            print('Missing Professor name while sending email.')
            return 'Missing Professor name while sending email.'
        if 'user_input' in assistant_returned_info[2]:
            question=assistant_returned_info[2].get('user_input')
        else:
            print('Missing user input for questions while sending email.')
            return 'Missing user input for questions while sending email.'
        #question = assistant_returned_info[4]
        student_name=self.user_object.name
        text=email.construct_email_appointment(professor_name,question,student_name)
        if 'email' in assistant_returned_info[2]:
            email_address=assistant_returned_info[2].get('email')
        else:
            print('Missing receiver email for questions while sending email.')
            return 'Missing receiver email for questions while sending email.'
        if self.debug_mode:
            print('[send_email.py] Send email info: ', email_address, professor_name, question, student_name)
        #print('[send_email.py] Send email info: ', email_address, professor_name, question, student_name)
        self.email_component.send(email_address, 'Appointment Scheduling', text)
        return 'Email Sent.'