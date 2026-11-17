#**********************************************
#*************Arithmetic Operators*************
#**********************************************

num1=5
num2=2

sum=num1+num2 #addition
difference=num1-num2 #subtraction
product=num1*num2 #multiplication
division=num1/num2 # Division
modulus=num1%num2 #Remainder
floor_division=num1//num2 # Floor division
exponentiation=num1**num2 #Exponentiation

print("The sum of", num1,"+",num2 ,"=",sum)
print("The difference of", num1,"-",num2 ,"=",difference)
print("The product of", num1,"*",num2 ,"=",product)
print("The quotient of", num1,"/",num2 ,"=",division)
print("The modulus(remainder) of", num1,"%",num2 ,"=",modulus)
print("The exponential of", num1,"**",num2 ,"=",exponentiation)
print("The floor division of ",num1,"//",num2 ," =", floor_division)

#**********************************************
#*************Conditional Operators*************
#**********************************************

#num1=5 
#num2=2
print(num1,'>',num2,num1>num2)  #Greater than
print(num1,'<',num2,num1<num2)   #Less than
print(num1,'>=',num2,num1>=num2) #Greater than or equal to
print(num1,'<=',num2,num1<=num2) #Less than or equal to
print(num1,'==',num2,num1==num2)  #Equal to
print(num1,'!=',num2,num1!=num2) #Not equal to

#**********************************************
#*************Logical Operators*************
#**********************************************

statement_1=True
statement_2=False
statement_3=True
statement_4=False

print(statement_1 and statement_2)   #True and False=False
print(statement_1 and statement_3)   #True and True=True
print(statement_1 and statement_4)   #True and False=False
print(statement_2 and statement_3)   #False and True=False
print(statement_2 and statement_4)   #False and False=False
print(statement_3 and statement_4)   #True and False=False

print(statement_1 or statement_2)    #True or False=True
print(statement_1 or statement_3)    #True or True=True
print(statement_1 or statement_4)    #True or False=True
print(statement_2 or statement_3)    #False or True=True
print(statement_2 or statement_4)    #False or False=False
print(statement_3 or statement_4)    #True or False=True

print(not(statement_1))              #Not True=False
print(not(statement_2))              #Not False=True

