import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key =  my_api_key)

model = "llama-3.3-70b-versatile"

JD = """
We are hiring a backend python developer.
requirements:
strong python
fast api or django
postgresql
dcoker
aws
rest apis
2+ years of experience
"""

RESUME =  """
Name: Rahul Sharma
Experience: 3 years
Skills: python, Django, Flask, MySQL, Docker, rest APIs

Projects: 
buiilt a food delivery backend using flask and mysql

developed application using docker."""

def ask_llm(system_prompt, user_prompt):
    sys_msg = {
        "role" : "system",
        "content" : system_prompt
    }

    user_msg = {
        "role" : "user",
        "content" : user_prompt
    }

    messages = [sys_msg, user_msg]
    response = client.chat.completions.create(model = model, messages = messages)
    answer = response.choices[0].message.content
    return answer

# step1
def resume_extract(RESUME):
    # Extract skills from resume
    system_prompt = """
    You are ann professional HR assistant.
    Extract skills from the candidate's resume provided.
    Only return the skills and no other information.
    Do not create information on yourself.

    Output format: 
    Skills should be seperated by commas and no other extra or filler information should be provided.
    """

    user_prompt = f"""
    Extract skills from this resume:
    {RESUME}"""

    return ask_llm(system_prompt, user_prompt)

# step2
def jd_extract(JD):
    # Extract skills from job description
    system_prompt = """
    You are ann professional HR assistant.
    Extract skills from the job description provided.
    Only return the skills and no other information.
    Do not create information on yourself.

    Output format: 
    Skills should be seperated by commas and no other extra or filler information should be provided.

    """

    user_prompt = f"""
    Extract skills from this job description:
    {JD}"""

    return ask_llm(system_prompt, user_prompt)


# step 
def match_skills(candidate , jd):
    system_prompt = """
    Yur are  a professional HR assistant. 
    Compare the skills of the candidate and the skils required in the jd and produce a
    a final score between  1-100. Also produce a short verdict if the candidate is a good fit for the job."""

    user_prompt = f"""
    Compare and match the skills
    JD: {jd}
    Candidate: {candidate}
    """
    return ask_llm(system_prompt, user_prompt)


candidate  = resume_extract(RESUME)
sleep(2)
jd = jd_extract(JD)
sleep(2)
score = match_skills(candidate, jd)
print(score)