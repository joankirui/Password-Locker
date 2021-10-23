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