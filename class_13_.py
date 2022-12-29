class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
# d = Dog()
# d.bark()
# d.speak()
class cat(Dog,Animal):
    def abc(Self):
        print("cat class")
c = cat()        
c.abc()
c.speak()
c.bark()