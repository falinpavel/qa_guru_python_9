

class User:
    def __init__(self, first_name, last_name, user_email,
                 gender, user_number, current_address):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.gender = gender
        self.user_number = user_number
        self.current_address = current_address

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.user_email,
                     self.gender, self.user_number, self.current_address))
