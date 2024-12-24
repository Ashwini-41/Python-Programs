import google.generativeai as genai

genai.configure(api_key="AIzaSyBPRPs_5-V2tQJ0yfswnbUeboJbc5NF2_w")
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = (
    """
    Give an sentiment from the sententence
    I am not happy with this product at all
    give in one word answer
    """
)
response = model.generate_content(prompt)
print(response.text)