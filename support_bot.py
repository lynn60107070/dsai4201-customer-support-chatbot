import os
from mistralai import Mistral, UserMessage
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

def call_mistral(prompt, model="mistral-large-latest"):
    messages = [UserMessage(content=prompt)]
    response = client.chat.complete(model=model, messages=messages)
    return response.choices[0].message.content


# 1️⃣ Intent Classification
def classify_intent(user_query):
    prompt = f"""
You are a customer support classification bot.

Classify the inquiry into ONE of the following:
card arrival
change pin
exchange rate
country support
cancel transfer
charge dispute
customer service

Only respond with the category.

Inquiry:
{user_query}
"""
    return call_mistral(prompt).strip()


# 2️⃣ Personalized Response
def generate_response(category, user_query):
    prompt = f"""
You are a professional customer support agent.

Customer category: {category}
Customer question: {user_query}

Provide a clear, friendly, and helpful response.
"""
    return call_mistral(prompt)


# 3️⃣ Summarization
def summarize_conversation(conversation):
    prompt = f"""
Summarize the following customer support conversation
in 3 bullet points:

{conversation}
"""
    return call_mistral(prompt)