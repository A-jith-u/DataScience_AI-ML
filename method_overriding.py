
# class Animal:
#     def move(self):
#         print("Animal walks")

# class Frog(Animal):
#     def move(self):
#         print("Frog Jump")
    

# frog=Frog()
# frog.move()

class Animal:
    def sound(self):
        print("Animal makinig sound")

class Cat(Animal):
    def sound(self):
        print("Meow..")

class Dog(Animal):
    def sound(self):
        print("woff..")

cat=Cat()
dog=Dog()
cat.sound()
dog.sound()



class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        print("Car start using key")

class Electric_bike(Vehicle):
    def start(self):
        print("Bike start using push button")

bike=Electric_bike()
car=Car()
bike.start()
car.start()

