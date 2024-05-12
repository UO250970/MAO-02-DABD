import streamlit as st

from transformers import pipeline

def load_llm(model_name):
    
    summarizer = pipeline("summarization", model=model_name)
    
    return summarizer

def submit():

    with st.sidebar.spinner('Transformando 🤘'):
            summarizer = load_llm(model_name)
            response = summarizer(txt_input, max_length=300, min_length=30, do_sample=True)
            resumen = response[0]['summary_text']
            result.append(resumen)
    
model_name = "Falconsai/text_summarization"

texts = {"":"",
         "A Study in Scarlet":"In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there, I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon. The regiment was stationed in India at the time, and before I could join it, the second Afghan war had broken out. On landing at Bombay, I learned that my corps had advanced through the passes, and was already deep in the enemy's country. I followed, however, with many other officers who were in the same situation as myself, and succeeded in reaching Candahar in safety, where I found my regiment, and at once entered upon my new duties. The campaign brought honours and promotion to many, but for me it had nothing but misfortune and disaster. I was removed from my brigade and attached to the Berkshires, with whom I served at the fatal battle of Maiwand. There I was struck on the shoulder by a Jezail bullet, which shattered the bone and grazed the subclavian artery. I should have fallen into the hands of the murderous Ghazis had it not been for the devotion and courage shown by Murray, my orderly, who threw me across a pack-horse, and succeeded in bringing me safely to the British lines. Worn with pain, and weak from the prolonged hardships which I had undergone, I was removed, with a great train of wounded sufferers, to the base hospital at Peshawar. Here I rallied, and had already improved so far as to be able to walk about the wards, and even to bask a little upon the verandah, when I was struck down by enteric fever, that curse of our Indian possessions.",
         "Twenty Thousand Leagues under the Sea":"Hola"}
         
# Page title 
st.set_page_config(page_title='🧩 Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.title('Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.markdown('*Lucía Méndez López - lmendez31786@alumnos.uemc.es*')

st.sidebar.divider()

option = st.sidebar.selectbox(
    "Textos de referencia para resumir",
    ("", "A Study in Scarlet", "Twenty Thousand Leagues under the Sea"))

st.header('🧩 Applicación para resumen de textos 🧩')

col1, col2 = st.columns(2)

# Text input
col1.subheader('Introduce tu texto aquí')
txt_input = col1.text_area('', texts[option], height=400)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=False):
    submitted = st.form_submit_button('Submit')
    #if submitted and openai_api_key.startswith('sk-'):
    if submitted:
        submit()

if len(result):
    col2.subheader('Tu texto resumido aquí')
    col2.info(result[0])
