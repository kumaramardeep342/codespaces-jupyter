# 🔍 Gemini Text Summarization App

# Overview
This Streamlit application leverages Google's Gemini AI to provide intelligent text summarization. Users can input long-form text and receive concise, coherent summaries using advanced natural language processing techniques.

# 🌟 Features
- **Easy-to-Use Interface:** Simple Streamlit web app
Powered by Gemini AI: Utilizes Google's state-of-the-art language model
Flexible Summarization: Works with various types of text
Secure API Key Management: Allows users to input their own Google AI API key

🛠 Prerequisites

Python 3.8+
Google AI Studio API Key

🚀 Installation

Clone the repository:

bashCopygit clone https://github.com/yourusername/gemini-text-summarizer.git
cd gemini-text-summarizer

Create a virtual environment:

bashCopypython3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:

bashCopypip install -r requirements.txt
🔑 Getting Your API Key

Visit Google AI Studio
Click "Create API Key"
Copy the generated key

🖥 Running the App
bashCopystreamlit run summarization_app.py
📝 How to Use

Navigate to the Streamlit app in your browser
Enter the text you want to summarize in the text area
Input your Google AI API key
Click "Submit"
View the generated summary

🔒 Security Note

Never share your API key publicly
The app is designed to keep your API key secure
Each session uses a unique, temporary API key

📦 Dependencies

Streamlit
Google Generative AI
LangChain
Tiktoken

🤝 Contributing

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.
🙌 Acknowledgments

Streamlit
Google Generative AI
LangChain


Disclaimer: This project is not officially associated with Google or Gemini. It's a community-driven project demonstrating the capabilities of Gemini AI.

#pip install -r requirements.txt
#streamlit run summary_app.py