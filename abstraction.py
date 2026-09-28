from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self):
#         self.l=int(input("enter length:"))
#         self.b=int(input("enter breadth:"))
#
#     def get_area(self):
#         print("AREA OF RECTANGLE:",self.l*self.b)
#
#     def get_perimeter(self):
#         print("PERIMETER OF RECTANGLE:",2*(self.l+self.b))
#
#     # def get_area(self):                            __init__() is mainly used when you want the
#                                    # object's data to be initialized immediately when the object is created.
#     #     self.l=int(input("enter length:"))
#     #     self.b=int(input("enter breadth:"))
#     #     print("AREA OF RECTANGLE:",self.l*self.b)
#     #
#     # def get_perimeter(self):
#     #     print("PERIMETER OF RECTANGLE:",2*(self.l*self.b))
#
#
#
# class Square(Shape):
#     def __init__(self):
#         self.s = int(input("enter side:"))
#
#     def get_area(self):
#         print("AREA OF SQUARE:",self.s*self.s)
#
#     def get_perimeter(self):
#         print("PERIMETER OF SQUARE",4*self.s)
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
# print()
# s=Square()
# s.get_area()
# s.get_perimeter()


#create an abstract class Employee with an abstract method calculate_salary()
# create two sub classes
# full time employee
# part time employee
# each class should calculate salary differently

# each employee
#      common properties-->empid,name,age
# full time employee
#       additional property-->monthly_salary
# part time employee
#       additional properties-->hours ,rate


# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
#
# class Fulltimeemployee(Employee):
#     def __init__(self):
#         self.id=int(input("enter id:"))
#         self.n=input("enter name:")
#         self.a=int(input("enter age:"))
#         self.s=int(input("enter salary:"))
#
#     def calculate_salary(self):
#         print("EMPLOYEE ID:",self.id)
#         print("EMPLOYEE NAME:",self.n)
#         print("EMPLOYEE AGE:",self.a)
#         print("EMPLOYEE SALARY:",self.s)
#
#
#
# class Parttimeemployee(Employee):
#     def __init__(self):
#         self.id = int(input("enter id:"))
#         self.n = input("enter name:")
#         self.a = int(input("enter age:"))
#         self.h = int(input("enter hour:"))
#         self.r = int(input("enter rate:"))
#
#
#
#     def calculate_salary(self):
#         print("EMPLOYEE ID:",self.id)
#         print("EMPLOYEE NAME:",self.n)
#         print("EMPLOYEE AGE:",self.a)
#         print("EMPLOYEE SALARY:",self.h*self.r)
#
# f=Fulltimeemployee()
# f.calculate_salary()
#
# print()
# p=Parttimeemployee()
# p.calculate_salary()




from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self):
        self.empid=input("ENTER EMPLOYEE ID: ")
        self.name=input("ENTER EMPLOYEE NAME: ")
        self.age=int(input("ENTER EMPLOYEE AGE: "))
    @abstractmethod
    def calculate_salary(self):
        pass

class Full_time_employee(Employee):
    def __init__(self):
        super().__init__()   #### init fn of parent class
        self.sal=int(input("ENTER THE SALARY : "))
    def calculate_salary(self):
        print("FULL__TIME__EMPLOYEE\n")
        print("EMPLOYEE ID: ",self.empid,"\n EMPLOYEE NAME: ",self.name,"\nEMPLOYEE AGE: ",self.age,"\nSALARY: ",self.sal)



class Part_time_employee(Employee):

    def __init__(self):
        super().__init__()
        self.hour=int(input("ENTER THE HOUR: "))
        self.rate=int(input("ENTER RATE/HOUR: "))
    def calculate_salary(self):
        print("PART__TIME__EMPLOYEE\n")
        print("EMPLOYEE ID: ", self.empid, "\nEMPLOYEE NAME: ", self.name, "\nEMPLOYEE AGE: ", self.age, "\nSALARY: ",
              self.hour*self.rate)
f=Full_time_employee()
f.calculate_salary()
p=Part_time_employee()
p.calculate_salary()