!pip install nltk

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

import tkinter as tk
from tkinter import scrolledtext

class FAQChatbot:
    def __init__(self, faqs):
        self.faqs = faqs
        self.stop_words = set(stopwords.words('english'))

    def preprocess(self, text):
        tokens = word_tokenize(text.lower())
        filtered_tokens = [word for word in tokens if word.isalnum() and word not in self.stop_words]
        return filtered_tokens

    def get_response(self, question):
        question_tokens = self.preprocess(question)
        best_match = None
        best_score = 0

        for faq, answer in self.faqs.items():
            faq_tokens = self.preprocess(faq)
            common_tokens = set(question_tokens) & set(faq_tokens)
            score = len(common_tokens)

            if score > best_score:
                best_score = score
                best_match = answer

        return best_match if best_match else "Sorry, I don't understand your question."

# Define your FAQ data including greetings
faqs = {
    "What is your return policy?": "You can return items within 30 days for a full refund.",
    "How can I track my order?": "You can track your order using the tracking number provided in the confirmation email.",
    "Do you ship internationally?": "Yes, we offer international shipping to most countries.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, PayPal, and American Express.",
    "Hello": "Hi there! How can I help you today?",
    "Hi": "Hello! How can I assist you?",
    "Good morning": "Good morning! How can I assist you today?",
    "Good afternoon": "Good afternoon! How can I help you?",
    "Good evening": "Good evening! How can I assist you?"
    "Thank you": "You're welcome! If you have any other questions, feel free to ask.",
    "Thanks": "You're welcome! Let me know if there's anything else I can help with.",
    "Thanks a lot": "You're welcome! I'm here to help with anything else you need.",
    "Thank you very much": "You're very welcome! If you need further assistance, just ask."
}


# Create an instance of the chatbot
chatbot = FAQChatbot(faqs)

# Set up the GUI
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FAQ Chatbot")

        # Create and place the chat history area
        self.chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20, width=50)
        self.chat_history.grid(row=0, column=0, columnspan=2)

        # Create and place the user input area
        self.user_input = tk.Entry(root, width=50)
        self.user_input.grid(row=1, column=0)

        # Create and place the send button
        self.send_button = tk.Button(root, text="Send", command=self.get_user_input)
        self.send_button.grid(row=1, column=1)

    def get_user_input(self):
        user_text = self.user_input.get()
        self.user_input.delete(0, tk.END)
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, "You: " + user_text + '\n')
        response = chatbot.get_response(user_text)
        self.chat_history.insert(tk.END, "Chatbot: " + response + '\n')
        self.chat_history.configure(state='disabled')
        self.chat_history.yview(tk.END)

# Create the main window
root = tk.Tk()
gui = ChatbotGUI(root)
root.mainloop()
