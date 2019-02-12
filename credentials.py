class User:
    """
    Class that generates new instances of contacts User.
    """
    user_list = [] #Empty user list
    def __init__(self,first_name,last_name,user_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

     def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		User.users_list.append(self) 
class Credential:
    """
    class that generates new instances
    """    
    credentials_list = []    

        def __init__(self,user_name,site_name,account_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		# global users_list
		Credential.credentials_list.append(self)