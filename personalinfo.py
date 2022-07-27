class PersonalInfo:

    def __init__(self, Id: int, name: str, phone_number: str, email_address: str):
        self.id = Id
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    def __str__(self) -> str:
        return f'id:{self.Id} name:{self.name} Phone number:{self.phone_number} Email address:{self.email_address}'
