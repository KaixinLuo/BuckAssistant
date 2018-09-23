import json
with open("index","r") as indexes:
    for courseNo in indexes:
        with open("TempText/CSE"+courseNo.rstrip('\n')+".txt","r") as inputFile:
            target = open("./temp2/CSE"+courseNo.rstrip('\n')+".txt","w")
            for (num,line) in enumerate(inputFile):
                if (num%2 ==1 ):
                    target.write(line.replace('\n',":"))
                else:
                    target.write(line)
            target.close()
            inputFile.close()
    indexes.close()

with open("index", "r") as indexes:
    for courseNo in indexes:
        with open("temp2/CSE" + courseNo.rstrip('\n') + ".txt", "r") as inputFile:
            target = open("./Json/CSE" + courseNo.rstrip('\n') + ".json", "w")
            content= {
                "title":None,
                "description":None,
                "credits":None,
                "attributes":None,
                "professors":None,
                "open_time":None,
                "average_size":None,
                "average_sections":None
            }
            for (num, line) in enumerate(inputFile):
                if (num == 0):
                    content["title"] = line
                else:
                    [label,token]=line.split(':',1)
                    if (label == "Description"):
                        content["description"]=token
                    elif(label == "Credits"):
                        content["credits"] = float(token.rstrip())
                    elif(label == "Attributes"):
                        content["attributes"] = token
                    elif (label == "Recent Professors"):
                        content["professors"] = token
                    elif (label == "Recent Semesters"):
                        content["open_time"] = token
                    elif (label == "Offered"):
                        pass
                    elif (label == "Avg. Class Size"):
                        content["average_size"] = int(token.rstrip())
                    elif (label == "Avg. Sections"):
                        content["average_sections"] = int(token.rstrip())
                    else :
                        pass
            json.dump(content,target,indent=4, separators=(',', ': '))
            target.close()
            inputFile.close()
    indexes.close()
