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

prompt = "Do you know Virat Kolhi?"

message = {
    "role" : role,
    "content": prompt
}

messages = [message]

response = client.chat.completions.create(model=model, messages=messages)
print(response)

print("######################################################")

answer = response.choices[0].message.content
print(answer)