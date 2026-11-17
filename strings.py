# string_1="Hello nice to meet you"
# string_2="Yes, it is nice to meet you too"
# string_3="Welcome to python strings"

# print(string_1)
# print(string_2)
# print(string_3)
# print('\n')
# print(string_1, string_2, string_3)
# print('\n')
# #By default python prints a new line after each print statement.

# # changing the end string
# print(string_2,end='&')
# print(string_3,end='&')
# print('\n')
# print(string_2,'\t',string_3,'\t')


# #*************************************************
# #*************String Concatentation****************
# #*************************************************

# s1="ICT"
# s2="Academy"
# s3="of"
# s4="Kerala"
# #print(s1,'\t',+s2,'\t',+s3,'\t',+s4)
# combined_string=s1+' '+s2+' '+s3+' '+s4 #space between concatenated strings
# print(combined_string)

# print(s1+s1+s1+s1+s1)
# print(s1*5)
# print((s1+' ')*5)
# print((s1+'\t ')*5)
# print((s1+' \n')*5)

# #*************************************************
# #*************String Indexing****************
# #*************************************************     
# print(string_3[0])  #string_3="Welcome to python strings"
# print(string_3[5])
# print(string_3.index('m'))
# print(len(string_3))
# print(string_3[-1]) #last index value through negative indexing
# #print(string_3[26])  #we cannot go beyong the maximum index of the string.


#*************************************************
#*************String slicing****************
#*************************************************

s1="Trivandrum"   

# print(s1[-4]) #printing 4th last character using negative indexing
# print(s1[6])  #printing 6th index character

# print(s1[:4]) #slicing from 0th index to 3rd index
# print(len(s1)) #Length of the string=10
# print(s1[4:]) #slicing from 4th index to last index
# print(s1[0:5]) #slicing from 0th index to 4th index
# print(s1[5:10]) #slicing from 5th index to 9th index 
# print(s1[4:7]) #slicing to get and 
# print(s1[:5:2]) #slicing from 0th index to 4th index with a step of 2 'Tia'
# print(s1[0::2]) 
# print(s1[::-1]) #reversing the string using slicing


#*************************************************
#*************String Functions****************
#*************************************************

print(s1.upper()) #converting to upper case
print(s1.lower()) # converting to lower case
print(s1.swapcase()) # swaping cases
print(s1.capitalize()) # captialize the first letter
print(s1.count('r')) #counting the number of occurences of 'r'
print(s1.replace('r','R')) #replacing 'r' with 'R'
print(s1.find('b')) #finding the index of 'b' in the string
print(s1.find('r')) #finding the index of 'r' in the string
print(s1.rpartition('d')) #splitting the string into 3 parts based on the last occurence of 'd'        


# my_name="Ajith Joy"
# print(my_name[-1])
# print(len(my_name))
# print("last index =",len(my_name)-1)
# print("Jo" in my_name)
# print(my_name[1:4])