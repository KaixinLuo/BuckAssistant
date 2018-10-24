from modules.module_pipeline import Module_Pipeline
mp=Module_Pipeline(False)
def test_db_search():
    assistant_returned_info=['Course_Average_Size_Of',True,{'course_num':'5914'},'']
    assert mp.process(assistant_returned_info)=='The average size of 5914 is 30','Error in pipeline, db_search, Course_Average_Size_Of'

    assistant_returned_info = ['Course_Credits_Of', True, {'course_num': '5914'}, '']
    assert mp.process(assistant_returned_info) == 'The credit hours of 5914 is 4', 'Error in pipeline, db_search, Course_Credits_Of'

    # assistant_returned_info = ['Course_Description_Of', True, {'course_num': '5914'}, '']
    # print (mp.process(assistant_returned_info))
    # assert mp.process(assistant_returned_info) == '5914 is about Capstone design project; conceptual and technical design; theory and practice of knowledge-based systems; teamwork, written and oral communication skills.Prereq: 2501 (601) or 5501, and 3901 (560) or 3902 or 3903, and 3521 (630) or 5521. Not open to students with credit for 731. Class Notes: If you are trying to get on the waitlist, but can\'t (because the pre-reqs are enforced), contact Kitty Reeves.92.\n', 'Error in pipeline, db_search, Course_Description_Of'

    assistant_returned_info = ['Course_Instructor_Of', True, {'course_num': '5914'}, '']
    assert 'Stephen Boxwell' in mp.process(assistant_returned_info), 'Error in pipeline, db_search, Course_Instructor_Of'

    assistant_returned_info = ['Course_Opentime_Of', True, {'course_num': '5914'}, '']
    assert 'pring 2019, Fall 2018, Spring 2018, Fall 2017' in mp.process(assistant_returned_info), 'Error in pipeline, db_search, Course_Opentime_Of'

    assistant_returned_info = ['Course_Title_Of', True, {'course_num': '5914'}, '']
    assert 'CSE 5914 - Capstone Design: Knowledge-Based Systems' in mp.process(assistant_returned_info), 'Error in pipeline, db_search, Course_Title_Of'

    assistant_returned_info = ['Instructor_Teaches', True, {'name': 'Stephen Boxwell'}, '']
    assert 'CSE 5914' in mp.process(assistant_returned_info), 'Error in pipeline, db_search, Instructor_Teaches'
    return True