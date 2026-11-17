# print("Hello World")
# print('''This is multi line string
# so you will see this as a pragraph''')
# ''' this is a multi line comment
# just to test this'''
# # showing different datatypes
# print("2026") #string
# print(2026) #integer
# print('2026') #string
# c=20
# print("Hello"+"world") #string concatentation
# print(f"hello {c} ")
# print("The datatype of 2026 is",type(20))
# print("The datatype of 20.0 is",type(20.0))
# print('The datatype of "20" is',type("20"))
# print("The datatype of '20' is",type('20'))
# print("The datatype of 50+10j is",type(50+10j))  #This is complex
# print("The datatype of True is",type(True))
# print(f"The type of 2026 is {type(1)}")
# #print("The datatype of True is",type(TRUE))    This is error
# print("The datatype of True is",type(False))  # This is boolean


#***************************
#********Variable***********
#***************************
my_name="Ajith Joy"
age=22
place_of_birth="Kottayam"
mobile_no=6238572794
height=163
weight=65
email="ajith14may@gmail.com"
gender="male"
education="B.Tech"
print("My mobile number is:",mobile_no)

fred=200
john=fred
print(john)
fred=3
print(john)

print("Data type of",my_name,"is",type(my_name))
print("Data type of age",age,"years is",type(age))
print("Data type of height",height,"cm is",type(height))
print("Data type of weight",weight,"kgis",type(weight))
print("Data type of",email,"is",type(email))
print("Data type of",gender,"is",type(gender))
print("Data type of",mobile_no,"is",type(mobile_no))


#***************************
#*******Type conversion***********
#***************************

num1=1900
num2=67.8
print("data type of ",num1,"is",type(num1))
print("data type of ",num2,"is",type(num2))

num3=int(num2)
num4=float(num1)
print("data type of ",num3,"is",type(num3))
print("data type of ",num4,"is",type(num4))