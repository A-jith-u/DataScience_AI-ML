#****************************************
#************INPUT FROM USER*************
#****************************************

# username=input("Enter your username:")  #waiting for user to enter value
# print("The username you entered is:",username) #printing the username entered by user

# password=int(input("Enter your password:"))
# print("The password you entered is:",password)

# print("Data type of",username,"is:",type(username))  #data type of username
# print("Data type of",password,"is:",type(password))  #data type of password

#Always the output form the function input() is of string data type.
#we have to explicitly convert numerical values.

# age=int(input("Enter your age:")) #Taking input from user and converting it into integer data type
# print("The age you entered is:",age,"and data type of",age,"is:",type(age)) #printing the age and data type 

# height=float(input("Enter your height:"))  #Taking the height of user as input and converting it into float data type
# print("The height you entered is:",height,"and data type of",height,"is:",type(height))  #Printing the heigth and data tyoe of height



#******************************
#*********SELF INTRODUCTION*****
#*******************************

name=input("Enter your name:")  #Taking user name as input
age=int(input("Enter your age:")) #Taking age as input 
course=input("Enter the course you are pursuing:") #Taking the course as input
place=input("Enter your place:")  #Taking the place as input
institution=input("Enter the institution you are studying in:") #Taking the institution name as input
qualification=input("Enter your current qualification:") #Taking the qualification as input
experience=input("Enter your experience:") #Taking the experience as input

#Printing the self introduction of the user using f-string formatting
print(f'''SELF INTRODUCTION\n Hi! I am {name}, a {age} years old student from {place} pursuing {course} from {institution}.
 I have completed my {qualification} and have an experience in working as {experience}.
 I am looking forward for a job in the field of {course}.''')


