import unittest # Importing the unittest module
import pyperclip # Importing the pyperclip module
from user import User # Importing the User class
from credentials import Credentials # Importing the Credentials class



class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Florence","Mbabazi","pswd12345",) # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Florence")
		self.assertEqual(self.new_user.last_name,"Mbabazi")
		self.assertEqual(self.new_user.password,"pswd12345")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		method to test whether the login in function check_user works as expected
		'''
        self.new_user = User('Florence','Mbabazi,'pswd12345')
		self.new_user.save_user()
		users = User('Bety','Mbabazi','pswd12345')
		users.save_user()

		for user in User.users_list:
			if user.first_name == users.first_name and user.password == users.password:
				current_user = user.first_name
		return current_user

        self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))
    
    def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Credential('Mary','Facebook','maryjoe','pswd100')

    def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'Mary')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'maryjoe')
		self.assertEqual(self.new_credential.password,'pswd100')

    def test_save_credentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Jane','Twitter','maryjoe','pswd100')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)

    def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		Credential.credentials_list = []
		User.users_list = []

	def test_display_credentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Jane','Twitter','maryjoe','pswd100')
		twitter.save_credentials()
		gmail = Credential('Jane','Gmail','maryjoe','pswd200')
		gmail.save_credentials()
		self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

    def test_find_by_site_name(self):
		'''
		Test to check if the find_by_site_name method returns the correct credential
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Jane','Twitter','maryjoe','pswd100')
		twitter.save_credentials()
		credential_exists = Credential.find_by_site_name('Twitter')
		self.assertEqual(credential_exists,twitter) 

    def test_copy_credential(self):
		'''
		Test to check if the copy a credential method copies the correct credential
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Jane','Twitter','maryjoe','pswd100')
		twitter.save_credentials()
		find_credential = None
		for credential in Credential.user_credentials_list:
				find_credential =Credential.find_by_site_name(credential.site_name)
				return pyperclip.copy(find_credential.password)
		Credential.copy_credential(self.new_credential.site_name)
		self.assertEqual('pswd100',pyperclip.paste())
		print(pyperclip.paste())           


if __name__ == '__main__':
    unittest.main()