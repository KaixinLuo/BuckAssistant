import requests
import re
address = "https://cse.osu.edu/about-us/"

targets = [
    'faculty',
    'clinical-faculty',
    'faculty/lecturers',
    'part-time-lecturers',
    'courtesy-appointments',
    'emeritus-faculty'
]
result = []
for t in targets:
    r = requests.get(address+t)
    result += [i for i in re.findall(r"[a-z]+\.[1-9]+",r.text,flags=0)if i not in result]

print (list(set(result)))
