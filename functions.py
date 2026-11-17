#*********************************
#********functions****************
#*********************************

'''functions are blocks of code that are designed to do one specific job.
Define a function using the def keyword, followed by the function name and parentheses.
A function should have a descriptive name that indicates what the function does.
 A function body should be indented and contain the code that performs the task of the function.
Functions can take parameters, which are values that are passed into the function when it is called.
while we define input variables in the function definition, we are creating  new variables withs scope withing the function'''

#function to add two numbers
def display_sum(num1,num2):
    print(f"The sum of {num1} and {num2} is:",num1+num2)
    #return(num1+num2)             #returning the sum of the two numbers



#display_sum(num1,num2)           #Invoking or calling the function
#print(display_sum(num1,num2))    #Invoking or calling the function and printing the return value from the function
#display_sum("happy","diwali")    #Invoking or calling the function with direct values

def display_sum_custom():
    print("We will display the sum of two numbers you enter")
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    display_sum(num1,num2)

#display_sum_custom()              #Calling the function to display sum of two numbers entered by user

def greeting_user():               #defining a function to greet the user
    name=input("Enter your name: ")   #taking the name of the user as input
    print(f"Hi, {name}\nGood Afternoon\nHow are you?")   #displaying the greetings
 
#greeting_user()           #calling the function to greet the user


#multiplication table

#num=int(input("Enter the number to display its multiplication table: "))

# for i in range(1,11):
#     print(f"{i}x{num}={i*num}")


#function to display multiplication table of any number

def display_multiplication_table():
    number=int(input("Enter the number to display its multiplication table: "))
    print("***************************************")
    print(f"The multiplication table of {number}")
    print("***************************************")
    i=1
    while i<=10:
     print(f"{i}x{number}={i*number}")
     i+=1
    print("***************************************")

#display_multiplication_table()

# subject_marks=[60,78,69,70]
# total_marks=0
# for i in range(len(subject_marks)):
#     total_marks+=subject_marks[i]
# print(f"Total marks scored ={total_marks}")

# def subjects_sum(sub1,sub2,sub3,sub4,sub5):
#    total_marks=sub1+sub2+sub3+sub4+sub5
#    #print(f"The total marks is:{total_marks}")
#    return (total_marks)

# def subjects_average(total_marks):
#     average_marks=total_marks/5
#     return average_marks

# def first_largest_score(sub1,sub2,sub3,sub4,sub5):
#     if(sub1>sub2 and sub1>sub3 and sub1>sub4 and sub1>sub5):
#         print(f"subject sub1 has largest score" )
#     elif(sub2>sub1 and sub2>sub3 and sub2>sub4 and sub2>sub5):
#         print(f"subject sub2 has largest score" )
#     elif(sub3>sub1 and sub3>sub2 and sub3>sub4 and sub3>sub5):
#         print(f"subject sub3 has largest score" )
#     elif(sub4>sub1 and sub4>sub2 and sub4>sub3 and sub4>sub5):
#                 print(f"subject sub4 has largest score" )
#     else:
#         print(f"subject sub5 has largest score" )

# def first_smallest_score(sub1,sub2,sub3,sub4,sub5):
#     if(sub1<sub2 and sub1<sub3 and sub1<sub4 and sub1<sub5):
#         print(f"subject python has smallest score" )
#     elif(sub2<sub1 and sub2<sub3 and sub2<sub4 and sub2<sub5):
#         print(f"subject Maths has smallest score" )
#     elif(sub3<sub1 and sub3<sub2 and sub3<sub4 and sub3<sub5):
#         print(f"subject Science has smallest score" )
#     elif(sub4<sub1 and sub4<sub2 and sub4<sub3 and sub4<sub5):
#             print(f"subject Social has smallest score" )
#     else:
#         print(f"subject DS has smallest score" )

# def score_calculation():
#     sub1=float(input("Enter the the mark of the subject python: "))
#     sub2=float(input("Enter the the mark of the subject Maths: "))
#     sub3=float(input("Enter the the mark of the subject Sciecne: "))
#     sub4=float(input("Enter the the mark of the subject Social: "))
#     sub5=float(input("Enter the the mark of the subject DS: "))
#     total=subjects_sum(sub1,sub2,sub3,sub4,sub5)
#     print(f"The toal marks scored is:{total}")
#     average=subjects_average(total)
#     print(f"The average marks scored is: {average}")
#     first_largest_score(sub1,sub2,sub3,sub4,sub5)
#     first_smallest_score(sub1,sub2,sub3,sub4,sub5)

# score_calculation()

def subject_total(subject_marks):
    total_marks=sum(subject_marks)
    # for i in range(len(subject_marks)):
    #     total_marks+=subject_marks[i]
    return total_marks

def subject_total_average(total,subject_marks):
    average_marks= total/len(subject_marks)
    print(f"The average marks scored in {len(subject_marks)} subjects is:{average_marks}")

def first_largest_score(subject_marks):
    max_score=max(subject_marks)
    return max_score

def first_smallest_score(subject_marks):
    min_score=min(subject_marks)
    return min_score

def subject_score_calculation():
    subject_marks=(40,50,78,89,56)
    total=subject_total(subject_marks)
    print(f"The total marks scored in 5 subjects is:{total}")
    subject_total_average(total,subject_marks)
    largest=first_largest_score(subject_marks)
    print(f"The highest score obtained in all {len(subject_marks)} subjects is:{largest}")
    smallest=first_smallest_score(subject_marks)
    print(f"The lowest score obtained in all {len(subject_marks)} subjects is:{smallest}")


#subject_score_calculation()


#*****************************************
#********optional arguments***************
#*****************************************

def calculate_exponent(num,exp=2):       #defining a function to calculate exponent of a number with default value of exponent as 2
    print(num**exp)

# calculate_exponent(5,3)                  #calling the function with both arguments, num=5 and exp=3
# calculate_exponent(5)                    #calling the function with only one argument, num=5, exp will take the default value of 2

def create_wish(name,wish="Good Day"):
    print(f"Hi {name}. {wish}")

#create_wish("Jerin")
# create_wish("jerin","Good Morning")
# create_wish(wish="Good Morning",name="Jerin")

#*******************************
#******function practice********
#*******************************
python=50
maths=78
science=75

list_marks=[20,40,69.75,80]

def subject_total(python,maths,science):
    total_marks=python+maths+science
    # for i in range(len(subject_marks)):
    #     total_marks+=subject_marks[i]
    return total_marks

def subject_total_average(total):
    average_marks= total/3
    return average_marks

def first_largest_score(python,maths,science):
    max_score=max(python,maths,science)
    return max_score

def first_smallest_score(python,maths,science):
    min_score=min(python,maths,science)
    return min_score

def calculate_result(python,maths,science):
  total=subject_total(python,maths,science)
  print(f"The total marks scored in three subjects is:{total}")
  average=subject_total_average(total)
  print(f"The average marks scored in three subjects is:{average}")
  print(f"The highest score is:{first_largest_score(python,maths,science)}")
  print(f"The lowest score is:{first_smallest_score(python,maths,science)}")

#calculate_result(python,maths,science)
     

def check_certificate_eligibility(python,maths,science):
   total=subject_total(python,maths,science)
   average=subject_total_average(total)
   if(average>=0 and python>=40 and maths>=40 and science>=40):
      print("You are eligible for the certificate.")
   else:
      print("You are not eligible for the certificate.")
            
    

def calculate_grade(python,maths,science):
    marks=float(input("Enter your mark to know your grade: "))
    if(marks>=90 and marks<=100):
     print("Your grade is 'A'")
     grade='A'
    elif(marks>=75 and marks<90):
      print("Your grade is 'B'")
      grade='B'
    elif(marks>=60 and marks<75):
      print("Your grade is 'C'")
      grade='C'
    elif(marks>=40 and marks<60):
      print("Your grade is 'D'")
      grade='D'
    elif(marks<40 and marks>=0):
      print("Your have failed")
      grade='failed'
    else:
      print("Enter valid marks")
    check_certificate_eligibility(python,maths,science)
 
 
#calculate_grade(python,maths,science)

def analyze_marks(list_marks):
   print(list_marks)

#****************************************
#************Exception Handling**********
#****************************************

''' Exception handling is a mechanism in programming that allows you to handle errors or exceptional situations that may occur during the execution of a program.
In Python, exception handling is done using the try-except block. 
The code that may raise an exception is placed inside the try block, and the code to handle the exception is placed inside the except block.'''

def divide(num,den):            #defininig a function to divide two numbers with exception handling
   try:                         #trying to execute the code that may raise an exception
      result=num/den            #performing the division operation
      print(f"The result is:{result}")
   #except ZeroDivisionError:
   except Exception as e:               #catching the exception and printing the error message
      print(f"There is an error {e}")
   #except TypeError:
    #  print("Both numerator and denominator should be numbers.")



# divide(40,5)
# divide('a','b')   #Type error
# divide(0,5)
# divide(40,0)      #Division by zero error

#printing clear error messages in exceptions

def divide(num,den):            #defininig a function to divide two numbers with exception handling
   try:                         #trying to execute the code that may raise an exception
      result=num/den            #performing the division operation
      print(f"The result is:{result}")
   except ZeroDivisionError:
      print("Please make sure you are entering a non-zero element as denominatorr")
   except TypeError:
      print("Both numerator and denominator should be numbers.")
   except Exception as e:               #catching the exception and printing the error message
      print(f"There is an error {e}")


divide(40,5)
divide('a','b')   #Type error
divide(0,5)
divide(40,0)      #Division by zero error

    



   