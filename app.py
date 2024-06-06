import streamlit as st
import openai

# Assuming you have set up OpenAI API key in your environment variables
openai_api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = openai_api_key

st.title('Car Repair Assistant')
st.write('Ask me how to repair your car!')

user_input = st.text_input('Describe your car issue')

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "I am an AI trained to help with car repairs."},
                  {"role": "user", "content": user_input}]
    )
    
    st.write(response['choices'][0]['message']['content'])
