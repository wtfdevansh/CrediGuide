from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad.openai_tools import format_to_openai_tool_messages
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from dotenv import load_dotenv
from langchain.tools import StructuredTool



from card_agent.recommender import Recommender
from schema.schema import RecommendationResponse
from schema.schema import RecommendedCard
from langchain.output_parsers import PydanticOutputParser
recommender_instance = Recommender()


def credit_card_recommendation_tool(credit_score:int , income:int , fee:int , usage: str) -> str:
    return recommender_instance.get_credit_card_recommendations(credit_score = credit_score, income = income , fee = fee , usage = usage)


class AgentCreator:
    def __init__(self, card_tools: Recommender):
        """
        Initializes the AgentCreator.

        Args:
            card_tools: An instantiated CardTools object containing the agent's tools.
        """
        load_dotenv()
        self.tools = [
            StructuredTool.from_function(
                credit_card_recommendation_tool,
                name="get_credit_card_recommendations",
                description="Get personalized credit card recommendations based on user's credit score, income, spending habits, and annual fee ."
            )
        ] 
        self.llm = ChatOpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0)
        self.parser = PydanticOutputParser(pydantic_object=RecommendationResponse)

    def create_agent_executor(self) -> AgentExecutor:
        """Creates and returns the LangChain agent executor."""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are Fitch, a helpful and friendly AI assistant specializing in credit card recommendations. Your goal is to gather the necessary information from the user (credit score, income, spending habits , annual fee) to use your tools effectively. Be conversational and clear."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

       
        llm_with_tools = self.llm.bind_tools(self.tools)

        
        agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_to_openai_tool_messages(x["intermediate_steps"]),
                "chat_history": lambda x: x["chat_history"],
            }
            | prompt
            | llm_with_tools
            | OpenAIToolsAgentOutputParser()
        )

       
        agent_executor = AgentExecutor(agent=agent, tools=self.tools, verbose=True , return_intermediate_steps=True)
        
        return agent_executor