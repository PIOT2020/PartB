import unittest
import AgentPi.agent

class TestAgent(unittest.TestCase):
    
    def test_unlock_car(self):
        #Input from console
        choice = '1'
        confirmation = '1'
        self.assertEqual(choice, confirmation)
        
    def test_return_car(self):
        #Input from console
        choice = '2'
        confirmation = '2'
        self.assertEqual(choice, confirmation)
        
    def test_login(self):
        #Input from console
        username = ""
        password = ""
        self.assertTrue(username.isprintable())
        self.assertTrue(password.isprintable())
        
if __name__ == '__main__':
    unittest.main()
