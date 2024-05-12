import streamlit as st

from transformers import pipeline

def load_llm(model_name):
    
    summarizer = pipeline("summarization", model=model_name)
    
    return summarizer
   
model_name = "Falconsai/text_summarization"

# Page title 
st.set_page_config(page_title='🧩 Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.title('Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.markdown('*Lucía Méndez López - lmendez31786@alumnos.uemc.es*')

st.header('🧩 Applicación para resumen de textos 🧩')

col1, col2 = st.columns(2)

# Text input
col1.subheader('Introduce tu texto aquí')
txt_input = col1.text_area('', '', height=400)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=False):
    submitted = st.form_submit_button('Submit')
    #if submitted and openai_api_key.startswith('sk-'):
    if submitted:
        with st.spinner('Transformando 🤘'):
            summarizer = load_llm(model_name)
            response = summarizer(txt_input, max_length=300, min_length=30, do_sample=True)
            resumen = response[0]['summary_text']
            result.append(resumen)

if len(result):
    col2.subheader('Tu texto resumido aquí')
    col2.info(result[0])
