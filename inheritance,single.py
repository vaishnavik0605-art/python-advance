# class Parent:
#     def m1(self):
#         print("in parent class method m1")
#     def m2(self):
#         print("in parent class method m2")
# # p=Parent()
# # p.m1()
# # p.m2()
#
# class Child(Parent):
#     def m3(self):  ##own attribute
#         print("in child class method m3")
#     def m1(self):    ##method overriding--->> used to modify/extend the parent functionality
#         super().m1()    ### to
#         print("in child class method m1")
#
#
# c=Child()
# c.m1()
# c.m2()
# c.m3()




# class Person:
#     def __init__(self):
#         self.name=input("enter name:")
#         self.age=int(input("enter age:"))
#
#     def show(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#
#
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()    ###call init of parent(person class)
#         self.rollno=int(input("enter rollno:"))
#         self.mark=int(input("enter mark:"))
#     def show(self):
#         super().show()
#         print("rollno",self.rollno)
#         print("mark",self.mark)
#
#     def updatemark(self):
#         self.mark=int(input("enter new mark:"))
#
#
#
# s=Student()
# s.show()
# s.updatemark()
# print()
# print("updated details")
# s.show()



# class Category:
#     def __init__(self):
#         self.category=input("enter category")
#     def showcategory(self):
#         print("category",self.category)
#
#
#
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.price=int(input("enter price"))
#         self.quantity=int(input("enter quantity"))
#     def totalprice(self):
#         print("total price",self.price*self.quantity)
#
# p=Product()
# p.totalprice()
# p.showcategory()
#


class Company:
    def __init__(self):
        self.cname=input("enter company name:")
        self.loc=input("enter company location:")
    def displaycompany(self):
        print("company name",self.cname)
        print("company location",self.loc)

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empname=input("enter name:")
        self.salary=int(input("enter salary:"))
    def details(self):
        print("Employee name",self.empname)
        print("salary",self.salary)

    def updatesalary(self):
        self.salary=self.salary+(self.salary*0.1)
        print("updated salary",self.salary)


e=Employee()
e.displaycompany() 
e.details()
e.updatesalary()
