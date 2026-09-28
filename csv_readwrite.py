#CSV READ
import csv
f=open("data.csv","r")

content=csv.reader(f)

for row in content:
    print(row)
f.close()


# write

import csv
f=open("book.csv","w",newline="")
content=[
    ['title','author','place'],
    ['book1','jhon','ekm'],
    ['book2','sam','tvm']
]

writer=csv.writer(f)
# writer.writerows(content)

for row in content:
    writer.writerow(row)
f.close()