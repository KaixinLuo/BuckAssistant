from watson_developer_cloud import SpeechToTextV1
class Speech_To_Text_Component:
    def __init__(self,debug_mode=False):
        self.debug_mode=debug_mode
        f = open("key.txt", "r")
        f1 = f.read().splitlines()
        f.close()
        self.speech_to_text = SpeechToTextV1(
            iam_apikey=f[14],
            url=f[15]
        )
speech_to_text = SpeechToTextV1(
    iam_apikey='{iam_api_key}',
    url='{url}'
)