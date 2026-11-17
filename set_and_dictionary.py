''' This is a set in Python.
A set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
Set supports heterogeneous data types. It can store any type of data. It is a collection of unique elements.
It does not allow duplicate values. It is mutable.
'''


#*********************************
#**************SET****************
#*********************************


#declaring a set
#method 1
set1={} #This is not a set, but this is a dictionary

# #method 2
set2={12,56,13,2027,"Ajith",True,2027.0,'2027'}  #This is a set

print(set2)

# #method 3

set3=set()   #This is a set

print(type(set1))
print(type(set2))
# print(type(set3))

roll={1,2,3,4,5,6}
roll_odd={1,3,5}
roll_even={2,4,6}
random={1,5,9,4}

random.add(2026)                     #Add an element to the set
print(random)

# #Difference of two sets
print(random.difference(roll_odd))   #Value present in random but not in roll_odd

print(roll_odd.difference(random))   #Value present in roll_odd but not in random

random.discard(2026)                 #Removing the specified value from the set
print(random)

print(roll.issuperset(roll_odd))     #Checking if the roll is a superset of roll_odd or not
print(roll_odd.issubset(roll))       # Checking if the roll_odd is a subset of roll or not

print("Intersection of random and roll set: ",random.intersection(roll_even))     #Returns the common elements in both sets

roll.remove(6)                       #Removing the specified value from the set
print(roll)

roll.clear()                          #Clearing all the elements from the set
print(roll)
 
pop=random.pop()                     #Popping the last element from the set (Actually, it removes a random element from the set as sets are unordered)
print("The popped value is: ",pop)
print(random)
pop=random.pop()
print("The popped value is: ",pop)
print(random)

pop=roll_odd.pop()
print("The popped value is: ",pop)
print(roll_odd)

pop=roll_odd.pop()
print("The popped value is: ",pop)
print(roll_odd)



''' Dictionary in Python
A dictionary is a collection which is unordered, changeable and unindexed. 
In Python dictionaries are written with curly brackets, and they have keys and values.
Dictionaries are used to store data values in key:value pairs.'''


#*********************************
#**************Dictionary*********
#*********************************

#method 1
dict1={} #This is a dictionary

# #method 2
dict2={"key1":'value1',8:10,"key2":'value2',8:4,True:"It works",8:5} #This is a dictionary and duplicate keys are not allowed. The last value of the duplicate key will be considered.

# #method 3
dict3=dict() #This is a dictionary

print(dict2)
print(dict2["key1"])  # Accessing the value of the key "key1"
print(dict2[8])       # Accessing the value of the key 8

print(dict2.keys())   ##Returns the keys of the dictionary


# Defining a dictionary to store student details
student_dict={"name":"Ajith Joy", 
              "age":22,
              "Course":"B.TEch",
              "University":"KTU",
              "College":"GECI",
              "District":"Kottayam",
              "State":"Kerala",
              }

print(student_dict)
print("The keys in the student dictionary are: ",student_dict.keys())     # Returns the keys of the dictionary
print("The values in the student dict are: ",student_dict.values())       #Values of the dictionary
print("The items in the student dict are: ",student_dict.items())         #Returns the key-value pairs of the dictionary as a list of tuples

#Modifying value of key

student_dict["University"]="ApJ Ktu"
print(student_dict["University"]) #Accessing the value of the key "University" after modifying it

personal={"name":"Ajith Joy",
          "Phone":6238572794,
          "DOB":"14-05-2004",
          "Age":22,
          "Gender":"Male",
          "Blood Group":"O+ve",
          "Qualification":"B.Tech"}
print(personal)
phone=int(input("Enter the phone number: "))
personal["Phone"]=phone
print(personal)