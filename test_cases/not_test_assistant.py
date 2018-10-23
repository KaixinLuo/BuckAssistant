from assistant import Assistant
assistant1 = Assistant(False)

def test_process_input_single_response():
    inputstr = 'test'
    result=assistant1.process_input(inputstr)
    assert result[0]=='Test_Intent','Error in test_assistant, test_process_input_single_response: intent'
    assert result[1], 'Error in test_assistant, test_process_input_single_response: flag'
    assert result[2].get('user_input')=='test', 'Error in test_assistant, test_process_input_single_response: context variable'
    assert result[3]==inputstr+' received', 'Error in test_assistant, test_process_input_single_response: flag'
    return True

def test_process_input_sequential_response():
    #Round 1
    inputstr='testseq'
    result=assistant1.process_input(inputstr)
    assert result[0] == 'Test_Intent_Sequential', 'Error in test_assistant, test_process_input_single_response: intent'
    assert not result[1], 'Error in test_assistant, test_process_input_single_response: flag'
    assert result[2].get(
        'user_input') == 'test', 'Error in test_assistant, test_process_input_single_response: context variable'
    assert result[3] == 'Test entity not found', 'Error in test_assistant, test_process_input_single_response: flag'
    #Round 2
    inputstr = 'entityfortesting'
    result = assistant1.process_input(inputstr)
    assert result[0] == 'No_Intent', 'Error in test_assistant, test_process_input_single_response: intent'
    assert result[1], 'Error in test_assistant, test_process_input_single_response: flag'
    assert result[2].get(
        'entity_for_testing') == 'entityfortesting', 'Error in test_assistant, test_process_input_single_response: context variable'
    assert result[3] == 'Test entity received', 'Error in test_assistant, test_process_input_single_response: flag'
    return True
