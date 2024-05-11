import streamlit as st
# import pickle
# import timm
import torch

from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain import PromptTemplate
from langchain.llms import CTransformers
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from transformers import AutoModelForCausalLM

# from huggingface_hub import hf_hub_url
# from transformers import GPT2LMHeadModel


# from huggingface_hub import ModelHubMixin

# this function is responsible for splitting the data into smaller chunks and convert the data in document format
def chunks_and_document(txt):
    
    text_splitter = CharacterTextSplitter() # text splitter method by default it has chunk_size = 200 and chunk_overlap = 200
    texts = text_splitter.split_text(txt) # split the text into smaller chunks
    docs = [Document(page_content=t) for t in texts] # convert the splitted chunks into document format
    
    return docs

# Esta función carga el modelo usando el ID del modelo de la biblioteca huggingface
#def load_llm(model_id):
    # Cargamos el modelo desde la biblioteca Hugging Face
   # model_llama = AutoModelForCausalLM.from_pretrained(
      #  model_id
   # )    
    # Instanciamos el modelo LLM
   # llm = CTransformers(
      #  model=model_llama,
      #  model_type="llama",
      #  max_new_tokens=512,
      #  temperature=0.5)
        
   # return llm

# def load_llm():
    # Obtener la URL del modelo utilizando el ID del modelo
    # model_url = hf_hub_url(model_username, model_filename)
    
    # Construir la URL del modelo utilizando la ruta del archivo en GitHub
   #  model_url = f"https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/raw/main/llama-2-7b-chat.ggmlv3.q4_0:8daa9615cce30c259a9555b1cc250d461d1bc69980a274b44d7eda0be78076d8"

   #  model_reloaded = timm.create_model('hf_hub:Soondra/llama-model.bin', pretrained=True)

    # Cargar el modelo utilizando la URL
   #  model_llm = GPT2LMHeadModel.from_pretrained(model_reloaded)
    
   #  return model_llm

#llm_model_id = "Soondra/llama-model.bin"  
#llm_model_id = "TheBloke/Llama-2-7B-Chat-GGML"

# Llamada a la función load_llm con el nombre de usuario y el nombre del archivo del modelo
# llm_model_id = "TheBloke/Llama-2-7B-Chat-GGML"
# model_url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin"
# model_username = "TheBloke"  # Reemplaza esto con el nombre de usuario del autor del modelo
# model_filename = "Llama-2-7B-Chat-GGML"  # Reemplaza esto con el nombre del archivo del modelo

# model_username = "TheBloke/Llama-2-7B-Chat-GGML"
# model_filename = "llama-2-7b-chat.ggmlv3.q4_0.bin"

def load_llm(model_name):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model = torch.load(model_path)
    return model
    
# model_path = "saved_models/llama-model.gzip"
model_name = "TheBloke/Llama-2-7B-Chat-GGML/llama-2-7b-chat.ggmlv3.q4_1.bin"

# this functions is used for applying the llm model with our document 
def chains_and_response(docs):
    
    llm = load_llm(model_name)
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
