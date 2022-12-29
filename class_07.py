'''
class Person:
    age=10

    def greet(self):
        print("hello")
p =Person()
print(p.age)
print(Person.greet)
print(p.greet)'''

class Dog:
    animal = "Dog"

    def __init__(self,breed,color):
        self.breed = breed
        self.color = color

Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print("Rodger details:")
print("Rodger is a ", Rodger.animal)
print("color: ", Rodger.color)

print("\nBuzo Details:")
print("Buzo is a" , Buzo.animal)
print("Breed:", Buzo.breed)
print("color: ", Buzo.color)
