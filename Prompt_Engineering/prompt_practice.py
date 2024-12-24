import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key1 = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key1)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Information about prompt engineering")

print(response.text)
