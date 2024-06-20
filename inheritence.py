class Animal:
    def speak(self):
        print('Animal is speaking')
class Dog(Animal):
    def bark(self):
        print('Dog is barking')
class Cat(Animal):
    def meow(self):
        print('Cat is meowing')
class Cow(Animal):
    def moo(self):
        print('Cow is mooing')
d=Dog()
d.bark()
c=Cat()
c.meow()
d.speak()
w=Cow()
w.moo()