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

	def create_user(first_name,last_name,user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,user_name,password)
    return new_user

    def save_use(user):
    """
    Function to save user
    """
    user.save_user()

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

	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass