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



     # Init method up here
    def save_user(self):

        '''
        save_account method saves user objects into user_list
        '''

        User.user_list.append(self)
    # delete account
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)





 # create contact objectself.assertEqual(self.new_user.first_name,"yvette")
       