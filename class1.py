class person:
    def __init__(self, n, a):      ########## any doudt abt fn's/keywords are specified in class2.py check there if any#################

      self.name=n
      self.age=a

    def show(self):
       print(self.name,self.age)

p1=person("arun",23)
p1.show()

p2=person("amal",25)
p2.show()