import json
import urllib

x = urllib.urlopen("http://course.us.to/school.json")
y = x.read()
#print(y)
z = json.loads(y)
longList = []

for eachClass in z:
    url = "http://course.us.to/school/"+eachClass['name']+".json"
    print url
    lists = urllib.urlopen(url)
    result = json.loads(lists.read())
    for eachThing in result:
        school = eachClass['name']
        name = eachThing["name"]
        longList.append(school+" "+name)

f = open("listfile.txt",'w')
#print(longList)
for eachitem in longList:
    f.write(eachitem)
    f.write("\r\n")
f.close()
