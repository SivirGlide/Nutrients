class UserOBJ:
    def __init__(self, user_data):
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
