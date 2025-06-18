import streamlit as st
import time
from llm_agent import AgentCreator
from card_agent.recommender import Recommender as CardTools

from schema.schema import RecommendationResponse
from langchain.output_parsers import PydanticOutputParser


st.set_page_config(page_title="Credi Guide", page_icon="💳")




if "agent_executor" not in st.session_state:
    try:
     
        card_tools_instance = CardTools()
        
      
        agent_creator_instance = AgentCreator(card_tools_instance)

        parser = PydanticOutputParser(pydantic_object=RecommendationResponse)
        
    
        st.session_state.agent_executor = agent_creator_instance.create_agent_executor()
        st.session_state.parser = parser
        
    except ValueError as e:
       
        st.error(f"Failed to initialize the application: {e}")
        st.stop()


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: radial-gradient(circle, #D3D3D3 1px, rgba(0, 0, 0, 0) 1px);
             background-size: 30px 30px;
             animation: move-dots 1s linear infinite;
         }}

         @keyframes move-dots {{
             0% {{
                 background-position: 0 0;
             }}
             100% {{
                 background-position: 30px 30px;
             }}
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()



st.title("Credi Guide 💳")


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! How can I help you find the best credit card today?"}]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is your credit score? What do you spend most on?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Fitch is thinking..."):
       
            if "agent_executor" in st.session_state:
                response = st.session_state.agent_executor.invoke({
                    "input": prompt,
                    "chat_history": st.session_state.messages
                })
                output_message = response["output"]
                intermediate_steps = response.get("intermediate_steps", [])
                
            else:
                output_message = "Sorry, the agent is not available due to an initialization error."

            # st.write(output_message)

        
            if intermediate_steps:
             
             tool_output = intermediate_steps[0][1]

             try:
              parsed_output = st.session_state.parser.parse(tool_output)

              st.write("### Structured Recommendation:")
              st.subheader(parsed_output.summary)

              for card in parsed_output.recommended_cards:
               st.write(f"**Card:** {card.card_name} ({card.issuer})")
               st.image(card.card_image, width=100)
               st.write(f"**Rewards Summary:** {card.card_reward}")
               st.write(f"**Annual Fee:** ${card.annual_fee}")
               st.write(f"**Reason:** {card.reason}")
               st.divider()

             except Exception as e:
              st.error(f"Failed to parse the agent's output: {e}")
            else:
               st.write(output_message)


    
    st.session_state.messages.append({"role": "assistant", "content": output_message})