import streamlit as st
import requests
import json

# Assuming you have set up OpenAI API key in your environment variables
openai_api_key = st.secrets["OPENAI_API_KEY"]

st.title('Car Repair Assistant')

# Create a container for the chat messages
chat_container = st.beta_container()

user_input = st.text_input('Describe your car issue', key="user_input")

if user_input:
    # Send the user message to the API
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json',
    }

    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "I am an AI trained to help with car repairs."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))
    response_json = response.json()
    answer = response_json['choices'][0]['message']['content']

    # Display the conversation in the chat container
    with chat_container:
        st.text_area("Conversation", value=f"You: {user_input}\nAI: {answer}", height=300, disabled=True)
