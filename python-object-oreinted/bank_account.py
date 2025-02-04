from random import randrange
from typing import Set


class BankAccount:
    """
    Bank Account Management
    """
    all_account_numbers: Set[int] = set()

    def __init__(self, name: str) -> None:
        self.account_number: int = 0
        while True:
            if (an := randrange(1000, 100000)) not in BankAccount.all_account_numbers:
                BankAccount.all_account_numbers.add(an)
                self.account_number = an
                break
        self.name = name
        self.balance: float = 0

    def display(self) -> None:
        """
        Show account balance
        :return:
        """
        print(40 * '-')
        print(f'Hi, {self.name}\nYour Account Balance: {self.balance}')
        print(40 * '-')

    def deposit(self) -> None:
        """
        deposit money to account balance
        :return:
        """
        amount = float(input(f'Enter amount to deposit: '))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        """
        withdraw money of account balance
        :return:
        """
        amount = float(input(f'Enter amount to withdraw: '))
        if amount > self.balance:
            print('Insufficient Balance!')
        else:
            self.balance -= amount
        self.display()


def main():
    account_1 = BankAccount('Ali')
    print(account_1.account_number)
    account_1.display()
    while True:
        choice = input('Enter:\n1.to show balance.\n2.to Deposit.\n3.to withdraw.\n4.Exit\n'
                       '\t\tchoices:')

        if choice == '1':
            account_1.display()
        elif choice == '2':
            account_1.deposit()
        elif choice == '3':
            account_1.withdraw()
        elif choice == '4':
            break
        else:
            print('Please enter a Valid Number !')


if __name__ == '__main__':
    main()
