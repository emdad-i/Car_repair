import streamlit as st
import requests
import json

# Assuming you have set up OpenAI API key in your environment variables
openai_api_key = st.secrets["OPENAI_API_KEY"]

st.title('Car Repair Assistant')

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to send messages to the LLM and get responses
def send_message(message):
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json',
    }

    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "I am an AI trained to help with car repairs."},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content']

# Chat input for user to type their message
user_input = st.chat_input('Describe your car issue', key="user_input")

# When the user sends a message, add it to the chat history and get a response
if user_input:
    st.session_state.chat_history.append({'message': user_input, 'is_user': True})
    answer = send_message(user_input)
    st.session_state.chat_history.append
