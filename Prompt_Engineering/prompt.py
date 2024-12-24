import google.generativeai as genai
data = """
Java is a high-level, class-based, object-oriented programming language that is designed to have as few 
implementation dependencies as possible. It is a general-purpose programming language intended to let programmers 
write once, run anywhere (WORA),[16] meaning that compiled Java code can run on all platforms that support Java
without the need to recompile.[17] Java applications are typically compiled to bytecode that can run on any Java 
virtual machine (JVM) regardless of the underlying computer architecture. The syntax of Java is similar to C and
C++, but has fewer low-level facilities than either of them. The Java runtime provides dynamic capabilities
(such as reflection and runtime code modification) that are typically not available in traditional compiled 
languages.Java gained popularity shortly after its release, and has been a popular programming language since
then.[18] Java was the third most popular programming language in 2022 according to GitHub.[19] Although still 
widely popular, there has been a gradual decline in use of Java in recent years with other languages using JVM
gaining popularity.Java was originally developed by James Gosling at Sun Microsystems. It was released in May 
1995 as a core component of Sun's Java platform. 

"""
prompt = (
            f"perform the following actions: "
            f"1- extract language used from the data given within the delimiter curly brace, "
            f"2- translate the paragraph from English to Hindi and store the translated data inside a key. "
            f"Data: {{{data}}}. Write the output in JSON format."
        )

data1 = """
   To make a delicious cake, start by gathering all the necessary ingredients: flour, 
   sugar, eggs, butter, baking powder, milk, and vanilla extract. Begin by preheating your oven to the 
   recommended temperature, usually around 350°F (175°C), and greasing your cake pan to prevent sticking. 
   In a large mixing bowl, cream together the butter and sugar until light and fluffy. Add the eggs one at a time,
   mixing well after each addition, and then stir in the vanilla extract for flavor. In a separate bowl, whisk 
   together the dry ingredients: flour and baking powder. Gradually add the dry mixture to the creamed butter, alternating with milk, 
   until the batter is smooth and lump-free. Pour the batter into the prepared cake pan, spreading it evenly.
   Place the pan in the oven and bake for 25-30 minutes, or until a toothpick inserted into the center comes out 
   clean. Once baked, let the cake cool in the pan for a few minutes before transferring it to a wire rack to cool 
   completely. You can then decorate the cake with frosting, whipped cream, or fresh fruits to your liking. Enjoy 
   your homemade cake as a sweet treat for any occasion!
"""
# prompt1 = (
#     f"Give answer in step wise manner: "
#     f"1 - "
#     f"2 - "
#     f"Data: {{{data1}}}"
# )

prompt1 = (
    f"""
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions, \ 
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions, \ 
    then simply write \"No steps provided.\"
    \"\"\"{data1}\"\"\"
        """
)

genai.configure(api_key="AIzaSyBPRPs_5-V2tQJ0yfswnbUeboJbc5NF2_w")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
response1 = model.generate_content(prompt1)
print(response.text)
print(response1.text)

