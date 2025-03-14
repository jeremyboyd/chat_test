# Deployed this app to streamlit, available at https://chattest-aefvm8zpygd8ehxnlqrmzx.streamlit.app/ Right now there's no security on it so anyone could use it and I'd be charged by OpenAI.

# Need to use a requirements.txt file to specify required python packages, or else app will fail to deploy on stramlit.

# This is a simple streamlit chat app. Easy to deploy to streamlit cloud. Some tips: (1) push project to GitHub repo; streamlit reads code from there (2) don't push .env file; streamlit has a text box during setup where you can paste contents of .env to keep secret, (3) create and push a requirements.txt file to specify python packages that streamlit will have to load, (4) easier to deploy to streamlit if the GitHub repo is public; supposedly it's possible to do for a private repo, but I couldn't get it to work.

# Need to figure out how to deploy more complicated RAG using streamlit.
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
