#read() returns string format
#readlines() return list format
f=open('k.txt','r')

s=f.read()
print(s)
print(type(s))   ### returns str format

s=f.readlines()
print(s)
print(type(s))   #### returns list format
    # according to our requirement we can choose any of them

f.close()