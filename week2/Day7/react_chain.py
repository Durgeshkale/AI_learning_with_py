import os
from pathlib import Path
from time import sleep
from dotenv import load_dotenv
from groq import Groq
import re


load_dotenv(Path(__file__).resolve().parents[2] / ".env")

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key = my_api_key)

model = "llama-3.3-70b-versatile"

#toold

def get_product_price(product):
    if(product == "laptop"):
        return 1000
    elif(product == "phone"):
        return 500
    else:
        return None

def calculator(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "calculation error!"

tools = {

    "get_product_price": get_product_price,
    "calculator": calculator
}

system_prompt = """
You are a shopping assistant.

You have these tools:
get_product_price(product)
calculator(expression)

IMPORTANT:
Call tools exactly like this examples:

Action:get_product_price("laptop")
Action:calculator("5000 - 2000")

Never write: 
get_prodcut_price(product = "laptop")

Never write:
calculator(expression = "5000 - 2000")

Follow these rules:
1. Decide what you need to do next.
2. Call only one tool at a time.
3. After writing an action stop immediatelty.
4. Never guess or invent a tool result.
5. Wait until you receive an observation.
6. Decide your next action.
7. When the task is complete, give the final answer.

Format:
Thought: what you need to do
Action: tool_name(argument)

When finished:

Final Answer: your answer
"""
def run_agent(question) :
    messages = [
        {
            "role" : "system",
            "content" :  system_prompt
        },
        {
            "role" : "user",
            "content" : question
        }
    ]

    for step in range(5):
        print("\n------------------------------------------------------")
        print(f"Step {step + 1}:")
        print("------------------------------------------------------")

        response = client.chat.completions.create(model = model, messages = messages)

        answer = response.choices[0].message.content

        print(answer)

        # agents has finished
        if "Final Answer" in answer:
            break

        # find the action
        match = re.search(
            r"Action: \s*(\w+)\((.*)\)",
              answer
        )

        if match:

            tool_name = match.group(1)

            tool_input = match.group(2).strip().strip('"')

            if tool_name in tools:

                tool = tools[tool_name]

                observation =  tool(tool_input)

            else:
                observation = "Tool not found!"

            print("Observation:" , observation)

            # add LLM response to memory
            messages.append(
                {
                    "role" : "assistant",
                    "content" : answer
                }
            )

            # give tool result back to LLM
            messages.append(
                {
                    "role": "user",
                    "content" : f"Observation: {observation}"
                }
            )
            sleep(5)

prompt = """ 
I have 5000 rupees. I want to buy a laptop and a phone. How much money will I have left after buying both?"""

run_agent(prompt)