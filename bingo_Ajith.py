'''This program takes a number as input from the user and
iterates through all numbers from 1 to that number. 
For each number, it checks if the number is divisible by 5.
If it is, it prints "Bingo!", otherwise it prints the number itself.'''


number=int(input("Enter a number: "))   #Taking input from user

for i in range (1,number+1):   #using for loop to iterate through the range of numbers from 1 to the input number
    if(i%5==0):                #Checking if the number is divisible by 5
        print("Bingo!")        #Printing "Bingo!" if the number is divisible by 5
    else:  
        print(i)               #Printing the number if it is not divisible by 5
        
i=1
while i<=number:
    if(i%5==0):
        print("Bingo!")
    else:
        print(i)
    i+=1

''' Get a number from the user and print all numbers from 1 to 30 that are divisible by 3.
Also, count how many numbers are divisible by 3 and print the count at the end.'''

number_1=int(input("Enter a number in between 1 and 30: "))  #Taking input from user
count=0      #initializing count variable to 0

for i in range(1,30):   #using for loop to iterate through the range of numbers from 1 to 30
    if(i%3==0):     #Checking if the number is divisible by 3
        print(i)    #Printing the number if it is divisible by 3
        count+=1    #Incrementing the count variable by 1 for each number that is divisible by 3

print("Total numbers divisible by 3 are: ",count)    #Printing the total count of numbers that are divisible by 3 out of the loop
              
i=1   #Initializing i variable to 1
while(i<=30):   #Checking if i is less than or equal to 30
    if(i%3==0): #Checking if the number is divisible by 3
        print(i)   #Printing the number if it is divisible by 3
        count+=1   #Incrementing the count variable by 1 for each number that is divisible by 3
    i+=1           #Incrementing i variable by 1 for each iteration of the loop

print("Total numbers divisible by 3 are: ",count)   #Prinitnig the total count of numbers that are divisible by 3 out of the loop