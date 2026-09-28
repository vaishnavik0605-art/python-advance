# class Employee:
#     def __init__(self):
#         print("enter the details")  # used to initialize object properties
#         self.empid=int(input("enter your id"))
#         self.name=input("enter your name")
#         self.age=int(input("enter your age"))
#         self.salary=int(input("enter your salary"))
#         self.designation=input("enter your designation")
#
#     def getsalary(self):
#         print("salary",self.salary)
#
#     def showpersondetails(self):
#         print("employee name",self.name,"employee age",self.age)
# emp=Employee()
# emp.getsalary()
# emp.showpersondetails()



###define a class  named student with attributes rollno,name,mark1,mark2,mark3
#and method display() to display roll number and total mark of a student
#create a student object and call the method

# class Student():
#     def __init__(self):
#         self.rollno=int(input("enter rollno"))
#         self.name=input("enter name")
#         self.mark1=int(input("enter mark1"))
#         self.mark2 = int(input("enter mark2"))
#         self.mark3 = int(input("enter mark3"))
#
#     def display(self):
#         print("roll no",self.rollno)
#         print("total mark of student",self.mark1+self.mark2+self.mark3)
# st=Student()
# st.display()



###create a class named book with attributes title,author,price,pages,language and method
##gettitle(),getauthor(),getprice()
##settitle(),setauthot(),setprice()
#create book objects and call the methods

# class Book():
#     def __init__(self):
#         self.title=input("enter title:")
#         self.author =input("enter author:")
#         self.price = int(input("enter price:"))
#         self.pages =int(input("enter no.of pages:"))
#         self.language = input("enter language:")
#
#     def gettitle(self):
#         print("title",self.title)
#
#     def getauthor(self):
#         print("author",self.author)
#
#     def getprice(self):
#         print("price",self.price)
#
#     def settitle(self):
#         self.title=input("enter new title")
#         self.gettitle()
#
#     def setauthor(self):
#         self.author=input("enter new author")
#         self.getauthor()
#
#     def setprice(self):
#         self.price=input("enter new price")
#         self.getprice()
#
#         ###self.attribute()
#         ##self.method()
# b=Book()
# b.gettitle()
# b.getauthor()
# b.getprice()
#
# ###objectname.attributename()
# #objectname.methodname()
# b.settitle()
# b.setauthor()
# b.setprice()



##create a class named account with attributes accname,accno,balance and method withdraw()
#depost(),showbalance()  create an account object and call the methods




class Account:
    def __init__(self):
        self.acctname = input("Enter account name: ")
        self.acctnumber = int(input("Enter account number: "))
        self.balance = int(input("Enter initial balance: "))

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def showbalance(self):
        print("Balance:", self.balance)
#
#
a = Account()
a.showbalance()

a.deposit()
a.showbalance()

a.withdraw()
a.showbalance()






# class Account():
#     def __init__(self):
#         self.accname=input("enter name:")
#         self.accno=int(input("enter acc no:"))
#         self.balance=int("enter balance")
#
#     def withdraw(self):
#         amount=int(input("enter amount"))
#         if amount>self.balance:
#             print("insufficient balance")
#         else:
#             self.balance=self.balance-amount
#             self.showbalance()
#
#     def deposit(self):
#         amount = int(input("enter amount"))
#         self.balanc=self.balance+amount
#         self.showbalance()

#     def showbalance(self):
#         print("current balance",self.balance)
#
# a1=Account
# # a2=Account
# a1.withdraw()
# a1.deposit()
# a1.showbalance()

# l=[a1,a2]
# for i in l:
#     print(i.accname)