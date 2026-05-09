import unittest

from check_pwd import check_pwd


class CheckPasswordTests(unittest.TestCase):
    
    def test_length_too_short(self):
        self.assertFalse(check_pwd("Pass1!"))
    

if __name__ == "__main__":
    unittest.main()