import gradio
from groq import Groq

client = Groq(
    api_key="",
)

def initialize_messages():
    return [{"role": "system",
             "content": """You are a knowledgeable flight assistant with 
             expertise in providing accurate information on flight schedules, timings, and available airline options. 
             Your role is to assist travelers by offering clear, up-to-date details about flights and 
             guiding them in a professional and helpful manner."""}]

messages_prmt = initialize_messages()

print(type(messages_prmt))

def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply

iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to your flight"),
                     title="Flight assist ChatBot",
                     description="Chat bot for flight assistance",
                     theme="soft",
                     examples=["hi","Available flights now", "What is the cabin baggage limit for Indigo?"]
                     )

iface.launch(share=True)