
#*******************************
#***********File Handling*******
#*******************************

path="E:/PGP_Data_Science_ AIML/python/sample.txt"    #Giving the path of the file which we want to open
relative_path='sample.txt'

def read_file_filepath():
  file=open(relative_path,'r')      #opening the file in read mode using the open() function by passing the path of the file and the mode in which we want to open the file
  content=file.read()      #contents of the file will be stored in the variable content
  print(content)
#print(type(content))
#file.write("Hello World")

def read_file_line():
  file=open(relative_path,'r')      #opening the file in read mode using the open() function by passing the path of the file and the mode in which we want to open the file
  content=file.readline ()      #contents of the file will be stored in the variable content
  print(content)


def read_file_lines():
  file=open(relative_path,'r')      #opening the file in read mode using the open() function by passing the path of the file and the mode in which we want to open the file
  content=file.readlines            # using readlines() and storing the contents in a list
  print(content)                    #Printing the contents of the file
  for line in content:              #
    print(line)
  file.close()

#read_file_filepath()
#read_file_lines()
write_path='student.txt'

def write_file():               #defining a function to write into a file
 file1=open(write_path,'w')     #Opening the file in write mode using the open() function by passing the path of the file and the mode in which we want to open the file
 file1.write("world\n") 
 file1.write("wow\n")
 file1.write("nice\n")          #Writing into the file using the write() function
 file1.close()                  #Closing the file using the close() function

def write_into_file(name):      #defining a function to write into a file
   file=open(write_path,'w')
   file.write(name)             #Writing into the file using the write() function which is passed as an argument to the function
   file.close()                 #Closing the file using the close() function

#write_file()

#write_into_file('Ajith')        #Calling the function with the argument 'Ajith'

def append_file():
  file=open(write_path,'a')
  file.write("Jerin")
  file.close()

#append_file()

def append_data(file_path,data):
  file=open(file_path,'a')
  file.write("\n")
  file.write(data)
  file.close()

file_path='data.txt'
#append_data(file_path,'Ajith')

#File assigning is done using the with statement which automatically closes the file after the nested block of code
def append_data_new(file_path,data):
  with open(file_path,'a') as file:
   file.write("\n")
   file.write(data)

append_data_new(file_path,'Airtel')