#class BankAccount:
#     def __init__(self,owner_name,bank_balance,account_type):
#         self.owner_name=owner_name
#         self.__bank_balance=bank_balance  #private attribute
#         self._account_type=account_type   #protected attribute which can be accessed by the child class but not by the object of the class. But external access is not recommended. It is a convention to use a single underscore to indicate that the attribute is intended for internal use only.

#     #to get the private attribute
#     @property                  #property decorator is used to access the private attribute
#     def bank_balance(self):    #defining the method to access the private attribute
#         return self.__bank_balance      #returning the private attribute

#     @property
#     def account(self):
#         return self._account_type

#     #to update the private attribute
#     @bank_balance.setter
#     def bank_balance(self,deposit_amount):
#         if deposit_amount<=0:
#             raise "Deposit amount cannot be zero or negative"
#         self.__bank_balance+=deposit_amount
    
#     @account.setter            #setter decorator is used to update the protected attribute
#     def account_type(self,ac_type):          #defining the method to update the protected attribute
#         if ac_type not in ["saving","current"]:          #checking if the account type is valid
#             raise "Account type can only be saving or current"       #raising an exception if the account type is invalid
#         self._account_type=ac_type                #updating the protected attribute
    
# bank=BankAccount("ABC",10000, "Saving")

# print('', bank.owner_name)
# print("Account type:",bank.account)

# #syntax: class.setter function=new value
# bank.bank_balance=123
# print(bank.bank_balance)

# bank.account_type="current"             #updating the protected attribute using the setter method
# print(bank.account)





# class Employee:
#     def __init__(self,employee_name,department,salary):
#         self.employee_name=employee_name
#         self._department=department
#         self.__salary=salary

#     @property
#     def salary(self):
#         return self.__salary


#     @salary.setter
#     def salary(self,increment):
#         if increment<=0:
#             raise "Salary increment cannot be zero or negative"
#         self.__salary+=increment

# class Manager(Employee):
#     #def __init__(self,employee_name,department,salary):
#       #  super().__init__(employee_name,department,salary)

#     def display_details(self):
#         print("The employee name is:",self.employee_name)
#         print("The employee department is:",self._department)

# # employee=("Hari","sales",50000)

# employee=Manager("Ramesh","Accounting",60000)
# employee.display_details()
# # print("The salary of the employee is:",employee.salary)

# employee.salary=1000
#print("The salary of the employee after increment is:", employee.salary)


class Vehicle:
    def __init__(self,_name,rental_type,rental_price):
        self._name=_name
        self._rental_type=rental_type
        self.__rental_price=rental_price

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self,increment):
        if increment<=0:
            raise "Rental price increment cannot be zero or negative"
        self.__rental_price = increment

    def display_details(self):
        print(f"The  name is:{self._name}.\nThe  rental type is:{self._rental_type}.")

class Car(Vehicle):

    def calculate_rent(self,days):
        self.rental_price=self.rental_price* days

    def display_details(self):
        print(f"The  name is:{self._name}.\nThe  rental type is:{self._rental_type}.\nThe  rent is :{self.rental_price}")


class Bike(Vehicle):
    def calculate_rent(self,days):
        self.rental_price=self.rental_price* days

    def display_details(self):
        print(f"The  name is:{self._name}.\nThe  rental type is:{self._rental_type}.\nThe  rent is :{self.rental_price}")
    

car=Car("Innova","Daily",2000)
bike=Bike("Honda","Daily",800)

print(car.rental_price * 3)
print(bike.rental_price * 3)

print("_______________________________________")
car.calculate_rent(3)
car.display_details()

print("_______________________________________")
bike.calculate_rent(3)
bike.display_details()

print("_______________________________________")
car.rental_price=2000
car.display_details()


