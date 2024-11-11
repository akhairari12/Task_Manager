from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv

import os
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

# agents/scheduling_agent.py
class SchedulingAgent:
    def schedule(self, details):
        # Simulate scheduling logic
        return f"Scheduled task: {details}"
    
    # agents/email_agent.py
class EmailAgent:
    def process_email(self, email):
        # Simulate email processing logic
        return f"Processed email: {email}"
    
# agents/data_analysis_agent.py
class DataAnalysisAgent:
    def analyze(self, data):
        # Simulate data analysis logic
        return f"Analyzed data: {data}"



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
