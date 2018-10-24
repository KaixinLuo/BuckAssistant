import os, json, re

from BuckAD.EmailModule import construct_email_appointment
debug_mode=False
path_to_json = 'crawler/courseInformation/Json'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
courses_info=[]
for js in json_files:
    with open(path_to_json + '/' + js) as f:
        courses_info.append(json.load(f))


def Course_Average_Size_Of(course_num):
    course_num=re.sub(r"\D", "", course_num)
    json_file_name='CSE'+course_num+'.json'
    if json_file_name in json_files:
        course_index=json_files.index(json_file_name)
        response_header='The average size of '+str(course_num)+' is '
        return response_header+str(courses_info[course_index].get('average_size'))
    else:
        return 'Cannot find the given course number'

def Course_Credits_Of(course_num):
    course_num=re.sub(r"\D", "", course_num)
    json_file_name='CSE'+course_num+'.json'
    if json_file_name in json_files:
        course_index=json_files.index(json_file_name)
        response_header='The credit hours of '+str(course_num)+' is '
        return response_header+str(courses_info[course_index].get('credits'))
    else:
        return 'Cannot find the given course number'

def Course_Description_Of(course_num):
    course_num=re.sub(r"\D", "", course_num)
    json_file_name='CSE'+course_num+'.json'
    if json_file_name in json_files:
        course_index=json_files.index(json_file_name)
        response_header=str(course_num)+' is about '
        return response_header+courses_info[course_index].get('description')
    else:
        return 'Cannot find the given course number'

def Course_Instructor_Of(course_num):
    course_num=re.sub(r"\D", "", course_num)
    json_file_name='CSE'+course_num+'.json'
    if json_file_name in json_files:
        course_index=json_files.index(json_file_name)
        response_header='The instructors of '+str(course_num)+' are '
        return response_header+courses_info[course_index].get('professors')
    else:
        return 'Cannot find the given course number'

def Email_Send_Appointment(email_module,user,question,professor,email):
    text=construct_email_appointment(professor,question,user.name)
    email_module.send(email,'Appointment Scheduling',text)
    return 'Email Sent!'


# def Course_Opentime_Of(course_num):
#     course_num=re.sub(r"\D", "", course_num)
#     json_file_name='CSE'+course_num+'.json'
#     if json_file_name in json_files:
#         course_index=json_files.index(json_file_name)
#         response_header='The open time of '+str(course_num)+' is '
#         return response_header+courses_info[course_index].get('open_time')
#     else:
#         return 'Cannot find the given course number'

def Course_Opentime_Of(course_num):
    num = re.sub(r"\D", "", course_num)
    course_num = "CSE " + num
    for course_info in courses_info:
        if course_info["title"] != None and course_num in course_info['title']:
            return course_info['open_time']

    not_found_message = "\nThere does not exit course_num in Ohio State University.\n"
    
    return not_found_message.replace("course_num", course_num)
    
def Course_Title_Of(course_num):
    num = re.sub(r"\D", "", course_num)
    course_num = "CSE " + num
    for course_info in courses_info:
        if course_info['title']!=None and course_num in course_info['title']:
            return course_info['title']

    not_found_message = "\nThere does not exit course_num in Ohio State University.\n"
    return not_found_message.replace("course_num", course_num)

def Credit_Course_Is(credits):

    courses =[]
    credits = credits[:len(credits)-1]
    for course_info in courses_info:
        if course_info["credits"] != None and credits in str(course_info["credits"]):
            courses.append(course_info["title"][:8])
    if len(courses) == 0:
        not_found_message = "\nThere does not exit course of $ credit hours.\n"
        
        return not_found_message.replace("$", credits)
    else:
        course_names = ""
        for course in courses:
            course_names += course
            course_names += ","
        
        return course_names

def Instructor_Teaches(name):
    courses =[]
    first_char = 0
    second_char = 0
    for i in range(len(name)):
        if name[i] == " ":
            second_char = i+1
            break
    if second_char !=0:
        name = name[:first_char+1].upper() + name[first_char+1:second_char]+ name[second_char:second_char+1].upper() + name[second_char+1:]
    else :
        name = name[:first_char+1].upper() + name[first_char+1:]

    for course_info in courses_info:
        if course_info['professors'] != None and name in course_info['professors']:
            courses.append(course_info['title'][:8])
    if len(courses) == 0:
        not_found_message = "\nIt seems $ haven't taught any courses in Ohio State University.\n"
        
        return not_found_message.replace("$", name)
    else:
        course_names = ""
        for course in courses:
            course_names += course
            course_names += ","
        
        return course_names
def Semester_Has_Courses(semester):
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
    for course_info in courses_info:
        if course_info["open_time"] != None and semester in course_info["open_time"]:
            courses.append(course_info["title"][:8])
    if len(courses) == 0:
        not_found_message = "\nNo course opens in $.\n"
        
        return not_found_message.replace("$", semester)
    else:
        course_names = ""
        for course in courses:
            course_names += course
            course_names += ","
        
        return course_names
    

    
    

            
