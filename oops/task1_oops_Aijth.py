#***********************************************
#**************EMPLOYEE SALARY MANAGEMENT********
#************************************************

from employee import ContractEmployee,PermanentEmployee     #Importing the ContractEmployee and PermanentEmployee classes from the employee module
from vehicle import Car,Bike                                 #Importing the Car and Bike classes from the vehicle module



print("**********EMPLOYEE SALARY MANAGEMENT SYSTEM**********")

permanent_employee=PermanentEmployee('Ajay',101,'Software Engineer','ajaywork@gmail.com','6238572794',50000,2000)      #Creating an object of the PermanentEmployee class and passing the required arguments to the constructor
contract_employee=ContractEmployee('Vijay',110,'Software Designer','vijaywork@gmail.com','9747626238',40000,1000)      #Creating an object of the ContractEmployee class and passing the required arguments to the constructor


permanent_employee.display_details()                  #Displaying the details of the permanent employee by calling the display_details method of the PermanentEmployee class
permanent_employee.calculate_salary()                 #Calculating the salary of the permanent employee by calling the calculate_salary method of the PermanentEmployee class

print("______________________________________________")
contract_employee.display_details()                   #Displaying the details of the contract employee by calling the display_details method of the ContractEmployee class
contract_employee.calculate_salary()                  #Calculating the salary of the contract employee by calling the calculate_salary method of the ContractEmployee class


print("\n")


#************************************************
#**************VEHICLE RENTAL MANAGEMENT*********
#************************************************


print("**********VEHICLE RENTAL MANAGEMENT**********")
print("\n")

car=Car("Maruti Suzuki","Daily use","KL01AB1234",6000)            #Creating an object of the Car class and passing the required arguments to the constructor
bike=Bike("Honda","Hourly","KL02CD5678",200)                      #Creating an object of the Bike class and passing the required arguments to the constructor

car.display_vehicle_details()                                     #Displaying the details of the car by calling the display_vehicle_details method of the Car class
car.calculate_rent(3)                                             #Calculating the rent of the car for 5 days by calling the calculate_rent method of the Car class

print("______________________________________________")

bike.display_vehicle_details()                                     #Displaying the details of the bike by calling the display_vehicle_details method of the Bike class
bike.calculate_rent(3)                                             #Calculating the rent of the bike for 3 days by calling the calculate_rent method of the Bike class
