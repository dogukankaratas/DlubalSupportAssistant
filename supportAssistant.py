import openai
import streamlit as st
from streamlit_chat import message

openai.api_key = st.secrets["openai_key"]

def generate_response(prompt):
    completions = openai.Completion.create(
        model="davinci:ft-dlubal-software-gmbh-2023-06-02-11-03-33",
        prompt=prompt,
        max_tokens=250,
        temperature=0,
        frequency_penalty = 1.0,
        stop=["END"]
    )

    message = completions.choices[0].text
    return message

col1, col2 = st.columns([1,4])
with col1:
    st.image("assets/dlubalLogo.png", width=100)
with col2:
    st.title("Dlubal AI Support Assistant")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("Ask something to the AI Support Asisstant: ","What is RFEM?", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')