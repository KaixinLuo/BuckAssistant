import os, json, re
path_to_json = 'crawler/courseInformation/Json'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
courses_info=[]
for js in json_files:
    with open(path_to_json + '/' + js) as f:
        courses_info.append(json.load(f))


def Course_Average_Size_Of(course_num):

    course_num=re.sub(r"\D", "", "course_num")
    course_index=json_files.index('CSE'+course_num+'.json')
    return courses_info[course_index].get('average_size')

def Course_Credits_Of(course_num):
    course_num=re.sub(r"\D", "", "course_num")
    course_index=json_files.index('CSE'+course_num+'.json')
    return courses_info[course_index].get('credits')

def Course_Description_Of(course_num):
    course_num=re.sub(r"\D", "", "course_num")
    course_index=json_files.index('CSE'+course_num+'.json')
    return courses_info[course_index].get('description')

def Course_Instructor_Of(course_num):
    course_num=re.sub(r"\D", "", "course_num")
    course_index=json_files.index('CSE'+course_num+'.json')
    return courses_info[course_index].get('professors')

def Course_Opentime_Of(course_num):
    course_num=re.sub(r"\D", "", "course_num")
    course_index=json_files.index('CSE'+course_num+'.json')
    return courses_info[course_index].get('open_time')
