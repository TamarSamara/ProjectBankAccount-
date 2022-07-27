import personalinfo


class BankAccount(personalinfo.PersonalInfo):
    def __init__(self, Id: int, name: str, phone_number: str, email_address: str, balance: float):
        super().__init__(Id, name, phone_number, email_address)
        self.balance = balance

    def __str__(self) -> str:
        return f'{super().__str__()} Balance is:{self.balance}'

    def Withdraw(self, money: float):
        self.balance -= money

    def Deposit(self, money: float):
        self.balance += money
