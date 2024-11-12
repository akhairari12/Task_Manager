from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv

import os
import numpy as np
import openai
import traceback
#print("OpenAI package works!")



load_dotenv(dotenv_path=".env")

class Completions:
    def __init__(self, api_key):
        self.api_key = api_key

    def create(self, model, messages):
        # Simulate a response based on the provided model and messages
        system_message = next((msg['content'] for msg in messages if msg['role'] == 'system'), "Default system message.")
        user_message = next((msg['content'] for msg in messages if msg['role'] == 'user'), "Default user message.")
        
        # Example response logic
        return {
            "model": model,
            "system": system_message,
            "user": user_message,
            "response": "Fast scheduling ensures timely task completion."
        }

# orchestrator.py
from agents.scheduling_agent import SchedulingAgent
from agents.email_agent import EmailHandlerAgent
from agents.data_analysis_agent import DataAnalysisAgent


from langchain.llms import openai
from langchain.prompts import PromptTemplate
from flask import Flask, request, jsonify
from orchestrator.orchestrator import Orchestrator

from langchain_interaction.langchain_interaction import LangChainInteraction

#class LangChainInteraction:
    #def __init__(self, api_key):
    #    self.llm = OpenAI(api_key=api_key)

  #  def classify_task(self, user_input):
        # Define the prompt template for task classification
   #     prompt_template = PromptTemplate(
   #         template="Classify the following task: {task}",
    #        input_variables=["task"]
    #    )
    #    response = self.llm(prompt_template.render(task=user_input))
    #    return response.strip().lower()

app = Flask("Edith")

orchestrator=Orchestrator()
langchain_interaction = LangChainInteraction(api_key = os.environ.get("API_KEY"))

@app.route("/task", methods=["POST"])
def handle_task():
    user_input = request.json.get("input")
    task_type = langchain_interaction.classify_task(user_input)
    response = orchestrator.delegate_task(task_type, user_input)
    ai_response = langchain_interaction.generate_response(task_type, user_input)

    return jsonify({"task_type": task_type,
        "agent_response": response,
        "ai_response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)



class ChatClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.completions = Completions(api_key)  # Use `completions` as an attribute

    def generate_response(self, prompt):
        # Example method for generating chat completions
        return f"Generated response for: {prompt}"


class Cerebras:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key is required for initialization.")
        self.api_key = api_key
        self.chat = ChatClient(api_key)  # Initialize ChatClient
        print("Cerebras client initialized successfully!")


#Test API Key and print it
api_key = os.environ.get("API_KEY")
try:
    client=Cerebras(api_key)
except ValueError as e:
    print(f"Client initilzation error: {e}")
#print(f"API Key: {api_key}")

# Initialize OpenAI client

#print("Client initialized successfully!")
#if client:
 ##      openai.api_key- api_key
        #client = openai.OpenAI(
   #     client = Cerebras(
    #        api_key=os.environ.get("API_KEY")
     #   )
           # api_key=os.environ.get("API_KEY")
   # )
      #  print("Client initialized successfully!")
    #except Exception as e:
     #   print("Error during client initilization:")
      #  traceback.print_exc()


chat_completion = client.chat.completions.create(
    model="llama3.1-8b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the importance of fast scheduling."}
            ],
      )
print("chat completion response:")
print(chat_completion)
