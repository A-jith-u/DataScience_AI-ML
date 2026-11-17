  # #***************************************
# #********Checking whether a number is bigger than 50********
# #****************************************
 
# # number=int(input("Enter a number: ")) #Prompting user to enter a number and converting to integer data type

# # if number>50:                          #checking whether the number entered is greater than 50
# #     print("The number you entered is greater than 50.") #prints if the number entered is greater than 50
# # else:
# #     print("The number you entered is not greater than 50.")  #printing if the number entered is less than 50

# # print("End of program.")

# # number_1=int(input("Enter your number: ")) #prompting user to enter a number
 
# # if ((number_1%2)==0):                          #checking whether the number is even or oddd using modulus operator(if remainder ==0 it is even))
# #     print(f"The number {number_1} you entered is an even number.")  #printing if the number is even.
# # else:
# #     print(f"The number {number_1} you entered is an odd number.")   #printing if the number is odd.


# #****************************************
# #**********CHECKING TEMPERATURE***************
# #****************************************

# temp=float((input("Enter the temperature in celsius: "))) #prompting user to enter temperature in celsius and converting to float data type

# # if(temp>=35):
# #     print("It is a very hot day.") #printing if the temperature is greater than or equal to 35
# # else:
# #     if(temp>=25):                   #checking if the temperature is greater than or equal to 25
# #      print("It is a warm day.")
# #     else:
# #         if(temp>=15):              # checking if the temperature is greater than or equal to 15
# #             print("It is a cold day.")
# #         else:
# #             print("It is a freezing day.") #printing if the temperature is less than 15


# if(temp>=35):                      #checking if the temperature is greater than or equal to 35
#     print("It is a very hot day.") #printing if the temperature is greater than or equal to 35
# elif(temp>=25 and temp<35):        #Checking if temperature is greater than or equal to 25 and less than 35 
#     print("It is a warm day.")     #printing if the temperature is greater than or equal to 25
# elif(temp>=15 and temp<25):        #Checking if temperature is greater than or equal to 15 and less than 25
#     print("It is a cold day.")     #Printing if the temperature is greater than or equal to 15
# else:
#     print("It is a freezing day.")  #Printing if the temperature is less than 15



#*****************************************
#**********ITERATIVE STATEMENTS***********
#*****************************************

#Iteratives statements are used when certain tasks are to be executed multiple times.
#for loop : used when nunmber iteration are known or finite.
#while loop: used when number of iteration are unknown and stopping condition is known.


#print numbers

for i in range(1,11):
    print(i)
for i in range(10):   #print numbers from 0 to 9 iterates 10 times
    print(i,": Ajith Joy")

print("Printing with step operator")
for i in range(1,11,2):    #print(i)  #prints numbers from 1 to 10 with step of 2
    print(i)

for i in range(10,2,-1):    #print numbers from 10 to 3 with step of -1, printing in reverse order
    print(i)

#range(start,stop,step) #start: starting number, stop: stopping number, step: step size

for i in range(3,10,3):
    print(i,"Ajith")


print("The odd number less than 50 are:")
for i in range(1,50):
    if(i%2!=0):
        print(i)

print("The odd numbers between 20 and 50 are:")
for i in range(20,50):
    if(i%2!=0):
        print(i)
for i in range(21,50,2):   # Another way to print odd numbers using step count
    print(i)


#while loop
num=1
while num<10:
    print(num)
    num+=1
print("End of while loop")

#Printing odd numbers between 1 and 50 using while loop
num=1
print("Odd number between 1 and 50 are:")
while num<50:   #Stopping condition is num<50, loop will run until num is less than 50
    print(num,end=',')
    num+=2     #Adding 2 to the number to get the next odd number
print("\nEnd of while loop")


#Printing odd numbers between 20 and 50 using while loop
num=21
print("Odd numbers between 20 and 50 are:")
while num<50:  #Stopping condition is num<50, loop will run until num is less than 50
    print(num,end=',')
    num+=2  #Adding 2 to the number to get the next odd number
print("\nEnd of while loop")

#Logical Operators in control flow statements

age=int(input("Enter your age: "))     #Taking input from user and converting to integer data type
valid_id=input("Do you have a valid ID?(Y/N): ")   #Taking input from user and storing it in valid_id variable

if(valid_id.upper()=='Y'):    #Checking if the user has a valid ID by converting the input to uppercase and comparing it to 'Y'
    valid_id=True             #Setting valid_id to True if the user has a valid ID
else:
    valid_id=False            #Setting valid_id to False if the user does not have a valid ID

print("We are checking your eligibility")

if(age>=18 and valid_id):  #Checking if age is greater than or equal to 18 and valid_id is True
    print("You are eligible to vote.")     #printing if the user is eligible to vote
else:
    print("You are not eligible to vote.")

