This project is about developing AI Recruiter Platform for recruiters to manage dashboard and easily shortlist the candidates based on their resumes corresponding to the job description.

The Problem:-

- Managing many applications can be time consuming
- It often includes human bias

The Solution:-

AI based screening that ranks candidates based on their score out of 100 for a particular job description and help in real time shortlisting.

---

## Features

- AI-based shortlisting
- Deterministic scoring system combined with LLM's capability to understand language
- Detailed breakdown of a particular candidate

---


## Architecture








---

## Project Structure





---

## Setup Guide

1. Clone the repository.

2. Initialize virtual environment.

```
powershell

python -m venv venv

set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process (if windows block it)

```

3. Initialize backend using uvicorn

```powershell

uvicorn main:app

```

4. Run the Live Server or use integrated browser

---

## Limitations

- Right now, it doesn't have the strength and weakness explaination of the candidate.
- Education is not taken into the final breakdown, keeping in mind that companies prefer skills and projects.
- No Agentic system

## Future Improvements

- Add 2-layer filtering such as candidates required a particular YOE before they can be further considered.
- Agentic architecture where Agents can work dynamically
- Production environment deployed on Docker, Linux, etc.







