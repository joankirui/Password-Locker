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