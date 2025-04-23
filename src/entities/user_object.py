""" A module for formatting for using user information throughout the application."""

class UserObject:
    """ Takes a json of user information and stores it in the object"""
    def __init__(self, user_data):
        """ Takes a json of user information and stores it in the object"""
        self.user = {
            "uuid":"",
            "name":"",
            "email":"",
            "password":""
        }
        #Fill user object with form data
        for key,data in user_data.items():
            if key in self.user:
                self.user[key] = data

    def get_user_id(self):
        """ Returns user id """
        return self.user["uuid"]
    def get_user_name(self):
        """ Returns user name """
        return self.user["name"]
    def get_user_email(self):
        """ Returns user email """
        return self.user["email"]
    def get_user_password(self):
        """ Returns user password """
        return self.user["password"]
