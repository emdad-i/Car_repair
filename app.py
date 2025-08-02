import streamlit as st
import requests
import json

# Assuming you have set up OpenAI API key in your environment variables
openai_api_key = st.secrets["OPENAI_API_KEY"]

st.title('Car Repair Assistant')
st.write('Ask me how to repair your car!')

user_input = st.text_input('Describe your car issue')

if user_input:
        headers = {
            'Authorization': f'Bearer {openai_api_key}',
            'Content-Type': 'application/json',
        }

        data = {
            'model': 'omni-moderation-latest',
            'input': user_input
        }

        mod_response = requests.post('https://api.openai.com/v1/moderations', headers=headers, data=json.dumps(data))

        if bool(mod_response.json()['results'][0]['flagged']) == False:
            headers = {
                'Authorization': f'Bearer {openai_api_key}',
                'Content-Type': 'application/json',
            }

            data = {
                "model": "gpt-4o",
                "messages": [
                    {"role": "system", "content": "I am an AI trained to help with car repairs."},
                    {"role": "user", "content": user_input}
                ]
            }

            response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))
            response_json = response.json()
            
            st.write(response_json['choices'][0]['message']['content'])
        else:
              st.write('Moderation Failed')
              st.write(mod_response.json())
