import os
from openai import OpenAI

model = "gpt-4o-mini"

client = OpenAI()

conversation = [{"role": "system", "content": "You are a helpful travel guide for the culturally rich city of Paris."}]

questions = ["How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"]

for question in questions:
    conversation.append({"role": "user", "content": question})
    
    reponse = client.chat.completions.create(
    model=model, messages=conversation, temperature=0.0, max_completion_tokens=100)

    answer = reponse.choices[0].message.content
    conversation.append({"role": "assistant", "content": answer})

    print(f"User: {question}")
    print(f"Assistant: {answer}")