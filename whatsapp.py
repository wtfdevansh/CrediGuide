import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv


from card_agent.recommender import Recommender as CardTools
from llm_agent import AgentCreator

load_dotenv()
app = Flask(__name__)


try:
    card_tools_instance = CardTools()
    agent_creator_instance = AgentCreator(card_tools_instance)
    agent_executor = agent_creator_instance.create_agent_executor()
    print("Agent initialized successfully.")
except Exception as e:
    print(f"Error initializing agent: {e}")
    agent_executor = None


chat_sessions = {}


@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    """Receives incoming messages from Twilio and sends back a response."""
    if not agent_executor:
        return "Agent not available.", 500

   
    sender_id = request.values.get('From', '')
    incoming_msg = request.values.get('Body', '').lower()

    print(f"Received message from {sender_id}: {incoming_msg}")

    if sender_id not in chat_sessions:
        chat_sessions[sender_id] = []
    
    chat_history = chat_sessions[sender_id]

  
    response = agent_executor.invoke({
        "input": incoming_msg,
        "chat_history": chat_history
    })
    
    output_message = response["output"]


    chat_history.append({"role": "user", "content": incoming_msg})
    chat_history.append({"role": "assistant", "content": output_message})
  
    if len(chat_history) > 10:
        chat_sessions[sender_id] = chat_history[-10:]


    twilio_response = MessagingResponse()
    twilio_response.message(output_message)

    return str(twilio_response)


if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)