print("menu driven program")
print("1.File Read")
print("2.File Write")
print("3.File Append")
print("4.File Search")
print("5.File delete")
print("6.exit")
def fileread():
    try:
        filename = input("Enter filename")
        f = open(filename, 'r')
        s = f.read()
        print(s)
        f.close()
    except:
        print("enter a valid filename")


def filewrite():
    filename = input("Enter filename")
    f = open(filename, 'w')
    d=input("enter the data")
    f.write(d)
    # f=open("k.txt","r")
    print(f.write())
    f.close()

def fileappend():
    filename = input("Enter filename")
    f = open(filename, 'a+')
    s=input("enter data")
    f.write(s)
    f.close()

def filesearch():
    try:
        filename = input("Enter filename")
        f = open(filename, 'r')
        s=input("enter search element")
        a=f.read()
        if s in a:
            print("word is found")
        else:
            print("word is not found")
        f.close()
    except:
        print("file does not found")

def filedelete():
    try:
        filename = input("Enter filename")
        import os
        os.remove(filename)
    except:
        print("file does not found")


while (True):
    ch=int(input("enter your choice:"))
    if ch==1:
        fileread()

       # f=open("k.txt","r")
       # r=f.read()
       # print(r)
       # f.close()
    elif ch==2:
        filewrite()
    elif ch==3:
        fileappend()
    elif ch==4:
        filesearch()
    elif ch==5:
        filedelete()
    elif ch==6:
        exit()
    else:
        print("enter a valid option")
