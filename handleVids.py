import requests

videoID = "J1sfsxUDaVM"

videosFile = open("videos.txt" ,"r")

fullFile = videosFile.readlines()

titles = []
ids = []

for i in range (0,len(fullFile)):
    workingString = fullFile[i]
    #print(workingString)
    if "title" in workingString:
        workingString = workingString.replace('"title": ','')
        workingString = workingString.replace('"','')
        workingString = workingString.replace(',','')
        print(workingString)
        titles.append(workingString)
    if "videoId" in workingString:
        workingString = workingString.replace('"videoId": ','')
        workingString = workingString.replace('"','')
        ids.append(workingString)
        print(workingString)
    
videosFile.close()

req = requests.get("https://www.youtube.com/shorts/n-BKnpqgZak")# + videoID)

print(req)