import streamlit as st
import pickle

from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain import PromptTemplate
from langchain.llms import CTransformers
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from transformers import AutoModelForCausalLM

from huggingface_hub import ModelHubMixin

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

def load_llm(model_id):
    # Obtener la URL del modelo utilizando el ID del modelo
    model_url = hf_hub_url(model_id)
    
    # Cargar el modelo utilizando la URL
    model_llm = GPT2LMHeadModel.from_pretrained(model_url)
    
    return model_llm

#llm_model_id = "Soondra/llama-model.bin"  
llm_model_id = "TheBloke/Llama-2-7B-Chat-GGML"

# this functions is used for applying the llm model with our document 
def chains_and_response(docs):
    
    llm = load_llm(llm_model_id)
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
