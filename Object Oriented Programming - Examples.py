# # class Dog:
# #     species = "mamal"
# #     def __init__(self,breed,name):
# #         self.breed = breed
# #         self.name = name
# #
# #
# #
# # # sam = Dog('Lab', 'Sam')
# # # print(sam.breed)
# # # print(sam.name)
# #
# # class Circle:
# #     pi = 3.14
# #     #Circle gets instantiated with a radius
# #     def __init__(self,radius=1):
# #         self.radius = radius
# #         self.area = radius**2 * Circle.pi
# #     #Methon for resetting radius
# #     def setRadius(self,new_radius):
# #         self.radius = new_radius
# #         self.area = new_radius**2 * Circle.pi
# #
# #     def getCircumference(self):
# #         return self.radius * self.pi * 2
# # c = Circle()
# # c.setRadius(2)
# # print('Radius is: ', c.radius)
# # print("Area is :", c.area)
# # print("Circumference is : ", c.getCircumference()
#
# # class Animal:
# #
# #     def __init__(self):
# #         print("Animal class created")
# #     def whoIam(self):
# #         print("I'm an animal ")
# #     def eat(self):
# #         print("I am eating")
# #
# # class Dog(Animal):
# #     def __init__(self):
# #         Animal.__init__(self)
# #     def bark(self):
# #         print("Wouf!")
# #     def eat(self):
# #         print("I am eating food")
# #
# # d = Dog()
# #
# # d.whoIam()
# # d.eat()
# # d.bark()
#
# # class Dog:
# #     def __init__(self,name):
# #         self.name = name
# #
# #     def speak(self):
# #         return  self.name + " says woof"
# #
# # class Cat:
# #     def __init__(self,name):
# #         self.name = name
# #
# #     def speak(self):
# #         return self.name + " says meaw"
# #
# # niko = Dog('Niko')
# # felix = Cat('Felix')
# #
# # print(niko.speak())
# # print(felix.speak())
# #
# #
# # for pet in [niko,felix]:
# #     print(pet.speak())
# #
# #
# # def pet_speak(pet):
# #     print(pet.speak())
# #
# # pet_speak(niko)
# # pet_speak(felix)
#
# # class Animal:
# #     def __init__(self,name):
# #         self.name = name
# #
# #     def speak(self):
# #         raise NotImplementedError("Subclass must implement abstract method")
# #
# # class Dog(Animal):
# #     def speak(self):
# #         return self.name + " says woof"
# #
# # class Cat(Animal):
# #     def speak(self):
# #         return self.name + " says meow"
# #
# # fido = Dog('Fido')
# # isi = Cat('Isis')
# #
# # print(fido.speak())
# # print(isi.speak())
#
# # class Line:
# #
# #     def __init__(self, coor1, coor2):
# #         self.coor1 = coor1
# #         self.coor2 = coor2
# #     def distance(self):
# #         a1,b1 = self.coor1
# #         a2,b2 = self.coor2
# #         return ((b2-b1)**2 + (a2-a1)**2) **0.5
# #     def slope(self):
# #         a1, b1 = self.coor1
# #         a2, b2 = self.coor2
# #         return (b2-b1)/(a2-a1)
# #
# # l = Line((3,2),(8,10))
# #
# # print(l.coor1)
# # print(l.coor2)
# # print(l.distance())
# # print(l.slope())
#
# # class Cylinder:
# #     pi = 3.14
# #     def __init__(self, height=1 , radius = 1):
# #         self.height = height
# #         self.radius = radius
# #     def volume(self):
# #         return Cylinder.pi * self.radius**2 * self.height
# #
# #     def surface_area(self):
# #         top = 3.14 * (self.radius) ** 2
# #         return (2 * top) + (2 * 3.14 * self.radius * self.height)
# #
# # c = Cylinder(2,3)
# # print(c.volume())
# # print(c.surface_area())
#
#
#
#
#
#
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Accout owner: {self.owner} \nAccount ballance is: {self.balance}$'

    def deposit(self, deposit):
        self.balance += deposit
        print(f'Deposit accepted: {deposit}$ \nNow the balance is: {self.balance}')

    def widraw(self,widraw):
        self.widraw=widraw
        if self.widraw <= self.balance:
            print(f'Withdrawal accepted: {self.widraw}$')
        else:
            print("FundsUnavailable!")


acct1 = Account('Jose', 100)
print(acct1)
acct1.deposit(50)
acct1.widraw(155)
# print('Account owner: ',acct1.owner)
# print('Account balance is : $',acct1.balance)
