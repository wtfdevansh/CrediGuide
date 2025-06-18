# Prompt Design in Credi Guide

Effective prompt design is crucial for guiding the Langchain Large Language Model (LLM) agent in the Credi Guide project. The prompts steer the agent to understand user needs, ask relevant questions, utilize available tools correctly, and ultimately provide accurate credit card recommendations.

## 1. Core Agent Prompt Structure

The primary prompt configuration for the agent is defined in `llm_agent.py` using `ChatPromptTemplate.from_messages`. This structure includes several components:

*   **System Message:** This is the foundational instruction that defines the agent's persona, objectives, and operational guidelines.
    ```
    ("system", "You are Fitch, a helpful and friendly AI assistant specializing in credit card recommendations. Your goal is to gather the necessary information from the user (credit score, income, spending habits , annual fee) to use your tools effectively. Be conversational and clear.")
    ```
    *   **Persona ("Fitch"):** Gives the agent a name, making interactions potentially more engaging.
    *   **Role ("helpful and friendly AI assistant"):** Sets the expected tone and behavior.
    *   **Specialization ("specializing in credit card recommendations"):** Defines the agent's domain of expertise.
    *   **Primary Goal ("gather the necessary information...to use your tools effectively"):** This is a key directive. It tells the agent that its main task is to collect specific data points before it can act.
    *   **Key Information to Gather:** The prompt explicitly lists `credit score`, `income`, `spending habits`, and `annual fee`. This tells the agent what data it needs from the user.
    *   **Desired Tone ("Be conversational and clear"):** Guides the agent's communication style.

*   **MessagesPlaceholder for `chat_history`:**
    ```
    MessagesPlaceholder(variable_name="chat_history")
    ```
    This component allows the agent to have memory of the ongoing conversation, providing context for follow-up questions and more natural interactions.

*   **User Input:**
    ```
    ("user", "{input}")
    ```
    This placeholder is where the current user's query or message is dynamically inserted into the prompt.

*   **MessagesPlaceholder for `agent_scratchpad`:**
    ```
    MessagesPlaceholder(variable_name="agent_scratchpad")
    ```
    This is used internally by the Langchain agent to store intermediate steps, such as the thoughts and decisions of the agent or the outputs from tool usage. This is important for the agent's reasoning process.

## 2. Guiding Tool Usage

The system prompt works in conjunction with tool descriptions to guide the agent:

*   **Tool Description:** The primary tool, `credit_card_recommendation_tool`, has a description:
    ```
    "Get personalized credit card recommendations based on user's credit score, income, spending habits, and annual fee ."
    ```
    This description is critical. The LLM uses this to understand what the tool does and what inputs it requires. The parameters listed in the tool description directly correspond to the information the system prompt instructs the agent to gather.

*   **Implicit Parameter Extraction:** The system prompt's explicit mention of `credit score, income, spending habits, annual fee` primes the agent to look for these details in the user's conversation. If these are not provided upfront, the agent's goal is to elicit them conversationally.

## 3. User Interaction Examples & Agent Understanding

The agent's interaction flow is guided by the prompt:

*   **Initial Greeting (from `app.py`):** The assistant starts with "Hi! How can I help you find the best credit card today?" This aligns with the "helpful and friendly" persona defined in the system prompt.

*   **Example User Scenarios:**
    1.  **Complete Information:**
        *   User: "My credit score is 720, I make $60k a year, mainly spend on groceries, and I'd prefer no annual fee or something under $50."
        *   Agent's Expected Behavior: Recognize all necessary parameters (`credit score`, `income`, `spending habits`, `annual fee`) are present. It should then directly use the `get_credit_card_recommendations` tool.

    2.  **Partial Information:**
        *   User: "I need a good card for travel rewards."
        *   Agent's Expected Behavior: The system prompt ("Your goal is to gather the necessary information...") will drive the agent to ask follow-up questions. For example: "Okay, I can help with that! To find the best travel card for you, could you please tell me your approximate credit score and annual income? Also, do you have a preference for the annual fee?"

    3.  **General Query:**
        *   User: "What's the best credit card?"
        *   Agent's Expected Behavior: Similar to partial information, the agent should understand this is too broad and use its conversational ability to narrow down the requirements based on the parameters listed in its system prompt.

## 4. Eliciting Desired Output Format (`RecommendationResponse`)

The system prompt does *not* directly instruct the LLM to format its response according to the `RecommendationResponse` Pydantic schema. Instead, this is handled through the agent's tool architecture:

*   **Tool's Responsibility:** The `credit_card_recommendation_tool` (which calls `Recommender.get_credit_card_recommendations` in `card_agent/recommender.py`) is responsible for fetching the data and then explicitly formatting it into the `RecommendationResponse` schema, serializing it to a JSON string.
*   **Parsing in Application:** The `app.py` then uses a `PydanticOutputParser` (configured with `RecommendationResponse`) to parse this JSON string received from the tool's output (via `intermediate_steps`).

The prompt's role here is to ensure the agent calls the *correct tool*. The tool itself guarantees the output format. The clarity of the tool's description and the parameters mentioned in the system prompt are key to ensuring the tool is called appropriately.

## 5. Considerations for Prompt Effectiveness

*   **Clarity:** The system prompt is clear in defining the agent's role, its objective (information gathering), and the specific pieces of information it needs.
*   **Conciseness:** It provides essential instructions without being overly verbose.
*   **Effectiveness:**
    *   The prompt effectively directs the agent to be an information gatherer, which is crucial before calling the recommendation tool.
    *   The instruction to be "conversational and clear" promotes a user-friendly experience during this information-gathering phase.
*   **Tool-Centric Design:** The current prompt design is heavily reliant on the agent identifying the need to use a specific tool. The LLM's main creative task is to conduct the conversation to get the tool's required inputs.

This design ensures that the agent is focused, gathers the necessary data methodically, and then leverages specialized tools to provide structured, accurate recommendations.
