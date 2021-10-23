import unittest #Importing the unittest module
from passlock import User #Importing the User class
from passlock import Credentials #Importing the Credentials class

class TestUser(unittest.TestCase):
    '''
    A Test class that defines test cases for the User class
    '''
    def setUp(self):
        '''
        Method that runs before each individual test methods run.
        '''
        self.new_user = User("JoanKirui","Wxyth1")
    def test_init(self):
        '''
        test init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"JoanKirui")
        self.assertEqual(self.new_user.password,"Wxyth1")
    def test_save_user(self):
        '''
        test_save_user test case to test if a new user instance has been saved into the User list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)
    def test_display_user(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_user(),User.user_list)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviours
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Ig","Joan_Kirui","weg5uytg")
    def test_init(self):
        '''
        Test case to check if a new Credentials instance has been initialized correctly
        '''
        self.assertEqual(self.new_credentials.account,"Ig")
        self.assertEqual(self.new_credentials.user_name,"Joan_Kirui")
        self.assertEqual(self.new_credentials.password,"weg5uytg")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)
        
if __name__ == "__main__":
    unittest.main()