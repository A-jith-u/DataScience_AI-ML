''' Object Oriented Programming (OOP) is a programming paradigm that uses objects and classes to organize code.
It allows for the creation of reusable and modular code, making it easier to maintain and extend.
In OOP, objects are instances of classes, which define the properties and behaviors of the objects.   
This approach promotes encapsulation, inheritance, and polymorphism, enabling developers to model real-world entities and their interactions effectively.
Always define a class before creating an object of that class.
A class is a blueprint for creating objects, and it defines the attributes and methods that the objects will have.
An object is an instance of a class, and it can access the attributes and methods defined in the class.'''


# student_name1='Ajith'
# student_age1=22
# student_name2='Vishnu'
# student_age2=21
# student_name3='Abhinav'
# student_age3=25
# student_name4='Aakash'
# student_age4=21
# student_name5='Dhanash'
# student_age5=26

# print("Name  Age")
#print('',student_name1, student_age1,'\n',student_name2, student_age2,'\n',student_name3, student_age3,'\n',student_name4, student_age4,'\n',student_name5, student_age5)


#Creating a class Student with the attributes name and age

# class Student:
#     def __init__(self,name,age):      #defining the constructor of the class Student which takes two parameters name and age
#         self.name=name                #making the name parameter as an instance variable of the class Student
#         self.age=age                  #making the age parameter as an instance variable of the class Student


# student1=Student('Ajith',22)   #object of the class Student is created with the name 'Ajith' and age 22.Here student1 is the object of the class Student

# print(student1.name,student1.age)       #Printing the name and age of the student1 object using the instance variables name and age of the class Student

# student2=Student('Aakash',21)
# student3=Student('Jerin',25)
# student4=Student('Vishnu',21)
# student5=Student('Abhinav',25)

# print(student2.name,student2.age)
# print(student3.name,student3.age)
# print(student4.name,student4.age)
# print(student5.name,student5.age)


#class Book
# class Book:
#     def __init__(self,name,author,pageno,year):    #defining the constructor of the class Book which takes four parameters name, author, pageno and year
#         self.name=name                             #making the name parameter as an instance variable of the class Book
#         self.author=author                         #making the author parameter as an instance variable of the class Book
#         self.pageno=pageno                         #making the pageno parameter as an instance variable of the class Book
#         self.year=year                             #making the year parameter as an instance variable of the class Book

# book1=Book('Harry Potter','J.K Rowling',300,1997)         #calling the constructor of the class Book and creating an object of the class Book with the name 'Harry Potter', author 'J.K Rowling', pageno 300 and year 1997
# book2=Book('The Alchemist','paulo coelo',250,1998)
# book3=Book('The Great Gatsby','F. Scott Fitzgerald',200,1995)
# book4=Book('Aadu Jeevitham','Benyamin',150,2010)

# print(book1.name,book1.author,book1.pageno,book1.year)         #Printing the name, author, pageno and year of the book1 object
# print(book2.name,book2.author,book2.pageno,book2.year)
# print(book3.name,book3.author,book3.pageno,book3.year)
#print(book4.name,book4.author,book4.pageno,book4.year)

# class Employee:
#     #class Attribute
#     age=24
#     def __init__(self, name, salary, job_id, job_role, joining_date):  #defining the constructor of the class Employee which takes five parameters name, salary, job_id, designation and joining_date
#         self.name = name
#         self.salary = salary         #instance attribute salary is assigned the value of the parameter salary
#         self.job_id = job_id
#         self.job_role = job_role
#         self.joining_date = joining_date

#     def display_details(self): # defining a method display_details which prints the details of the employee. self should be the first parameter of the method as it refers to the instance of the class Employee
#         print(f"Name: {self.name}, Salary: {self.salary}, Job ID: {self.job_id}, Job Role: {self.job_role}, Joining Date: {self.joining_date}")


# employee1=Employee('Harish',500000,101,'SE','12-05-2019')  #creating an object of the class Employee with the name 'Harish', salary 500000, job_id 101, designation 'SE' and joining_date '12-05-2019'
# employee2=Employee('Suresh',550000,102,'AM','14-1-2018')
# employee3=Employee('Ramesh',650000,110,'Manager','28-05-2016')
# employee4=Employee('Reghu',400000,106,'SD','13-05-2020')
# employee5=Employee('Swathi',380000,112,'Data Analyst','10-10-2024')

# employee1.display_details() # calling the display_details method of the employee1 object to print the details of the employee1
# employee2.display_details() # calling the display_details method of the employee2 object to print the details of the employee2
# employee3.display_details()
# employee4.display_details()
# employee5.display_details()

# print(employee1.age)    #accessing the class attribute age using the object employee1. The output will be 24 as the class attribute age is defined as 24 in the class Employee 
#print(Employee.age)     #accessing the class attribute age using the class name Employee. The output will be 24 as the class attribute age is defined as 24 in the class Employee


# class Student:
#    count=0 #class attribute to keep track of the number of students created
#    def __init__(self,name,age,height):        #defining the constructor of the class Student which takes three parameters name, age and height
#       self.name=name
#       self.age=age
#       self.height=height
#       Student.count+=1          #incrementing the class attribute count by 1 every time a new student object is created

#    def display_student_details(self):
#         print(f"Number of objects created:{Student.count}") #accessing the class attribute count using the class name Student. The output will be 0 as the class attribute count is defined as 0 in the class Student
#         print(f"Name: {self.name}, Age: {self.age}, Height: {self.height}")

# student1=Student('Ajith',22,163)
# student1.display_student_details() # calling the display_student_details method of the student1 object to print the details of the student1

# student2=Student('Adarsh',21,170)
# student2.display_student_details()

# student3=Student('Venu',22,180)
# student3.display_student_details()

# print(Student.count)

#**********************************
#******class inheritance***********
#**********************************

   # class Animal:
   #     def __init__(self,has_legs):
   #         self.has_legs=has_legs

   # class Dog(Animal):                   # Dog is a subclass of Animal. 
   #     pass                             #pass is used to indicate that the Dog class does not have any additional attributes or methods of its own, and it inherits all the attributes and methods from the Animal class.

   # dog=Dog(True)
#print("The dog has 4 legs:",dog.has_legs)

# class Animal:
#     def __init__(self,eat,sleep):
#         self.eat=eat
#         self.sleep=sleep

# class Cat(Animal):
#     def __init__(self,eat,sleep):
#         super().__init__(eat,sleep)
#         self.speak='Meow Meow'

# class Dog(Animal):
#     def __init__(self,eat,sleep):
#         super().__init__(eat,sleep)    #super() is used to call the constructor of the parent class Animal, allowing the Dog class to inherit the attributes eat and sleep from the Animal class.
#         self.speak="Bow Bow"  #speak is an instance variable of the Dog class which is assigned the value "Bow Bow"


# dog=Dog(True,True)
# cat=Cat(True,True)

# print("The dog can eat:",dog.eat,"\nThe dog can sleep:",dog.sleep,"\nThe dog speaks:",dog.speak)
# print("The cat can eat:",cat.eat,"\nThe cat can sleep:",cat.sleep,"\nThe cat speaks:",cat.speak)

# class Animal:
#    def __init__(self,name,age):
#       self.name=name
#       self.age=age
#    def eat(self):
#       print("The animal is eating")

# class Dog(Animal):
#    #def __init__(self,name,age):
#      # super().__init__(name,age)
#      # self.speak="Bow...Bow.."

#    #def dog_info(self):
#       #print(f"The dog's name is {self.name} and his age is {self.age} ")
      
#    def bark(self):
#       return "Bow....Bow..!"

# class Cat(Animal):
#    #def __init__(self,name,age):
#      # super().__init__(name,age)
#       #self.speak="Meow..Meow..."

#    #def cat_info(self):
#       #print(f"The cat's name is {self.name} and his age is {self.age}")

#    def meow(self):
#       #print("The cat says", self.speak)
#       return "Meow...Meow...!"

# dog=Dog('Bob',2)
# cat=Cat('Jack',2)

# print(f"The dog's name is {dog.name} and his age is {dog.age} ")
# print(f"The dog says {dog.bark()}")
# dog.eat()

# print(f"The cat's name is {cat.name} and his age is {cat.age}")
# # cat.cat_info()
# print(f"The cat says{cat.meow()}")


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"The person's name is {self.name} and age is {self.age}")

# class Student(Person):
#     def __init__(self,name,age,course):
#         super().__init__(name,age)
#         self.course=course
#     def show_course(self):
#         print(f"The course of the student is {self.course}")

# student1=Student('Ajith',22, "DS AI/ML")
# student1.display()
# student1.show_course()

#******************************************************
#***********Abstract class and abstract method*********
#******************************************************

from abc import ABC,abstractmethod

# class Bank(ABC): #Bank is an abstract class which inherits from the ABC class of the abc module
    
#     @abstractmethod
#     def deposit(self): #abstract method which is defined in the abstract class Bank. This method does not have any implementation and must be implemented by the subclasses of the Bank class.
#         pass
    
#     @abstractmethod
#     def loan(self):
#         pass
    
# class SBI(Bank):    #SBI is a subclass of the abstract class Bank. It must implement the abstract methods deposit and loan defined in the Bank class.
#    def deposit(self):
#        print("SBI deposit method is called")
    
#    def loan(self):
#         print("SBI loan method is called")
#    def profit(self):
#         print("SBI profit method is called")

# sbi=SBI()
# sbi.deposit()
# sbi.loan()
# sbi.profit()


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius


rectangle=Rectangle(5,10)
print("The area of the rectangle is:",rectangle.area())     

circle=Circle(3)
print(f"The area of the circle is:{circle.area()}")

