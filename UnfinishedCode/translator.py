
from watson_developer_cloud import LanguageTranslatorV3
import json

src_lang = 'en'
tgt_lang = 'ja'
language_translator = LanguageTranslatorV3(
    version='2018-08-23',
    iam_api_key=trans_crn['apikey'],
    url=trans_crn['url']
)
src_lang = input("Please enter your mother tone, Blyat (you'd better enter en): ")
if src_lang == 'en':
    tgt_lang = input("Please enter your target lang, Blyat (you'd better enter zh): ")
    if tgt_lang == 'zh':
        pass
    else:
        print ("Cyka, nuclear missle luanch")
        exit(1) 
else:
    print ("Cyka, nuclear missle luanch")
    exit(1)
print ("put your sentence now")
while True:
    s = input(">")
    translation = language_translator.translate(
    text=s,
    model_id=src_lang+'-'+tgt_lang)
    print(translation['translations'][0]['translation'])