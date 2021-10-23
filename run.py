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
    
