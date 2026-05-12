import unittest

from check_pwd import check_pwd


class CheckPasswordTests(unittest.TestCase):
    
    def test_length_too_short(self):
        self.assertFalse(check_pwd("Pass1!"))
    # def test_length_too_long(self):
    #     self.assertTrue(check_pwd("ThisIsAVeryLongPassword123!"))
    def test_second_length_too_long(self):
        self.assertFalse(check_pwd("ThisIsAVeryLongPassword123!"))
    # def test_fail_on_all_uppercase_present(self):
    #     self.assertFalse(check_pwd("password"))
    def test_fail_on_all_uppercase_present2(self):
        self.assertFalse(check_pwd("PASSWORD123!"))
    def test_fail_on_all_lowercase_present(self):
        self.assertFalse(check_pwd("password123!"))
    

if __name__ == "__main__":
    unittest.main()