# Customer Support Chatbot using Mistral AI  
**DSAI4201 – Selected Topics in Data Science (5/6)**  
**LLM Lab Project**

**Student:** Lynn Younes  
**Student ID:** 60107070  
**Institution:** University of Doha for Science and Technology (UDST)  
**Course:** DSAI4201 – Selected Topics in Data Science  

---

## Project Overview

This project is part of the LLM Lab for the course DSAI4201.  
The goal is to explore Large Language Models (LLMs) using Mistral AI and apply them to real-world NLP tasks.  
Based on the lab activities, a Customer Support Chatbot was designed and deployed as both a web application and a REST API.

---

## Project Structure

customer-support-chatbot/
│
├── customer_support_chatbot_lab.ipynb
├── support_bot.py
├── api.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
└── README.md


---

## Notebook Description  
### `customer_support_chatbot_lab.ipynb`

The notebook demonstrates the core LLM tasks required in the lab:

### 1. Setup and Configuration
- Install required libraries
- Load and configure the Mistral API key
- Create a helper function to call Mistral models

### 2. Intent Classification
- Classify customer inquiries into predefined support categories
- Use prompt-based text classification

### 3. Information Extraction
- Extract structured data from unstructured text
- Enforce a predefined JSON schema

### 4. Personalized Response Generation
- Generate professional and context-aware customer support responses
- Use provided facts to ground model output

### 5. Summarization
- Summarize a news article
- Generate analytical questions and a structured report

---

## Final Task: Customer Support Chatbot

Using the notebook as a foundation, a complete customer support chatbot was implemented with the following features:

- Customer intent classification
- Context-aware response generation
- Conversation summarization
- Modular and reusable architecture

---

## Deployment Options

### 1. Web Application (Streamlit)

The chatbot is deployed as a web application where users can submit customer support questions and receive responses.

Run the web app:
```bash
streamlit run streamlit_app.py
```
---
### 2. REST API (Flask)

The chatbot is also deployed as a REST API that can be integrated into other applications.

Run the API: 
```bash
python api.py
```

Available endpoints:
- `POST /chat` returns detected intent and response
- `POST /summarize` returns a summary of a conversation

---

## Testing the API

This section describes how the Customer Support Chatbot API was tested to ensure correct functionality.

### 1. Start the API Server

From the project root directory, run:

```bash
python api.py
```
The API should start successfully and run at:
```bash
http://127.0.0.1:5000
```

### 2. Test the `/chat` Endpoint (PowerShell)

On Windows, the API was tested using Invoke-RestMethod in PowerShell.

```bash
Invoke-RestMethod -Uri "http://127.0.0.1:5000/chat" `
-Method POST `
-Headers @{ "Content-Type" = "application/json" } `
-Body '{"message":"When will my card arrive?"}'
```

Expected output:
* The intent is correctly classified (e.g., card arrival)
* A relevant customer support response is returned

Additional test example:
```bash
Invoke-RestMethod -Uri "http://127.0.0.1:5000/chat" `
-Method POST `
-Headers @{ "Content-Type" = "application/json" } `
-Body '{"message":"I want to change my PIN"}'
```
### 3. Test the `/summarize` Endpoint

The summarization endpoint was tested using the following command:
```bash
Invoke-RestMethod -Uri "http://127.0.0.1:5000/summarize" `
-Method POST `
-Headers @{ "Content-Type" = "application/json" } `
-Body '{"conversation":"User asked about card arrival. Agent explained delivery time."}'
```
Expected output:
* A concise summary of the provided conversation

### 4. Test Validation

The API was verified to:
- Run without errors
- Correctly classify customer intents
- Return clear and relevant responses
- Handle different user inputs without crashing

---
## Technologies Used
* Python
* Mistral AI
* Flask
* Streamlit
* python-dotenv

---
## Learning Outcomes
- Understand how to interact with Large Language Model APIs
- Apply LLMs to classification, extraction, personalization, and summarization tasks
- Design and deploy AI systems as web applications and APIs
- Build modular and maintainable AI projects

---
## Course Context
This project fulfills the LLM Lab requirement for
DSAI4201 Selected Topics in Data Science at UDST