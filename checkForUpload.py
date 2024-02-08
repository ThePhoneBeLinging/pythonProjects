import requests
# Making a GET request
r = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCIoxBbxCTaoYcwsSowTIsVA&maxResults=5&order=date&type=video&key=AIzaSyCLF1ucUAwxmBXvsFsyh_wEJAXfSBN8iJQ')
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(type(r.text))

file1 = open("videos.txt", "w")
file1.write(str(r.text))
file1.close() 
