import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key1 = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key1)
model = genai.GenerativeModel("gemini-1.5-flash")

# sentiment and review for a restaurant
sentiment = "positive"

review = """
I recently dined at Bella Bistro, and it was an exceptional experience from start to finish. The ambiance was warm
and inviting, with elegant decor and soft lighting that set the perfect mood for a relaxing meal. 
The staff was attentive and friendly, ensuring we were comfortable and well taken care of throughout the evening.
The menu offered a wide range of options, and every dish we ordered was beautifully presented and bursting with flavor. 
The highlight for me was the creamy truffle pasta, which was perfectly cooked and absolutely delicious. The dessert,
a rich chocolate lava cake, was the perfect way to end the meal. While the restaurant was a bit busy, the service
remained efficient, and the staff made sure we never felt rushed. I highly recommend Bella Bistro for anyone looking
for a delightful dining experience!
"""
prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```, \
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for \
their review.
If the sentiment is negative, apologize and suggest that \
they can reach out to customer service. 
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""

response = model.generate_content(prompt)
print(response.text)