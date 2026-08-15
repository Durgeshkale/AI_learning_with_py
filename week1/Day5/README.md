# LLM Resume Evaluator

An LLM-powered resume evaluation system that analyzes job descriptions, extracts structured information from resumes, and evaluates candidates based on their relevance to a given job description.

## Overview

The project uses an LLM to convert unstructured job descriptions and resumes into structured JSON data using Pydantic schemas. The structured information is then compared to generate a candidate match score and evaluation details.

The current implementation supports PDF and DOCX resumes and can process multiple candidates in a single run.

## Features

- Extracts structured information from job descriptions
- Parses resumes into structured JSON
- Supports PDF and DOCX resume files
- Extracts candidate information including:
  - Name
  - Email
  - Phone
  - Total experience
  - Skills
  - Work experience
  - Education
  - Projects
  - Certifications
- Compares resumes against job requirements
- Generates a match score from 0 to 100
- Identifies matching skills
- Identifies missing important skills
- Checks whether the experience requirement is met
- Generates a concise candidate verdict
- Processes multiple resumes in batch
- Ranks candidates based on their match scores

## Tech Stack

- Python
- Groq API
- Llama 3.3 70B
- Pydantic
- PyPDF
- python-docx
- python-dotenv
- uv

## Project Structure

```text
resume-evaluator/
│
├── .env
├── .gitignore
├── pyproject.toml
├── job_description.txt
├── resumes/
│   ├── resume1.pdf
│   ├── resume2.pdf
│   └── resume3.docx
│
└── resume_parser.py

## System Workflow

```text
Job Description
       |
       v
LLM Job Description Parser
       |
       v
Structured Job Description
       |
       |
Resume (PDF/DOCX)
       |
       v
Document Text Extraction
       |
       v
LLM Resume Parser
       |
       v
Structured Resume
       |
       v
LLM Matching Engine
       |
       v
Match Score + Evaluation
       |
       v
Candidate Ranking