from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

class LangChainInteraction:
    def __init__(self, api_key):
        self.llm = ChatOpenAI(api_key=api_key, temperature=0)  # Use correct LLM class

    def classify_task(self, user_input):
        prompt_template = PromptTemplate(
            template="Classify the following task: {task}",
            input_variables=["task"]
        )
        response = self.llm.predict(prompt_template.render(task=user_input))
        return response.strip().lower()
    
    def generate_response(self, task_type, user_input):
        # AI-generated response
        prompt_template = PromptTemplate(
            template="For a task of type '{task_type}', respond to this input: {input}",
            input_variables=["task_type", "input"]
        )
        return self.llm.predict(prompt_template.render(task_type=task_type, input=user_input)).strip()
    


