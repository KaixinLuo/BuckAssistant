import requests
import nltk
import re
from bs4 import BeautifulSoup

address = "https://www.coursicle.com/osu/courses/CSE/"

response = requests.get(address)
print (" connection established")
coursesNumber = [re.search(r"[0-9]+/",t).group(0).rstrip('/') for t in re.findall(r"href=\"[0-9]+/\"",response.text)]
response.close()
#print(coursesNumber)


for cid in coursesNumber:
    with open('./courseInformation/CSE'+cid+'.html',"w") as f:
        r = requests.get(address+cid+'/')
        filter = BeautifulSoup(r.text,features="html.parser")
        [s.extract() for s in filter('script')]
        f.write(filter.get_text())
        r.close()
        f.close()

'''
with open('./courseInformation/index',"w") as fp:
    for i in coursesNumber:
        fp.write(i+'\n')
    fp.close()
    
'''



