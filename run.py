#!/usr/bin/env python3.6
from passlock import User, Credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user
def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()
def login_user(username,password):
    '''
    function that checks whether a user exists and then login the user
    '''
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_credentials(account,user_name,password):
    '''
    Function that creates new credentials
    '''
    new_credentials = Credentials(account,user_name,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
def del_credentials(credentials):
    '''
    Function to delete credentials
    '''
    credentials.delete_credentials()
def find_credentials(account):
    '''
    Function that finds credentials by account and returns the credentials
    '''
    return Credentials.find_by_account(account)
def check_existing_credentials(account):
    '''
    Function that checks if credentials exist with that account and return a Boolean
    '''
    return Credentials.credentials_exist(account)
def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    '''
    A function that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    '''
    return Credentials.copy_password(account)
def main():
    print("Hello welcome to your credentials store...\n Use these short codes:\n ca --create new account\n ha --have an existing account") 
    short_code = input("").lower().strip()

    if short_code == 'ca':
        print("Sign up")
        print("-"*20)

        username = input("Username: ")
        while True:
            print("ip - to input your own password:\n gp - to generate random password")
            password_choice = input().lower().strip()
            if password_choice == 'ip':
                password = input("Enter Password\n")
                break
            elif password_choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password choice")
        save_user(create_user(username,password)) # create and save new user.
        print("-"*20)
        print(f"Hello {username} Your account has been created successfully! Your password is {password}")
        print("-"*20)
    elif short_code == 'ha':
        print("*"*30)
        print("Enter your username and your password:")
        print("*"*30)
        username = input("Username: ")
        password = input("Password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome to Credentials store")
            print('\n')
    while True:
        print("Use these short codes:\n cc - Create a new credential \n dc - Display credentials\n fc - Find a credential\n gp - Generate a random password \n d - Delete a credential \n ex - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("-"*20)
            print("Acount name ...")
            account = input().lower()
            print("Your Account username")
            user_name = input()
            while True:
                print("ip - to input your own password:\n gp - to generate random password")
                password_choice = input().lower().strip()
                if password_choice == 'ip':
                    password = input("Enter Password\n")
                    break
                elif password_choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password choice")
                    
            save_credentials(create_credentials(account,user_name,password))
            print('\n')
            print(f"Account Credential for: {account} -UserName: {user_name} - Password:{password} created succesfully")
            print('\n')
        elif short_code == 'dc':
            if display_credentials():
                print("Here's your list of credentials: ")
                print('_'*40)
                print('~'*40)
                for account in display_credentials():
                    print(f"Account{account.account} \n UserName:{user_name}\n Password:{password}")
                print("_"*40)
            else:
                print("\n")
                print("You dont seem to have any credentials saved yet")
                print("\n")
        elif short_code == "fc":
            print("Enter the account name you want to search for")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-'*50)
                print(f"UserName: {search_credential.user_name} Password:{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")
        elif short_code == 'gp':
            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using credentials store ..")
            break
        else:
            print("I really didn't get that.Please use the short codes")
    else:
        print("Please enter a valid input to continue")

if __name__== '__main__':
    main()


