class myClass:
    def _int_(self,name,age):
        self.name = name
        self.age = age
    
name = input("enter ur name:")
age = input("enter ur age:")
p1 = myClass(name, age)
print(p1.name)
print(p1.age)
