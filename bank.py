import businessbankaccount
import bankaccount
import os
import studentbankaccount
import xml.etree.ElementTree as ET


def add_new_account(account):
    f = open("my_bank_account.xml", "r")
    s = f.read()
    f = open("my_bank_account.xml", "w")
    if isinstance(account, businessbankaccount.BusinessBankAccount):
        f.write(s[:-11] + forBusinessBankAccount(account) + '</accounts>')
    elif isinstance(account, studentbankaccount.StudentBankAccount):
        f.write(s[:-11] + forStudentBankAccount(account) + '</accounts>')
    elif isinstance(account, bankaccount.BankAccount):
        f.write(s[:-11] + forBankAccount(account) + '</accounts>')
    f.close()


def printAllAccounts(root, attr='id'):
    for account in root.findall('account'):
        currAtt = account.find(attr).text
        print(currAtt)


def removeAccountByAtt(root, val, attr):
    for account in root.findall('account'):
        currAtt = account.find(attr).text
        if currAtt == val:
            print("removing account...")
            root.remove(account)
    return root


def Withdraw_by_user_id(root, withdrawnum, val, attr ):
    for account in root.findall('account'):
        currAtt = account.find(attr).text
        if currAtt == val:
            print("tm")
            print(account.find('balance').text)
            account.find('balance').text = withdrawnum
            print(account.find('balance').text)

    return root


def getTreeAndRoot(path):
    tree = ET.parse(path)
    root = tree.getroot()
    return tree, root


def personalInfoXml(elements):
    st = ""
    st += "<name>" + elements.name + "</name>" + "\n"
    st += "<id>" + str(elements.id) + "</id>" + "\n"
    st += "<phone>" + elements.phone_number + "</phone>" + "\n"
    st += "<email>" + elements.email_address + "</email>" + "\n"
    return st


def forStudentBankAccount(elements: studentbankaccount.StudentBankAccount):
    st = "<account name='StudentBankAccount'>" + "\n"
    st += personalInfoXml(elements)
    st += "<balance>" + str(elements.balance) + "</balance>" + "\n"
    st += "<college>" + elements.college_name + "</college>" + "\n"
    st += "</account>" + "\n"
    return st


def forBusinessBankAccount(elements: businessbankaccount.BusinessBankAccount):
    st = "<account name='BusinessBankAccount'>" + "\n"
    st += personalInfoXml(elements)
    st += "<balance>" + str(elements.balance) + "</balance>" + "\n"
    st += "<business_info>" + elements.business_info + "</business_info>" + "\n"
    st += "</account>" + "\n"
    return st


def forBankAccount(elements: bankaccount.BankAccount):
    st = "<account name='BankAccount'>" + "\n"
    st += personalInfoXml(elements)
    st += "<balance>" + str(elements.balance) + "</balance>" + "\n"
    st += "</account>" + "\n"
    return st


def hasXmlFile():
    return os.path.exists('./my_bank_account.xml')


def buildXmlFile():
    if not hasXmlFile():
        f = open("my_bank_account.xml", "w")
        f.write("\n" + "<accounts>" + "</accounts>" + "\n")
        f.close()


def main():
    """
    To remove an account with ID number
    """
    # tree, root = getTreeAndRoot('my_bank_account.xml')
    # id_num = input("Enter the ID to remove: ")
    # print('Accouts before removing:')
    # printAllAccounts(root)
    # print("--" * 10)
    # removeAccountByAtt(root, val=id_num, attr='id')
    # print('Accounts after removing:')
    # printAllAccounts(root)
    # print("--" * 10)
    # print('saving to file: my_bank_account.xml')
    # print("--" * 10)
    # tree.write('my_bank_account.xml')
    # tree2, root2 = getTreeAndRoot('my_bank_account.xml')
    # print('Accounts in the new file:')
    # printAllAccounts(root2)
    # print("--" * 10)

    """
    To add an account : 
    """
    # account_to_add = studentbankaccount.StudentBankAccount(5, "tamar", "054-6837579", "tamar.samara@gmail.com", 500,
    #                                                        "Sela college")
    # add_new_account(account_to_add)
    # account_to_add = studentbankaccount.StudentBankAccount(6, "kareen", "052-6524578", "kareen@gmail.com", 700,
    #                                                        "itsafe college")
    # add_new_account(account_to_add)
    # account_to_add = businessbankaccount.BusinessBankAccount(7, "rola", "054-2581325", "rula@gmail.com", 800,
    #                                                          "Rola is the businesswoman")
    # add_new_account(account_to_add)
    # account_to_add = bankaccount.BankAccount(8, "adham", "054-1282555", "adham@gmail.com", 1000)
    # add_new_account(account_to_add)

    tree, root = getTreeAndRoot('my_bank_account.xml')
    id_num = input("Enter the ID to change the balance: ")
    withdrawnum = int(input("Enter the amount to change the balance: "))
    Withdraw_by_user_id(root, withdrawnum, val=id_num, attr='id')


if __name__ == "__main__":
    main()
