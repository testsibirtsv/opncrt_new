"""
Contains PersonalDetails class that provides help with
interacting with the Edit Account page.
"""


class PersonalDetails:
    """
    Use to edit user's personal info
    on the Edit Account page.
    """

    def __init__(self,
                 firstname=None,
                 lastname=None,
                 email=None,
                 telephone=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.telephone = telephone

    def __repr__(self):
        return "{} {} {} {}".format(self.firstname,
                                    self.lastname,
                                    self.email,
                                    self.telephone)

    def __eq__(self, other):
        return self.firstname == other.firstname \
               and self.lastname == other.lastname \
               and self.email == other.email \
               and self.telephone == other.telephone
