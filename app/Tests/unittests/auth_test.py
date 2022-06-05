import unittest
from app.Security.JWT.Auth import Auth


class Test_CreateAuthUser(unittest.TestCase):

    def login_empty_test(self):
        self.assertRaises(ValueError('login_is_empty'),
                          Auth('', '1565415321', 'dfds', 1))
