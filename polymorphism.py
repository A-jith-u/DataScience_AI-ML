class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,emp_id,salary,job_role):
        super().__init__(name,age,)
        self.emp_id=emp_id
        self.salary=salary
        self.job_role=job_role

    def display_details(self):
        print(f"{self.name} is an employee of ABC company with id {self.emp_id}, salary of {self.salary} as an {self.job_role}")

class Father(Person):
    def __init__(self,name,age,no_of_children):
        super().__init__(name,age)
        self.no_of_children=no_of_children

    def display_details(self):
        print(f"{self.name} is a father of {self.no_of_children} children")

class Son(Person):
    def __init__(self,name,age,father,mother):
        super().__init__(name,age)
        self.father=father
        self.mother=mother

    def display_details(self):
        print(f"{self.name} father's name:{self.father} and mother's name:{self.mother}")

class Husband(Person):
    def __init__(self,name,age,wife_name,date_of_marriage):
        super().__init__(name,age)
        self.wife_name=wife_name
        self.date_of_marriage=date_of_marriage
    def display_details(self):
        print(f"{self.name} Wife's name:{self.wife_name} and Date of Marriage:{self.date_of_marriage}")



person=Person("Ramesh",32)
emp=Employee("Ramesh",32,'A102',23000,'SD')
father=Father("Ramesh",32,2)
son=Son('Ramesh',22,'Suresh','Sudha')
hus=Husband('Ramesh',22,'Maya','24/05/2018')
emp.display_details()
father.display_details()
son.display_details()
hus.display_details()


class Employee:
    def calculate_salary(self):
        print("Calculating employee salary")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full-time employee receives a fixed month salary")

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Part-time employee salary is based on working hours")

class Freelancer(Employee):
    def calculate_salary(self):
        print("Freelancer salary is based on completed projects")

emp=Employee()
emp.calculate_salary()

full_time=FullTimeEmployee()
full_time.calculate_salary()

part_time=PartTimeEmployee()
part_time.calculate_salary()

freelance=Freelancer()
freelance.calculate_salary()





from abc import ABC,abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass

    def __init__(self,account_holder,account_type,balance):
        self.account_holder=account_holder
        self._account_type=account_type
        self.__balance=balance

    @property
    def balance(self):
        return self.__balance

    # @property
    # def account_type(self):
    #     return self._account_type
    
    @balance.setter
    def balance(self,increment):
        if increment<=0:
            raise "The balance cannot be zero or negative"
        self.__balance=increment

    def deposit(self,deposit_amount):
        if deposit_amount<=0:
            raise "Deposit amount cannot be zero or negative"
        self.__balance=self.balance+deposit_amount
        print("Deposit succesful: Rs.",deposit_amount)

    def withdraw(self,withdraw_amount):
        if withdraw_amount>self.balance:
            raise "Insufficient balance"
        self.__balance=self.balance-withdraw_amount
        print(f"Withdrawal succesful: Rs.{withdraw_amount}.")
        
    def display_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: Rs.{self.balance}")
    # @account_type.setter
    # def account_type(self,ac_type):
    #          self._account_type=ac_type


class SavingsAccount(BankAccount):
    def __init__(self,account_holder,account_type,balance):
        super().__init__(account_holder,account_type,balance)
        self.account_type=account_type

    def calculate_interest(self):
        interest=self.balance*0.05
        print(f"{self.account_holder}'s Annual Interset: Rs.{interest}")

class CurrentAccount(BankAccount):
    def __init__(self,account_holder,account_type,balance):
        super().__init__(account_holder,account_type,balance)
        self.account_type="current"

    def calculate_interest(self):
        interest=self.balance*(2/100)
        print(f"{self.account_holder}'s Annual Interset: Rs.{interest}")


customer1=SavingsAccount("Ashbi","Savings",10000)
customer2=CurrentAccount("Rahul","current",20000)

customer1.deposit(5000)
customer1.withdraw(2000)
print("\n")

customer2.deposit(3000)
customer2.withdraw(5000)

print("---------- ACCOUNT DETAILS ----------")
customer1.display_details()
print("\n")
customer2.display_details()

print("---------- ANNUAL INTEREST ----------")
customer1.calculate_interest()
customer2.calculate_interest()
    
