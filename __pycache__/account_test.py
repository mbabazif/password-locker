import unittest # Importing the unittest module
from user import Account # Importing the Account class

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the Account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Account("Florence","Mbabazi","pswd12345",) # create contact object


    def test_init(self):unitest
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,'Florence')
		self.assertEqual(self.new_user.last_name,'Mbabazi)
		self.assertEqual(self.new_user.password,'pswd12345')

    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_contact() # saving the new contact
        self.assertEqual(len(Account.user_list),1)
    



if __name__ == '__main__':
    unittest.main()