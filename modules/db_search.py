import os, json, re, sys
class Db_Search:
    acceptable_intents=[
        'Course_Average_Size_Of',
        'Course_Credits_Of',
        'Course_Description_Of',
        'Course_Instructor_Of',
        'Course_Opentime_Of',
        'Course_Title_Of',
        'Credit_Course_Is',
        'Instructor_Teaches',
        'Semester_Has_Courses'
    ]

    def __init__(self,debug_mode):
        self.debug_mode = debug_mode
        path_to_json = 'crawler/courseInformation/Json'
        self.json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        self.courses_info = []
        for js in self.json_files:
            with open(path_to_json + '/' + js) as f:
                self.courses_info.append(json.load(f))

    '''
    Check if the passed in intent can be processed in this model and process it.
    :param potato: a list of the same format as the return list which is passed in to this module.
    :param assistant_returned_info: a list contains processed returned info from assistant in the format of
        [intend(str),flag(bool),context(dict),response(str)]
    :returns: a list [is_successfully_processed (bool), result (str)], where result can also be a string contains
        necessary info about processing a request which involves more than 1 modules if is_successfully_processed is. It will be passed to other
        modules.
    '''
    def process(self, potato, assistant_returned_info):
        result=[]
        intent=assistant_returned_info[0]
        if intent in Db_Search.acceptable_intents:
            result.append(True) #This is hard coded for now since current requests do not involve more than 1 module
            paramlist=[]
            result.append(getattr(Db_Search, intent)(self, assistant_returned_info))
        else:
            result.append(False)
            result.append('No result')
        return result

    # def Course_Average_Size_Of(self, course_num):
    #     #For test purpose only
    #     print(course_num)
    def Course_Average_Size_Of(self, assistant_returned_info):
        if 'course_num' in assistant_returned_info[2]:
            course_num = re.sub(r"\D", "", assistant_returned_info[2].get('course_num'))
        else:
            return 'Can you rephrase your question with more details?'
        #course_num = re.sub(r"\D", "", course_num)
        json_file_name = 'CSE' + course_num + '.json'
        if json_file_name in self.json_files:
            course_index = self.json_files.index(json_file_name)
            response_header = 'The average size of ' + str(course_num) + ' is '
            value_found = self.courses_info[course_index].get('average_size')
            #Clear variable value
            assistant_returned_info[2]['course_num']=None
            if value_found is not None:
                return response_header + str(value_found)
            else:
                return 'Sorry, we do not have information about it. Please try another question.'
        else:
            assistant_returned_info[2]['course_num']=None
            return 'Cannot find the given course number'

    def Course_Credits_Of(self, assistant_returned_info):
        if 'course_num' in assistant_returned_info[2]:
            course_num = re.sub(r"\D", "", assistant_returned_info[2].get('course_num'))
        else:
            return 'Can you rephrase your question with more details?'
        #course_num = re.sub(r"\D", "", course_num)
        json_file_name = 'CSE' + course_num + '.json'
        if json_file_name in self.json_files:
            course_index = self.json_files.index(json_file_name)
            response_header = 'The credit hours of ' + str(course_num) + ' is '
            value_found=self.courses_info[course_index].get('credits')
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            if value_found is not None:
                return response_header + str(value_found)
            else:
                return 'Sorry, we do not have information about it. Please try another question.'
        else:
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return 'Cannot find the given course number'

    def Course_Description_Of(self, assistant_returned_info):
        if 'course_num' in assistant_returned_info[2]:
            course_num = re.sub(r"\D", "", assistant_returned_info[2].get('course_num'))
        else:
            return 'Can you rephrase your question with more details?'
        #course_num = re.sub(r"\D", "", course_num)
        json_file_name = 'CSE' + course_num + '.json'
        if json_file_name in self.json_files:
            course_index = self.json_files.index(json_file_name)
            response_header = str(course_num) + ' is about '
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return response_header + self.courses_info[course_index].get('description')
        else:
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return 'Cannot find the given course number'

    def Course_Instructor_Of(self, assistant_returned_info):
        if 'course_num' in assistant_returned_info[2]:
            course_num = re.sub(r"\D", "", assistant_returned_info[2].get('course_num'))
        else:
            return 'Can you rephrase your question with more details?'
        course_num = re.sub(r"\D", "", course_num)
        json_file_name = 'CSE' + course_num + '.json'
        if json_file_name in self.json_files:
            course_index = self.json_files.index(json_file_name)
            response_header = 'The instructors of ' + str(course_num) + ' are '
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return response_header + self.courses_info[course_index].get('professors')
        else:
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return 'Cannot find the given course number'

    # def Email_Send_Appointment(email_module, user, question, professor, email):
    #     text = construct_email_appointment(professor, question, user.name)
    #     email_module.send(email, 'Appointment Scheduling', text)
    #     return 'Email Sent!'


    # def Course_Opentime_Of(course_num):
    #     course_num=re.sub(r"\D", "", course_num)
    #     json_file_name='CSE'+course_num+'.json'
    #     if json_file_name in json_files:
    #         course_index=json_files.index(json_file_name)
    #         response_header='The open time of '+str(course_num)+' is '
    #         return response_header+courses_info[course_index].get('open_time')
    #     else:
    #         return 'Cannot find the given course number'

    def Course_Opentime_Of(self, assistant_returned_info):
        if 'course_num' in assistant_returned_info[2]:
            num = re.sub(r"\D", "", assistant_returned_info[2].get('course_num'))
        else:
            return 'Can you rephrase your question with more details?'
        #num = re.sub(r"\D", "", course_num)
        course_num = "CSE " + num
        for course_info in self.courses_info:
            if course_info["title"] != None and course_num in course_info['title']:
                # Clear variable value
                assistant_returned_info[2]['course_num'] = None
                return course_info['open_time']

        not_found_message = "\nThere does not exit course_num in Ohio State University.\n"
        # Clear variable value
        assistant_returned_info[2]['course_num'] = None
        return not_found_message.replace("course_num", course_num)

    def Course_Title_Of(self, assistant_returned_info):
        if 'course_num' in assistant_returned_info[2]:
            num = re.sub(r"\D", "", assistant_returned_info[2].get('course_num'))
        else:
            return 'Can you rephrase your question with more details?'
        #num = re.sub(r"\D", "", course_num)
        course_num = "CSE " + num
        for course_info in self.courses_info:
            if course_info['title'] != None and course_num in course_info['title']:
                # Clear variable value
                assistant_returned_info[2]['course_num'] = None
                return course_info['title']

        not_found_message = "\nThere does not exit course_num in Ohio State University.\n"
        # Clear variable value
        assistant_returned_info[2]['course_num'] = None
        return not_found_message.replace("course_num", course_num)

    def Credit_Course_Is(self, assistant_returned_info):
        if 'credit' in assistant_returned_info[2]:
            credits = re.sub(r"\D", "", assistant_returned_info[2].get('credit'))
        else:
            return 'Can you rephrase your question with more details?'
        courses = []
        if len(credits)>1 :
            credits = credits[0:1]
        print("credits: " + credits + "\n")

        for course_info in self.courses_info:
            if course_info["credits"] != None and credits in str(course_info["credits"]):
                courses.append(course_info["title"][:8])
        if len(courses) == 0:
            not_found_message = "\nThere's no course of $ credit hours.\n"
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return not_found_message.replace("$", credits)
        else:
            course_names = ""
            for course in courses:
                course_names += course
                course_names += ","
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return course_names

    def Instructor_Teaches(self, assistant_returned_info):
        if 'name' in assistant_returned_info[2]:
            name = assistant_returned_info[2].get('name')
        else:
            return 'Can you rephrase your question with more details?'
        courses = []
        first_char = 0
        second_char = 0
        for i in range(len(name)):
            if name[i] == " ":
                second_char = i + 1
                break
        if second_char != 0:
            name = name[:first_char + 1].upper() + name[first_char + 1:second_char] + name[
                                                                                      second_char:second_char + 1].upper() + name[
                                                                                                                             second_char + 1:]
        else:
            name = name[:first_char + 1].upper() + name[first_char + 1:]

        for course_info in self.courses_info:
            if course_info['professors'] != None and name in course_info['professors']:
                courses.append(course_info['title'][:8])
        if len(courses) == 0:
            not_found_message = "\nIt seems $ haven't taught any courses in Ohio State University.\n"
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return not_found_message.replace("$", name)
        else:
            course_names = ""
            for course in courses:
                course_names += course
                course_names += ","
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return course_names

    def Semester_Has_Courses(self, assistant_returned_info):
        if 'semester' in assistant_returned_info[2]:
            semester = assistant_returned_info[2].get('semester')
        else:
            return 'Can you rephrase your question with more details?'
        print(semester + '\n')
        year = re.sub(r"\D", "", semester)
        if len(str(year)) == 2:
            year = "20" + year
        if semester[0] == 'a' or semester[0] == 'A' or semester[0] == 'F' or semester[0] == 'f':
            semester = "Fall " + year
        elif semester[0:3] == "SU" or semester[0:3] == "su" or semester[0:3] == "Su" or semester[0:3] == "sU":
            semester = "Summer " + year
        elif semester[0:3] == "Sp" or semester[0:3] == "sp" or semester[0:3] == "sP" or semester[0:3] == "SP":
            semester = "Spring " + year
        courses = []
        for course_info in self.courses_info:
            if course_info["open_time"] != None and semester in course_info["open_time"]:
                courses.append(course_info["title"][:8])
        if len(courses) == 0:
            not_found_message = "\nNo course opens in $.\n"
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return not_found_message.replace("$", semester)
        else:
            course_names = ""
            for course in courses:
                course_names += course
                course_names += ","
            # Clear variable value
            assistant_returned_info[2]['course_num'] = None
            return course_names