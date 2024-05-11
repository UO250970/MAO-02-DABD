import streamlit as st
import pickle

from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain import PromptTemplate
from langchain.llms import CTransformers
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


from huggingface_hub import ModelHubMixin, RepositoryMixin, get_repo_download_url

# this function is responsible for splitting the data into smaller chunks and convert the data in document format
def chunks_and_document(txt):
    
    text_splitter = CharacterTextSplitter() # text splitter method by default it has chunk_size = 200 and chunk_overlap = 200
    texts = text_splitter.split_text(txt) # split the text into smaller chunks
    docs = [Document(page_content=t) for t in texts] # convert the splitted chunks into document format
    
    return docs

import requests

def query(payload, model_id, api_token):
	headers = {"Authorization": f"Bearer {api_token}"}
	API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

model_id = "llama-model"
api_token = "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" # get yours at hf.co/settings/tokens
data = query("The goal of life is [MASK].", model_id, api_token)

# Loading the Llama 2's LLM
def load_llm():
    # We instantiate the callback with a streaming stdout handler
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])   

    # loading the LLM model
    # This open source model can be downloaded from here
    # Their are multiple models available just replace it in place of model and try it.
    model_llama = pickle.load(model_id)
    
    llm = CTransformers(
        model=model_llama,
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.5)
        
    return llm


# Esta función carga el modelo usando el ID del modelo de la biblioteca huggingface
def load_llm(model_id):
    # Cargamos el modelo desde la biblioteca Hugging Face
    model_llama = ModelHubMixin.from_pretrained(model_id)
    
    # Instanciamos el modelo LLM
    llm = CTransformers(
        model=model_llama,
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5)
        
    return llm

# Llamamos a la función load_llm con el ID del modelo
llm_model_id = "Soondra/llama-model"  # Reemplaza esto con el ID de tu modelo
llm = load_llm(llm_model_id)

# this functions is used for applying the llm model with our document 
def chains_and_response(docs):
    
    llm = load_llm()
    chain = load_summarize_chain(llm,chain_type='map_reduce')
    
    return chain.run(docs)
    
# Page title 
st.set_page_config(page_title='🧩 Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.title('Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.markdown('*Lucía Méndez López - lmendez31786@alumnos.uemc.es*')

st.header('🧩 Applicación para resumen de textos 🧩')

col1, col2 = st.columns(2)

# Text input
col1.subheader('Introduce tu texto aquí')
txt_input = col1.text_area('', '', height=300)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=False):
    submitted = st.form_submit_button('Submit')
    #if submitted and openai_api_key.startswith('sk-'):
    if submitted:
        with st.spinner('Calculating...'):
            docs = chunks_and_document(txt_input)
            response = chains_and_response(docs)
            result.append(response)

if len(result):
    col2.subheader('Tu texto resumido aquí')
    col2.info(response)
