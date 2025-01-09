from random import randrange
from typing import Set


class BankAccount:
    all_account_number: Set = set()

    def __init__(self, name):
        self.account_number = 0
        while True:
            if (an := randrange(1000, 100000)) not in BankAccount.all_account_number:
                BankAccount.all_account_number.add(an)
                self.account_number = an
                break
        self.name = name
        self.balance = 0

    def display(self) -> None:
        """
        Show account balance
        :return:
        """
        print(f"Hi, {self.name}\n Your current balance: {self.balance}")

    def deposit(self) -> None:
        """
        Increase account balance
        :return:
        """
        amount = float(input("Please enter amount to deposit : "))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        """
        withdraw from bank account
        :return:
        """
        amount = float(input("Please enter amount to withdraw : "))
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
        self.display()


def main():
    acc1 = BankAccount("reza dolati")
    print(40 * "_")
    print(f"Account_number: {acc1.account_number}")
    print(40 * "_")
    acc1.display()

    while True:
        choice = int(input(f"Enter:\n1. to see your balance\n2. to deposit\n"
                           f"3. to withdraw\n4. to exit.\n\t\tYOUR CHOICE: "))
        if choice == 1:
            acc1.display()
        elif choice == 2:
            acc1.deposit()
        elif choice == 3:
            acc1.withdraw()
        elif choice == 4:
            break
        else:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
