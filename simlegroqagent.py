from phi.agent import Agent
from phi.model.groq import GroqModel
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=GroqModel(id="llama-3.3-70b-versatile")
)

agent.print_response("Hello, world!")
                    
