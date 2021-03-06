import unittest #Importing the unittest module
import pyperclip
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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test has run
        '''
        Credentials.credentials_list = []
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Gmail","Lalakirui","we56fng")  #new Credentials
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a Credential from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Gmail","Lalakirui","we56fng") #new credentials
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials() #deleting a credentials object
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_account(self):
        '''
        test to check if we can find credentials by account and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Gmail","Lalakirui","we56fng") #new contact
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_account("Gmail")

        self.assertEqual(found_credentials.user_name,test_credentials.user_name)
        self.assertEqual(found_credentials.password,test_credentials.password)

    def test_credentials_exist(self):
        '''
        test to check if we can return a Boolean if we cannot find the credentials
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Gmail","Lalakirui","we56fng") # new contact
        test_credentials.save_credentials()

        credentials_exist = Credentials.credentials_exist("Gmail")

        self.assertTrue(credentials_exist)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from credentials
        '''
        self.new_credentials.save_credentials()
        Credentials.copy_password("we56fng")
        self.assertEqual(self.new_credentials.password,pyperclip.paste)
        
if __name__ == "__main__":
    unittest.main()