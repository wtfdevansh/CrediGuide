# Langchain Agent Flow in Credi Guide

This document outlines the flow of information and the decision-making process of the Langchain agent used in the Credi Guide project. The agent is responsible for understanding user queries and recommending suitable credit cards.

## 1. User Interaction and Input

*   **Interface:** The user interacts with the system through a chat interface powered by Streamlit (`app.py`).
*   **Input:** Users provide information such as their credit score, income, spending habits (e.g., "travel", "cashback"), and preferences for annual fees. This input is captured as a text query.
    *   Example: "What is your credit score? What do you spend most on?" followed by user's answers.

## 2. Agent Initialization

The agent and its components are initialized when the Streamlit application (`app.py`) starts:

*   **CardTools (`card_agent/recommender.py`):**
    *   An instance of the `Recommender` class (aliased as `CardTools` in `app.py`) is created.
    *   Upon initialization, the `Recommender` loads credit card data from `data/sampleData.json` (via `card_agent/data_loader.py`). This data forms the knowledge base for card comparisons.
*   **AgentCreator (`llm_agent.py`):**
    *   An `AgentCreator` instance is initialized, taking the `CardTools` instance.
    *   **LLM:** It initializes the language model (e.g., `ChatOpenAI` with a specific model like "gpt-4.1-nano").
    *   **Tools:** It defines the tools available to the agent. The primary tool is `credit_card_recommendation_tool`.
        *   This tool is a `StructuredTool` created from the `Recommender.get_credit_card_recommendations` method.
        *   It's described to the agent as a way to "Get personalized credit card recommendations based on user's credit score, income, spending habits, and annual fee."
    *   **Output Parser:** A `PydanticOutputParser` is configured with the `RecommendationResponse` schema (`schema/schema.py`) to parse the structured output from the recommendation tool.
*   **Agent Executor (`llm_agent.py`):**
    *   The `AgentCreator.create_agent_executor()` method builds and returns the `AgentExecutor`.
    *   This involves:
        *   Defining a chat prompt template (`ChatPromptTemplate`) that includes:
            *   A system message instructing the agent ("You are Fitch, a helpful and friendly AI assistant...").
            *   Placeholders for chat history (`chat_history`), user input (`input`), and agent scratchpad (`agent_scratchpad`).
        *   Binding the defined tools to the LLM.
        *   Setting up the agent logic using Langchain Expression Language (LCEL) to chain input processing, prompt formatting, LLM interaction, and output parsing (`OpenAIToolsAgentOutputParser`).
*   **Session State (`app.py`):** The initialized `agent_executor` and the `parser` are stored in Streamlit's session state for use across user interactions.

## 3. Processing Input and Tool Usage

When the user sends a message:

*   **Invocation (`app.py`):** The user's input string and the current chat history are passed to `st.session_state.agent_executor.invoke()`.
*   **LLM Decision Making (`llm_agent.py`):**
    *   The LLM, guided by its system prompt and the conversation history, processes the user's input.
    *   It determines whether it has enough information to call the `get_credit_card_recommendations` tool. If not, it might ask follow-up questions (though the current prompt emphasizes gathering necessary info to use tools).
    *   If it decides to use the tool, it extracts the required arguments (credit score, income, fee, usage) from the conversation.
*   **Tool Execution (`llm_agent.py` -> `card_agent/recommender.py`):**
    *   The `credit_card_recommendation_tool` is invoked. This directly calls the `recommender_instance.get_credit_card_recommendations()` method.
    *   **Information Gathering & Filtering (`card_agent/recommender.py`):**
        1.  `find_suitable_cards(credit_score, income, fee)`:
            *   This method filters the loaded card data (`self.card_data` originally from `sampleData.json`).
            *   It considers the user's credit score, income (evaluating against income tiers defined in `card_agent/tier_logic.py`), and maximum preferred annual fee.
            *   Only cards meeting these criteria are considered "suitable."
        2.  `sort_by_usage(suitable_cards, primary_usage)`:
            *   The list of suitable cards is then sorted based on the user's stated primary usage (e.g., "travel," "cashback"). The sorting logic is handled by `card_agent/sort.py`.
        3.  The top 3 cards from the sorted list are selected for recommendation.

## 4. Agent Response and Output Parsing

*   **Tool Output Formatting (`card_agent/recommender.py`):**
    *   The `get_credit_card_recommendations` method formats each of the selected cards into a `RecommendedCard` Pydantic model (defined in `schema/schema.py`). This includes details like card name, issuer, image URL, rewards, benefits, annual fee, and a reason for the recommendation.
    *   These `RecommendedCard` objects are then packaged into a `RecommendationResponse` Pydantic model, which also includes an overall `summary` string.
    *   This `RecommendationResponse` object is serialized into a JSON string using `.model_dump_json(indent=2)`. This JSON string is the direct output of the `credit_card_recommendation_tool`.
*   **Agent Output (`llm_agent.py`):** The `AgentExecutor` receives this JSON string as the result of the tool execution (available in `response["intermediate_steps"]`). The `response["output"]` will typically be the LLM's textual summary or confirmation of using the tool.
*   **Output Parsing and Display (`app.py`):**
    *   The Streamlit application (`app.py`) accesses the `intermediate_steps` from the agent's response.
    *   The JSON output from the tool (i.e., `intermediate_steps[0][1]`) is parsed using `st.session_state.parser.parse()`. This parser was initialized with the `RecommendationResponse` Pydantic schema.
    *   This converts the JSON string back into a structured `RecommendationResponse` Python object.
    *   The application then iterates through the `recommended_cards` list within this object and displays the details for each card (name, image, rewards, fee, reason) in a user-friendly format in the chat interface. The overall `summary` is also displayed.
    *   If no tool was called (e.g., the agent is just conversing) or if parsing the tool output fails, the direct `output_message` from the LLM is displayed.

This flow allows Credi Guide to take unstructured user input, use an LLM to understand intent and extract parameters, leverage a dedicated tool with specific business logic (card filtering and sorting) and structured data (`sampleData.json`), and then present a rich, structured recommendation back to the user.
