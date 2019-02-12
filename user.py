class User:
    """
    Class that generates new instances of user.
    """

    user_list = [] # Empty user list

    def __init__(self,first_name,last_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    def save_user(self):
		'''
		 test_save_user test case to test if the contact object is saved into
         the user list
		'''
		User.user_list.append(self) 

    def delete_user(self):

        '''
        delete_user method deletes a saved contact from the contact_list
        '''

        Contact.user_list.remove(self)

class Credentials:
  
  '''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credentials_list =[]
	user_credentials_list = []
	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

  def __init__(self,user_name,account_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.account_name = account_name
		self.password = password

    def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		# global users_list
		Credential.credentials_list.append(self)

  @classmethod
	def display_credentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list
  

	