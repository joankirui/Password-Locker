#!/usr/bin/env python3.6
from passlock import User, Credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user