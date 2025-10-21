import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import google.generativeai as genai
from database import SessionLocal, Chat

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# FastAPI setup
app = FastAPI()

# Static & Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})






'''
@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: str = Form(...)):
    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = f"Error: {e}"

    # --- Save to SQLite ---
    db = SessionLocal()
    try:
        chat_entry = Chat(user_input=user_input, bot_reply=reply)
        db.add(chat_entry)
        db.commit()
    finally:
        db.close()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "response": reply, "user_input": user_input}
    )
'''
@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: str = Form(...)):
    db = SessionLocal()
    reply = ""

    try:
        # --- Step 1: Fetch all previous chat history ---
        # Fetching all previous entries to build context
        history_entries = db.query(Chat).order_by(Chat.created_at).all()

        # --- Step 2: Format the history for the Gemini API ---
        # The history must be a list of dictionaries with 'role' and 'parts'
        # The 'user' role is for the user_input, 'model' for the bot_reply
        chat_history = []
        for entry in history_entries:
            # Add user's turn
            chat_history.append({"role": "user", "parts": [{"text": entry.user_input}]})
            # Add model's turn
            chat_history.append({"role": "model", "parts": [{"text": entry.bot_reply}]})

        # --- Step 3: Append the *current* user input to the history list ---
        # The final prompt is the *last* item in the list
        chat_history.append({"role": "user", "parts": [{"text": user_input}]})

        # --- Step 4: Call the model with the complete history ---
        # For multi-turn conversations, use generate_content with the history list
        response = model.generate_content(chat_history)
        reply = response.text

    except Exception as e:
        reply = f"Error: {e}"
        # If an error occurred, we still want to save the user input with the error message
        # but only if a database session is open.
        
    finally:
        # --- Save to SQLite (user input and bot reply/error) ---
        try:
            chat_entry = Chat(user_input=user_input, bot_reply=reply)
            db.add(chat_entry)
            db.commit()
        except Exception as db_e:
             # Handle any potential database save error
             print(f"Database Save Error: {db_e}")
        finally:
            db.close()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "response": reply, "user_input": user_input}
    )