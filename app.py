from dotenv import load_dotenv
from agents.agent import Agent
from agents.agent import AvailableModel

load_dotenv()

if __name__ == "__main__":
    agent = Agent(AvailableModel.LLAMA3_70b.value)
    print(agent.Run("hii"))