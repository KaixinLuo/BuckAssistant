with open("index","r") as indexes:
    for courseNo in indexes:
        with open("CSE"+courseNo.rstrip('\n')+".html","r") as inputFile:
            target = open("./TempText/CSE"+courseNo+".txt","w")
            for (num,line) in enumerate(inputFile):
                if (num>=52 and line !="\n"):
                    target.write(line.replace('\t',""))
            target.close()
            inputFile.close()
    indexes.close()

