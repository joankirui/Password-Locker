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

