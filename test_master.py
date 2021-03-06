import unittest

class TestAgent(unittest.TestCase):
    
    def test_agentpi_login(self):
        """Tests if agent pi can login through master"""
        param = {
            'username' : "seth", 
            'password' : "testing"
        }
        response = param

        self.assertEqual(response.text, "User Exists")
        
    def test_agentpi_connection(self):
        """Test connection with Agent Pi"""
        response = socket_utils.sendJson(conn, { "authenticated": True })

        self.assertTrue(response.text == "authenticated")
        
    def test_login(self):
        """Test logging in"""
        #Input from console
        username = ""
        password = ""
        self.assertTrue(username.isprintable())
        self.assertTrue(password.isprintable())
        
if __name__ == '__main__':
    unittest.main()
