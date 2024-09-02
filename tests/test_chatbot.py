import unittest
from src.chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_greetings(self):
        self.assertEqual(self.chatbot.get_response("Hello"), "Hi there! How can I assist you today?")

    def test_name_query(self):
        self.assertEqual(self.chatbot.get_response("What is your name?"), "I’m a simple rule-based chatbot, here to help you!")

    def test_farewell(self):
        self.assertEqual(self.chatbot.get_response("bye"), "Goodbye! Feel free to come back anytime.")

    def test_default_response(self):
        self.assertEqual(self.chatbot.get_response("What time is it?"), 
                         "I'm sorry, I didn’t quite catch that. Could you please rephrase?")
    
if __name__ == "__main__":
    unittest.main()
