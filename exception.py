# from math import factorial
import math
from xml.parsers import expat


# try:
#
#
#     n=int(input("enter a number:"))
#     n1=int(input("enter a number:"))
#     d=n//n1
#
# except ValueError:
#     print("Value error")
#
# except ZeroDivisionError:
#     print("zero division error")
# except:
#     print("error")
#
# else:
#     print("result=",d)
#
# finally:         ######### it will always executed whether except / else block executes at end of execution
#     print("completed")



###########hw#################

# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
#
# while(1):
#     try:
#         n=int(input("enter a number:"))
#         f=math.factorial(n)
#
#     except ValueError:
#         print("value error")
#     else:
#         print("factorial",f)
#         exit()

########### with fn infinite loop  after value error user have to enter a number to check factorial ###################

# def fact():
#     try:
#         n = int(input("enter a number:"))
#         f = math.factorial(n)
#
#     except ValueError:
#         print("value error")
#         fact()     ###recursion --->fn call itself its fn  ##########
#     else:
#         print("factorial", f)
#         exit()
#
# fact()


# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.


# def opr(n1,n2):
#     a=n1+n2
#     print("ADDITION",a)
#
# def sub(n1,n2):
#     s=n1-n2
#     print("SUBSTRACTION",s)
#
# def mul(n1,n2):
#     m=n1*n2
#     print("MULTIPLICATION",m)
#
# def div(n1,n2):
#     d=n1/n2
#     print("DIVISION",d)
#
# def ex():
#     exit()
#
# try:
#     while(1):
#         ch=int(input("\n1.ADDITION \n2.DIVISION \n3.SUBSTRACTION \n4.MULTIPLICATION \n5.EXIT \nENTER YOUR CHOICE:"))
#         if ch==5:
#             ex()
#         n1=int(input("Enter a number1:"))
#         n2= int(input("Enter a number2:"))
#         if ch==1:
#             opr(n1,n2)
#         elif ch==2:
#             div(n1,n2)
#         elif ch==3:
#             sub(n1,n2)
#         elif ch==4:
#             mul(n1,n2)
#         # elif ch==5:
#         #     ex()
#         else:
#             print("enter a valid choice")
#
#
# except ValueError:
#     print("ValueError")
#
# except ZeroDivisionError:
#     print("ZeroDivisionError")
#
# finally:
#     print("CALCULATED")
#
#   ################## WHITHOUT FUNCTION ####################3
#
# try:
#     while(1):
#
#         print("1.ADDITION \n2.DIVISION \n3.SUBSTRACTION \n4.MULTIPLICATION \n5.EXIT")
#         ch=int(input("Enter your choice:"))
#         if ch==5:
#             break
#
#         a=float(input("Enter a number1:"))
#         b=float(input("Enter a number2:"))
#
#
#         if ch==1:
#             print("ADDITION:",a+b)
#         elif ch==2:
#             print("DIVISION",a/b)
#         elif ch==3:
#             print("SUBSTRACTION",a-b)
#         elif ch==4:
#             print("MULTIPLICATION",a*b)
#         else:
#             print("Enter a valid choice")
#         print()
#
# except ValueError:
#         print("enter a valid value")
#
# except ZeroDivisionError:
#         print("its a ZeroDivisionError")
#
# finally:
#         print("COMPLETED")





# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

# try:
#     f=open('file.txt','r')
#     # f = open('k.txt', 'r')   ###3 file doesn't found
#     print(f.read())
# except FileNotFoundError:
#     print("file does not exist")
#
# else:
#     print("file opened")


#Given a Dictionary
#
#
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist


# d={"name":"arun","age":23,"place":"ekm"}
# try:
#     k=input("Enter a Key:")
#     # if k in d:
#     print("Value=",d[k])
# except KeyError:
#     print("key doesn't found")
#
# finally:
#     print("done")

 ############ exception system generated###########

# try:
#
#
#     n=int(input("enter a number:"))
#     n1=int(input("enter a number:"))
#     d=n//n1
#     print("result=", d)
#
# except ValueError as e:
#     print(e)
#
# except ZeroDivisionError as z:
#     print(z)
# except Exception as c:
#     print(c)
#
# else:
#     pass

##################-----------------raise------------##################333
# try:
#     n=int(input("enter age:"))
#     if n<18:
#         raise ValueError("not eligile for voting")
#     else:
#         print("eligible")
#
# except Exception as e:
#     print(e)



 # for coustom exception define class

class Myexception(Exception):
    pass

try:
    n=int(input("enter age:"))
    if n<18:
        raise Myexception("not eligile for voting")
    else:
        print("eligible")

except Myexception as e:
    print(e)