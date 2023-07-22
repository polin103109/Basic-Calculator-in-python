
class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Ask the user for input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Creating an instance of the myClass
p1 = myClass(name, age)

# Now you can use the p1 object to access the attributes of the myClass instance:
print(f"Name: {p1.name}")
print(f"Age: {p1.age}")