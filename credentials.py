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