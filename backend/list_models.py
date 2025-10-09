# backend/list_models.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

print("--- Listing available Gemini models ---")

try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file!")

    genai.configure(api_key=api_key)

    print("\nModels that support 'generateContent':")
    for model in genai.list_models():
        # The error message mentioned 'generateContent', so let's check for that
        if 'generateContent' in model.supported_generation_methods:
            print(model.name)
    
    print("\n--- Listing complete ---")

except Exception as e:
    print("\n--- ERROR ---")
    print(f"Could not list models. Error:\n{e}")