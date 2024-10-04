class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Cannot deposit zero or negative funds")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        elif amount > 0:
            self.__balance -= amount
        else:
            raise ValueError("Cannot withdraw zero or negative funds")

def main():
            account_number = f"{345678:010}"
            balance = 1000
            account_user1 = BankAccount(account_number, balance)
            print(f"Account current saldo is: {account_user1.get_balance()}$")
            print(f"User's account private bank number is: {account_user1.get_account_number()}")
            print(f"You want to withdraw: {600}$"), account_user1.withdraw(600)
            print(f"Account current saldo is: {account_user1.get_balance()}$")

main()
