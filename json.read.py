###read
import json

f=open("data.json","r")

content=json.load(f)
print(content)
print(content[0])
print(content[0]['name'],content[0]['age'])
print(content[1]['name'],content[1]['age'])
f.close()


import json
f=open("data.json","r")
content=json.load(f)
print(content)
print(content[0])
f.close()


# ##write
content=[
    {"title":"book","author":"john","price":200},
    {"title":"book2","author":"sam","price":300},
]

f=open("books.json","w")

json.dump(content,f)
f.close()