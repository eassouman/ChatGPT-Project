import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a holistic doctor"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Holistic Doctor Bot")

demo.launch(share=True)
