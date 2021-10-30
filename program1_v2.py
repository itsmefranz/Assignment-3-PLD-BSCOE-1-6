
def getName():
    _name= input("Name: ")
    return _name 

def getAge():
    _age= input("Age: ")
    return _age

def getAddress():
    _add= input("Address: ")
    return _add

def display(nameF, ageF, addF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addF}.")

#steps
#1. ask for name then save as variable
name= getName()
#2. ask for age then save as variable
age= getAge()
#3. ask for address then save as variable
address= getAddress()
#4. display the details

display(name, age, address)