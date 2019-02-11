import unittest # Importing the unittest module
from user import Account # Importing the Account class

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Account("Florence","Mbabazi","pswd12345",) # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,'Florence')
		self.assertEqual(self.new_user.last_name,'Mbabazi)
		self.assertEqual(self.new_user.password,'pswd12345')



if __name__ == '__main__':
    unittest.main()