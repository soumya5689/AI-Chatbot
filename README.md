![image](https://github.com/user-attachments/assets/f8322bd5-d7db-4244-8f82-160a27f5bc7f)
﻿# AI-Chatbot
AI Assistant 🤖
This project is a Streamlit-based AI Assistant powered by Hugging Face models. The application provides conversational AI capabilities, enabling users to interact with an assistant that answers general questions in the user's preferred language.

Features
Conversational AI: Engage in a dialogue with the assistant.
Hugging Face Integration: Leverages Hugging Face models for generating intelligent responses.
Language Adaptability: Automatically detects and responds in the language used by the user.
Streamlit UI: Provides an intuitive and interactive user interface.

Requirements
Python 3.8 or higher
Hugging Face API Key
Internet connection

Installation
1. Clone the repository
git clone <repository_url>
cd <repository_name>

2. Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

6. Configure the environment variables
Create a .env file in the project root and add your Hugging Face API key:
HUGGINGFACE_API_KEY=your_huggingface_api_key
Run the Streamlit app:
streamlit run app.py
Open the app in your web browser (default: http://localhost:8501).

Start chatting with the AI assistant by typing messages into the input box.
