import os
from pathlib import Path
from dotenv  import load_dotenv
from groq import Groq

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key = my_api_key)

model = "llama-3.3-70b-versatile"

def llm_ans(prompt):
    message = {
        "role" : "user",
        "content" : prompt
    }

    messages = [message]

    response = client.chat.completions.create(model = model,  messages = messages)
    answer = response.choices[0].message.content
    return answer

bad_prompt = """ 
#ROLE:
You are support assistant at a mobile/laptop company.
#TASK:
You have to classify the issue in a category.
#COSTRAINTS:
You have to classify the issue in one of the following categories:
1. Billing
2. Technical
3. Return/Exchange
# OUTPUT:
Your answer should be in one word only. The one word should be one of the categories given in the constraints.
#EXAMPLE:
For instance if a user complain says they want a refund then the category is Return.
#FALLBACK:
If the issue is not related to any of the given catergories mentioned in constraints then the answer should be "Other".
#USER COMPLAINT:
This is a user complaint.
My poem didn't win the contest.
"""

print(llm_ans(bad_prompt))