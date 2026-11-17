'''List is data type to store a collection of values.
It is a derived data type. It is a mutable data type.
It can store different datatypes in a single list.
A list is declared using square brackets [].
A lsit can contain different datatypes like string, integer, float, boolean, list, tuple, dictionary etc. - Hetrogeneous data type.'''

# list=["Ajith",45,True]
# print(list)
# print(list[0])

#Declaring an empty list   method_1
# list1=[]
# print(type(list1))   #Printing the type of an empty list

# #Declaring a list of names    method_2
list_names=["Ajith","Akash","Vishnu"] 
# print(type(list_names))  #Printing th type of the list of names.
# print(list_names[0])  #Fetching the first element of the list_names using indexing.
# #print(list_names[2])  

# #Declaring a list method_3
# list_3=list()        #Just a list declaration using list() method
# print(type(list_3))  #Printing the type of the list_3


#List containing multiple datatypes -demo
#Personal info as a list:name, age, graduation year, university, height,friends

# ajith_info=["Ajith Joy",22,2026,"KTU",163,list_names]  #Creating a list containing multiple datatypes. The last element of the list is a list of names.

# print(type(ajith_info))                  #Fetching the type of the list ajith_info
# print(ajith_info[0],type(ajith_info[0])) #Fetching the first element and it's type of the list ajith_info using indexing.
# print(ajith_info[1],type(ajith_info[1])) #Fetching the second element and it's type of the list ajith_info using indexing.
# print(ajith_info[2],type(ajith_info[2])) #Fetching the third element and it's type of the list ajith_info using indexing.
# print(ajith_info[3],type(ajith_info[3])) #Fetching the fourth element and it's type of the list ajith_info using indexing.
# print(ajith_info[4],type(ajith_info[4])) #Fetching the fifth element and it's type of the list ajith_info using indexing.
# print(ajith_info[5],type(ajith_info[5])) #Fetching the sixth element and it's type of the list ajith_info using indexing. The sixth element is a list of names.



#*****************************************
#*************List FUnctions**************
#*****************************************

# list_2=[False,True,False]   #List of boolean values
# list_1=[3,1,7,8]            #List of integer values
# #print(list_1+list_2)       #Concatenation of two lists

# list_1.sort()               #Sorting the list_1 in ascending order 
# print(list_1)               #Printing the sorted list

# list_1.sort(reverse=True)   #Sorting the list_1 in descending order
# print(list_1)               #Printing the sorted list

# list_names.sort()
# print(list_names)           #Printing the sorted list of names

# list_names.extend(list_1)   #Extending the list_names with the elements of list_1
# print(list_names)           #Printing the extended list_names

# list_2.append(list_1)       #Appending the list_1 as a single element to the list_2
# print(list_2)
# print(list_2[3])

# list_1.append("A")
# print(list_1)               #Appending a string to the list_1

# list_1.reverse()            #Reversing the list_1  [8,7,3,1,'A']  
# print(list_1)               #Printing the reversed list_1 ['A',1,3,7,8]

# #list_2.count(False)
# print("No. of times 'False' appeared in the list_2 is: ",list_2.count(False))  #Counting the number of occurences of False in the list_2
# print("No. of times 'X' appeared in the list_2 is: ",list_2.count('x'))        #Counting the number of occurences of 'x' in the list_2
# print("No. of times 'True' appeared in the list_2 is: ",list_2.count(True))    #Counting the number of occurences of 'True' in the list_2

# #Value at last index
# print("Value at last index of list_2 is: ",list_2[-1])
# print("Value at lat index of list_2 is: ",list_2[len(list_2)-1])   #Fetching the value at last index of the list_2 using len() function

# #Fetching no. of items in the list_1 using len() function
# print("No. of items in the list_2 is: ",len(list_2))

# print("Before clearing list_2:\n",list_2)
# list_2.clear() #Clearing all the elements of the list_2
# print("After clearing the list_2:\n",list_2)

# print("\n")

# #Inserting an element at a specific index
# list_1.insert(2,100) #Inserting the value 100 at index 2 of the list_1
# print("After inserting 100 at index 2 in list_1:\n",list_1)

# #removing an element from the list
# list_1.remove(3) #Removing the value 3 from the list_1
# print("After removing 3 from list_1:\n",list_1)

# #using pop() function to remove an item from the list. By default it removes the last item of the list.
# list_1.pop()
# print("After popping and item in the list_1:\n",list_1)



#***************************************
#************TUPLE**********************
#***************************************
#Tuple is a derived data type. It is an immutable data type. It can store different datatypes in a single tuple.

#Declaring a tuple
tuple_1=()
tuple_2=(1,2,3,4,5,"Ajith",[6,7,8])  

print(type(tuple_2))  # Finding the type of the tuple_2
print(tuple_2)
print(tuple_2[2])

print(tuple_2.index(3))    #finding the index of the value 3 in the tuple_2
print(tuple_2.count("Ajith"))  #Fniding the number of occurences of "Ajith" in the tuple_2

del(tuple_2)  #Deleting the tuple_2

#print(tuple_2)  #This will give an error as the tuple_2 is deleted.