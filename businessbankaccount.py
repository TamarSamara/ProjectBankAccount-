import bankaccount


class BusinessBankAccount(bankaccount.BankAccount):
    def __init__(self, Id: int, name: str, phone_number: str, email_address: str, balance: float, business_info: str):
        super().__init__(Id, name, phone_number, email_address, balance)
        self.business_info = business_info

    def __str__(self) -> str:
        return f'{super().__str__()} business_info:{self.business_info}'

    def withdraw(self, amount):
        self.balance = self.balance - (amount * (1.50 / 100))

    def deposit(self, amount):
        self.balance = self.balance - (amount * (1.50 / 100))
