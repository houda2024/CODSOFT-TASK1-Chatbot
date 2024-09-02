class Chatbot:
    def __init__(self):
        pass

    def get_response(self, user_input):
        user_input = user_input.lower()

        if "hello" in user_input:
            return "Hi there! How can I assist you today?"
        elif "what is your name" in user_input or "who are you" in user_input:
            return "I’m a simple rule-based chatbot, here to help you!"
        elif "bye" in user_input:
            return "Goodbye! Feel free to come back anytime."
        else:
            return "I'm sorry, I didn’t quite catch that. Could you please rephrase?"
