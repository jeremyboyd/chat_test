# This is a simple streamlit chat app. Looks super easy to do UI and to deploy
# to web. Need to figure out how to deploy more complicated RAG using streamlit.
# Need to hook up RAG input_message with this app's user_input
# On press of send, if there's user input, run for event in agent_executor.stream part. response will be event["messages"][-1].pretty_print()


import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API
openai_api_key = os.getenv("OPENAI_API_KEY")

def chat_with_assistant(user_input):
    response = OpenAI().chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("Chat Assistant 💬")
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = chat_with_assistant(user_input)
        st.text_area("Assistant:", response, height=200)
