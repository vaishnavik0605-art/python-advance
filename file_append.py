###append####
# f=open("k.txt","a")
# f.write("morning")
# f.close()


#write a prgrm to append the content from one file into another text file

# f1 = open("k.txt", "r")
# f2 = open("a.txt", "a")
# data = f1.readlines()
# for i in data:
#     f2.write(i)
# f1.close()
# f2.close()

# f=open("k.txt","r")
# s=f.read()
# f.close()
#
# f=open("a.txt",'a')
# f.write(s)
# f.close()

# f=open("k.txt","a+")
# f.write("python")
# s=f.read()
# print(s)


####3 to display the appendted content

# f=open("k.txt","a+")
# print("first position",f.tell())  #returns the current file pointer
# f.write("python")
#
# print("second  position",f.tell())
# f.seek(0)  ##change the file pointer position
#
# print("third  position",f.tell())
# s=f.read()
# print(s)
# f.close()



##### to remove a file
import os
os.remove("a.txt")
print("the file is deleted")

