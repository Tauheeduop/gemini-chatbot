# agent.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- Load API Key from .env file ---
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- Create the model ---
model = genai.GenerativeModel("gemini-2.5-flash")

print("  Salam! Main Gemini 2.5 Flash agent hoon. 'bye' likh kar exit karein.\n")

# --- Chat Loop ---
while True:
    user_input = input("Aap: ")

    if user_input.lower().strip() == "bye":
        print("Agent: Allah Hafiz!")
        break

    # Send prompt to Gemini
    try:
        response = model.generate_content(user_input)
        print(f"Agent: {response.text}\n")
    except Exception as e:
        print(f" Error: {e}\n")
