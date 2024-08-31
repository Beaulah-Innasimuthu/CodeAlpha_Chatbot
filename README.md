# CodeAlpha_Chatbot
# FAQ Chatbot GUI Application

## Overview

This project is a simple FAQ chatbot implemented with a graphical user interface (GUI) using Python's `tkinter` library. The chatbot can handle frequently asked questions, greetings, and expressions of thanks. It uses Natural Language Toolkit (NLTK) for text preprocessing and matching.

## Features

- Handle FAQs with predefined responses.
- Respond to common greetings and expressions of gratitude.
- Interactive GUI for user-friendly interaction.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `nltk`

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/faq-chatbot.git
   cd faq-chatbot
2. **Install Required Python Libraries**

   Ensure you have Python installed. Then, install the necessary libraries using pip:

   ```bash
   pip install nltk
3. **Download NLTK Resources**

   Run the following code to download the required NLTK resources:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
## Usage

1. **Run the Application**

   Execute the Python script to launch the GUI application:

   ```bash
   python chatbot_gui.py
2. **Interact with the Chatbot**

   - Type your question or greeting into the input field.
   - Click the "Send" button to receive a response from the chatbot.
   - The chat history will display both user input and chatbot responses.

## Code Overview

- **`chatbot_gui.py`**: Main script for running the GUI application. Contains the following components:
  - **`FAQChatbot` Class**: Handles the logic for processing user input and finding the most relevant FAQ response. Utilizes NLTK for text preprocessing and matching.
  - **`ChatbotGUI` Class**: Manages the tkinter interface for the chatbot. Includes methods for updating the chat history and handling user interactions.

- **`faqs` Dictionary**: Stores frequently asked questions, greetings, and thank-you responses along with their answers. Example format:
  
  ```python
  faqs = {
      "greetings": {
          "hello": "Hi there! How can I help you today?",
          "hi": "Hello! What can I assist you with?",
          "good morning": "Good morning! How can I assist you today?"
      },
      "thanks": {
          "thank you": "You're welcome! If you have any other questions, feel free to ask.",
          "thanks": "My pleasure! Let me know if you need further assistance."
      },
      "faqs": {
          "order status": "To check your order status, please visit our tracking page.",
          "return policy": "Our return policy allows returns within 30 days of purchase.",
          "contact support": "You can contact support via email at support@example.com."
      }
  }
