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

#3 prompts
prompt1 = "Hii"
prompt2 = "Explain time travel in detail."
prompt3 = "write a 500 words eassy on machine learning"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role" : role,
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, max_tokens = 50)
    usage = response.usage
    print(f"Prompt: {prompt} --> prompt_tokens: {usage.prompt_tokens}  completion_tokens: {usage.completion_tokens} total_tokens = {usage.total_tokens} Finish reason: {response.choices[0].finish_reason}")

# # SYSTEM
# message_system = {
#     "role": "system",
#     "content": "You are a brand manager who suggests name for my brand, Name should be in one word. Suggest one name only"
# }

# #temperature by deault is 0 which means safe. Temperature range is usually [0, 2]