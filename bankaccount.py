import xml.etree.ElementTree as ET
import os


class PersonalInfo:
    # phone number str?
    def __init__(self, Id: int, name: str, phone_number: str, email_address: str):
        self.id = Id
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

# yemken a3mal name abel Id
    def __str__(self) -> str:
        return f'id:{self.Id} name:{self.name} Phone number:{self.phone_number} Email address:{self.email_address}'



class BankAccount(PersonalInfo):
    def __init__(self, Id: int, name: str, phone_number: str, email_address: str, balance: float):
        super().__init__(Id, name, phone_number, email_address)
        self.balance = balance

    def __str__(self) -> str:
        return f'{super().__str__()} Balance is:{self.balance}'

    def Withdraw(self, money: float):
        self.balance -= money

    def Deposit(self, money: float):
        self.balance += money

# https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
# def deposit(self):
#     amount = float(input("Enter amount to be Deposited: "))
#     self.balance += amount
#     print("\n Amount Deposited:", amount)
#
#
# def withdraw(self):
#     amount = float(input("Enter amount to be Withdrawn: "))
#     if self.balance >= amount:
#         self.balance -= amount
#         print("\n You Withdrew:", amount)
#     else:
#         print("\n Insufficient balance  ")
#
#
# def display(self):
#     print("\n Net Available Balance=", self.balance)



class StudentBankAccount(BankAccount):
    def __init__(self, Id: int, name: str, phone_number: str, email_address: str, balance: float, college_name: str):
        super().__init__(Id, name, phone_number, email_address, balance)
        self.college_name = college_name
        if balance < 0:
            raise ValueError("Student can’t have negative balance ")

    def __str__(self) -> str:
        return f'{super().__str__()} college_name:{self.college_name}'

    # لا يمكن أن يكون لدى الطالب رصيد سلبي
    # ?????????????????????
    def Withdraw(self, money: float):
        self.balance += super().Withdraw(money) - super().Withdraw(money) * 1.5

    def Deposit(self, money: float):
        self.balance += super().Deposit(money) - super().Deposit(money) * 1.5


class BusinessBankAccount(BankAccount):
    def __init__(self, Id: int, name: str, phone_number: str, email_address: str, balance: float, business_info: str):
        # if balance < 0: raise ValueError("Student can’t have negative balance ")
        super().__init__(Id, name, phone_number, email_address, balance)
        self.business_info = business_info

    def __str__(self) -> str:
        return f'{super().__str__()} business_info:{self.business_info}'

# ستكون العمولات 150٪ لعمليات السحب والإيداع الخاصة بحساب BusinessBankAccount المتعلق بضربات BankAccount



class Bank:
    def __init__(self):
        pass

    # load_and_parse_init_data

    def add_new_account(self):
        pass

    # Push in saveinxml python file

    def delete_by_userID(self):
        tree = ET.parse('my_bank_account.xml')
        root = tree.getroot()
        for account in root.findall('account'):
            pid = account.find('id').text
            if pid == '5':
                print("tamaaaaaaaaaaaaaaaaaaaar")

    def print_xml(self):
        tree = ET.parse('my_bank_account.xml')
        root = tree.getroot()
        print(root)
        # to print xml data
        for account in root.findall('account'):
            print(account.get('type'))
            print(account.find('name').text)
            print(account.find('phone').text)
            print(account.find('email').text)
            if account.findtext("college"):
                print(account.find('college').text)
            print(" \n")

# from xml.etree.ElementTree import ElementTree
# import xml.etree.ElementTree as ET
#
# file = ET.parse('my_bank_account.xml')
# root = file.getroot()
# for elem in root.findall('account'):
#     if elem.find('id') == 5:
#             elem.remove(elem.find('id'))
#
# file.write('my_bank_account.xml')



def personalInfoXml(a):
    st = ""
    st += "<name>" + a.name + "</name>" + "\n"
    st += "<id>" + str(a.id) + "</id>" + "\n"
    st += "<phone>" + a.phone_number + "</phone>" + "\n"
    st += "<email>" + a.email_address + "</email>" + "\n"
    return st


def forStudentBankAccount(a: StudentBankAccount):
    st =  "<account name='StudentBankAccount'>" + "\n"
    st += personalInfoXml(a)
    st += "<balance>" + str(a.balance) + "</balance>" + "\n"
    st += "<college>" + a.college_name + "</college>" + "\n"
    st += "</account>" + "\n"
    return st


def forBusinessBankAccount(a: BusinessBankAccount):
    st =  "<account name='BusinessBankAccount'>" + "\n"
    st += personalInfoXml(a)
    st += "<balance>" + str(a.balance) + "</balance>" + "\n"
    st += "<business_info>" + a.business_info + "</business_info>" + "\n"
    st += "</account>" + "\n"
    return st


def forBankAccount(a: BankAccount):
    st =  "<account name='BankAccount'>" + "\n"
    st += personalInfoXml(a)
    st += "<balance>" + str(a.balance) + "</balance>" + "\n"
    st += "</account>" + "\n"
    return st


def hasXmlFile():
    return os.path.exists('./my_bank_account.xml')


def buildXmlFile():
    if not hasXmlFile():
        # f = open("my_bank_account.xml", "w")
        # f.close()
        f = open("my_bank_account.xml", "w")
        f.write("\n" + "<accounts>" + "</accounts>" + "\n")
        f.close()


def AddAccountToXmlFile(a):
    f = open("my_bank_account.xml", "r")
    s = f.read()
    f.close()
    f = open("my_bank_account.xml", "w")

    with open(r"my_bank_account.xml", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[:-1])
    if isinstance(a, BusinessBankAccount):
        f.write(s + forBusinessBankAccount(a) + '</accounts>')
    elif isinstance(a, StudentBankAccount):
        f.write(s + forStudentBankAccount(a) + '</accounts>')
    elif isinstance(a, BankAccount):
        f.write(s + forBankAccount(a) + '</accounts>')

    f.close()

# buildXmlFile()

# , name, Id, phone_number, email_address, balance, college_name):
emp1 = StudentBankAccount(5, "tamar", "054-6837579", "tamar.samara@gmail.com", 500, "Sela college")
AddAccountToXmlFile(emp1)
# emp2 = StudentBankAccount(6, "kareen", "052-6524578", "kareen@gmail.com", 700, "itsafe college")
# AddAccountToXmlFile(emp2)
# emp3=BusinessBankAccount(7, "rola", "054-2581325", "rula@gmail.com", 800,"Rola is the businesswoman")
# AddAccountToXmlFile(emp3)
# emp4=BankAccount(8, "adham", "054-1282555", "adham@gmail.com", 1000)
# AddAccountToXmlFile(emp4)

# remove_by_ID(5)


# Bank.delete_by_userID()


#"******************"

tree = ET.parse('my_bank_account.xml')
root = tree.getroot()
print(root)
# to print xml data
# for account in root.findall('account'):
#     print(account.get('type'))
#     print(account.find('name').text)
#     print(account.find('phone').text)
#     print(account.find('email').text)
#     if account.findtext("college"):
#         print(account.find('college').text)
#     print(" \n")


num = 5
for account in root.findall('account'):
    pid = account.find('id').text
    with open(r"my_bank_account.xml", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()

    if pid == '6':
        print("tejmd")
        # fp.writelines(lines[:-1])
# import xml.etree.ElementTree as ET
#
# tree = ET.parse('stam.xml')
# root = tree.getroot()
# print(root)
# print("****")
# for country in root.findall('country'):
#     print(country.get('name'))
#     print(country.find('rank').text)
#     print(country.find('year').text)
#     print(country.find('gdppc').text)



# from xml.dom import minidom
#
# # parse an xml file by name
# file = minidom.parse('my_bank_account.xml')
#
# #use getElementsByTagName() to get tag
# models = file.getElementsByTagName('account')
#
# # one specific item attribute
# print('model #2 attribute:')
# print(models[1].attributes['name'].value)