# Rule-Based Chatbot
This project is a simple yet elegant rule-based chatbot that responds to user inputs based on predefined rules. It is built using Python's Tkinter library for the user interface, and it utilizes basic if-else statements and pattern matching techniques to identify user queries and provide appropriate responses.

# Project Structure


Rule_based_chatbot/
│
├── venv/                # Virtual environment (not included in version control)
├── src/                 # Source code directory
│   ├── __init__.py      # Initialization file for the src module
│   ├── chatbot.py       # Core logic for the chatbot's response mechanism
│   ├── gui.py           # Graphical User Interface for the chatbot
│
├── tests/               # Unit tests directory
│   ├── __init__.py      # Initialization file for the tests module
│   ├── test_chatbot.py  # Unit tests for the chatbot logic
│
├── main.py              # Entry point to run the chatbot
└── README.md            # Project documentation (this file)

# Features
Rule-Based Responses: The chatbot uses predefined rules to generate responses to user inputs.
Modern UI Design: The interface is designed to be visually appealing and user-friendly, using Tkinter.
Keyboard Interaction: Users can press "Enter" to send messages, making the chatbot more intuitive to use.

# Getting Started
#Prerequisites#
To run this project, you need to have the following installed on your machine:

Python 3.x: Ensure that Python is installed and added to your system's PATH.
## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Rule_based_chatbot.git
   cd Rule_based_chatbot

## Set Up a Virtual Environment:


python -m venv venv
Activate the Virtual Environment:

On Windows:


.\venv\Scripts\activate
On macOS/Linux:


source venv/bin/activate


Install Dependencies:

Since this project uses only the standard Python library (Tkinter), there are no additional packages to install. Tkinter is included with Python by default.

Running the Chatbot
Once the setup is complete, you can run the chatbot using the following command:

bash
Copy code
python main.py
Running Tests
To ensure that the chatbot's logic works as expected, you can run the unit tests. This project uses Python's built-in unittest framework.

Navigate to the Tests Directory:

bash
Copy code
cd tests
Run the Tests:

bash
Copy code
python -m unittest discover
This command will automatically discover and run all the test cases defined in the tests directory.

Usage
Interact with the Chatbot:

Type your message in the input field.
Press "Enter" or click "Send" to send your message.
Customization:

To modify the chatbot's responses, edit the rules dictionary in the chatbot.py file located in the src/ directory.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Tkinter: For providing a simple and powerful library to build the graphical interface.
Python: For being an awesome programming language.
