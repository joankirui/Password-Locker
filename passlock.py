import string
import random
import pyperclip
class User:
    '''
    Class that generates new instances of user
    '''

    user_list = [] #Empty user list

    def __init__(self,username,password):
        '''
        method that defines the properties of a user
        '''
        self.username = username
        self.password = password
    
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

class Credentials:
    '''
    Create credentials class to help create new objects of credentials
    '''
    credentials_list = []  
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user 
    def __init__(self,account,user_name,password):
        '''
        method that defines user credentials to be stored
        '''
        self.account = account
        self.user_name = user_name
        self.password = password
    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''
        Credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved Credential from the credentials_list
        '''
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in account name and returns credentials that matches that account name
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials
    @classmethod
    def credentials_exist(cls,account):
        '''
        Method that checks if credentials exist in the credentials list
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    # @classmethod
    # def copy_password(cls,account):
    #     credentials_found = Credentials.find_by_account(account)
    #     pyperclip.copy(credentials_found.password)

    def generatePassword(stringLength=8):
        '''Generate a random password string of letters and digits and special characters'''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
