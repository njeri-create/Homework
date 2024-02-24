class BankAccount:
    def __init__(self,Account_number,balance,date_of_opening,customer_name):
        self.Account_number = Account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self):
        deposit = int(input("Enter amount you like to deposit: "))
        balance = self.balance + deposit
        print(f"Dear {self.customer_name} your balance is {balance}")
    def withdraw(self):
        withdraw = int(input("Enter amount you would like to withdraw: "))
        balance = self.balance - withdraw
        print(f"Dear {self.customer_name} your new balance is {balance}")
Obj1 = BankAccount(54789,600000,"14/7/2018","Jayden")
Obj1.withdraw()