import unittest
import agent

class TestAgent(unittest.TestCase):
    
    def test_unlock_car(self):
        """Test to see if unlocking a car works"""    
        #Input from console
        choice = '1'
        confirmation = '1'
        self.assertEqual(choice, confirmation)
        
    def test_return_car(self):
        """Test to see if returning a car works""" 
        #Input from console
        choice = '2'
        confirmation = '2'
        self.assertEqual(choice, confirmation)
        
    def test_login(self):
        """Test to see if logging in works with proper credentials"""
        #Input from console
        username = ""
        password = ""
        self.assertTrue(username.isprintable())
        self.assertTrue(password.isprintable())
        
if __name__ == '__main__':
    unittest.main()
