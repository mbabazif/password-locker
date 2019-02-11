class Account:
    """
    Class that generates new instances of accounts.
    """

    users_list = [] # Empty Account list

    def __init__(self,first_name,last_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    def save_user(self):
		'''
		 test_save_contact test case to test if the contact object is saved into
         the contact list
		'''
		Account.users_list.append(self)    