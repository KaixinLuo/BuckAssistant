from watson_developer_cloud import TextToSpeechV1
class Text_To_Speech_Component:
    def __init__(self,debug_mode=False):
        self.debug_mode=debug_mode
        f = open("key.txt", "r")
        f1 = f.read().splitlines()
        f.close()
        self.text_to_speech = TextToSpeechV1(
            iam_apikey=f[14],
            url=f[15]
        )
    def synthesize(self,string):
        pass