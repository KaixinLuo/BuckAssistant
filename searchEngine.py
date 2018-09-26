import os, json

path_to_json = 'crawler/courseInformation/Json'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
courses_info=[]
for js in json_files:
    with open(path_to_json + '/' + js) as f:
        courses_info.append(json.load(f))

def Course_Opentime_Of(course_num):
    for course_info in courses_info:
        if course_num in course_info["title"]:
            return course_info["open_time"]

    not_found_message = "\nThere does not exit course_num in Ohio State University.\n"
    not_found_message.replace("course_num", course_num)
    return not_found_message
    
def Course_Title_Of(course_num):
    for course_info in courses_info:
        if course_num in course_info["title"]:
            return course_info["title"]

    not_found_message = "\nThere does not exit course_num in Ohio State University.\n"
    not_found_message.replace("course_num", course_num)
    return not_found_message

def Credit_Course_Is(credits):
    courses =[]
    for course_info in courses_info:
        if credits == course_info["credits"]:
            courses.append(course_info["title"][:7])
    if len(courses) == 0:
        not_found_message = "\nThere does not exit course of $ credits.\n"
        not_found_message.replace("$", credits)
        return not_found_message
    else:
        course_names = ""
        for course in courses:
            course_names += course
            course_names += ","
        
        return course_names

def Instructor_Teaches(name):
    courses =[]
    for course_info in courses_info:
        if name in course_info["professors"]:
            courses.append(course_info["title"][:7])
    if len(courses) == 0:
        not_found_message = "\nIt seems $ haven't taught any courses in Ohio State University.\n"
        not_found_message.replace("$", name)
        return not_found_message
    else:
        course_names = ""
        for course in courses:
            course_names += course
            course_names += ","
        
        return course_names
def Semester_Has_Courses(semester):
    courses = []
    for course_info in courses_info:
        if semester in course_info["open_time"]:
            courses.append(course_info["title"][:7])
    if len(courses) == 0:
        not_found_message = "\nNo course opens in $.\n"
        not_found_message.replace("$", semester)
        return not_found_message
    else:
        course_names = ""
        for course in courses:
            course_names += course
            course_names += ","
        
        return course_names
    

    
    

            
