import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key1 = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key1)
model = genai.GenerativeModel("gemini-1.5-flash")

product_review = """
I recently purchased Boat earbuds, and I must say they have exceeded 
my expectations in every way. The sound quality is crisp and well-balanced, 
 delivering deep bass and clear treble that make listening to music a delightful experience.
 The earbuds are lightweight, comfortable, and fit snugly in the ears, making them ideal for long 
 usage without any discomfort. The build quality feels premium and durable, while the sleek design
 adds a modern touch. The battery life is impressive, providing hours of uninterrupted listening, 
 and the quick charging feature is a huge plus. The seamless Bluetooth connectivity ensures hassle-free pairing, 
 and the touch controls are intuitive and easy to use. Overall, Boat earbuds are an excellent choice for anyone
 looking for great sound quality, stylish design, and reliable performance at an affordable price. Highly
 recommended!
"""
prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words. 

Review: ```{product_review}```
"""

response = model.generate_content(prompt)
print("Result for Prompt0 : ")
print(response.text)

prompt1 = prompt = f"""
Your task is to generate a short summary of a product 
review from an ecommerce site to give feedback to the 
Shipping deparmtment. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects 
that mention shipping and delivery of the product.
If not present this aspects mention No detail found about it  

Review: ```{product_review}```
"""
response1 = model.generate_content(prompt1)
print("Result for Prompt1 : ")
print(response1.text)


review_1 = product_review 

# review for a standing lamp
review_2 = """
Needed a nice lamp for my bedroom, and this one \
had additional storage and not too high of a price \
point. Got it fast - arrived in 2 days. The string \
to the lamp broke during the transit and the company \
happily sent over a new one. Came within a few days \
as well. It was easy to put together. Then I had a \
missing part, so I contacted their support and they \
very quickly got me the missing piece! Seems to me \
to be a great company that cares about their customers \
and products. 
"""

# review for an electric toothbrush
review_3 = """
My dental hygienist recommended an electric toothbrush, 
which is why I got this. The battery life seems to be 
pretty impressive so far. After initial charging and 
leaving the charger plugged in for the first week to 
condition the battery, I've unplugged the charger and 
been using it for twice daily brushing for the last 
3 weeks all on the same charge. But the toothbrush head 
is too small. I’ve seen baby toothbrushes bigger than 
this one. I wish the head was bigger with different 
length bristles to get between teeth better because 
this one doesn’t.  Overall if you can get this one 
around the $50 mark, it's a good deal. The manufactuer's 
replacements heads are pretty expensive, but you can 
get generic ones that're more reasonably priced. This 
toothbrush makes me feel like I've been to the dentist 
every day. My teeth feel sparkly clean! 
"""

# review for a blender
review_4 = """
So, they still had the 17 piece system on seasonal 
sale for around $49 in the month of November, about \
half off, but for some reason (call it price gouging) \
around the second week of December the prices all went \
up to about anywhere from between $70-$89 for the same \
system. And the 11 piece system went up around $10 or \
so in price also from the earlier sale price of $29. \
So it looks okay, but if you look at the base, the part \
where the blade locks into place doesn’t look as good \
as in previous editions from a few years ago, but I \
plan to be very gentle with it (example, I crush 
very hard items like beans, ice, rice, etc. in the \ 
blender first then pulverize them in the serving size 
I want in the blender then switch to the whipping 
blade for a finer flour, and use the cross cutting blade 
first when making smoothies, then use the flat blade 
if I need them finer/less pulpy). Special tip when making 
smoothies, finely cut and freeze the fruits and 
vegetables (if using spinach-lightly stew soften the \ 
spinach then freeze until ready for use-and if making 
sorbet, use a small to medium sized food processor) 
that you plan to use that way you can avoid adding so 
much ice if at all-when making your smoothie. 
After about a year, the motor was making a funny noise. 
I called customer service but the warranty expired 
already, so I had to buy another one. FYI: The overall 
quality has gone done in these types of products, so 
they are kind of counting on brand recognition and 
consumer loyalty to maintain sales. Got it in about 
two days.
"""

reviews = [review_1, review_2, review_3, review_4]

print("Result for prompt 3 : ")
for i in range(len(reviews)):
    prompt3 = f"""
    Your task is to generate a short summary of a product \ 
    review from an ecommerce site. 

    Summarize the review below, delimited by triple \
    backticks in at most 20 words. 

    Review: ```{reviews[i]}```
    """

    response3 = model.generate_content(prompt3)
    # print(response3.text)
    print(i, response3.text, "\n")
