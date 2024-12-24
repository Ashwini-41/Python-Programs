import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key1 = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key1)
model = genai.GenerativeModel("gemini-1.5-flash")


study_table_review = """ I was looking for a sturdy and stylish study table, and this one checked all the boxes 
without breaking the bank. It arrived quickly, and the packaging ensured it stayed in perfect condition during transit.
Assembly was straightforward, with clear instructions that made the process easy to follow. The table is spacious
enough to hold my laptop, books, and other essentials, with additional compartments that help keep everything
organized. One of the screws was missing, but their customer support was excellent—they responded promptly 
and shipped the missing part within a couple of days. The wood finish looks premium and blends beautifully 
with my room decor. Overall, this study table is a fantastic purchase, and the company’s dedication 
to customer satisfaction really stands out!"""

prompt = (
    f"""
    What is the sentiment of the following product review
    which is in the delimiter with triple backtricks?
    
    Review text : '''{study_table_review}'''
"""
)

response1 = model.generate_content(prompt)
print("Response of prompt 1: ")
print(response1.text)

prompt2 = (
    f"""
    What is the sentiment of the following product review
    which is in the delimiter with triple backtricks?
    Give answer as single word positive or negative
    
    Review text : '''{study_table_review}'''
"""
)

response2 = model.generate_content(prompt2)
print("Response of prompt 2: ")
print(response2.text)

prompt3 = (
    f"""
    Identify the list of emotions that the writer of the following expressing include all the items 
    in list of lower case words and separeted by commas
    
    Review text: '''{study_table_review}'''
    """
)
response3 = model.generate_content(prompt3)
print("Response of prompt 3: ")
print(response3.text)

prompt4 = f"""
Is the writer of the following review expressing anger?\
The review is delimited with triple backticks. \
Give your answer as either yes or no.

Review text: '''{study_table_review}'''
"""

response4 = model.generate_content(prompt4)
print("Response of prompt 4: ")
print(response4.text)

prompt5 = f"""
Identify the following items from the review text: 
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Item" and "Brand" as the keys. 
If the information isn't present, use "unknown" \
as the value.
Make your response as short as possible.
  
Review text: '''{study_table_review}'''
"""
response5 = model.generate_content(prompt5)
print("Response of prompt 5: ")
print(response5.text)

prompt6 = f"""
Identify the following items from the review text: 
- sentiment of the review (positive or negative)
- Is the reviewer expressing anger (True or false)
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Item" and "Brand" as the keys. 
If the information isn't present, use "unknown" \
as the value.
Make your response as short as possible.
  
Review text: '''{study_table_review}'''
"""
response6 = model.generate_content(prompt6)
print("Response of prompt 6: ")
print(response6.text)

