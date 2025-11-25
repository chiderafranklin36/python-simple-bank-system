import os
import random

Name = {}
create_account_pin = None
accounts = {}

def create_account_interactive():
    Name['user'] = input('Enter Your Name: ')

    # create random ID to assign User
    account_ID = ''.join(str(random.randint(1, 100)) for _ in range(6))
    print(f"welcome, {Name['user']}! Your account_ID is {account_ID}")

    while True:
        try:
            Pin = int(input('Enter Your New 4-digit PIN: '))
            if 1000 <= Pin <= 9999:
                create_account_pin = Pin
                print('Account creation complete')
                accounts[account_ID] = {
                    "Name": Name['user'],
                    "Pin": create_account_pin,
                    "balance": 0.0
                }
                print('\nYour account details: ')
                print(accounts[account_ID])
                break
            else:
                print('Invalid input, Please enter a 4 digit number')
        except ValueError:
            print('Invalid input, please be sure to input a number')

    print('\nProceeding to login page...\n')
    import login
    return login.login(account_ID, accounts)

if __name__ == "__main__":
    create_account_interactive()