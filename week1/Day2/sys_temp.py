import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

#register as client
client = Groq(api_key = my_api_key)

model = "llama-3.3-70b-versatile"

#create message
role = "user"

prompt = "Suggest a name for my media production company"

# SYSTEM
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests name for my brand, Name should be in one word. Suggest one name only"
}

#message have role and contnet
message = {
    "role" : role,
    "content": prompt
}

messages = [message_system, message]

#temperature by deault is 0 which means safe. Temperature range is usually [0, 2]

response = client.chat.completions.create(model=model, messages=messages, temperature = 1.7)
print(response)

print("######################################################")

answer = response.choices[0].message.content
print(answer)