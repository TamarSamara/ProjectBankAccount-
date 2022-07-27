import bankaccount


class StudentBankAccount(bankaccount.BankAccount):
    def __init__(self, Id: int, name: str, phone_number: str, email_address: str, balance: float, college_name: str):
        super().__init__(Id, name, phone_number, email_address, balance)
        self.college_name = college_name
        if balance < 0:
            raise ValueError("Student can’t have negative balance ")

    def __str__(self) -> str:
        return f'{super().__str__()} college_name:{self.college_name}'

    def Withdraw(self, amount: float):
        if self.balance - amount >= 0:
            super().withdraw(amount)
