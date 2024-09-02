import tkinter as tk
from tkinter import scrolledtext
from src.chatbot import Chatbot

class ChatbotUI:
    def __init__(self, root):
        self.chatbot = Chatbot()
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")  # Set background color

        # Text area for chat history with improved design
        self.text_area = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, font=("Helvetica", 12), bg="#34495e", fg="white", bd=0)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Entry field for user input with custom styling
        self.entry_frame = tk.Frame(root, bg="#2c3e50")
        self.entry_frame.pack(padx=10, pady=10, fill=tk.X)

        self.entry = tk.Entry(self.entry_frame, font=("Helvetica", 14), bg="#ecf0f1", fg="#2c3e50", bd=0, relief=tk.FLAT)
        self.entry.pack(padx=10, pady=10, fill=tk.X, side=tk.LEFT, expand=True)
        self.entry.bind("<Return>", self.send_message_with_return)  # Bind Enter key to send message

        # Send button with custom design
        self.send_button = tk.Button(self.entry_frame, text="Send", font=("Helvetica", 12, "bold"), bg="#1abc9c", fg="white", bd=0, relief=tk.FLAT, command=self.send_message)
        self.send_button.pack(padx=10, pady=10, side=tk.RIGHT)

    def send_message_with_return(self, event):
        self.send_message()

    def send_message(self):
        user_input = self.entry.get().strip()
        if user_input:
            response = self.chatbot.get_response(user_input)

            self.text_area.configure(state='normal')
            self.text_area.insert(tk.END, f"You: {user_input}\n", "user")
            self.text_area.insert(tk.END, f"Chatbot: {response}\n\n", "bot")
            self.text_area.configure(state='disabled')

            self.text_area.yview(tk.END)  # Auto-scroll to the bottom
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    ui = ChatbotUI(root)
    root.mainloop()
