# class Hospital:
#     def __init__(self):
#         self.hos_name=input("enter hospital name:")
#         self.loc=input("enter the location:")
#         self.ph=int(input("enter ph no: "))
#     def display_hospital(self):
#         print("Hospital name:",self.hos_name)
#         print("Hospital location:",self.loc)
#         print("contact:",self.ph)
#
# class Department:
#     def __init__(self):
#         self.dept_name=input("enter department name:")
#         self.doc_name=input("enter doctor name:")
#     def display_dep(self):
#         print("DEPARTMENT NAME",self.dept_name)
#         print("DOCTOR NAME",self.doc_name)
#
#
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.p_name=input("enter patient name:")
#         self.age=int(input("enter age:"))
#         self.gender=input("enter gender:")
#         self.phone=int(input("enter ph no:"))
#         self.adm_date=input("enter admission date:")
#         self.bed_no=int(input("enter bed no:"))
#         self.discharge_date=" "
#     def setdischarge(self):
#         self.discharge_date=input("enter discharge date:")
#
#     def full_summary(self):
#         Hospital.display_hospital(self)
#         Department.display_dep(self)
#         print("PATIENT NAME:",self.p_name)
#         print("PATIENT AGE:", self.age)
#         print("PATIENT GENDER:", self.gender)
#         print("PATIENT CONTACT:", self.phone)
#         print("PATIENT ADMISSION DATE:", self.adm_date)
#         print("PATIENT BED_NO:", self.bed_no)
#         if self.discharge_date==" ":
#             print("not yet discharged")
#         else:
#             print("PATIENT DISCHARGE DATE:", self.discharge_date)
#
#
# p=Patient()
# print()
# p.full_summary()
# print()
# p.setdischarge()
# print()
# p.full_summary()


######method overriding#############
class A:
    def f(self):
        print("in first fn f")

    def f(self,a):
        print("in second fn f")

    def f(self,a,b):
        print("in third fn f")           ####endly defined code is taken  here the last one

a=A()
a.f(2,3)
# a.f(2)
# a.f(1,2)

