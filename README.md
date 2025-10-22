# Gemini AI Chatbot

I’m excited to share my latest project as a **PIAIC (Presidential Initiative for Artificial Intelligence and Computing) student** — I’ve built my very own **Gemini AI Chatbot**!  

---

## 🌟 Features

- ✨ **AI-Powered Conversations** – Powered by Gemini AI  
- 💾 **Persistent Chat History** – Stored securely in a **SQLite database**  
- ⚡ **Real-Time Interaction** – FastAPI backend with a sleek frontend  

---

## 🛠 Skills Learned & Applied

Python | FastAPI | Databases | AI Integration | Web Development  

---

## 📂 Project Setup & First Steps

Follow these steps to run the project locally:

### 1. Create project folder
```bash
mkdir gemini-chatbot
cd gemini-chatbot
2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment

Windows (PowerShell):

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

4. Create a .env file

Create a .env file in the project root to store your Gemini API key:

GEMINI_API_KEY=your_gemini_api_key_here


Note: Keep your API key secret!

5. Install dependencies

Make sure you have a requirements.txt file in the project root, then run:

pip install -r requirements.txt


This will install:

FastAPI

SQLAlchemy

Jinja2

Uvicorn

google-generativeai

python-dotenv

6. Database setup

The project uses SQLite for persistent chat storage.
No additional setup is needed; the database file (chat.db) will be created automatically in the project folder.

7. Run the application
uvicorn main:app --reload


Then open your browser at:

http://127.0.0.1:8000

💬 Usage

Type your messages in the input box

The chatbot replies in real-time

All previous chats are stored and used as context for multi-turn conversation

📂 GitHub Project

Check the full project here:
Gemini Chatbot on GitHub

🙏 Acknowledgements

Big thanks to the PIAIC community for guidance and inspiration!
Your thoughts and suggestions are welcome!

Enjoy building and chatting with your Gemini AI Chatbot!


---

If you want, I can also **create a shorter, LinkedIn-ready version** of this README that’s more like a post to share your project, keeping the GitHub link and tags.  

Do you want me to do that?
