class InvalidAgeError(Exception):
    pass

class InvalidAccountNumberError(Exception):
    pass

class InvalidAccountTypeError(Exception):
    pass

class InvalidBalanceError(Exception):
    pass

class DepositLimitExceededError(Exception):
    pass

class WithdrawLimitExceededError(Exception):
    pass

class Bank:
    def __init__(self, name, age, account_number, account_type, balance):
        self.name = name
        if age < 18 or age >= 100:
            raise InvalidAgeError("Age should be greater than 18 and less than 100.")
        self.age = age
        if not (10000 <= account_number <= 99999):
            raise InvalidAccountNumberError("Account number should have exactly 5 digits.")
        self.account_number = account_number
        if account_type not in ['S', 'C']:
            raise InvalidAccountTypeError("Account type should be 'S' for Savings or 'C' for Current.")
        self.account_type = account_type
        if balance < 1000:
            raise InvalidBalanceError("Balance should be non-negative and greater than Rs.1000.")
        self.balance = balance

    def deposit(self, amount):
        if amount > 10000:
            raise DepositLimitExceededError("Daily deposit limit is Rs.10000.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > 5000:
            raise WithdrawLimitExceededError("Daily withdrawal limit is Rs.5000.")
        if self.balance - amount < 1000:
            raise InvalidBalanceError("Withdrawal not allowed. Balance should not go below Rs.1000.")
        self.balance -= amount

    def display_account_details(self):
        print("Account Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {'Savings' if self.account_type == 'S' else 'Current'}")
        print(f"Balance: Rs.{self.balance}")

# Sample usage of the Bank class
try:
    account1 = Bank("Alice", 25, 12345, 'S', 5000)
    account2 = Bank("Bob", 30, 67890, 'C', 15000)
    
    account1.deposit(2000)
    account1.withdraw(3000)
    
    account2.deposit(7000)
    account2.withdraw(10000)
    
    account1.display_account_details()
    account2.display_account_details()
except (InvalidAgeError, InvalidAccountNumberError, InvalidAccountTypeError, InvalidBalanceError, DepositLimitExceededError, WithdrawLimitExceededError) as e:
    print(f"Error: {e}")
