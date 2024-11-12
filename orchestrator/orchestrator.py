from agents.scheduling_agent import SchedulingAgent
from agents.email_agent import EmailHandlerAgent
from agents.data_analysis_agent import DataAnalysisAgent

# agents/__init__.py
#from .scheduling_agent import SchedulingAgent
#from .email_agent import EmailHandlerAgent
#from .data_analysis_agent import DataAnalysisAgent

import sys
import os

# Add the root directory (Cerebras) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Orchestrator:
    def __init__(self):
        # Initialize agents
        self.agents = {
            "scheduling": SchedulingAgent(),
            "email": EmailHandlerAgent(),
            "data_analysis": DataAnalysisAgent(),
        }

    def delegate_task(self, task_type, details):
        # Delegate task to the correct agent
        if task_type in self.agents:
            agent = self.agents[task_type]
            if task_type == "scheduling":
                return agent.schedule(details)
            elif task_type == "email":
                return agent.process_email(details)
            elif task_type == "data_analysis":
                return agent.analyze(details)
        return f"Task type '{task_type}' is not supported."