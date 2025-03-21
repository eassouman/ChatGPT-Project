from dotenv import load_dotenv
import os

load_dotenv()

# Add this debug line
print("API Key:", os.getenv('OPENAI_API_KEY'))

from openai import OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": "write a blog article about the importance of wellness and healthy lifestyle"
    }]
)

print(completion.choices[0].message.content)

import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")

    import openai
import gradio

openai.api_key = "####"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)
