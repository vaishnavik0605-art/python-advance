##write

f=open('k.txt','w')   #if file exists it will erase the file contents and returns its reference to f

                      #else it will create a new empty file and returns its reference to f

f.write("hello\n")  #string(inputting format)

f.writelines(['hello\n','python\n'])  #list  #multiple lines inputting
f.close()