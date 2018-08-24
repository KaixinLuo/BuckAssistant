trans_crn={
  "apikey": "w4FPkSm4kp47hFH9NVQeHjt8KSlUF1Tlqz2O-iVFjHJp",
  "iam_apikey_description": "Auto generated apikey during resource-key operation for Instance - crn:v1:bluemix:public:language-translator:us-east:a/2a9e67fa0908487998d77534954c99b7:b020b9e0-6653-44c9-91a3-1a0e428cff75::",
  "iam_apikey_name": "auto-generated-apikey-3020b160-9570-4ced-adcf-ec0811a9d7b3",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/2a9e67fa0908487998d77534954c99b7::serviceid:ServiceId-dd5bd223-d5f1-4372-8cfb-4ebbbb4e28c7",
  "url": "https://gateway-wdc.watsonplatform.net/language-translator/api",
}

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