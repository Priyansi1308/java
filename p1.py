t1=(1,2,3,4,5,5,6)
t2=(7,8,9)
l1=[10,20,30,40]
print(t1[1])
print(t1[2:5])
print(len(t1))
print(t1+t2)
print(t1.count(5))
print(*t1)
print(min(t1))
print(max(t1))
print(min(t2))
print(max(t2))
print(sorted(t1))
print(tuple(l1))

class student :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
s1=student("riya",23)
s1.display()

class product:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price
    def display2(self):
        print("pname:",self.pname)
        print("price:",self.price)
s3=product("TV",15000)
s3.display2()        

class ATM:
    def __init__(self,__balance):
        self.__balance=__balance
    def deposite(self,amount):
        self.__balance+=amount
    def display(self):
        print("current balance:",self.__balance)
a=ATM(50000)
a.deposite(500)
a.display()

#inheritance      
class Parent:
    def parent(self):
        print("from parent class")
class Child(Parent):        
    def child(self):
        print("from child class")
c=Child()
c.child()
c.parent()                