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

# structure it 
from pydantic import BaseModel  
class Ticket(BaseModel):
    name : str
    email : str
    contact: int
    issue : str

schema = Ticket.model_json_schema()

response_format = {
    "type" : "json_object"
}

system_prompt = f"""Extract the personal information form the ticket strictly based on the given schema and give me a json output {schema} """

message_system = {
    "role" : "system",
    "content" : system_prompt
}


text = "Hii, I'm Durgesh.  I recently bought an Iphone from your store and I'm facing issue regarding display. Please contact me asap on abc@gmail.com or 365353463. Thank you for your attention."

prompt = f"""This is the customer ticket and help me extract the personal information about the customer from this {text} """

message = {
    "role" : role,
    "content": prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format = response_format)
answer = response.choices[0].message.content
print(answer)

# how to read this structured output 
import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.issue)
print(ticket.email)