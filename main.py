import tkinter as tk
from src import ChatbotUI  # Ensure this matches the `__init__.py` configuration

def main():
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
